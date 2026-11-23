---
name: flatsome-ux-builder
description: Expert engineering, design standards, shortcode architecture, and visual editing guidelines for WordPress Flatsome theme and UX Builder.
---

# 🎨 Flatsome & UX Builder — Standard Operating Procedure & Skill

## 📌 Overview
This skill governs the development, editing, and architectural rules for WordPress websites built on the **Flatsome Theme** and its native visual editor **UX Builder**. It enforces strict standards ensuring all graphics, banners, and layout blocks are 100% editable by non-technical clients and site owners via the visual UI.

---

## ⭐️ THE IRON RULE OF EDITABLE BANNERS & GRAPHICS

### 🚫 Categorical Ban on Hardcoded Inline HTML Images
- **CATEGORICALLY FORBIDDEN:** Inserting raw `<img src="...">` tags or CSS `background-image: url(...)` inside text areas or HTML blocks for main banners, hero sections, and category cards.
- **Why:** Hardcoded HTML images do not integrate with the UX Builder inspector. When a client (e.g. Tatiana or Vladimir) clicks the image in the visual editor, no "Change Image / Replace" setting appears in the left panel, making image replacement impossible without code editing.

### ✅ Mandatory Native Flatsome Shortcodes
All images and banners MUST be registered in the WordPress Media Library and referenced exclusively via native Flatsome shortcodes:
1. **Full-width and section banners:**
   ```html
   [ux_banner height="280px" height__sm="340px" bg="MEDIA_ID" bg_color="#f7f2ee" border="1px 1px 1px 1px" border_color="#ebd9d4" border_radius="12"]
     [text_box width="60" width__sm="92" position_x="5" position_y="50" text_align="left"]
       ...
     [/text_box]
   [/ux_banner]
   ```
2. **Standalone visual images:**
   ```html
   [ux_image id="MEDIA_ID" height="340px" image_size="medium" depth="2" border_radius="12"]
   ```
3. **Interactive category cards:**
   ```html
   [ux_image_box img="MEDIA_ID" link="/category-slug/" text_padding="12px 0px 5px 0px"]
     <h4 style="font-size: 16px; font-weight: 700; color: #2c1a16; margin: 0;">Category Name</h4>
   [/ux_image_box]
   ```

---

## 💎 TYPOGRAPHY READABILITY & GLASSMORPHISM STANDARDS

When typography is placed over photography, high contrast and legibility are mandatory across all viewport sizes.

### Frosted Glass Card Standard (Glassmorphism)
Wrap headline and descriptive text inside an elegant semi-transparent frosted card:
```html
<div style="background: rgba(255, 255, 255, 0.92); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); padding: 24px 28px; border-radius: 12px; box-shadow: 0 6px 24px rgba(44, 26, 22, 0.10); border: 1px solid rgba(235, 217, 212, 0.9);">
  <span style="display: inline-block; font-size: 12px; font-weight: 700; letter-spacing: 1.5px; text-transform: uppercase; color: #d26e4b; margin-bottom: 6px;">CATEGORY / OVERTITLE</span>
  <h1 style="font-size: 28px; font-weight: 700; color: #2c1a16; margin: 0 0 8px 0; font-family: Merriweather, serif; line-height: 1.25;">Main Title</h1>
  <p style="font-size: 14.5px; color: #55413d; margin: 0 0 16px 0; line-height: 1.55;">Clear, high-contrast descriptive text.</p>
  [button text="Action Button →" link="/target-url/" color="secondary" radius="25" size="small"]
</div>
```

---

## 🎨 ALPHA GRADIENT BANNER GENERATION

For banners that blend photos smoothly into solid or pastel background colors:
1. **Resolution:** 1600x520 for wide hero banners; 1200x500 for 2-column banners.
2. **S-Curve (Cosine) Transition:** Never use harsh linear cutoffs. Build smooth mathematical cosine alpha masks:
   ```python
   # Smooth cosine alpha mask in Python Pillow
   t = (x - fade_start_x) / (fade_end_x - fade_start_x)
   alpha = int(255 * (0.5 - 0.5 * math.cos(t * math.pi)))
   ```
3. **Registration:** Always import generated images into WordPress via WP-CLI:
   ```bash
   sudo -u wowflow wp media import /path/to/banner.jpg --porcelain
   ```

---

## 🧩 UX BLOCKS & MULTILINGUAL ARCHITECTURE

Reusable sections (Footers, Category Headers, Sticky bars, Callouts) must be created as **UX Blocks** (`post_type=blocks`).

### Key Rules for UX Blocks:
1. **Author Assignment:** Always set `post_author=1` (or active admin user) so blocks appear in WordPress Admin ➔ UX Blocks.
2. **Polylang Synchronization:**
   - Create separate UX Blocks per language (e.g. `Footer_CZ`, `Footer_RU`, `Footer_EN`).
   - Assign Polylang taxonomy term: `pll_set_post_language($block_id, 'cs')`.
3. **Flatsome WooCommerce Category Hooks:**
   - Flatsome category archives support native top and bottom UX blocks via term metadata:
     - `cat_meta['cat_header'] = '[block id="block_slug"]'`
     - `cat_meta['cat_footer'] = '[block id="block_slug"]'`

---

## 📱 MOBILE RESPONSIVENESS & BREAKPOINTS

Flatsome utilizes suffix classes/attributes for mobile:
- `height="280px" height__sm="360px"`
- `width="60" width__sm="92"`
- `span="6" span__sm="12"`
- Always test layouts down to 360px mobile viewports.
