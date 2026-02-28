# State — Gallea & Rohner Interactive Quarto Site

**Last updated**: 2026-02-27 (initial setup)
**Current phase**: Phase 0 complete → Ready for Phase 1
**Blocking issues**: Need to download replication data from Harvard Dataverse

## Progress

| Phase | Status | Notes |
|-------|--------|-------|
| Phase 0: Setup | 🟢 Complete | Structure, config, skills, skeleton pages |
| Phase 1: Data Foundation | 🔴 Not started | Need replication data |
| Phase 2: Core Pages | 🟡 Partial | slider.qmd has OJS code (needs data) |
| Phase 3: Polish & Deploy | 🔴 Not started | — |
| Phase 4: Workshop Package | 🔴 Not started | — |

## Data Files Status

| File | Status | Location |
|------|--------|----------|
| `chokepoints.json` | ❌ | `site/data/` |
| `conflict_events.json` | ❌ | `site/data/` |
| `trade_openness.json` | ❌ | `site/data/` |
| `marginal_effects.json` | ❌ | `site/data/` |
| `regional_panels.json` | ❌ | `site/data/` |
| `world-110m.json` | ❌ | `site/data/` |

## Page Status

| Page | File | OJS | Data | Polish |
|------|------|-----|------|--------|
| Home | 🟢 `index.qmd` | N/A (static) | N/A | 🟡 |
| Map | 🟢 `map.qmd` | 🔴 placeholder | ❌ needs data | 🔴 |
| Mechanism | 🟢 `mechanism.qmd` | 🔴 text only | N/A | 🔴 |
| **Slider** | 🟢 `slider.qmd` | 🟢 **full OJS** | hardcoded ✅ | 🟡 |
| Evidence | 🟢 `evidence.qmd` | 🔴 placeholder | ❌ needs data | 🔴 |
| Policy | 🟢 `policy.qmd` | 🔴 none | ❌ needs data | 🔴 |
| About | 🟢 `about.qmd` | N/A (static) | N/A | 🟡 |

## Decisions Made
- Quarto + GitHub Pages (not single-file HTML)
- Observable JS for interactivity (native Quarto, no build step)
- D3.js for map, OJS Inputs for slider
- Litera base theme + custom SCSS
- Paper's blue/red color palette
- One page per section (navbar navigation)

## Next Steps
1. Download replication data → `raw_data/replication_data/`
2. Run `/process-data all` to generate JSON files
3. Wire `slider.qmd` to real data (currently hardcoded — still correct)
4. Build `map.qmd` with real conflict events
5. `quarto preview` to test everything together
