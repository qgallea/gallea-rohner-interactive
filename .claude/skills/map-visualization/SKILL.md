# Skill: Map Visualization

## Purpose
Build interactive geographic visualizations showing maritime choke points, conflict events, and strategic proximity. The map is the visual centerpiece of the site.

## Key Geographic Data

### Famous Choke Points (must be accurately placed)
| Name | Lat | Lng | Context |
|------|-----|-----|---------|
| Strait of Hormuz | 26.57 | 56.25 | Oil route, Iran tensions |
| Strait of Malacca | 2.50 | 101.50 | Asia-Europe trade, busiest strait |
| Suez Canal | 30.46 | 32.35 | Mediterranean-Red Sea link |
| Panama Canal | 9.08 | -79.68 | Atlantic-Pacific shortcut |
| Strait of Gibraltar | 35.97 | -5.50 | Mediterranean entry |
| Bab el-Mandeb | 12.58 | 43.33 | Red Sea entry, Yemen conflict |
| Strait of Taiwan | 24.00 | 119.50 | US-China flashpoint |
| Cape of Good Hope | -34.36 | 18.47 | Alternative to Suez |
| Strait of Dover | 51.05 | 1.45 | English Channel narrows |
| Turkish Straits | 41.12 | 29.05 | Bosphorus, Black Sea access |
| Strait of Kerch | 45.30 | 36.60 | Russia-Ukraine, 2018 incident |
| Lombok Strait | -8.47 | 115.72 | Alternative to Malacca |

### Proximity Shading (reproducing Fig. 1C)
- Use pre-computed grid: for each land cell, distance to nearest choke point
- Color scale: dark blue (close, <500 km) → light blue → white (far, >3000 km)
- If full grid data unavailable, approximate with distance-to-nearest-point calculation in JS

## Map Technology Choices

### Option A: D3.js + TopoJSON (Recommended for single-file)
```
Pros: No tile server, fully self-contained, precise control
Cons: No zoom/pan (or must implement manually), larger bundle
Best for: The main showcase map with toggle
```

### Option B: Leaflet + OpenStreetMap tiles
```
Pros: Smooth zoom/pan, familiar UX, smaller initial load
Cons: Requires internet for tiles, harder to style, external dependency
Best for: Detailed zoom panels on specific straits
```

### Recommendation
Use **D3.js for the main world map** (self-contained, styleable) and optionally Leaflet for "zoom into Hormuz" detail panels.

## Map Layers (bottom to top)

1. **Base**: World countries (Natural Earth 110m, TopoJSON, ~150KB)
2. **Proximity shading**: Blue gradient overlay on land polygons
3. **Trade routes**: Simplified shipping lane lines (optional, from paper's Fig. 1B concept)
4. **Choke points**: Pulsing orange/yellow circles at key straits
5. **Conflict events**: Red dots, size ∝ event count, opacity by period
6. **Labels**: Strait names on hover, country borders subtle

## The High/Low Trade Toggle

### Implementation
- Pre-filter conflict events into two groups:
  - `high_trade_events`: years where world trade openness > median (~0.48)
  - `low_trade_events`: years where world trade openness ≤ median
- Toggle button or animated switch
- On toggle: D3 transition — dots fade in/out with 500ms transition
- Key visual: near choke points, low-trade should show MORE red dots

### Regional Zoom Panels (from paper's Fig. 2)
Recreate the paper's four panels:
1. Africa (Cape of Good Hope + East Africa) — High trade
2. Africa — Low trade
3. Central America (Panama Canal) — High trade
4. Central America — Low trade

Show these as clickable inset maps or a carousel.

## Performance Optimization
- World TopoJSON: simplify to < 200KB (topojson-simplify)
- Conflict events: aggregate to grid cells, not individual events
  - Max ~5,000 dots on map at once (more = sluggish)
  - Use canvas rendering for dots if > 2,000
- Lazy load: map renders only when scrolled into view
- Pre-render proximity shading as a single image overlay if computation is too heavy

## Accessibility
- All map elements have `role="img"` with descriptive `aria-label`
- Provide text alternative below map: "Map showing X conflict events near Y choke points"
- Color-blind safe: don't rely solely on red/blue distinction — use shapes + opacity too
