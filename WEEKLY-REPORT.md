# Weekly Master Report — 2026-09-20

## Site Audit Results

---

### Jacksonville Water Damage Pros (jacksonvillewaterdamagepros.com)
**11 pages | Cloudflare Workers**

| Check | Status | Notes |
|---|---|---|
| Broken links | ✅ PASS | All local refs resolve |
| Meta title | ✅ PASS | All 11 pages |
| Meta description | ⚠️ ISSUE | Missing on thank-you.html (noindexed — low priority) |
| Meta keywords | ❌ FAIL | Missing on ALL 11 pages |
| OG tags | ❌ FAIL | ALL 4 OG tags missing on ALL 11 pages |
| sitemap.xml | ✅ PASS | Exists, covers all 10 indexable pages |
| robots.txt | ✅ PASS | Exists, allows all crawlers |
| Schema markup | ⚠️ ISSUE | index.html has rich LocalBusiness + FAQPage schema (PASS); sewage-backup-jacksonville.html has ZERO schema (only content page missing it) |
| Page speed | ✅ PASS | No images, no external JS — excellent |

**Action needed:** Add OG tags to all pages; add JSON-LD schema to sewage-backup-jacksonville.html

---

### Nashville Water Damage Pros (nashvillewaterdamagepros.com)
**15 pages | Cloudflare Workers**

| Check | Status | Notes |
|---|---|---|
| Broken links | ✅ PASS | All local refs resolve |
| Meta title | ✅ PASS | All 15 pages |
| Meta description | ⚠️ ISSUE | Missing on thank-you.html (noindexed) |
| Meta keywords | ❌ FAIL | Missing on ALL 15 pages |
| OG tags | ❌ FAIL | ALL 4 OG tags missing on ALL 15 pages |
| sitemap.xml | ❌ FAIL | Exists but MISSING 4 indexable pages: commercial-water-damage-nashville, hardwood-floor-water-damage-nashville, insurance-claim-water-damage-nashville, water-damage-restoration-cost-nashville |
| robots.txt | ✅ PASS | Exists, allows all crawlers |
| Schema markup | ✅ PASS | EmergencyService + FAQPage on index.html; inner pages also have schemas |
| Page speed | ✅ PASS | No images, no external JS |
| Internal linking | ⚠️ ISSUE | 4 newest pages not linked from nav/footer — isolated from main link graph |

**Action needed:** Add 4 missing pages to sitemap.xml; add OG tags; add internal links to newer pages

---

### Cincinnati Water Damage Pros (cincinnatiwaterdamagepros.com)
**10 pages | Cloudflare Workers**

| Check | Status | Notes |
|---|---|---|
| Broken links | ✅ PASS | All local refs resolve |
| Meta title | ✅ PASS | All 10 pages |
| Meta description | ✅ PASS | All indexable pages |
| Meta keywords | ❌ FAIL | Missing on ALL 10 pages |
| OG tags | ❌ FAIL | ALL 4 OG tags missing on ALL 10 pages |
| sitemap.xml | ✅ PASS | Exists, covers all 9 indexable pages |
| robots.txt | ✅ PASS | Exists, allows all crawlers |
| Schema markup | ✅ PASS | Rich EmergencyService + FAQPage on index.html (minor HTML microdata bug on line 112) |
| Page speed | ✅ PASS | No images, no external JS |
| **CRITICAL: Nashville copy bug** | 🚨 CRITICAL | 7 instances of wrong city/state text on live pages |

**Nashville contamination details:**
- `index.html` line 138: hero badge says "Nashville & Surrounding Areas"
- `index.html` line 230: section "Why **Nashville** Trusts Us"
- `index.html` line 232: body copy "treat every **Nashville** homeowner"
- `index.html` line 260: "approved by every major insurance carrier in **Tennessee**" (should be Ohio)
- `index.html` line 274: "We're a **Nashville** company"
- `index.html` line 321: testimonials "Real **Nashville** Homeowners"
- `emergency.html` line 48: H1 "24/7 Emergency Water Damage Response in **Nashville**"

**Action needed (URGENT):** Fix all 7 Nashville copy instances in index.html and emergency.html

---

### HAKD (hakd.app)
**Next.js App Router | Vercel**

| Check | Status | Notes |
|---|---|---|
| Broken links | ⚠️ ISSUE | /public/og-image.png does not exist |
| Meta title | ✅ PASS | Set in layout.js + per-page metadata |
| Meta description | ✅ PASS | Set globally and per-page (articles pull from Supabase) |
| Meta keywords | ❌ FAIL | Not set anywhere in codebase |
| og:title | ✅ PASS | Set in layout openGraph |
| og:description | ✅ PASS | Set in layout openGraph |
| og:url | ✅ PASS | Set in layout + per-page |
| og:image | ❌ FAIL | Not set in any metadata object; og-image.png also missing from /public/ |
| sitemap.xml | ✅ PASS | Dynamic Next.js sitemap covers all routes + Supabase-driven articles/listings |
| robots.txt | ✅ PASS | Dynamic robots.js, allows all content bots |
| Schema markup | ⚠️ ISSUE | WebSite + Person schema: PASS. Article/FAQ/Breadcrumb: PASS. LocalBusiness/Organization top-level: FAIL |
| Page speed | ✅ PASS | No img tags, no external scripts; minor: unused Google Fonts preconnect links in layout.js |
| **Security: Hardcoded API key** | 🚨 SECURITY | ConvertKit API key hardcoded in app/api/subscribe/route.js — must move to env var |

**Action needed:** Create og-image.png; add og:image to layout.js; move ConvertKit API key to env var; add Organization JSON-LD to homepage

---

### InboundAI (inboundai-site-)
**Static HTML single-page | Cloudflare Workers**

| Check | Status | Notes |
|---|---|---|
| Broken links | ❌ FAIL | Terms of Service link (line 1118) is href="#" — no ToS page exists |
| Meta title | ✅ PASS | Line 6: strong title tag |
| Meta description | ✅ PASS | Line 7: 157 chars, keyword-rich |
| Meta keywords | ❌ FAIL | Missing entirely |
| OG tags | ❌ FAIL | ALL 4 OG tags missing |
| sitemap.xml | ❌ FAIL | Does not exist |
| robots.txt | ❌ FAIL | Does not exist |
| Schema markup | ❌ FAIL | ZERO JSON-LD schema anywhere — FAQPage, Service, Organization all missing despite content existing for all three |
| Page speed | ⚠️ ISSUE | Render-blocking Google Fonts CSS (line 9); missing fonts.gstatic.com preconnect; no favicon declared |

**Action needed:** Add OG tags, sitemap, robots.txt, JSON-LD schema; fix render-blocking fonts; create ToS page or remove link

---

## Deploy Queue

**Git commits in the last 7 days (since 2026-09-13):**

| Repo | New Commits | Deployment Needed? |
|---|---|---|
| jacksonville-water-damage | None (last: 2026-03-24) | No |
| nashville-water-damage | None (last: 2026-03-25) | No |
| cincinnati-water-damage | None (last: 2026-03-24) | No |
| hakd-site | None (last: 2026-03-25) | No |
| inboundai-site- | 1 commit — `b11fc87 chore: weekly master report 2026-09-13` (last week's report only) | No (report file only) |

**No active deployments needed this week.** All 5 repos have been dormant for ~6 months. Once Cincinnati copy bug fix and other changes are committed, those repos will need Cloudflare Workers re-deployment.

---

## Broken Affiliate Links (HAKD)

External href links found in hakd-site:

| URL | Location | Status | Issue |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js nav + CTA, page.js hero/banner/about, articles/[slug] sidebar, about/page.js | 🚨 FLAGGED | **Netlify STAGING URL used as primary EMM Assessment CTA across the entire production site.** Visitors clicking the main CTA could land on a staging/dev build instead of a live experience. Replace with the real production URL. |
| `https://coach.everfit.io/package/GL583637` | layout.js footer, about/page.js | ⚠️ UNVERIFIED | Monthly Coaching — $250/mo. URL appears well-formed but not live-tested. |
| `https://coach.everfit.io/package/KX912574` | layout.js footer, articles/[slug] sidebar | ⚠️ UNVERIFIED | Monthly Training — $80/mo. URL appears well-formed but not live-tested. |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js footer, about/page.js | ⚠️ UNVERIFIED | Discovery Call booking. URL appears well-formed but not live-tested. |

**Critical finding:** The primary CTA throughout HAKD points to a Netlify staging URL (`deluxe-moxie-d4016f.netlify.app`), not a production domain. This is the same issue flagged in last week's report — still unresolved.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. *(Today is 2026-09-20)*

---

## THIS WEEK'S TOP 5 PRIORITIES

**Ranked by revenue impact:**

### 1. 🚨 Fix Cincinnati "Nashville" Copy Bug — Cincinnati Water Damage Pros
**Revenue impact: HIGH** — Live rank-and-rent pages that say "Nashville company" and "Tennessee" instead of Ohio destroy local SEO credibility with both visitors and Google. Fix 7 instances across `index.html` and `emergency.html`. Estimated: 15 minutes. Deploy to Cloudflare Workers immediately.

**Files:** `cincinnati-water-damage/index.html` (lines 138, 230, 232, 260, 274, 321) and `cincinnati-water-damage/emergency.html` (line 48)

### 2. 🚨 Replace HAKD Staging URL with Production URL — HAKD
**Revenue impact: HIGH** — The primary EMM Assessment CTA across the entire HAKD site (`layout.js`, `page.js`, `about/page.js`, `articles/[slug]`) points to a Netlify staging URL (`https://deluxe-moxie-d4016f.netlify.app`). Every visitor clicking the main CTA hits a staging environment. Replace with the real production URL. This is also a carryover from last week's report.

### 3. 🔒 Move HAKD ConvertKit API Key to Environment Variable — HAKD
**Revenue impact: MEDIUM (security)** — The ConvertKit API key `unwsbthP07XOrlhfGdfrkg` is hardcoded in `hakd-site/app/api/subscribe/route.js`. Anyone with repo access can see and use this key. Move to `process.env.CONVERTKIT_API_KEY` and add to Vercel environment variables. Rotate the key after moving it.

### 4. Add OG Tags to All 5 Sites — All Sites
**Revenue impact: MEDIUM** — All 5 sites are completely missing `og:image` (some missing all OG tags). Every social share generates a blank preview card with no image, no description, and no branding. Batch-add OG tags to all 5 sites. HAKD also needs the `/public/og-image.png` file created. For rank-and-rent sites, create a single shared OG image per brand.

### 5. Add JSON-LD Schema + Sitemap + Robots to InboundAI — InboundAI Site
**Revenue impact: MEDIUM** — The InboundAI sales site has zero structured data despite having 7 FAQ items and full business contact info ready to mark up. Adding FAQPage + Service schema could generate SERP rich results for the highest-revenue product in the portfolio. Also needs sitemap.xml and robots.txt created (5-minute fixes).

---

*Report generated: 2026-09-20 | Repos audited: jacksonville-water-damage, nashville-water-damage, cincinnati-water-damage, hakd-site, inboundai-site-*
