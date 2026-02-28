# Skill: Econometrics Results Display

## Purpose
Transform standard econometric outputs (regression tables, marginal effects, CIs) into visually compelling, interactive web elements that non-economists can understand.

## Translating Table 2 for the Web

The paper's Table 2 is the core evidence. Here's how to present each element:

### Coefficient Display
Instead of a raw LaTeX table, show coefficients as **visual magnitudes**:
- Bar chart where bar length = coefficient magnitude
- Color: blue for positive, red for negative
- Stars replaced by CI whiskers (more informative)
- Hover for exact values + interpretation in plain English

### Interactive Table
If showing the traditional table:
- Highlight the row being discussed (proximity, interaction)
- Click a coefficient → expand to show:
  - What it means in words
  - The magnitude in real-world terms (e.g., "1,100 km ≈ Paris to Rome")
  - Visual: small inline marginal effect chart
- Gray out less important rows (observations, R², FE indicators)

### Significance Communication
- Never rely solely on stars (***). Use:
  - CI bands in charts (visual)
  - "Statistically significant at the 1% level" in tooltip text
  - Color intensity to encode precision (darker = more precise)

## The Interaction Effect — Making It Intuitive

### The "Two Worlds" Framing
Present the interaction as two contrasting scenarios:

**World 1: Low Globalization (trade = 0.40)**
```
ME = 0.0148 - 0.0277 × 0.40 = +0.0037
→ Each 1,100 km closer to strait = +25% conflict risk
→ Visual: red-tinted map, conflict dots clustering near straits
```

**World 2: High Globalization (trade = 0.60)**
```
ME = 0.0148 - 0.0277 × 0.60 = -0.0018
→ Each 1,100 km closer to strait = -12% conflict risk
→ Visual: blue-tinted map, conflict dots dispersed away from straits
```

### The Crossover Story
- ME = 0 at trade ≈ 0.534
- This is the "tipping point" where globalization neutralizes the strategic curse
- Annotate this on the slider chart with a vertical line + label
- Historical context: world trade openness crossed this threshold in the mid-2000s

## Fixed Effects Explanation (for non-specialists)
If the site includes a methodology section, explain FE visually:
- **Year FE**: "We account for global events like 9/11 or the 2008 crisis"
- **Country FE**: "We compare locations *within* the same country" (Medellin vs. Bogota)
- **Cell FE**: "We compare the *same location* across time" (55km grid cell)
- Use a small animated diagram showing what "variation" remains after each FE

## Numbers to Always Have Ready

| Metric | Value | Context |
|--------|-------|---------|
| Baseline conflict risk | 1.5% | Per cell-year |
| 1 SD proximity | 1,100 km | Paris→Rome, NYC→Chicago |
| Observations | 1,944,540 | 64,818 cells × 30 years |
| Grid cell size | 55 × 55 km | At equator |
| Time span | 1989–2018 | 30 years |
| Low trade example | 0.40 | Early 1990s |
| High trade example | 0.60 | Mid-2000s peak |
| Crossover trade | ~0.534 | ME = 0 |
