---
name: branding-logo-vector-graphics
description: >-
  Brand identity design, logo engineering, vector graphic standards (SVG, AI, EPS), mathematical bezier curve geometry, typography pairing, color theory (Pantone, CMYK, RGB), and comprehensive corporate brand manuals.
---
# Brand Identity Design, Logo Engineering & Vector Graphic Systems

A master manual for architecting iconic brand marks, geometric vector logos, mathematical bezier curve construction, corporate identity systems, brand guideline manuals, and production-ready vector assets.

---

## 1. Logo Anatomy & Archetype Selection

### A. Structural Logo Archetypes:
1. **Wordmark / Logotype**: Custom typographic rendering of the company name (e.g., Google, Braun, Sony). Focus on letter-spacing (kerning), custom ligatures, and distinctive terminal curves.
2. **Lettermark / Monogram**: Typographic abbreviation or initials (e.g., IBM, HP, CNN). Ideal for multi-word or international corporate entities.
3. **Brandmark / Symbol**: Abstract or pictorial symbol functioning without text (e.g., Apple, Nike, Twitter/X). Requires intense geometric simplicity for micro-scale recognizability.
4. **Combination Mark**: Symbol coupled with a wordmark; must function both lock-stepped together and separated.
5. **Emblem / Crest**: Text encased inside a badge or geometric container (e.g., Porsche, Starbucks, Harley-Davidson).

### B. Golden Ratio & Geometric Grid Construction:
- Construction lines based on Fibonacci ratios (1:1.618), concentric circles, and strict angular constraints (30°, 45°, 60°).
- Optical balance vs Mathematical perfection: Correcting optical illusions (e.g., a triangle placed inside a square must be slightly enlarged and offset to appear centered to the human eye).
- Tangent and curve continuity: Ensuring smooth transitions between curves (G2 curvature continuity) without jagged anchor points or inflection breaks.

---

## 2. Vector Engineering Standards (SVG / EPS / AI)

### A. Anchor Point Optimization & Clean Path Rules:
- Minimum necessary anchor points: Curves should be defined using extreme point anchors (top, bottom, leftmost, rightmost - nodes at extents) with horizontal/vertical control handles whenever possible.
- Closed paths: Zero unjoined endpoints or stray anchor nodes.
- Path boolean operations: Flatten all overlapping strokes into unified solid vectors (Stroke to Outline / Expand Stroke). Remove redundant hidden nodes and coincident paths.

### B. SVG Production Code Standards:
- Clean SVG markup: Removal of proprietary editor metadata (Adobe Illustrator, Inkscape namespace tags).
- ViewBox definition: Always set `viewBox="0 0 W H"` without hardcoded `width` and `height` to ensure fluid scalability.
- Semantic paths and IDs: Grouping logical elements with `<g id="...">` and reusing repetitive vectors with `<defs>` and `<use>`.
- Optimization: Processing through SVGO (precision set to 2-3 decimal places, stripping comments, minifying path data).

---

## 3. Color Space Engineering & Chromatic Systems

### A. Multi-Media Color Mapping:
- **RGB / HEX (Digital Screens)**: sRGB and Display P3 color gamut specifications for web and mobile interfaces.
- **CMYK (Offset & Digital Printing)**: Process ink limits (Total Area Coverage - TAC maximum 300%–320% to prevent ink smearing on coated paper).
- **Pantone Matching System (PMS)**: Spot colors for absolute corporate brand consistency across merchandise, packaging, and fleet livery (e.g., Pantone Formula Guide Coated / Uncoated).
- **Monochrome & High-Contrast Fallbacks**: Every logo MUST render flawlessly in 100% pure black (`#000000`) on white and 100% pure white (`#FFFFFF`) on dark backgrounds without losing structural identity.

---

## 4. Corporate Brand Manual Architecture (Brand Guidelines)

### A. Mandatory Brand Book Sections:
1. **Brand Story & Core Mission**: Vision, values, tone of voice (formal, technical, approachable, disruptive).
2. **Primary Logo Lockup**: Definitive arrangement of symbol and logotype.
3. **Clear Space & Exclusion Zone**: Minimum protective boundary around the logo (typically defined by the height of an element from the logo, e.g., "X-height") where no text or graphics may encroach.
4. **Minimum Reproduction Size**: Smallest permissible dimensions for digital (e.g., 24px height) and print (e.g., 10mm width) ensuring legibility.
5. **Unacceptable Usage / Misuse Matrix**: Visual rules forbidding stretching, skewing, rotating, recoloring outside the palette, applying drop shadows, or placing over busy photo backgrounds.
6. **Typography System**: Primary brand font (headlines), secondary font (body copy), and system fallback font (web-safe stack: Arial, Roboto, Inter).

