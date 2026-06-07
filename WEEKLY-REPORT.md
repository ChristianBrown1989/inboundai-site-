# Weekly Master Report — 2026-06-07

---

## Site Audit Results

### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

**Pages:** 10 public HTML + thank-you.html = 11 files

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 11 pages |
| Meta description | ✅ Pass | Present on all public pages; thank-you.html omitted (acceptable) |
| Meta keywords | ❌ Missing | No `<meta name="keywords">` on any page |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url — **CARRY-OVER WK 3** |
| sitemap.xml | ✅ Pass | 10 URLs — matches all public pages exactly |
| robots.txt | ✅ Pass | `Allow: /` — not blocking crawlers; references sitemap |
| LocalBusiness schema | ✅ Pass | index.html: `"@type": ["LocalBusiness","EmergencyService"]` + FAQPage + AggregateRating |
| Page speed | ✅ Pass | Zero `<img>` tags, no external/blocking JS, system fonts only |
| Broken local links | ✅ Pass | All href/src targets (incl. CSS) resolve to files in repo |

**Action items (carry-over):** Add OG tags (og:title, og:description, og:image, og:url) to all 10 public pages.

---

### Nashville Water Damage (nashvillewaterdamagepros.com)

**Pages:** 14 public HTML + thank-you.html = 15 files

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | All pages |
| Meta description | ✅ Pass | All public pages |
| Meta keywords | ❌ Missing | No keywords meta on any page |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER WK 3** |
| sitemap.xml | ⚠️ Incomplete | Still only 10 URLs listed; same 4 published pages missing — **CARRY-OVER WK 3, STILL NOT FIXED** |
| robots.txt | ✅ Pass | Allows all crawlers; references sitemap |
| EmergencyService schema | ✅ Pass | index.html `"@type":"EmergencyService"` + FAQPage + AggregateRating |
| Page speed | ✅ Pass | No images, no external/blocking JS |
| Broken local links | ✅ Pass | None found |

**Sitemap gaps — verified again, unchanged from last 2 weeks:**
- `/commercial-water-damage-nashville`
- `/hardwood-floor-water-damage-nashville`
- `/insurance-claim-water-damage-nashville`
- `/water-damage-restoration-cost-nashville`

**Action items:** Update sitemap.xml to add the 4 missing URLs (this is now a 5-minute fix that has gone undone for 3 straight weeks); add OG tags to all pages.

---

### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

**Pages:** 9 public HTML + thank-you.html = 10 files

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | All pages |
| Meta description | ✅ Pass | All public pages |
| Meta keywords | ❌ Missing | No keywords meta on any page |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER WK 3** |
| sitemap.xml | ✅ Pass | 9 URLs — matches all public pages |
| robots.txt | ✅ Pass | Allows all crawlers; references sitemap |
| EmergencyService schema | ✅ Pass | index.html + FAQPage |
| Page speed | ✅ Pass | No images, no external/blocking JS |
| Broken local links | ✅ Pass | None found |

**🚨🚨 CRITICAL — Nashville/Tennessee brand contamination — STILL LIVE, 3 WEEKS UNFIXED:**

Re-verified line-by-line; all 7 instances are still present, byte-for-byte identical to week 1:

| File:Line | Wrong Text |
|-----------|-----------|
| index.html:138 | "⚡ 60-Minute Response · **Nashville** & Surrounding Areas" |
| index.html:230 | "Why **Nashville** Trusts Us" |
| index.html:232 | "treat every **Nashville** homeowner the way we'd want our own family treated" |
| index.html:260 | "approved by every major insurance carrier in **Tennessee**" |
| index.html:274 | "We're a **Nashville** company. We live here too." |
| index.html:321 | "Real **Nashville** Homeowners" |
| emergency.html:48 | "24/7 Emergency Water Damage … Response in **Nashville**" |

**🆕 Also still broken — invalid NAP microdata (index.html:112):**
```html
<!-- Current (still broken): -->
<span itemprop="addressLocality": "Cincinnati</span>
<!-- Should be: -->
<span itemprop="addressLocality">Cincinnati</span>
```

**Action items:** Fix all 7 Nashville/Tennessee references in index.html + emergency.html; fix the broken `itemprop` attribute. Total effort ~20 minutes — this has now sat unfixed for 3 consecutive audits while the site is live and taking traffic.

---

### HAKD (hakd.app) — Next.js on Vercel

**Pages:** Static: `/`, `/about`, `/articles`, `/directory` + dynamic: `articles/[slug]`, `articles/category/[category]`, `directory/[slug]`, `directory/category/[category]`, `directory/city/[city]`, `directory/city/[city]/[category]`

| Check | Status | Notes |
|-------|--------|-------|
| Title tags | ✅ Pass | root layout metadata + per-page generateMetadata |
| Meta description | ✅ Pass | layout.js + per-page overrides |
| OG tags | ⚠️ Partial | og:title/description/url/siteName present in layout.js; **og:image still missing — `/public/og-image.png` does not exist** — **CARRY-OVER WK 3** |
| sitemap | ✅ Pass | Dynamic `app/sitemap.js`: static + articles + listings + dir categories + city × category combos |
| robots | ✅ Pass | Dynamic `app/robots.js` with AI crawler allowlist |
| Schema | ✅ Pass | WebSite + Person in layout.js; Article + BreadcrumbList on articles |
| Page speed | ✅ Pass | SSG, no render-blocking resources |
| Broken internal links | ✅ Pass | All internal `Link`/`href` targets (`/`, `/about`, `/articles`, `/directory`, category routes) resolve to real routes |

**🚨🚨 SECURITY — ConvertKit API key still hardcoded in source — 3 WEEKS UNFIXED, RE-ESCALATING:**
`/app/api/subscribe/route.js:16` — `api_key: 'unwsbthP07XOrlhfGdfrkg'` is committed in plaintext to the **public** git repository (and has been in git history for 3+ weeks now).
Fix steps (unchanged from week 1):
1. ConvertKit → Settings → Advanced → API → **Regenerate API Key** (the old one must be rotated regardless of code changes — it's already exposed in history)
2. Add `CONVERTKIT_API_KEY` to Vercel project environment variables
3. Replace the hardcoded string with `process.env.CONVERTKIT_API_KEY`
4. Redeploy

This is the single most actionable security item across all 5 properties and has now been flagged in three consecutive reports without action.

**External / affiliate link audit — unchanged from last week:**

| URL | Location | Risk |
|-----|---------|------|
| `https://deluxe-moxie-d4016f.netlify.app` | Announce bar, nav CTA, hero, EMM banner, about strip, footer — **6+ placements** | ⚠️ **HIGH** — random Netlify subdomain; primary revenue CTA chain breaks site-wide if the project is deleted/renamed |
| `https://coach.everfit.io/package/GL583637` | Footer — Monthly Coaching $250/mo | ✅ Active SaaS platform |
| `https://coach.everfit.io/package/KX912574` | Footer — Monthly Training $80/mo | ✅ Active SaaS platform |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Footer — Discovery Call | ✅ Standard Calendly link |

**Action items:** (1) Rotate ConvertKit key NOW — week 3 escalation, this cannot wait another cycle; (2) add `/public/og-image.png` (1200×630) and reference it in `layout.js` `openGraph.images`; (3) migrate EMM Assessment off the random Netlify subdomain to a custom domain/path.

---

### InboundAI (inboundai.app) — Static HTML on Cloudflare Workers/Pages

**Pages:** 1 (single-page — index.html, 57KB)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present |
| Meta keywords | ❌ Missing | |
| OG tags | ❌ Missing | No og:title, og:description, og:image, og:url — **CARRY-OVER WK 3** |
| sitemap.xml | ❌ Missing | File not in repo — **CARRY-OVER WK 3** |
| robots.txt | ❌ Missing | File not in repo — **CARRY-OVER WK 3** |
| JSON-LD schema | ❌ Missing | No SoftwareApplication or Organization schema — **CARRY-OVER WK 3** |
| Page speed | ✅ Pass | Inline CSS, zero `<img>` tags, emoji-only visuals |
| Broken local links | ⚠️ 2 found, unchanged | `href="#"` on nav logo (line 538) and on "Terms of Service" (line 1118) — no `/terms.html` exists in repo |

**Pipeline scripts present:** `scripts/inboundai_client_intelligence.py` and `scripts/inboundai_market_intelligence.py` (Python, run on Hetzner server `65.21.61.61` per `scripts/README.md`). Market intelligence is cron'd for **every Monday at 7am** — its output (`inboundai-market-intel-latest.md`) is the actual revenue-driving deliverable; the marketing site below is just the funnel front door.

**Action items (all carry-over, now 3 weeks old):** Create robots.txt and sitemap.xml; add OG tags; add SoftwareApplication + Organization JSON-LD schema; fix the 2 dead `href="#"` links (point logo to `/`, and either build `/terms.html` or remove the link).

---

## Deploy Queue

`git log --since='7 days ago' --oneline` results (run 2026-06-07):

| Repo | New Commits (7 days) | Needs Deploy? |
|------|---------------------|---------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 — `5215569 chore: weekly master report 2026-05-31` (report file only) | No |

**No code deployments required.** All 5 sites are still running the same code as 3 weeks ago — `jacksonville-water-damage`, `nashville-water-damage`, and `cincinnati-water-damage` have had zero commits since 2026-03-24/25; `hakd-site` since 2026-03-25.

> ⚠️ **Third consecutive week with zero substantive commits across all 5 properties.** Every carry-over item below (Cincinnati brand contamination, HAKD API key, Nashville sitemap gap, missing OG tags everywhere, missing InboundAI SEO foundation) is now 3 weeks old. These are small, fast fixes — the backlog is a prioritization problem, not a complexity problem.

---

## Broken Affiliate Links (HAKD)

**Note on methodology:** Attempted live HTTP checks via `curl` and WebFetch on all 4 external URLs plus 3 known-good control URLs (`github.com`, `google.com`, `example.com`). The sandbox's outbound network policy returned **HTTP 403 for every domain except `github.com`** — including the control URLs — confirming this is an environment-wide network restriction, not a signal about the target sites. Live verification still requires a manual click-through from Christian's own connection.

| URL | Context | Static-scan assessment |
|-----|---------|-----------|
| `https://deluxe-moxie-d4016f.netlify.app` | EMM Assessment — primary CTA, 6+ placements across hakd.app | ⚠️ **HIGH RISK** — auto-generated Netlify subdomain (not a custom domain). Structurally fragile: if the Netlify project is renamed/deleted/lapses, every CTA on the site 404s simultaneously. Click-test manually this week. |
| `https://coach.everfit.io/package/GL583637` | Monthly Coaching $250/mo | ✅ Real platform domain — verify package still published |
| `https://coach.everfit.io/package/KX912574` | Monthly Training $80/mo | ✅ Real platform domain — verify package still published |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Discovery Call booking | ✅ Real platform domain — verify availability is turned on |

No placeholder URLs (`example.com`, `#`, `TODO`, `YOUR_*_HERE`) or wrong-domain links found in HAKD's external link set. The `deluxe-moxie-d4016f.netlify.app` link remains the only structurally risky one — it isn't *broken*, but it's one accidental Netlify cleanup away from taking down hakd.app's entire conversion path.

---

## Monthly Summary

Today is **2026-06-07** — not the 1st of the month (next monthly summary due **2026-07-01**).

> **Note:** June's monthly summary appears to have been missed. The 2026-05-31 report said "today is 2026-05-31 … monthly summary scheduled for tomorrow (2026-06-01)," but the only commit since then (`5215569`, pushed 2026-06-01) just re-saved the 2026-05-31 report — no June 1 summary was generated. Recommend the 2026-07-01 audit explicitly checks for and produces the monthly summary so this doesn't slip again.

**Monthly summary scheduled for 1st of month.**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Review this week's InboundAI market intelligence brief and act on it same-day [INBOUNDAI PIPELINE — HIGHEST PRIORITY]
**Revenue impact: HIGHEST** — `inboundai_market_intelligence.py` runs every Monday at 7am on the Hetzner server and outputs `/root/Desktop/CBrownOS/System/inboundai-market-intel-latest.md`: competitor change alerts, Reddit-mined contractor pain language, and "market gaps you can own this week." This is the actual revenue-generating intelligence loop — not the marketing site. These insights decay fast; the value is in acting on them the same day they're generated, before competitors close the gap. Pull this morning's brief and turn at least one "market gap" into a script/copy change or outreach angle today.

---

### 2. 🔴 Fix Cincinnati Nashville/Tennessee brand contamination [RANK-AND-RENT — 3 WEEKS UNFIXED, URGENT]
**Revenue impact: HIGH** — Live visitors on cincinnatiwaterdamagepros.com are reading "We're a Nashville company" and "every insurance carrier in Tennessee" — this directly kills conversion trust on an active lead-gen property that's been taking traffic with this bug for 3 weeks straight. 7 text fixes + 1 broken HTML attribute, ~20 minutes total, re-verified still present line-for-line.

Fix in `index.html` (lines 138, 230, 232, 260, 274, 321) and `emergency.html` (line 48): replace "Nashville"/"Tennessee" with "Cincinnati"/"Ohio".
Fix in `index.html:112`: `itemprop="addressLocality": "Cincinnati` → `itemprop="addressLocality">Cincinnati`.

---

### 3. 🟠 Add the 4 missing pages to Nashville's sitemap.xml [RANK-AND-RENT — 3 WEEKS UNFIXED]
**Revenue impact: MEDIUM-HIGH** — `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, and `water-damage-restoration-cost-nashville` are live, internally-linked, high-value SEO pages that Google may not be crawling/indexing because they're absent from the sitemap. This is a literal 5-minute copy-paste fix that has now been flagged 3 weeks running.

---

### 4. 🔴 Rotate the HAKD ConvertKit API key [SECURITY — 3 WEEKS EXPOSED, RE-ESCALATING]
**Revenue impact: HIGH** — The hardcoded key in `/app/api/subscribe/route.js:16` (`unwsbthP07XOrlhfGdfrkg`) has now been sitting in the **public** git history for 3+ weeks. Anyone who finds it can pollute the subscriber list, inject fake tags, or spam the audience under the HAKD brand. Steps: (1) regenerate in ConvertKit, (2) add `CONVERTKIT_API_KEY` to Vercel env vars, (3) swap the hardcoded string for `process.env.CONVERTKIT_API_KEY`, (4) redeploy. ~15 minutes.

---

### 5. 🟡 Build InboundAI's SEO foundation: robots.txt + sitemap.xml + schema + OG tags [INBOUNDAI SITE — 3 WEEKS MISSING]
**Revenue impact: MEDIUM** — InboundAI is the funnel for the highest-value product, and the marketing site is still missing the basics: no robots.txt, no sitemap.xml, no Organization/SoftwareApplication JSON-LD, no OG tags, plus 2 dead `href="#"` links (logo + Terms of Service). ~30 minutes total and Google still can't reliably discover or represent the page.

Files/changes needed:
- `robots.txt` — `User-agent: * / Allow: / / Sitemap: https://inboundai.app/sitemap.xml`
- `sitemap.xml` — single `<url>` entry for `https://inboundai.app/`
- `<head>` additions: OG tags (title/description/image/url) + SoftwareApplication + Organization JSON-LD
- Fix `href="#"` on the nav logo (→ `/`) and Terms of Service link (build `/terms.html` or remove until ready)
