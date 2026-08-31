# Weekly Master Report — 2026-08-31

---

## Site Audit Results

### Jacksonville Water Damage Pros

- **Pages:** 11 HTML (10 indexable, 1 thank-you)
- **Meta Title:** ✅ All 10 real pages
- **Meta Description:** ✅ 10/11 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing capability
- **Schema Markup:** ⚠️ 9/10 — `sewage-backup-jacksonville.html` still missing LocalBusiness/EmergencyService JSON-LD
- **Sitemap:** ✅ All 10 real pages covered
- **Robots.txt:** ✅ `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None
- **Page Speed:** ✅ No unoptimized images, no render-blocking scripts, no Google Fonts
- **Status vs Last Week:** No changes — OG tag + schema issues carried over (unresolved)

---

### Nashville Water Damage Pros

- **Pages:** 15 HTML (14 indexable, 1 thank-you)
- **Meta Title:** ✅ All 14 real pages
- **Meta Description:** ✅ 14/15 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing capability
- **Schema Markup:** ⚠️ 7/15 with schema — MISSING on 8 pages: `basement-flooding-nashville`, `brentwood-water-damage`, `franklin-water-damage`, `mold-remediation-nashville`, `murfreesboro-water-damage`, `sewage-backup-nashville`, `storm-damage-nashville`, `thank-you`
- **Sitemap:** 🔴 **STILL 10/14 real pages — 4 pages NOT IN SITEMAP (3rd week outstanding):**
  - `commercial-water-damage-nashville`
  - `hardwood-floor-water-damage-nashville`
  - `insurance-claim-water-damage-nashville`
  - `water-damage-restoration-cost-nashville`
- **Robots.txt:** ✅ Exists, `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None
- **Status vs Last Week:** 🔴 Sitemap fix NOT completed — now entering 3rd consecutive week. These 4 high-intent pages remain unindexable.

---

### Cincinnati Water Damage Pros

- **Pages:** 10 HTML (9 indexable, 1 thank-you)
- **Meta Title:** ✅ All 9 real pages
- **Meta Description:** ✅ 9/10 (thank-you missing — acceptable)
- **Meta Keywords:** ❌ Missing on ALL pages
- **OG Tags (title/desc/image/url):** ❌ Missing on ALL pages — zero social sharing capability
- **Schema Markup:** ✅ 9/10 — only thank-you missing (acceptable)
- **Sitemap:** ✅ All 9 real pages covered
- **Robots.txt:** ✅ Exists, `Allow: /` with sitemap reference
- **Broken Local Links:** ✅ None
- **Page Speed:** ✅ No unoptimized images, no render-blocking scripts
- **Status vs Last Week:** No changes — OG tag issue carried over (unresolved)

---

### HAKD (hakd.app) — Next.js

- **Meta Title:** ✅ Set in `app/layout.js`
- **Meta Description:** ✅ Set in `app/layout.js`
- **Meta Keywords:** ❌ Not set (low priority — Google ignores meta keywords)
- **OG:title / OG:description / OG:url / OG:siteName / OG:type:** ✅ All set in `layout.js`
- **OG:image:** 🔴 **STILL MISSING** — no `images` array in `openGraph` config, no `og-image.png` in `/public/` (3rd week outstanding)
- **Twitter Card:** ✅ `summary_large_image` set (blank without og:image)
- **Schema Markup:** ✅ `WebSite` + `Person` (Christian Brown) JSON-LD in layout
- **Sitemap:** ✅ Dynamic `sitemap.js` covering articles, directory, and static routes
- **Robots.txt:** ✅ `robots.js` — allows all crawlers including AI bots (GPTBot, ClaudeBot, Perplexity)
- **Status vs Last Week:** No changes — og:image fix carried over (unresolved)

---

### InboundAI (inboundai-site-)

- **Pages:** 1 (`index.html`)
- **Meta Title:** ✅ Present
- **Meta Description:** ✅ Present
- **Meta Keywords:** ❌ Missing
- **OG Tags (title/desc/image/url):** 🔴 **COMPLETELY MISSING** — no social share preview on any platform
- **Twitter Card:** 🔴 Missing
- **Schema Markup:** 🔴 Missing — no SoftwareApplication, Organization, or LocalBusiness JSON-LD
- **Sitemap:** 🔴 Missing — no `sitemap.xml`
- **Robots.txt:** 🔴 Missing — no `robots.txt`
- **Page Speed:** ✅ Google Fonts loaded with `display=swap` — no render-blocking issue
- **Status vs Last Week:** No changes — all critical SEO gaps carried over (unresolved)

---

## Deploy Queue

**Period:** 2026-08-24 through 2026-08-31

| Repo | New Commits (7 days) | Needs Deploy? |
|------|----------------------|---------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 0 | No (last commit: 2026-08-23 weekly report, 8 days ago) |

**No code deployments required this week.** All sites stable. No new feature commits on any repo.

---

## Broken Affiliate Links (HAKD)

Full source scan of all `.js`/`.ts`/`.tsx`/`.jsx` files completed this week (grep-based, no outbound requests):

| URL | Location | Status |
|-----|----------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | `layout.js` — announce bar, nav, footer (5+ uses per page) | ⚠️ **RISK** — auto-generated Netlify subdomain is the site's #1 CTA for EMM Assessment. Fragile: one project deletion breaks all conversion paths sitewide. Migrate to `assessment.hakd.app`. |
| `https://coach.everfit.io/package/GL583637` | `layout.js` footer | ✅ Valid (Everfit coaching) |
| `https://coach.everfit.io/package/KX912574` | `layout.js` footer | ✅ Valid (Everfit training) |
| `https://calendly.com/christianb3/15-minute-discovery-call` | `layout.js` footer | ✅ Valid (Calendly) |
| `https://api.convertkit.com/v3/form...` | API route (backend only) | ✅ Backend — not user-facing |
| `https://api.telegram.org/bot...` | API route (backend only) | ✅ Backend template string — not hardcoded |

No confirmed dead links. Primary structural risk: Netlify subdomain fragility for the EMM Assessment CTA.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. Full performance report will run on **2026-09-01** covering: total pages per site, sitemap coverage %, schema coverage %, and new pages added per site.

---

## THIS WEEK'S TOP 5 PRIORITIES

*(Ranked by revenue impact — items 1, 2 & 3 are CARRIED OVER for 3rd consecutive week)*

### 1. 🔴 Nashville Sitemap — Add 4 Missing Pages [RANK-AND-RENT] ⚠️ WEEK 3 OUTSTANDING
**Revenue impact: HIGH — these pages are deployed but invisible to Google for 3 weeks now.**
`nashville-water-damage/sitemap.xml` has 10 entries. Four high-intent SEO pages are live but missing:
- `commercial-water-damage-nashville`
- `hardwood-floor-water-damage-nashville`
- `insurance-claim-water-damage-nashville`
- `water-damage-restoration-cost-nashville`
Add 4 `<url>` blocks, push, redeploy. 15-minute fix. Every day of delay is a day of lost indexing.

### 2. 🔴 InboundAI Landing Page — OG Tags + Schema + Sitemap + Robots.txt [INBOUNDAI] ⚠️ WEEK 3 OUTSTANDING
**Revenue impact: HIGHEST per unit — this page sells the highest-ticket product.**
`index.html` is missing all social metadata, structured data, sitemap.xml, and robots.txt. Social shares show blank preview cards. Required additions:
- `og:title`, `og:description`, `og:image`, `og:url`, `og:type`
- `twitter:card` meta tags
- `SoftwareApplication` or `Organization` JSON-LD schema
- `sitemap.xml` (1 URL)
- `robots.txt` (`User-agent: * / Allow: /`)

### 3. 🟡 HAKD — Create og:image and Wire Into layout.js [HAKD] ⚠️ WEEK 3 OUTSTANDING
**Revenue impact: MEDIUM — every article share and homepage share shows a blank thumbnail.**
Steps: Create 1200×630px branded image → save as `/public/og-image.png` → add to `app/layout.js`:
```js
openGraph: {
  ...existing fields,
  images: [{ url: 'https://hakd.app/og-image.png', width: 1200, height: 630, alt: 'HAKD Performance Intelligence' }],
},
twitter: { ...existing fields, images: ['https://hakd.app/og-image.png'] },
```

### 4. 🟡 OG Tags — Add to All Pages on All 3 Rank-and-Rent Sites [JAX + NASHVILLE + CINCINNATI]
**Revenue impact: MEDIUM — no OG = blank social preview on every page across 30 combined URLs.**
Template for each page (paste in `<head>` after existing meta tags, update URL and title per page):
```html
<meta property="og:type" content="website">
<meta property="og:title" content="[page title]">
<meta property="og:description" content="[page description]">
<meta property="og:url" content="[canonical URL]">
<meta property="og:image" content="[shared OG image URL]">
```

### 5. 🟡 Nashville Schema — Add EmergencyService JSON-LD to 8 Missing Pages [RANK-AND-RENT]
**Revenue impact: MEDIUM — rich snippets lift CTR on high-intent keywords.**
Copy the `EmergencyService` JSON-LD block from `burst-pipe-nashville.html` or `emergency.html` and add (with adapted URL field) to: `basement-flooding-nashville`, `brentwood-water-damage`, `franklin-water-damage`, `mold-remediation-nashville`, `murfreesboro-water-damage`, `sewage-backup-nashville`, `storm-damage-nashville`.
