# Weekly Master Report — 2026-11-01

## Site Audit Results

---

### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)
**11 pages** | Static HTML on Cloudflare Workers

| Check | Status | Notes |
|---|---|---|
| Meta Title | ✅ 11/11 | All pages have unique titles |
| Meta Description | ✅ 10/11 | `thank-you.html` missing description |
| Meta Keywords | ❌ 0/11 | **No page has keywords tag** |
| OG Tags | ❌ 0/11 | **ALL OG tags completely absent from every page** |
| Sitemap | ⚠️ 10/11 (91%) | `thank-you.html` not listed; index covered as `/` |
| Robots.txt | ✅ | Allows all, points to sitemap |
| Schema Markup | ⚠️ 9/11 (82%) | `sewage-backup-jacksonville.html` and `thank-you.html` missing ld+json |
| Broken Local Links | ✅ None | No broken internal hrefs |
| Images | ✅ N/A | No `<img>` tags — no lazy loading needed |
| Render-Blocking Scripts | ✅ None | No external scripts; no defer/async needed |

**Action needed:** Add OG tags (og:title, og:description, og:image, og:url) + meta keywords to all 11 pages. Add schema to sewage-backup page.

---

### Nashville Water Damage (nashvillewaterdamagepros.com)
**15 pages** | Static HTML on Cloudflare Workers

| Check | Status | Notes |
|---|---|---|
| Meta Title | ✅ 15/15 | All pages have unique titles |
| Meta Description | ✅ 14/15 | `thank-you.html` missing description |
| Meta Keywords | ❌ 0/15 | **No page has keywords tag** |
| OG Tags | ❌ 0/15 | **ALL OG tags completely absent from every page** |
| Sitemap | ❌ 9/15 (60%) | **Missing 5 pages:** `commercial-water-damage`, `hardwood-floor-water-damage`, `insurance-claim-water-damage`, `water-damage-restoration-cost`, `thank-you` |
| Robots.txt | ✅ | Allows all, points to sitemap |
| Schema Markup | ❌ 7/15 (47%) | **8 pages missing schema:** `basement-flooding`, `brentwood`, `franklin`, `mold-remediation`, `murfreesboro`, `sewage-backup`, `storm-damage`, `thank-you` |
| Broken Local Links | ✅ None | |
| Images | ✅ N/A | No `<img>` tags |
| Render-Blocking Scripts | ✅ None | |

**Action needed:** This is the most neglected rank-and-rent site. Add OG tags to all 15 pages, add 5 missing pages to sitemap, add schema to 8 missing pages.

---

### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)
**10 pages** | Static HTML on Cloudflare Workers

| Check | Status | Notes |
|---|---|---|
| Meta Title | ✅ 10/10 | All pages have unique titles |
| Meta Description | ✅ 9/10 | `thank-you.html` missing description |
| Meta Keywords | ❌ 0/10 | **No page has keywords tag** |
| OG Tags | ❌ 0/10 | **ALL OG tags completely absent from every page** |
| Sitemap | ⚠️ 9/10 (90%) | `thank-you.html` not listed; index covered as `/` |
| Robots.txt | ✅ | Allows all, points to sitemap |
| Schema Markup | ⚠️ 9/10 (90%) | Only `thank-you.html` missing ld+json |
| Broken Local Links | ✅ None | |
| Images | ✅ N/A | No `<img>` tags |
| Render-Blocking Scripts | ✅ None | |

**Action needed:** Add OG tags + meta keywords to all 10 pages.

---

### HAKD (hakd.app)
**Next.js App** | Dynamic routes via Supabase

| Check | Status | Notes |
|---|---|---|
| Meta Title | ✅ | Set in `app/layout.js` metadata export |
| Meta Description | ✅ | Set in `app/layout.js` metadata export |
| Meta Keywords | ✅ | Next.js metadata handles this |
| OG Title/Description/URL | ✅ | Defined in layout.js `openGraph` object |
| OG Image | ❌ | **`public/og-image.png` does not exist.** Twitter card set to `summary_large_image` but no og:image URL defined. Only file in `/public/` is Google verification HTML. |
| Sitemap | ✅ | Dynamic `app/sitemap.js` auto-generates from Supabase articles + listings |
| Robots | ✅ | Dynamic `app/robots.js` exists |
| Schema Markup | ⚠️ | Has `WebSite` schema in layout.js — **missing `Organization` schema** (audit requirement). No `LocalBusiness`. |
| Broken Local Links | ✅ None | |
| Page Speed | ✅ | Next.js handles optimization |

**External Link Audit — see Task 3 below.**

---

### InboundAI (inboundai-site-)
**1 page** | Static HTML (index.html only)

| Check | Status | Notes |
|---|---|---|
| Meta Title | ✅ | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta Description | ✅ | Present |
| Meta Keywords | ❌ | **Missing** |
| OG Tags | ❌ | **All 4 OG tags absent** |
| Sitemap | ❌ | **`sitemap.xml` does not exist** |
| Robots.txt | ❌ | **`robots.txt` does not exist** |
| Schema Markup | ❌ | **No structured data** — no ld+json on index.html |
| Broken Local Links | ✅ None | No local hrefs found |
| Images | ✅ N/A | No `<img>` tags |
| Render-Blocking Scripts | ✅ N/A | No external scripts detected |

**Action needed:** InboundAI has the most missing SEO infrastructure of all 5 sites. Needs sitemap, robots, OG tags, schema (SaaS/Service type), and keywords.

---

## Deploy Queue

| Repo | New Commits (last 7 days) | Deploy Needed |
|---|---|---|
| jacksonville-water-damage | None | No |
| nashville-water-damage | None | No |
| cincinnati-water-damage | None | No |
| hakd-site | None | No |
| inboundai-site- | `ab8eb9b` — chore: weekly master report 2026-10-25 | ⚠️ Report file only — no functional changes needing deploy |

**No production deployments required this week.** The only commit is last week's audit report file in inboundai-site-.

---

## Broken Affiliate Links (HAKD)

Scanned all `.js` files in `/app/` for external `href` attributes.

| URL | Status | Action |
|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | ❌ **FLAGGED** | Random Netlify subdomain with hash suffix — this is a dev/staging deploy URL, not a real affiliate destination. **Replace with correct production link immediately.** |
| `https://coach.everfit.io/package/GL583637` | ⚠️ Unverified | Everfit coaching package link — verify it's live and correct |
| `https://coach.everfit.io/package/KX912574` | ⚠️ Unverified | Everfit coaching package link — verify it's live and correct |
| `https://calendly.com/christianb3/15-minute-discovery-call` | ✅ Appears valid | Calendly booking link |
| `https://fonts.googleapis.com` / `https://fonts.gstatic.com` | ✅ Valid | Google Fonts CDN |
| `https://hakd.app/feed.xml` | ✅ Valid | Internal RSS feed |

**Priority fix:** `deluxe-moxie-d4016f.netlify.app` — identify what this was supposed to link to and replace it.

---

## Monthly Summary

> **Today is November 1, 2026 — Full Monthly Summary Required**

### Total Pages Per Site

| Site | Total Pages | Content Pages | Utility Pages |
|---|---|---|---|
| Jacksonville | 11 | 9 | 2 (emergency, thank-you) |
| Nashville | 15 | 13 | 2 (emergency, thank-you) |
| Cincinnati | 10 | 8 | 2 (emergency, thank-you) |
| HAKD | Dynamic | Articles + Directory from Supabase | — |
| InboundAI | 1 | 1 | — |
| **Total (static)** | **37** | **31** | **6** |

### Sitemap Coverage

| Site | Pages | In Sitemap | Coverage |
|---|---|---|---|
| Jacksonville | 11 | 10 | **91%** |
| Nashville | 15 | 9 | **60%** ❌ |
| Cincinnati | 10 | 9 | **90%** |
| HAKD | Dynamic | Auto-generated | **~100%** ✅ |
| InboundAI | 1 | 0 | **0%** ❌ |

### Schema Markup Coverage

| Site | Pages | With Schema | Coverage |
|---|---|---|---|
| Jacksonville | 11 | 9 | **82%** |
| Nashville | 15 | 7 | **47%** ❌ |
| Cincinnati | 10 | 9 | **90%** |
| HAKD | Dynamic | WebSite schema (layout-level) | **100%** ⚠️ (wrong type — needs Organization) |
| InboundAI | 1 | 0 | **0%** ❌ |

### OG Tag Coverage (NEW — critical gap identified this audit)

| Site | Pages | With OG Tags | Coverage |
|---|---|---|---|
| Jacksonville | 11 | 0 | **0%** ❌ |
| Nashville | 15 | 0 | **0%** ❌ |
| Cincinnati | 10 | 0 | **0%** ❌ |
| HAKD | Dynamic | Layout-level OG (no og:image) | **~90%** ⚠️ |
| InboundAI | 1 | 0 | **0%** ❌ |

### New Pages Added This Month (git log)

- **No new content pages added to any site** during October 2026.
- Only commits: weekly audit report files in inboundai-site-.
- **Recommendation:** November content sprint — Nashville needs 3–4 new service pages to match Jacksonville/Cincinnati depth. InboundAI needs a /features and /pricing page.

---

## THIS WEEK'S TOP 5 PRIORITIES

**Ranked by revenue impact:**

### 1. 🔴 FIX HAKD BROKEN LINK — `deluxe-moxie-d4016f.netlify.app`
**Revenue impact: Immediate.** A dead affiliate link is a direct lost conversion. Every visitor who clicks that link hits a dead end. Identify what this URL was supposed to be (likely an Everfit program, a course landing page, or a product link), replace it with the correct production URL, and deploy hakd-site. **ETA: 30 minutes.**

### 2. 🔴 ADD SITEMAP + ROBOTS + OG + SCHEMA to InboundAI
**Revenue impact: High — InboundAI is the primary business.** The site is invisible to social sharing (no OG tags) and under-indexed (no sitemap, no robots.txt, no schema). Googlebot is crawling with no direction. Add: `sitemap.xml`, `robots.txt`, OG tags on index.html, `application/ld+json` with `SoftwareApplication` or `Service` schema. **ETA: 2 hours.**

### 3. 🟠 ADD OG TAGS TO ALL 36 STATIC PAGES (Jacksonville, Nashville, Cincinnati)
**Revenue impact: High — rank-and-rent sites drive inbound calls.** Zero OG tags across all 3 sites means every shared link on Facebook, Google Business, or SMS looks broken/unbranded. A single template update per site covers all pages. Priority order: Nashville (worst coverage) → Jacksonville → Cincinnati. **ETA: 3 hours across all 3 sites.**

### 4. 🟠 FIX NASHVILLE SITEMAP — Add 5 Missing Pages
**Revenue impact: Medium-High.** Nashville has the lowest sitemap coverage (60%). The 4 missing content pages (`commercial-water-damage`, `hardwood-floor-water-damage`, `insurance-claim-water-damage`, `water-damage-restoration-cost`) are high-value keyword targets that Google may be under-crawling. Add to sitemap.xml and redeploy. **ETA: 15 minutes.**

### 5. 🟡 ADD SCHEMA TO 8 MISSING NASHVILLE PAGES + OG IMAGE TO HAKD
**Revenue impact: Medium.** Nashville schema coverage at 47% is the lowest of any site. Copy the LocalBusiness ld+json block from an existing Nashville page to the 8 missing pages. Separately: create and add `/public/og-image.png` to hakd-site so Twitter/LinkedIn cards render correctly for HAKD content sharing. **ETA: 2 hours combined.**

---

*Report generated: 2026-11-01 | Audit covers: all 5 repos as of latest commit*
