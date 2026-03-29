# Weekly Master Report — 2026-03-29

---

## Site Audit Results

### Jacksonville (jacksonvillewaterdamagepros.com)

**Pages found:** 11 HTML files (index, burst-pipe, emergency, flood-damage, mold-remediation, orange-park, ponte-vedra, sewage-backup, storm-damage, st-johns, thank-you)

| Check | Status | Notes |
|---|---|---|
| Broken links | ✅ PASS | All footer/nav `.html` hrefs reference existing files |
| Meta title | ✅ PASS | Present on index.html |
| Meta description | ✅ PASS | Present on index.html |
| Meta keywords | ❌ MISSING | Not present on any page |
| OG tags | ❌ MISSING | No og:title, og:description, og:image, og:url on any page |
| Sitemap | ✅ PASS | sitemap.xml exists, lists 10 URLs (all content pages covered) |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap linked |
| Schema markup | ✅ PASS | `LocalBusiness` + `EmergencyService` + `FAQPage` on index.html |
| Page speed | ✅ GOOD | No external images, no render-blocking scripts, CSS-only layout |

**Action items:**
- Add OG tags to all pages (og:title, og:description, og:image, og:url) — required for social sharing and link previews
- Add meta keywords to all pages

---

### Nashville (nashvillewaterdamagepros.com)

**Pages found:** 16 HTML files (index + 15 inner pages including 4 new SEO pages added Mar 25)

| Check | Status | Notes |
|---|---|---|
| Broken links | ⚠️ MINOR | Footer service links use `#services` anchors instead of linking to dedicated service pages |
| Meta title | ✅ PASS | Present on index.html |
| Meta description | ✅ PASS | Present on index.html |
| Meta keywords | ❌ MISSING | Not present on any page |
| OG tags | ❌ MISSING | No OG tags on any page |
| Sitemap | ❌ OUTDATED | 4 new pages added Mar 25 are NOT in sitemap.xml |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap linked |
| Schema markup | ✅ PASS | `EmergencyService` + `FAQPage` on index.html |
| Page speed | ✅ GOOD | No external images, no render-blocking scripts |

**Sitemap gaps — add these 4 URLs:**
- `https://nashvillewaterdamagepros.com/commercial-water-damage-nashville`
- `https://nashvillewaterdamagepros.com/hardwood-floor-water-damage-nashville`
- `https://nashvillewaterdamagepros.com/insurance-claim-water-damage-nashville`
- `https://nashvillewaterdamagepros.com/water-damage-restoration-cost-nashville`

**Action items:**
- Update sitemap.xml to include 4 new pages immediately (they won't index until listed)
- Add OG tags to all pages
- Add meta keywords to all pages
- Update footer service links to point to actual service pages instead of #anchors

---

### Cincinnati (cincinnatiwaterdamagepros.com)

**Pages found:** 12 HTML files

| Check | Status | Notes |
|---|---|---|
| Broken links | ⚠️ MINOR | Footer service links use `#services` anchors only |
| Meta title | ✅ PASS | Present on index.html |
| Meta description | ✅ PASS | Present on index.html |
| Meta keywords | ❌ MISSING | Not present on any page |
| OG tags | ❌ MISSING | No OG tags on any page |
| Sitemap | ✅ PASS | sitemap.xml exists, lists 9 URLs (all main pages covered) |
| Robots.txt | ✅ PASS | `Allow: /`, sitemap linked |
| Schema markup | ✅ PASS | `EmergencyService` + `FAQPage` on index.html |
| Page speed | ✅ GOOD | No external images, no render-blocking scripts |

**🚨 CRITICAL BUGS — Nashville copy-paste errors still live in index.html:**
1. **Hero badge:** reads `"60-Minute Response · Nashville & Surrounding Areas"` — should say Cincinnati
2. **Section label:** `"Why Nashville Trusts Us"` — should say Cincinnati
3. **Section copy:** `"treat every Nashville homeowner"` — should say Cincinnati
4. **Testimonials label:** `"Real Nashville Homeowners"` — should say Cincinnati
5. **Schema text:** references insurance carriers in `"Tennessee"` — should be Ohio
6. **HTML syntax error:** NAP div has malformed attribute `"addressLocality": "Cincinnati</span>` — missing closing quote on attribute, invalid HTML

**Action items:**
- Fix all 6 Nashville copy-paste errors in index.html BEFORE next deploy
- Fix HTML syntax error in NAP div
- Add OG tags to all pages
- Add meta keywords

---

### HAKD (hakd.app — Next.js / Vercel)

**Pages:** Dynamic — home, /articles, /directory, /about + articles (Supabase), 53+ listings, 18 city pages, 126 city×category pages

| Check | Status | Notes |
|---|---|---|
| Broken links | ✅ PASS | All hrefs in layout.js and page.js reference valid destinations |
| Meta title | ✅ PASS | Set in layout.js metadata export |
| Meta description | ✅ PASS | Set in layout.js metadata export |
| Meta keywords | ✅ N/A | Deprecated tag, not needed in Next.js metadata API |
| OG title | ✅ PASS | `og:title` set in openGraph metadata |
| OG description | ✅ PASS | `og:description` set |
| OG url | ✅ PASS | `og:url` set |
| OG image | ❌ MISSING | **No `og:image` in metadata. No `og-image.png` in /public.** Social shares will show no image. |
| Sitemap | ✅ PASS | Dynamic sitemap.js covers static routes, all articles, all listings, city + city×category pages |
| Robots.txt | ✅ PASS | Dynamic robots.js — all crawlers allowed + AI bots explicitly whitelisted (Perplexity, GPTBot, ClaudeBot) |
| Schema markup | ✅ PASS | `WebSite` + `Person` schema in layout.js; `FAQPage` on article pages |
| Page speed | ✅ GOOD | Google Fonts loaded via preconnect, no render-blocking scripts |

**Action items:**
- Create og-image.png (1200×630) and add to /public
- Add `images: [{ url: '/og-image.png', width: 1200, height: 630 }]` to openGraph in layout.js

---

### InboundAI (inboundai-site-)

**Status:** Repository initialized only — contains `.gitkeep`, no site files yet.

Initialized: 2026-03-27

- No HTML, no sitemap, no robots.txt, no schema, no pages to audit
- **Nothing to deploy** — site build has not started

---

## Deploy Queue

Today: 2026-03-29. All commits below are within the last 7 days.

| Repo | Platform | Latest Commit | Status | Notes |
|---|---|---|---|---|
| **jacksonville-water-damage** | Cloudflare Workers | `5c0a956` 2026-03-24 — FAQ schema | 🔴 NEEDS DEPLOY | 4 commits since initial build |
| **nashville-water-damage** | Cloudflare Workers | `9442985` 2026-03-25 — 4 new SEO pages | 🔴 NEEDS DEPLOY | **Priority** — new pages not live until deployed. Fix sitemap first. |
| **cincinnati-water-damage** | Cloudflare Workers | `f21d85e` 2026-03-24 — FAQ schema | 🔴 NEEDS DEPLOY | **Fix Nashville copy errors BEFORE deploying** |
| **hakd-site** | Vercel | `cee01f2` 2026-03-25 — Newsletter subscriber tagging | 🟡 CHECK | Likely auto-deploying via Vercel Git integration. Verify. |
| **inboundai-site-** | — | `1ea8ef8` 2026-03-27 — Initialize repo | ⚪ NOT READY | No site to deploy |

### Nashville commit detail (last 7 days):
- `9442985` 2026-03-25 — Add 4 high-value SEO pages: cost guide, insurance claims, hardwood floors, commercial
- `eb87ee0` 2026-03-24 — Add FAQ schema and AggregateRating to homepage
- `ee8ee49` 2026-03-24 — Add wrangler.toml for static site deployment
- `21694dd` 2026-03-23 — Update phone number to real 615 OpenPhone number
- `82e7da7` 2026-03-22 — Add sitemap and robots.txt

### HAKD commit detail (last 7 days):
- `cee01f2` 2026-03-25 — Tag HAKD newsletter subscribers as EMM Lead - Hakd
- `b5f729f` 2026-03-22 — Add mid-article newsletter CTA, directory search, Kit source tagging, sitemap pings

---

## Broken Affiliate Links (HAKD)

Links found in layout.js and page.js:

| URL | Location | Status | Notes |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | Nav, hero, banners, footer (6+ instances) | ⚠️ FLAG | Auto-generated Netlify subdomain. If this is the permanent EMM Assessment URL it needs a custom domain. Looks like a staging/temp URL. |
| `https://coach.everfit.io/package/GL583637` | Footer — Monthly Coaching | ✅ Appears valid | Everfit coaching package link |
| `https://coach.everfit.io/package/KX912574` | Footer — Monthly Training | ✅ Appears valid | Everfit training package link |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Footer — Discovery Call | ✅ Appears valid | Calendly booking link |

**Summary:** No confirmed 404s. Main concern is the Netlify subdomain for the EMM Assessment — if that app is the primary conversion CTA appearing 6+ times on the site, it should be on a custom domain for brand credibility and link stability.

---

## Monthly Summary

Monthly summary scheduled for 1st of month.

*(Next full summary: April 1, 2026)*

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🚨 Fix Cincinnati copy-paste errors + deploy all 3 rank-and-rent sites
**Revenue impact: HIGH** — Cincinnati is live with "Nashville & Surrounding Areas" in the hero and a broken HTML attribute. This kills trust and conversions. Fix the 6 Nashville copy errors and the HTML syntax bug, then deploy all 3 sites to Cloudflare Workers. Nashville has 4 new SEO pages that have been sitting undeployed since Mar 25.

**Steps:**
- Fix Cincinnati index.html: hero badge, "Why Nashville" section, testimonials label, schema, HTML syntax error
- Update Nashville sitemap.xml to add the 4 new pages
- Deploy: Jacksonville → Nashville → Cincinnati (in that order)

---

### 2. 🏗️ Start InboundAI site build
**Revenue impact: HIGH** — The inboundai-site- repo was initialized 2 days ago but has no content. InboundAI is listed as the highest-priority business. The landing page, positioning, and lead capture need to be built out.

**Steps:**
- Define the core InboundAI offer and build the landing page
- Set up deployment pipeline (Vercel recommended, matching HAKD setup)
- Add meta tags, OG tags, schema, sitemap, robots.txt from day one

---

### 3. 📋 Add OG tags to all 3 rank-and-rent sites
**Revenue impact: MEDIUM-HIGH** — All 3 water damage sites are completely missing OG tags. Every time a link is shared on Facebook, iMessage, LinkedIn, or SMS, there's no image, no description, no preview. For emergency services where referrals and shares matter, this is a real conversion leak.

**Steps:**
- Add `og:title`, `og:description`, `og:image`, `og:url` to `<head>` on all HTML pages
- Create a generic OG image for each site (1200×630) showing brand name + phone number
- Do all 3 sites in one pass

---

### 4. 🖼️ Add og:image to HAKD
**Revenue impact: MEDIUM** — HAKD has all OG tags except the image. Every article share and homepage link preview shows blank. For a content/media brand, this is essential for click-through on social. Create one branded og-image.png, add to /public, and reference in layout.js metadata.

**Steps:**
- Design og-image.png (1200×630): HAKD logo + tagline on dark background
- Place in `/public/og-image.png`
- Add `images: [{ url: '/og-image.png', width: 1200, height: 630, alt: 'HAKD Performance Intelligence' }]` to openGraph in layout.js

---

### 5. 🔗 Move EMM Assessment to custom domain
**Revenue impact: MEDIUM** — The EMM Assessment at `deluxe-moxie-d4016f.netlify.app` is the primary CTA across the entire HAKD site — appearing in the nav, hero, two banners, and footer. A Netlify auto-generated subdomain erodes trust and is fragile (any Netlify account change could break all 6+ CTAs simultaneously). Move to `assessment.hakd.app` or `emm.hakd.app`.

**Steps:**
- Add custom domain to the Netlify assessment app
- Do a find-and-replace across all HAKD source files to update the URL
- Deploy

---

*Generated by Claude Code — Weekly Master Audit*
*Run every Monday | Full monthly summary on the 1st*
