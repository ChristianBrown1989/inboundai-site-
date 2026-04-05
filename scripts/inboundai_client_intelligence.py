#!/usr/bin/env python3
"""
InboundAI — Client Intelligence Engine
Reads a client's Google Sheets call log, analyzes patterns with Claude,
and generates a plain-English insight report.

Run monthly (or weekly for high-volume clients).
Output: Markdown report saved to /root/Desktop/CBrownOS/System/inboundai-client-insights-[client].md

Usage:
  python3 inboundai_client_intelligence.py --sheet-id SHEET_ID --client-name "Jacksonville Water Pros"
"""

import os
import sys
import json
import argparse
import requests
from datetime import datetime, timedelta
from collections import defaultdict, Counter
import anthropic

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
GOOGLE_SHEETS_API_KEY = os.environ.get("GOOGLE_SHEETS_API_KEY")

OUTPUT_DIR = "/root/Desktop/CBrownOS/System/"

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def fetch_sheet_data(sheet_id, range_name="Sheet1!A:L"):
    """Fetch call log data from Google Sheets via API."""
    url = f"https://sheets.googleapis.com/v4/spreadsheets/{sheet_id}/values/{range_name}"
    params = {"key": GOOGLE_SHEETS_API_KEY}
    try:
        r = requests.get(url, params=params, timeout=15)
        r.raise_for_status()
        return r.json().get("values", [])
    except Exception as e:
        log(f"Error fetching sheet: {e}")
        return []

def parse_call_log(rows):
    """Parse raw sheet rows into structured call records."""
    if not rows or len(rows) < 2:
        return []
    headers = [h.lower().replace(" ", "_") for h in rows[0]]
    records = []
    for row in rows[1:]:
        if not row:
            continue
        record = {}
        for i, h in enumerate(headers):
            record[h] = row[i] if i < len(row) else ""
        records.append(record)
    return records

def analyze_patterns(calls):
    """Extract statistical patterns from call records."""
    if not calls:
        return {}

    total = len(calls)
    dispositions = Counter(c.get("disposition", "unknown") for c in calls)
    emergencies = sum(1 for c in calls if str(c.get("was_emergency", "")).lower() in ("true", "1", "yes"))

    # Parse call hours from timestamp
    hour_buckets = defaultdict(list)
    for c in calls:
        ts = c.get("timestamp", "")
        try:
            dt = datetime.fromisoformat(ts.replace("Z", "+00:00"))
            hour_buckets[dt.hour].append(c.get("disposition", ""))
        except Exception:
            pass

    # Identify low-converting time windows
    window_analysis = {}
    for hour, disps in hour_buckets.items():
        booked = sum(1 for d in disps if "estimate" in d.lower() or "emergency" in d.lower() or "service" in d.lower())
        rate = booked / len(disps) if disps else 0
        window_analysis[hour] = {"calls": len(disps), "booked": booked, "rate": rate}

    # Find worst windows
    worst_windows = sorted(
        [(h, v) for h, v in window_analysis.items() if v["calls"] >= 3],
        key=lambda x: x[1]["rate"]
    )[:3]

    # Duration parsing
    durations = []
    for c in calls:
        dur = c.get("call_duration", "")
        try:
            if "m" in dur:
                parts = dur.replace("s", "").split("m")
                seconds = int(parts[0]) * 60 + int(parts[1].strip())
                durations.append(seconds)
            elif dur.isdigit():
                durations.append(int(dur))
        except Exception:
            pass

    avg_duration = sum(durations) / len(durations) if durations else 0

    return {
        "total_calls": total,
        "dispositions": dict(dispositions),
        "emergency_count": emergencies,
        "emergency_rate": emergencies / total if total else 0,
        "worst_time_windows": [
            {"hour": f"{h}:00", "calls": v["calls"], "conversion_rate": f"{v['rate']:.0%}"}
            for h, v in worst_windows
        ],
        "avg_call_duration_seconds": round(avg_duration),
        "top_disposition": dispositions.most_common(1)[0][0] if dispositions else "unknown",
        "hour_breakdown": {f"{h}:00": v for h, v in sorted(window_analysis.items())}
    }

def generate_client_report(client_name, calls, patterns, client_industry="HVAC"):
    """Use Claude to generate plain-English insights report."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # Build sample summaries for Claude (last 20 calls)
    recent_summaries = []
    for c in calls[-20:]:
        s = c.get("summary", "")
        if s and len(s) > 20:
            recent_summaries.append(s[:300])

    prompt = f"""You are analyzing call log data for InboundAI client: {client_name} ({client_industry})

CALL PATTERNS (last {patterns.get('total_calls', 0)} calls):
{json.dumps(patterns, indent=2)}

RECENT CALL SUMMARIES (sample):
{chr(10).join(f'- {s}' for s in recent_summaries[:10])}

Generate a plain-English monthly insights report for the business owner.
The owner is a hands-on contractor — not a marketer. Write like you're texting a friend who runs a small business.

Structure your report exactly as:

## What Your AI Did This Month
[2-3 sentences, key numbers — calls handled, emergencies flagged, types of calls]

## Where You're Winning
[2-3 specific things going well, based on the data]

## Where Revenue Is Leaking
[Identify 1-3 specific choke points with exact numbers. Be specific: "Your 6-9pm calls converted at X% vs Y% average — that's approximately Z jobs/month leaking through that window."]

## What We're Fixing Next Month
[2-3 specific improvements we're making based on the data]

## Quick Numbers
[Bullet list: total calls, emergency rate, most common call type, avg call duration]

Keep the whole report under 350 words. No jargon. Write like a trusted advisor, not a software company."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=800,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        log(f"Claude error: {e}")
        return f"Error generating report: {e}"

def save_report(client_name, report_text, patterns):
    """Save report as markdown file."""
    slug = client_name.lower().replace(" ", "-").replace("/", "-")
    filename = f"inboundai-client-insights-{slug}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    date_str = datetime.now().strftime("%Y-%m-%d")
    full_report = f"""# InboundAI — Client Insights: {client_name}
> Generated: {date_str}
> Total calls analyzed: {patterns.get('total_calls', 0)}

---

{report_text}

---

## Raw Pattern Data
```json
{json.dumps(patterns, indent=2)}
```
"""
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(full_report)
        log(f"Report saved: {filepath}")
        return filepath
    except Exception as e:
        log(f"Error saving report: {e}")
        print(full_report)
        return None

def main():
    parser = argparse.ArgumentParser(description="InboundAI Client Intelligence Engine")
    parser.add_argument("--sheet-id", required=True, help="Google Sheets ID")
    parser.add_argument("--client-name", required=True, help="Client business name")
    parser.add_argument("--industry", default="HVAC", choices=["HVAC", "Water Restoration"], help="Client industry")
    args = parser.parse_args()

    if not ANTHROPIC_API_KEY:
        log("ERROR: ANTHROPIC_API_KEY not set")
        sys.exit(1)

    log(f"Starting client intelligence run for: {args.client_name}")

    # Fetch data
    log("Fetching call log from Google Sheets...")
    rows = fetch_sheet_data(args.sheet_id)
    if not rows:
        log("No data found in sheet")
        sys.exit(1)

    # Parse
    calls = parse_call_log(rows)
    log(f"Parsed {len(calls)} call records")

    # Analyze
    patterns = analyze_patterns(calls)
    log(f"Pattern analysis complete — {patterns.get('total_calls', 0)} calls, {patterns.get('emergency_count', 0)} emergencies")

    # Generate report
    log("Generating Claude insights report...")
    report = generate_client_report(args.client_name, calls, patterns, args.industry)

    # Save
    save_report(args.client_name, report, patterns)
    log("Done.")

if __name__ == "__main__":
    main()
