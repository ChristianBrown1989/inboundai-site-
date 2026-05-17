# Weekly Master Report — 2026-05-17

---

## Site Audit Results

### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

**Pages:** 10 public HTML files + thank-you.html (noindex)

| Check | Status | Notes |
|---|---|---|
| Title tags | ✅ Pass | All 10 public pages have descriptive titles |
| Meta description | ✅ Pass | All 10 public pages |
| Meta keywords | ⚠️ Missing | All pages — low priority (Google ignores) |
| OG tags | ❌ FAIL | **Zero OG tags on any page** — no og:title/description/image/url — CARRIED OVER |
| Sitemap | ✅ Pass | sitemap.xml exists, all 10 URLs valid, thank-you.html correctly excluded |
| Robots.txt | ✅ Pass | `Allow: /` — not blocking crawlers, sitemap declared |
| Schema markup | ⚠️ Partial | index.html has LocalBusiness + EmergencyService + FAQPage ✅; `sewage-backup-jacksonville.html` **missing JSON-LD entirely** ❌ — CARRIED OVER |
| Broken local links | ✅ Pass | No broken href/src references |
| Images | ✅ Pass | No images (emoji + inline SVG only) — no optimization issues |
| Render-blocking scripts | ✅ Pass | Only JSON-LD scripts; no external JS loaded |
| Canonical tags | ✅ Pass | All public pages |

**Action items (both carried over from 2026-05-10):**
1. Add OG tags to all 10 public pages (needs og:image asset — 1200×630px)
2. Add EmergencyService JSON-LD schema to `sewage-backup-jacksonville.html`

---

### Nashville Water Damage (nashvillewaterdamagepros.com)

**Pages:** 14 public HTML files + thank-you.html (noindex)

| Check | Status | Notes |
|---|---|---|
| Title tags | ✅ Pass | All 14 public pages |
| Meta description | ✅ Pass | All 14 public pages |
| Meta keywords | ⚠️ Missing | All pages — low priority |
| OG tags | ❌ FAIL | **Zero OG tags on any page** — CARRIED OVER |
| Sitemap | ⚠️ Incomplete | sitemap.xml has 10 URLs; **4 pages still missing**: `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville` — CARRIED OVER |
| Robots.txt | ✅ Pass | `Allow: /` — correctly configured |
| Schema markup | ✅ Good | index.html has EmergencyService + FAQPage ✅; cost/insurance/commercial/hardwood pages have FAQPage ✅ |
| Broken local links | ✅ Pass | No broken href/src references |
| Images | ✅ Pass | No images |
| Render-blocking scripts | ✅ Pass | Clean |

**Action items (both carried over from 2026-05-10):**
1. Add OG tags to all 14 public pages
2. **Update sitemap.xml** — add 4 missing high-value SEO pages (likely not being crawled/indexed by Google)

---

### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

**Pages:** 9 public HTML files + thank-you.html (noindex)

| Check | Status | Notes |
|---|---|---|
| Title tags | ✅ Pass | All 9 public pages |
| Meta description | ✅ Pass | All 9 public pages |
| Meta keywords | ⚠️ Missing | All pages — low priority |
| OG tags | ❌ FAIL | **Zero OG tags on any page** — CARRIED OVER |
| Sitemap | ✅ Pass | sitemap.xml exists, all 9 URLs valid |
| Robots.txt | ✅ Pass | `Allow: /` — correctly configured |
| Schema markup | ✅ Pass | Excellent — index.html has EmergencyService + FAQPage + LocalBusiness microdata; service pages also have schema |
| Broken local links | ✅ Pass | No broken href/src references |
| Images | ✅ Pass | No images |
| Render-blocking scripts | ✅ Pass | Clean |
| **CONTENT BUG** | ❌ FAIL | **Nashville references on Cincinnati pages — CARRIED OVER, still not fixed** |

**Content bugs still present (critical for rank-and-rent credibility):**
- `index.html` line 138: "Nashville & Surrounding Areas" → should be "Cincinnati & Surrounding Areas"
- `index.html` line 230: "Why Nashville Trusts Us" → "Why Cincinnati Trusts Us"
- `index.html` line 232: "treat every Nashville homeowner" → "treat every Cincinnati homeowner"
- `index.html` line 274: "We're a Nashville company" → "We're a Cincinnati company"
- `index.html` line 321: "Real Nashville Homeowners" → "Real Cincinnati Homeowners"
- `emergency.html` line 48: "Response in Nashville" → "Response in Cincinnati"
- `styles.css` line 2: "Nashville Water Damage Pros" → "Cincinnati Water Damage Pros"

**Action items:**
1. **Fix all Nashville→Cincinnati copy bugs immediately** — 3 weeks unfixed; geo-trust and ranking risk
2. Add OG tags to all 9 public pages

---

### HAKD (hakd.app) — Next.js

**Pages:** App Router — ~160+ dynamic routes (articles, directory listings, 18 city pages, 7 categories, 126 city×category combos)

| Check | Status | Notes |
|---|---|---|
| Title tags | ✅ Pass | All pages via metadata exports / generateMetadata |
| Meta description | ✅ Pass | All pages |
| Meta keywords | ⚠️ Missing | Not implemented — low priority |
| OG title/description/url | ✅ Pass | All pages |
| **og:image** | ❌ FAIL | **`/public/og-image.png` does not exist** — all OG image code is wired but the actual file is missing — CARRIED OVER |
| Sitemap | ✅ Pass | Dynamic `/app/sitemap.js` — covers all static + DB-driven routes |
| Robots.txt | ✅ Pass | `/app/robots.js` — allows all crawlers including AI bots (GPTBot, ClaudeBot, Perplexity, Amazonbot) |
| Schema markup | ✅ Excellent | WebSite, Person, Article, CollectionPage, FAQPage, BreadcrumbList — comprehensive |
| Broken local links | ✅ Pass | All Next.js routes valid |
| Images | ✅ Pass | CSS-based design; no `<img>` tags |
| Render-blocking | ✅ Pass | ISR caching, preconnected Google Fonts, no blocking scripts |
| **Security** | ⚠️ Warn | ConvertKit API key hardcoded in `/app/api/subscribe/route.js` line 14 — CARRIED OVER |

**Action items (both carried over from 2026-05-10):**
1. Create 1200×630px branded `og-image.png`, save to `/public/`, wire into `/app/layout.js` metadata `images` field
2. Move ConvertKit API key to `CONVERTKIT_API_KEY` env var in Vercel; rotate key in ConvertKit dashboard

---

### InboundAI (inboundai-site-)

**Pages:** 1 page (single-page static HTML, 57 KB) — last code change: 2026-04-03 (44 days ago)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ⚠️ Too long | 203 chars — trim to ~160 |
| Meta keywords | ❌ Missing | Low priority |
| OG tags | ❌ FAIL | **Zero OG tags** — CARRIED OVER (4th consecutive week) |
| Sitemap | ❌ Missing | No sitemap.xml — CARRIED OVER |
| Robots.txt | ❌ Missing | No robots.txt — CARRIED OVER |
| Schema markup | ❌ Missing | **No LocalBusiness or Organization schema** — CARRIED OVER |
| Broken links | ⚠️ One issue | Terms of Service link (line 1118) points to `href="#"` — placeholder, never built — CARRIED OVER |
| Images | ✅ Pass | No images — text/CSS-based |
| Render-blocking | ✅ Pass | Google Fonts preconnected, no external JS |

**Action items (all carried over — site code frozen since April 3):**
1. Add OG tags (title, description, image, url)
2. Add Organization/LocalBusiness JSON-LD schema
3. Create `sitemap.xml` and `robots.txt` (one URL each — ~10 min)
4. Fix or remove the dead Terms of Service `href="#"` link
5. Trim meta description to ≤160 chars

---

## Deploy Queue

**Git log — last 7 days across all repos:**

| Repo | New Commits | Deploy Needed? |
|---|---|---|
| jacksonville-water-damage | None | No |
| nashville-water-damage | None | No |
| cincinnati-water-damage | None | No |
| hakd-site | None | No |
| inboundai-site- | 1 (this report) | Yes — push after commit |

No code changes were deployed to any site this week. All 5 sites are at their previously deployed state. The Cincinnati copy bug fix (Priority #1 for 3 weeks running) and Nashville sitemap update remain uncommitted and undeployed.

---

## Broken Affiliate Links (HAKD)

Manual click-verification still required on all 4 links (same as last week — unconfirmed):

| Link | Occurrences | Risk | Notes |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | 10+ (layout.js, page.js, about, article detail, city/category pages) | ⚠️ HIGH | Netlify subdomain for EMM Assessment — if project is deleted or renamed, ALL CTAs break simultaneously. Migrate to permanent domain ASAP. |
| `https://coach.everfit.io/package/GL583637` | 3 (layout.js, about/page.js, articles/[slug]/page.js) | Medium | Monthly coaching package ($250/mo) — verify still active |
| `https://coach.everfit.io/package/KX912574` | 2 (layout.js, articles/[slug]/page.js) | Medium | Monthly training package ($80/mo) — verify still active |
| `https://calendly.com/christianb3/15-minute-discovery-call` | 2 (layout.js, about/page.js) | Low | Discovery call booking — verify event type is published and accepting bookings |

**None of these were verified last week.** The Netlify subdomain remains the most urgent — a single Netlify project deletion would break 10+ CTAs site-wide.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. (Today: 2026-05-17)

Next full performance summary: **June 1, 2026** — will include:
- Total pages per site
- Sitemap coverage %
- Schema markup coverage %
- New pages added this month (from git log)

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. Fix Cincinnati "Nashville" Copy Bugs — DEPLOY IMMEDIATELY
**Revenue impact:** Rank-and-rent conversion killer — now in its 3rd consecutive week unfixed. A prospect or lead buyer seeing "Nashville" content on a Cincinnati site loses trust instantly and bounces. Google also reads geo-mismatches as a relevance signal and can suppress rankings for the target city. This is a 30-minute fix.

**What to do:** Edit 7 specific lines across `cincinnati-water-damage/index.html` (lines 138, 230, 232, 274, 321), `emergency.html` (line 48), and `styles.css` (line 2). Replace "Nashville" with "Cincinnati". Commit and deploy to Cloudflare Workers.

---

### 2. InboundAI: Add OG Tags + Schema + robots.txt + sitemap.xml
**Revenue impact:** InboundAI is the highest-revenue-potential asset. The site has been code-frozen for 44 days and still has zero schema, no OG tags, no robots.txt, and no sitemap — now in its 4th consecutive week as Priority #2. Every sales prospect who searches for InboundAI before a demo sees an unoptimized result with no social card. These are table-stakes for a SaaS landing page going into demo season.

**What to do:** Add OG meta block to `index.html` `<head>`, add Organization/LocalBusiness JSON-LD, create one-URL `sitemap.xml`, create `robots.txt`, fix or remove the dead `href="#"` Terms of Service link, and trim the meta description to ≤160 chars. Est. 1–2 hours.

---

### 3. Nashville: Add 4 Missing Pages to sitemap.xml
**Revenue impact:** `commercial-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville`, and `hardwood-floor-water-damage-nashville` have FAQPage schema and target high-intent commercial + cost-comparison keywords. They are not in sitemap.xml and may not be signaled to Google for crawling. Adding them is a 15-minute fix that could unlock ranking gains on pages that already exist.

**What to do:** Edit `nashville-water-damage/sitemap.xml`, add 4 `<url>` entries (priority 0.8, changefreq monthly, current lastmod). Commit and deploy to Cloudflare Workers.

---

### 4. HAKD: Create og-image.png + Wire to Layout Metadata
**Revenue impact:** HAKD grows via content sharing on Twitter/X, LinkedIn, and newsletters. Social previews currently show nothing — no og:image on any page and `/public/og-image.png` does not exist. A branded image card increases link click-through rate and positions HAKD content as credible and authoritative when shared. The Next.js code is already wired to use the image; it just doesn't exist yet.

**What to do:** Design a 1200×630px branded HAKD card (dark background, logo, tagline), save to `/public/og-image.png`. Add `images: [{ url: 'https://hakd.app/og-image.png', width: 1200, height: 630 }]` to the root `openGraph` object in `/app/layout.js`. Deploy to Vercel. Est. 2–3 hours including design.

---

### 5. HAKD: Manually Verify All 4 External Links (Affiliate + Booking)
**Revenue impact:** 10+ broken CTAs across HAKD would silently kill conversions from the highest-traffic site in the portfolio. The Netlify EMM Assessment subdomain (`deluxe-moxie-d4016f.netlify.app`) is the most fragile — one project rename or deletion breaks all "Free EMM Assessment" buttons across the entire site. The Everfit coaching packages also need to be confirmed active.

**What to do:** Click all 4 external links in a browser and verify they load and function. If the Netlify subdomain is fragile, migrate the assessment tool to a permanent domain (custom domain on Netlify, or move to Vercel). Est. 30 min verification + 1–2 hrs migration if needed.

---

*Report generated: 2026-05-17 | Audited by Claude Code*
