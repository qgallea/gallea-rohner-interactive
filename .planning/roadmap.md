# Roadmap — Gallea & Rohner Interactive Quarto Site

## Phase 0: Setup ✅
- [x] Project structure created
- [x] CLAUDE.md written
- [x] Skills, agents, commands defined
- [x] `_quarto.yml` configured
- [x] Custom SCSS theme created
- [x] Skeleton `.qmd` pages created
- [x] Paper PDF in `raw_data/paper/`
- [ ] Git repo initialized + GitHub remote added
- [ ] Quarto installed and verified (`quarto check`)

## Phase 1: Data Foundation (code_build/)
**Goal**: Get all data into web-ready JSON in `site/data/`.

- [ ] 1.1 Download replication data from Harvard Dataverse
- [ ] 1.2 Catalog replication package contents
- [ ] 1.3 `01_extract_chokepoints.ipynb` → `site/data/chokepoints.json`
- [ ] 1.4 `02_extract_conflicts.ipynb` → `site/data/conflict_events.json`
- [ ] 1.5 `03_trade_openness.ipynb` → `site/data/trade_openness.json`
- [ ] 1.6 `04_marginal_effects.ipynb` → `site/data/marginal_effects.json`
- [ ] 1.7 `05_regional_panels.ipynb` → `site/data/regional_panels.json`
- [ ] 1.8 Download world TopoJSON (Natural Earth 110m) → `site/data/world-110m.json`

**Deliverable**: All JSON files in `site/data/`, each under size target.

## Phase 2: Core Pages (site/)
**Goal**: Build each .qmd page with working OJS interactivity.

- [ ] 2.1 `slider.qmd` — THE slider (already has OJS code, needs data wiring)
- [ ] 2.2 `map.qmd` — D3 world map with choke points + toggle
- [ ] 2.3 `mechanism.qmd` — Animated causal diagram (upgrade from text boxes)
- [ ] 2.4 `evidence.qmd` — Interactive regression tables
- [ ] 2.5 `index.qmd` — Polish hero page
- [ ] 2.6 `policy.qmd` — Add trade openness timeline chart
- [ ] 2.7 `about.qmd` — Finalize

**Deliverable**: All pages render with `quarto preview`.

## Phase 3: Polish & Deploy
**Goal**: Ship it live on GitHub Pages.

- [ ] 3.1 Visual consistency pass (SCSS tweaks, spacing, colors)
- [ ] 3.2 Responsive design check (1024px, 768px)
- [ ] 3.3 Performance: lazy-load map data, check total bundle size
- [ ] 3.4 Accessibility: alt text, keyboard nav, ARIA labels
- [ ] 3.5 `quarto render` — full clean build
- [ ] 3.6 `quarto publish gh-pages` — deploy live
- [ ] 3.7 Verify live URL works

**Deliverable**: Live site at `https://qgallea.github.io/gallea-rohner-interactive/`

## Phase 4: Workshop Packaging
- [ ] 4.1 Record build time (screenshot timestamps)
- [ ] 4.2 Write 2-minute demo script
- [ ] 4.3 Create before/after slide (static paper → interactive site)
- [ ] 4.4 Prepare "try it yourself" prompt for participants
