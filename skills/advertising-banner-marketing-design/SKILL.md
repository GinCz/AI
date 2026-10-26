---
name: advertising-banner-marketing-design
description: >-
  Digital advertising design, marketing banner production, conversion rate optimization (CTR), visual hierarchy, ad formats for Google Display Network, Meta, LinkedIn, animated HTML5 banners, and A/B test creative engineering.
---
# Digital Advertising Design, Marketing Banners & Visual Conversion Engineering

A production manual for designing high-converting digital ad creatives, Google Display banners, social media marketing assets (Meta, Instagram, LinkedIn), animated HTML5 banners, visual hierarchy, and programmatic ad export workflows.

---

## 1. Visual Hierarchy & The 3-Second Conversion Rule

### A. The Three-Second Cognitive Filter:
Users scrolling social media or browsing websites scan ad creatives in under 1.5–3 seconds. The design must communicate value instantaneously through a strict visual hierarchy:
1. **The Hook / Primary Visual (40%–50% area)**: High-contrast product hero render, human emotional face, or bold pattern capturing eye saccades.
2. **The Headline / Core Value Proposition (30% area)**: Concise text (maximum 5–7 words) addressing a concrete pain point or quantifiable benefit (e.g., "Cut Cloud Costs by 45%").
3. **The Call-to-Action (CTA) Button (15%–20% area)**: Distinct button styling with high-contrast color differing from the background; action-oriented copy ("Start Free Audit", "Deploy in 60s").
4. **Trust Anchor / Social Proof (5% area)**: Subtle star ratings, security badges (ISO 27001, PCI DSS), or partner logos boosting credibility.

### B. The F-Pattern & Z-Pattern Scanning Paths:
- **Display Banners (Horizontal 728x90, 970x250)**: Left-to-right Z-pattern: Logo top-left -> Value proposition center -> CTA button far-right.
- **Feed Creatives (1080x1080, 1080x1350, 9:16 Stories/Reels)**: Vertical top-down scan: Headline Hook at eye level -> Hero demonstration center -> Floating sticky CTA bottom third.

---

## 2. Standardized Dimensional Specifications

### A. Google Display Network (GDN) Standard Sizes:
- **Leaderboard**: `728 x 90 px` (Desktop top banner).
- **Medium Rectangle (MPU)**: `300 x 250 px` (Universal high-CTR inventory for both mobile and desktop).
- **Large Rectangle**: `336 x 280 px`.
- **Half Page / Double Billboard**: `300 x 600 px` (Dominant vertical desktop real estate).
- **Billboard**: `970 x 250 px` (Premium desktop masthead).
- **Mobile Leaderboard**: `320 x 50 px` and `320 x 100 px` (Mobile sticky banner).
- *Technical Constraint*: Maximum file size for GDN static/HTML5 assets is strictly **150 KB**.

### B. Social Media Ad Inventory (Meta, LinkedIn, X):
- **Square (1:1)**: `1080 x 1080 px` (Universal feed format across Instagram, Facebook, LinkedIn).
- **Portrait (4:5)**: `1080 x 1350 px` (Maximum vertical feed real estate in mobile app feeds without truncation).
- **Vertical Fullscreen (9:16)**: `1080 x 1920 px` (Instagram Stories, Reels, YouTube Shorts, TikTok). Safe zones: Keep critical text 250px away from top and bottom to avoid native UI overlays (username, caption, share buttons).

---

## 3. High-Performance HTML5 Animated Banners

### A. Technical Architecture & Constraints:
- Lightweight CSS3 animations and GreenSock Animation Platform (GSAP) over heavy animated GIFs.
- Maximum 15-second loop duration; animation must stop completely after 30 seconds (IAB standards).
- Zero external CDN dependencies that fail offline ad validation: Fonts embedded as WOFF2 base64 or converted into vector SVG paths.
- Mandatory 1px solid gray/dark border (`#CCCCCC` or `#333333`) around banners with white or light backgrounds to separate creative from publisher page content.

### B. Automated Asset Generation via Sharp / ImageMagick:
```bash
# Resize and compress hero product image to exact 300x250 web asset under 150KB
magick hero_render.png -resize 300x250^ -gravity center -extent 300x250 -quality 85 -strip banner_300x250.webp
```

