# Weekly Master Report — 2026-08-09

---

## Site Audit Results

### Jacksonville | Nashville | Cincinnati | HAKD | InboundAI

---

#### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 11 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No `<meta name="keywords">` on any page — **CARRY-OVER, WEEK 12** |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url on any page — **CARRY-OVER, WEEK 12** |
| sitemap.xml | ✅ Pass | 10 public pages listed; thank-you intentionally excluded |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted; sitemap referenced |
| Schema markup | ⚠️ Issue | `sewage-backup-jacksonville.html` and `thank-you.html` missing schema — **CARRY-OVER, WEEK 12** |
| Page speed | ✅ Pass | No `<img>` tags, no render-blocking JS; LD+JSON only |
| Broken local links | ✅ Pass | No broken local file references found |

**Pages missing schema:** `sewage-backup-jacksonville.html`, `thank-you.html`

**Action items (carry-over):** Add OG tags to all 11 pages; add `<meta name="keywords">`; add schema to `sewage-backup-jacksonville.html`; add meta description to `thank-you.html`.

---

#### Nashville Water Damage (nashvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 15 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No keywords meta — **CARRY-OVER, WEEK 12** |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER, WEEK 12** |
| sitemap.xml | ⚠️ Incomplete | 10 of 15 URLs listed — 4 content pages excluded — **CARRY-OVER, WEEK 12** |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted |
| Schema markup | ⚠️ Issue | 7 content pages missing schema — **CARRY-OVER, WEEK 12** |
| Page speed | ✅ Pass | No images, no render-blocking JS |
| Broken local links | ✅ Pass | No broken local file references found |

**Sitemap gaps — re-verified, 12 weeks unchanged:**
- `/commercial-water-damage-nashville` — NOT in sitemap.xml
- `/hardwood-floor-water-damage-nashville` — NOT in sitemap.xml
- `/insurance-claim-water-damage-nashville` — NOT in sitemap.xml
- `/water-damage-restoration-cost-nashville` — NOT in sitemap.xml

**Pages missing schema:** `basement-flooding-nashville.html`, `brentwood-water-damage.html`, `franklin-water-damage.html`, `mold-remediation-nashville.html`, `murfreesboro-water-damage.html`, `sewage-backup-nashville.html`, `storm-damage-nashville.html`

**Action items:** Add 4 missing URLs to sitemap.xml; add schema to 7 un-schema'd pages; add OG tags to all pages.

---

#### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all 10 pages |
| Meta description | ⚠️ Issue | Missing on `thank-you.html` |
| Meta keywords | ❌ Missing | No keywords meta — **CARRY-OVER, WEEK 12** |
| OG tags | ❌ Missing | No OG tags on any page — **CARRY-OVER, WEEK 12** |
| sitemap.xml | ✅ Pass | 9 content pages listed correctly |
| robots.txt | ✅ Pass | `Allow: /` — crawlers permitted |
| Schema markup | ⚠️ Issue | `thank-you.html` missing schema only; all other 9 pages OK |
| Page speed | ✅ Pass | No images, no render-blocking JS |
| Broken local links | ✅ Pass | No broken local file references found |

**🚨 CRITICAL — Nashville/Tennessee brand contamination — STILL LIVE, 12 WEEKS UNFIXED:**

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

**This is an active conversion killer.** Every Cincinnati visitor who reads this leaves. 25-minute fix, 12 weeks overdue.

---

#### HAKD (hakd.app — Next.js / Vercel)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Set in `layout.js` metadata export |
| Meta description | ✅ Pass | Set in `layout.js` metadata export |
| Meta keywords | ✅ Pass | N/A for Next.js App Router (not a ranking factor) |
| og:title | ✅ Pass | Present in openGraph block |
| og:description | ✅ Pass | Present in openGraph block |
| og:image | ❌ Missing | Not set in `layout.js` openGraph object; `/public/og-image.png` does not exist — **CARRY-OVER, WEEK 12** |
| og:url | ✅ Pass | `https://hakd.app` set |
| sitemap.xml | ✅ Pass | Dynamic `sitemap.js` pulls articles + listings from Supabase; includes city/category matrix |
| robots.js | ✅ Pass | `Allow: /`, AI crawlers explicitly permitted (Perplexity, GPTBot, ClaudeBot) |
| Schema markup | ✅ Pass | WebSite + Person JSON-LD in `layout.js` |
| Page speed | ✅ Pass | Next.js image optimization + App Router streaming |
| Broken local links | ✅ Pass | No broken internal routes detected |
| 🔴 ConvertKit API key | ❌ EXPOSED | Hardcoded `unwsbthP07XOrlhfGdfrkg` at `app/api/subscribe/route.js:14` — **CARRY-OVER, WEEK 12** |

**Action items (carry-over):** Add `og:image` to `layout.js` openGraph block + create `/public/og-image.png` (1200×630px); rotate ConvertKit API key and move to Vercel env var.

---

#### InboundAI (inboundai-site-)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present and descriptive |
| Meta keywords | ❌ Missing | — **CARRY-OVER, WEEK 12** |
| OG tags | ❌ Missing | No og:title / og:description / og:image / og:url — **CARRY-OVER, WEEK 12** |
| sitemap.xml | ❌ Missing | File does not exist in repo — **CARRY-OVER, WEEK 12** |
| robots.txt | ❌ Missing | File does not exist in repo — **CARRY-OVER, WEEK 12** |
| JSON-LD schema | ❌ Missing | No SoftwareApplication or Organization schema — **CARRY-OVER, WEEK 12** |
| Page speed | ⚠️ Issue | Google Fonts loaded via external `<link>` stylesheet (render-blocking) |
| Broken local links | ⚠️ 2 found | `href="#"` on nav logo (line 538) and Terms of Service (line 1118) — no `/terms.html` exists — **CARRY-OVER, WEEK 12** |

Zero substantive commits to `index.html` since launch (~18 weeks). Every gap flagged in week 1 remains present.

**Action items (all carry-over):** Create `robots.txt`; create `sitemap.xml`; add OG tags; add `SoftwareApplication` + `Organization` JSON-LD; fix 2 dead `href="#"` links.

---

## Deploy Queue

`git log --since='2026-08-02' --oneline` results:

| Repo | New Commits (7 days) | Needs Deployment? |
|------|---------------------|-------------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 — `a534412 chore: weekly master report 2026-08-02` (report file only, no code) | No |

**No code deployments required this week.** All 5 sites running identical code to last week.

> ⚠️ **Twelfth consecutive week with zero substantive code commits across all 5 properties.** The Cincinnati brand contamination fix is ~25 minutes. The HAKD API key rotation is ~15 minutes. The Nashville sitemap update is ~5 minutes. The InboundAI SEO foundation is ~30 minutes. None of these are complex problems.

---

## Broken Affiliate Links (HAKD)

Full external link scan across all `app/` JS files:

| URL | Context | Status |
|-----|---------|--------|
| `https://deluxe-moxie-d4016f.netlify.app` | EMM Assessment — primary CTA in announce bar, nav, footer, and every article sidebar/CTA (30+ placements) | ⚠️ **HIGH RISK** — Random hash Netlify subdomain with no custom domain protection. Cannot verify from audit sandbox (proxy timeout). **Open in a real browser now.** Long-term: migrate to `assessment.hakd.app` — **CARRY-OVER, WEEK 12** |
| `https://coach.everfit.io/package/GL583637` | Monthly Coaching package — footer + sidebar | ⚠️ Returns HTTP 000 from audit sandbox (proxy-blocked); verify by clicking in browser |
| `https://coach.everfit.io/package/KX912574` | Monthly Training package — footer + sidebar | ⚠️ Returns HTTP 000 from audit sandbox (proxy-blocked); verify by clicking in browser |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Discovery Call — footer, about page | ⚠️ Returns HTTP 000 from audit sandbox (proxy-blocked); verify by clicking in browser |

> The Netlify hash URL (`deluxe-moxie-d4016f.netlify.app`) remains the highest-risk link. **Click-test all 4 links from a real browser this week.**

---

## Monthly Summary

Today is **2026-08-09** — not the 1st of the month.

**Monthly summary scheduled for 1st of month (next: 2026-09-01).**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Fix Cincinnati Nashville/Tennessee brand contamination [RANK-AND-RENT — 12 WEEKS UNFIXED, CRITICAL]
**Revenue impact: HIGHEST active loss** — Live visitors on cincinnatiwaterdamagepros.com are reading "We're a Nashville company" and "every insurance carrier in Tennessee." This destroys conversion trust on an active lead-gen property. Re-verified all 7 instances present this week for the 12th consecutive audit.

**Exact changes needed (~25 minutes):**
- `index.html` line 138: `Nashville & Surrounding Areas` → `Cincinnati & Surrounding Areas`
- `index.html` line 230: `Why Nashville Trusts Us` → `Why Cincinnati Trusts Us`
- `index.html` line 232: `every Nashville homeowner` → `every Cincinnati homeowner`
- `index.html` line 260: `every major insurance carrier in Tennessee` → `every major insurance carrier in Ohio`
- `index.html` line 274: `We're a Nashville company. We live here too.` → `We're a Cincinnati company. We live here too.`
- `index.html` line 321: `Real Nashville Homeowners` → `Real Cincinnati Homeowners`
- `emergency.html` line 48: `Response in Nashville` → `Response in Cincinnati`

---

### 2. 🔴 Rotate the HAKD ConvertKit API key [SECURITY — 12 WEEKS EXPOSED, CRITICAL]
**Revenue impact: HIGH** — API key `unwsbthP07XOrlhfGdfrkg` hardcoded at `app/api/subscribe/route.js:14` has been visible in a public GitHub repo for 12+ weeks. Any bad actor can pollute your subscriber list, inject fake tags, or spam your audience. **15-minute fix:**
1. Regenerate key in ConvertKit dashboard
2. Add `CONVERTKIT_API_KEY` env var in Vercel project settings
3. Replace hardcoded string with `process.env.CONVERTKIT_API_KEY`
4. Redeploy

---

### 3. 🔴 Verify HAKD EMM Assessment link + migrate to custom domain [HAKD — HIGH RISK]
**Revenue impact: HIGH** — `https://deluxe-moxie-d4016f.netlify.app` is the primary conversion CTA on hakd.app appearing in 30+ places. If the Netlify project was renamed or deleted, every conversion point on HAKD is dead simultaneously. **Right now:** open the link in a real browser. **This week:** migrate to `assessment.hakd.app` with a proper custom domain so one project deletion can't kill the entire funnel.

---

### 4. 🟠 Update Nashville sitemap.xml — add 4 missing pages [RANK-AND-RENT — 12 WEEKS, 5-MINUTE FIX]
**Revenue impact: MEDIUM-HIGH** — Google is de-prioritizing crawl of `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, and `water-damage-restoration-cost-nashville` because they aren't in the sitemap. These are high-intent landing pages that should be indexed. Also add schema to the 7 Nashville pages still missing it (basement-flooding, brentwood, franklin, mold-remediation, murfreesboro, sewage-backup, storm-damage).

---

### 5. 🟡 Build InboundAI's SEO foundation [INBOUNDAI SITE — 12 WEEKS MISSING, ~18 WEEKS SINCE LAUNCH]
**Revenue impact: MEDIUM** — InboundAI is the funnel for the highest-value product. It has no robots.txt, no sitemap.xml, no OG tags (social shares render blank), and no JSON-LD schema. Google cannot reliably discover or represent the page. **~30 minutes of work:**
- Create `robots.txt` → `User-agent: * / Allow: / / Sitemap: https://inboundai.app/sitemap.xml`
- Create `sitemap.xml` → single `<url>` for `https://inboundai.app/`
- Add to `index.html <head>`: 4 OG meta tags + `SoftwareApplication` JSON-LD
- Fix 2 dead `href="#"` links: nav logo → `/`, Terms of Service → build `/terms.html` or remove the link
