# /build-page

Create or update a Quarto `.qmd` page for the site.

## Usage
```
/build-page [page-name]
```

## Pages
- `index` — Landing page with hero, hook, key numbers
- `map` — Interactive D3 world map with choke points + conflict toggle
- `mechanism` — Animated causal diagram (game theory intuition)
- `slider` — THE trade openness slider with marginal effects chart
- `evidence` — Regression table + coefficient visualizations
- `policy` — Collective action / policy implications
- `about` — Authors, citation, data availability

## Process
1. Read `.claude/skills/quarto-observable/SKILL.md` for OJS patterns
2. Read `.claude/agents/quarto-dev.md` for conventions
3. Read `.claude/agents/design-director.md` for storytelling + design
4. Check that required data exists in `site/data/`
5. Create or update `site/[page-name].qmd`
6. Run `cd site && quarto render [page-name].qmd` to verify it compiles
7. Update `.planning/state.md`

## Quality Checks
- [ ] YAML frontmatter has `title:` and `description:`
- [ ] OJS cells have `//| echo: false`
- [ ] All `FileAttachment()` paths resolve correctly
- [ ] Visualizations are responsive (use `viewBox`, not fixed px)
- [ ] Numbers match the paper exactly
- [ ] Page renders without errors: `quarto render site/[page].qmd`
- [ ] Prose is editorial, not academic (think Pudding.cool, not LaTeX)
