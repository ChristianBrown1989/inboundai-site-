# Weekly Master Report — 2026-09-06

---

## Site Audit Results

### Jacksonville Water Damage Pros

- **Pages:** 11 HTML (10 indexable, 1 thank-you)
- **Meta Title:** ✅ All 10 real pages
- **Meta Description:** ✅ 10/11 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing preview
- **Twitter Card:** ❌ Missing on ALL pages
- **Schema Markup:** ✅ 2 JSON-LD blocks (LocalBusiness + EmergencyService) on index.html
- **Sitemap:** ✅ 10 real pages covered; thank-you omitted (acceptable)
- **Robots.txt:** ✅ `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None detected
- **Page Speed:** ✅ No `<img>` tags found (CSS backgrounds only); no external render-blocking scripts
- **Status vs Last Week:** No changes — OG tag gap remains unresolved (4th consecutive week)

---

### Nashville Water Damage Pros

- **Pages:** 15 HTML (14 indexable, 1 thank-you)
- **Meta Title:** ✅ All 14 real pages
- **Meta Description:** ✅ 14/15 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing preview
- **Twitter Card:** ❌ Missing on ALL pages
- **Schema Markup:** ✅ 2 JSON-LD blocks on index.html; non-index pages not audited this cycle
- **Sitemap:** 🔴 **10/14 real pages — 4 content pages STILL missing from sitemap (4th consecutive week):**
  - `commercial-water-damage-nashville`
  - `hardwood-floor-water-damage-nashville`
  - `insurance-claim-water-damage-nashville`
  - `water-damage-restoration-cost-nashville`
- **Robots.txt:** ✅ Exists, `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None detected
- **Status vs Last Week:** 🔴 Sitemap fix still NOT completed — now 4 consecutive weeks. These pages are live but invisible to Google.

---

### Cincinnati Water Damage Pros

- **Pages:** 10 HTML (9 indexable, 1 thank-you)
- **Meta Title:** ✅ All 9 real pages
- **Meta Description:** ✅ 9/10 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing preview
- **Twitter Card:** ❌ Missing on ALL pages
- **Schema Markup:** ✅ 2 JSON-LD blocks on index.html
- **Sitemap:** ✅ All 9 real pages covered; thank-you omitted (acceptable)
- **Robots.txt:** ✅ Exists, `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None detected
- **Page Speed:** ✅ No `<img>` tags; no render-blocking external scripts
- **Status vs Last Week:** No changes — OG tag gap remains unresolved (4th consecutive week)

---

### HAKD (hakd.app) — Next.js

- **Meta Title:** ✅ Set in `app/layout.js` metadata export
- **Meta Description:** ✅ Set in `app/layout.js`
- **Meta Keywords:** ❌ Not defined (low priority — Google ignores meta keywords; Next.js doesn't surface them easily)
- **OG:title / OG:description / OG:url / OG:siteName / OG:type:** ✅ All set in `layout.js` metadata
- **OG:image:** 🔴 **MISSING — no `images` array in `openGraph` config; `public/og-image.png` does not exist (4th consecutive week)**
- **Twitter Card:** ⚠️ `summary_large_image` set but no image defined — shows blank thumbnail on all shares
- **Schema Markup:** ✅ `WebSite` + `Person` (Christian Brown) JSON-LD injected in `layout.js`; no `Organization` or `LocalBusiness` (acceptable for personal brand/media site)
- **Sitemap:** ✅ Dynamic `app/sitemap.js` covering static routes, articles, directory listings, and city pages
- **Robots.txt:** ✅ `app/robots.js` — allows all crawlers including AI bots (GPTBot, ClaudeBot, PerplexityBot, Google-Extended)
- **Broken Local Links:** ✅ None
- **Status vs Last Week:** No changes — `og:image` gap remains unresolved (4th consecutive week)

---

### InboundAI (inboundai-site-)

- **Pages:** 1 (`index.html`)
- **Meta Title:** ✅ Present — "InboundAI — Every Missed Call Is a Job You Didn't Get"
- **Meta Description:** ✅ Present
- **Meta Keywords:** ❌ Missing
- **OG Tags (title/desc/image/url):** 🔴 **COMPLETELY MISSING — blank preview on every social share (4th consecutive week)**
- **Twitter Card:** 🔴 Missing
- **Schema Markup:** 🔴 Missing — no `SoftwareApplication`, `Organization`, or `LocalBusiness` JSON-LD
- **Sitemap:** 🔴 Missing — no `sitemap.xml`
- **Robots.txt:** 🔴 Missing — no `robots.txt`
- **Page Speed:** ✅ Google Fonts loaded with `display=swap`; no render-blocking issues
- **Status vs Last Week:** No changes — all critical SEO gaps remain unresolved (4th consecutive week)

---

## Deploy Queue

**Period:** 2026-08-30 through 2026-09-06

| Repo | New Commits (7 days) | Needs Deploy? |
|------|----------------------|---------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 (chore: weekly master report 2026-08-31) | No — report only, no functional changes |

**No code deployments required this week.** All sites stable. Zero new feature commits across all five repos.

---

## Broken Affiliate Links (HAKD)

Full source scan of all files in `hakd-site/app/` completed:

| URL | Location | Status |
|-----|----------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | `layout.js`, `page.js`, `about/page.js` — nav, hero, footer, banners (6+ uses per page) | ⚠️ **STRUCTURAL RISK** — auto-generated Netlify subdomain is the site's #1 CTA for the EMM Assessment. One accidental project deletion breaks every conversion path sitewide. Migrate to `assessment.hakd.app` custom subdomain. |
| `https://coach.everfit.io/package/GL583637` | `layout.js` footer + `about/page.js` | ✅ Valid — Everfit monthly coaching package |
| `https://coach.everfit.io/package/KX912574` | `layout.js` footer | ✅ Valid — Everfit monthly training package |
| `https://calendly.com/christianb3/15-minute-discovery-call` | `layout.js` footer + `about/page.js` | ✅ Valid — Calendly discovery call |

**No confirmed 404s.** Primary risk: the EMM Assessment CTA (`deluxe-moxie-d4016f.netlify.app`) is a randomly-named Netlify subdomain with no custom domain protection — carries over from prior audits as unresolved.

---

## Monthly Summary

Today is **2026-09-06** — not the 1st of the month.

Monthly summary scheduled for **2026-10-01**. Full report on that date will cover:
- Total pages per site
- Sitemap coverage %
- Schema markup coverage %
- New pages added since September 1

*(Note: Sep 1 monthly report was due but this audit cycle fired on Sep 6 — no Oct 1 coverage gap expected.)*

---

## THIS WEEK'S TOP 5 PRIORITIES

*(Ranked by revenue impact — items 1–4 are CARRIED OVER for 4th consecutive week)*

### 1. 🔴 Nashville Sitemap — Add 4 Missing Pages [RANK-AND-RENT] ⚠️ WEEK 4 OUTSTANDING
**Revenue impact: HIGH — these pages are live but Google-invisible for 4 weeks.**

`nashville-water-damage/sitemap.xml` has 10 entries. Four high-intent SEO pages are deployed and receiving traffic but not indexed:
- `commercial-water-damage-nashville`
- `hardwood-floor-water-damage-nashville`
- `insurance-claim-water-damage-nashville`
- `water-damage-restoration-cost-nashville`

**Fix:** Add 4 `<url>` blocks to `sitemap.xml`, push, redeploy to Cloudflare Workers. This is a 15-minute fix. Every additional week = another week of lost crawl budget and indexing.

---

### 2. 🔴 InboundAI Landing Page — OG Tags + Schema + Sitemap + Robots.txt [INBOUNDAI] ⚠️ WEEK 4 OUTSTANDING
**Revenue impact: HIGHEST per unit — this page sells the highest-ticket product and shares blank on every platform.**

Add to `index.html` `<head>`:
```html
<!-- OG Tags -->
<meta property="og:type" content="website">
<meta property="og:title" content="InboundAI — Every Missed Call Is a Job You Didn't Get">
<meta property="og:description" content="InboundAI answers every call 24/7, books the job on the spot, and sends you a text with full details. Built for HVAC and water restoration owners.">
<meta property="og:url" content="https://inboundai.co">
<meta property="og:image" content="https://inboundai.co/og-image.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="InboundAI — Every Missed Call Is a Job You Didn't Get">
<meta name="twitter:description" content="AI answers calls 24/7 and books jobs on the spot. Built for HVAC and water restoration owners.">
<meta name="twitter:image" content="https://inboundai.co/og-image.png">
<!-- Schema -->
<script type="application/ld+json">{"@context":"https://schema.org","@type":"SoftwareApplication","name":"InboundAI","applicationCategory":"BusinessApplication","description":"AI phone answering and job booking for HVAC and water restoration contractors.","url":"https://inboundai.co","offers":{"@type":"Offer","availability":"https://schema.org/InStock"}}</script>
```
Also add `sitemap.xml` and `robots.txt` files to the repo.

---

### 3. 🔴 HAKD — Create og:image and Wire Into layout.js [HAKD] ⚠️ WEEK 4 OUTSTANDING
**Revenue impact: MEDIUM — every article share, homepage share, and directory listing shows a blank thumbnail.**

Create a 1200×630px branded image → save as `/public/og-image.png` → update `app/layout.js`:
```js
openGraph: {
  // ...existing fields,
  images: [{ url: 'https://hakd.app/og-image.png', width: 1200, height: 630, alt: 'HAKD Performance Intelligence' }],
},
twitter: {
  // ...existing fields,
  images: ['https://hakd.app/og-image.png'],
},
```

---

### 4. 🟡 OG Tags — Add to All Pages on All 3 Rank-and-Rent Sites [JAX + NASHVILLE + CINCINNATI] ⚠️ WEEK 4 OUTSTANDING
**Revenue impact: MEDIUM — no OG = blank preview across 30+ combined live URLs, harming referral conversion.**

Template (paste in `<head>`, update title/URL/description per page):
```html
<meta property="og:type" content="website">
<meta property="og:title" content="[Page Title]">
<meta property="og:description" content="[Page Meta Description]">
<meta property="og:url" content="[Canonical URL]">
<meta property="og:image" content="[Shared site-wide OG image URL]">
<meta name="twitter:card" content="summary_large_image">
```

---

### 5. 🟡 HAKD EMM Assessment — Migrate to Custom Subdomain [HAKD]
**Revenue impact: MEDIUM — single point of failure for all HAKD coaching conversions.**

`deluxe-moxie-d4016f.netlify.app` is referenced 6+ times per page as the primary CTA. If the Netlify project is accidentally deleted or renamed, all coaching conversions break instantly.

**Fix:** Configure `assessment.hakd.app` as a custom domain on the Netlify project, then do a find-and-replace across `layout.js`, `page.js`, and `about/page.js` to update all 6+ references. Future-proofs against accidental deletion and improves brand trust.
