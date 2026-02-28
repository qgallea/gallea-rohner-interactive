# Skill: Quarto + Observable JS

## Purpose
Guide creation of interactive data visualizations inside Quarto `.qmd` files using Observable JS (OJS). This is the primary interactivity mechanism — no custom build steps, no React, no npm.

## How OJS Works in Quarto

### Basic OJS Cell
In a `.qmd` file, use fenced code blocks with `{ojs}`:

````qmd
```{ojs}
viewof tradeOpenness = Inputs.range([0.35, 0.60], {
  value: 0.47,
  step: 0.001,
  label: "World Trade Openness"
})
```
````

### Key OJS Concepts
- **Reactive**: cells re-run automatically when dependencies change
- **viewof**: creates an input and exposes its value. `viewof x = ...` creates both `viewof x` (the DOM element) and `x` (the current value)
- **FileAttachment**: loads data files relative to the `.qmd` file
- **d3**, **Plotly**, **htl** are available by default in Quarto OJS
- Cells are **topologically ordered** — define in any order, Quarto sorts dependencies

### Loading Data

```{ojs}
// Load JSON from site/data/
chokepoints = FileAttachment("data/chokepoints.json").json()
conflicts = FileAttachment("data/conflict_events.json").json()
tradeData = FileAttachment("data/trade_openness.json").json()
```

### Passing Python Data to OJS

In a Python cell, use `ojs_define()`:

````qmd
```{python}
import json
import pandas as pd

df = pd.read_csv("data/some_data.csv")
ojs_define(myData = df.to_dict(orient='records'))
```

```{ojs}
// myData is now available as a JS array of objects
myData
```
````

## Pattern: Interactive Slider + Dynamic Chart

This is THE core pattern for the marginal effects slider:

````qmd
```{ojs}
//| echo: false

// --- THE SLIDER ---
viewof tradeOpenness = Inputs.range([0.35, 0.60], {
  value: 0.47,
  step: 0.001,
  label: "World Trade Openness (share of GDP)"
})

// --- MARGINAL EFFECT COMPUTATION ---
beta1 = 0.0148
beta2 = -0.0277
me = beta1 + beta2 * tradeOpenness
baselineRisk = 0.015

// --- DYNAMIC TEXT ---
htl.html`<div class="data-callout">
  <strong>Marginal effect</strong>: ${me > 0 ? '+' : ''}${me.toFixed(4)}
  <br>
  <strong>Interpretation</strong>: Being 1,100 km closer to a choke point
  ${me > 0
    ? `<span class="color-conflict">increases</span> conflict risk by ${(me / baselineRisk * 100).toFixed(1)}% of baseline`
    : `<span class="color-peace">decreases</span> conflict risk by ${Math.abs(me / baselineRisk * 100).toFixed(1)}% of baseline`
  }
</div>`

// --- THE CHART ---
{
  const width = 700;
  const height = 350;
  const margin = {top: 30, right: 40, bottom: 50, left: 60};

  const tradeRange = d3.range(0.35, 0.601, 0.001);
  const meData = tradeRange.map(t => ({
    trade: t,
    me: beta1 + beta2 * t,
    // Approximate SE (conservative, without covariance)
    se: Math.sqrt(0.0010**2 + t**2 * 0.008**2)
  }));

  const x = d3.scaleLinear()
    .domain([0.35, 0.60])
    .range([margin.left, width - margin.right]);

  const y = d3.scaleLinear()
    .domain([-0.005, 0.007])
    .range([height - margin.bottom, margin.top]);

  const svg = d3.create("svg")
    .attr("viewBox", [0, 0, width, height])
    .attr("width", width)
    .attr("height", height)
    .style("max-width", "100%")
    .style("font-family", "'Source Sans 3', sans-serif");

  // 99% CI band
  const area99 = d3.area()
    .x(d => x(d.trade))
    .y0(d => y(d.me - 2.576 * d.se))
    .y1(d => y(d.me + 2.576 * d.se))
    .curve(d3.curveLinear);

  svg.append("path")
    .datum(meData)
    .attr("d", area99)
    .attr("fill", "#42a5f5")
    .attr("opacity", 0.15);

  // 90% CI band
  const area90 = d3.area()
    .x(d => x(d.trade))
    .y0(d => y(d.me - 1.645 * d.se))
    .y1(d => y(d.me + 1.645 * d.se))
    .curve(d3.curveLinear);

  svg.append("path")
    .datum(meData)
    .attr("d", area90)
    .attr("fill", "#42a5f5")
    .attr("opacity", 0.25);

  // ME line
  const line = d3.line()
    .x(d => x(d.trade))
    .y(d => y(d.me))
    .curve(d3.curveLinear);

  svg.append("path")
    .datum(meData)
    .attr("d", line)
    .attr("fill", "none")
    .attr("stroke", "#1a237e")
    .attr("stroke-width", 2.5);

  // Zero line
  svg.append("line")
    .attr("x1", margin.left).attr("x2", width - margin.right)
    .attr("y1", y(0)).attr("y2", y(0))
    .attr("stroke", "#999")
    .attr("stroke-dasharray", "4,3");

  // Crossover annotation
  const crossover = -beta1 / beta2;
  svg.append("line")
    .attr("x1", x(crossover)).attr("x2", x(crossover))
    .attr("y1", y(-0.004)).attr("y2", y(0.006))
    .attr("stroke", "#7e57c2")
    .attr("stroke-dasharray", "6,3")
    .attr("stroke-width", 1.5);

  svg.append("text")
    .attr("x", x(crossover) + 5)
    .attr("y", y(0.005))
    .attr("fill", "#7e57c2")
    .attr("font-size", "11px")
    .text(`Crossover: ${crossover.toFixed(3)}`);

  // Current position marker
  svg.append("circle")
    .attr("cx", x(tradeOpenness))
    .attr("cy", y(me))
    .attr("r", 6)
    .attr("fill", me > 0 ? "#e53935" : "#43a047")
    .attr("stroke", "white")
    .attr("stroke-width", 2);

  // Axes
  svg.append("g")
    .attr("transform", `translate(0,${height - margin.bottom})`)
    .call(d3.axisBottom(x).ticks(6).tickFormat(d3.format(".2f")))
    .call(g => g.append("text")
      .attr("x", width / 2).attr("y", 40)
      .attr("fill", "#555").attr("text-anchor", "middle")
      .attr("font-size", "13px")
      .text("World Trade Openness"));

  svg.append("g")
    .attr("transform", `translate(${margin.left},0)`)
    .call(d3.axisLeft(y).ticks(6).tickFormat(d3.format("+.3f")))
    .call(g => g.append("text")
      .attr("transform", "rotate(-90)")
      .attr("x", -height / 2).attr("y", -45)
      .attr("fill", "#555").attr("text-anchor", "middle")
      .attr("font-size", "13px")
      .text("Marginal Effect of Proximity"));

  return svg.node();
}
```
````

## Pattern: Interactive Map with Toggle

````qmd
```{ojs}
//| echo: false

// Load data
world = FileAttachment("data/world-110m.json").json()
chokepoints = FileAttachment("data/chokepoints.json").json()
conflicts = FileAttachment("data/conflict_events.json").json()

// Toggle
viewof tradePeriod = Inputs.radio(
  ["High Trade Openness", "Low Trade Openness"],
  {value: "High Trade Openness", label: "Period"}
)

// Filter conflicts
filteredConflicts = {
  const isHigh = tradePeriod === "High Trade Openness";
  return conflicts.filter(d => d.high_trade === isHigh);
}

// Map
{
  const width = 900;
  const height = 500;

  const projection = d3.geoNaturalEarth1()
    .fitSize([width, height], {type: "Sphere"});
  const path = d3.geoPath(projection);

  const svg = d3.create("svg")
    .attr("viewBox", [0, 0, width, height])
    .style("max-width", "100%");

  // Countries
  const countries = topojson.feature(world, world.objects.countries);
  svg.append("g")
    .selectAll("path")
    .data(countries.features)
    .join("path")
    .attr("d", path)
    .attr("fill", "#e8e8e0")
    .attr("stroke", "#ccc")
    .attr("stroke-width", 0.5);

  // Conflict dots
  svg.append("g")
    .selectAll("circle")
    .data(filteredConflicts)
    .join("circle")
    .attr("cx", d => projection([d.lng, d.lat])?.[0])
    .attr("cy", d => projection([d.lng, d.lat])?.[1])
    .attr("r", d => Math.max(1.5, Math.sqrt(d.events) * 1.5))
    .attr("fill", "#e53935")
    .attr("opacity", 0.5);

  // Choke points
  svg.append("g")
    .selectAll("circle")
    .data(chokepoints)
    .join("circle")
    .attr("cx", d => projection([d.lng, d.lat])?.[0])
    .attr("cy", d => projection([d.lng, d.lat])?.[1])
    .attr("r", 8)
    .attr("fill", "none")
    .attr("stroke", "#ff9800")
    .attr("stroke-width", 2.5);

  return svg.node();
}
```
````

## Pattern: Importing Libraries in OJS

```{ojs}
// topojson is not built-in; import it
topojson = require("topojson-client@3")

// For Plotly (if preferred over D3)
Plotly = require("https://cdn.plot.ly/plotly-2.27.0.min.js")
```

## OJS Tips & Gotchas

1. **No `let` / `const` at top level** — OJS cells are implicitly `const`. Just write `x = 5`, not `const x = 5`.
2. **Curly braces for blocks** — Multi-statement cells must be wrapped in `{ ... return ... }`.
3. **`viewof` is special** — `viewof x = Inputs.range(...)` creates BOTH `viewof x` (widget) and `x` (value).
4. **Reactivity is automatic** — if cell B uses variable from cell A, B re-runs when A changes.
5. **`htl.html` for dynamic HTML** — use tagged template literals for reactive text/HTML.
6. **FileAttachment paths** are relative to the `.qmd` file, not the project root.
7. **`//| echo: false`** at the top of an OJS cell hides the code in output.
8. **`d3`** is available globally in Quarto OJS — no import needed.
9. **Large datasets**: prefer aggregated data. Don't load 1.9M rows into the browser.

## File Size Guidelines for OJS Data

| Data | Target size | Strategy |
|------|-------------|----------|
| World TopoJSON | < 200 KB | Use 110m simplified |
| Choke points | < 5 KB | ~15 points with metadata |
| Conflict events | < 300 KB | Aggregate to grid cells |
| Trade openness | < 2 KB | 30 annual values |
| Marginal effects | < 5 KB | Pre-computed curve |
