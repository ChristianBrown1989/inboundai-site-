# Weekly Master Report — 2026-04-05

---

## Site Audit Results

### Jacksonville (jacksonvillewaterdamagepros.com)

**Pages found:** 11 HTML files (index, burst-pipe, emergency, flood-damage, mold-remediation, orange-park, ponte-vedra, sewage-backup, storm-damage, st-johns, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All local file references valid |
| Title tags | ✅ PASS | Unique titles on all 11 pages |
| Meta description | ✅ PASS | Present on all indexable pages |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url on any page |
| Sitemap | ✅ PASS | 10 URLs, well-formed, all service/location pages included |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ✅ PASS | LocalBusiness + EmergencyService + FAQPage on index.html |
| Image optimization | ✅ N/A | No images on site |
| Render-blocking scripts | ✅ PASS | No external JS, JSON-LD only |

**Action needed:** Add OG tags to all pages.

---

### Nashville (nashvillewaterdamagepros.com)

**Pages found:** 15 HTML files (index, burst-pipe, emergency, basement-flooding, mold-remediation, sewage-backup, storm-damage, brentwood, franklin, murfreesboro, commercial, hardwood-floor, insurance-claim, water-damage-cost, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All local file references valid |
| Title tags | ✅ PASS | Unique titles on all 15 pages |
| Meta description | ✅ PASS | Present on all indexable pages |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No OG tags on any page |
| Sitemap | ⚠️ PARTIAL | 10 URLs listed — missing 4 high-value pages: `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `commercial-water-damage-nashville`, `water-damage-restoration-cost-nashville` |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ✅ PASS | EmergencyService + FAQPage on index; FAQPage on 4 high-value inner pages |
| Image optimization | ✅ N/A | No images on site |
| Render-blocking scripts | ✅ PASS | No external JS |

**Actions needed:** (1) Add OG tags to all pages. (2) Add 4 missing pages to sitemap.xml.

---

### Cincinnati (cincinnatiwaterdamagepros.com)

**Pages found:** 10 HTML files (index, emergency, basement-flooding, blue-ash, burst-pipe, mason, mold-remediation, sewage-backup, storm-damage, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All local file references valid |
| Title tags | ✅ PASS | Unique titles on all 10 pages |
| Meta description | ✅ PASS | Present on 9/10 (thank-you missing, acceptable) |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No OG tags on any page |
| Sitemap | ✅ PASS | 9 URLs, all service/location pages covered |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ✅ PASS | EmergencyService + FAQPage on index.html |
| Image optimization | ✅ N/A | No images on site |
| Render-blocking scripts | ✅ PASS | No external JS |
| Form compatibility | ⚠️ WARNING | Contact form uses `data-netlify="true"` but site is on Cloudflare Workers — form submissions may silently fail |

**Actions needed:** (1) Add OG tags. (2) Verify/fix contact form — either switch to a Cloudflare-compatible form handler or configure Netlify correctly.

---

### HAKD (hakd.app) — Next.js / Vercel

**Routes found:** Dynamic Next.js app — homepage, /about, /articles, /articles/[slug], /articles/category/[category] (7 categories), /directory, /directory/[slug], /directory/category/[category] (7 categories), /directory/city/[city] (18 cities), /directory/city/[city]/[category] (~126 combos). Dynamic sitemap generates 180+ URLs.

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All internal Next.js routes valid |
| Title tags | ✅ PASS | Dynamic metadata on all routes |
| Meta description | ✅ PASS | Present on all routes, including dynamic |
| Meta keywords | ✅ N/A | Next.js metadata API; not required |
| OG tags (title/desc/url) | ✅ PASS | og:title, og:description, og:url on all pages |
| OG image | ❌ CRITICAL | `og:image` NOT configured; `/public/og-image.png` does NOT exist |
| Sitemap | ✅ PASS | Dynamic `app/sitemap.js` covering all routes |
| Robots.txt | ✅ PASS | `app/robots.js` — allows all crawlers including AI bots (Perplexity, GPTBot, ClaudeBot) |
| Schema markup | ✅ EXCELLENT | WebSite + Person on layout; Article, FAQPage, CollectionPage, BreadcrumbList on relevant pages |
| Image optimization | ✅ PASS | Text-first design, no unoptimized images |
| Render-blocking scripts | ✅ PASS | Next.js handles bundling; no blocking issues |
| Public assets | ⚠️ WARNING | `/public/` has only 1 file (Google Search Console verification) — no favicon, no og-image |

**Actions needed:** Create `/public/og-image.png` (1200×630px) and wire `og:image` into `layout.js` metadata.

---

### InboundAI (inboundai-site-)

**Pages found:** 1 HTML file (index.html — single-page app, 57 KB with embedded CSS + JS)
**Deployment status:** ⚠️ BUILT BUT NOT YET DEPLOYED — DEPLOY.md exists with Cloudflare Pages instructions; site not yet live.

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All href/src references valid (Stripe, Calendly, phone, fragments) |
| Title tags | ✅ PASS | `InboundAI — Every Missed Call Is a Job You Didn't Get` |
| Meta description | ✅ PASS | Present, compelling copy |
| Meta keywords | ❌ MISSING | Not present |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url |
| Sitemap | ❌ MISSING | No sitemap.xml exists |
| Robots.txt | ❌ MISSING | No robots.txt exists |
| Schema markup | ❌ MISSING | No JSON-LD schema (no Organization, no FAQPage, no WebSite) |
| Image optimization | ✅ PASS | No images used |
| Render-blocking scripts | ✅ PASS | All JS inline, no external blocking scripts |
| FAQs | ⚠️ OPPORTUNITY | 7 FAQ pairs in HTML — could add FAQPage schema for Featured Snippets |

**Actions needed before deploy:** (1) Add OG tags + og:image. (2) Create sitemap.xml. (3) Create robots.txt. (4) Add Organization + FAQPage JSON-LD schema.

---

## Deploy Queue

Commits in the last 7 days per repo (`git log --since='7 days ago' --oneline`):

| Repo | New Commits | Deploy Needed? |
|------|-------------|---------------|
| jacksonville-water-damage | None | No new changes |
| nashville-water-damage | None | No new changes |
| cincinnati-water-damage | None | No new changes |
| hakd-site | None | No new changes |
| **inboundai-site-** | **3 commits** | **YES — Site built this week, not yet deployed** |

**inboundai-site- commits:**
```
65811b5  Launch InboundAI website + intelligence engine scripts
be799b2  chore: weekly master report 2026-03-29
1ea8ef8  Initialize repository
```

**Deploy action:** Push inboundai-site- to Cloudflare Pages per DEPLOY.md instructions. Resolve pre-deploy checklist items (OG tags, sitemap, robots.txt, schema) before going live.

---

## Broken Affiliate Links (HAKD)

External `href` links found in hakd-site — all scanned:

| URL | Location | Status | Notes |
|-----|----------|--------|-------|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js, page.js, articles/page.js, articles/[slug]/page.js, directory pages, about/page.js (10+ instances) | ⚠️ FLAG | Raw Netlify subdomain (`deluxe-moxie-d4016f`). Used as the EMM Assessment CTA across the entire site. This is the primary revenue-driving CTA. If this URL breaks, all conversions stop. **Strongly recommend migrating to a custom domain (e.g., assess.hakd.app).** |
| `https://coach.everfit.io/package/GL583637` | layout.js (footer), about/page.js, articles/[slug]/page.js | ⚠️ UNVERIFIED | Everfit coaching package link ($250/mo Monthly Coaching). Package IDs are opaque — if package is deleted or changed in Everfit, URL will silently 404. Recommend periodic manual verification. |
| `https://coach.everfit.io/package/KX912574` | layout.js (footer), about/page.js, articles/[slug]/page.js | ⚠️ UNVERIFIED | Everfit training package link ($80/mo Self-Guided Training). Same risk as above. |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js (footer), about/page.js | ✅ LIKELY VALID | Standard Calendly URL format; no indicators of being broken. |
| `https://fonts.googleapis.com` | layout.js (preconnect) | ✅ VALID | Google Fonts infrastructure |

**Summary:** No confirmed 404s (live URL verification not possible without network access), but the raw Netlify subdomain for EMM Assessment is the highest-risk link on the site — it appears on every single page as the primary CTA and is not using a custom/branded domain.

---

## Monthly Summary

Monthly summary scheduled for 1st of month.

*(Today is 2026-04-05 — full performance summary with page counts, sitemap coverage %, schema coverage %, and new pages added will run on 2026-05-01.)*

---

## THIS WEEK'S TOP 5 PRIORITIES

### Ranked by revenue impact:

**1. 🚀 DEPLOY INBOUNDAI SITE — Highest Revenue Priority**
The InboundAI site was built this week (65811b5) and is sitting undeployed. Every day it's not live is a day HVAC and restoration owners can't find it or sign up. Before pushing: add OG tags, create sitemap.xml + robots.txt, and add Organization/FAQPage schema. Then deploy to Cloudflare Pages. This is the top money-making asset.

**2. 🔗 MOVE HAKD EMM ASSESSMENT TO CUSTOM DOMAIN**
The primary CTA across the entire HAKD site points to `https://deluxe-moxie-d4016f.netlify.app` — a raw Netlify subdomain. This is a single point of failure for all HAKD conversions (assessment → coaching funnel). Migrate the EMM app to `assess.hakd.app` or similar, then update all 10+ link instances in the codebase. This protects the HAKD revenue stream.

**3. 🖼️ ADD OG IMAGE TO HAKD**
`/public/og-image.png` does not exist and `og:image` is not configured in metadata. Every social share of any HAKD page (articles, directory listings, about) shows a blank preview. Create a 1200×630px branded image and wire it into `layout.js`. Directly impacts click-through from social/referral traffic to the HAKD audience.

**4. 📋 ADD OG TAGS TO ALL 3 RANK-AND-RENT SITES**
Jacksonville, Nashville, and Cincinnati are all missing all OG tags (`og:title`, `og:description`, `og:image`, `og:url`). When these rank-and-rent sites get shared or cited, social previews are blank. These sites exist to generate leads → leasable revenue. A single batch of OG tag updates across all 3 repos is a quick win.

**5. 🗺️ FIX NASHVILLE SITEMAP + CINCINNATI FORM**
Nashville's sitemap.xml is missing 4 high-value SEO pages: `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `commercial-water-damage-nashville`, `water-damage-restoration-cost-nashville`. These pages exist and are live but Google won't prioritize crawling them. Add them to sitemap.xml and redeploy. Also: verify Cincinnati's contact form actually submits (Netlify form handler on a Cloudflare Workers site may silently fail — this kills lead capture).
