# Weekly Master Report — 2026-04-19

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
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url on any page — **unresolved from last week** |
| Sitemap | ✅ PASS | 10 URLs, well-formed; thank-you correctly excluded (noindex) — 100% indexable coverage |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ⚠️ PARTIAL | LocalBusiness + EmergencyService + FAQPage on index.html ✅; EmergencyService on 9 service pages ✅; **sewage-backup-jacksonville.html still missing schema** ❌ — unresolved from last week |
| Image optimization | ✅ N/A | No img tags — emoji/SVG/CSS only |
| Render-blocking scripts | ✅ PASS | No external JS; JSON-LD only (non-blocking) |

---

### Nashville (nashvillewaterdamagepros.com)

**Pages found:** 15 HTML files (index, burst-pipe, emergency, basement-flooding, mold-remediation, sewage-backup, storm-damage, brentwood, franklin, murfreesboro, commercial, hardwood-floor, insurance-claim, water-damage-cost, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All local file references valid |
| Title tags | ✅ PASS | Unique titles on all 15 pages |
| Meta description | ✅ PASS | Present on all 15 pages |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No OG tags on any page — **unresolved from last week** |
| Sitemap | ❌ CRITICAL | **66.7% coverage (10/15).** Missing: `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `commercial-water-damage-nashville`, `water-damage-restoration-cost-nashville` — **unresolved from last week** |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ⚠️ PARTIAL | EmergencyService + FAQPage on index ✅; inner pages have EmergencyService ✅; some pages still missing schema |
| Image optimization | ✅ N/A | No img tags |
| Render-blocking scripts | ✅ PASS | No external JS |

---

### Cincinnati (cincinnatiwaterdamagepros.com)

**Pages found:** 10 HTML files (index, emergency, basement-flooding, blue-ash, burst-pipe, mason, mold-remediation, sewage-backup, storm-damage, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All local file references valid |
| Title tags | ✅ PASS | Unique titles on all 10 pages |
| Meta description | ✅ PASS | Present on 9/10 (thank-you missing — acceptable, noindex) |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url on any page — **unresolved from last week** |
| Sitemap | ✅ PASS | 9/9 indexable pages covered — 100% coverage |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ✅ PASS | EmergencyService + FAQPage + AggregateRating (4.9★, 98 reviews) on index.html |
| Image optimization | ✅ N/A | No img tags — SVG data URI only |
| Render-blocking scripts | ✅ PASS | No external JS |
| Content accuracy | ⚠️ WARNING | Pages reference "Nashville" in body copy instead of "Cincinnati" (index.html ~lines 138, 230–232) — damages local SEO credibility |
| Form compatibility | ⚠️ WARNING | Contact form uses `data-netlify="true"` but site is on Cloudflare Workers — form submissions may be silently failing |

---

### HAKD (hakd.app) — Next.js / Vercel

**Routes found:** 11 App Router page files — homepage, /about, /articles, /articles/[slug], /articles/category/[category] (7 categories), /directory, /directory/[slug], /directory/category/[category] (7 categories), /directory/city/[city] (18 cities), /directory/city/[city]/[category] (~126 combos). Dynamic sitemap generates 180+ URLs.

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All internal Next.js routes valid |
| Title tags | ✅ PASS | Dynamic metadata via `generateMetadata()` on all routes |
| Meta description | ✅ PASS | Present on all routes including dynamic |
| OG tags (title/desc/url) | ✅ PASS | og:title, og:description, og:url set in root layout + per-page |
| OG image | ❌ CRITICAL | `og:image` NOT configured; `/public/og-image.png` does NOT exist — social shares show blank preview — **unresolved from last week** |
| Sitemap | ✅ PASS | Dynamic `app/sitemap.js` covering all routes |
| Robots.txt | ✅ PASS | `app/robots.js` — allows all crawlers including AI bots (Perplexity, GPTBot, ClaudeBot, Google-Extended) |
| Schema markup | ⚠️ PARTIAL | WebSite + Person on homepage; Article/FAQPage/BreadcrumbList on content pages ✅; **No LocalBusiness or Organization schema on homepage** ❌ |
| Image optimization | ✅ PASS | Text-first design; no unoptimized images |
| Render-blocking scripts | ✅ PASS | Next.js handles bundling optimally |
| Public assets | ⚠️ WARNING | `/public/` contains only Google Search Console verification file — no favicon, no og-image |

---

### InboundAI (inboundai.app)

**Pages found:** 1 HTML file (index.html — single-page, 57 KB, embedded CSS + vanilla JS)
**Deployment status:** ❌ STILL NOT DEPLOYED — Site built ~4 weeks ago, DEPLOY.md exists with Cloudflare Pages instructions. No live URL yet.

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ⚠️ WARNING | Footer "Terms of Service" link uses `href="#"` — no target page or section exists |
| Title tags | ✅ PASS | `InboundAI — Every Missed Call Is a Job You Didn't Get` |
| Meta description | ✅ PASS | Present, compelling 158-character copy |
| Meta keywords | ❌ MISSING | Not present |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url — **unresolved from last week** |
| Sitemap | ❌ MISSING | No sitemap.xml — **unresolved from last week** |
| Robots.txt | ❌ MISSING | No robots.txt — **unresolved from last week** |
| Schema markup | ❌ MISSING | No JSON-LD — no Organization, no WebSite, no FAQPage (7 FAQ pairs in HTML with no structured data) — **unresolved from last week** |
| Image optimization | ✅ N/A | No images used |
| Render-blocking scripts | ✅ PASS | All JS inline at end of body; no external blocking scripts |
| External links | ✅ VALID | `https://calendly.com/inboundai/20min` (×6), `https://buy.stripe.com/...`, `tel:+18322815911` — all valid |

---

## Deploy Queue

`git log --since='7 days ago' --oneline` results per repo:

| Repo | New Commits (last 7 days) | Deploy Needed? |
|------|--------------------------|----------------|
| jacksonville-water-damage | None | No new changes |
| nashville-water-damage | None | No new changes |
| cincinnati-water-damage | None | No new changes |
| hakd-site | None | No new changes |
| inboundai-site- | `d79033f chore: weekly master report 2026-04-12` (report only) | ⚠️ Site built but never deployed — initial Cloudflare Pages deploy pending |

No new feature commits across any repo this week. InboundAI remains the only site awaiting initial deployment.

---

## Broken Affiliate Links (HAKD)

Full scan of all external `href` links in hakd-site:

| URL | Location | Status |
|-----|----------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js, page.js, and 10+ files sitewide — **primary CTA/revenue link across entire site** | ⚠️ HIGH RISK: Raw Netlify auto-generated subdomain (not a custom domain). If the Netlify project is renamed, deleted, or disrupted, all HAKD assessment conversions go to zero simultaneously. Migrate to custom domain immediately. — **unresolved from last week** |
| `https://coach.everfit.io/package/GL583637` | layout.js, about/page.js, articles/[slug]/page.js | ⚠️ UNVERIFIED: Package ID opaque — verify manually that the Everfit listing is still live |
| `https://coach.everfit.io/package/KX912574` | layout.js, articles/[slug]/page.js | ⚠️ UNVERIFIED: Same risk as above |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js, about/page.js | ✅ Standard Calendly format, likely valid |
| `https://api.convertkit.com/v3/forms/9216083/subscribe` | API route (server-side only) | ✅ ConvertKit newsletter integration |
| `https://fonts.googleapis.com` | layout.js | ✅ Google Fonts CDN |

**No confirmed 404s or dead affiliate links.** The Netlify subdomain for the EMM Assessment is the highest-risk link — it is the primary revenue CTA on every single page of the site.

---

## Monthly Summary

Monthly summary scheduled for 1st of month.

*(Today is 2026-04-19 — full performance summary with page counts, sitemap coverage %, schema coverage %, and new pages added will run on 2026-05-01.)*

---

## THIS WEEK'S TOP 5 PRIORITIES

### Ranked by revenue impact:

**1. [InboundAI Pipeline] DEPLOY INBOUNDAI — Do it this week, not next**
The InboundAI site has been fully built for ~4 weeks and is still not live. Every day offline is a missed HVAC and water restoration owner who can't find it, book a demo, or subscribe. The pre-deploy checklist (OG tags, sitemap.xml, robots.txt, Organization + FAQPage JSON-LD, fix Terms of Service link) is 30–60 minutes of work that has carried over two weeks in a row. Complete the checklist in a single commit, then follow DEPLOY.md to publish to Cloudflare Pages. This is the highest-leverage action across all 5 businesses — nothing else matters until the product is live.

**2. [InboundAI Site] Complete the pre-deploy SEO checklist before launch**
All 4 items are quick adds to index.html: (a) add og:title, og:description, og:image, og:url meta tags; (b) create sitemap.xml with a single URL entry; (c) create robots.txt allowing all crawlers; (d) add Organization + FAQPage JSON-LD schema. Without these, launching means a site that can't be crawled properly, won't show social previews, and has no structured data from day one. Fix as a single pre-launch commit alongside fixing the footer Terms of Service `href="#"` broken link.

**3. [Rank-and-Rent] Fix Nashville sitemap — 4 high-value SEO pages still invisible to Google**
Nashville's sitemap.xml is missing `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `commercial-water-damage-nashville`, and `water-damage-restoration-cost-nashville`. These are the highest-intent, highest-differentiation pages on the site — cost guides and insurance guides that capture mid-funnel research traffic — and Google is not being directed to crawl them. This is a 15-minute fix: add 4 `<url>` entries to sitemap.xml, commit, redeploy. Has carried over two weeks.

**4. [Rank-and-Rent] Fix Cincinnati "Nashville" copy error + verify contact form**
Multiple Cincinnati pages reference "Nashville" in body copy (index.html ~lines 138, 230–232). This is a credibility and local SEO signal problem. Fix is a fast find-and-replace. Simultaneously, the Cincinnati contact form uses `data-netlify="true"` on a Cloudflare Workers deployment — lead capture may be silently failing. Verify whether form submissions are being received; if not, swap the form handler to Cloudflare Pages form handling or a Formspree endpoint.

**5. [HAKD] Migrate EMM Assessment off Netlify auto-subdomain**
The primary revenue CTA across every HAKD page links to `https://deluxe-moxie-d4016f.netlify.app` — a raw Netlify-generated subdomain, not a custom domain. One accidental project deletion or Netlify account change and every single HAKD assessment conversion goes dead simultaneously. Migrate the assessment to `assess.hakd.app` or `tools.hakd.app`, do a find-and-replace across the 10+ files that reference it, commit, and redeploy. This is a single-point-of-failure risk sitting on top of the primary coaching funnel.
