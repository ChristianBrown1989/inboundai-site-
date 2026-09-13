# Weekly Master Report — 2026-09-13

---

## Site Audit Results

### Jacksonville Water Damage Pros
**Pages:** 11 HTML files (index, emergency, 5 service pages, 3 city pages, thank-you)
**Deployment:** Cloudflare Workers (wrangler.toml)

| Check | Status |
|---|---|
| Title tags | ✅ All 10 indexable pages have titles |
| Meta descriptions | ✅ All 10 indexable pages (thank-you missing, has noindex) |
| Meta keywords | ❌ Missing on all pages (low priority — Google ignores) |
| OG tags (og:title/desc/image/url) | ❌ **MISSING on all 11 pages** |
| sitemap.xml | ✅ Exists, all 10 indexable pages listed |
| robots.txt | ✅ Exists, correct configuration |
| Schema markup | ✅ LocalBusiness + EmergencyService + FAQPage on index.html |
| Broken local links | ✅ None found |
| Page speed | ✅ No render-blocking scripts; no images on site (conversion gap) |

**Schema issues:** `image` property missing from LocalBusiness schema (required for Google rich results). `streetAddress` absent from PostalAddress.

**Internal linking:** `emergency.html` is a near-orphan — only linked from index.html, not from any service/city pages.

**Git log (last 7 days):** No commits.

---

### Nashville Water Damage Pros
**Pages:** 15 HTML files (index, emergency, 7 service pages, 3 city pages, thank-you)
**Deployment:** Cloudflare Workers (wrangler.toml)

| Check | Status |
|---|---|
| Title tags | ✅ All pages present (all exceed 60 chars — phone # in title eating space) |
| Meta descriptions | ✅ Present on 14/15 (thank-you missing, has noindex). 5 pages over 160 chars. |
| Meta keywords | ❌ Missing on all pages |
| OG tags (og:title/desc/image/url) | ❌ **MISSING on all 15 pages** |
| sitemap.xml | ⚠️ **Exists but 4 new pages are MISSING** |
| robots.txt | ✅ Exists, correct configuration |
| Schema markup | ✅ EmergencyService + FAQPage on index.html; 7 inner pages lack any schema |
| Broken local links | ✅ None found |
| Page speed | ✅ No render-blocking scripts; no images on site |

**Critical sitemap gap:** 4 high-value pages added in the last commit are NOT in sitemap.xml:
- `commercial-water-damage-nashville.html`
- `hardwood-floor-water-damage-nashville.html`
- `insurance-claim-water-damage-nashville.html`
- `water-damage-restoration-cost-nashville.html`

These pages will not be reliably crawled or indexed until the sitemap is updated.

**Git log (last 7 days):** No commits.

---

### Cincinnati Water Damage Pros
**Pages:** 10 HTML files (index, emergency, 5 service pages, 2 city pages, thank-you)
**Deployment:** Cloudflare Workers (wrangler.toml)

| Check | Status |
|---|---|
| Title tags | ✅ All pages present (all exceed 60 chars) |
| Meta descriptions | ✅ Present on 9/10 (thank-you missing). 5 pages over 160 chars. |
| Meta keywords | ❌ Missing on all pages |
| OG tags (og:title/desc/image/url) | ❌ **MISSING on all 10 pages** |
| sitemap.xml | ✅ Exists, covers all 9 indexable pages |
| robots.txt | ✅ Exists, correct configuration |
| Schema markup | ✅ EmergencyService + FAQPage on index.html |
| Broken local links | ✅ None found |
| Page speed | ✅ No render-blocking scripts; no images on site |

**🚨 CRITICAL COPY BUG — Nashville text still in Cincinnati site:**
- `index.html` line 138: "60-Minute Response · **Nashville** & Surrounding Areas" (hero badge)
- `index.html` line 230: "Why **Nashville** Trusts Us"
- `index.html` line 232: "treat every **Nashville** homeowner..."
- `index.html` line 274: "We're a **Nashville** company. We live here too..."
- `index.html` line 321: "Real **Nashville** Homeowners" (testimonials heading)
- `emergency.html` H1: "24/7 Emergency Water Damage Response in **Nashville**"

This is actively harming trust (visitors see wrong city), sending mixed location signals to Google, and the emergency page H1 is optimized for Nashville, not Cincinnati.

**Git log (last 7 days):** No commits. Site last updated ~6 months ago (March 2026).

---

### HAKD (hakd.app)
**Pages:** Next.js app — 4 static routes + dynamic article/directory/city/category routes (126+ programmatic SEO pages)
**Deployment:** Vercel (Next.js)

| Check | Status |
|---|---|
| Title tags | ✅ All pages — dynamic generation via metadata exports |
| Meta descriptions | ✅ All pages — dynamic generation |
| Meta keywords | N/A — Next.js App Router does not use keywords meta |
| OG tags (og:title/desc) | ✅ Present on all pages |
| **og:image** | ❌ **MISSING on all pages — /public/og-image.png does not exist** |
| og:url / canonical | ✅ Present on all pages |
| sitemap.xml | ✅ Dynamic via app/sitemap.js |
| robots.txt | ✅ Dynamic via app/robots.js |
| Schema markup | ✅ WebSite, Person, Article, BreadcrumbList, FAQPage, ItemList |
| Broken local links | ❌ **3 broken category links on homepage (→ 404)** |

**🚨 CRITICAL BUG — 3 broken homepage category links:**
In `app/page.js` CATEGORIES array, 3 slugs don't match actual routes:
- `'training'` → should be `'training-science'` (link sends to 404)
- `'wearables'` → should be `'wearables-hrv'` (link sends to 404)
- `'mental'` → should be `'mental-performance'` (link sends to 404)

**🚩 FLAGGED: Primary CTA uses staging/dev URL**
`https://deluxe-moxie-d4016f.netlify.app` appears 10+ times across layout.js, page.js, about/page.js, articles pages, and directory pages as the EMM Assessment CTA link. This is an auto-generated Netlify staging subdomain. If the project is redeployed or deleted, every CTA on the site breaks. Should be replaced with a custom domain (e.g., `assessment.hakd.app`).

**Git log (last 7 days):** No commits.

---

### InboundAI (inboundai site)
**Pages:** 1 HTML file (single-page site, index.html)
**Deployment:** Static (Cloudflare or similar)

| Check | Status |
|---|---|
| Title tag | ✅ Present (62 chars) |
| Meta description | ✅ Present (157 chars) |
| Meta keywords | ❌ Missing |
| OG tags (og:title/desc/image/url) | ❌ **ALL MISSING** |
| sitemap.xml | ❌ **MISSING** |
| robots.txt | ❌ **MISSING** |
| Schema markup | ❌ **NONE** (FAQPage, LocalBusiness/Service opportunities) |
| Broken local links | ⚠️ Terms of Service link is `href="#"` (dead promise) |
| Page speed | ⚠️ Google Fonts stylesheet is render-blocking; missing preconnect to fonts.gstatic.com |

**Biggest missed opportunities:**
- 7 existing FAQ items — zero effort FAQPage schema would generate SERP rich results
- Service/professional schema (phone (832) 281-5911, service type) completely absent
- No OG image means zero visual presence when link is shared

**Git log (last 7 days):** 1 commit — `cc67362 chore: weekly master report 2026-09-06` (last week's report only, no content changes).

---

## Deploy Queue

| Repo | Commits (last 7 days) | Needs Deploy? |
|---|---|---|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 (this report) | Yes — push this report |

No revenue-affecting code changes were deployed to any site in the past 7 days.

---

## Broken Affiliate Links (HAKD)

No classic dead affiliate links found. However, one significant URL issue flagged:

| URL | Occurrences | Status | Action |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | 10+ (layout, home, about, articles, directory) | ⚠️ Staging/dev URL used as primary CTA in production | Replace with custom domain |
| `https://coach.everfit.io/package/GL583637` | 3 (footer, about, article sidebar) | ✅ Appears valid | Verify link is still live |
| `https://coach.everfit.io/package/KX912574` | 2 (footer, article sidebar) | ✅ Appears valid | Verify link is still live |
| `https://calendly.com/christianb3/15-minute-discovery-call` | 2 (footer, about) | ✅ Appears valid | Verify booking availability |

---

## Monthly Summary

Monthly summary scheduled for 1st of month. (Today is 2026-09-13.)

---

## THIS WEEK'S TOP 5 PRIORITIES

**1. 🚨 Fix Cincinnati "Nashville" copy-paste bug** *(Revenue impact: HIGH — rank-and-rent)*
The Cincinnati emergency page H1 and 5 body copy instances say "Nashville." This is actively suppressing Cincinnati rankings, confusing visitors, and undermining the trust signal of a local service business. Fix is a 5-minute find-replace: 6 lines across 2 files. Every day this stays live is a day the site fails to convert Cincinnati visitors.

**2. 🚨 Fix HAKD broken category links on homepage** *(Revenue impact: HIGH — HAKD)*
3 of 7 category navigation links on the hakd.app homepage go to 404 pages. Any visitor clicking Training Science, Wearables/HRV, or Mental Performance immediately hits a dead end. Fix is a 3-line code change in `app/page.js`. Push and redeploy to Vercel.

**3. Add OG tags to all rank-and-rent sites** *(Revenue impact: MEDIUM — all 3 sites)*
Jacksonville, Nashville, and Cincinnati have zero Open Graph tags. Any future paid social campaign, local Facebook ad, or word-of-mouth share produces a blank link preview card. Adding `og:title`, `og:description`, `og:image`, and `og:url` to all pages in all 3 sites takes ~1 hour with a script and dramatically improves click-through on any shared URL.

**4. Update Nashville sitemap + add 4 missing pages** *(Revenue impact: MEDIUM — rank-and-rent)*
4 high-value Nashville pages (cost guide, insurance claims, commercial, hardwood floors) added in the last commit were never added to `sitemap.xml`. Until the sitemap is updated, Google has no reliable signal to crawl or index these pages. Update sitemap.xml, push, and resubmit to Search Console.

**5. Replace HAKD staging URL with custom domain** *(Revenue impact: MEDIUM — HAKD)*
`deluxe-moxie-d4016f.netlify.app` appears as the primary EMM Assessment CTA across 10+ places on hakd.app. A staging URL in production looks unprofessional in link previews, damages trust, and is a single-point-of-failure — if the Netlify project is redeployed, every CTA on the site dies. Add a custom domain to the Netlify project (e.g., `assessment.hakd.app`) and do one find-replace across the codebase.

---

*Report generated: 2026-09-13 | Audited by: Claude Code (automated weekly schedule)*
