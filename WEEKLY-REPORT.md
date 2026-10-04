# Weekly Master Report — 2026-10-04

> **Audit status:** All 5 repos cloned and fully audited. No new commits landed in any repo this week. All 5 priorities from the 2026-09-27 report remain **UNRESOLVED** — urgency has escalated on items 1 and 2.

---

## Site Audit Results

### Jacksonville Water Damage (`jacksonvillewaterdamagepros.com`)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | "Water Damage Restoration Jacksonville FL \| 24/7 Emergency \| (904) 792-5162" |
| Meta description | ✅ Pass | Present on index.html |
| Meta keywords | ❌ Missing | Not present on index.html or any subpage |
| OG tags (og:title, og:description, og:image, og:url) | ❌ Missing | Zero OG tags across all 11 pages — social shares show blank card |
| Sitemap | ✅ Pass | 10 URLs — `thank-you.html` absent (acceptable) |
| Robots.txt | ✅ Pass | Allows all crawlers; references sitemap |
| Schema markup | ✅ Pass | `LocalBusiness + EmergencyService + FAQPage` on index.html |
| Broken local links | ✅ Pass | All CSS/page refs resolve |
| Page speed / lazy loading | ✅ Good | No `<img>` tags — layout is CSS-only, no lazy-loading issues |
| Render-blocking scripts | ✅ Pass | No render-blocking scripts in `<head>` |
| Form (Netlify on Cloudflare) | ⚠️ Warning | `data-netlify="true"` used but site runs on **Cloudflare Workers** — form submissions likely failing silently |
| Meta robots | ⚠️ Missing | No `<meta name="robots" content="index, follow">` (Nashville/Cincinnati have it) |

**Pages (11 HTML):** index, emergency, burst-pipe, flood-damage, mold-remediation, orange-park, ponte-vedra, sewage-backup, st-johns, storm-damage, thank-you
**Sitemap coverage: 10/10 meaningful pages (100%)**

---

### Nashville Water Damage (`nashvillewaterdamagepros.com`)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | Present on index.html |
| Meta description | ✅ Pass | Present on index.html |
| Meta keywords | ❌ Missing | Not present |
| OG tags | ❌ Missing | Zero OG tags across all pages |
| Sitemap | ⚠️ Incomplete | 10 URLs listed — **4 high-value pages missing** (see below) |
| Robots.txt | ✅ Pass | Exists, allows all crawlers |
| Schema markup | ✅ Pass | `EmergencyService + FAQPage` on index.html |
| Broken local links | ✅ Pass | No broken refs |
| Page speed | ✅ Good | CSS-only layout, no render-blocking scripts |
| Form (Netlify on Cloudflare) | ⚠️ Warning | Same `data-netlify` issue as Jacksonville |

**4 pages STILL MISSING from sitemap.xml (now 2+ weeks):**
- `commercial-water-damage-nashville.html` ❌
- `hardwood-floor-water-damage-nashville.html` ❌
- `insurance-claim-water-damage-nashville.html` ❌
- `water-damage-restoration-cost-nashville.html` ❌

These 4 pages have title tags and meta descriptions but are invisible to Google Search Console via sitemap. High commercial-intent long-tail keywords are being left on the floor.

**Pages (15 HTML):** index, emergency, burst-pipe, basement-flooding, brentwood, commercial, franklin, hardwood-floor, insurance-claim, mold-remediation, murfreesboro, sewage-backup, storm-damage, thank-you, water-damage-restoration-cost
**Sitemap coverage: 10/14 meaningful pages (71%)**

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

**🚨 CRITICAL — Nashville Copy-Paste Bugs STILL NOT FIXED (2 weeks old):**

| Location | Bug |
|---|---|
| Hero badge | Says **"Nashville & Surrounding Areas"** — should be Cincinnati |
| "Why" section heading | Says **"Why Nashville Trusts Us"** — should be Cincinnati |
| "Why" section body | Says **"We're a Nashville company"** — should be Cincinnati |
| "Why" section | Says **"insurance carrier in Tennessee"** — should be Ohio |
| Testimonials section | Says **"Real Nashville Homeowners"** — should be Cincinnati |
| NAP hidden div | **Malformed HTML** — `itemprop="addressLocality": "Cincinnati` — broken attribute syntax |

This is actively destroying conversion rate for any Cincinnati visitor who notices the Nashville branding. Every week this remains unfixed is revenue lost.

**Pages (10 HTML):** index, emergency, basement-flooding, blue-ash, burst-pipe, mason, mold-remediation, sewage-backup, storm-damage, thank-you
**Sitemap coverage: 9/9 meaningful pages (100%)**

---

### HAKD (`hakd.app`) — Next.js

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | `HAKD — Performance Intelligence for High Achievers` in layout.js |
| Meta description | ✅ Pass | Present |
| Meta keywords | N/A | Next.js App Router metadata object used instead |
| OG title | ✅ Pass | `HAKD — Performance Intelligence` |
| OG description | ✅ Pass | Present |
| **OG image** | **❌ MISSING** | No `images` field in openGraph config; `public/` has no og-image.png |
| OG url | ✅ Pass | `https://hakd.app` |
| Twitter card | ⚠️ Broken | `summary_large_image` set but no `twitter:image` — downgrades to text-only |
| Sitemap | ✅ Dynamic | `app/sitemap.js` — dynamically generates from Supabase articles + listings |
| Robots | ✅ Dynamic | `app/robots.js` — allows all crawlers, explicitly allows AI crawlers |
| Schema | ✅ Pass | `WebSite` + `Person` schemas — appropriate for content/personal-brand site |
| og-image.png | ❌ MISSING | Only file in `/public/` is Google Search Console verification HTML |

**Fix needed in `app/layout.js`:**
```js
openGraph: {
  title: 'HAKD — Performance Intelligence',
  description: 'Evidence-based performance optimization for high achievers.',
  type: 'website',
  url: 'https://hakd.app',
  siteName: 'HAKD',
  images: [{ url: '/og-image.png', width: 1200, height: 630, alt: 'HAKD Performance Intelligence' }],
},
twitter: {
  card: 'summary_large_image',
  title: 'HAKD — Performance Intelligence',
  description: 'Evidence-based performance optimization for high achievers.',
  images: ['/og-image.png'],
},
```
Then create a 1200×630px branded PNG at `public/og-image.png`.

---

### InboundAI (`inboundai.app`)

| Check | Status | Notes |
|---|---|---|
| Title tag | ✅ Pass | "InboundAI — Every Missed Call Is a Job You Didn't Get" |
| Meta description | ✅ Pass | Present |
| Meta keywords | ❌ Missing | Not present |
| OG tags | ❌ Missing | No `og:title`, `og:description`, `og:image`, `og:url` found |
| Schema markup | ❌ Missing | No `application/ld+json` found |
| **Sitemap.xml** | **❌ MISSING** | Not in repo — still unfixed from last week |
| **Robots.txt** | **❌ MISSING** | Not in repo — still unfixed from last week |
| Broken local links | ✅ Pass | All `href` values are anchor tags (`#section`) — no broken page links |
| Page speed | ✅ Good | Single-page app with inline CSS; Google Fonts loaded via preconnect |

**Still needed (2nd week):**
- `robots.txt` (3 lines)
- `sitemap.xml` (homepage entry)
- OG tags block in `<head>`
- `SoftwareApplication` or `Organization` JSON-LD schema

---

## Deploy Queue

**Commits in last 7 days (2026-09-27 to 2026-10-04):**

| Repo | New Commits | Needs Deploy? |
|---|---|---|
| jacksonville-water-damage | 0 | No |
| nashville-water-damage | 0 | No |
| cincinnati-water-damage | 0 | No |
| hakd-site | 0 | No |
| inboundai-site- | 0 (last: automated report 2026-09-27) | No |

**No development commits this week.** All 5 repos unchanged since Sept 27. No Cloudflare Workers or Vercel deployments required.

---

## Broken Affiliate Links (HAKD)

Scanned `hakd-site/app/` for all external hrefs:

| Link | Location | Status | Risk |
|---|---|---|---|
| `https://deluxe-moxie-d4016f.netlify.app` | Announce bar, Nav CTA, multiple page CTAs | ⚠️ **HIGH RISK** | Random Netlify subdomain for the primary EMM Assessment CTA. If this Netlify project is renamed or deleted, every CTA on hakd.app goes dead. **2nd week unfixed.** Migrate to `hakd.app/assessment` redirect ASAP. |
| `https://coach.everfit.io/package/GL583637` | Footer — Monthly Coaching | ✅ Valid format | Legitimate everfit.io platform URL |
| `https://coach.everfit.io/package/KX912574` | Footer — Monthly Training | ✅ Valid format | Standard package link |
| `https://calendly.com/christianb3/15-minute-discovery-call` | Footer — Discovery Call | ✅ Valid format | Standard Calendly personal link |
| `https://hakd.app/feed.xml` | Head — RSS alternate | ✅ Self-hosted | RSS feed served by Next.js route |

**Action required:** Verify `deluxe-moxie-d4016f.netlify.app` is live. Add a `/assessment` redirect on hakd.app pointing to the real URL. Replace all hardcoded Netlify links with `https://hakd.app/assessment`.

---

## Monthly Summary

📅 Today is **October 4, 2026** — not the 1st of the month.

**Monthly summary scheduled for November 3, 2026** (first Monday run on or after Nov 1). Full performance summary (total pages per site, sitemap coverage %, schema markup coverage %, new pages added in October) will be generated then.

---

## THIS WEEK'S TOP 5 PRIORITIES

### 1. 🚨 FIX CINCINNATI "NASHVILLE" BUGS — *Now 2 Weeks Unresolved — Revenue Impact: CRITICAL*
**What:** `cincinnati-water-damage/index.html` says "Nashville," "Tennessee," and "Nashville Homeowners" in 5+ visible locations. Also has a malformed HTML attribute in the NAP microdata div.
**Why escalated:** Every phone call from Cincinnati that bounces because of "Nashville" branding is money gone. This has been identified for 2 weeks. It takes 20 minutes to fix.
**Fix:** Open `cincinnati-water-damage/index.html`. Find-replace Nashville→Cincinnati and Tennessee→Ohio in the visible text sections. Fix the NAP attribute (`itemprop="addressLocality" content="Cincinnati"`). Push + deploy to Cloudflare Workers.

### 2. 🔧 Add sitemap.xml + robots.txt to InboundAI — *2nd Week — Revenue Impact: HIGH*
**What:** `inboundai-site-` has no `sitemap.xml` and no `robots.txt`. InboundAI is your primary revenue product.
**Why now:** Two weeks without a sitemap means Google is crawling your SaaS landing page cold. This is the site you're selling — it needs to rank.
**Fix:** Create `sitemap.xml` (single homepage entry) and `robots.txt` (allow all). Push. 10 minutes.

### 3. 📊 Add OG Tags to All 3 Rank-and-Rent Sites — *2nd Week — Revenue Impact: MEDIUM-HIGH*
**What:** All 36 pages across Jacksonville, Nashville, and Cincinnati have zero OG tags. Social previews are blank cards.
**Why now:** Nextdoor, Facebook local groups, and referral texts are a real source of water damage leads. Blank share cards are invisible. A single OG block template takes 1 hour to add across 3 repos.
**Fix:** Add to each `index.html` `<head>` (and subpages): `og:title`, `og:description`, `og:image` (use a generic 1200×630 banner), `og:url`, `og:type`.

### 4. 📋 Add 4 Missing Pages to Nashville Sitemap — *2nd Week — Revenue Impact: MEDIUM*
**What:** Nashville sitemap covers only 71% of pages. Missing: commercial, hardwood-floor, insurance-claim, water-damage-cost.
**Why now:** These 4 pages target high-intent searchers (commercial property managers, cost-conscious homeowners). They exist but Google has no sitemap signal for them.
**Fix:** Add 4 `<url>` entries to `nashville-water-damage/sitemap.xml`. 10 minutes.

### 5. 🖼️ Add OG Image to HAKD + Fix Assessment CTA Link — *2nd Week — Revenue Impact: MEDIUM*
**What:** HAKD articles shared on LinkedIn, Twitter/X, and Slack show no thumbnail. Primary CTA (`deluxe-moxie-d4016f.netlify.app`) is a fragile staging URL used as a production link.
**Why now:** HAKD's growth funnel is: article share → assessment → coaching sale. A broken share card kills step 1. A Netlify project deletion kills step 2.
**Fix 1:** Create a 1200×630px `public/og-image.png` and add it to the `openGraph.images` and `twitter.images` arrays in `app/layout.js`.
**Fix 2:** Add a `/assessment` redirect in Next.js pointing to the Netlify URL (short-term) and migrate the URL to a custom domain (long-term).

---

*Report generated by Claude Code — automated weekly audit, 2026-10-04*
