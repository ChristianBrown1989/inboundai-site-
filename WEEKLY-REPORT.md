# Weekly Master Report — 2026-11-08

## Site Audit Results

### Jacksonville (jacksonvillewaterdamagepros.com)

| Check | Status | Notes |
|---|---|---|
| Broken local links | ✅ OK | Anchor fragment refs (#areas, #contact, etc.) are intentional in-page anchors |
| Meta title | ✅ Present | "Water Damage Restoration Jacksonville FL \| 24/7 Emergency \| (904) 792-5162" |
| Meta description | ✅ Present | All pages checked |
| Meta keywords | ❌ MISSING | No `<meta name="keywords">` on any page |
| OG tags | ❌ MISSING | No og:title, og:description, og:image, og:url on ANY page |
| Sitemap | ⚠️ INCOMPLETE | 10 entries / 11 HTML pages — `thank-you.html` excluded (acceptable) but `index.html` itself wasn't parsed correctly; confirm `/` is listed |
| Robots.txt | ✅ Present | Exists in repo |
| Schema markup | ✅ Present | LocalBusiness + EmergencyService JSON-LD on index.html |
| Lazy loading | ⚠️ N/A | No `<img>` tags found — CSS-only design; no image optimization needed |
| Render-blocking | ✅ OK | No unoptimized external scripts |

**Missing from sitemap:** `thank-you.html` (intentionally excluded is fine)

---

### Nashville (nashvillewaterdamagepros.com)

| Check | Status | Notes |
|---|---|---|
| Broken local links | ✅ OK | Anchor fragments only |
| Meta title | ✅ Present | All pages |
| Meta description | ✅ Present | All pages |
| Meta keywords | ❌ MISSING | No `<meta name="keywords">` on any page |
| OG tags | ❌ MISSING | No OG tags on ANY of 15 pages |
| Sitemap | ❌ INCOMPLETE | 10 entries / 15 HTML pages — **5 pages missing** (see below) |
| Robots.txt | ✅ Present | `index, follow` |
| Schema markup | ✅ Present | LocalBusiness JSON-LD on index.html |
| Lazy loading | ⚠️ N/A | No img tags; CSS-only design |

**Pages missing from sitemap (4 real content pages + thank-you):**
- `commercial-water-damage-nashville.html`
- `hardwood-floor-water-damage-nashville.html`
- `insurance-claim-water-damage-nashville.html`
- `water-damage-restoration-cost-nashville.html`
- `thank-you.html` (can exclude intentionally)

---

### Cincinnati (cincinnatiwaterdamagepros.com)

| Check | Status | Notes |
|---|---|---|
| Broken local links | ✅ OK | Anchor fragments only |
| Meta title | ✅ Present | All pages |
| Meta description | ✅ Present | All pages |
| Meta keywords | ❌ MISSING | No `<meta name="keywords">` on any page |
| OG tags | ❌ MISSING | No OG tags on ANY of 10 pages |
| Sitemap | ⚠️ INCOMPLETE | 9 entries / 10 HTML pages — `thank-you.html` excluded (acceptable) |
| Robots.txt | ✅ Present | Exists in repo |
| Schema markup | ✅ Present | LocalBusiness JSON-LD on index.html |
| Lazy loading | ⚠️ N/A | No img tags; CSS-only design |

---

### HAKD (hakd.app) — Next.js

| Check | Status | Notes |
|---|---|---|
| Broken local links | ✅ OK | No broken local refs |
| Meta title | ✅ Present | In `app/layout.js` metadata export |
| Meta description | ✅ Present | In layout.js |
| Meta keywords | ✅ N/A | Next.js metadata API does not use keywords meta by default; acceptable |
| OG tags | ⚠️ PARTIAL | `openGraph` config present in layout.js but **no `/public/og-image.png`** — only `googledd73f79cadf7fe77.html` in /public. OG image will 404 for any page that references one. |
| Sitemap | ✅ Dynamic | `app/sitemap.js` — database-driven, includes articles + listings + static routes |
| Robots.txt | ✅ Present | `app/robots.js` — allows all, explicitly whitelists AI bots (Perplexity, GPTBot, ClaudeBot, Google-Extended) |
| Schema markup | ✅ Present | WebSite + Person JSON-LD in layout.js |
| Lazy loading | ✅ N/A | Next.js handles image optimization |

---

### InboundAI (inboundai-site-)

| Check | Status | Notes |
|---|---|---|
| Broken local links | ✅ OK | No local file references broken |
| Meta title | ✅ Present | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Present | Strong description present |
| Meta keywords | ❌ MISSING | No keywords meta tag |
| OG tags | ❌ MISSING | No og:title, og:description, og:image, og:url |
| Sitemap | ❌ MISSING | No sitemap.xml in repo |
| Robots.txt | ❌ MISSING | No robots.txt in repo |
| Schema markup | ❌ MISSING | No JSON-LD schema (no LocalBusiness, Organization, or SoftwareApplication) |
| Lazy loading | ⚠️ N/A | No images present in page |

---

## Deploy Queue

**Last 7 days (since 2026-11-01):**

| Repo | New Commits | Action Needed |
|---|---|---|
| jacksonville-water-damage | None | None |
| nashville-water-damage | None | None |
| cincinnati-water-damage | None | None |
| hakd-site | None | None |
| inboundai-site- | 1 commit — `chore: weekly master report 2026-11-01` | No code changes; report only |

**No repos have new feature/content commits requiring deployment this week.**

---

## Broken Affiliate Links (HAKD)

| URL | Status | Location | Severity |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | 🔴 **LIKELY BROKEN** | Nav (desktop + mobile), homepage hero CTA, article sidebars, article category pages, directory pages — **20+ occurrences across all templates** | **CRITICAL** |
| `https://coach.everfit.io/package/GL583637` | ✅ Appears valid | layout.js footer, article sidebar, about page | OK |
| `https://coach.everfit.io/package/KX912574` | ✅ Appears valid | layout.js footer, article sidebar | OK |
| `https://calendly.com/christianb3/15-minute-discovery-call` | ✅ Appears valid | layout.js footer | OK |

**CRITICAL — EMM Assessment Netlify URL:** `deluxe-moxie-d4016f.netlify.app` is a randomly-generated Netlify dev subdomain (auto-generated project slug pattern). This is almost certainly a development placeholder that was never replaced with the production URL. It appears on EVERY page of hakd.app as the primary CTA ("EMM Assessment" button in nav, hero, article sidebars, etc.). Every click by every visitor is going to a broken or unbranded dev URL instead of the real EMM assessment. This is the highest-priority HAKD fix.

**Files containing broken Netlify URL:**
- `app/layout.js` (nav + footer — affects every page)
- `app/page.js` (homepage — 3 occurrences)
- `app/articles/[slug]/page.js`
- `app/articles/page.js`
- `app/articles/category/[category]/page.js`
- `app/directory/page.js`
- `app/directory/city/[city]/page.js`
- `app/directory/city/[city]/[category]/page.js`
- `app/directory/category/[category]/page.js`

---

## Monthly Summary

Monthly summary scheduled for 1st of month. *(Today is 2026-11-08)*

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🔴 HAKD — Fix Broken EMM Assessment URL (Revenue Impact: HIGH)
**Action:** Replace all 20+ instances of `https://deluxe-moxie-d4016f.netlify.app` with the real production EMM Assessment URL across hakd-site. This CTA is on every single page — every visitor clicking "EMM Assessment" in the nav hits a dead or unbranded dev URL. This is active revenue leakage. Find the real URL (Typeform, Jotform, or wherever the assessment lives) and do a global find-and-replace.

### 2. 🔴 HAKD — Add og-image.png to /public (Revenue Impact: HIGH)
**Action:** Create a 1200×630px og-image.png for HAKD and add it to `hakd-site/public/`. Without it, sharing any HAKD URL on social media (LinkedIn, X, iMessage) shows a broken image card. The layout.js already has the openGraph config — just needs the actual image file.

### 3. 🟡 Nashville — Add 4 Missing Pages to Sitemap (Revenue Impact: MEDIUM)
**Action:** Add `commercial-water-damage-nashville`, `hardwood-floor-water-damage-nashville`, `insurance-claim-water-damage-nashville`, and `water-damage-restoration-cost-nashville` to Nashville's `sitemap.xml`. These 4 content pages are invisible to Google right now. Nashville has 15 pages but only 10 are indexed.

### 4. 🟡 All Rank-and-Rent Sites — Add OG Tags to All Pages (Revenue Impact: MEDIUM)
**Action:** Add `og:title`, `og:description`, `og:image`, and `og:url` to every HTML page across Jacksonville (11 pages), Nashville (15 pages), and Cincinnati (10 pages). Currently zero OG tags exist on any of these sites. Without them, sharing a link on social shows a blank preview — reduces referral traffic quality. Use a simple placeholder image (even the site logo) initially.

### 5. 🟡 InboundAI Site — Add Sitemap, Robots.txt, Schema, OG Tags (Revenue Impact: MEDIUM)
**Action:** InboundAI is completely missing 4 SEO fundamentals:
- Create `sitemap.xml` listing the homepage
- Create `robots.txt` allowing all crawlers
- Add `application/ld+json` schema (SoftwareApplication or Organization)
- Add OG tags to `index.html`

This is a one-time 30-minute fix that unlocks proper indexing and social sharing for the highest-value product page.

---

*Generated by Claude Code — Weekly Master Audit*
*Repos audited: jacksonville-water-damage, nashville-water-damage, cincinnati-water-damage, hakd-site, inboundai-site-*
