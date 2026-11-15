# Weekly Master Report — 2026-11-15

## Site Audit Results

### Jacksonville — jacksonvillewaterdamagepros.com
| Check | Status |
|-------|--------|
| HTML pages | 11 pages |
| Sitemap | ✅ Exists — 10 entries (all non-thank-you pages covered) |
| Robots.txt | ✅ Exists — allows all crawlers |
| Schema markup | ✅ LocalBusiness/Organization on index.html |
| `<title>` tags | ✅ Present on all pages |
| Meta description | ✅ Present on all pages except thank-you.html |
| Meta keywords | ❌ **MISSING on all 11 pages** |
| OG tags (og:title / og:description / og:image / og:url) | ❌ **MISSING on ALL 11 pages** |
| Lazy loading on images | ❌ **Not implemented** |
| Render-blocking scripts | ⚠️ Needs manual review |
| Broken local file links | ✅ No missing local files detected |

---

### Nashville — nashvillewaterdamagepros.com
| Check | Status |
|-------|--------|
| HTML pages | 15 pages |
| Sitemap | ⚠️ **10 entries — 4 pages MISSING from sitemap:** |
| | — commercial-water-damage-nashville.html |
| | — hardwood-floor-water-damage-nashville.html |
| | — insurance-claim-water-damage-nashville.html |
| | — water-damage-restoration-cost-nashville.html |
| Robots.txt | ✅ Exists — allows all crawlers |
| Schema markup | ✅ Present on index.html |
| `<title>` tags | ✅ Present on all pages |
| Meta description | ✅ Present on most pages |
| Meta keywords | ❌ **MISSING on all pages** |
| OG tags (og:title / og:description / og:image / og:url) | ❌ **MISSING on ALL 15 pages** |
| Lazy loading on images | ❌ **Not implemented** |
| Broken local file links | ✅ No missing local files detected |

---

### Cincinnati — cincinnatiwaterdamagepros.com
| Check | Status |
|-------|--------|
| HTML pages | 10 pages |
| Sitemap | ✅ Exists — 9 entries (all non-thank-you pages covered) |
| Robots.txt | ✅ Exists — allows all crawlers |
| Schema markup | ✅ Present on index.html |
| `<title>` tags | ✅ Present on all pages |
| Meta description | ✅ Present on most pages |
| Meta keywords | ❌ **MISSING on all pages** |
| OG tags (og:title / og:description / og:image / og:url) | ❌ **MISSING on ALL 10 pages** |
| Lazy loading on images | ❌ **Not implemented** |
| Broken local file links | ✅ No missing local files detected |

---

### HAKD — hakd.app (Next.js)
| Check | Status |
|-------|--------|
| App directory | ✅ /app directory structure confirmed |
| Sitemap | ✅ Dynamic sitemap.js (Supabase-driven, includes articles + directory listings) |
| Robots.txt | ✅ robots.js — allows all crawlers including AI bots (GPTBot, ClaudeBot, PerplexityBot) |
| Schema markup | ✅ WebSite + Person schema in layout.js |
| OG tags | ✅ og:title, og:description, og:url, og:type in layout.js |
| OG image | ❌ **MISSING — no og-image.png in /public/ directory** — social shares will display blank image |
| Twitter card | ✅ summary_large_image configured |
| Meta keywords | N/A (Next.js metadata API) |
| Lazy loading | ✅ Next.js handles automatically |

---

### InboundAI — inboundai-site-
| Check | Status |
|-------|--------|
| HTML pages | 1 page (single-page site) |
| Sitemap | ❌ **MISSING sitemap.xml** |
| Robots.txt | ❌ **MISSING robots.txt** |
| Schema markup | ❌ **MISSING — no LocalBusiness or Organization schema** |
| `<title>` tag | ✅ Present |
| Meta description | ✅ Present |
| OG tags | ❌ **MISSING all OG tags (og:title, og:description, og:image, og:url)** |
| Lazy loading | ⚠️ Single page — needs image audit |
| External links | Stripe checkout link + Calendly booking link present |

---

## Deploy Queue

Commits in the last 7 days (since 2026-11-08):

| Repo | New Commits | Deploy Needed? |
|------|-------------|----------------|
| jacksonville-water-damage | None | No |
| nashville-water-damage | None | No |
| cincinnati-water-damage | None | No |
| hakd-site | None | No |
| inboundai-site- | 1 commit — `b94e8bf chore: weekly master report 2026-11-08` | No code changes — report file only |

**No repos require deployment this week.** All sites are current with their last deployed state.

---

## Broken Affiliate Links (HAKD)

External links found in `hakd-site/app/`:

| URL | Status |
|-----|--------|
| https://calendly.com/christianb3/15-minute-discovery-call | ✅ Legitimate — Discovery Call |
| https://coach.everfit.io/package/GL583637 | ✅ Legitimate — Monthly Coaching package |
| https://coach.everfit.io/package/KX912574 | ✅ Legitimate — Monthly Training package |
| https://deluxe-moxie-d4016f.netlify.app | ⚠️ **Verify — EMM Assessment tool on hashed Netlify URL** — confirm still live |
| https://fonts.googleapis.com | ✅ Google Fonts CDN |
| https://fonts.gstatic.com | ✅ Google Fonts CDN |

**Action needed:** Manually verify `deluxe-moxie-d4016f.netlify.app` is live and loading correctly. This link appears on the announce bar, nav, and hero CTA — high traffic exposure.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. Next full summary: **2026-12-01**.

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 InboundAI: Add OG tags + sitemap.xml + robots.txt + schema
**Revenue impact: HIGHEST** — InboundAI is the primary revenue-generating product. Missing OG tags means blank/broken social share previews when prospects share the landing page link. Missing sitemap.xml and robots.txt delays Google indexing. Missing LocalBusiness/SoftwareApplication schema means less visibility in AI search tools (Perplexity, ChatGPT).

**Files to update:** `inboundai-site-/index.html` (add `<meta property="og:...">` tags + JSON-LD schema), create `inboundai-site-/sitemap.xml` and `inboundai-site-/robots.txt`.

---

### 2. 🟠 Nashville: Add 4 missing pages to sitemap.xml
**Revenue impact: HIGH** — Four high-value service pages are invisible to Google because they're not in the sitemap: `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville`. These are likely high-intent, high-ticket search terms. Sitemap coverage is currently 67% (10/15 pages).

**File to update:** `nashville-water-damage/sitemap.xml` — add 4 `<url>` entries.

---

### 3. 🟠 All 3 Rank-and-Rent Sites: Add OG tags to every page
**Revenue impact: HIGH** — All 36 pages across Jacksonville (11), Nashville (15), and Cincinnati (10) are completely missing og:title, og:description, og:image, og:url. Affiliate buyers and local partners often share these pages to validate quality. Broken previews damage credibility and reduce click-through from social referrals.

**Approach:** Add OG meta tags to each page's `<head>`. Use the existing `<title>` and `<meta name="description">` values as content. Create a generic og:image (1200×630) for each domain and store in repo.

---

### 4. 🟡 HAKD: Create and add og:image.png
**Revenue impact: MEDIUM** — The layout.js OpenGraph config has no `images` field, and `/public/` has no og-image.png. Every article, directory listing, and page share on X/Twitter and LinkedIn will show a blank image instead of the brand card. This directly hurts article virality and newsletter growth.

**File to create:** `hakd-site/public/og-image.png` (1200×630px HAKD branded card) + add `images: [{ url: '/og-image.png', width: 1200, height: 630 }]` to `openGraph` in `layout.js`.

---

### 5. 🟡 HAKD: Manually verify EMM Assessment link is live
**Revenue impact: MEDIUM** — `deluxe-moxie-d4016f.netlify.app` appears 4+ times across the HAKD site (announce bar, main nav, hero CTA, footer). This is the top-of-funnel lead capture tool. If the Netlify deployment has been paused, suspended, or deleted, all CTAs on the site are broken. Verify the URL loads correctly and the assessment is functional.

---

*Report generated: 2026-11-15 | Next report: 2026-11-22 | Monthly summary: 2026-12-01*
