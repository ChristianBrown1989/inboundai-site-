# Weekly Master Report — 2026-05-31

---

## Site Audit Results

### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

**Pages:** 10 public HTML + thank-you.html = 11 files

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "Water Damage Restoration Jacksonville FL \| 24/7 Emergency \| (904) 792-5162" |
| Meta description | ✅ Pass | Present on index.html; thank-you.html omitted (acceptable) |
| Meta keywords | ❌ Missing | No `<meta name="keywords">` on any page |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url — **CARRY-OVER WK 2** |
| sitemap.xml | ✅ Pass | 10 URLs — matches all public pages exactly |
| robots.txt | ✅ Pass | `Allow: /` — not blocking crawlers; references sitemap |
| LocalBusiness schema | ✅ Pass | index.html: LocalBusiness + EmergencyService + FAQPage |
| Page speed | ✅ Pass | No images, no external JS, system fonts only |
| Broken local links | ✅ Pass | All 9 internal href targets verified present in repo |

**Action items (carry-over from last week):**
- Add OG tags (og:title, og:description, og:image, og:url) to all 10 public pages — zero social link previews without this

---

### Nashville Water Damage (nashvillewaterdamagepros.com)

**Pages:** 14 public HTML + thank-you.html = 15 files

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | All pages |
| Meta description | ✅ Pass | All public pages |
| Meta keywords | ❌ Missing | No keywords meta on any page |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER WK 2** |
| sitemap.xml | ⚠️ Incomplete | 10 URLs listed; 4 published pages not in sitemap — **CARRY-OVER WK 2** |
| robots.txt | ✅ Pass | Allows all crawlers; references sitemap |
| EmergencyService schema | ✅ Pass | index.html + FAQPage |
| Page speed | ✅ Pass | No images, no external JS |
| Broken local links | ✅ Pass | None found |

**Sitemap gaps — 4 live pages Google may not be indexing:**
- `/commercial-water-damage-nashville`
- `/hardwood-floor-water-damage-nashville`
- `/insurance-claim-water-damage-nashville`
- `/water-damage-restoration-cost-nashville`

**Action items:** Update sitemap.xml to add 4 missing URLs; add OG tags to all pages.

---

### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

**Pages:** 9 public HTML + thank-you.html = 10 files

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | All pages |
| Meta description | ✅ Pass | All public pages |
| Meta keywords | ❌ Missing | No keywords meta on any page |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER WK 2** |
| sitemap.xml | ✅ Pass | 9 URLs — matches all public pages |
| robots.txt | ✅ Pass | Allows all crawlers; references sitemap |
| EmergencyService schema | ✅ Pass | index.html + FAQPage |
| Page speed | ✅ Pass | No images, no external JS |
| Broken local links | ✅ Pass | None found |

**🚨 CRITICAL — Nashville/Tennessee brand contamination (STILL UNFIXED — WK 2):**

7 instances of wrong-city copy confirmed in index.html + emergency.html:

| Location | Wrong Text |
|----------|-----------|
| index.html hero badge | "⚡ 60-Minute Response · **Nashville** & Surrounding Areas" |
| index.html section label | "Why **Nashville** Trusts Us" |
| index.html section sub | "treat every **Nashville** homeowner" |
| index.html insurance copy | "approved by every major insurance carrier in **Tennessee**" |
| index.html footer | "We're a **Nashville** company. We live here too." |
| index.html testimonials | "Real **Nashville** Homeowners" |
| emergency.html | "Response in **Nashville**" |

**🆕 NEW BUG — Broken HTML in Cincinnati NAP microdata:**
```html
<!-- Current (broken): -->
<span itemprop="addressLocality": "Cincinnati</span>

<!-- Should be: -->
<span itemprop="addressLocality">Cincinnati</span>
```
The colon after the attribute name is invalid HTML — this microdata will fail to parse and may confuse schema crawlers.

**Action items:** Fix 7 Nashville/Tennessee references across index.html + emergency.html; fix broken HTML attribute in NAP div.

---

### HAKD (hakd.app) — Next.js on Vercel

**Pages:** Static: `/`, `/about`, `/articles`, `/directory` + dynamic: `articles/[slug]`, `articles/category/[category]`, `directory/[slug]`, `directory/category/[category]`, `directory/city/[city]`, `directory/city/[city]/[category]`

| Check | Status | Notes |
|-------|--------|-------|
| Title tags | ✅ Pass | root layout metadata + per-page generateMetadata |
| Meta description | ✅ Pass | layout.js + per-page overrides |
| OG tags | ⚠️ Partial | og:title, og:description, og:url, og:siteName in layout.js; **og:image still missing** — no /public/og-image.png exists — **CARRY-OVER WK 2** |
| sitemap | ✅ Pass | Dynamic sitemap.js: static + articles + listings + 7 dir categories + 18 cities × 7 city+category combos |
| robots | ✅ Pass | Dynamic robots.js with AI crawler allowlist (Claude, GPT, Perplexity) |
| Schema | ✅ Pass | WebSite + Person in layout.js; Article + BreadcrumbList on articles; CollectionPage missing on directory/category pages |
| Page speed | ✅ Pass | Proper SSG, no render-blocking resources |
| Broken internal links | ✅ Pass | No broken local hrefs found |

**🚨 SECURITY — ConvertKit API key hardcoded in source (WK 2 — STILL NOT FIXED, ESCALATED):**
`/app/api/subscribe/route.js` — key committed to the public git repository and in git history.
Steps to fix:
1. ConvertKit → Settings → Advanced → API → Regenerate API Key
2. Add `CONVERTKIT_API_KEY` to Vercel project environment variables
3. Replace hardcoded string in code with `process.env.CONVERTKIT_API_KEY`
4. Redeploy — key must be rotated even after the code change because old key is in git history

**External / affiliate link audit:**

| URL | Location | Risk |
|-----|---------|------|
| `https://deluxe-moxie-d4016f.netlify.app` | Announce bar, nav CTA, hero, EMM banner, about strip, footer — **6+ placements** | ⚠️ **HIGH** — Random Netlify subdomain; entire site's primary CTA chain breaks if project is deleted or renamed |
| `https://coach.everfit.io/package/GL583637` | Footer — Monthly Coaching $250/mo | ✅ Everfit is active SaaS platform |
| `https://coach.everfit.io/package/KX912574` | Footer — Monthly Training $80/mo | ✅ Everfit is active SaaS platform |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Footer — Discovery Call | ✅ Standard Calendly; verify account active |

**⚠️ EMM Assessment link risk:** `deluxe-moxie-d4016f.netlify.app` is a randomly-generated Netlify project subdomain — the primary revenue CTA appearing 6+ times across the site. If the Netlify project is renamed, deleted, or lapses, every CTA on hakd.app sends users to a 404. Strongly recommended: migrate EMM Assessment to `hakd.app/assessment` or a custom subdomain.

**Action items:** (1) Rotate ConvertKit key NOW — week 2 escalation; (2) add /public/og-image.png 1200×630 and reference in layout.js `openGraph.images`; (3) migrate EMM Assessment to custom domain.

---

### InboundAI (inboundai.app) — Static HTML on Cloudflare Workers

**Pages:** 1 (single-page — index.html, 57KB)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | 157 characters |
| Meta keywords | ❌ Missing | |
| OG tags | ❌ Missing | No og:title, og:description, og:image, og:url — **CARRY-OVER WK 2** |
| sitemap.xml | ❌ Missing | File not in repo — **CARRY-OVER WK 2** |
| robots.txt | ❌ Missing | File not in repo — **CARRY-OVER WK 2** |
| JSON-LD schema | ❌ Missing | No SoftwareApplication or Organization schema — **CARRY-OVER WK 2** |
| Page speed | ✅ Pass | Inline CSS, no images, emoji-only visuals |
| Broken local links | ⚠️ 2 found | `href="#"` on logo (line ~538) and Terms of Service (line ~1118) — no /terms.html exists |

**Scripts present:** `scripts/inboundai_client_intelligence.py` (8KB) and `scripts/inboundai_market_intelligence.py` (12KB) — Python automation scripts for market + client intelligence pipeline.

**Action items (all carry-over from WK 1):** Create robots.txt and sitemap.xml; add OG tags; add SoftwareApplication + Organization JSON-LD schema; fix 2 dead `href="#"` links.

---

## Deploy Queue

`git log --since='2026-05-24' --oneline` results:

| Repo | New Commits (7 days) | Needs Deploy? |
|------|---------------------|---------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 (this report file only) | No |

**No code deployments required this week.** All 5 sites are running last week's code.

> ⚠️ **Second consecutive week with zero commits across all 5 sites.** Every action item below is a direct carry-over from the 2026-05-24 report. The Cincinnati brand fix and HAKD security issue are now 2 weeks old.

---

## Broken Affiliate Links (HAKD)

Static scan complete. Live HTTP checks require manual click-through.

| URL | Context | Assessment |
|-----|---------|-----------|
| `https://deluxe-moxie-d4016f.netlify.app` | EMM Assessment — primary CTA (6+ placements across site) | ⚠️ **HIGH RISK** — Random Netlify subdomain. Manually verify weekly. Migrate to custom domain ASAP. |
| `https://coach.everfit.io/package/GL583637` | Monthly Coaching $250/mo | ✅ Everfit is active platform — verify package is still published |
| `https://coach.everfit.io/package/KX912574` | Monthly Training $80/mo | ✅ Everfit is active platform — verify package is still published |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Discovery Call booking | ✅ Standard Calendly link — verify availability is turned on |

**Recommended this week:** Manually click all 4 links and confirm they resolve and are bookable/accessible.

---

## Monthly Summary

Today is **2026-05-31 (Sunday)**. Monthly summary scheduled for 1st of month (tomorrow — 2026-06-01).

> Next Monday's report (2026-06-02) will include the full June monthly summary: total pages per site, sitemap coverage %, schema markup coverage %, and new pages added in May from git log.

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Fix Cincinnati Nashville brand contamination [RANK-AND-RENT — WK 2, URGENT]
**Revenue impact: HIGH** — Visitors on cincinnatiwaterdamagepros.com read "We're a Nashville company" and "every insurance carrier in Tennessee." This directly kills conversion trust on an active lead-gen property. 7 text fixes + 1 HTML attribute fix, ~20 minutes total.

Fix in `index.html`: hero badge, "Why Nashville Trusts Us", "Nashville homeowner", "Tennessee" insurance copy, "Nashville company" footer, "Nashville Homeowners" testimonials label.
Fix in `emergency.html`: "Response in Nashville."
Fix in `index.html` NAP div: `itemprop="addressLocality": "Cincinnati` → `itemprop="addressLocality">Cincinnati`

---

### 2. 🔴 Rotate HAKD ConvertKit API key [SECURITY — WK 2, ESCALATED]
**Revenue impact: HIGH** — Hardcoded key in `/app/api/subscribe/route.js` is in the public git history for 2+ weeks. Any actor can use it to corrupt your subscriber list, add fake tags, or spam your audience. Every week this remains unfixed is additional exposure.

Steps: (1) Regenerate key in ConvertKit → Settings → Advanced → API. (2) Add `CONVERTKIT_API_KEY` to Vercel env vars. (3) Replace hardcoded string in code. (4) Redeploy.

---

### 3. 🟠 Update Nashville sitemap.xml — add 4 missing pages [SEO — RANK-AND-RENT]
**Revenue impact: MEDIUM-HIGH** — Four high-value pages (commercial water damage, hardwood floor damage, insurance claims, cost guide) are live but absent from sitemap.xml. Google deprioritizes crawling pages it can't discover via sitemap. 5-minute fix.

Add to sitemap.xml: `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville`

---

### 4. 🟠 Add OG tags to all 3 rank-and-rent sites [SEO/SOCIAL — RANK-AND-RENT]
**Revenue impact: MEDIUM** — 33 pages across Jacksonville (10), Nashville (14), Cincinnati (9) have zero OG tags. Every text message share, iMessage link preview, Slack post, and Facebook share produces a blank card. One batch commit per site. Need a 1200×630 brand image for each.

Template for each page:
```html
<meta property="og:title" content="[PAGE TITLE]">
<meta property="og:description" content="[META DESCRIPTION]">
<meta property="og:image" content="https://[DOMAIN]/og-image.jpg">
<meta property="og:url" content="https://[DOMAIN]/[SLUG]">
<meta property="og:type" content="website">
```

---

### 5. 🟡 Add InboundAI SEO foundation: robots.txt + sitemap.xml + schema + OG tags [INBOUNDAI SITE]
**Revenue impact: MEDIUM** — InboundAI is top-of-funnel for your highest-value product. Missing robots.txt, sitemap, Organization/SoftwareApplication JSON-LD schema, and OG tags are all basic infrastructure that takes ~30 minutes. Without them, Google can't reliably discover, represent, or rank the page.

Files to create:
- `robots.txt` — `User-agent: * / Allow: / / Sitemap: https://inboundai.app/sitemap.xml`
- `sitemap.xml` — single URL entry for `https://inboundai.app/`
- Add to `index.html` `<head>`: OG tags + SoftwareApplication + Organization JSON-LD
