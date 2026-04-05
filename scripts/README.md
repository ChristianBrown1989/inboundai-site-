# InboundAI Intelligence Scripts

## Server: Hetzner 65.21.61.61 — /root/scripts/

---

## 1. inboundai_client_intelligence.py
**What:** Analyzes a client's Google Sheets call log, finds patterns, generates plain-English monthly report.
**When:** Monthly (or weekly for high-volume clients)
**Output:** `/root/Desktop/CBrownOS/System/inboundai-client-insights-[client].md`

**Run:**
```bash
export ANTHROPIC_API_KEY="your-key"
export GOOGLE_SHEETS_API_KEY="your-key"
python3 inboundai_client_intelligence.py \
  --sheet-id "GOOGLE_SHEET_ID_HERE" \
  --client-name "Jacksonville Water Pros" \
  --industry "Water Restoration"
```

**What it produces:**
- What the AI did this month (call counts, emergency rate)
- Where revenue is leaking (specific time windows, conversion rates)
- Specific choke points with numbers
- Recommendations for next month

---

## 2. inboundai_market_intelligence.py
**What:** Scrapes all 6 competitors weekly, mines Reddit for pain language, detects changes, generates competitive brief.
**When:** Every Monday (cron)
**Output:**
- `/root/Desktop/CBrownOS/System/inboundai-market-intel-[date].md`
- `/root/Desktop/CBrownOS/System/inboundai-market-intel-latest.md`
- `/root/inboundai-market-snapshot.json` (for week-over-week diff)

**Cron setup:**
```bash
0 7 * * 1 /usr/bin/python3 /root/scripts/inboundai_market_intelligence.py >> /root/logs/market_intel.log 2>&1
```

**What it produces:**
- Competitor change alerts (HIGH/MEDIUM/LOW urgency)
- Current competitor positioning summary
- Real contractor pain language from Reddit
- Market gaps you can own this week
- Script/copy update recommendations

---

## Intelligence Loop — How It Gets Smarter

```
Week 1: First run — snapshot saved, no changes to compare yet
Week 2: Diff against Week 1 — first change detection
Month 1: First client intelligence report — call pattern baseline established
Month 3: Choke point detection becomes meaningful (enough data)
Month 6: Industry benchmarking possible (multiple clients)
Year 1: Predictive recommendations (seasonal, market-driven)
```

---

## Dependencies
```bash
pip install anthropic requests beautifulsoup4
```

## Environment Variables
```bash
export ANTHROPIC_API_KEY="org_..."
export GOOGLE_SHEETS_API_KEY="..."  # For client intelligence only
```
