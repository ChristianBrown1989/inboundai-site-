# Weekly Master Report — 2026-04-26

---

## Site Audit Results

### Jacksonville (jacksonvillewaterdamagepros.com)

**Pages found:** 11 HTML files (index, burst-pipe, emergency, flood-damage, mold-remediation, orange-park, ponte-vedra, sewage-backup, storm-damage, st-johns, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All local file references valid; footer links point to existing .html files |
| Title tags | ✅ PASS | Unique, keyword-rich titles on all 11 pages |
| Meta description | ✅ PASS | Present on all indexable pages |
| Meta keywords | ❌ MISSING | Absent from all pages — low SEO priority but worth adding |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url on any page — **3rd week unresolved** |
| Sitemap | ✅ PASS | 10 URLs, well-formed; thank-you correctly excluded — 100% indexable coverage |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ✅ PASS | LocalBusiness + EmergencyService + FAQPage (5 Q&As) + AggregateRating on index.html |
| Image optimization | ✅ N/A | No `<img>` tags — emoji/SVG/CSS only |
| Render-blocking scripts | ✅ PASS | No external JS; JSON-LD only (non-blocking) |
| Page speed hints | ✅ CLEAN | Single CSS file, no external fonts, inline SVGs — lean stack |

---

### Nashville (nashvillewaterdamagepros.com)

**Pages found:** 15 HTML files (index, burst-pipe, emergency, basement-flooding, mold-remediation, sewage-backup, storm-damage, brentwood, franklin, murfreesboro, commercial, hardwood-floor, insurance-claim, water-damage-cost, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All footer links use #section anchors — no broken file refs |
| Title tags | ✅ PASS | Unique titles on all 15 pages |
| Meta description | ✅ PASS | Present on all 15 pages |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No OG tags on any page — **3rd week unresolved** |
| Sitemap | ❌ CRITICAL | **71.4% coverage (10/14 indexable pages).** Missing: `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville` — **3rd week unresolved** |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ✅ PASS | EmergencyService + FAQPage (5 Q&As) + AggregateRating on index.html |
| Image optimization | ✅ N/A | No `<img>` tags |
| Render-blocking scripts | ✅ PASS | No external JS or font CDN calls |

---

### Cincinnati (cincinnatiwaterdamagepros.com)

**Pages found:** 10 HTML files (index, emergency, basement-flooding, blue-ash, burst-pipe, mason, mold-remediation, sewage-backup, storm-damage, thank-you)

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All footer links use #section anchors — no broken file refs |
| Title tags | ✅ PASS | Unique, city-specific titles on all 10 pages |
| Meta description | ✅ PASS | Present on all 10 pages |
| Meta keywords | ❌ MISSING | Absent from all pages |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url on any page — **3rd week unresolved** |
| Sitemap | ✅ PASS | 9/9 indexable pages covered — 100% coverage |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap reference present |
| Schema markup | ✅ PASS | EmergencyService + FAQPage (5 Q&As) + AggregateRating (4.9★, 98 reviews) on index.html |
| Image optimization | ✅ N/A | No `<img>` tags |
| Render-blocking scripts | ✅ PASS | No external JS or font CDN calls |
| **Copy errors** | ❌ BUG | index.html contains "Nashville" in 4 places: hero badge ("Nashville & Surrounding Areas"), section label "Why Nashville Trusts Us", body copy "every Nashville homeowner", section label "Real Nashville Homeowners" — all should say **Cincinnati** — **3rd week unresolved** |
| **Malformed HTML** | ❌ NEW | `<span itemprop="addressLocality": "Cincinnati</span>` — colon instead of `=` sign, attribute never closes. Invalid microdata. Fix: `<span itemprop="addressLocality">Cincinnati</span>` |
| **Form handler** | ⚠️ WARNING | Contact form uses `data-netlify="true"` on a Cloudflare Workers deployment — form submissions may be silently dropping. Verify or swap to Formspree. |

---

### HAKD (hakd.app) — Next.js / Vercel

**App Router structure:** homepage, /about, /articles, /articles/[slug], /articles/category/[7 categories], /directory, /directory/[slug], /directory/category/[7 categories], /directory/city/[18 cities], /directory/city/[city]/[category] (~126 combos). Dynamic sitemap.js generates 180+ URLs from Supabase.

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ✅ PASS | All internal Next.js routes valid; dynamic routes resolved via Supabase data |
| Title tags | ✅ PASS | Root metadata + dynamic `generateMetadata()` on all routes |
| Meta description | ✅ PASS | Present on all routes |
| Meta keywords | N/A | Not used in Next.js Metadata API — acceptable for modern SEO |
| OG title / description / url | ✅ PASS | Configured in layout.js `openGraph` object |
| **OG image** | ❌ CRITICAL | `og:image` not set; `/public/og-image.png` does **not exist** (public/ contains only Google Search Console verification file) — social shares show blank preview — **3rd week unresolved** |
| Twitter card | ✅ PARTIAL | `summary_large_image` card configured but no `twitter:image` — same root cause as og:image |
| Sitemap | ✅ PASS | Dynamic `app/sitemap.js` — comprehensive, covers articles + directory + city combos |
| Robots.txt | ✅ PASS | `app/robots.js` — allows all crawlers including AI bots (Perplexity, GPTBot, ClaudeBot, Google-Extended, Amazonbot) |
| Schema markup | ✅ PASS | WebSite schema + Person schema in root layout.js |
| Image optimization | ✅ PASS | Text-first design; Next.js Image component used where applicable |
| Render-blocking | ✅ PASS | Next.js handles bundling; Google Fonts loaded via `link rel="preconnect"` in layout.js |
| Favicon | ⚠️ WARNING | No favicon.ico or apple-touch-icon in `/public/` — browser tabs show blank icon |

---

### InboundAI (inboundai.app)

**Pages found:** 1 HTML file (index.html — single-page, 57 KB, embedded CSS + vanilla JS calculator + FAQ accordion)
**Deployment status:** ❌ **STILL NOT DEPLOYED** — Site has been fully built for 5+ weeks. DEPLOY.md present with Cloudflare Pages instructions. No live URL confirmed.

| Check | Status | Notes |
|-------|--------|-------|
| Broken links | ❌ BUG | Footer "Terms of Service" uses `href="#"` — no target page or `#terms` anchor exists — **3rd week unresolved** |
| Title tag | ✅ PASS | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ PASS | Compelling, benefit-focused, 158 chars |
| Meta keywords | ❌ MISSING | Not present |
| OG tags | ❌ CRITICAL | No og:title, og:description, og:image, og:url — social sharing broken — **3rd week unresolved** |
| Sitemap | ❌ MISSING | No sitemap.xml — **3rd week unresolved** |
| Robots.txt | ❌ MISSING | No robots.txt — **3rd week unresolved** |
| Schema markup | ❌ MISSING | No JSON-LD — 7 FAQ pairs in HTML with zero structured data; no Organization or WebSite schema — **3rd week unresolved** |
| Image optimization | ✅ N/A | No images used |
| Render-blocking | ⚠️ WARNING | Google Fonts loaded via `link rel="stylesheet"` (preconnect present but stylesheet still render-blocks initial paint) — swap to `font-display: swap` via CSS or load asynchronously |
| External links | ✅ PASS | `https://calendly.com/inboundai/20min` (×8), `https://buy.stripe.com/8x2eVe3TP1o5bl93znds400`, `tel:+18322815911` — all structurally valid |

---

## Deploy Queue

`git log --since='7 days ago' --oneline` results:

| Repo | New Commits (Apr 19–26) | Deploy Status |
|------|------------------------|---------------|
| jacksonville-water-damage | **None** | No action needed |
| nashville-water-damage | **None** | No action needed |
| cincinnati-water-damage | **None** | No action needed |
| hakd-site | **None** | No action needed |
| inboundai-site- | `93e1423 chore: weekly master report 2026-04-19` (report file only) | No deploy needed for report commit |

**No feature commits across any repo this week.** All sites are static on their last deployed state. InboundAI remains the only site awaiting initial deployment.

---

## Broken Affiliate Links (HAKD)

Full scan of external `href` links in hakd-site codebase:

| URL | Location | Risk |
|-----|----------|------|
| `https://deluxe-moxie-d4016f.netlify.app` | layout.js nav + footer, page.js hero + banners, articles/[slug] — **primary CTA across entire site** | ⚠️ **HIGH** — Raw auto-generated Netlify subdomain, not a custom domain. One project deletion/rename kills all HAKD assessment conversions. Migrate to `assess.hakd.app` — **3rd week unresolved** |
| `https://coach.everfit.io/package/GL583637` | layout.js footer, about/page.js | ⚠️ **UNVERIFIED** — Verify this Everfit package is still active and live |
| `https://coach.everfit.io/package/KX912574` | layout.js footer, articles/[slug]/page.js | ⚠️ **UNVERIFIED** — Same risk as above; verify manually |
| `https://calendly.com/christianb3/15-minute-discovery-call` | layout.js footer, about/page.js | ✅ Standard Calendly URL format — verify link is still accepting bookings |
| `https://api.convertkit.com/v3/forms/9216083/subscribe` | app/api/newsletter/route.js (server-side POST) | ✅ ConvertKit newsletter integration — server-side only, not a user-facing href |
| `https://fonts.googleapis.com` | layout.js | ✅ Google Fonts CDN |

**No confirmed 404s.** The Netlify subdomain for the EMM Assessment is the single highest-risk link — it is the primary revenue conversion point on every page of the site and has no fallback.

---

## Monthly Summary

Monthly summary scheduled for 1st of month.

*(Today is 2026-04-26 — full performance summary with page counts, sitemap coverage %, schema coverage %, and new pages added will run on 2026-05-01.)*

---

## THIS WEEK'S TOP 5 PRIORITIES

### Ranked by revenue impact:

---

**1. [InboundAI Pipeline] DEPLOY INBOUNDAI — Now 5+ weeks offline, immediate action required**

The site is fully built and has been sitting in a repo for over a month. Every week this stays undeployed is a week where HVAC and water restoration owners searching for this solution find nothing. The deployment itself (DEPLOY.md → Cloudflare Pages) is a 20-minute task. The pre-deploy checklist below should be done in the same commit. This is the highest-leverage action across all 5 businesses — a live InboundAI site at $750/month per client has the potential to outperform all 3 rank-and-rent sites combined.

**Pre-deploy commit checklist (30–45 min total):**
- Add OG tags to `<head>`: og:title, og:description, og:image (create a 1200×630 branded image), og:url
- Create `sitemap.xml` with single entry for the live domain
- Create `robots.txt` with `Allow: /` and sitemap reference
- Add `Organization` + `FAQPage` JSON-LD schema (7 FAQ pairs already exist in HTML)
- Fix footer Terms of Service `href="#"` → either add `#faq` or create a terms page

---

**2. [Rank-and-Rent] Nashville sitemap — 4 high-intent pages still invisible to Google (3rd week)**

`commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, and `water-damage-restoration-cost-nashville` are missing from sitemap.xml. These are the highest-differentiation pages on the Nashville site — cost guides and insurance guides capture mid-funnel research traffic that converts. Google is not being directed to crawl them. Fix is 4 `<url>` block additions to sitemap.xml, commit, redeploy. 15-minute task. Has been flagged 3 weeks in a row.

---

**3. [Rank-and-Rent] Cincinnati copy errors + malformed HTML — damages local SEO credibility (3rd week)**

Four instances of "Nashville" in Cincinnati's index.html body copy are a direct local SEO credibility problem — if Google reads "Nashville" on a page targeting Cincinnati queries, it weakens geo-relevance signals. Additionally, a **new finding this week**: `<span itemprop="addressLocality": "Cincinnati</span>` is malformed HTML (colon instead of `=`) — the microdata is invalid and not being parsed. Both are fast fixes: find-and-replace "Nashville" → "Cincinnati" in index.html, fix the malformed span, commit, redeploy. While in the file, verify the contact form handler works on Cloudflare Workers (swap `data-netlify="true"` to Formspree if not).

---

**4. [HAKD] Add og:image — currently breaks every social share on the site (3rd week)**

The HAKD layout.js has `openGraph` and `twitter` card configured but no image. `/public/` contains zero images (only Google Search Console verification). Every tweet, LinkedIn post, or shared link from hakd.app renders as a blank card — missing the single biggest visual driver of click-through on social. Fix: create a 1200×630 branded `og-image.png` (HAKD dark theme, white/gold typography), add to `/public/og-image.png`, then add `images: ['https://hakd.app/og-image.png']` to the `openGraph` and `twitter` objects in layout.js. Also add a `favicon.ico` while in `/public/`.

---

**5. [HAKD] Migrate EMM Assessment off raw Netlify subdomain (3rd week)**

`deluxe-moxie-d4016f.netlify.app` is the primary CTA on every single HAKD page — in the nav, hero, banners, article CTAs, footer, and About page. It is a raw auto-generated Netlify subdomain with no custom domain. One accidental project deletion, a Netlify account change, or a team member renaming the project causes a complete and silent conversion blackout across the entire site. Migration path: add a custom domain (`assess.hakd.app` or `tools.hakd.app`) to the Netlify project, then do a single find-and-replace across all hakd-site files. Verify the two Everfit coaching package links (`GL583637`, `KX912574`) are still active at the same time.
