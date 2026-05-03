# Weekly Master Report — 2026-05-03

---

## Site Audit Results

### Jacksonville Water Damage Pros (jacksonvillewaterdamagepros.com)

**Pages:** 10 content pages — index, emergency, burst-pipe, flood-damage, mold-remediation, orange-park, ponte-vedra, sewage-backup, st-johns, storm-damage — plus thank-you.html

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ | "Water Damage Restoration Jacksonville FL \| 24/7 Emergency \| (904) 792-5162" |
| Meta description | ✅ | Present and descriptive |
| Meta keywords | ❌ | Missing on all pages |
| og:title | ❌ | Missing on all pages |
| og:description | ❌ | Missing on all pages |
| og:image | ❌ | Missing on all pages |
| og:url | ❌ | Missing on all pages |
| robots.txt | ✅ | `Allow: /` — sitemap URL referenced |
| sitemap.xml | ✅ | 10 URLs — 100% content page coverage |
| Schema markup | ✅ | LocalBusiness + EmergencyService + FAQPage on index.html |
| Broken local links | ✅ | All footer hrefs reference existing HTML files |
| Page speed | ✅ | No images, no external JS, single CSS file — minimal risk |

---

### Nashville Water Damage Pros (nashvillewaterdamagepros.com)

**Pages:** 14 content pages — index, emergency, basement-flooding, brentwood, burst-pipe, commercial, franklin, hardwood-floor, insurance-claim, mold-remediation, murfreesboro, sewage-backup, storm-damage, water-damage-restoration-cost — plus thank-you.html

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ | Present |
| Meta description | ✅ | Present |
| Meta keywords | ❌ | Missing on all pages |
| og:title | ❌ | Missing on all pages |
| og:description | ❌ | Missing on all pages |
| og:image | ❌ | Missing on all pages |
| og:url | ❌ | Missing on all pages |
| robots.txt | ✅ | `Allow: /` — sitemap URL referenced |
| sitemap.xml | ⚠️ | 10 URLs but only 71% coverage — 4 pages missing (see below) |
| Schema markup | ✅ | EmergencyService + FAQPage on index.html |
| Broken local links | ✅ | None detected |
| Page speed | ✅ | No images, single CSS, no external JS |

**Sitemap gaps — 4 pages not listed:**
- `/commercial-water-damage-nashville`
- `/hardwood-floor-water-damage-nashville`
- `/insurance-claim-water-damage-nashville`
- `/water-damage-restoration-cost-nashville`

These are likely high-value long-tail pages. Add all 4 to sitemap.xml immediately.

---

### Cincinnati Water Damage Pros (cincinnatiwaterdamagepros.com)

**Pages:** 9 content pages — index, emergency, basement-flooding, blue-ash, burst-pipe, mason, mold-remediation, sewage-backup, storm-damage — plus thank-you.html

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ | Present |
| Meta description | ✅ | Present |
| Meta keywords | ❌ | Missing on all pages |
| og:title | ❌ | Missing on all pages |
| og:description | ❌ | Missing on all pages |
| og:image | ❌ | Missing on all pages |
| og:url | ❌ | Missing on all pages |
| robots.txt | ✅ | `Allow: /` — sitemap URL referenced |
| sitemap.xml | ✅ | 9 URLs — 100% content page coverage |
| Schema markup | ✅ | EmergencyService + FAQPage on index.html |
| Broken local links | ✅ | None detected (footer uses #anchor links) |
| Page speed | ✅ | No images, single CSS, no external JS |

**🚨 CRITICAL — 5 Nashville copy-paste bugs live on Cincinnati site:**

These actively signal geo mismatch to Google's local ranking algorithm and will suppress Cincinnati search rankings.

| Location | Bug | Fix |
|----------|-----|-----|
| Hero badge | "Nashville & Surrounding Areas" | Change to "Cincinnati & Surrounding Areas" |
| Why Us section label | "Why Nashville Trusts Us" | Change to "Why Cincinnati Trusts Us" |
| Locally Owned body copy | "We're a Nashville company. We live here too." | Change to Cincinnati |
| Insurance carrier copy | "every major insurance carrier in Tennessee" | Change to Ohio |
| Testimonials section label | "Real Nashville Homeowners" | Change to "Real Cincinnati Homeowners" |

**🐛 HTML Bug:** Malformed attribute in NAP `<div>` — `"addressLocality": "Cincinnati</span>` is missing the closing double-quote on the attribute value. Browsers will silently handle it but it's invalid HTML that could confuse structured data parsers.

---

### HAKD (hakd.app) — Next.js / Vercel

**Routes:** `/` (home), `/articles`, `/articles/[slug]`, `/articles/category/[slug]`, `/directory`, `/directory/[slug]`, `/directory/category/[slug]`, `/directory/city/[city]`, `/about`

| Check | Status | Notes |
|-------|--------|-------|
| Title | ✅ | Set via Next.js `metadata` export in layout.js |
| Meta description | ✅ | Set |
| og:title | ✅ | Set in layout.js openGraph |
| og:description | ✅ | Set |
| og:url | ✅ | Set to `https://hakd.app` |
| og:image | ❌ | **NOT SET** — `openGraph.images` missing from metadata; no og-image.png in /public |
| Twitter card | ⚠️ | Type set to `summary_large_image` but no `twitter:image` defined |
| robots.js | ✅ | Comprehensive — explicitly allows PerplexityBot, GPTBot, ClaudeBot, Google-Extended |
| sitemap.js | ✅ | Dynamic — pulls articles + listings from Supabase, includes all city/category combos |
| Schema markup | ✅ | WebSite + Person schema via layout.js |
| /public/og-image.png | ❌ | Does not exist — only file in /public is Google Search Console verification |
| Broken internal links | ✅ | All nav and footer internal links correct |

---

### InboundAI (inboundai-site-)

**Pages:** 1 page — index.html only

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ | Present |
| Meta keywords / OG tags / Schema | ❓ | File is 57KB with extensive inline CSS — full head section requires manual verification |
| robots.txt | ❌ | **MISSING** — no robots.txt in repo |
| sitemap.xml | ❌ | **MISSING** — no sitemap.xml in repo |
| Page speed | ⚠️ | Loads Google Fonts via external `<link>` — minor render-blocking risk on slow connections; add `font-display: swap` |

---

## Deploy Queue

`git log --since='7 days ago'` results per repo:

| Repo | New Commits | Deploy Needed? |
|------|-------------|----------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 (this report — 2026-04-26 weekly report) | No new code |

**No repos have pending code changes requiring deployment this week.** The single InboundAI commit was the previous weekly audit report.

---

## Broken Affiliate Links (HAKD)

Live HTTP verification is not available in this environment. The following external links were found in HAKD source files and require manual browser verification this week:

| URL | Location | Risk Level |
|-----|----------|------------|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js + page.js (7+ instances — primary CTA site-wide) | 🔴 HIGH |
| `https://coach.everfit.io/package/GL583637` | layout.js footer ("Monthly Coaching") | 🟡 MEDIUM |
| `https://coach.everfit.io/package/KX912574` | layout.js footer ("Monthly Training") | 🟡 MEDIUM |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js footer | 🟡 MEDIUM |

**Priority flag on Netlify URL:** `deluxe-moxie-d4016f.netlify.app` is a Netlify auto-generated subdomain used as the primary conversion CTA across the entire HAKD site (hero button, EMM banner, about section, nav, footer). If this URL ever goes down or the Netlify project is deleted, the entire HAKD conversion funnel fails silently. Strongly recommended: point a custom subdomain (e.g., `assessment.hakd.app` via CNAME) so you can redirect it without touching code.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. *(Next full summary: June 1, 2026)*

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. [Cincinnati] Fix 5 Nashville copy-paste bugs — Rank-and-Rent
**Revenue impact: HIGH.** Five instances of "Nashville" copy are live on the Cincinnati site right now. Google's local algorithm reads geo signals from on-page text. This actively suppresses Cincinnati rankings and could generate trust issues if a real prospect reads it. Estimated fix time: 15 minutes.

**Files to edit:** `index.html`
- Hero badge: "Nashville & Surrounding Areas" → "Cincinnati & Surrounding Areas"
- Why Us label: "Why Nashville Trusts Us" → "Why Cincinnati Trusts Us"
- Locally Owned copy: "We're a Nashville company" → "We're a Cincinnati company"
- Insurance copy: "in Tennessee" → "in Ohio"
- Testimonials label: "Real Nashville Homeowners" → "Real Cincinnati Homeowners"
- Fix malformed HTML: `"addressLocality": "Cincinnati</span>` (add missing `"`)

---

### 2. [All 3 Water Damage Sites] Add OG tags to every page — Rank-and-Rent
**Revenue impact: HIGH.** Jacksonville, Nashville, and Cincinnati have zero OG tags on any page. Without these, Facebook/Instagram ad link previews render blank, social shares show no image or title, and Google may pull incorrect snippet text. Every lead-gen page needs: `og:title`, `og:description`, `og:image`, `og:url`.

**Files to edit:** All `.html` files across all 3 repos. Add to `<head>`:
```html
<meta property="og:title" content="[Page Title]">
<meta property="og:description" content="[Page Description]">
<meta property="og:image" content="https://[domain]/og-image.jpg">
<meta property="og:url" content="https://[domain]/[page-path]">
<meta property="og:type" content="website">
```

---

### 3. [Nashville] Add 4 missing pages to sitemap.xml — Rank-and-Rent
**Revenue impact: MEDIUM-HIGH.** Four content pages are absent from Nashville's sitemap: `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville`. These are long-tail pages (cost and specialty queries convert at high rates) that Googlebot is not being directed to crawl efficiently. Add them to `sitemap.xml` at priority 0.8.

---

### 4. [HAKD] Create og-image.png + add to layout.js — HAKD
**Revenue impact: MEDIUM.** Every social share of every HAKD page or article currently shows a blank image. Create a branded 1200×630 PNG (place at `/public/og-image.png`) and update `layout.js`:
```js
openGraph: {
  // ... existing fields ...
  images: [{ url: '/og-image.png', width: 1200, height: 630, alt: 'HAKD — Performance Intelligence' }],
},
twitter: {
  // ... existing fields ...
  images: ['/og-image.png'],
},
```
Also manually verify `https://deluxe-moxie-d4016f.netlify.app` is live. If stable, consider adding a custom subdomain alias.

---

### 5. [InboundAI] Add sitemap.xml + robots.txt to inboundai-site- — InboundAI Site
**Revenue impact: MEDIUM.** InboundAI's site has neither file. Google has no structured crawl directive and no sitemap to follow. Add both files to the repo root:

**robots.txt:**
```
User-agent: *
Allow: /

Sitemap: https://[inboundai-domain]/sitemap.xml
```

**sitemap.xml:**
```xml
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://[inboundai-domain]/</loc>
    <changefreq>monthly</changefreq>
    <priority>1.0</priority>
  </url>
</urlset>
```
Also manually verify OG tags and LocalBusiness schema are present in index.html `<head>`.

---

*Report generated: 2026-05-03 | Audited by: Claude Code Weekly Master Audit*
