---
name: ui-ux-gui-design-systems
description: >-
  Enterprise UI/UX design, cross-platform GUI architecture (Web, Desktop WPF/WinUI/Qt, Mobile Android/iOS), design systems, atomic design tokens, accessibility (WCAG 2.2 AAA), typography scales, layout grids, and interactive prototyping.
---
# Enterprise UI/UX & GUI Design Systems Engineering

A master engineering and aesthetic manual for architecting high-performance, accessible, and scalable graphical user interfaces (GUI), modern design systems, cross-platform user experience (UX) flows, and production-ready component libraries.

---

## 1. Design System Architecture & Atomic Design

### A. Token Hierarchy (Design Tokens):
- **Global / Primitive Tokens**: Base values for colors, typography, spacing, shadows, and radii (e.g., `color-blue-500: #0066FF`, `spacing-4: 16px`, `radius-md: 8px`).
- **Semantic / Alias Tokens**: Purpose-driven tokens mapping primitives to systemic roles (e.g., `surface-primary: {color-neutral-900}`, `text-interactive: {color-blue-500}`, `border-focus: {color-cyan-400}`).
- **Component-Specific Tokens**: Scoped to discrete UI elements (e.g., `button-primary-bg: {surface-interactive}`, `card-elevation-hover: {shadow-lg}`).
- **Format Delivery**: Tokens defined in JSON format compliant with Design Tokens Community Group (DTCG) specification; compiled via Style Dictionary into CSS variables, SCSS, Android Compose XML/Themes, and TypeScript theme interfaces.

### B. Atomic Component Taxonomy:
1. **Atoms**: Fundamental HTML/native elements (Buttons, Inputs, Checkboxes, Icons, Badges, Typography primitives).
2. **Molecules**: Simple groups of atoms functioning as a single unit (Search input with submit button, Form field with label and helper text, Notification toast).
3. **Organisms**: Distinct UI sections composed of molecules (Global navigation bar, Data table with sorting/filtering headers, Modal dialog).
4. **Templates**: Page-level wireframe skeletons defining content placement and responsive layout grids.
5. **Pages**: Instantiated templates populated with real data, handling empty, loading, error, and populated states.

---

## 2. Layout Grids, Responsive Breakpoints & Spatial Systems

### A. 8-Point Spatial Grid:
- All dimensions, paddings, margins, and line heights follow strict multiples of 8px (with 4px half-grid for dense components like badges, icons, and toolbars).
- Prevents sub-pixel rendering blur on high-DPI displays (Retina, 4K).
- Vertical rhythm: Line heights aligned to baseline grid of 4px/8px to eliminate layout shift during async font loading.

### B. Responsive Viewport Strategy:
- **Mobile First (`< 640px`)**: Single-column layout, bottom sheets instead of modals, touch target sizes minimum `48x48px` (WCAG 2.5.5).
- **Tablet (`640px - 1024px`)**: Fluid 8-column grid, responsive sidebars collapsible into drawer panels.
- **Desktop (`1024px - 1440px`)**: 12-column grid, 24px gutters, max-width container constraints (`1280px` or fluid with fixed max).
- **Ultra-Wide (`> 1440px`)**: Content clamping (`clamp()`), side rail navigation, multi-column dashboard widgets to avoid excessive horizontal eye strain.

---

## 3. Typography Scales & Visual Hierarchy

### A. Modular Typography Scale (Major Third - 1.250 or Perfect Fourth - 1.333):
- **Display / H1**: 32px – 48px | Line Height: 1.15 – 1.25 | Bold / Extra Bold (Page hero titles).
- **Heading H2 / H3**: 20px – 28px | Line Height: 1.3 | Semi-Bold (Section dividers, modal headers).
- **Body Large**: 16px – 18px | Line Height: 1.5 – 1.6 | Regular / Medium (Lead paragraphs, article text).
- **Body Regular**: 14px – 15px | Line Height: 1.5 | Regular (Standard UI text, tables, form fields).
- **Caption / Microcopy**: 12px – 13px | Line Height: 1.4 | Medium (Timestamps, helper hints, badges).

### B. Contrast & Accessibility Standards (WCAG 2.2):
- **Level AA**: Minimum 4.5:1 for regular text (< 18px), 3:1 for large text (>= 18px bold or >= 24px) and UI components/borders.
- **Level AAA**: Minimum 7:1 for normal text, 4.5:1 for large text.
- Focus Indicators: Unambiguous focus ring minimum 2px solid with 3:1 contrast ratio against adjacent background, never disabled with `outline: none` without replacement.

---

## 4. Cross-Platform Framework Implementation

### A. Web (React / Vue / Next.js / Tailwind CSS):
- Strict semantic HTML (`<nav>`, `<main>`, `<article>`, `<dialog>`, `<section>`).
- Headless accessible components (Radix UI, Headless UI, Ark UI) coupled with Tailwind CSS design tokens.
- Light/Dark theme switching via CSS variables and `prefers-color-scheme` media query.

### B. Modern Android GUI (Jetpack Compose):
- Single source of truth Theme utilizing `MaterialTheme` with custom color schemes and typography shapes.
- Modifiers chaining order: `Modifier.clickable().padding().background()` vs `Modifier.background().padding().clickable()`.
- Dynamic color support (Material You Monet engine) with fallback to custom brand palette.

### C. Desktop GUI (WPF / WinUI 3 / Qt):
- Hardware accelerated rendering, DPI awareness per monitor (`PerMonitorV2`).
- Asynchronous UI binding (MVVM architecture), avoiding UI thread blocking on data retrieval.

