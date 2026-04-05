# InboundAI Website — Deploy to Cloudflare Pages

## Files
- `index.html` — Full single-page website (self-contained)
- `scripts/` — Intelligence engine Python scripts (deploy to Hetzner server, not Cloudflare)

## Deploy Steps

### 1. Push to GitHub
```bash
cd ~/Projects/inboundai-site-
git init  # if not already
git add index.html
git commit -m "Launch InboundAI website"
git remote add origin https://github.com/YOUR_USERNAME/inboundai-site.git
git push -u origin main
```

### 2. Connect to Cloudflare Pages
1. Log in to Cloudflare dashboard
2. Go to Pages → Create a project → Connect to Git
3. Select the `inboundai-site` repo
4. Build settings: **none needed** (static HTML, no build step)
5. Deploy

### 3. Connect Domain
1. In Cloudflare Pages → Custom domains → Add domain
2. Enter `inboundai.app`
3. Follow DNS instructions (already on Cloudflare since domain is on Hover — may need to point nameservers)

### 4. Before Launch — Update These
In `index.html`, find and replace:
- `YOUR_FORM_ID` (if adding Formspree for email capture)
- Calendly link is already set: `https://calendly.com/inboundai/20min`
- Demo number is already set: `(832) 281-5911`
- Stripe link is already set

### 5. Test Before Launch
- [ ] Call (832) 281-5911 — confirm demo works
- [ ] Click "Book a Call" — confirm Calendly loads
- [ ] Run ROI calculator — confirm math
- [ ] Test on mobile — confirm mobile CTA bar shows
- [ ] Test FAQ accordions open/close

## After Launch
- Add Google Analytics (paste tag before `</head>`)
- Submit to Google Search Console
- Add `og:image` meta tag for social sharing
