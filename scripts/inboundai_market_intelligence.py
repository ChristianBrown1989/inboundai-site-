#!/usr/bin/env python3
"""
InboundAI — Market Intelligence Engine
Runs weekly. Monitors competitors, mines Reddit/reviews for pain language,
scores market gaps, and generates a competitive brief for InboundAI.

Gets smarter over time — compares against previous snapshots to detect changes.

Cron: 0 7 * * 1 /usr/bin/python3 /root/scripts/inboundai_market_intelligence.py >> /root/logs/market_intel.log 2>&1

Output:
  /root/Desktop/CBrownOS/System/inboundai-market-intel-[date].md
  /root/inboundai-market-snapshot.json  (for diff comparison next week)
"""

import os
import sys
import json
import time
import requests
import hashlib
from datetime import datetime
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import anthropic

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
OUTPUT_DIR = "/root/Desktop/CBrownOS/System/"
SNAPSHOT_FILE = "/root/inboundai-market-snapshot.json"

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

COMPETITORS = [
    {"name": "HVAC Frontdesk", "url": "https://hvacfrontdesk.com", "priority": "high"},
    {"name": "CallOS", "url": "https://callos.ai", "priority": "high"},
    {"name": "AirFlow AI", "url": "https://airflowaiagency.com", "priority": "medium"},
    {"name": "Breezy", "url": "https://getbreezy.app", "priority": "medium"},
    {"name": "Dial Bridge", "url": "https://dialbridge.ai", "priority": "medium"},
    {"name": "HiThere AI", "url": "https://hithereai.com", "priority": "low"},
]

REDDIT_SEARCHES = [
    "HVAC missed calls answering service",
    "water damage restoration answering service",
    "HVAC receptionist AI",
    "contractor answering service review",
    "HVAC after hours calls problem",
    "water restoration emergency answering",
]

def log(msg):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")

def safe_get(url, timeout=15):
    try:
        r = requests.get(url, headers=HEADERS, timeout=timeout)
        return r.text if r.ok else None
    except Exception as e:
        log(f"  GET failed {url}: {e}")
        return None

def scrape_competitor(comp):
    """Scrape competitor homepage for key content."""
    log(f"Scraping {comp['name']}...")
    html = safe_get(comp["url"])
    if not html:
        return {"name": comp["name"], "error": "failed to fetch"}

    soup = BeautifulSoup(html, "html.parser")

    # Extract meaningful content
    title = soup.find("title")
    title_text = title.get_text(strip=True) if title else ""

    # Get all headings
    headings = [h.get_text(strip=True) for h in soup.find_all(["h1", "h2", "h3"])[:10]]

    # Get price mentions
    body_text = soup.get_text(separator=" ", strip=True)[:4000]
    price_signals = []
    import re
    prices = re.findall(r'\$[\d,]+(?:/mo(?:nth)?)?', body_text)
    price_signals = list(set(prices))[:5]

    # Hash for change detection
    content_hash = hashlib.md5(body_text[:2000].encode()).hexdigest()

    return {
        "name": comp["name"],
        "url": comp["url"],
        "title": title_text,
        "headings": headings,
        "price_signals": price_signals,
        "body_excerpt": body_text[:1500],
        "content_hash": content_hash,
        "scraped_at": datetime.now().isoformat(),
    }

def search_reddit_pain(query):
    """Search DuckDuckGo for Reddit discussions on a topic."""
    encoded = quote_plus(f"site:reddit.com {query}")
    url = f"https://html.duckduckgo.com/html/?q={encoded}"
    html = safe_get(url)
    if not html:
        return []

    soup = BeautifulSoup(html, "html.parser")
    results = []
    for result in soup.select(".result")[:5]:
        title = result.select_one(".result__title")
        snippet = result.select_one(".result__snippet")
        if title and snippet:
            results.append({
                "title": title.get_text(strip=True),
                "snippet": snippet.get_text(strip=True)
            })
    return results

def detect_competitor_changes(current_data, snapshot):
    """Compare current scrape against last snapshot to find changes."""
    changes = []
    for comp in current_data:
        name = comp.get("name")
        prev = next((s for s in snapshot.get("competitors", []) if s.get("name") == name), None)
        if not prev:
            changes.append({"competitor": name, "type": "new_data", "detail": "First time scraped"})
            continue

        # Hash comparison
        if comp.get("content_hash") != prev.get("content_hash"):
            # Find what changed
            old_headings = set(prev.get("headings", []))
            new_headings = set(comp.get("headings", []))
            added = new_headings - old_headings
            removed = old_headings - new_headings

            old_prices = set(prev.get("price_signals", []))
            new_prices = set(comp.get("price_signals", []))
            price_changes = (new_prices - old_prices) | (old_prices - new_prices)

            if price_changes:
                changes.append({"competitor": name, "type": "PRICING_CHANGE", "detail": f"Prices changed: {price_changes}", "urgency": "HIGH"})
            if added:
                changes.append({"competitor": name, "type": "new_messaging", "detail": f"New headings: {list(added)[:3]}", "urgency": "MEDIUM"})
            if removed:
                changes.append({"competitor": name, "type": "removed_messaging", "detail": f"Removed: {list(removed)[:3]}", "urgency": "LOW"})

            if not price_changes and not added and not removed:
                changes.append({"competitor": name, "type": "content_change", "detail": "Page content changed — review recommended", "urgency": "LOW"})

    return changes

def generate_market_brief(competitor_data, reddit_results, changes, snapshot_date):
    """Use Claude to generate the weekly market intelligence brief."""
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # Summarize competitor headings
    comp_summary = []
    for c in competitor_data:
        if "error" not in c:
            comp_summary.append(f"**{c['name']}** ({c['url']})\n  Headings: {c['headings'][:5]}\n  Prices found: {c.get('price_signals', 'none')}")

    reddit_summary = []
    for topic, results in reddit_results.items():
        for r in results[:2]:
            reddit_summary.append(f"- [{topic}] {r['title']}: {r['snippet'][:200]}")

    changes_summary = json.dumps(changes, indent=2) if changes else "No significant changes detected."

    prompt = f"""You are the market intelligence analyst for InboundAI — a done-for-you AI receptionist service for HVAC and water restoration owners.

INBOUNDAI POSITIONING:
- Done-for-you service (not SaaS), $750/month, 20 clients max
- Targets: 1-9 person HVAC and water restoration shops, owner-operated
- Key differentiators: custom-built, books job on call, instant owner SMS, weekly revenue report, Spanish language, direct human contact, competitor monitoring included
- Only visible competitor price: HVAC Frontdesk at $299/month

COMPETITOR DATA THIS WEEK:
{chr(10).join(comp_summary)}

DETECTED CHANGES SINCE LAST SCAN:
{changes_summary}

REDDIT / MARKET PAIN (raw):
{chr(10).join(reddit_summary[:15])}

Generate a weekly market intelligence brief for Christian (the owner of InboundAI).
Write like a trusted advisor texting a friend — direct, useful, no fluff.

Structure:
## Market Brief — Week of {datetime.now().strftime('%B %d, %Y')}

### ⚠️ Changes to Act On
[Only include if there are real changes. List competitor changes with urgency level and recommended response. If none, say "No urgent changes this week."]

### 📍 Competitor Positioning Update
[2-3 sentences on how competitors are positioning themselves this week. What language are they using? Any new features mentioned?]

### 💬 What Contractors Are Complaining About
[3-5 bullets of real pain language from Reddit/forums. Quote where possible. This is what to use in ads and outreach.]

### 🎯 Market Gaps We Can Own This Week
[2-3 specific gaps that are NOT being addressed by any competitor right now. Score each: HIGH/MEDIUM/LOW opportunity.]

### 📝 Recommended Script/Copy Updates
[1-2 specific suggestions for updating InboundAI's sales scripts or website copy based on this week's intel.]

Keep it under 450 words. Be specific. If you don't have enough data on something, say so rather than guessing."""

    try:
        message = client.messages.create(
            model="claude-sonnet-4-6",
            max_tokens=900,
            messages=[{"role": "user", "content": prompt}]
        )
        return message.content[0].text
    except Exception as e:
        log(f"Claude error: {e}")
        return f"Error generating brief: {e}"

def save_snapshot(competitor_data):
    """Save current scrape as snapshot for next week's diff."""
    snapshot = {
        "scraped_at": datetime.now().isoformat(),
        "competitors": competitor_data,
    }
    try:
        with open(SNAPSHOT_FILE, "w") as f:
            json.dump(snapshot, f, indent=2)
        log(f"Snapshot saved: {SNAPSHOT_FILE}")
    except Exception as e:
        log(f"Error saving snapshot: {e}")

def load_snapshot():
    """Load previous week's snapshot."""
    try:
        with open(SNAPSHOT_FILE) as f:
            return json.load(f)
    except Exception:
        return {"competitors": [], "scraped_at": None}

def save_report(brief_text, changes):
    """Save market intel report as markdown."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"inboundai-market-intel-{date_str}.md"
    filepath = os.path.join(OUTPUT_DIR, filename)

    urgent = [c for c in changes if c.get("urgency") == "HIGH"]
    urgent_banner = ""
    if urgent:
        urgent_banner = f"\n> ⚠️ **{len(urgent)} HIGH URGENCY item(s) detected — act this week**\n"

    full_report = f"""# InboundAI — Market Intelligence Brief
> Generated: {date_str}
{urgent_banner}
---

{brief_text}

---

## Raw Change Log
```json
{json.dumps(changes, indent=2)}
```
"""
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(filepath, "w") as f:
            f.write(full_report)
        log(f"Market brief saved: {filepath}")

        # Also overwrite the "latest" file for easy access
        latest_path = os.path.join(OUTPUT_DIR, "inboundai-market-intel-latest.md")
        with open(latest_path, "w") as f:
            f.write(full_report)
        log(f"Latest brief updated: {latest_path}")
    except Exception as e:
        log(f"Error saving report: {e}")
        print(full_report)

def main():
    if not ANTHROPIC_API_KEY:
        log("ERROR: ANTHROPIC_API_KEY not set")
        sys.exit(1)

    log("=== InboundAI Market Intelligence Engine ===")
    date_str = datetime.now().strftime("%Y-%m-%d")

    # Load previous snapshot
    snapshot = load_snapshot()
    if snapshot.get("scraped_at"):
        log(f"Previous snapshot: {snapshot['scraped_at']}")
    else:
        log("No previous snapshot — first run")

    # Scrape competitors
    competitor_data = []
    for comp in COMPETITORS:
        data = scrape_competitor(comp)
        competitor_data.append(data)
        time.sleep(2)  # Polite delay

    # Detect changes
    log("Comparing against previous snapshot...")
    changes = detect_competitor_changes(competitor_data, snapshot)
    log(f"Changes detected: {len(changes)}")
    for c in changes:
        log(f"  [{c.get('urgency', 'INFO')}] {c['competitor']}: {c['type']}")

    # Reddit pain mining
    log("Mining Reddit for contractor pain language...")
    reddit_results = {}
    for query in REDDIT_SEARCHES[:4]:  # Limit to 4 queries
        log(f"  Searching: {query}")
        results = search_reddit_pain(query)
        if results:
            reddit_results[query] = results
        time.sleep(1.5)

    # Generate brief
    log("Generating market intelligence brief with Claude...")
    brief = generate_market_brief(competitor_data, reddit_results, changes, snapshot.get("scraped_at"))

    # Save everything
    save_snapshot(competitor_data)
    save_report(brief, changes)

    log("=== Market Intelligence run complete ===")
    if changes:
        log(f"Summary: {len([c for c in changes if c.get('urgency') == 'HIGH'])} HIGH, {len([c for c in changes if c.get('urgency') == 'MEDIUM'])} MEDIUM, {len([c for c in changes if c.get('urgency') == 'LOW'])} LOW priority changes")

if __name__ == "__main__":
    main()
