# Weekly Master Report — 2026-10-25

> **Audit status:** All 5 repos audited. No new commits in any repo this past week. **NEW CRITICAL BUG FOUND THIS WEEK:** Cincinnati's live index.html contains multiple "Nashville" copy/paste errors visible to site visitors and search engines — needs immediate fix. All prior issues now at **5+ weeks unaddressed**.

---

## Site Audit Results

### Jacksonville Water Damage (`jacksonvillewaterdamagepros.com`)
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ All 11 pages | |
| Meta description | ⚠️ 10/11 pages | `thank-you.html` missing description |
| Meta keywords | ❌ All pages | Zero pages have keywords meta tag |
| OG tags | ❌ All pages | No og:title, og:description, og:image, og:url on any page — 5th week unaddressed |
| Sitemap | ✅ | 10/11 pages listed; `thank-you` excluded (correct — no SEO value) |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ✅ | LocalBusiness + EmergencyService + FAQPage schemas on index |
| Broken local links | ✅ None | All HTML files referenced in footer/nav exist |
| Images / lazy loading | ✅ N/A | No `<img>` tags — no lazy-load needed |
| Render-blocking scripts | ✅ None | Only JSON-LD scripts (non-blocking) |

**Outstanding fixes (5+ weeks):**
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
| OG tags | ❌ All pages | No og:title, og:description, og:image, og:url — 5th week unaddressed |
| Sitemap | ❌ Critical gap | **4 content pages still missing:** `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville` (10 of 15 pages listed) — 5th week |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ✅ | EmergencyService + FAQPage schemas on index |
| Broken local links | ✅ None | All referenced files confirmed present |

**Outstanding fixes (5+ weeks):**
- **URGENT: Add 4 missing URLs to sitemap.xml** — these pages are almost certainly not indexed by Google. High-value commercial + insurance + cost keywords generating zero organic traffic.
- Add OG tags to all 15 pages
- Add meta keywords across all pages

---

### Cincinnati Water Damage (`cincinnatiwaterdamagepros.com`)
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ All 10 pages | |
| Meta description | ⚠️ 9/10 pages | `thank-you.html` missing description |
| Meta keywords | ❌ All pages | Zero pages have keywords meta tag |
| OG tags | ❌ All pages | No og:title, og:description, og:image, og:url — 5th week unaddressed |
| Sitemap | ✅ | 9/10 pages listed; `thank-you` excluded (correct) |
| Robots.txt | ✅ | `Allow: /` — crawlers permitted |
| Schema markup | ✅ | EmergencyService + FAQPage schemas on index |
| Broken local links | ✅ None | |
| **🆕 CRITICAL HTML BUG** | ❌ **NEW** | **Multiple "Nashville" references live in Cincinnati index.html** (see below) |

**🚨 NEW CRITICAL BUG — Cincinnati index.html (found this week):**

Three copy/paste errors from the Nashville template are live in production on `cincinnatiwaterdamagepros.com`:

1. **Hero badge:** `⚡ 60-Minute Response · Nashville & Surrounding Areas` (should say Cincinnati)
2. **Section heading:** `Why Nashville Trusts Us` (should say Cincinnati)
3. **Body text:** `treat every Nashville homeowner the way we'd want our own family treated` (should say Cincinnati)
4. **Malformed HTML in NAP microdata:** `<span itemprop="addressLocality": "Cincinnati</span>` — broken attribute syntax (colon after attribute name, missing closing quote). Likely breaks schema parsing.

**Impact:** Visible to site visitors and Google. A visitor who sees "Nashville" on a Cincinnati site loses trust immediately. Google's local ranking signals see conflicting city name. Fix is ~5 minutes.

**Fix needed in `cincinnati-water-damage/index.html`:**
- Line ~hero: Change `Nashville & Surrounding Areas` → `Cincinnati & Surrounding Areas`
- Line ~why-section: Change `Why Nashville Trusts Us` → `Why Cincinnati Trusts Us`
- Line ~why-section: Change `every Nashville homeowner` → `every Cincinnati homeowner`
- Line ~why-section: Change `We're a Nashville company. We live here too.` → `We're a Cincinnati company. We live here too.`
- NAP span: Fix `<span itemprop="addressLocality": "Cincinnati</span>` → `<span itemprop="addressLocality">Cincinnati</span>`

**Outstanding fixes (5+ weeks):**
- Add OG tags to all 10 pages
- Add meta keywords across all pages

---

### HAKD (`hakd.app`) — Next.js
| Check | Status | Notes |
|-------|--------|-------|
| Title | ✅ | Set in `app/layout.js` |
| Meta description | ✅ | Set in `app/layout.js` |
| Meta keywords | ⚠️ Minor | Not in layout.js (less critical for Google) |
| OG title / description / url | ✅ | Set in `app/layout.js` openGraph config |
| OG image | ❌ | No `openGraph.images` in layout metadata; `/public/` only contains Google verification HTML — no `og-image.png` — 5th week |
| Twitter card | ⚠️ | `summary_large_image` type set but no `twitter:image` — image won't show on Twitter/X |
| Sitemap | ✅ | Dynamic via `app/sitemap.js` (pulls from Supabase) |
| Robots | ✅ | `app/robots.js` — allows all crawlers |
| Schema markup | ✅ | WebSite + Person schema in layout (appropriate for content site) |
| Broken affiliate links | ⚠️ | See below |

**Outstanding fix (5+ weeks):**
- Create `/public/og-image.png` (1200×630px) and add `openGraph.images` to `app/layout.js`

---

### InboundAI (`inboundai.ai`) — Static HTML on Cloudflare Workers
| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ | `index.html` has title |
| Meta description | ✅ | `index.html` has description |
| Meta keywords | ❌ | Missing — 5th week |
| OG tags | ❌ | No og:title, og:description, og:image, og:url — 5th week |
| Twitter card | ❌ | Missing — 5th week |
| Sitemap | ❌ | **sitemap.xml does not exist** — 5th week |
| Robots.txt | ❌ | **robots.txt does not exist** — 5th week |
| Schema markup | ❌ | No SoftwareApplication or Organization schema — 5th week |
| Broken local links | ✅ None | |
| Render-blocking scripts | ⚠️ Minor | Inline script + Google Fonts link (blocking) |

**Outstanding fixes (5+ weeks — all critical for SEO):**
- Add `sitemap.xml`
- Add `robots.txt`
- Add OG + Twitter card meta tags
- Add SoftwareApplication/Organization schema
- Add meta keywords

---

## Deploy Queue

**Git log — past 7 days (since 2026-10-18):**

| Repo | New Commits | Action Needed |
|------|-------------|---------------|
| jacksonville-water-damage | None | No deploy needed |
| nashville-water-damage | None | No deploy needed |
| cincinnati-water-damage | None | No deploy needed |
| hakd-site | None | No deploy needed |
| inboundai-site- | 1 commit (automated report 2026-10-18) | No deploy needed |

**No repos have new content commits requiring deployment this week.**

---

## Broken Affiliate Links (HAKD)

External links found across `hakd-site/app/layout.js` and `app/page.js`:

| URL | Found In | Status | Action |
|-----|----------|--------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js (nav CTA, footer, announce bar), page.js (hero, EMM banner, about strip) | ⚠️ **Risk: Random Netlify subdomain** | This is the **primary CTA on every page**. Random subdomain format (`deluxe-moxie-d4016f`) indicates a non-permanent deployment. If this Netlify deployment is deleted, every call-to-action on the site goes dead with no error. Has been flagged 5 weeks. **Action: Point a custom domain (e.g. `assessment.hakd.app`) at this deployment, or migrate to a stable host.** |
| `https://coach.everfit.io/package/GL583637` | layout.js footer (Monthly Coaching) | ⚠️ Cannot verify | Check manually — confirm coaching package still active |
| `https://coach.everfit.io/package/KX912574` | layout.js footer (Monthly Training) | ⚠️ Cannot verify | Check manually — confirm training package still active |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js footer | ⚠️ Cannot verify | Check manually — confirm Calendly link is live |

> **Note:** Outbound HTTPS is restricted in this environment. Cannot auto-verify link status. Manual check recommended for Everfit and Calendly links.

---

## Monthly Summary

Monthly summary scheduled for 1st of month. **(Next full summary: 2026-11-01)**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🚨 Cincinnati — Fix "Nashville" Copy/Paste Errors on Live Site *(Immediate — 5 Minutes)*
**Revenue reason:** A visitor or Google bot reading "Nashville" on a Cincinnati water damage site signals it's the wrong page — both humans and algorithms use this to determine relevance. Hurts local pack rankings and conversion rate. This is the only **new** bug found this week and the only one that's a visible content error.

**Fix in `cincinnati-water-damage/index.html`:**
- Change `Nashville & Surrounding Areas` → `Cincinnati & Surrounding Areas` (hero badge)
- Change `Why Nashville Trusts Us` → `Why Cincinnati Trusts Us` (section label)
- Change `every Nashville homeowner` → `every Cincinnati homeowner` (body text)
- Change `We're a Nashville company.` → `We're a Cincinnati company.` (body text)
- Fix malformed NAP span: `<span itemprop="addressLocality": "Cincinnati</span>` → `<span itemprop="addressLocality">Cincinnati</span>`

Then deploy to Cloudflare Workers.

---

### 2. 🔴 InboundAI — Add Complete SEO Infrastructure *(Highest Long-Term Revenue Impact)*
**Revenue reason:** InboundAI is the primary monetization vehicle. Without sitemap.xml, robots.txt, OG tags, and schema, Google cannot reliably crawl or index the site, and every social share generates no preview card — directly harming the organic funnel. **5th week unaddressed.**

**Actions (30 min total):**
- Create `inboundai-site-/sitemap.xml` — list `https://inboundai.ai/`
- Create `inboundai-site-/robots.txt` — `Allow: /`, Sitemap reference
- Add `og:title`, `og:description`, `og:image`, `og:url`, `og:type` to `index.html`
- Add `twitter:card`, `twitter:title`, `twitter:description` to `index.html`
- Add `SoftwareApplication` or `Organization` schema to `index.html`
- Add `<meta name="keywords">` to `index.html`

---

### 3. 🔴 Nashville — Fix Sitemap (4 Content Pages = Zero Google Traffic) *(Direct Revenue Loss)*
**Revenue reason:** Four live content pages are not in the sitemap and almost certainly not indexed by Google — commercial water damage, hardwood floors, insurance claims, and water damage cost. These are high-value, high-intent commercial keywords generating zero organic traffic. **5th week unaddressed.**

**Action (5 min) — Add to `nashville-water-damage/sitemap.xml`:**
```xml
<url>
  <loc>https://nashvillewaterdamagepros.com/commercial-water-damage-nashville</loc>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
<url>
  <loc>https://nashvillewaterdamagepros.com/hardwood-floor-water-damage-nashville</loc>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
<url>
  <loc>https://nashvillewaterdamagepros.com/insurance-claim-water-damage-nashville</loc>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
<url>
  <loc>https://nashvillewaterdamagepros.com/water-damage-restoration-cost-nashville</loc>
  <changefreq>monthly</changefreq>
  <priority>0.8</priority>
</url>
```
Then deploy to Cloudflare Workers.

---

### 4. 🟠 All 3 Rank-and-Rent Sites — Add OG Tags to Every Page *(CTR + Social Sharing)*
**Revenue reason:** All 36 pages across Jacksonville (11), Nashville (15), and Cincinnati (10) have zero OG tags. Any shared link on Facebook, iMessage, email, or LinkedIn produces no preview card — missed opportunities when contractors share their own pages or you run outreach campaigns. **5th week unaddressed.**

**Action:** Add to every HTML page's `<head>`:
```html
<meta property="og:title" content="[page title]">
<meta property="og:description" content="[meta description]">
<meta property="og:image" content="[site-url]/og-image.jpg">
<meta property="og:url" content="[canonical url]">
<meta property="og:type" content="website">
```

---

### 5. 🟡 HAKD — Create OG Image + Stabilize Assessment Link *(Brand + Affiliate Revenue)*
**Revenue reason:** Two issues block HAKD revenue:
1. **OG image missing** → Article shares on Twitter/LinkedIn/iMessage generate no image card — lower click rates on content meant to drive coaching and affiliate revenue.
2. **Assessment CTA uses random Netlify subdomain** → If that deployment is ever deleted, every CTA on every HAKD page silently breaks.

**Actions:**
- Design 1200×630px branded HAKD image → save as `/hakd-site/public/og-image.png`
- Add to `app/layout.js` openGraph: `images: [{ url: '/og-image.png', width: 1200, height: 630, alt: 'HAKD Performance Intelligence' }]`
- Add to twitter config: `images: ['/og-image.png']`
- Verify `https://deluxe-moxie-d4016f.netlify.app` is still live — if so, immediately point a stable custom domain at it and update all references in `app/layout.js`
