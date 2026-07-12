# Weekly Master Report — 2026-07-12

---

## Site Audit Results

### Jacksonville | Nashville | Cincinnati | HAKD | InboundAI

---

#### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 10 public pages |
| Meta description | ✅ Pass | Present on all public pages |
| Meta keywords | ❌ Missing | No `<meta name="keywords">` on any page — **CARRY-OVER, WEEK 8** |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url on any page — **CARRY-OVER, WEEK 8** |
| sitemap.xml | ✅ Pass | All 10 public pages listed; correct URLs |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted; sitemap referenced |
| LocalBusiness schema | ✅ Pass | `["LocalBusiness"]` + `FAQPage` + `AggregateRating` on index.html |
| Page speed | ✅ Pass | No `<img>` tags, no render-blocking JS |
| Broken local links | ✅ Pass | All internal `href` values resolve to existing files |

**Action items (carry-over):** Add OG tags (og:title, og:description, og:image, og:url) to all 10 pages; add `<meta name="keywords">`.

---

#### Nashville Water Damage (nashvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all pages |
| Meta description | ✅ Pass | Present on all public pages (thank-you.html missing, acceptable) |
| Meta keywords | ❌ Missing | No keywords meta — **CARRY-OVER, WEEK 8** |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER, WEEK 8** |
| sitemap.xml | ⚠️ Incomplete | 10 of 14 public URLs listed — **CARRY-OVER, WEEK 8** |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted |
| EmergencyService schema | ✅ Pass | EmergencyService + FAQPage + AggregateRating on index.html; 7 inner pages missing schema |
| Page speed | ✅ Pass | No images, no render-blocking JS |
| Broken local links | ✅ Pass | None found |
| Homepage → sub-page links | ❌ Issue | `index.html` footer links only to `#anchor` targets — zero real hrefs to the 14 service/location pages — **CARRY-OVER, WEEK 8** |

**Sitemap gaps — re-verified, 8 weeks unchanged:**
- `/commercial-water-damage-nashville` — NOT in sitemap.xml
- `/hardwood-floor-water-damage-nashville` — NOT in sitemap.xml
- `/insurance-claim-water-damage-nashville` — NOT in sitemap.xml
- `/water-damage-restoration-cost-nashville` — NOT in sitemap.xml

**Action items:** Add the 4 missing URLs to sitemap.xml; add real homepage footer/nav links to service and location pages (use Jacksonville as the template); add OG tags to all pages.

---

#### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all pages |
| Meta description | ✅ Pass | Present on all public pages |
| Meta keywords | ❌ Missing | No keywords meta — **CARRY-OVER, WEEK 8** |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER, WEEK 8** |
| sitemap.xml | ✅ Pass | 9 public pages listed correctly |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted |
| EmergencyService schema | ✅ Pass | EmergencyService on all pages; FAQPage + AggregateRating on index.html |
| Page speed | ✅ Pass | No images, no render-blocking JS |
| Broken local links | ✅ Pass | None found |
| Homepage → sub-page links | ❌ Issue | `index.html` footer links only to `#anchor` targets — no real hrefs to service/location pages — **CARRY-OVER, WEEK 8** |

**🚨 CRITICAL — Nashville/Tennessee brand contamination — STILL LIVE, 8 WEEKS UNFIXED:**

All 7 instances present, unchanged since week 1:

| File | Wrong Text |
|------|-----------|
| index.html (hero badge) | "⚡ 60-Minute Response · **Nashville** & Surrounding Areas" |
| index.html (section heading) | "Why **Nashville** Trusts Us" |
| index.html (section sub) | "treat every **Nashville** homeowner the way we'd want our own family treated" |
| index.html (why-item) | "approved by every major insurance carrier in **Tennessee**" |
| index.html (why-item) | "We're a **Nashville** company. We live here too." |
| index.html (testimonials) | "Real **Nashville** Homeowners" |
| emergency.html | "24/7 Emergency Water Damage Response in **Nashville**" |

**Also still broken — invalid NAP microdata (index.html line 112):**
```html
<!-- BROKEN (live now): -->
<span itemprop="addressLocality": "Cincinnati</span>
<!-- CORRECT: -->
<span itemprop="addressLocality">Cincinnati</span>
```

**Action items:** Fix all 7 Nashville/Tennessee references in `index.html` and `emergency.html`; fix the broken `itemprop` attribute on line 112; add real footer links to the 7 service/area pages. ~25 minutes total. This conversion-killing brand contamination has now been live for **8 consecutive audited weeks**.

---

#### HAKD (hakd.app) — Next.js on Vercel

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Root layout + per-page `generateMetadata` on all 11 routes |
| Meta description | ✅ Pass | Root layout + per-page overrides |
| Meta keywords | ❌ Missing | Not present in any page metadata export — **CARRY-OVER, WEEK 8** |
| og:title | ✅ Pass | Present via root layout and per-page overrides |
| og:description | ✅ Pass | Present via root layout and per-page overrides |
| og:image | ❌ Missing | `/public/` contains only `googledd73f79cadf7fe77.html` — no `og-image.png` — **CARRY-OVER, WEEK 8** |
| og:url | ✅ Pass | Present via root layout and per-page overrides |
| sitemap | ✅ Pass | Dynamic `app/sitemap.js` covers static + category + article + directory + city routes |
| robots | ✅ Pass | Dynamic `app/robots.js` with AI crawler allowlist (PerplexityBot, GPTBot, ClaudeBot, Google-Extended) |
| Schema | ✅ Pass | WebSite + Person (global); Article + BreadcrumbList (articles); CollectionPage + BreadcrumbList (categories/cities) |
| Page speed | ⚠️ Issue | Google Fonts loaded via CSS `@import` in `globals.css` — render-blocking; should migrate to `next/font/google` |
| Broken internal links | ✅ Pass | All internal routes resolve |

**🚨 SECURITY — ConvertKit API key hardcoded in public source — 8 WEEKS EXPOSED, CRITICAL:**

`app/api/subscribe/route.js` line 14 — `api_key: 'unwsbthP07XOrlhfGdfrkg'` committed in plaintext to the public GitHub repo.

Fix (15 minutes):
1. ConvertKit → Settings → Advanced → API → **Regenerate API Key** (must rotate — key is in public history)
2. Add `CONVERTKIT_API_KEY` to Vercel project environment variables
3. Replace hardcoded string with `process.env.CONVERTKIT_API_KEY`
4. Redeploy

This has been flagged in **eight** consecutive weekly reports without action.

**Action items:** (1) Rotate ConvertKit API key immediately; (2) add `/public/og-image.png` (1200×630 px) and reference it in `layout.js` `openGraph.images`; (3) migrate EMM Assessment off the Netlify auto-subdomain (see Broken Affiliate Links).

---

#### InboundAI (inboundai.app) — Static HTML on Cloudflare Pages

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present |
| Meta keywords | ❌ Missing | — **CARRY-OVER, WEEK 8** |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url — **CARRY-OVER, WEEK 8** |
| sitemap.xml | ❌ Missing | File does not exist in repo — **CARRY-OVER, WEEK 8** |
| robots.txt | ❌ Missing | File does not exist in repo — **CARRY-OVER, WEEK 8** |
| JSON-LD schema | ❌ Missing | No SoftwareApplication or Organization schema — **CARRY-OVER, WEEK 8** |
| Page speed | ✅ Pass | Inline `<style>` + `<script>` at end of body; zero `<img>` tags |
| Broken local links | ⚠️ 2 found | `href="#"` on nav logo and "Terms of Service" link — no `/terms.html` exists — **CARRY-OVER, WEEK 8** |

Zero code commits to `index.html` since launch on 2026-04-05 (~14 weeks). Every gap flagged in week 1 is still present.

**Action items (all carry-over):** Create `robots.txt`; create `sitemap.xml`; add OG tags to `<head>`; add `SoftwareApplication` + `Organization` JSON-LD; fix the 2 dead `href="#"` links (logo → `/`, Terms → build `/terms.html` or remove).

---

## Deploy Queue

`git log --since='2026-07-05' --oneline` results:

| Repo | New Commits (7 days) | Needs Deployment? |
|------|---------------------|-------------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 — `15a4234 chore: weekly master report 2026-07-05` (report file only) | No |

**No code deployments required this week.** All 5 sites are running the same code as last week.

> ⚠️ **Eighth consecutive week with zero substantive code commits across all 5 properties.** Every item in the backlog (Cincinnati brand contamination, HAKD API key security issue, Nashville sitemap gap, missing OG tags on all 5 sites, InboundAI SEO foundation) is a small, well-scoped fix. The Cincinnati contamination is ~25 minutes and directly impacts active lead generation on a live site.

---

## Broken Affiliate Links (HAKD)

Full external link scan across all `app/` files:

| URL | Context | Status |
|-----|---------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | EMM Assessment — primary CTA, 30+ placements across all routes (announce bar, nav, hero, about, every article sidebar, all directory pages) | ⚠️ **HIGH RISK** — auto-generated Netlify subdomain. One Netlify project deletion or rename breaks every single CTA on hakd.app simultaneously. Migrate to a custom subdomain (e.g. `assessment.hakd.app`) — **CARRY-OVER, WEEK 8** |
| `https://coach.everfit.io/package/GL583637` | Monthly Coaching ($250/mo) — footer, sidebar | ✅ Live Everfit platform URL |
| `https://coach.everfit.io/package/KX912574` | Monthly Training ($80/mo) — footer, sidebar | ✅ Live Everfit platform URL |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Discovery Call — footer, about page | ✅ Live Calendly URL |
| `https://api.convertkit.com/v3/forms/9216083/subscribe` | Newsletter subscribe (server-side) | ⚠️ API key hardcoded in source (see HAKD security note above) |
| `https://api.telegram.org/bot${TELEGRAM_TOKEN}/sendMessage` | Lead + Stripe notifications (server-side) | ✅ Token correctly in env vars |

No placeholder URLs (`example.com`, `#`, `TODO`), wrong-domain links, or dead affiliate patterns found beyond the above. Live 404 checks cannot be completed from this audit environment (proxy blocks outbound); verify by clicking each link directly.

---

## Monthly Summary

Today is **2026-07-12** — not the 1st of the month.

**Monthly summary scheduled for 1st of month (next: 2026-08-01).**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Check this week's InboundAI market intelligence brief and act on it same-day [INBOUNDAI PIPELINE — HIGHEST PRIORITY]
**Revenue impact: HIGHEST** — The `inboundai_market_intelligence.py` script runs every Monday at 7am on the Hetzner server and writes a brief with competitor change alerts, contractor pain-point language scraped from Reddit, and market gaps scored for urgency. These insights decay within days. Pull the brief from `/root/Desktop/CBrownOS/System/inboundai-market-intel-latest.md` and turn at least one finding into a script change, copy update, or outreach angle today. The audit environment is sandboxed to GitHub repos and cannot access the Hetzner server directly.

---

### 2. 🔴 Fix Cincinnati Nashville/Tennessee brand contamination NOW [RANK-AND-RENT — 8 WEEKS UNFIXED, CRITICAL]
**Revenue impact: HIGH** — Live visitors on cincinnatiwaterdamagepros.com are reading "We're a Nashville company" and "every insurance carrier in Tennessee." This directly destroys conversion trust on an active lead-gen property that is receiving real traffic. Re-verified present this audit, all 7 instances unchanged for the 8th consecutive week.

Exact changes needed (~25 min):
- `index.html`: Replace all 6 instances of "Nashville" → "Cincinnati", 1 instance of "Tennessee" → "Ohio"
- `emergency.html`: Replace Nashville reference → Cincinnati
- `index.html` line 112: Fix broken attribute `itemprop="addressLocality": "Cincinnati` → `itemprop="addressLocality">Cincinnati`

---

### 3. 🔴 Rotate the HAKD ConvertKit API key [SECURITY — 8 WEEKS EXPOSED, CRITICAL]
**Revenue impact: HIGH** — Hardcoded key `unwsbthP07XOrlhfGdfrkg` at `app/api/subscribe/route.js:14` has been in the public GitHub repo for 8+ weeks. Any bad actor can pollute your subscriber list, inject fake tags, or spam your audience under the HAKD brand identity. 15-minute fix: (1) regenerate key in ConvertKit, (2) add `CONVERTKIT_API_KEY` env var in Vercel, (3) replace hardcoded string with `process.env.CONVERTKIT_API_KEY`, (4) redeploy.

---

### 4. 🟠 Fix Nashville sitemap + homepage navigation on Nashville and Cincinnati [RANK-AND-RENT — 8 WEEKS UNFIXED]
**Revenue impact: MEDIUM-HIGH** — Nashville's sitemap.xml is missing 4 live URLs, meaning those pages get zero sitemap-driven crawl priority. On both Nashville and Cincinnati, the homepage contains zero real outbound links to individual service/area pages — only `#anchor` self-links, passing no internal link equity. Jacksonville does this correctly — copy its footer link structure as the template. (~30 minutes total for both sites.)

---

### 5. 🟡 Build InboundAI's SEO foundation [INBOUNDAI SITE — 8 WEEKS MISSING, ~14 WEEKS SINCE LAUNCH]
**Revenue impact: MEDIUM** — InboundAI is the funnel for the highest-value product and still has the same foundational SEO gaps since launch: no robots.txt, no sitemap.xml, no OG tags, no JSON-LD schema, 2 dead `href="#"` links. ~30 minutes of work total. Until these exist, Google cannot reliably discover or represent the page, and social shares render with no preview image.

Files needed:
- `robots.txt` — `User-agent: * / Allow: / / Sitemap: https://inboundai.app/sitemap.xml`
- `sitemap.xml` — single `<url>` for `https://inboundai.app/`
- `index.html` `<head>`: add OG tags (og:title, og:description, og:image 1200×630, og:url) + `SoftwareApplication` + `Organization` JSON-LD
- Fix `href="#"` on nav logo (→ `/`) and Terms of Service (build `/terms.html` or remove the link)
