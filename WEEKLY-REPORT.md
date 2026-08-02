# Weekly Master Report — 2026-08-02

---

## Site Audit Results

### Jacksonville | Nashville | Cincinnati | HAKD | InboundAI

---

#### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 11 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No `<meta name="keywords">` on any page — **CARRY-OVER, WEEK 11** |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url on any page — **CARRY-OVER, WEEK 11** |
| sitemap.xml | ✅ Pass | 10 public pages listed; thank-you intentionally excluded |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted; sitemap referenced |
| Schema markup | ⚠️ Issue | `sewage-backup-jacksonville.html` and `thank-you.html` have no schema; all other 9 pages OK — **CARRY-OVER, WEEK 11** |
| Page speed | ✅ Pass | No `<img>` tags, no render-blocking JS; LD+JSON only |
| Broken local links | ✅ Pass | No broken local file references found |

**Action items (carry-over):** Add OG tags to all 11 pages; add `<meta name="keywords">`; add schema to `sewage-backup-jacksonville.html`; add meta description to `thank-you.html`.

---

#### Nashville Water Damage (nashvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 15 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No keywords meta — **CARRY-OVER, WEEK 11** |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER, WEEK 11** |
| sitemap.xml | ⚠️ Incomplete | 10 of 14 public URLs listed — **CARRY-OVER, WEEK 11** |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted |
| Schema markup | ⚠️ Issue | 7 pages missing schema: basement-flooding, brentwood, franklin, mold-remediation, murfreesboro, sewage-backup, storm-damage — **CARRY-OVER, WEEK 11** |
| Page speed | ✅ Pass | No images, no render-blocking JS |
| Broken local links | ✅ Pass | No broken local file references found |

**Sitemap gaps — re-verified, 11 weeks unchanged:**
- `/commercial-water-damage-nashville` — NOT in sitemap.xml
- `/hardwood-floor-water-damage-nashville` — NOT in sitemap.xml
- `/insurance-claim-water-damage-nashville` — NOT in sitemap.xml
- `/water-damage-restoration-cost-nashville` — NOT in sitemap.xml

**Action items:** Add 4 missing URLs to sitemap.xml; add schema to 7 unschema'd pages; add OG tags to all pages.

---

#### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 10 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No keywords meta — **CARRY-OVER, WEEK 11** |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER, WEEK 11** |
| sitemap.xml | ✅ Pass | 9 content pages listed correctly |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted |
| Schema markup | ⚠️ Issue | `thank-you.html` missing schema only; all other pages OK |
| Page speed | ✅ Pass | No images, no render-blocking JS |
| Broken local links | ✅ Pass | No broken local file references found |

**🚨 CRITICAL — Nashville/Tennessee brand contamination — STILL LIVE, 11 WEEKS UNFIXED:**

All 7 instances confirmed present on this audit, unchanged since week 1:

| File | Line | Wrong Text |
|------|------|-----------|
| index.html | 138 | `"⚡ 60-Minute Response · Nashville & Surrounding Areas"` |
| index.html | 230 | `"Why Nashville Trusts Us"` |
| index.html | 232 | `"treat every Nashville homeowner the way we'd want our own family treated"` |
| index.html | 260 | `"every major insurance carrier in Tennessee"` |
| index.html | 274 | `"We're a Nashville company. We live here too."` |
| index.html | 321 | `"Real Nashville Homeowners"` |
| emergency.html | 48 | `"24/7 Emergency Water Damage Response in Nashville"` |

**Also still broken — invalid NAP microdata (index.html line 112):**
```html
<!-- BROKEN (live now): -->
<span itemprop="addressLocality": "Cincinnati</span>
<!-- CORRECT: -->
<span itemprop="addressLocality">Cincinnati</span>
```

**Action items:** Fix all 7 Nashville/Tennessee references; fix broken `itemprop` attribute on line 112; add OG tags; add meta keywords. This is ~25 minutes of work and has been live on an active lead-gen property for **11 consecutive audited weeks**.

---

#### HAKD (hakd.app) — Next.js on Vercel

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Root layout + per-page `generateMetadata` on all routes |
| Meta description | ✅ Pass | Root layout + per-page overrides |
| Meta keywords | ❌ Missing | Not present in any page metadata export — **CARRY-OVER, WEEK 11** |
| og:title | ✅ Pass | Present via root `openGraph` in layout.js |
| og:description | ✅ Pass | Present via root `openGraph` in layout.js |
| og:image | ❌ Missing | `/public/` contains only `googledd73f79cadf7fe77.html` — no `og-image.png` and no `images` field in `openGraph` — **CARRY-OVER, WEEK 11** |
| og:url | ✅ Pass | Present via root layout |
| sitemap | ✅ Pass | Dynamic `app/sitemap.js` covers static + category + article + directory + city routes |
| robots | ✅ Pass | Dynamic `app/robots.js` with AI crawler allowlist (PerplexityBot, GPTBot, ClaudeBot, Google-Extended) |
| Schema | ✅ Pass | WebSite + Person (global); Article + BreadcrumbList (articles) |
| Page speed | ⚠️ Issue | Google Fonts loaded via `<link>` preconnects in layout.js head — migrate to `next/font/google` to eliminate render-blocking |
| Broken internal links | ✅ Pass | All internal routes resolve |

**🚨 SECURITY — ConvertKit API key hardcoded in public source — 11 WEEKS EXPOSED, CRITICAL:**

`app/api/subscribe/route.js` line 14 — API key `unwsbthP07XOrlhfGdfrkg` committed in plaintext to the public GitHub repo. Confirmed present on this audit.

Fix (15 minutes):
1. ConvertKit → Settings → Advanced → API → **Regenerate API Key** (key is in public git history, must rotate)
2. Add `CONVERTKIT_API_KEY` to Vercel project environment variables
3. Replace hardcoded string with `process.env.CONVERTKIT_API_KEY`
4. Redeploy

**Action items:** (1) Rotate ConvertKit API key immediately; (2) create `/public/og-image.png` (1200×630 px) and wire into `layout.js` `openGraph.images`; (3) migrate EMM Assessment to a custom subdomain (`assessment.hakd.app`).

---

#### InboundAI (inboundai.app) — Static HTML on Cloudflare Pages

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present and descriptive |
| Meta keywords | ❌ Missing | — **CARRY-OVER, WEEK 11** |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url — **CARRY-OVER, WEEK 11** |
| sitemap.xml | ❌ Missing | File does not exist in repo — **CARRY-OVER, WEEK 11** |
| robots.txt | ❌ Missing | File does not exist in repo — **CARRY-OVER, WEEK 11** |
| JSON-LD schema | ❌ Missing | No SoftwareApplication or Organization schema — **CARRY-OVER, WEEK 11** |
| Page speed | ⚠️ Issue | Google Fonts loaded via external `<link>` stylesheet (render-blocking) |
| Broken local links | ⚠️ 2 found | `href="#"` on nav logo and "Terms of Service" — no `/terms.html` exists — **CARRY-OVER, WEEK 11** |

Zero substantive commits to `index.html` since launch on 2026-04-05 (~17 weeks). Every gap flagged in week 1 remains present.

**Action items (all carry-over):** Create `robots.txt`; create `sitemap.xml`; add OG tags; add `SoftwareApplication` + `Organization` JSON-LD; fix 2 dead `href="#"` links (logo → `/`, Terms → build `/terms.html` or remove).

---

## Deploy Queue

`git log --since='2026-07-26' --oneline` results:

| Repo | New Commits (7 days) | Needs Deployment? |
|------|---------------------|-------------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 — `0dcbec0 chore: weekly master report 2026-07-26` (report file only, no code) | No |

**No code deployments required this week.** All 5 sites running identical code to last week.

> ⚠️ **Eleventh consecutive week with zero substantive code commits across all 5 properties.** The Cincinnati brand contamination fix is ~25 minutes. The HAKD API key rotation is ~15 minutes. The Nashville sitemap update is ~5 minutes. The InboundAI SEO foundation is ~30 minutes. None of these are complex problems.

---

## Broken Affiliate Links (HAKD)

Full external link scan across all `app/` files:

| URL | Context | Status |
|-----|---------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | EMM Assessment — primary CTA, 30+ placements across all routes (nav, announce bar, footer, article sidebars, article CTAs) | ⚠️ **HIGH RISK / LIKELY BROKEN** — Auto-generated Netlify subdomain with a random hash — one project rename/deletion breaks every CTA simultaneously. Migrate to `assessment.hakd.app` — **CARRY-OVER, WEEK 11** |
| `https://coach.everfit.io/package/GL583637` | Monthly Coaching — footer, sidebar | ⚠️ Returns HTTP 000 from audit sandbox (proxy-blocked); verify by clicking in browser |
| `https://coach.everfit.io/package/KX912574` | Monthly Training — footer, sidebar | ⚠️ Returns HTTP 000 from audit sandbox (proxy-blocked); verify by clicking in browser |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Discovery Call — footer, about page | ⚠️ Returns HTTP 000 from audit sandbox (proxy-blocked); verify by clicking in browser |
| `https://api.convertkit.com/v3/forms/9216083/subscribe` | Newsletter subscribe (server-side) | ⚠️ API key hardcoded in source (see HAKD security note above) |

> Note: The Netlify URL (`deluxe-moxie-d4016f.netlify.app`) is the highest-risk link — a random hash subdomain with no custom domain protection. **Click-test all 4 links from a real browser this week.**

---

## Monthly Summary

Today is **2026-08-02** — not the 1st of the month.

**Monthly summary scheduled for 1st of month (next: 2026-09-01).**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Fix Cincinnati Nashville/Tennessee brand contamination NOW [RANK-AND-RENT — 11 WEEKS UNFIXED, CRITICAL]
**Revenue impact: HIGHEST active loss** — Live visitors on cincinnatiwaterdamagepros.com are reading "We're a Nashville company" and "every insurance carrier in Tennessee." This destroys conversion trust on an active lead-gen property. Re-verified all 7 instances present this audit for the 11th consecutive week.

Exact changes needed (~25 min):
- `index.html` lines 138, 230, 232, 260, 274, 321: Replace "Nashville" → "Cincinnati", "Tennessee" → "Ohio"
- `emergency.html` line 48: Replace "Nashville" → "Cincinnati"
- `index.html` line 112: Fix `itemprop="addressLocality": "Cincinnati` → `itemprop="addressLocality">Cincinnati`

---

### 2. 🔴 Rotate the HAKD ConvertKit API key [SECURITY — 11 WEEKS EXPOSED, CRITICAL]
**Revenue impact: HIGH** — Hardcoded API key `unwsbthP07XOrlhfGdfrkg` at `app/api/subscribe/route.js:14` has been in the public GitHub repo for 11+ weeks. Any bad actor can pollute your subscriber list, inject fake tags, or spam your audience under the HAKD brand. 15-minute fix: (1) regenerate key in ConvertKit, (2) add `CONVERTKIT_API_KEY` env var in Vercel, (3) replace hardcoded string with `process.env.CONVERTKIT_API_KEY`, (4) redeploy.

---

### 3. 🔴 Verify and fix the HAKD EMM Assessment link [HAKD — HIGH RISK CTA]
**Revenue impact: HIGH** — `https://deluxe-moxie-d4016f.netlify.app` appears in 30+ places across hakd.app (announce bar, nav, footer, every article sidebar, every article CTA). If the Netlify deployment was deleted or renamed, every single conversion point on HAKD is dead. **Open the link in a real browser right now.** If broken: restore the Netlify deploy or redirect to a working URL immediately. Long-term fix: migrate to `assessment.hakd.app`.

---

### 4. 🟠 Update Nashville sitemap + add schema to 7 pages [RANK-AND-RENT — 11 WEEKS UNFIXED]
**Revenue impact: MEDIUM-HIGH** — Nashville's sitemap.xml is missing 4 live URLs, and 7 pages have no schema markup. Pages outside the sitemap are deprioritized by Google's crawl budget. (~35 minutes total.)

Missing from sitemap: `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, `water-damage-restoration-cost-nashville`.

Pages needing schema: `basement-flooding-nashville.html`, `brentwood-water-damage.html`, `franklin-water-damage.html`, `mold-remediation-nashville.html`, `murfreesboro-water-damage.html`, `sewage-backup-nashville.html`, `storm-damage-nashville.html`.

---

### 5. 🟡 Build InboundAI's SEO foundation [INBOUNDAI SITE — 11 WEEKS MISSING, ~17 WEEKS SINCE LAUNCH]
**Revenue impact: MEDIUM** — InboundAI is the funnel for the highest-value product and still has no robots.txt, no sitemap.xml, no OG tags, no JSON-LD schema, and 2 dead `href="#"` links — all since launch. ~30 minutes of work. Until these exist, Google cannot reliably discover or represent the page, and social shares render with no preview card.

Files needed:
- `robots.txt` — `User-agent: * / Allow: / / Sitemap: https://inboundai.app/sitemap.xml`
- `sitemap.xml` — single `<url>` for `https://inboundai.app/`
- `index.html` `<head>`: add 4 OG tags + `SoftwareApplication` + `Organization` JSON-LD
- Fix `href="#"` on logo (→ `/`) and Terms link (build `/terms.html` or remove)
