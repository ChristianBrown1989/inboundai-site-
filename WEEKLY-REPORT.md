# Weekly Master Report — 2026-05-10

---

## Site Audit Results

### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

**Pages:** 10 public HTML files + thank-you.html (noindex)

| Check | Status | Notes |
|---|---|---|
| Title tags | ✅ Pass | All 10 public pages have descriptive titles |
| Meta description | ✅ Pass | All 10 public pages |
| Meta keywords | ⚠️ Missing | All pages — low priority (Google ignores) |
| OG tags | ❌ FAIL | **Zero OG tags on any page** — no og:title/description/image/url |
| Sitemap | ✅ Pass | sitemap.xml exists, all 10 URLs valid, thank-you.html correctly excluded |
| Robots.txt | ✅ Pass | `Allow: /` — not blocking crawlers, sitemap declared |
| Schema markup | ⚠️ Partial | index.html has LocalBusiness + EmergencyService + FAQPage ✅; `sewage-backup-jacksonville.html` **missing JSON-LD entirely** ❌ |
| Broken local links | ✅ Pass | No broken href/src references |
| Images | ✅ Pass | No images used (emoji + inline SVG) — no optimization issues |
| Render-blocking scripts | ✅ Pass | Only JSON-LD scripts; no external JS loaded |
| Canonical tags | ✅ Pass | All public pages |

**Action items:**
1. Add OG tags to all 10 public pages (needs og:image asset created — 1200×630px)
2. Add EmergencyService JSON-LD schema to `sewage-backup-jacksonville.html`
3. Fix CSS comment on `styles.css` line 2: says "Nashville Water Damage Pros" — should say "Jacksonville"

---

### Nashville Water Damage (nashvillewaterdamagepros.com)

**Pages:** 14 public HTML files + thank-you.html (noindex)

| Check | Status | Notes |
|---|---|---|
| Title tags | ✅ Pass | All 14 public pages |
| Meta description | ✅ Pass | All 14 public pages |
| Meta keywords | ⚠️ Missing | All pages — low priority |
| OG tags | ❌ FAIL | **Zero OG tags on any page** |
| Sitemap | ⚠️ Incomplete | sitemap.xml exists but **missing 4 pages**: `hardwood-floor-water-damage-nashville`, `commercial-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville` |
| Robots.txt | ✅ Pass | `Allow: /` — correctly configured |
| Schema markup | ⚠️ Partial | index.html has EmergencyService + FAQPage ✅; cost/insurance/commercial/hardwood pages have FAQPage ✅; service pages (basement, mold, storm, sewage, regional) missing or minimal schema |
| Broken local links | ✅ Pass | No broken href/src references |
| Images | ✅ Pass | No images |
| Render-blocking scripts | ✅ Pass | Clean |

**Action items:**
1. Add OG tags to all 14 public pages
2. **Update sitemap.xml** to include 4 missing high-value pages (these are likely getting organic traffic but not signaled to Google)
3. Add EmergencyService schema to service pages missing it (sewage, basement, storm, regional pages)

---

### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

**Pages:** 9 public HTML files + thank-you.html (noindex)

| Check | Status | Notes |
|---|---|---|
| Title tags | ✅ Pass | All 9 public pages |
| Meta description | ✅ Pass | All 9 public pages |
| Meta keywords | ⚠️ Missing | All pages — low priority |
| OG tags | ❌ FAIL | **Zero OG tags on any page** |
| Sitemap | ✅ Pass | sitemap.xml exists, all 9 URLs valid |
| Robots.txt | ✅ Pass | `Allow: /` — correctly configured |
| Schema markup | ✅ Pass | Excellent — index.html has EmergencyService + FAQPage + LocalBusiness; service pages also have schema |
| Broken local links | ✅ Pass | No broken href/src references |
| Images | ✅ Pass | No images |
| Render-blocking scripts | ✅ Pass | Clean |
| **CONTENT BUG** | ❌ FAIL | **Multiple "Nashville" references in Cincinnati pages** |

**Content bugs (Cincinnati — critical for rank-and-rent credibility):**
- `index.html` line 138: "Nashville & Surrounding Areas" → should be "Cincinnati & Surrounding Areas"
- `index.html` line 230: "Why Nashville Trusts Us" → "Why Cincinnati Trusts Us"
- `index.html` line 232: "treat every Nashville homeowner" → "treat every Cincinnati homeowner"
- `index.html` line 274: "We're a Nashville company" → "We're a Cincinnati company"
- `index.html` line 321: "Real Nashville Homeowners" → "Real Cincinnati Homeowners"
- `emergency.html` line 48: "Response in Nashville" → "Response in Cincinnati"
- `styles.css` line 2: "Nashville Water Damage Pros" → "Cincinnati Water Damage Pros"

**Action items:**
1. **Fix all Nashville→Cincinnati copy bugs immediately** — a prospect reading this will lose trust
2. Add OG tags to all 9 public pages
3. Meta robots tag missing on 8 of 9 pages (non-critical but clean-up recommended)

---

### HAKD (hakd.app) — Next.js

**Pages:** App Router — ~140+ dynamic pages (articles, directory listings, city/category combos)

| Check | Status | Notes |
|---|---|---|
| Title tags | ✅ Pass | All pages via metadata exports / generateMetadata |
| Meta description | ✅ Pass | All pages |
| Meta keywords | ⚠️ Missing | Not implemented — low priority |
| OG title/description/url | ✅ Pass | All pages |
| **og:image** | ❌ FAIL | **No og:image on ANY page; /public/og-image.png does not exist** |
| Sitemap | ✅ Pass | Dynamic `/app/sitemap.js` — covers all static + DB-driven routes |
| Robots.txt | ✅ Pass | `/app/robots.js` — allows all crawlers including AI bots (GPTBot, ClaudeBot, Perplexity, etc.) |
| Schema markup | ✅ Excellent | WebSite, Person, Article, CollectionPage, FAQPage, BreadcrumbList — comprehensive |
| Broken local links | ✅ Pass | All internal Next.js routes valid |
| /public/og-image.png | ❌ FAIL | File does not exist |
| Images | ✅ Pass | No img tags — CSS-based design |
| Render-blocking | ✅ Pass | ISR caching, code-split client components, preconnected Google Fonts |
| **Security issue** | ⚠️ Warn | ConvertKit API key hardcoded in `/app/api/subscribe/route.js` line 14 |

---

### InboundAI (inboundai-site-)

**Pages:** 1 page (single-page static HTML, 57.7 KB)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ⚠️ Too long | 203 chars — trim to ~160 |
| Meta keywords | ❌ Missing | Low priority |
| OG tags | ❌ FAIL | **Zero OG tags** |
| Sitemap | ❌ Missing | No sitemap.xml — single page, low impact but should exist |
| Robots.txt | ❌ Missing | No robots.txt |
| Schema markup | ❌ Missing | **No LocalBusiness or Organization schema at all** |
| Broken links | ⚠️ One issue | Terms of Service link (line 1118) points to `href="#"` — placeholder, never built |
| Images | ✅ Pass | No images — text/CSS-based |
| Render-blocking | ✅ Pass | Google Fonts preconnected, no external JS |

**Action items:**
1. Add OG tags
2. Add Organization/LocalBusiness schema
3. Create sitemap.xml and robots.txt (minimal — one URL each)
4. Fix or remove the Terms of Service dead link
5. Trim meta description to ~160 chars

---

## Deploy Queue

**Git log — last 7 days (all repos):**

| Repo | New Commits | Deploy Needed? |
|---|---|---|
| jacksonville-water-damage | None | No |
| nashville-water-damage | None | No |
| cincinnati-water-damage | None | No |
| hakd-site | None | No |
| inboundai-site- | This report commit | Yes — push to Vercel after commit |

**No emergency deploys pending.** All sites are at their last deployed state. The Cincinnati copy bug fix (Priority #1) will require a Cloudflare Workers deploy once committed.

---

## Broken Affiliate Links (HAKD)

The following external links appear across hakd-site and require manual verification:

| Link | Location | Risk Level | Notes |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js:62,77,80; page.js:70,196,226; about/page.js:140; articles/[slug]/page.js:201; multiple city/category pages | ⚠️ HIGH | Netlify subdomain — 10+ occurrences across site. If this project is ever deleted or renamed, ALL EMM Assessment CTAs break simultaneously. Should be moved to a permanent domain. |
| `https://coach.everfit.io/package/GL583637` | layout.js:113; about/page.js:114; articles/[slug]/page.js:210 | Medium | Everfit coaching package — verify package still active |
| `https://coach.everfit.io/package/KX912574` | layout.js:114; articles/[slug]/page.js:221 | Medium | Everfit training package — verify package still active |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js:115; about/page.js:123 | Low | Calendly link — confirm event type is still published and taking bookings |

**Recommended action:** Click all 4 links manually this week. The Netlify subdomain is the highest risk — migrate the EMM Assessment to a stable domain or Vercel deployment before it becomes a broken-link emergency.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. (Today: 2026-05-10)

Next full performance summary: **June 1, 2026** — will include:
- Total pages per site
- Sitemap coverage %
- Schema markup coverage %
- New pages added this month (from git log)

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. Fix Cincinnati "Nashville" Copy Bugs — DEPLOY IMMEDIATELY
**Revenue impact:** Rank-and-rent conversion killer. A potential client or lead buyer finding "Nashville" content on a Cincinnati water damage site will immediately distrust the business and bounce. Also signals geo-relevance mismatch to Google, which can suppress rankings.

**What to do:** Fix 7 specific lines across `cincinnati-water-damage/index.html` (lines 138, 230, 232, 274, 321), `emergency.html` (line 48), and `styles.css` (line 2). Commit and deploy to Cloudflare Workers. ~30 min.

---

### 2. InboundAI: Add OG Tags + Schema + robots.txt + sitemap.xml
**Revenue impact:** InboundAI is the highest-revenue-potential asset. It currently has no schema, no OG tags, no robots.txt, and no sitemap. Every sales prospect who Googles it before a demo sees an unoptimized result with no social card. These are table-stakes for a SaaS landing page.

**What to do:** Add OG block to `index.html` `<head>`, add LocalBusiness/Organization JSON-LD, create a one-URL `sitemap.xml`, create `robots.txt`, fix or remove the dead Terms of Service link, and trim the meta description to 160 chars. ~1–2 hours.

---

### 3. Nashville: Add 4 Missing Pages to sitemap.xml
**Revenue impact:** `commercial-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville`, and `hardwood-floor-water-damage-nashville` exist with FAQPage schema and target high-intent commercial + cost-comparison keywords. They are not in sitemap.xml and may not be crawled/indexed by Google. Adding them costs nothing and could unlock ranking gains.

**What to do:** Edit `nashville-water-damage/sitemap.xml`, add 4 `<url>` entries with priority 0.8 and current date. Commit and deploy. ~15 min.

---

### 4. HAKD: Create og-image.png + Wire og:image to All Pages
**Revenue impact:** HAKD grows via content sharing on Twitter/X, LinkedIn, and newsletters. Social previews currently show nothing (no og:image anywhere, `/public/og-image.png` missing). A branded image card dramatically increases click-through rate on shared articles and directory listings.

**What to do:** Design a 1200×630px branded HAKD image, save to `/public/og-image.png`, add `images: [{ url: '/og-image.png', width: 1200, height: 630 }]` to the root layout metadata in `/app/layout.js`. For articles, also pull the article's featured image from the DB if available. ~2–3 hours including design.

---

### 5. HAKD: Move ConvertKit API Key to Environment Variable
**Revenue impact:** Security hygiene protecting the newsletter subscriber list. The ConvertKit API key `unwsbthP07XOrlhfGdfrkg` is hardcoded in `/app/api/subscribe/route.js` line 14 and readable in git history. If the repo is ever exposed, anyone can send emails from the newsletter account or exhaust API quota.

**What to do:** Add `CONVERTKIT_API_KEY` to Vercel environment variables, replace the hardcoded string in `route.js` with `process.env.CONVERTKIT_API_KEY`, rotate the key in ConvertKit dashboard. ~15 min.

---

*Report generated: 2026-05-10 | Audited by Claude Code (claude-sonnet-4-6)*
