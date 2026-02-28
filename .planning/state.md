# State — Gallea & Rohner Interactive Quarto Site

**Last updated**: 2026-02-28
**Current phase**: Phase 3 complete — Site deployed to GitHub Pages
**Live URL**: https://qgallea.github.io/gallea-rohner-interactive/

## Progress

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 0: Setup | 🟢 Complete | Structure, config, skills, skeleton pages |
| Phase 1: Data Foundation | 🟢 Complete | 6 Python scripts, all JSON files generated |
| Phase 2: Core Pages | 🟢 Complete | All 7 pages with OJS interactivity |
| Phase 3: Deploy | 🟢 Complete | Git repo + GitHub Pages live |
| Phase 4: Workshop Package | 🔴 Not started | — |

## Data Files Status

| File | Status | Size | Location |
|------|--------|------|----------|
| `chokepoints.json` | 🟢 | 1.5 KB | `site/data/` |
| `conflict_events.json` | 🟢 | 607 KB | `site/data/` |
| `trade_openness.json` | 🟢 | 1.8 KB | `site/data/` |
| `marginal_effects.json` | 🟢 | 49 KB | `site/data/` |
| `regional_panels.json` | 🟢 | 158 KB | `site/data/` |
| `world-110m.json` | 🟢 | 105 KB | `site/data/` |

## Page Status

| Page | File | OJS | Data | Polish |
|------|------|-----|------|--------|
| Home | 🟢 `index.qmd` | N/A (static) | N/A | 🟢 |
| Map | 🟢 `map.qmd` | 🟢 D3 map + toggle | 🟢 3 JSON files | 🟢 |
| Mechanism | 🟢 `mechanism.qmd` | 🟢 interactive diagram | N/A | 🟢 |
| **Slider** | 🟢 `slider.qmd` | 🟢 **full OJS** | hardcoded | 🟢 |
| Evidence | 🟢 `evidence.qmd` | 🟢 tables + comparison | hardcoded | 🟢 |
| Policy | 🟢 `policy.qmd` | 🟢 trade timeline | 🟢 trade_openness.json | 🟢 |
| About | 🟢 `about.qmd` | N/A (static) | N/A | 🟢 |

## Key Variable Names (from globalization_data.dta)

- `tradeworld` — world trade openness (NOT `tradew` as in do-file)
- `near_dist` — log proximity to nearest choke point
- `trade_lin` — interaction term (near_dist x tradeworld)
- `conflict` — binary conflict indicator
- `gid` — grid cell ID
- `xcoord` / `ycoord` — longitude / latitude

## Decisions Made
- Quarto + GitHub Pages (not single-file HTML)
- Observable JS for interactivity (native Quarto, no build step)
- D3.js for map, OJS Inputs for slider
- Litera base theme + custom SCSS
- Paper's blue/red color palette
- One page per section (navbar navigation)
- Trade openness median = 0.5177 (computed from data)
