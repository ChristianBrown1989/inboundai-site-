# Weekly Master Report — 2026-10-11

> **Audit status:** All 5 repos audited. No new commits in any repo this past week. Core issues from prior weeks remain unresolved — OG tags, Nashville sitemap gap, and InboundAI missing SEO infrastructure are now in their **3rd+ week unaddressed**.

---

## Site Audit Results

### Jacksonville Water Damage (`jacksonvillewaterdamagepros.com`)
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ All 11 pages | |
| Meta description | ⚠️ 10/11 pages | `thank-you.html` missing description |
| Meta keywords | ❌ All pages | Zero pages have keywords meta tag |
| OG tags | ❌ All pages | No og:title, og:description, og:image, og:url on any page |
| Sitemap | ⚠️ Partial | `thank-you` not listed (minor — no SEO value) |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ⚠️ 9/11 pages | `sewage-backup-jacksonville.html` and `thank-you.html` missing schema |
| Broken local links | ✅ None found | |
| Images / lazy loading | ✅ N/A | No `<img>` tags on index; no lazy-load needed |
| Render-blocking scripts | ✅ None | |

**Site-level priority fixes:**
- Add OG tags to all 11 pages (affects social sharing + CTR)
- Add meta keywords across all pages
- Add schema to `sewage-backup-jacksonville.html`

---

### Nashville Water Damage (`nashvillewaterdamagepros.com`)
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ All 15 pages | |
| Meta description | ⚠️ 14/15 pages | `thank-you.html` missing description |
| Meta keywords | ❌ All pages | Zero pages have keywords meta tag |
| OG tags | ❌ All pages | No og:title, og:description, og:image, og:url on any page |
| Sitemap | ❌ Critical gap | **4 content pages missing:** `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville` |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ✅ | LocalBusiness schema on index |
| Broken local links | ✅ None found | |

**Site-level priority fixes:**
- **URGENT: Add 4 missing URLs to sitemap.xml** — these pages cannot be indexed by Google
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
| Sitemap | ⚠️ Minor | `thank-you` not listed (minor — no SEO value) |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ✅ | LocalBusiness schema on index |
| Broken local links | ✅ None found | |

**Site-level priority fixes:**
- Add OG tags to all 10 pages
- Add meta keywords across all pages

---

### HAKD (`hakd.app`) — Next.js
| Check | Status | Notes |
|-------|--------|-------|
| Title | ✅ | Set in `app/layout.js` |
| Meta description | ✅ | Set in `app/layout.js` |
| Meta keywords | ⚠️ | Not set in layout.js (less critical for Next.js/Google, but worth adding) |
| OG title/description/url | ✅ | Set in `app/layout.js` openGraph config |
| OG image | ❌ | `og:image` not defined in metadata; no `/public/og-image.png` found |
| Twitter card | ✅ | summary_large_image set |
| Sitemap | ✅ | Dynamic via `app/sitemap.js` pulling from Supabase |
| Robots | ✅ | `app/robots.js` — allows all crawlers including AI bots (Perplexity, GPTBot, ClaudeBot) |
| Schema markup | ✅ | WebSite + Person schema in layout (appropriate for content site) |
| Page speed | ✅ | No blocking issues found |

**Site-level priority fixes:**
- Create `/public/og-image.png` and add `openGraph.images` to `app/layout.js` — missing OG image means no preview card on social shares

---

### InboundAI (`inboundai.ai`) — Static HTML on Cloudflare
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ | Present on index.html |
| Meta description | ✅ | Present on index.html |
| Meta keywords | ❌ | Missing |
| OG tags | ❌ | No og:title, og:description, og:image, og:url |
| Twitter card | ❌ | Missing |
| Sitemap | ❌ | **sitemap.xml does not exist** |
| Robots.txt | ❌ | **robots.txt does not exist** |
| Schema markup | ❌ | No LocalBusiness or Organization schema |
| Images / lazy loading | ✅ N/A | No `<img>` tags found |
| Broken local links | ✅ None | |

**Site-level priority fixes (ALL critical for SEO):**
- Add sitemap.xml
- Add robots.txt
- Add OG + Twitter card meta tags
- Add LocalBusiness or SaaS schema
- Add meta keywords

---

## Deploy Queue

**Git log — past 7 days (since 2026-10-04):**

| Repo | New Commits | Action Needed |
|------|-------------|---------------|
| jacksonville-water-damage | None | No deploy needed |
| nashville-water-damage | None | No deploy needed |
| cincinnati-water-damage | None | No deploy needed |
| hakd-site | None | No deploy needed |
| inboundai-site- | None (last commit was 2026-10-04 automated report) | No deploy needed |

**No repos have new content commits requiring deployment this week.**

---

## Broken Affiliate Links (HAKD)

External links found in `hakd-site/app/`:

| URL | Status | Action |
|-----|--------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | ⚠️ **Suspicious** | Netlify subdomain with random string — this appears to be a dev/staging URL. Verify this is the correct production URL for the EMM Assessment, or replace with a custom domain. |
| `https://coach.everfit.io/package/GL583637` | Cannot verify (proxy) | Monitor manually |
| `https://coach.everfit.io/package/KX912574` | Cannot verify (proxy) | Monitor manually |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Cannot verify (proxy) | Monitor manually |

> Note: Direct URL status checks are blocked by the container proxy. The Netlify subdomain (`deluxe-moxie-d4016f.netlify.app`) is the highest-risk link — it returned 403 Forbidden and the random subdomain format suggests it may be a dev deployment that could be torn down.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. (Next full summary: **2026-11-01**)

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 InboundAI — Add Complete SEO Infrastructure *(Highest Revenue Impact)*
**Revenue reason:** InboundAI is the primary monetization vehicle. Without sitemap.xml, robots.txt, OG tags, and schema, Google cannot reliably crawl or index the site, and social shares produce no preview cards — harming organic funnel performance.

**Actions:**
- Create `sitemap.xml` (list index.html)
- Create `robots.txt` (Allow: /, Sitemap: reference)
- Add og:title, og:description, og:image, og:url, og:type to `index.html`
- Add twitter:card, twitter:title, twitter:description to `index.html`
- Add Organization/SaaS schema to `index.html`
- Add meta keywords to `index.html`

---

### 2. 🔴 Nashville — Fix Sitemap (4 Content Pages Missing = Zero Google Indexing) *(Direct Revenue Loss)*
**Revenue reason:** Four live content pages — commercial jobs, hardwood floors, insurance claims, water damage cost — are not in the sitemap. Google has likely NOT indexed them. These are high-value, high-intent keywords that generate calls.

**Action:** Add to `nashville-water-damage/sitemap.xml`:
```
https://nashvillewaterdamagepros.com/commercial-water-damage-nashville
https://nashvillewaterdamagepros.com/hardwood-floor-water-damage-nashville
https://nashvillewaterdamagepros.com/insurance-claim-water-damage-nashville
https://nashvillewaterdamagepros.com/water-damage-restoration-cost-nashville
```

---

### 3. 🟠 All 3 Rank-and-Rent Sites — Add OG Tags to Every Page *(CTR + Social Sharing)*
**Revenue reason:** All 36 pages across Jacksonville, Nashville, and Cincinnati have zero OG tags. Any link shared on Facebook, iMessage, LinkedIn, or email generates no preview card — missed opportunities when contractors share their own pages or you run link-building campaigns.

**Action:** Add to every HTML page's `<head>`:
```html
<meta property="og:title" content="[page title]">
<meta property="og:description" content="[meta description]">
<meta property="og:image" content="[site-url]/og-image.jpg">
<meta property="og:url" content="[canonical url]">
<meta property="og:type" content="website">
```

---

### 4. 🟡 HAKD — Create OG Image *(Brand + Affiliate Revenue)*
**Revenue reason:** HAKD drives coaching + affiliate revenue. Twitter/LinkedIn/iMessage shares from articles have no preview image. A single branded `og-image.png` (1200×630px) added to `/public/` and referenced in `app/layout.js` fixes all pages at once via Next.js metadata inheritance.

**Action:**
- Design 1200×630px branded OG image → save as `/hakd-site/public/og-image.png`
- Add to `app/layout.js` openGraph config: `images: [{ url: '/og-image.png', width: 1200, height: 630 }]`

---

### 5. 🟡 Verify HAKD Assessment Link Domain *(Risk: Broken Conversion Funnel)*
**Revenue reason:** The EMM Assessment at `https://deluxe-moxie-d4016f.netlify.app` is linked in the nav bar, footer, and CTA of every HAKD page. A Netlify subdomain with a random identifier is not a stable production URL. If this deployment is removed or expires, every call-to-action on the site goes dead.

**Action:** Confirm this is the intended production URL. If so, consider pointing a custom domain (e.g., `assessment.hakd.app`) at it for stability. If it's a dev URL, migrate to production and update all links in `app/layout.js`.
