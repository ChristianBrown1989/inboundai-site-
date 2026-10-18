# Weekly Master Report — 2026-10-18

> **Audit status:** All 5 repos audited. No new commits in any repo this past week. Core issues from prior weeks remain unresolved — OG tags, Nashville sitemap gap, and InboundAI missing SEO infrastructure are now in their **4th+ week unaddressed**. Prioritization unchanged; top items need action this week.

---

## Site Audit Results

### Jacksonville Water Damage (`jacksonvillewaterdamagepros.com`)
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ All 11 pages | |
| Meta description | ⚠️ 10/11 pages | `thank-you.html` missing description |
| Meta keywords | ❌ All pages | Zero pages have keywords meta tag |
| OG tags | ❌ All pages | No og:title, og:description, og:image, og:url on any page |
| Sitemap | ⚠️ Partial | 10/11 pages listed; `thank-you` not listed (minor — no SEO value); `index` listed as root `/` |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ✅ | LocalBusiness + EmergencyService schema on index |
| Broken local links | ✅ None | No missing CSS/JS/image file references found |
| Images / lazy loading | ✅ N/A | No `<img>` tags — no lazy-load needed |
| Render-blocking scripts | ✅ None | Only JSON-LD scripts (non-blocking) |

**Outstanding fixes (4+ weeks):**
- Add OG tags to all 11 pages (affects social sharing + CTR)
- Add meta keywords across all pages
- Add meta description to `thank-you.html`

---

### Nashville Water Damage (`nashvillewaterdamagepros.com`)
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ All 15 pages | |
| Meta description | ⚠️ 14/15 pages | `thank-you.html` missing description |
| Meta keywords | ❌ All pages | Zero pages have keywords meta tag |
| OG tags | ❌ All pages | No og:title, og:description, og:image, og:url on any page |
| Sitemap | ❌ Critical gap | **4 content pages still missing:** `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville` (10 of 15 pages listed) |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ✅ | LocalBusiness schema on index |
| Broken local links | ✅ None | No missing local file references |

**Outstanding fixes (4+ weeks):**
- **URGENT: Add 4 missing URLs to sitemap.xml** — these pages likely not indexed by Google
- Add OG tags to all 15 pages
- Add meta keywords across all pages

---

### Cincinnati Water Damage (`cincinnatiwaterdamagepros.com`)
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ All 10 pages | |
| Meta description | ⚠️ 9/10 pages | `thank-you.html` missing description |
| Meta keywords | ❌ All pages | Zero pages have keywords meta tag |
| OG tags | ❌ All pages | No og:title, og:description, og:image, og:url on any page |
| Sitemap | ⚠️ Minor | 9/10 pages listed; `thank-you` not listed (no SEO value) |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ✅ | LocalBusiness schema on index |
| Broken local links | ✅ None | No missing local file references |

**Outstanding fixes (4+ weeks):**
- Add OG tags to all 10 pages
- Add meta keywords across all pages

---

### HAKD (`hakd.app`) — Next.js
| Check | Status | Notes |
|-------|--------|-------|
| Title | ✅ | Set in `app/layout.js` |
| Meta description | ✅ | Set in `app/layout.js` |
| Meta keywords | ⚠️ Minor | Not in layout.js; only set on article slug pages (less critical for Google) |
| OG title/description/url | ✅ | Set in `app/layout.js` openGraph config |
| OG image | ❌ | No `openGraph.images` in layout metadata; no `/public/og-image.png` found |
| Twitter card | ✅ | `summary_large_image` set; no twitter:image specified |
| Sitemap | ✅ | Dynamic via `app/sitemap.js` — pulls articles + listings from Supabase |
| Robots | ✅ | `app/robots.js` — allows all crawlers including AI bots (PerplexityBot, GPTBot, ClaudeBot) |
| Schema markup | ✅ | WebSite + Person schema in layout (appropriate for content site) |
| Page speed | ✅ | No blocking issues found |

**Outstanding fix (4+ weeks):**
- Create `/public/og-image.png` (1200×630px) and add `openGraph.images` to `app/layout.js` — missing OG image means no preview card on social shares from any page

---

### InboundAI (`inboundai.ai`) — Static HTML on Cloudflare Workers
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ | `index.html` has title |
| Meta description | ✅ | `index.html` has description |
| Meta keywords | ❌ | Missing |
| OG tags | ❌ | No og:title, og:description, og:image, og:url on any page |
| Twitter card | ❌ | Missing |
| Sitemap | ❌ | **sitemap.xml does not exist** |
| Robots.txt | ❌ | **robots.txt does not exist** |
| Schema markup | ❌ | No LocalBusiness or Organization/SoftwareApplication schema |
| Images / lazy loading | ✅ N/A | No `<img>` tags found |
| Broken local links | ✅ None | |
| Render-blocking scripts | ⚠️ Minor | Inline `<script>` at line 1128 (no defer/async); Google Fonts loaded via blocking `<link rel="stylesheet">` |

**Outstanding fixes (4+ weeks — all critical for SEO):**
- Add `sitemap.xml`
- Add `robots.txt`
- Add OG + Twitter card meta tags
- Add SoftwareApplication/Organization schema
- Add meta keywords

---

## Deploy Queue

**Git log — past 7 days (since 2026-10-11):**

| Repo | New Commits | Action Needed |
|------|-------------|---------------|
| jacksonville-water-damage | None | No deploy needed |
| nashville-water-damage | None | No deploy needed |
| cincinnati-water-damage | None | No deploy needed |
| hakd-site | None | No deploy needed |
| inboundai-site- | 1 commit (automated report 2026-10-11) | No deploy needed |

**No repos have new content commits requiring deployment this week.**

---

## Broken Affiliate Links (HAKD)

External links found across `hakd-site/app/`:

| URL | Found In | Status | Action |
|-----|----------|--------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js, all page templates | ⚠️ **Suspicious** | Random Netlify subdomain — appears to be a dev/staging URL. Used as the primary CTA (nav, footer, hero) on every page. Verify this is the intended production URL or replace with a custom domain (e.g., `assessment.hakd.app`). |
| `https://coach.everfit.io/package/GL583637` | layout.js, article slug page | Cannot verify (proxy) | Check manually — Monthly Coaching package link |
| `https://coach.everfit.io/package/KX912574` | layout.js, article slug page | Cannot verify (proxy) | Check manually — Monthly Training package link |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js (footer) | Cannot verify (proxy) | Check manually — Discovery Call booking link |

> Note: Outbound HTTPS checks are blocked by the container's network policy. The Netlify subdomain (`deluxe-moxie-d4016f.netlify.app`) remains the highest-risk link — random subdomain format indicates a non-permanent deployment URL. If this link ever goes dead, every CTA on the site fails silently.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. (Next full summary: **2026-11-01**)

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 InboundAI — Add Complete SEO Infrastructure *(Highest Revenue Impact)*
**Revenue reason:** InboundAI is the primary monetization vehicle. Without sitemap.xml, robots.txt, OG tags, and schema, Google cannot reliably crawl or index the site, and every social share generates no preview card — harming the organic funnel. This has been open 4+ weeks.

**Actions (30 min total):**
- Create `inboundai-site-/sitemap.xml` — list `https://inboundai.ai/`
- Create `inboundai-site-/robots.txt` — `Allow: /`, Sitemap reference
- Add `og:title`, `og:description`, `og:image`, `og:url`, `og:type` to `index.html`
- Add `twitter:card`, `twitter:title`, `twitter:description` to `index.html`
- Add `SoftwareApplication` or `Organization` schema to `index.html`
- Add `<meta name="keywords">` to `index.html`

---

### 2. 🔴 Nashville — Fix Sitemap (4 Content Pages Missing = Zero Google Indexing) *(Direct Revenue Loss)*
**Revenue reason:** Four live content pages — commercial jobs, hardwood floors, insurance claims, water damage cost — are not in the sitemap and likely not indexed. These are high-value, high-intent keywords that generate calls. Now 4+ weeks unaddressed.

**Action (5 min):** Add to `nashville-water-damage/sitemap.xml`:
```
https://nashvillewaterdamagepros.com/commercial-water-damage-nashville
https://nashvillewaterdamagepros.com/hardwood-floor-water-damage-nashville
https://nashvillewaterdamagepros.com/insurance-claim-water-damage-nashville
https://nashvillewaterdamagepros.com/water-damage-restoration-cost-nashville
```

---

### 3. 🟠 All 3 Rank-and-Rent Sites — Add OG Tags to Every Page *(CTR + Social Sharing)*
**Revenue reason:** All 36 pages across Jacksonville (11), Nashville (15), and Cincinnati (10) have zero OG tags. Any shared link on Facebook, iMessage, email, or LinkedIn produces no preview card — missed opportunities when contractors share their own pages or you run outreach campaigns. 4+ weeks unaddressed.

**Action:** Add to every HTML page's `<head>`:
```html
<meta property="og:title" content="[page title]">
<meta property="og:description" content="[meta description]">
<meta property="og:image" content="[site-url]/og-image.jpg">
<meta property="og:url" content="[canonical url]">
<meta property="og:type" content="website">
```

---

### 4. 🟡 HAKD — Create OG Image *(Brand + Affiliate + Coaching Revenue)*
**Revenue reason:** HAKD drives coaching + affiliate revenue through article shares. Twitter/LinkedIn/iMessage shares from articles have no image preview. A single branded `og-image.png` fixes all pages at once via Next.js metadata inheritance. 4+ weeks unaddressed.

**Action (20 min):**
- Design 1200×630px branded image → save as `/hakd-site/public/og-image.png`
- Add to `app/layout.js` openGraph config:
  ```js
  images: [{ url: '/og-image.png', width: 1200, height: 630, alt: 'HAKD Performance Intelligence' }]
  ```
- Add same to twitter config: `images: ['/og-image.png']`

---

### 5. 🟡 HAKD — Verify or Replace Assessment Link Domain *(Risk: Broken Conversion Funnel)*
**Revenue reason:** The EMM Assessment at `https://deluxe-moxie-d4016f.netlify.app` is the primary CTA linked in the nav bar, footer, and hero of every HAKD page. A Netlify subdomain with a random identifier is not a stable production URL — if this deployment is deleted or expires, every call-to-action on the site goes dead with no error indicator.

**Action:** Confirm this is the intended production URL. If so, point a custom domain (e.g., `assessment.hakd.app`) at it for link stability, and update `app/layout.js`. If it's a dev URL, migrate to production and update all references.
