# Weekly Master Report — 2026-06-21

---

## Site Audit Results

### Jacksonville | Nashville | Cincinnati | HAKD | InboundAI

#### Jacksonville Water Damage (jacksonvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | Present on all pages |
| Meta description | ✅ Pass | Present on all public pages |
| Meta keywords | ❌ Missing | No `<meta name="keywords">` on any page |
| OG tags | ❌ Missing | No og:title/description/image/url — **CARRY-OVER, 5 WEEKS** |
| sitemap.xml | ✅ Pass | All 10 public pages listed correctly |
| robots.txt | ✅ Pass | Allows crawlers; references sitemap |
| LocalBusiness schema | ✅ Pass | `["LocalBusiness","EmergencyService"]` + FAQPage + AggregateRating on index.html |
| Page speed | ✅ Pass | No images, no blocking JS |
| Broken local links | ✅ Pass | None found — all internal hrefs resolve |

**Action items (carry-over):** Add OG tags to all pages.

---

#### Nashville Water Damage (nashvillewaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | All pages |
| Meta description | ✅ Pass | All public pages |
| Meta keywords | ❌ Missing | No keywords meta anywhere |
| OG tags | ❌ Missing | No OG tags — **CARRY-OVER, 5 WEEKS** |
| sitemap.xml | ⚠️ Incomplete | Only 10 of 14 URLs listed — **CARRY-OVER, STILL UNFIXED 5 WEEKS** |
| robots.txt | ✅ Pass | Allows crawlers; references sitemap |
| EmergencyService schema | ✅ Pass | `EmergencyService` + FAQPage + AggregateRating |
| Page speed | ✅ Pass | No images, no blocking JS |
| Broken local links | ✅ Pass | None found |

**Sitemap gaps — re-verified, unchanged for 5 weeks, and worse than previously documented:**
- `/insurance-claim-water-damage-nashville` — missing from sitemap, but **is** linked from index.html nav (discoverable by visitors, not by Google)
- `/water-damage-restoration-cost-nashville` — missing from sitemap, but **is** linked from index.html nav
- `/commercial-water-damage-nashville` — missing from sitemap **and** has zero internal links anywhere on the site (fully orphaned page — only reachable by typing the URL directly)
- `/hardwood-floor-water-damage-nashville` — missing from sitemap **and** has zero internal links anywhere on the site (fully orphaned page)

**Action items:** Add the 4 missing URLs to sitemap.xml (5-minute fix, unaddressed for 5 weeks); additionally link `commercial-water-damage-nashville` and `hardwood-floor-water-damage-nashville` from the homepage/nav — right now they're invisible to both users and crawlers; add OG tags to all pages.

---

#### Cincinnati Water Damage (cincinnatiwaterdamagepros.com)

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | All pages |
| Meta description | ✅ Pass | All public pages |
| Meta keywords | ❌ Missing | No keywords meta anywhere |
| OG tags | ❌ Missing | No OG tags — **CARRY-OVER, 5 WEEKS** |
| sitemap.xml | ✅ Pass | All 9 public pages listed correctly |
| robots.txt | ✅ Pass | Allows crawlers; references sitemap |
| EmergencyService schema | ✅ Pass | index.html + FAQPage |
| Page speed | ✅ Pass | No images, no blocking JS |
| Broken local links | ✅ Pass | None found |

**🚨🚨 CRITICAL — Nashville/Tennessee brand contamination — STILL LIVE, 5 WEEKS UNFIXED:**

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

**Action items:** Fix all 7 Nashville/Tennessee references in index.html + emergency.html; fix the broken `itemprop` attribute. ~20 minutes total — this has now sat unfixed for **5 consecutive weekly audits** on a live, traffic-receiving site.

---

#### HAKD (hakd.app) — Next.js on Vercel

| Check | Status | Notes |
|-------|--------|-------|
| Title tags | ✅ Pass | root layout + per-page generateMetadata |
| Meta description | ✅ Pass | layout.js + per-page overrides |
| OG tags | ⚠️ Partial | og:title/description/url/siteName present; **og:image still missing — `/public/og-image.png` does not exist** — **CARRY-OVER, 5 WEEKS** (only `googledd73f79cadf7fe77.html` verification file present in `/public`) |
| sitemap | ✅ Pass | Dynamic `app/sitemap.js` covers static + category + article + directory listing routes |
| robots | ✅ Pass | Dynamic `app/robots.js` with AI crawler allowlist (Perplexity, GPTBot, ClaudeBot, Google-Extended, Amazonbot) |
| Schema | ✅ Pass | WebSite + Person in layout.js; Article + BreadcrumbList on articles; FAQPage on listings |
| Page speed | ✅ Pass | SSG, no render-blocking resources |
| Broken internal links | ✅ Pass | All internal routes resolve |

**🚨🚨 SECURITY — ConvertKit API key still hardcoded in source — 5 WEEKS UNFIXED, RE-ESCALATING:**
`/app/api/subscribe/route.js:14` — `api_key: 'unwsbthP07XOrlhfGdfrkg'` is committed in plaintext to the **public** git repository (in git history for 5+ weeks now). No `CONVERTKIT_API_KEY` env var reference exists anywhere in `app/`.

Fix steps (unchanged):
1. ConvertKit → Settings → Advanced → API → **Regenerate API Key** (must rotate regardless — already exposed in history)
2. Add `CONVERTKIT_API_KEY` to Vercel project environment variables
3. Replace the hardcoded string in `route.js:14` with `process.env.CONVERTKIT_API_KEY`
4. Redeploy

This is the single most actionable security item across all 5 properties and has now been flagged in **five** consecutive reports without action.

**Action items:** (1) Rotate ConvertKit key NOW; (2) add `/public/og-image.png` (1200×630) and reference in `layout.js` `openGraph.images`; (3) migrate EMM Assessment off the random Netlify subdomain (see below).

---

#### InboundAI (inboundai.app) — Static HTML on Cloudflare Pages

| Check | Status | Notes |
|-------|--------|-------|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present |
| Meta keywords | ❌ Missing | |
| OG tags | ❌ Missing | No og:title/description/image/url — **CARRY-OVER, 5 WEEKS** |
| sitemap.xml | ❌ Missing | File not in repo — **CARRY-OVER, 5 WEEKS** |
| robots.txt | ❌ Missing | File not in repo — **CARRY-OVER, 5 WEEKS** |
| JSON-LD schema | ❌ Missing | No SoftwareApplication or Organization schema — **CARRY-OVER, 5 WEEKS** |
| Page speed | ✅ Pass | Inline `<script>` placed at end of body (non-blocking); zero `<img>` tags |
| Broken local links | ⚠️ 2 found, unchanged | `href="#"` on nav logo (line 538) and "Terms of Service" (line 1118) — no `/terms.html` exists |

The entire site (`index.html`) has had **zero code commits since launch on 2026-04-05** — these are the same gaps that existed on day one, now ~11 weeks old.

**Action items (all carry-over, now 5 weeks old in this audit, ~11 weeks since launch):** Create robots.txt and sitemap.xml; add OG tags; add SoftwareApplication + Organization JSON-LD schema; fix the 2 dead `href="#"` links.

---

## Deploy Queue

`git log --since='7 days ago' --oneline` results (run 2026-06-21):

| Repo | New Commits (7 days) | Needs Deploy? |
|------|---------------------|---------------|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 — `7ae240e chore: weekly master report 2026-06-14` (report file only) | No |

**No code deployments required.** All 5 sites are still running the same code as last week. `jacksonville-water-damage`, `nashville-water-damage`, and `cincinnati-water-damage` have had zero commits since 2026-03-24/25; `hakd-site` since 2026-03-25; `inboundai-site-`'s actual site code since launch on 2026-04-05 (only the weekly report file has moved since).

> ⚠️ **Fifth consecutive week with zero substantive commits across all 5 properties.** Every carry-over item below (Cincinnati brand contamination, HAKD API key, Nashville sitemap gap + 2 orphaned pages, missing OG tags everywhere, missing InboundAI SEO foundation) is now five weeks old in this audit cycle. These remain small, fast fixes — the backlog is a prioritization problem, not a complexity problem.

---

## Broken Affiliate Links (HAKD)

External link scan of `app/` and `lib/` (unchanged from prior weeks):

| URL | Context | Assessment |
|-----|---------|-----------|
| `https://deluxe-moxie-d4016f.netlify.app` | EMM Assessment — primary CTA, 6+ placements across hakd.app | ⚠️ **HIGH RISK** — auto-generated Netlify subdomain (not custom). One Netlify cleanup/rename away from breaking every CTA on the site simultaneously. |
| `https://coach.everfit.io/package/GL583637` | Monthly Coaching $250/mo | ✅ Real platform domain |
| `https://coach.everfit.io/package/KX912574` | Monthly Training $80/mo | ✅ Real platform domain |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Discovery Call booking | ✅ Real platform domain |
| `https://api.convertkit.com/v3/forms/9216083/subscribe` | Newsletter signup API | ✅ Real platform domain (associated with the exposed API key above) |
| `https://api.telegram.org/bot...` | Internal notification webhook | ✅ Real platform domain |

No placeholder URLs (`example.com`, `#`, `TODO`, `YOUR_*_HERE`) or wrong-domain links found. The `deluxe-moxie-d4016f.netlify.app` link remains the only structurally risky one — still not broken, but still one accidental Netlify cleanup away from taking down hakd.app's entire conversion path. Live click-through/404 verification still requires Christian's own connection (sandbox network policy blocks outbound HTTP checks from this environment).

---

## Monthly Summary

Today is **2026-06-21** — not the 1st of the month (next monthly summary due **2026-07-01**).

**Monthly summary scheduled for 1st of month.**

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 Review this week's InboundAI market intelligence brief and act on it same-day [INBOUNDAI PIPELINE — HIGHEST PRIORITY]
**Revenue impact: HIGHEST** — `inboundai_market_intelligence.py` runs every Monday at 7am on the Hetzner server (65.21.61.61) and outputs the latest brief to `/root/Desktop/CBrownOS/System/inboundai-market-intel-latest.md`: competitor change alerts, contractor pain-point language scraped from Reddit, and "market gaps you can own this week." This is the actual revenue-generating intelligence loop — the marketing site is just the funnel front door. This audit runs in a sandboxed repo-only environment with no access to the Hetzner server, so the brief itself couldn't be pulled from here — Christian needs to check it directly. These insights decay fast; turn at least one "market gap" into a script/copy change or outreach angle today.

---

### 2. 🔴 Fix Cincinnati Nashville/Tennessee brand contamination [RANK-AND-RENT — 5 WEEKS UNFIXED, URGENT]
**Revenue impact: HIGH** — Live visitors on cincinnatiwaterdamagepros.com are reading "We're a Nashville company" and "every insurance carrier in Tennessee" — this directly kills conversion trust on an active lead-gen property that's been taking traffic with this bug for over a month. 7 text fixes + 1 broken HTML attribute, ~20 minutes total, re-verified still present line-for-line.

Fix in `index.html` (lines 138, 230, 232, 260, 274, 321) and `emergency.html` (line 48): replace "Nashville"/"Tennessee" with "Cincinnati"/"Ohio".
Fix in `index.html:112`: `itemprop="addressLocality": "Cincinnati` → `itemprop="addressLocality">Cincinnati`.

---

### 3. 🟠 Add the 4 missing pages to Nashville's sitemap.xml — and link the 2 orphaned ones [RANK-AND-RENT — 5 WEEKS UNFIXED]
**Revenue impact: MEDIUM-HIGH** — `commercial-water-damage-nashville` and `hardwood-floor-water-damage-nashville` are not just missing from the sitemap, they have **zero internal links anywhere on the site** — Google and visitors can only find them by guessing the exact URL. `insurance-claim-water-damage-nashville` and `water-damage-restoration-cost-nashville` are linked in the nav but still absent from the sitemap. All 4 are live, high-value SEO pages sitting undiscovered for 5 weeks running. Add all 4 to `sitemap.xml` (5-minute fix) and add nav/footer links to the 2 fully orphaned pages.

---

### 4. 🔴 Rotate the HAKD ConvertKit API key [SECURITY — 5 WEEKS EXPOSED, RE-ESCALATING]
**Revenue impact: HIGH** — The hardcoded key in `/app/api/subscribe/route.js:14` (`unwsbthP07XOrlhfGdfrkg`) has now been sitting in the **public** git history for 5+ weeks. Anyone who finds it can pollute the subscriber list, inject fake tags, or spam the audience under the HAKD brand. Steps: (1) regenerate in ConvertKit, (2) add `CONVERTKIT_API_KEY` to Vercel env vars, (3) swap the hardcoded string for `process.env.CONVERTKIT_API_KEY`, (4) redeploy. ~15 minutes.

---

### 5. 🟡 Build InboundAI's SEO foundation: robots.txt + sitemap.xml + schema + OG tags [INBOUNDAI SITE — 5 WEEKS MISSING, ~11 WEEKS SINCE LAUNCH]
**Revenue impact: MEDIUM** — InboundAI is the funnel for the highest-value product, and the marketing site still has the same gaps it launched with on 2026-04-05: no robots.txt, no sitemap.xml, no Organization/SoftwareApplication JSON-LD, no OG tags, plus 2 dead `href="#"` links (logo + Terms of Service). ~30 minutes total and Google still can't reliably discover or represent the page.

Files/changes needed:
- `robots.txt` — `User-agent: * / Allow: / / Sitemap: https://inboundai.app/sitemap.xml`
- `sitemap.xml` — single `<url>` entry for `https://inboundai.app/`
- `<head>` additions: OG tags (title/description/image/url) + SoftwareApplication + Organization JSON-LD
- Fix `href="#"` on the nav logo (→ `/`) and Terms of Service link (build `/terms.html` or remove until ready)
