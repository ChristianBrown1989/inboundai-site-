# Weekly Master Report — 2026-08-16

---

## Site Audit Results

### Jacksonville Water Damage Pros

- **Pages:** 11 HTML (10 indexable, 1 thank-you)
- **Meta Title:** ✅ All 10 real pages
- **Meta Description:** ✅ 10/11 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing capability
- **Schema Markup:** ⚠️ 9/11 — missing on `sewage-backup-jacksonville.html` and thank-you
- **Sitemap:** ✅ Exists, covers all 10 real pages
- **Robots.txt:** ✅ Exists, `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None — `index.html#services/#areas/#contact` anchor IDs confirmed present in `index.html`
- **Page Speed:** ✅ No unoptimized images, no render-blocking scripts, no Google Fonts
- **Action Needed:** Add OG tags sitewide + add schema to sewage-backup page

---

### Nashville Water Damage Pros

- **Pages:** 15 HTML (14 indexable, 1 thank-you)
- **Meta Title:** ✅ All 14 real pages
- **Meta Description:** ✅ 14/15 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing capability
- **Schema Markup:** ⚠️ 7/15 with schema — MISSING on 8 pages: `basement-flooding`, `brentwood-water-damage`, `franklin-water-damage`, `mold-remediation-nashville`, `murfreesboro-water-damage`, `sewage-backup-nashville`, `storm-damage-nashville`, `thank-you`
- **Sitemap:** 🔴 **10/14 real pages covered — 4 new pages NOT IN SITEMAP:**
  - `commercial-water-damage-nashville`
  - `hardwood-floor-water-damage-nashville`
  - `insurance-claim-water-damage-nashville`
  - `water-damage-restoration-cost-nashville`
  *(Added in commit `eb87ee0` — Google cannot discover them until sitemap is updated)*
- **Robots.txt:** ✅ Exists, `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None — anchor links confirmed valid
- **Page Speed:** ✅ No unoptimized images, no render-blocking scripts
- **Action Needed:** (1) Add 4 pages to sitemap — HIGH URGENCY. (2) Add OG tags sitewide. (3) Add schema to 8 missing pages.

---

### Cincinnati Water Damage Pros

- **Pages:** 10 HTML (9 indexable, 1 thank-you)
- **Meta Title:** ✅ All 9 real pages
- **Meta Description:** ✅ 9/10 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing capability
- **Schema Markup:** ✅ 9/10 — only thank-you page missing (acceptable)
- **Sitemap:** ✅ Exists, all 9 real pages covered
- **Robots.txt:** ✅ Exists, `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None — anchor links confirmed valid
- **Page Speed:** ✅ No unoptimized images, no render-blocking scripts
- **Action Needed:** Add OG tags sitewide (same template as other sites)

---

### HAKD (hakd.app) — Next.js

- **Meta Title:** ✅ Set in `layout.js`
- **Meta Description:** ✅ Set in `layout.js`
- **Meta Keywords:** ❌ Not set (minor — Google ignores meta keywords; not critical)
- **OG:title / OG:description / OG:url / OG:siteName:** ✅ All set in `layout.js`
- **OG:image:** 🔴 **MISSING** — no `og:image` URL in layout metadata, no `og-image.png` in `/public/`. Social shares show blank thumbnails.
- **Twitter Card:** ✅ `summary_large_image` set (but will be blank without og:image)
- **Schema Markup:** ✅ `WebSite` + `Person` (Christian Brown) JSON-LD in layout
- **Sitemap:** ✅ Dynamic `sitemap.js` (articles + listings + static routes + city pages)
- **Robots.txt:** ✅ `robots.js` — correctly allows AI crawlers (Perplexity, GPTBot, ClaudeBot)
- **Affiliate Links:** ⚠️ Could not verify via curl (network proxy restriction in this session). Links present:
  - `https://deluxe-moxie-d4016f.netlify.app` — EMM Assessment (**generic Netlify subdomain — recommend custom domain**)
  - `https://coach.everfit.io/package/GL583637` — Monthly Coaching
  - `https://coach.everfit.io/package/KX912574` — Monthly Training
  - `https://calendly.com/christianb3/15-minute-discovery-call` — Discovery Call
- **Action Needed:** Create `og-image.png` (1200×630px) → add to `/public/` → add `images` array to `openGraph` config in `layout.js`

---

### InboundAI (inboundai-site-)

- **Pages:** 1 (`index.html`)
- **Meta Title:** ✅ Present — "InboundAI — Every Missed Call Is a Job You Didn't Get"
- **Meta Description:** ✅ Present
- **Meta Keywords:** ❌ Missing
- **OG Tags (all):** 🔴 **COMPLETELY MISSING** — no `og:title`, `og:description`, `og:image`, `og:url`
- **Twitter Card:** 🔴 Missing
- **Schema Markup:** 🔴 Missing — no LocalBusiness, SoftwareApplication, or Organization schema
- **Sitemap:** 🔴 Missing — no `sitemap.xml`
- **Robots.txt:** 🔴 Missing — no `robots.txt`
- **Page Speed:** ⚠️ External Google Fonts loaded without `font-display: swap` or preload hint (minor render delay)
- **Action Needed:** This is the highest-revenue product landing page — add OG tags, schema markup, sitemap.xml, and robots.txt.

---

## Deploy Queue

**Period:** 2026-08-10 through 2026-08-16

| Repo | New Commits (7 days) | Needs Deploy? |
|------|----------------------|---------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 (automated weekly report, 2026-08-09) | No |

**No code deployments required this week.** All repos stable from prior deploys.

> Note: Nashville's 4 new SEO pages are deployed and live. The sitemap.xml gap is a maintenance issue, not a deployment gap.

---

## Broken Affiliate Links (HAKD)

Network-level proxy in this session blocked outbound HTTPS — all curl requests returned `000`. Links could not be confirmed live or dead. **Manual spot-check recommended:**

- `https://coach.everfit.io/package/GL583637` (Monthly Coaching)
- `https://coach.everfit.io/package/KX912574` (Monthly Training)

**Flag:** `https://deluxe-moxie-d4016f.netlify.app` is a generic Netlify project subdomain used as the primary call-to-action URL across the announce bar, nav, hero, and footer. If this is the permanent URL, map a custom subdomain (`assessment.hakd.app`) to it for brand trust.

No confirmed dead links found.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. Full performance report will run on **2026-09-01** covering: total pages per site, sitemap coverage %, schema coverage %, and new pages added per site.

---

## THIS WEEK'S TOP 5 PRIORITIES

*(Ranked by revenue impact)*

### 1. 🔴 Nashville Sitemap — Add 4 Missing High-Value SEO Pages [RANK-AND-RENT]
**Revenue impact: HIGH — these pages are live but invisible to Google.**
Last push (`eb87ee0`) added 4 high-intent pages (cost guide, insurance claims, hardwood floors, commercial) but `sitemap.xml` was not updated. Google cannot discover or index them. Open `nashville-water-damage/sitemap.xml` and add the 4 missing `<url>` blocks. 15-minute fix — deploy immediately.

### 2. 🔴 InboundAI Landing Page — Add OG Tags, Schema, Sitemap, Robots.txt [INBOUNDAI]
**Revenue impact: HIGHEST per dollar — this page sells the highest-ticket service.**
`index.html` is missing all social metadata, structured data, sitemap, and robots.txt. Sharing the URL on social produces a blank preview card. Add a standard OG block, `SoftwareApplication` or `LocalBusiness` schema, `sitemap.xml` (1-page), and `robots.txt`. Estimated effort: 1-2 hours.

### 3. 🟡 OG Tags — Add to All Pages on All 3 Rank-and-Rent Sites [JAX + NASHVILLE + CINCINNATI]
**Revenue impact: MEDIUM — no OG = no social preview on any page across all three sites.**
Every single page on all three sites has zero OG tags. Mirror the existing meta title and description into OG tags, add a shared placeholder OG image URL, and add the canonical URL for each page. Can be batched with a find-and-replace template update per site.

### 4. 🟡 HAKD — Create og:image and Add to layout.js [HAKD]
**Revenue impact: MEDIUM — every HAKD article share and homepage share shows a blank thumbnail.**
Create a 1200×630px branded image (HAKD navy/orange), save as `/public/og-image.png`, and add `images: [{ url: 'https://hakd.app/og-image.png', width: 1200, height: 630 }]` to the `openGraph` export in `app/layout.js`. 30-minute task.

### 5. 🟡 Nashville Schema — Add EmergencyService JSON-LD to 8 Missing Pages [RANK-AND-RENT]
**Revenue impact: MEDIUM — rich snippets improve CTR on high-intent keywords like "sewage backup Nashville".**
Nashville has 8 pages without schema: `basement-flooding`, `brentwood-water-damage`, `franklin-water-damage`, `mold-remediation-nashville`, `murfreesboro-water-damage`, `sewage-backup-nashville`, `storm-damage-nashville`, `thank-you`. Copy the `EmergencyService` JSON-LD block already present on `burst-pipe-nashville.html` or `emergency.html` and adapt the URL field for each page.
