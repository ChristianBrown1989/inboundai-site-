# Weekly Master Report — 2026-11-22

## Site Audit Results

### Jacksonville — jacksonvillewaterdamagepros.com
| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | Present on index.html |
| Meta description | ✅ Pass | Present on index.html |
| Meta keywords | ❌ FAIL | Missing on ALL 11 pages |
| OG tags (og:title/desc/image/url) | ❌ FAIL | Missing on ALL 11 pages — zero social preview support |
| Schema markup | ✅ Pass | LocalBusiness + FAQPage on index.html |
| Robots.txt | ✅ Pass | Allows all, links to sitemap |
| Sitemap.xml | ✅ Pass | 10 pages (index.html = "/" included; thank-you intentionally excluded) |
| Broken internal links | ✅ Pass | Anchor links (#areas, #contact, #services) resolve to valid section IDs |
| Images / lazy loading | N/A | No images in codebase |
| Render-blocking scripts | ✅ Pass | No blocking scripts found |

**Action items:** Add OG tags + meta keywords to all 11 pages.

---

### Nashville — nashvillewaterdamagepros.com
| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | Present on index.html |
| Meta description | ✅ Pass | Present on index.html |
| Meta keywords | ❌ FAIL | Missing on ALL 15 pages |
| OG tags (og:title/desc/image/url) | ❌ FAIL | Missing on ALL 15 pages |
| Schema markup | ✅ Pass | EmergencyService + LocalBusiness on index.html |
| Robots.txt | ✅ Pass | Allows all, links to sitemap |
| Sitemap.xml | ⚠️ Partial | 10/14 pages covered (71%). **4 pages missing:** commercial-water-damage-nashville, hardwood-floor-water-damage-nashville, insurance-claim-water-damage-nashville, water-damage-restoration-cost-nashville |
| Broken internal links | ✅ Pass | Anchor links resolve correctly |
| Images / lazy loading | N/A | No images in codebase |
| Render-blocking scripts | ✅ Pass | No blocking scripts found |

**Action items:** (1) Add 4 missing pages to sitemap.xml. (2) Add OG tags + meta keywords to all 15 pages.

---

### Cincinnati — cincinnatiwaterdamagepros.com
| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | Present on index.html |
| Meta description | ✅ Pass | Present on index.html |
| Meta keywords | ❌ FAIL | Missing on ALL 10 pages |
| OG tags (og:title/desc/image/url) | ❌ FAIL | Missing on ALL 10 pages |
| Schema markup | ✅ Pass | EmergencyService + LocalBusiness on index.html |
| Robots.txt | ✅ Pass | Allows all, links to sitemap |
| Sitemap.xml | ✅ Pass | 9/9 real pages covered (100%; thank-you excluded) |
| Broken internal links | ✅ Pass | No broken links found |
| Images / lazy loading | N/A | No images in codebase |
| Render-blocking scripts | ✅ Pass | No blocking scripts found |

**Action items:** Add OG tags + meta keywords to all 10 pages.

---

### HAKD — hakd.app (Next.js)
| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | Configured in layout.js metadata export |
| Meta description | ✅ Pass | Present in layout metadata |
| Meta keywords | N/A | Next.js metadata API (keywords not a standard meta in Next.js 13+) |
| OG title/description/url | ✅ Pass | openGraph block in layout.js |
| OG image (og:image) | ❌ FAIL | No og:image in openGraph config; /public/og-image.png does NOT exist. Twitter card set to `summary_large_image` with no image — broken social previews |
| Schema markup | ✅ Pass | WebSite + Person JSON-LD in layout.js |
| Robots | ✅ Pass | Dynamic robots.js allows all; explicitly whitelists AI crawlers (Perplexity, GPTBot, ClaudeBot) |
| Sitemap | ✅ Pass | Dynamic sitemap.js pulls articles + listings from Supabase |
| Broken affiliate links | ⚠️ SEE BELOW | EMM Assessment URL appears to be a Netlify test deployment |
| Images / lazy loading | ✅ Pass | Next.js Image component handles optimization automatically |

**Action items:** Create and add og:image (minimum 1200×630px) to /public/ and reference it in layout.js openGraph config.

---

### InboundAI — inboundai-site-
| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present and compelling |
| Meta keywords | ❌ FAIL | Missing |
| OG tags (og:title/desc/image/url) | ❌ FAIL | Completely missing — no social preview on any share |
| Schema markup | ❌ FAIL | No JSON-LD schema (no Organization, SoftwareApplication, or LocalBusiness) |
| Robots.txt | ❌ FAIL | File does not exist |
| Sitemap.xml | ❌ FAIL | File does not exist |
| Broken internal links | ✅ Pass | No internal hrefs found |
| Images / lazy loading | N/A | No images in codebase |
| Render-blocking scripts | ✅ Pass | Inline script at end of body, not render-blocking |

**Action items:** Add OG tags, schema markup (SoftwareApplication), robots.txt, and sitemap.xml.

---

## Deploy Queue

| Repo | Commits Last 7 Days | Status |
|---|---|---|
| jacksonville-water-damage | 0 | No deployment needed |
| nashville-water-damage | 0 | No deployment needed |
| cincinnati-water-damage | 0 | No deployment needed |
| hakd-site | 0 | No deployment needed |
| inboundai-site- | 1 (weekly report commit 2026-11-15) | Report commit only — no feature changes |

**No repos require deployment this week.**

---

## Broken Affiliate Links (HAKD)

| URL | Appearances | Status | Risk |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | 12+ (every page via layout.js, homepage, articles, directory) | ⚠️ **SUSPICIOUS** | HIGH — This is a Netlify auto-generated subdomain (`adjective-noun-xxxxxx.netlify.app` format), which is the URL pattern Netlify assigns to test/preview deployments. This is used as the primary EMM Assessment CTA sitewide. Likely should be a custom domain or proper app URL. |
| `https://coach.everfit.io/package/GL583637` | 2 (layout.js, articles/[slug]/page.js) | ⚠️ Could not verify (network proxy) | Medium — verify manually |
| `https://coach.everfit.io/package/KX912574` | 2 (layout.js, articles/[slug]/page.js) | ⚠️ Could not verify (network proxy) | Medium — verify manually |
| `https://calendly.com/christianb3/15-minute-discovery-call` | 2 (layout.js, about/page.js) | ⚠️ Could not verify (network proxy) | Low — Calendly links are typically stable |

**Priority action:** Confirm whether `deluxe-moxie-d4016f.netlify.app` is the intended destination for the EMM Assessment. If it's a placeholder, replace it with the real URL across all 10+ files.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. Next full summary: 2026-12-01.

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 InboundAI — Add Full SEO Infrastructure (Revenue Impact: HIGH)
InboundAI has zero social sharing support, no schema, no robots.txt, and no sitemap. This is a revenue page and the current state means it won't rank or share well. Add: `og:title`, `og:description`, `og:image`, `og:url`, `SoftwareApplication` JSON-LD schema, `robots.txt`, and `sitemap.xml`. Estimated 2–3 hours; could directly increase demo bookings from organic/social traffic.

### 2. 🔴 HAKD — Verify & Replace EMM Assessment URL (Revenue Impact: HIGH)
`deluxe-moxie-d4016f.netlify.app` is used as the primary CTA on every HAKD page (12+ instances in layout.js, homepage, articles, directory). The Netlify auto-generated subdomain format strongly suggests this is a test deployment, not production. If this URL is broken or wrong, every coaching/assessment conversion on HAKD is failing silently. **Check and replace immediately.**

### 3. 🟠 All 3 Rank-and-Rent Sites — Add OG Tags to All Pages (Revenue Impact: MEDIUM-HIGH)
Jacksonville (11 pages), Nashville (15 pages), and Cincinnati (10 pages) all have zero OG tags. Any time a page link is shared — by a lead, in a local Facebook group, via text — there is no preview card. For water damage (emergency, high-intent, often shared between homeowners and neighbors), this matters. Use a shared template to batch-add OG tags efficiently.

### 4. 🟠 Nashville — Add 4 Pages to Sitemap (Revenue Impact: MEDIUM)
`commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, and `water-damage-restoration-cost-nashville` exist as HTML pages but are not in `sitemap.xml`. Google may not discover or prioritize these pages. Insurance claims and commercial damage are high-ticket services — they should be indexed. Quick fix: add 4 `<url>` entries to sitemap.xml.

### 5. 🟡 HAKD — Add og:image (Revenue Impact: MEDIUM)
The Twitter/X card is configured as `summary_large_image` but there is no og:image set and no `/public/og-image.png`. Every HAKD article share on Twitter/X shows a broken image placeholder. Create a 1200×630px branded og-image, place it at `/public/og-image.png`, and add `images: [{ url: '/og-image.png', width: 1200, height: 630 }]` to the openGraph config in `layout.js`.
