# Weekly Master Report — 2026-05-24

---

## Site Audit Results

### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

**Pages:** 10 public HTML files + thank-you.html (noindex)

| Check | Status | Notes |
|-------|--------|-------|
| Title tags | ✅ Pass | All 11 pages |
| Meta description | ⚠️ Partial | thank-you.html missing description |
| Meta keywords | ❌ Missing | All pages |
| OG tags (og:title/description/image/url) | ❌ Missing | All pages — impacts social sharing |
| sitemap.xml | ✅ Pass | 10 URLs, all map to real files |
| robots.txt | ✅ Pass | Allows all crawlers, references sitemap |
| LocalBusiness / EmergencyService schema | ✅ Pass | index.html has both; FAQPage schema also present |
| Page speed | ✅ Pass | No images, no external JS, system fonts only |
| Broken local links | ✅ Pass | None found |

**Action items:** Add OG tags to all pages; add meta description to thank-you.html; fix "Nashville" comment in styles.css (line 2).

---

### Nashville Water Damage (nashvillewaterdamagepros.com)

**Pages:** 15 HTML files (14 public + thank-you.html noindex)

| Check | Status | Notes |
|-------|--------|-------|
| Title tags | ✅ Pass | All 15 pages |
| Meta description | ✅ Pass | All 15 pages |
| Meta keywords | ❌ Missing | All pages |
| OG tags | ❌ Missing | All pages |
| sitemap.xml | ⚠️ Incomplete | 10 URLs listed; 4 published pages missing: commercial-water-damage-nashville, hardwood-floor-water-damage-nashville, insurance-claim-water-damage-nashville, water-damage-restoration-cost-nashville |
| robots.txt | ✅ Pass | Allows all crawlers, references sitemap |
| EmergencyService schema | ✅ Pass | index.html + FAQPage; all service pages have schema |
| Page speed | ✅ Pass | No images, no external JS, inline SVG |
| Broken local links | ✅ Pass | None found |

**Action items:** Add 4 missing pages to sitemap.xml; add OG tags to all pages.

---

### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

**Pages:** 9 public HTML files + thank-you.html (noindex)

| Check | Status | Notes |
|-------|--------|-------|
| Title tags | ✅ Pass | All 10 pages |
| Meta description | ✅ Pass | All public pages; thank-you.html intentionally omitted |
| Meta keywords | ❌ Missing | All pages |
| OG tags | ❌ Missing | All pages |
| sitemap.xml | ✅ Pass | 9 URLs, all map to real files |
| robots.txt | ✅ Pass | Allows all crawlers, references sitemap |
| EmergencyService schema | ✅ Pass | index.html + FAQPage; all pages have schema |
| Page speed | ✅ Pass | No images, no external JS |
| Broken local links | ✅ Pass | None found |

**🚨 CRITICAL — Brand copy contamination (Nashville → Cincinnati):**
index.html contains Nashville text that was never updated:
- Line 138: hero badge says "Nashville & Surrounding Areas"
- Line 230: section header "Why Nashville Trusts Us"
- Line 232: body copy references "Nashville homeowner"
- Line 274: footer reads "We're a Nashville company. We live here too…"
- Line 321: testimonials section "Real Nashville Homeowners"
- emergency.html Line 48: "Response in Nashville"
- styles.css Line 2: header comment says "Nashville Water Damage Pros — Styles"

**Action items:** Fix 6 Nashville references in HTML and 1 in CSS immediately — this actively harms local SEO and conversion trust.

---

### HAKD (hakd.app) — Next.js on Vercel

**Pages:** 10 route groups (home, about, articles, articles/[slug], articles/category/[category], directory, directory/[slug], directory/category/[category], directory/city/[city], directory/city/[city]/[category]) + 5 API routes

| Check | Status | Notes |
|-------|--------|-------|
| Title tags | ✅ Pass | All pages via generateMetadata or root layout |
| Meta description | ✅ Pass | All pages |
| OG tags | ⚠️ Partial | og:title/description/url present; **og:image missing** from all metadata exports; no /public/og-image.png |
| sitemap.xml | ✅ Pass | Dynamic via app/sitemap.js — static + DB routes |
| robots.txt | ✅ Pass | Dynamic via app/robots.js; AI crawler allowlist (Claude, GPT, Perplexity) |
| JSON-LD schema | ✅ Pass | WebSite, Person, Article, BreadcrumbList, CollectionPage implemented; gap on directory/category pages |
| Page speed | ✅ Pass | No images, no external JS, proper 'use client' usage |
| Broken local links | ✅ Pass | None found |

**🚨 SECURITY CRITICAL — Hardcoded API key:**
`/app/api/subscribe/route.js` line 14 has the ConvertKit API key hardcoded in source:
```
api_key: 'unwsbthP07XOrlhfGdfrkg',
```
This key is visible in the git repo. **Rotate this key immediately** and move to `process.env.CONVERTKIT_API_KEY`.

**External links found (affiliate/partner):**
- https://deluxe-moxie-d4016f.netlify.app — EMM Assessment (6+ uses) — appears live
- https://coach.everfit.io/package/GL583637 — Monthly Coaching $250/mo
- https://coach.everfit.io/package/KX912574 — Monthly Training $80/mo
- https://calendly.com/christianb3/15-minute-discovery-call — Discovery Call booking
- https://api.convertkit.com — ConvertKit newsletter API

**Action items:** (1) Rotate ConvertKit API key NOW; (2) add og:image (1200×630 PNG) to /public and reference in layout metadata; (3) add CollectionPage JSON-LD to directory/category pages.

---

### InboundAI (inboundai.app) — Static HTML on Cloudflare Workers

**Pages:** 1 (index.html — single-page site)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | index.html line 6 |
| Meta description | ✅ Pass | 157 characters, well-written |
| Meta keywords | ❌ Missing | |
| OG tags | ❌ Missing | No og:title, og:description, og:image, og:url |
| sitemap.xml | ❌ Missing | File does not exist |
| robots.txt | ❌ Missing | File does not exist |
| JSON-LD schema | ❌ Missing | No Organization or LocalBusiness schema |
| Page speed | ✅ Pass | Emoji-only visuals, inline CSS, no images |
| Broken local links | ⚠️ 2 found | Logo href="#" (line 538); Terms of Service href="#" (line 1118) — no /terms.html exists |

**Action items:** Create robots.txt and sitemap.xml; add OG tags; add JSON-LD Organization schema; fix 2 dead href="#" links.

---

## Deploy Queue

Run `git log --since='7 days ago' --oneline` results:

| Repo | Commits (7 days) | Needs Deploy? |
|------|-----------------|---------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 (weekly report update only) | No — report file only |

**No code deployments required this week.** All sites are stable. The only commit is this report file being added to inboundai-site-.

---

## Broken Affiliate Links (HAKD)

Static URL analysis complete (live HTTP checks not run — network verification pending):

| URL | Context | Status |
|-----|---------|--------|
| https://deluxe-moxie-d4016f.netlify.app | EMM Assessment — 6+ placements | ⚠️ Netlify subdomain — verify it's live; consider moving to custom domain |
| https://coach.everfit.io/package/GL583637 | Monthly Coaching $250/mo | ✅ Appears valid (Everfit is active platform) |
| https://coach.everfit.io/package/KX912574 | Monthly Training $80/mo | ✅ Appears valid |
| https://calendly.com/christianb3/15-minute-discovery-call | Discovery Call | ✅ Appears valid |

**Recommended:** Manually click all 4 links to confirm they load. The Netlify assessment URL is the highest risk — if that app goes down or the Netlify project is deleted, 6+ CTAs across the site will send users to a dead page.

---

## Monthly Summary

Today is May 24, 2026. **Monthly summary scheduled for 1st of month.**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Fix Cincinnati "Nashville" copy contamination [RANK-AND-RENT — URGENT]
**Revenue impact: HIGH** — A visitor landing on cincinnatiwaterdamagepros.com and reading "We're a Nashville company" will immediately distrust the site and bounce. This is actively destroying conversion rate on a lead-gen property.
- Fix 6 instances in index.html (lines 138, 230, 232, 274, 321) and emergency.html (line 48)
- Fix styles.css line 2 comment

### 2. 🔴 Rotate HAKD ConvertKit API key [SECURITY — URGENT]
**Revenue impact: HIGH** — Hardcoded API key in `/app/api/subscribe/route.js` line 14 is in git history. Anyone who sees the repo can spam your list, add fake subscribers, or corrupt your tags. Rotate immediately via ConvertKit dashboard and move to `CONVERTKIT_API_KEY` env var in Vercel.

### 3. 🟠 Add OG tags to all 3 rank-and-rent sites [SEO/SOCIAL — RANK-AND-RENT]
**Revenue impact: MEDIUM-HIGH** — All 36 pages across Jacksonville, Nashville, and Cincinnati have zero OG tags. Any social share produces no rich preview. One batch PR per site adds og:title, og:description, og:image, og:url to all pages.
- Use a consistent brand image (e.g., logo on brand-colored background 1200×630px)

### 4. 🟠 Add Nashville's 4 missing pages to sitemap.xml [SEO — RANK-AND-RENT]
**Revenue impact: MEDIUM** — Four high-value SEO pages (commercial, hardwood floor, insurance claims, cost guide) are live on disk but not in the sitemap. Google may not index them or may deprioritize crawl. Update sitemap.xml to include all 4 URLs.

### 5. 🟡 Add sitemap.xml, robots.txt, and JSON-LD schema to InboundAI [INBOUNDAI SITE]
**Revenue impact: MEDIUM** — InboundAI is the top-of-funnel for the highest-value business. Missing robots.txt, sitemap, and Organization schema are basic SEO infrastructure gaps. Add all three plus OG tags to maximize discoverability for inbound leads searching for AI phone answering services.
