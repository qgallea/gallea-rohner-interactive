# Project: Gallea & Rohner (2021) — Interactive Research Showcase

## Purpose

This project creates an **interactive Quarto website** deployed on **GitHub Pages** that brings to life the PNAS paper "Globalization mitigates the risk of conflict caused by strategic territory" (Gallea & Rohner, 2021). The site is the flagship demo for a "Claude Code for Research" workshop, showcasing how Claude Code can transform a static academic paper into a dynamic, visual, explorable Quarto site — and deploy it live in minutes.

**The pitch**: "I gave Claude Code my PNAS paper, a dataset, and said 'make it a Quarto website on GitHub Pages.' 20 minutes later, anyone in the world can explore my results interactively."

## The Paper in One Paragraph

Strategic locations near maritime choke points (straits, capes) face higher conflict risk. But globalization *reverses* this: when world trade openness is high, major powers intervene to keep trade routes open, shielding strategic locations from violence. The core empirical result is an interaction: `Marginal Effect = β₁ + β₂ × TradeOpenness`, where β₁ > 0 (proximity increases conflict) and β₂ < 0 (trade dampens this effect). The crossover happens around TradeOpenness ≈ 0.53.

## Key Numbers from the Paper (Table 2, Column 1)

```
β_proximity         = 0.0148  (SE: 0.0010)
β_proximity×trade   = -0.0277 (SE: 0.008)
Baseline conflict    = 0.015 (1.5% unconditional)
1 SD proximity       = 1,100 km
Trade openness range = [0.35, 0.60]
Observations         = 1,944,540
```

**Marginal effect formula**: `ME(trade) = 0.0148 - 0.0277 × trade`
- At low trade (0.40): ME = +0.0037 → +24.8% of baseline
- At high trade (0.60): ME = -0.0018 → -12.1% of baseline
- Crossover (ME = 0): trade ≈ 0.534

## Tech Stack

- **Quarto** (website project) — `.qmd` files with Observable JS (OJS) for interactivity
- **Observable JS** — native Quarto integration for reactive charts (no build step)
- **Plotly.js** via OJS — for the marginal effects slider chart
- **D3.js** via OJS — for the interactive world map
- **Python** code chunks — for data processing within `.qmd` if needed
- **GitHub Pages** — deployment via `quarto publish gh-pages`
- **Custom SCSS** — Quarto theme customization

## Project Structure

```
gallea-rohner-interactive/
├── CLAUDE.md                    # ← You are here
├── .claude/
│   ├── commands/
│   │   ├── build-page.md        # Build/update a .qmd page
│   │   ├── process-data.md      # Transform raw data for viz
│   │   ├── preview.md           # quarto preview
│   │   ├── deploy.md            # quarto publish gh-pages
│   │   └── update-state.md      # Update progress tracker
│   ├── skills/
│   │   ├── quarto-observable/SKILL.md  # Quarto + OJS patterns
│   │   ├── econometrics-display/SKILL.md
│   │   └── map-visualization/SKILL.md
│   └── agents/
│       ├── quarto-dev.md        # Quarto + OJS specialist
│       ├── data-engineer.md     # Data processing for web
│       └── design-director.md   # Visual cohesion & storytelling
├── .planning/
│   ├── roadmap.md
│   └── state.md
├── raw_data/
│   ├── paper/                   # Original paper PDF
│   └── replication_data/        # Harvard Dataverse files
├── data/                        # Processed JSON/CSV for viz
├── code_build/                  # Python notebooks: raw → clean
├── code_run/                    # Python notebooks: analysis
├── site/                        # ← THE QUARTO PROJECT
│   ├── _quarto.yml              # Quarto project config
│   ├── index.qmd                # Landing page / hero
│   ├── map.qmd                  # Interactive world map
│   ├── mechanism.qmd            # Causal mechanism diagram
│   ├── slider.qmd               # THE trade openness slider
│   ├── evidence.qmd             # Regression results
│   ├── policy.qmd               # Policy implications
│   ├── about.qmd                # About authors + citation
│   ├── styles/
│   │   └── custom.scss          # Theme overrides
│   ├── data/                    # JSON data consumed by OJS
│   └── images/                  # Static images, paper figures
└── output/                      # Build artifacts (git-ignored)
```

## How We Work

### Data Pipeline (code_build/)
1. Download replication data from Harvard Dataverse (DOI: 10.7910/DVN/P4RJBC)
2. Each step is a **numbered Jupyter notebook**
3. Raw data in `raw_data/` is **READ-ONLY**
4. Output to `data/` as JSON — then copy/symlink into `site/data/`
5. Key outputs:
   - `chokepoints.json` — lat/lng + name of major maritime choke points
   - `conflict_events.json` — geolocalized conflict events (aggregated to grid)
   - `trade_openness.json` — world trade openness time series
   - `marginal_effects.json` — precomputed ME curve
   - `regional_panels.json` — subsets for Africa, Central America, SE Asia

### Quarto Site (site/)
1. Each major section is its own `.qmd` file
2. Interactive elements use **Observable JS (OJS) blocks** — ` ```{ojs} ` code cells
3. Static elements use standard Quarto markdown
4. Python chunks (`{python}`) can pass data to OJS via `ojs_define()`
5. Data files in `site/data/` loaded with `FileAttachment()` in OJS
6. Navigation via Quarto navbar (defined in `_quarto.yml`)
7. Theme: custom SCSS extending a clean Quarto base theme

### Deployment
```bash
cd site
quarto publish gh-pages
```
Live URL: `https://qgallea.github.io/gallea-rohner-interactive/`

## Pages of the Site (navbar order)

1. **Home** (`index.qmd`): Hero + hook + paper abstract visual
2. **The Map** (`map.qmd`): Interactive D3 world map — choke points + conflict toggle
3. **The Mechanism** (`mechanism.qmd`): Animated causal diagram
4. **Explore** (`slider.qmd`): THE trade openness slider with marginal effects
5. **Evidence** (`evidence.qmd`): Interactive regression table + coefficient plots
6. **Policy** (`policy.qmd`): Collective action argument
7. **About** (`about.qmd`): Authors, citation, data, replication

## Non-Negotiable Rules

1. **Never fabricate data** — all numbers trace to the paper or replication data
2. **Slider math must be exact**: ME = 0.0148 - 0.0277 × trade
3. **Conflict locations must be real** — UCDP GED coordinates
4. **Choke points geographically accurate**
5. **Cite**: "Gallea & Rohner, PNAS 2021" visible on every page footer
6. **Performance**: each page < 3 second load
7. **OJS for interactivity**: use ` ```{ojs} ` cells, not custom JS hacks
8. **Color palette**: paper's blue/red (CSS variables in SCSS)
9. **Accessibility**: alt text, keyboard nav
10. **Quarto conventions**: all config in `_quarto.yml`

## Session Startup Checklist

Every new Claude Code session:
1. Read this CLAUDE.md
2. Read `.planning/state.md`
3. Check `data/` and `site/data/` for JSON files
4. Check `site/*.qmd` for existing pages
5. `cd site && quarto preview` if pages exist
6. Resume from state

## GitHub Setup (first time only)

```bash
git init
git remote add origin git@github.com:qgallea/gallea-rohner-interactive.git
git add -A
git commit -m "Initial project setup"
git push -u origin main

cd site
quarto publish gh-pages
```
