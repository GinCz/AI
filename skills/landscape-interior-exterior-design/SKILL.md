---
name: landscape-interior-exterior-design
description: >-
  Architectural spatial planning, landscape architecture, interior and exterior design, 3D photorealistic rendering (Blender, Cycles, Unreal Engine, SketchUp), lighting calculation (Lux/Lumens), ergonomics, and Czech building code zoning standards.
---
# Architectural Spatial Planning, Landscape, Interior & Exterior Design

A master design, architectural visualization, and spatial planning manual covering residential interior ergonomics, exterior facade engineering, outdoor landscape zoning, lighting simulation, and 3D CAD/rendering pipelines.

---

## 1. Residential Interior Architecture & Ergonomics

### A. Spatial Flow & Circulation:
- **Minimum Clear Passages**:
  - Main corridors and hallways: Minimum 900 mm (recommended 1100–1200 mm for dual passage).
  - Kitchen working triangle: Distance between Refrigerator, Sink, and Cooktop should sum to 4.0 m – 7.0 m; minimum clearance between opposing counters is 1200 mm.
  - Door swings: Doors must never swing into main circulation corridors or collide with opposing cabinet doors; 800 mm minimum interior door width.
- **Zoning (Day vs Night Zones)**:
  - Day zone (Kitchen, Dining, Living, Guest WC): Oriented South/West for maximum natural sunlight.
  - Night zone (Bedrooms, Master Bath, Dressing): Oriented East/North for cool sleeping conditions and morning light.
  - Acoustic buffer: Bathrooms, technical rooms, and staircases placed between living areas and master bedrooms.

### B. Material Selection & Tactile Durability:
- **Flooring**:
  - High-traffic / moisture areas (entry hall, kitchen, bathrooms): Porcelain stoneware tile (gres) with R10/R11 slip resistance rating.
  - Living spaces: Engineered hardwood (multi-layer oak with UV oil/matte lacquer finish) or heavy-duty SPC vinyl (0.55 mm wear layer, AC5 rating).
- **Wall Surfaces**:
  - High-durability washable latex paints (Class 1 wet scrub resistance according to EN 13300).
  - Acoustic paneling: Slatted oak/walnut acoustic felt panels (NRC rating >= 0.85) to eliminate reverberation in open-plan spaces.

---

## 2. Lighting Engineering (Lux, Lumens & Color Temperature)

### A. Photometric Standards by Space Type:
- **Workspaces & Kitchen Countertops**: 500 – 750 Lux | CRI (Color Rendering Index) >= 90 | Color Temp: 4000K (Neutral White).
- **Living Rooms & Lounges**: 150 – 300 Lux | CRI >= 85 | Color Temp: 2700K – 3000K (Warm White) for relaxation and melatonin maintenance.
- **Bathrooms**: 300 – 500 Lux general | 500 Lux at mirror (shadowless bilateral facial illumination) | IP44/IP65 ingress protection in wet zones.
- **Bedrooms**: 100 – 200 Lux general ambient | 300 Lux directional reading lamps | Dimmable down to 10% with circadian rhythm modulation.

### B. Layered Lighting Hierarchy:
1. **Ambient / General**: Recessed downlights, magnetic low-voltage track systems (48V), or indirect ceiling cove LED strips (COB LED without visible dots).
2. **Task / Functional**: Under-cabinet LED profiles, pendant fixtures directly above dining tables (750–850 mm above tabletop).
3. **Accent / Decorative**: Narrow-beam spotlights (15°–24° beam angle) highlighting art, textured stone walls, or architectural niches.

---

## 3. Exterior Architecture & Facade Design

### A. Facade Composition & Insulation Standards:
- Thermal envelope (ETICS - External Thermal Insulation Composite System): Mineral wool or graphite EPS (lambda 0.031 W/mK) minimum 160–200 mm thickness.
- Ventilated facade systems: Fiber-cement boards, porcelain slabs, or thermo-wood (Thermo-Ash/Pine) mounted on aluminum substructure with vapor-permeable wind barrier membrane.
- Window systems: Triple-glazed insulated glass units (Ug <= 0.5–0.6 W/m²K), aluminum or wood-aluminum frames, external concealed venetian blinds (*venkovní žaluzie Z-90*) for solar heat gain mitigation.

---

## 4. Landscape Architecture & Outdoor Zoning

### A. Site Planning & Functional Zones:
- **Terrace & Outdoor Living**: Direct flush connection between interior living floor and exterior deck (hidden trench drain channels to prevent water ingress).
- **Private Green Lawn**: Automated underground irrigation (pop-up rotors with rain/soil moisture sensors), robotic mower perimeter planning.
- **Utility / Parking Zone**: Permeable pavers with crushed aggregate joints allowing rainwater infiltration, EV charging station infrastructure (3-phase 11kW/22kW).

### B. Planting Palettes & Microclimate Engineering:
- Windbreak planting on northern perimeter (evergreen conifers: Pinus nigra, Taxus baccata).
- Deciduous shade trees on southern terrace exposure (Carpinus betulus, Acer palmatum) providing shade in summer while allowing low winter sun to penetrate indoors.
- Drought-tolerant perennial borders (Lavandula angustifolia, Salvia nemorosa, ornamental grasses like Calamagrostis and Stipa).

---

## 5. 3D CAD & Visualization Pipeline (Blender / Cycles)

### A. Realistic Scene Construction:
- Photorealistic physically-based rendering (PBR) workflows: Albedo, Roughness, Normal (OpenGL), Metallic, and Displacement maps.
- Lighting setup: Calibrated HDRIs with sun lamp matching exact solar angle, lux-based intensity values, and filmic / AgX tone mapping.
- Camera calibration: Real-world focal lengths (24mm–35mm for interiors, 50mm–85mm for exteriors), two-point perspective with corrected vertical shifts.

