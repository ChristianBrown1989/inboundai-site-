# Weekly Master Report — 2026-07-19

---

## Site Audit Results

### Jacksonville | Nashville | Cincinnati | HAKD | InboundAI

---

#### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 11 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No `<meta name="keywords">` on any page — **CARRY-OVER, WEEK 9** |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url on any page — **CARRY-OVER, WEEK 9** |
| sitemap.xml | ✅ Pass | 10 public pages listed; thank-you intentionally excluded |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted; sitemap referenced |
| Schema markup | ⚠️ Issue | `sewage-backup-jacksonville.html` and `thank-you.html` have no schema; all other pages OK |
| Page speed | ✅ Pass | No `<img>` tags, no render-blocking JS; LD+JSON only |
| Broken local links | ✅ Pass | `index.html#section` anchor links are valid browser navigation, not broken |

**Action items (carry-over):** Add OG tags to all 11 pages; add `<meta name="keywords">`; add LocalBusiness schema to `sewage-backup-jacksonville.html`; add meta description to `thank-you.html`.

---

#### Nashville Water Damage (nashvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 15 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No keywords meta — **CARRY-OVER, WEEK 9** |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER, WEEK 9** |
| sitemap.xml | ⚠️ Incomplete | 10 of 14 public URLs listed — **CARRY-OVER, WEEK 9** |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted |
| Schema markup | ⚠️ Issue | 8 pages missing schema: basement-flooding, brentwood, franklin, mold-remediation, murfreesboro, sewage-backup, storm-damage, thank-you |
| Page speed | ✅ Pass | No images, no render-blocking JS |
| Homepage nav links | ❌ Issue | `index.html` footer only has 6 internal page links; Jacksonville has 9 — missing service & location pages — **CARRY-OVER, WEEK 9** |

**Sitemap gaps — re-verified, 9 weeks unchanged:**
- `/commercial-water-damage-nashville` — NOT in sitemap.xml
- `/hardwood-floor-water-damage-nashville` — NOT in sitemap.xml
- `/insurance-claim-water-damage-nashville` — NOT in sitemap.xml
- `/water-damage-restoration-cost-nashville` — NOT in sitemap.xml

**Action items:** Add 4 missing URLs to sitemap.xml; add schema to 8 unschema'd pages; add OG tags to all pages; expand footer links to match Jacksonville's pattern.

---

#### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 10 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No keywords meta — **CARRY-OVER, WEEK 9** |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER, WEEK 9** |
| sitemap.xml | ✅ Pass | 9 content pages listed correctly |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted |
| Schema markup | ⚠️ Issue | `thank-you.html` missing schema only; all other pages OK |
| Page speed | ✅ Pass | No images, no render-blocking JS |

**🚨 CRITICAL — Nashville/Tennessee brand contamination — STILL LIVE, 9 WEEKS UNFIXED:**

All 7 instances confirmed present on this audit, unchanged since week 1:

| File | Line | Wrong Text |
|------|------|-----------|
| index.html | 138 | `"⚡ 60-Minute Response · **Nashville** & Surrounding Areas"` |
| index.html | 230 | `"Why **Nashville** Trusts Us"` |
| index.html | 232 | `"treat every **Nashville** homeowner the way we'd want our own family treated"` |
| index.html | 260 | `"every major insurance carrier in **Tennessee**"` |
| index.html | 274 | `"We're a **Nashville** company. We live here too."` |
| index.html | 321 | `"Real **Nashville** Homeowners"` |
| emergency.html | 48 | `"24/7 Emergency Water Damage Response in **Nashville**"` |

**Also still broken — invalid NAP microdata (index.html line 112):**
```html
<!-- BROKEN (live now): -->
<span itemprop="addressLocality": "Cincinnati</span>
<!-- CORRECT: -->
<span itemprop="addressLocality">Cincinnati</span>
```

**Action items:** Fix all 7 Nashville/Tennessee references; fix broken `itemprop` attribute on line 112; add OG tags; add meta keywords. This is ~25 minutes of work and has been live on an active lead-gen property for **9 consecutive audited weeks**.

---

#### HAKD (hakd.app) — Next.js on Vercel

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Root layout + per-page `generateMetadata` on all routes |
| Meta description | ✅ Pass | Root layout + per-page overrides |
| Meta keywords | ❌ Missing | Not present in any page metadata export — **CARRY-OVER, WEEK 9** |
| og:title | ✅ Pass | Present via root layout and per-page overrides |
| og:description | ✅ Pass | Present via root layout and per-page overrides |
| og:image | ❌ Missing | `/public/` contains only `googledd73f79cadf7fe77.html` — no `og-image.png` — **CARRY-OVER, WEEK 9** |
| og:url | ✅ Pass | Present via root layout |
| sitemap | ✅ Pass | Dynamic `app/sitemap.js` covers static + category + article + directory + city routes |
| robots | ✅ Pass | Dynamic `app/robots.js` with AI crawler allowlist (PerplexityBot, GPTBot, ClaudeBot, Google-Extended) |
| Schema | ✅ Pass | WebSite + Person (global); Article + BreadcrumbList (articles) |
| Page speed | ⚠️ Issue | Google Fonts loaded via `<link>` preconnects in layout.js head — should migrate to `next/font/google` to eliminate render-blocking |
| Broken internal links | ✅ Pass | All internal routes resolve |

**🚨 SECURITY — ConvertKit API key hardcoded in public source — 9 WEEKS EXPOSED, CRITICAL:**

`app/api/subscribe/route.js` line 14 — `api_key: 'unwsbthP07XOrlhfGdfrkg'` committed in plaintext to the public GitHub repo. Confirmed present on this audit.

Fix (15 minutes):
1. ConvertKit → Settings → Advanced → API → **Regenerate API Key** (must rotate — key is in public git history)
2. Add `CONVERTKIT_API_KEY` to Vercel project environment variables
3. Replace `'unwsbthP07XOrlhfGdfrkg'` with `process.env.CONVERTKIT_API_KEY`
4. Redeploy

**Action items:** (1) Rotate ConvertKit API key immediately; (2) create `/public/og-image.png` (1200×630 px) and wire into `layout.js` `openGraph.images`; (3) migrate EMM Assessment to a custom subdomain.

---

#### InboundAI (inboundai.app) — Static HTML on Cloudflare Pages

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present and descriptive |
| Meta keywords | ❌ Missing | — **CARRY-OVER, WEEK 9** |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url — **CARRY-OVER, WEEK 9** |
| sitemap.xml | ❌ Missing | File does not exist in repo — **CARRY-OVER, WEEK 9** |
| robots.txt | ❌ Missing | File does not exist in repo — **CARRY-OVER, WEEK 9** |
| JSON-LD schema | ❌ Missing | No SoftwareApplication or Organization schema — **CARRY-OVER, WEEK 9** |
| Page speed | ✅ Pass | Inline CSS; Google Fonts loaded with `display=swap`; scripts deferred |
| Broken local links | ⚠️ 2 found | `href="#"` on nav logo and "Terms of Service" — no `/terms.html` exists — **CARRY-OVER, WEEK 9** |

Zero substantive commits to `index.html` since launch on 2026-04-05 (~15 weeks). Every gap flagged in week 1 remains present.

**Action items (all carry-over):** Create `robots.txt`; create `sitemap.xml`; add OG tags; add `SoftwareApplication` + `Organization` JSON-LD; fix 2 dead `href="#"` links (logo → `/`, Terms → build `/terms.html` or remove).

---

## Deploy Queue

`git log --since='2026-07-12' --oneline` results:

| Repo | New Commits (7 days) | Needs Deployment? |
|------|---------------------|-------------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 — `ec342a6 chore: weekly master report 2026-07-12` (report file only, no code) | No |

**No code deployments required this week.** All 5 sites running identical code to last week.

> ⚠️ **Ninth consecutive week with zero substantive code commits across all 5 properties.** The Cincinnati brand contamination fix is ~25 minutes. The HAKD API key rotation is ~15 minutes. The Nashville sitemap update is ~5 minutes. These are not complex problems.

---

## Broken Affiliate Links (HAKD)

Full external link scan across all `app/` files — same URLs as previous weeks:

| URL | Context | Status |
|-----|---------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | EMM Assessment — primary CTA, 30+ placements across all routes | ⚠️ **HIGH RISK** — auto-generated Netlify subdomain. One project deletion/rename breaks every CTA on hakd.app simultaneously. Migrate to `assessment.hakd.app` — **CARRY-OVER, WEEK 9** |
| `https://coach.everfit.io/package/GL583637` | Monthly Coaching — footer, sidebar | ✅ Valid Everfit platform URL |
| `https://coach.everfit.io/package/KX912574` | Monthly Training — footer, sidebar | ✅ Valid Everfit platform URL |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Discovery Call — footer, about page | ✅ Valid Calendly URL |
| `https://api.convertkit.com/v3/forms/9216083/subscribe` | Newsletter subscribe (server-side) | ⚠️ API key hardcoded in source (see HAKD security note) |

Note: Live 404 checks cannot be performed from this audit sandbox (outbound proxy restrictions). Verify each link by clicking directly in a browser session.

---

## Monthly Summary

Today is **2026-07-19** — not the 1st of the month.

**Monthly summary scheduled for 1st of month (next: 2026-08-01).**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Check this week's InboundAI market intelligence brief and act on it same-day [INBOUNDAI PIPELINE — HIGHEST PRIORITY]
**Revenue impact: HIGHEST** — The market intelligence script runs every Monday and writes a brief with competitor change alerts, contractor pain-point language, and market gaps scored for urgency. These insights decay within days. Pull the brief from `/root/Desktop/CBrownOS/System/inboundai-market-intel-latest.md` on the Hetzner server and convert at least one finding into a script change, copy update, or outreach angle today.

---

### 2. 🔴 Fix Cincinnati Nashville/Tennessee brand contamination NOW [RANK-AND-RENT — 9 WEEKS UNFIXED, CRITICAL]
**Revenue impact: HIGH** — Live visitors on cincinnatiwaterdamagepros.com are reading "We're a Nashville company" and "every insurance carrier in Tennessee." This destroys conversion trust on an active lead-gen property. Re-verified present this audit, all 7 instances unchanged for the 9th consecutive week.

Exact changes needed (~25 min):
- `index.html` lines 138, 230, 232, 260, 274, 321: Replace "Nashville" → "Cincinnati", "Tennessee" → "Ohio"
- `emergency.html` line 48: Replace "Nashville" → "Cincinnati"
- `index.html` line 112: Fix `itemprop="addressLocality": "Cincinnati` → `itemprop="addressLocality">Cincinnati`

---

### 3. 🔴 Rotate the HAKD ConvertKit API key [SECURITY — 9 WEEKS EXPOSED, CRITICAL]
**Revenue impact: HIGH** — Hardcoded key `unwsbthP07XOrlhfGdfrkg` at `app/api/subscribe/route.js:14` has been in the public GitHub repo for 9+ weeks. Any bad actor can pollute your subscriber list, inject fake tags, or spam your audience under the HAKD brand. 15-minute fix: (1) regenerate key in ConvertKit, (2) add `CONVERTKIT_API_KEY` env var in Vercel, (3) replace hardcoded string with `process.env.CONVERTKIT_API_KEY`, (4) redeploy.

---

### 4. 🟠 Fix Nashville sitemap + expand homepage navigation [RANK-AND-RENT — 9 WEEKS UNFIXED]
**Revenue impact: MEDIUM-HIGH** — Nashville's sitemap.xml is missing 4 live URLs (`commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville`). Nashville and Cincinnati homepages also lack the real footer links that Jacksonville has, meaning zero internal link equity flows to service/area pages. Copy Jacksonville's footer nav as the template. (~35 minutes total for both sites.)

---

### 5. 🟡 Build InboundAI's SEO foundation [INBOUNDAI SITE — 9 WEEKS MISSING, ~15 WEEKS SINCE LAUNCH]
**Revenue impact: MEDIUM** — InboundAI is the funnel for the highest-value product and still has no robots.txt, no sitemap.xml, no OG tags, no JSON-LD schema, and 2 dead `href="#"` links — all since launch. ~30 minutes of work. Until these exist, Google cannot reliably discover or represent the page, and social shares render with no preview image.

Files needed:
- `robots.txt` — `User-agent: * / Allow: / / Sitemap: https://inboundai.app/sitemap.xml`
- `sitemap.xml` — single `<url>` for `https://inboundai.app/`
- `index.html` `<head>`: add OG tags + `SoftwareApplication` + `Organization` JSON-LD
- Fix `href="#"` on logo (→ `/`) and Terms link (build `/terms.html` or remove)
