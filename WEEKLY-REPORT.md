# Weekly Master Report — 2026-04-12

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
| Sitemap | ✅ PASS | 10 URLs, well-formed; thank-you correctly excluded (noindex) — 100% indexable coverage |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ⚠️ PARTIAL | LocalBusiness + EmergencyService + FAQPage on index.html ✅; EmergencyService on 9 service pages ✅; **sewage-backup-jacksonville.html missing schema** ❌ |
| Image optimization | ✅ N/A | No img tags — emoji/SVG/CSS only |
| Render-blocking scripts | ✅ PASS | No external JS; JSON-LD only (non-blocking) |

**Unresolved from last week:** OG tags still missing on all pages. Schema still missing on sewage-backup page.

---

### Nashville (nashvillewaterdamagepros.com)

**Pages found:** 15 HTML files (index, burst-pipe, emergency, basement-flooding, mold-remediation, sewage-backup, storm-damage, brentwood, franklin, murfreesboro, commercial, hardwood-floor, insurance-claim, water-damage-cost, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All local file references valid |
| Title tags | ✅ PASS | Unique titles on all 15 pages |
| Meta description | ✅ PASS | Present on all 15 pages |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No OG tags on any page |
| Sitemap | ❌ CRITICAL | **66.7% coverage (10/15).** Missing 4 high-value SEO pages: `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `commercial-water-damage-nashville`, `water-damage-restoration-cost-nashville` |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ⚠️ PARTIAL | EmergencyService + FAQPage on index ✅; FAQPage on 4 high-value inner pages ✅; **8 pages still missing schema** (basement, brentwood, franklin, mold, murfreesboro, sewage, storm, thank-you) |
| Image optimization | ✅ N/A | No img tags |
| Render-blocking scripts | ✅ PASS | No external JS |

**Unresolved from last week:** Sitemap gap (4 pages) still not fixed. OG tags still missing.

---

### Cincinnati (cincinnatiwaterdamagepros.com)

**Pages found:** 10 HTML files (index, emergency, basement-flooding, blue-ash, burst-pipe, mason, mold-remediation, sewage-backup, storm-damage, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All local file references valid |
| Title tags | ✅ PASS | Unique titles on all 10 pages |
| Meta description | ✅ PASS | Present on 9/10 (thank-you missing — acceptable, noindex) |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url on any page |
| Sitemap | ✅ PASS | 9/9 indexable pages covered — 100% coverage |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ✅ PASS | EmergencyService + FAQPage + AggregateRating (4.9★, 98 reviews) on index.html |
| Image optimization | ✅ N/A | No img tags — SVG data URI only |
| Render-blocking scripts | ✅ PASS | No external JS |
| Form compatibility | ⚠️ WARNING | Contact form uses `data-netlify="true"` but site is on Cloudflare Workers — form submissions may silently fail |

**Unresolved from last week:** OG tags still missing. Netlify form warning on Cloudflare Workers still unresolved.

---

### HAKD (hakd.app) — Next.js / Vercel

**Routes found:** 11 App Router page files — homepage, /about, /articles, /articles/[slug], /articles/category/[category] (7 categories), /directory, /directory/[slug], /directory/category/[category] (7 categories), /directory/city/[city] (18 cities), /directory/city/[city]/[category] (~126 combos). Dynamic sitemap generates 180+ URLs.

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All internal Next.js routes valid |
| Title tags | ✅ PASS | Dynamic metadata via `generateMetadata()` on all routes |
| Meta description | ✅ PASS | Present on all routes including dynamic |
| OG tags (title/desc/url) | ✅ PASS | og:title, og:description, og:url set in root layout + per-page |
| OG image | ❌ CRITICAL | `og:image` NOT configured; `/public/og-image.png` does NOT exist — all social shares show blank preview |
| Sitemap | ✅ PASS | Dynamic `app/sitemap.js` covering all routes |
| Robots.txt | ✅ PASS | `app/robots.js` — allows all crawlers including AI bots (Perplexity, GPTBot, ClaudeBot, Google-Extended) |
| Schema markup | ⚠️ PARTIAL | WebSite + Person on homepage; Article/FAQPage/BreadcrumbList on content pages ✅; **No LocalBusiness or Organization schema** ❌ |
| Image optimization | ✅ PASS | Text-first design; no unoptimized images |
| Render-blocking scripts | ✅ PASS | Next.js handles bundling optimally |
| Public assets | ⚠️ WARNING | `/public/` contains only Google Search Console verification — no favicon, no og-image |

**Unresolved from last week:** og:image still not created. EMM Assessment still on raw Netlify subdomain. Organization schema still missing.

---

### InboundAI (inboundai-site-)

**Pages found:** 1 HTML file (index.html — single-page, 57 KB, embedded CSS + vanilla JS)
**Deployment status:** ⚠️ STILL NOT DEPLOYED — Site built ~3 weeks ago, DEPLOY.md exists with Cloudflare Pages instructions. No live URL yet.

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All href references valid (Stripe checkout, Calendly, phone, fragment anchors) |
| Title tags | ✅ PASS | `InboundAI — Every Missed Call Is a Job You Didn't Get` |
| Meta description | ✅ PASS | Present, compelling copy |
| Meta keywords | ❌ MISSING | Not present |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url |
| Sitemap | ❌ MISSING | No sitemap.xml |
| Robots.txt | ❌ MISSING | No robots.txt |
| Schema markup | ❌ MISSING | No JSON-LD — no Organization, no WebSite, no FAQPage (7 FAQ pairs in HTML with no schema) |
| Image optimization | ✅ N/A | No images used |
| Render-blocking scripts | ✅ PASS | All JS inline at end of body; no external blocking scripts |
| External links | ✅ VALID | `https://calendly.com/inboundai/20min` (×6), `https://buy.stripe.com/...` (Stripe checkout), `tel:+18322815911` — all valid |

**Unresolved from last week:** All 4 pre-deploy items (OG tags, sitemap, robots.txt, schema) remain unresolved. Site still not live.

---

## Deploy Queue

`git log --since='7 days ago' --oneline` results per repo:

| Repo | New Commits (last 7 days) | Deploy Needed? |
|------|--------------------------|----------------|
| jacksonville-water-damage | None | No new changes |
| nashville-water-damage | None | No new changes |
| cincinnati-water-damage | None | No new changes |
| hakd-site | None | No new changes |
| inboundai-site- | `71d8056 chore: weekly master report 2026-04-05` (report only) | ⚠️ Site built but never deployed — deploy pending |

**No new feature commits across any repo this week.** InboundAI remains the only site awaiting initial deployment.

---

## Broken Affiliate Links (HAKD)

Full scan of all external `href` links in hakd-site — no confirmed 404s or dead affiliate links found. All external URLs are legitimate:

| URL | Location | Status |
|-----|----------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js, page.js, 10+ files — **primary CTA across entire site** | ⚠️ RISK: Raw Netlify subdomain — no custom domain. Single point of failure for all HAKD conversions. |
| `https://coach.everfit.io/package/GL583637` | layout.js, about, articles (Monthly Coaching $250/mo) | ⚠️ UNVERIFIED: Package ID opaque — verify manually that link is live |
| `https://coach.everfit.io/package/KX912574` | layout.js, about, articles (Self-Guided Training $80/mo) | ⚠️ UNVERIFIED: Same risk as above |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js, about | ✅ Standard format, likely valid |
| `https://api.convertkit.com/v3/forms/9216083/subscribe` | API route | ✅ ConvertKit newsletter integration |
| `https://fonts.googleapis.com` | layout.js | ✅ Google Fonts CDN |

**No broken affiliate links confirmed. The raw Netlify subdomain for EMM Assessment is the highest-risk link — used as the primary revenue CTA on every page.**

---

## Monthly Summary

Monthly summary scheduled for 1st of month.

*(Today is 2026-04-12 — full performance summary with page counts, sitemap coverage %, schema coverage %, and new pages added will run on 2026-05-01.)*

---

## THIS WEEK'S TOP 5 PRIORITIES

### Ranked by revenue impact:

**1. DEPLOY INBOUNDAI — Highest Revenue Priority**
The InboundAI site has been built for ~3 weeks and is still not live. Every day offline = missed HVAC and water restoration owners who can't find it, can't book a demo, can't subscribe. The pre-deploy checklist items (OG tags, sitemap.xml, robots.txt, Organization + FAQPage JSON-LD schema) are all quick wins — 30–60 minutes of work — and then the site needs to ship to Cloudflare Pages per DEPLOY.md. This is the highest-leverage action across all 5 businesses.

**2. FIX NASHVILLE SITEMAP — 4 High-Value SEO Pages Invisible to Google**
Nashville's sitemap.xml is missing `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `commercial-water-damage-nashville`, and `water-damage-restoration-cost-nashville`. These are the highest-intent, highest-differentiation pages on the site (cost guide, insurance guide, commercial services) and Google is not being directed to crawl them. Fix: add 4 `<url>` entries to sitemap.xml, redeploy. 15-minute fix with real ranking impact.

**3. MOVE HAKD EMM ASSESSMENT TO CUSTOM DOMAIN**
The primary CTA on every HAKD page points to `https://deluxe-moxie-d4016f.netlify.app` — a raw Netlify deploy subdomain. If Netlify changes this URL, rotates the project, or the free tier is disrupted, all HAKD assessment conversions (and the entire coaching funnel) go to zero simultaneously. Migrate to `assess.hakd.app` or `tools.hakd.app`, then do a find-and-replace across the codebase. Protects all HAKD revenue.

**4. ADD OG TAGS TO ALL 5 SITES**
Jacksonville (11 pages), Nashville (15 pages), Cincinnati (10 pages), InboundAI (1 page), and HAKD (og:image missing) are all lacking full Open Graph coverage. This is a pattern-level fix: one template batch across all sites. Without OG tags, social shares and referral previews are blank — directly reducing click-through on any link shares, featured snippets, or AI-generated citations. HAKD specifically needs `og:image` created (1200×630px branded graphic) and wired into `layout.js`.

**5. FIX CINCINNATI FORM + FILL NASHVILLE/JACKSONVILLE SCHEMA GAPS**
Cincinnati's contact form uses `data-netlify="true"` on a Cloudflare Workers site — form submissions are likely silently failing, which kills lead capture on the site. Verify or swap the form handler immediately. Alongside this: add EmergencyService JSON-LD schema to Jacksonville's `sewage-backup-jacksonville.html`, and add LocalBusiness/Service schema to Nashville's 8 pages that are still missing it. Schema gaps suppress rich result eligibility for those pages.
