# Weekly Master Report — 2026-09-27

---

## Site Audit Results

### Jacksonville Water Damage (`jacksonvillewaterdamagepros.com`)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | "Water Damage Restoration Jacksonville FL \| 24/7 Emergency \| (904) 792-5162" |
| Meta description | ✅ Pass | Present on index.html |
| Meta keywords | ❌ Missing | Not present on index.html or any subpage |
| OG tags (og:title, og:description, og:image, og:url) | ❌ Missing | Zero OG tags across all 11 pages — social shares show blank card |
| Sitemap | ✅ Exists | 10 URLs listed — `thank-you.html` absent (acceptable) |
| Robots.txt | ✅ Pass | Allows all crawlers; references sitemap |
| Schema markup | ✅ Pass | `LocalBusiness + EmergencyService + FAQPage` on index.html |
| Broken local links | ✅ Pass | All footer/nav links reference existing files |
| Page speed / lazy loading | ⚠️ Unverified | No `<img>` tags visible in index.html — likely CSS backgrounds only |
| Form (Netlify forms) | ⚠️ Warning | `data-netlify="true"` used but site runs on **Cloudflare Workers**, not Netlify — contact form submissions may be silently failing |

**Pages (11 HTML):** index, emergency, burst-pipe, flood-damage, mold-remediation, orange-park, ponte-vedra, sewage-backup, st-johns, storm-damage, thank-you  
**Sitemap coverage: 10/10 meaningful pages (100%)**

---

### Nashville Water Damage (`nashvillewaterdamagepros.com`)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | Present on index.html |
| Meta description | ✅ Pass | Present on index.html |
| Meta keywords | ❌ Missing | Not present |
| OG tags | ❌ Missing | Zero OG tags across all pages — social shares show blank card |
| Sitemap | ⚠️ Incomplete | 10 URLs listed — **4 high-value pages missing** (see below) |
| Robots.txt | ✅ Pass | Exists (82 bytes) |
| Schema markup | ✅ Pass | `EmergencyService + FAQPage` on index.html |
| Broken local links | ✅ Pass | No broken internal hrefs found |
| Page speed / lazy loading | ⚠️ Unverified | CSS-based layout, no img tags confirmed missing |
| Form (Netlify forms) | ⚠️ Warning | Same `data-netlify` issue as Jacksonville — hosted on Cloudflare Workers |

**4 pages MISSING from sitemap.xml:**
- `commercial-water-damage-nashville.html` ❌
- `hardwood-floor-water-damage-nashville.html` ❌
- `insurance-claim-water-damage-nashville.html` ❌
- `water-damage-restoration-cost-nashville.html` ❌

These are long-tail, high-commercial-intent pages that are not receiving direct sitemap indexation signals.

**Pages (15 HTML):** index, emergency, burst-pipe, basement-flooding, brentwood, commercial, franklin, hardwood-floor, insurance-claim, mold-remediation, murfreesboro, sewage-backup, storm-damage, thank-you, water-damage-restoration-cost  
**Sitemap coverage: 10/15 pages (67%)**

---

### Cincinnati Water Damage (`cincinnatiwaterdamagepros.com`)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | Present (correctly says Cincinnati) |
| Meta description | ✅ Pass | Present |
| Meta keywords | ❌ Missing | Not present |
| OG tags | ❌ Missing | Zero OG tags across all pages |
| Sitemap | ✅ Good | 9 URLs — all meaningful pages covered |
| Robots.txt | ✅ Pass | Exists |
| Schema markup | ✅ Pass | `EmergencyService + FAQPage` |
| Broken local links | ✅ Pass | No broken hrefs |

**🚨 CRITICAL — Copy-Paste Nashville Bugs Found in index.html:**

| Location | Bug | Fix Needed |
|---|---|---|
| Hero badge | Says **"Nashville & Surrounding Areas"** | Change to "Cincinnati & Surrounding Areas" |
| "Why" section heading | Says **"Why Nashville Trusts Us"** | Change to "Why Cincinnati Trusts Us" |
| "Why" section body | Says **"We're a Nashville company. We live here too."** | Change to Cincinnati |
| "Why" section | Says **"insurance carrier in Tennessee"** | Change to Ohio |
| Testimonials section | Says **"Real Nashville Homeowners"** | Change to "Real Cincinnati Homeowners" |
| NAP hidden div | **Malformed HTML:** `itemprop="addressLocality": "Cincinnati` — attribute value has a colon and missing closing quote | Fix attribute to `itemprop="addressLocality" content="Cincinnati"` |

This is a **conversion-killing bug** — any Cincinnati visitor who notices "Nashville" will immediately distrust the brand.

**Pages (10 HTML):** index, emergency, basement-flooding, blue-ash, burst-pipe, mason, mold-remediation, sewage-backup, storm-damage, thank-you  
**Sitemap coverage: 9/10 pages (90% — thank-you excluded intentionally)**

---

### HAKD (`hakd.app`) — Next.js

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | `HAKD — Performance Intelligence for High Achievers` in layout.js metadata |
| Meta description | ✅ Pass | Present |
| Meta keywords | N/A | Not required in Next.js App Router; handled via metadata object |
| OG title | ✅ Pass | `HAKD — Performance Intelligence` |
| OG description | ✅ Pass | Present |
| **OG image** | **❌ MISSING** | No `images` field in openGraph config — all social share cards show no thumbnail |
| OG url | ✅ Pass | `https://hakd.app` |
| Twitter card | ✅ Partial | `summary_large_image` card type set — but missing `twitter:image`, so will downgrade to text-only |
| Sitemap | ✅ Dynamic | `app/sitemap.js` generates sitemap at build time |
| Robots | ✅ Dynamic | `app/robots.js` generates robots.txt |
| Schema | ✅ Pass | `WebSite` + `Person` schemas in layout.js |
| og-image.png | ❌ MISSING | `/public/` only contains Google verification HTML — no OG image file |
| Pages | Audit note | `app/about/`, `app/articles/`, `app/directory/` routes confirmed |

**Fix:** Add to layout.js metadata:
```js
openGraph: {
  ...
  images: [{ url: '/og-image.png', width: 1200, height: 630, alt: 'HAKD Performance Intelligence' }]
}
```
Then create a 1200×630px branded image at `public/og-image.png`.

---

### InboundAI (`inboundai-site-` repo)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present |
| Meta keywords | ❌ Not verified | File is 57KB — OG/meta section partially visible |
| OG tags | ❓ Unverified | Head section preview did not include OG tags — likely missing |
| Schema markup | ❓ Unverified | Large file; not confirmed |
| **Sitemap.xml** | **❌ MISSING** | No sitemap.xml in repo |
| **Robots.txt** | **❌ MISSING** | No robots.txt in repo |
| Broken links | Unverified | Would require live site crawl |

**Repo contains only:** index.html, DEPLOY.md, WEEKLY-REPORT.md, scripts/, .gitkeep

Needed immediately:
- `robots.txt` — 3 lines, allows all crawlers
- `sitemap.xml` — single entry for the homepage (or multi-page if site grows)
- Verify OG tags exist in full index.html head

---

## Deploy Queue

**Commits in last 7 days (2026-09-20 to 2026-09-27):**

| Repo | New Commits | Needs Deploy? |
|---|---|---|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 1 (automated weekly report 2026-09-20) | No |

**No development commits this week.** All repos are in stable deployed state. No Cloudflare Workers or Vercel deployments required.

---

## Broken Affiliate Links (HAKD)

Scanned `app/layout.js` for external hrefs:

| Link | Location | Status | Risk |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | Nav bar (all pages), Announce bar, CTA buttons | ⚠️ **SUSPICIOUS** | Random Netlify subdomain used as primary EMM Assessment link — appears to be a **staging URL deployed to production**. If this Netlify project is deleted or renamed, all assessment CTAs across the entire site go dead. Migrate to `hakd.app/assessment` or a proper custom domain immediately. |
| `https://coach.everfit.io/package/GL583637` | Footer — Monthly Coaching | ✅ Appears valid | everfit.io is a legitimate coaching platform |
| `https://coach.everfit.io/package/KX912574` | Footer — Monthly Training | ✅ Appears valid | Package URL format is standard |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Footer — Discovery Call | ✅ Appears valid | Standard Calendly personal link |

**Priority action:** The Netlify link `deluxe-moxie-d4016f.netlify.app` is the most-clicked element on the site (nav CTA, announce bar). Confirm the link is live and working. If it's a staging URL, create a proper redirect at `hakd.app/assessment`.

---

## Monthly Summary

📅 Today is **September 27, 2026** — not the 1st of the month.

**Monthly summary is scheduled for October 1, 2026.** Full performance summary (pages per site, sitemap coverage %, schema coverage %, new pages added) will be generated on the next scheduled Monday run on or after Oct 1.

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🚨 Fix Cincinnati's Nashville Copy-Paste Bugs — *Revenue Impact: HIGH*
**What:** `cincinnati-water-damage/index.html` contains 5+ instances of "Nashville" and "Tennessee" that should say Cincinnati/Ohio. Also has a malformed HTML attribute in the NAP div.
**Why now:** Local trust is the #1 conversion factor for water damage leads. A Cincinnati homeowner seeing "Nashville" immediately bounces. This is actively costing phone calls and rank-and-rent lease value.
**Time:** 20 minutes. Open `index.html` in the cincinnati repo, find-replace Nashville→Cincinnati and Tennessee→Ohio in the relevant sections, fix the malformed NAP attribute, push.

### 2. 🔧 Add sitemap.xml + robots.txt to InboundAI Site — *Revenue Impact: HIGH*
**What:** The primary revenue site (`inboundai-site-`) has no `sitemap.xml` and no `robots.txt`.
**Why now:** InboundAI is the product you're monetizing. Without a sitemap, Google is crawling it cold — no priority signals, no guaranteed indexation of the homepage. Takes 10 minutes to add both files.
**Time:** 10 minutes. Create `sitemap.xml` with the homepage URL and `robots.txt` allowing all crawlers. Push to main.

### 3. 📊 Add OG Tags to All 3 Rank-and-Rent Sites — *Revenue Impact: MEDIUM-HIGH*
**What:** Jacksonville, Nashville, and Cincinnati all lack `og:title`, `og:description`, `og:image`, and `og:url` on every page.
**Why now:** Social sharing (Facebook local groups, Nextdoor, referral texts) is a significant source of water damage leads. Blank preview cards get ignored. A single template fix can propagate to all ~36 pages across 3 repos.
**Time:** 1 hour. Add OG block to `<head>` on index.html for each site. Then check subpages and add per-page OG where possible.

### 4. 📋 Update Nashville Sitemap — Add 4 Missing Pages — *Revenue Impact: MEDIUM*
**What:** `nashville-water-damage/sitemap.xml` is missing 4 pages with high commercial intent keywords:
- `commercial-water-damage-nashville.html`
- `hardwood-floor-water-damage-nashville.html`
- `insurance-claim-water-damage-nashville.html`
- `water-damage-restoration-cost-nashville.html`
**Why now:** These pages exist but aren't receiving sitemap indexation signals. Google will discover them eventually via internal links, but sitemap submission accelerates ranking.
**Time:** 10 minutes. Add 4 `<url>` entries to `nashville-water-damage/sitemap.xml`.

### 5. 🖼️ Add OG Image to HAKD — *Revenue Impact: MEDIUM*
**What:** `hakd-site` OpenGraph config has no `images` field. Twitter/LinkedIn/Facebook shares of articles show no thumbnail.
**Why now:** HAKD monetizes through coaching packages and the EMM Assessment. Articles shared socially are the top of the funnel. A branded OG image (1200×630px) turns text-only shares into click-worthy cards.
**Time:** 30 minutes to design + 5 minutes to add to `layout.js` and push.
**Bonus:** Also investigate the `deluxe-moxie-d4016f.netlify.app` Assessment link — confirm it's live, and plan migration to a stable URL.

---

*Report generated by Claude Code — automated weekly audit, 2026-09-27*
