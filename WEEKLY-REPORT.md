# Weekly Master Report — 2026-06-14

---

## Site Audit Results

### Jacksonville | Nashville | Cincinnati | HAKD | InboundAI

#### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all pages |
| Meta description | ✅ Pass | Present on all public pages |
| Meta keywords | ❌ Missing | No `<meta name="keywords">` on any page |
| OG tags | ❌ Missing | No og:title/description/image/url — **CARRY-OVER, 4 WEEKS** |
| sitemap.xml | ✅ Pass | Matches all public pages |
| robots.txt | ✅ Pass | Allows crawlers; references sitemap |
| LocalBusiness schema | ✅ Pass | `["LocalBusiness","EmergencyService"]` + FAQPage + AggregateRating |
| Page speed | ✅ Pass | No images, no blocking JS |
| Broken local links | ✅ Pass | None found |

**Action items (carry-over):** Add OG tags to all pages.

---

#### Nashville Water Damage (nashvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | All pages |
| Meta description | ✅ Pass | All public pages |
| Meta keywords | ❌ Missing | No keywords meta anywhere |
| OG tags | ❌ Missing | No OG tags — **CARRY-OVER, 4 WEEKS** |
| sitemap.xml | ⚠️ Incomplete | Only 10 of 14 URLs listed — **CARRY-OVER, STILL UNFIXED 4 WEEKS** |
| robots.txt | ✅ Pass | Allows crawlers; references sitemap |
| EmergencyService schema | ✅ Pass | `EmergencyService` + FAQPage + AggregateRating |
| Page speed | ✅ Pass | No images, no blocking JS |
| Broken local links | ✅ Pass | None found |

**Sitemap gaps — verified again, unchanged for 4 weeks:**
- `/commercial-water-damage-nashville`
- `/hardwood-floor-water-damage-nashville`
- `/insurance-claim-water-damage-nashville`
- `/water-damage-restoration-cost-nashville`

**Action items:** Add the 4 missing URLs to sitemap.xml (5-minute fix, unaddressed for a full month); add OG tags to all pages.

---

#### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | All pages |
| Meta description | ✅ Pass | All public pages |
| Meta keywords | ❌ Missing | No keywords meta anywhere |
| OG tags | ❌ Missing | No OG tags — **CARRY-OVER, 4 WEEKS** |
| sitemap.xml | ✅ Pass | Matches all public pages |
| robots.txt | ✅ Pass | Allows crawlers; references sitemap |
| EmergencyService schema | ✅ Pass | index.html + FAQPage |
| Page speed | ✅ Pass | No images, no blocking JS |
| Broken local links | ✅ Pass | None found |

**🚨🚨 CRITICAL — Nashville/Tennessee brand contamination — STILL LIVE, 4 WEEKS UNFIXED:**

Re-verified line-by-line, all 7 instances still present, byte-for-byte identical to week 1:

| File:Line | Wrong Text |
|-----------|-----------|
| index.html:138 | "⚡ 60-Minute Response · **Nashville** & Surrounding Areas" |
| index.html:230 | "Why **Nashville** Trusts Us" |
| index.html:232 | "treat every **Nashville** homeowner the way we'd want our own family treated" |
| index.html:260 | "approved by every major insurance carrier in **Tennessee**" |
| index.html:274 | "We're a **Nashville** company. We live here too." |
| index.html:321 | "Real **Nashville** Homeowners" |
| emergency.html:48 | "24/7 Emergency Water Damage … Response in **Nashville**" |

**Also still broken — invalid NAP microdata (index.html:112):**
```html
<!-- Current (still broken): -->
<span itemprop="addressLocality": "Cincinnati</span>
<!-- Should be: -->
<span itemprop="addressLocality">Cincinnati</span>
```

**Action items:** Fix all 7 Nashville/Tennessee references in index.html + emergency.html; fix the broken `itemprop` attribute. ~20 minutes total — this has now sat unfixed for 4 consecutive audits on a live, traffic-receiving site.

---

#### HAKD (hakd.app) — Next.js on Vercel

| Check | Status | Notes |
|-------|--------|-------|
| Title tags | ✅ Pass | root layout + per-page generateMetadata |
| Meta description | ✅ Pass | layout.js + per-page overrides |
| OG tags | ⚠️ Partial | og:title/description/url/siteName present; **og:image still missing — `/public/og-image.png` does not exist** — **CARRY-OVER, 4 WEEKS** (only `googledd73f79cadf7fe77.html` verification file present in `/public`) |
| sitemap | ✅ Pass | Dynamic `app/sitemap.js` covers static + dynamic routes |
| robots | ✅ Pass | Dynamic `app/robots.js` with AI crawler allowlist |
| Schema | ✅ Pass | WebSite + Person in layout.js; Article + BreadcrumbList on articles |
| Page speed | ✅ Pass | SSG, no render-blocking resources |
| Broken internal links | ✅ Pass | All internal routes resolve |

**🚨🚨 SECURITY — ConvertKit API key still hardcoded in source — 4 WEEKS UNFIXED, RE-ESCALATING:**
`/app/api/subscribe/route.js:14` — `api_key: 'unwsbthP07XOrlhfGdfrkg'` is committed in plaintext to the **public** git repository (in git history for 4+ weeks now). No `CONVERTKIT_API_KEY` env var reference exists anywhere in `app/`.

Fix steps (unchanged):
1. ConvertKit → Settings → Advanced → API → **Regenerate API Key** (must rotate regardless — already exposed in history)
2. Add `CONVERTKIT_API_KEY` to Vercel project environment variables
3. Replace the hardcoded string in `route.js:14` with `process.env.CONVERTKIT_API_KEY`
4. Redeploy

This is the single most actionable security item across all 5 properties and has now been flagged in **four** consecutive reports without action.

**Action items:** (1) Rotate ConvertKit key NOW; (2) add `/public/og-image.png` (1200×630) and reference in `layout.js` `openGraph.images`; (3) migrate EMM Assessment off the random Netlify subdomain (see Task 3 below).

---

#### InboundAI (inboundai.app) — Static HTML on Cloudflare Workers/Pages

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present |
| Meta keywords | ❌ Missing | |
| OG tags | ❌ Missing | No og:title/description/image/url — **CARRY-OVER, 4 WEEKS** |
| sitemap.xml | ❌ Missing | File not in repo — **CARRY-OVER, 4 WEEKS** |
| robots.txt | ❌ Missing | File not in repo — **CARRY-OVER, 4 WEEKS** |
| JSON-LD schema | ❌ Missing | No SoftwareApplication or Organization schema — **CARRY-OVER, 4 WEEKS** |
| Page speed | ✅ Pass | Inline CSS, zero `<img>` tags, emoji-only visuals |
| Broken local links | ⚠️ 2 found, unchanged | `href="#"` on nav logo (line 538) and "Terms of Service" (line 1118) — no `/terms.html` exists |

**Action items (all carry-over, now 4 weeks old):** Create robots.txt and sitemap.xml; add OG tags; add SoftwareApplication + Organization JSON-LD schema; fix the 2 dead `href="#"` links.

---

## Deploy Queue

`git log --since='7 days ago' --oneline` results (run 2026-06-14):

| Repo | New Commits (7 days) | Needs Deploy? |
|------|---------------------|---------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 — `ef1e37d chore: weekly master report 2026-06-07` (report file only) | No |

**No code deployments required.** All 5 sites are still running the same code as 4 weeks ago — `jacksonville-water-damage`, `nashville-water-damage`, and `cincinnati-water-damage` have had zero commits since 2026-03-24/25; `hakd-site` since 2026-03-25.

> ⚠️ **Fourth consecutive week with zero substantive commits across all 5 properties.** Every carry-over item below (Cincinnati brand contamination, HAKD API key, Nashville sitemap gap, missing OG tags everywhere, missing InboundAI SEO foundation) is now a full month old. These remain small, fast fixes — the backlog is a prioritization problem, not a complexity problem.

---

## Broken Affiliate Links (HAKD)

External link scan of `app/` and `lib/` (unchanged from last 3 weeks):

| URL | Context | Assessment |
|-----|---------|-----------|
| `https://deluxe-moxie-d4016f.netlify.app` | EMM Assessment — primary CTA, 6+ placements across hakd.app | ⚠️ **HIGH RISK** — auto-generated Netlify subdomain (not custom). One Netlify cleanup/rename away from breaking every CTA on the site simultaneously. |
| `https://coach.everfit.io/package/GL583637` | Monthly Coaching $250/mo | ✅ Real platform domain |
| `https://coach.everfit.io/package/KX912574` | Monthly Training $80/mo | ✅ Real platform domain |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Discovery Call booking | ✅ Real platform domain |
| `https://api.convertkit.com/v3/forms/9216083/subscribe` | Newsletter signup API | ✅ Real platform domain (associated with the exposed API key above) |
| `https://api.telegram.org/bot...` | Internal notification webhook | ✅ Real platform domain |

No placeholder URLs (`example.com`, `#`, `TODO`, `YOUR_*_HERE`) or wrong-domain links found. The `deluxe-moxie-d4016f.netlify.app` link remains the only structurally risky one — still not broken, but still one accidental Netlify cleanup away from taking down hakd.app's entire conversion path. Live click-through verification still requires Christian's own connection (sandbox network policy blocks outbound HTTP checks).

---

## Monthly Summary

Today is **2026-06-14** — not the 1st of the month (next monthly summary due **2026-07-01**).

**Monthly summary scheduled for 1st of month.**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Review this week's InboundAI market intelligence brief and act on it same-day [INBOUNDAI PIPELINE — HIGHEST PRIORITY]
**Revenue impact: HIGHEST** — `inboundai_market_intelligence.py` runs every Monday at 7am on the Hetzner server and outputs the latest market intel brief: competitor change alerts, contractor pain-point language, and "market gaps you can own this week." This is the actual revenue-generating intelligence loop — the marketing site is just the funnel front door. These insights decay fast. Pull this morning's brief and turn at least one "market gap" into a script/copy change or outreach angle today.

---

### 2. 🔴 Fix Cincinnati Nashville/Tennessee brand contamination [RANK-AND-RENT — 4 WEEKS UNFIXED, URGENT]
**Revenue impact: HIGH** — Live visitors on cincinnatiwaterdamagepros.com are reading "We're a Nashville company" and "every insurance carrier in Tennessee" — this directly kills conversion trust on an active lead-gen property that's been taking traffic with this bug for a full month. 7 text fixes + 1 broken HTML attribute, ~20 minutes total, re-verified still present line-for-line.

Fix in `index.html` (lines 138, 230, 232, 260, 274, 321) and `emergency.html` (line 48): replace "Nashville"/"Tennessee" with "Cincinnati"/"Ohio".
Fix in `index.html:112`: `itemprop="addressLocality": "Cincinnati` → `itemprop="addressLocality">Cincinnati`.

---

### 3. 🟠 Add the 4 missing pages to Nashville's sitemap.xml [RANK-AND-RENT — 4 WEEKS UNFIXED]
**Revenue impact: MEDIUM-HIGH** — `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, and `water-damage-restoration-cost-nashville` are live, internally-linked, high-value SEO pages that Google may not be crawling/indexing because they're absent from the sitemap. A literal 5-minute copy-paste fix, now flagged 4 weeks running.

---

### 4. 🔴 Rotate the HAKD ConvertKit API key [SECURITY — 4 WEEKS EXPOSED, RE-ESCALATING]
**Revenue impact: HIGH** — The hardcoded key in `/app/api/subscribe/route.js:14` (`unwsbthP07XOrlhfGdfrkg`) has now been sitting in the **public** git history for 4+ weeks. Anyone who finds it can pollute the subscriber list, inject fake tags, or spam the audience under the HAKD brand. Steps: (1) regenerate in ConvertKit, (2) add `CONVERTKIT_API_KEY` to Vercel env vars, (3) swap the hardcoded string for `process.env.CONVERTKIT_API_KEY`, (4) redeploy. ~15 minutes.

---

### 5. 🟡 Build InboundAI's SEO foundation: robots.txt + sitemap.xml + schema + OG tags [INBOUNDAI SITE — 4 WEEKS MISSING]
**Revenue impact: MEDIUM** — InboundAI is the funnel for the highest-value product, and the marketing site is still missing the basics: no robots.txt, no sitemap.xml, no Organization/SoftwareApplication JSON-LD, no OG tags, plus 2 dead `href="#"` links (logo + Terms of Service). ~30 minutes total and Google still can't reliably discover or represent the page.

Files/changes needed:
- `robots.txt` — `User-agent: * / Allow: / / Sitemap: https://inboundai.app/sitemap.xml`
- `sitemap.xml` — single `<url>` entry for `https://inboundai.app/`
- `<head>` additions: OG tags (title/description/image/url) + SoftwareApplication + Organization JSON-LD
- Fix `href="#"` on the nav logo (→ `/`) and Terms of Service link (build `/terms.html` or remove until ready)
