# Communication Review: Gallea & Rohner Interactive Research Site

**Reviewer perspective**: Science communication, UX design for academic websites, data storytelling
**Date**: 2026-02-28
**Site reviewed**: `c:\Users\qgallea\Dropbox\PhD\gallea-rohner-interactive\site\`
**Live URL**: https://qgallea.github.io/gallea-rohner-interactive/

---

## 1. Narrative Flow

### Overall Arc

The site follows a seven-page structure through the navbar:

**Home -> The Map -> Mechanism -> Explore -> Evidence -> Policy -> About**

This ordering is logical and largely effective. It follows a classic science-storytelling arc:

1. **Hook** (Home) -- "Does globalization make conflict better or worse?"
2. **Show the world** (Map) -- "Here's where the action is"
3. **Explain the theory** (Mechanism) -- "Here's why"
4. **Let the reader explore** (Slider) -- "See for yourself"
5. **Present the proof** (Evidence) -- "Here are the numbers"
6. **So what?** (Policy) -- "Here's why it matters now"
7. **Credits** (About) -- "Who did this, how to cite"

This mirrors the structure used by The Pudding and Our World in Data: ground the reader visually, build intuition, then let them explore before presenting formal evidence. That is a sound editorial choice.

### Strengths

- The **Map-before-Evidence** ordering is excellent. Showing conflict dots near choke points before explaining regression coefficients gives the reader a visual anchor. When they later see "0.0148" in a table, they've already seen what that number *looks like* on a map.
- The **Mechanism page as a bridge** between "here's the pattern" (Map) and "here's the quantification" (Slider) is well-placed. It answers "but *why*?" before asking the reader to engage with coefficients.
- The **Slider page** ("Explore") is correctly positioned as the centerpiece -- after theory and before formal evidence. This is the "aha moment" and it earns its prime position.

### Weaknesses

- **No explicit cross-page transitions.** Each page ends with a blockquote link like `> [Explore the map](map.qmd)` (in `index.qmd`, line 59) or `> [Test this yourself](slider.qmd)` (in `mechanism.qmd`, line 169). These are functional but minimal. Best-in-class scrollytelling sites use transitional sentences: "Now that you've seen where conflict clusters, the natural question is *why*..." The current blockquote links feel like afterthoughts rather than intentional narrative bridges.
- **The Map page has no forward link.** After the map and the "What to look for" callout (`map.qmd`, line 199), the page simply ends. There is no "Next: The Mechanism" prompt. A reader who is not using the navbar may feel stranded.
- **The Evidence page links backward only.** It ends with `> [Play with the slider](slider.qmd)` -- pointing the reader *back* to a page they presumably already visited. It should instead point forward to Policy. This is a navigational dead-end that breaks momentum.
- **The Policy page has no forward link either.** After the trade openness time-series chart, the page ends with a callout box. No link to About, no "Learn more about the authors and data."
- **Quarto's built-in page-navigation is enabled** (`page-navigation: true` in `_quarto.yml`, line 30), which adds Previous/Next arrows at the bottom of each page. This partially mitigates the missing cross-page links, but the automatic arrows lack narrative context.

### Recommendation

Add a 1-2 sentence narrative transition at the end of every page, above the Quarto navigation arrows. Example for `map.qmd`: "The clustering you see is not coincidence -- there is a game-theoretic mechanism that explains it. [Next: The Mechanism](mechanism.qmd)."

---

## 2. Accessibility for Non-Experts

### What Works Well

- **The two-view framing on the Home page** (Lenin vs. Montesquieu, `index.qmd`, lines 47-56) is inspired. Framing the research question as a 300-year-old intellectual debate immediately signals that this is not just a statistics exercise -- it is a debate with human stakes. Using historical names (even with emoji flags) gives non-economists an entry point.
- **The "How to read this chart" callout** on the Slider page (`slider.qmd`, lines 193-196) is well-executed. It defines "blue line," "shaded bands," and "purple dashed line" in plain terms.
- **The collapsible "What do the column headers mean?" callout** on the Evidence page (`evidence.qmd`, lines 14-21) is a smart design pattern: it provides jargon definitions on demand without cluttering the page for experts. This is the kind of progressive disclosure that Our World in Data uses effectively.
- **The "Reading the table" callout** (`evidence.qmd`, lines 62-64) explains standard errors, significance stars, and fixed effects in plain language. This is generous to non-expert readers and necessary.
- **The "Two Worlds" comparison** on the Evidence page (`evidence.qmd`, lines 126-171) is perhaps the single best communication device on the site. It takes abstract coefficients and renders them as a concrete side-by-side: "World 1: Low Globalization" vs. "World 2: High Globalization." The color-coded cards, the monospace marginal effect values, and the plain-English interpretations ("Being 1,100 km closer to a strait increases conflict risk by 24.8% of baseline") are excellent.

### Where Jargon Creeps In

- **"Marginal Effect of Proximity on Conflict"** -- this is the y-axis label on the main chart (`slider.qmd`, line 185) and appears multiple times. "Marginal effect" is economics jargon. A non-expert will not know what it means. Consider: "Change in conflict risk per 1,100 km closer" or "How much does being near a strait change conflict risk?"
- **"FE" is defined but still opaque.** The Evidence page explains "FE stands for fixed effects" (`evidence.qmd`, line 64), but the explanation -- "statistical controls that account for differences across latitudes, countries, or years" -- could be clearer. A non-expert might wonder: *what kind of differences?* Consider adding: "For example, controlling for the fact that some regions are inherently more conflict-prone than others."
- **"Mean dep. var." in the regression tables** (`evidence.qmd`, lines 53 and 114) is not defined anywhere. A general reader will not know what a dependent variable is, let alone its mean. This should either be defined in the callout or replaced with "Average conflict rate."
- **The equation on the Slider page** (`slider.qmd`, lines 11-13) uses LaTeX notation with beta subscripts. While the "In words:" explanation that follows is good, the equation itself may intimidate some readers. Consider presenting the equation *after* the plain-language explanation, not before.
- **"One-sided" violence** (Evidence page tables) -- the column header explanation says "Violence by an organized group against civilians" but the term "one-sided" is UCDP-specific jargon that could confuse readers who might think it means "one country attacking another."
- **"ln(deaths+1)"** -- the log transformation is explained in the collapsible callout as "captures conflict *intensity*, not just occurrence," which is serviceable but does not explain *why* the log transform is used (to handle skewness / extreme values). Consider: "A logarithmic scale that prevents a single massive battle from dominating the results."

### The "Paris to Rome" Analogy

The repeated use of "1,100 km closer (Paris to Rome)" (`slider.qmd`, line 52) as a concrete distance is effective. It translates a standard deviation into something a European reader can visualize. However, for a global audience, a second reference point would help (e.g., "roughly New York to Chicago" or "about the distance from Lagos to Accra"). Currently, the analogy is Eurocentric.

### Recommendation

Create a small glossary callout (collapsible) on the Slider and Evidence pages that defines: marginal effect, standard deviation, standard error, fixed effects, significance stars. This would be a single reusable component, not a wall of text.

---

## 3. Interactive Elements

### The Map (`map.qmd`)

**Strengths:**
- The radio toggle between High/Low trade openness is simple and effective. It directly encodes the paper's core comparison.
- The summary stats bar (conflict cell count, choke point count, period) updates reactively -- good feedback.
- The D3 rendering is clean: Natural Earth projection, appropriately sized conflict dots, orange ring markers for choke points with labels, a proper legend.
- Using circle area proportional to event count (via `Math.sqrt`) is the correct scaling choice for bubble maps.

**Weaknesses:**
- **No tooltip on hover.** The map has no interactivity beyond the toggle. A reader cannot click on a choke point to learn its name, context, or event count. The `chokepoints.json` file includes a `context` field (e.g., "Oil route, Iran tensions") that is never displayed. This is a missed opportunity.
- **No zoom or pan.** With 12 choke points and thousands of conflict dots, the fixed viewport (960x500) means dense regions like the Middle East and East Africa are hard to read. Even a basic zoom-on-click for regional views would help.
- **The toggle is a radio button, not a visual control.** Best practice (see Our World in Data's map explorer) is to use a toggle switch or a slider that is visually integrated with the map, not a separate Quarto Input widget. The current radio button looks like a form element, not a storytelling tool.
- **"High Trade Openness" and "Low Trade Openness" are not defined on this page.** How is high/low determined? The data uses a `high_trade` boolean field. The callout tip says "above/below median" but the actual median value is not given. The reader has to guess what threshold separates the two periods.
- **Conflict dot sizing.** The `conflict_events.json` file is 607 KB -- that is large for a web page. The file contains approximately 8,000+ records. While this is manageable, lazy loading or a simplified version might improve initial load time.

### The Mechanism Diagram (`mechanism.qmd`)

**Strengths:**
- This is genuinely innovative. The causal diagram is not a static image -- the arrow thickness and node colors respond to the trade openness slider in real time. As you increase trade, the "Incentive to Fight" pathway thins while "Major Power Intervention" thickens. This is an excellent use of interactivity for explanation, not decoration.
- The background color shift (warm orange for low trade, green for high trade) provides ambient feedback without requiring the reader to interpret numbers.
- The two side-by-side explanation cards below the diagram (`mechanism.qmd`, lines 142-161) highlight/dim based on the slider, providing redundant encoding (color + text + opacity). This is good accessibility practice.

**Weaknesses:**
- **The slider is not labeled as interactive.** There is no "drag me" prompt or animation cue. A reader might scroll past it thinking it is static.
- **Arrow semantics are not labeled.** The red arrows represent "conflict pathway" and blue arrows represent "intervention pathway," but this is never explicitly stated on the diagram itself. Adding small inline labels on the arrows ("fuels conflict" / "suppresses conflict") would help.
- **The diagram uses the same slider range (0.35-0.60) and tipping point (0.534) as the Slider page but does not reference the Slider page's equation.** A brief note like "This slider controls the same Trade Openness variable you'll explore in detail on the next page" would connect the two.

### The Slider (`slider.qmd`)

**Strengths:**
- This is the crown jewel of the site and it delivers. The slider is smooth, the chart updates in real time, the confidence intervals are correctly computed (using the delta method approximation for SE), and the color-coded zones (red = conflict zone, green = peace zone) are immediately legible.
- The tipping-point detection (`Math.abs(tradeOpenness - crossover) < 0.005`) that triggers a special message when the user finds the crossover is a delightful discovery moment.
- The data-callout bar above the chart provides precise numerical feedback: trade openness value, marginal effect, direction, and percentage relative to baseline. This allows both casual exploration and precise reading.
- The custom SCSS slider styling (gradient background from red through yellow to green, `custom.scss`, lines 123-142) is a nice touch that makes the HTML range input feel purposeful rather than generic.

**Weaknesses:**
- **The slider step size (0.001) is very fine.** On mobile, this makes it difficult to land precisely on the tipping point. Consider adding a "snap to tipping point" button or at least a coarser mobile step size.
- **No historical context overlay.** The chart shows the marginal effect curve but does not indicate *where on this curve the world currently is or has been*. Adding small year markers on the x-axis (e.g., "1990 was here, 2008 was here, 2018 was here") would connect the abstract curve to lived experience. The Policy page does this separately with the time-series chart, but integrating a light version into the Slider page would strengthen the connection.
- **The confidence interval explanation** says "90% and 99% confidence intervals" but does not explain what these mean for a non-expert. A sentence like "If the shaded band crosses the zero line at a given trade level, we cannot be statistically confident that proximity affects conflict at that level" would add interpretive value.

### Missing Interactions

- **Regional zoom on the map.** The `regional_panels.json` file (158 KB) exists in `site/data/` but is never used on any page. This file presumably contains data for Africa, Central America, and SE Asia -- exactly the regions where conflict clustering near choke points would be most vivid. A "Zoom to: Africa / Middle East / SE Asia" button on the Map page would be high-value and the data already exists.
- **Hoverable regression table.** The Evidence page tables are static HTML. Making rows highlight with tooltips explaining each coefficient's real-world meaning would bridge the gap between the abstract table and the concrete implications.
- **Animated transitions on the map toggle.** Currently, switching between High/Low trade redraw the entire SVG. D3's `transition()` API could smoothly animate dots appearing/disappearing, which would make the comparison more visceral.

---

## 4. Visual Design & Consistency

### Color Palette

The SCSS file (`custom.scss`) defines a clear semantic palette:

| Variable     | Color   | Meaning               |
|-------------|---------|----------------------|
| `$danger`   | #e53935 | Conflict / risk      |
| `$success`  | #43a047 | Peace / trade benefit |
| `$warning`  | #ff9800 | Choke point markers  |
| `$info`     | #7e57c2 | Crossover / tipping  |
| `$primary`  | #1a237e | Deep navy (brand)    |
| `$secondary`| #42a5f5 | Proximity / CI bands |

This palette is applied consistently across all pages:
- Red for conflict elements (map dots, "conflict zone" labels, negative marginal effects)
- Green for peace elements ("peace zone" labels, positive trade effects)
- Orange for choke point markers on the map
- Purple for the tipping point line

**This is well done.** The color usage is semantic rather than decorative, which is a hallmark of good data visualization. The reader learns the color code once and can apply it across all pages.

### Typography

The font choices are excellent:
- **Playfair Display** (serif) for headings -- editorial, authoritative, evokes PNAS quality
- **Source Sans 3** (sans-serif) for body text -- highly readable, optimized for screen
- **JetBrains Mono** for data values -- signals "this is a precise number"

The line height (1.7) and font size (1.05rem) are generous and comfortable for extended reading. The paragraph spacing (1.25rem) is appropriate.

**One concern:** Three Google Fonts imports (`custom.scss`, line 4) add to page load time. Source Sans 3 and JetBrains Mono together are approximately 100-200 KB depending on weights. For a performance-conscious site (target: < 3 seconds), this is worth monitoring.

### Layout

- `page-layout: full` (`_quarto.yml`, line 45) gives the site a modern, edge-to-edge feel.
- The `column-page` class is used on the map and slider for wider rendering.
- The `.full-width` CSS class (`custom.scss`, lines 75-83) uses the viewport-width breakout technique for charts -- standard and effective.
- `max-width: 960px` for content is slightly narrow for a data-heavy site. Our World in Data uses ~1100px. The 960px works fine for text but may feel cramped for the regression tables.

### Responsiveness

- SVG elements use `viewBox` with `max-width: 100%`, which is the correct approach for responsive D3 charts.
- The `clamp()` function is used for hero title sizing (`custom.scss`, line 41), providing fluid scaling.
- Flexbox with `flex-wrap: wrap` is used for the key-number stats and two-column comparison cards.
- **However:** the mechanism diagram (`mechanism.qmd`) uses hardcoded pixel coordinates for nodes and arrows (e.g., `x: 170, y: 200`). At narrow viewports (< 500px), labels will overlap and arrows will misalign. This is the weakest point of the responsive design.
- The regression tables use `width: 100%` but do not have horizontal scroll on mobile. Five columns of data with standard errors will overflow on phones.

### Chart Labels

All charts have:
- Axis labels (x and y)
- Legends (map)
- Zone labels ("CONFLICT ZONE" / "PEACE ZONE")
- Tipping point annotations with value

This is thorough. The only missing label is the y-axis on the mechanism diagram, which does not need one since it is a node diagram, not a chart.

### Consistency Issues

- The Home page uses inline `style` attributes extensively (`index.qmd`, lines 6, 16, etc.) rather than CSS classes. While functional, this creates a maintenance issue and diverges from the SCSS-based approach used elsewhere.
- The mechanism diagram cards (`mechanism.qmd`, lines 146-159) use inline styles for colors and padding rather than the `.data-callout` class or custom SCSS classes. This is inconsistent with the Evidence page's "Two Worlds" cards, which also use inline styles but with different border-radius and padding values.

---

## 5. Writing Quality

### Tone

The writing strikes an effective middle ground between academic rigor and journalistic accessibility. It is clear without being dumbed down, and engaging without being sensationalist. Examples:

- **Good**: "The question is which force wins" (`slider.qmd`, line 15) -- simple, direct, creates tension.
- **Good**: "Peace near strategic waterways is currently a byproduct of self-interest, not coordinated policy" (`policy.qmd`, line 8) -- concise, provocative, substantiated.
- **Good**: "This research puts both views to the test. The answer? It depends on how much trade is flowing" (`index.qmd`, line 57) -- rhythmic, uses a setup/punchline structure.

### Sentence Length and Variety

The site generally maintains good sentence variety. Short punchy sentences alternate with longer explanatory ones. The average sentence length appears to be 15-20 words, which is within the ideal range for online reading (15-25 words per the Nielsen Norman Group).

### Use of Bold and Emphasis

Bold is used strategically and not overused:
- Key findings are bolded: "Move the slider to find the tipping point" (`slider.qmd`, line 18)
- Key terms in context: "marginal effect is positive" vs. "marginal effect is negative"
- The Evidence page bolds policy-relevant conclusions

Italic is used sparingly and correctly (for *PNAS*, for emphasis on *up* and *down*).

### Weaknesses

- **The Home page is slightly too sparse.** After the hero section and the Lenin/Montesquieu framing, the page has only two blockquote links. There is no brief summary of the findings, no teaser visualization, no "what you'll learn" preview. Best-in-class landing pages (e.g., Distill.pub articles) include a brief abstract or "in 30 seconds" summary. A reader landing on this page might not understand *what* the paper found -- only that it asked a question.
- **The Policy page is the densest page on the site** and could benefit from subheading restructuring. The "Through the Lens of 2026" section has four subsections (Tariffs, Red Sea, Hormuz, What the Model Predicts) but the writing runs long in places. The Houthi crisis paragraph (`policy.qmd`, lines 37-39) packs too much information into a single sentence: "Traffic through the Suez Canal dropped by roughly 75%, forcing vessels to reroute around the Cape of Good Hope at an additional cost of approximately $1 million in fuel per voyage and 11,000 extra nautical miles." This should be broken into two sentences.
- **Some passages feel like they were written for the workshop pitch rather than the reader.** The About page's "Time to build: ~20 minutes with Claude Code (Opus 4.6)" (`about.qmd`, line 49) is promotional. While this is appropriate for a workshop demo, it may undermine the site's credibility as a standalone research communication tool.

---

## 6. The "Through the Lens of 2026" Section

This section (`policy.qmd`, lines 27-54) is the most ambitious part of the site -- and the most editorially delicate.

### Strengths

- **The tariff analysis is rigorous.** It cites specific numbers (145% on China, 25% on Canada/Mexico, 10% baseline), specific sources (WTO Global Trade Outlook, April 2025), and makes predictions *within the paper's framework* rather than offering independent policy opinions. The key sentence -- "The paper's framework makes a clear prediction here: falling trade openness pushes the world back below the 0.534 tipping point" -- is carefully constructed. It attributes the prediction to "the framework," not to the author or the site.
- **The Red Sea crisis analysis is balanced.** The callout box explicitly acknowledges the model's limitations: "The Houthi crisis both confirms and challenges the model." It notes that major powers *did* intervene but attacks persisted, which is an honest engagement with the framework's boundary conditions. The distinction between "the model predicts *incentives* to intervene... not guaranteed success" is exactly the kind of nuance that separates rigorous application from editorializing.
- **The Hormuz example is timely and specific.** Citing the February 17, 2026 closure and Iran-Russia exercises at Bandar Abbas grounds the analysis in verifiable current events.
- **All contemporary claims are sourced.** WTO report, UNCTAD report, and The National News are all linked. This is essential for credibility.

### Concerns

- **The section title "Tariffs and the Return to the 'Conflict Zone'" is slightly sensationalist.** The scare quotes around "Conflict Zone" help, but the phrase "Return to" implies certainty about a directional shift that is, at this point, a prediction based on one model. Consider: "Tariffs and the Risk of Returning to the 'Conflict Zone'."
- **The Houthi crisis paragraph mentions "over 190 attacks" and "$1 trillion in goods disrupted" without date-stamping the "$1 trillion" figure.** The UNCTAD source is cited as January 2026, but the reader might wonder if this is cumulative since November 2023 or an annual figure.
- **The prediction section** ("If tariffs and deglobalization continue to depress world trade openness, the framework predicts a dangerous trajectory") could be read as policy advocacy rather than analysis. The word "dangerous" is a value judgment. Consider: "a trajectory that increases conflict risk near strategic locations, according to the model."
- **Missing: acknowledgment of model limitations in the 2026 context.** The paper covers 1989-2018. The post-2018 world includes new variables not in the original model: autonomous drone warfare (the Houthi attacks use drones and missiles, not traditional naval forces), US-China technological decoupling (which affects trade composition, not just volume), and Russia's invasion of Ukraine (which fundamentally restructured European energy trade routes). A brief disclaimer -- "The model does not account for..." -- would strengthen rather than weaken the analysis.

### Overall Verdict on This Section

It works. The section is closer to rigorous application of a framework than to editorializing, which is the right side of the line. The sourcing is solid, the predictions are attributed to the model, and the Red Sea callout explicitly engages with limitations. The main risk is that a reader might perceive the tariff-conflict link as a partisan political argument (tariffs = bad = more war) rather than a model-derived prediction. Adding a sentence about the model's assumptions and limitations would mitigate this.

---

## 7. Missing Elements

### High Priority

1. **No images directory is populated.** `site/images/` is empty. The site has no photographs, paper figures, or author photos. A photo of the Strait of Hormuz from space, or a historical image of Salamis, would strengthen the Home page immensely. Visual storytelling sites like The Pudding and Our World in Data almost always include at least one iconic image on the landing page.

2. **No social sharing metadata.** The `_quarto.yml` does not include Open Graph tags (`og:image`, `og:description`) or Twitter Card metadata. If someone shares the URL on social media, it will render as a plain text link with no preview image or description. This is a significant missed opportunity for discoverability.

3. **No "summary" or "key takeaway" section on the Home page.** The Home page asks the question but does not preview the answer. A reader who only sees the landing page (the most common behavior) leaves without knowing the paper's main finding. Best practice: include a 2-3 sentence "The Finding" summary between the question and the navigation links.

4. **`regional_panels.json` (158 KB) is unused.** This prepared data file exists but no page references it. Regional deep-dives (Africa, Middle East, SE Asia) would be high-value additions, especially since these are the regions where the paper's predictions are most visible in current events.

5. **The About page has no author photos** and the workshop link (`about.qmd`, line 51) is a dead end: "Learn more about the Claude Code for Research workshop" links nowhere. Either add the link target or remove the prompt.

### Medium Priority

6. **No data download option.** Academic readers may want to download the underlying JSON data. A "Download data" link on the About page (or a collapsible section with direct download links to each JSON file) would serve this audience.

7. **No mobile-specific optimizations for the mechanism diagram.** The hardcoded pixel positions will break on screens narrower than ~600px.

8. **No "how to use this site" micro-tutorial.** Interactive sites benefit from a brief "This site is interactive -- drag sliders, toggle views, and hover over charts" onboarding prompt. First-time visitors to data-driven sites often do not realize elements are interactive.

9. **No skip-to-content or ARIA landmarks.** The `_quarto.yml` does not configure `aria-labels`. While Quarto provides some accessibility features by default, the OJS-rendered SVG charts have no `role="img"` or `aria-label` attributes. Screen readers will see these as empty SVG elements.

10. **The footer citation** (`_quarto.yml`, line 27) is minimal: "Gallea & Rohner, PNAS 2021" with links. Adding the full year and a brief one-line description would improve footer value: "Globalization mitigates conflict near strategic waterways | Gallea & Rohner, PNAS 2021."

### Lower Priority

11. **No favicon.** The site uses the default Quarto favicon.
12. **No loading states.** The map loads ~700 KB of data (world-110m.json + conflict_events.json). During this load, the user sees a blank space. A skeleton loader or "Loading map..." message would improve perceived performance.
13. **No print stylesheet.** Academic users may want to print pages. The current layout (full-width maps, interactive elements) will not print well.

---

## 8. Comparison to Best Practices

### Our World in Data

**What they do better:**
- Every chart has a "Download" button (PNG, SVG, data)
- Every chart has an explicit source citation directly below it
- Toggle controls are visually integrated into charts, not separate form elements
- Every article starts with a "key insights" box
- Extensive use of annotations directly on charts (not just legends)

**What this site does comparably:**
- Semantic color coding
- Progressive disclosure (collapsible callouts)
- Clean typography and generous whitespace

### Distill.pub

**What they do better:**
- Hover-to-explore interactions on every diagram
- Margin notes for definitions (avoiding the need for callout boxes)
- Mathematical notation is always accompanied by interactive manipulables
- Articles include a standardized metadata header (authors, affiliations, date, DOI)

**What this site does comparably:**
- The mechanism diagram's reactive arrows are Distill-quality interactive explanation
- The slider page's real-time equation updating is well-executed

### The Pudding

**What they do better:**
- Stronger visual hooks on landing pages (full-bleed images, animations)
- Scrollytelling transitions between sections
- More aggressive use of animation to guide attention
- Social sharing is built into every article

**What this site does comparably:**
- Strong editorial voice
- Clear question-driven narrative structure

### Overall Positioning

This site is closer to Our World in Data in its approach (data-driven, interactive, educational) than to The Pudding (narrative-first, visual-essay). For an academic paper communication tool, this is the right model. The site's main deficit relative to these benchmarks is in **polish details**: tooltips, download buttons, loading states, social metadata, and accessibility annotations.

---

## 9. Overall Assessment

### Strengths

1. **The core interactive experience is excellent.** The slider page alone justifies the site's existence. The ability to drag a slider and watch a coefficient flip sign -- while seeing the background color shift from red to green and the interpretation text update in real time -- is a more effective way to understand an interaction term than any static table or paragraph.

2. **The narrative arc is sound.** Question -> Evidence -> Exploration -> Implications is the right structure. The Lenin/Montesquieu framing on the Home page is genuinely creative and memorable.

3. **The color semantics are consistently applied.** Red = conflict, green = peace, purple = tipping point across all seven pages. This is not a trivial achievement -- many academic sites use inconsistent color coding.

4. **The "Through the Lens of 2026" section is well-sourced and balanced**, avoiding the trap of editorializing while still making the research feel urgent and relevant.

5. **The technical execution is clean.** Observable JS cells are properly structured, D3 code is idiomatic, SCSS is well-organized, and the Quarto configuration is minimal and correct.

### Weaknesses

1. **Accessibility gaps.** No alt text on SVG charts, no ARIA labels, regression tables will overflow on mobile, mechanism diagram breaks on narrow screens.

2. **The Home page undersells the findings.** It asks the question but does not preview the answer. A first-time visitor may leave without understanding what the paper found.

3. **No tooltips or hover interactions.** The map, tables, and mechanism diagram are all hover-free. This is below the standard set by comparable sites.

4. **Missing social and sharing infrastructure.** No Open Graph tags, no author photos, no favicon, no social sharing buttons. For a site intended as a workshop showcase, discoverability matters.

5. **The Evidence page regression tables are static HTML.** They work, but they miss the opportunity for interactive exploration (highlight a row, see the real-world interpretation).

---

## Top 5 Prioritized Improvements

Ranked by impact on user experience and comprehension:

### 1. Add a "Key Finding" summary to the Home page
**Impact: Very High | Effort: Low**
Add 3-4 sentences between the question section and the navigation links that preview the answer: "We find that proximity to maritime choke points increases conflict risk when global trade is low, but this effect reverses when trade openness exceeds a tipping point of 0.534. Globalization, at sufficient levels, protects strategic locations rather than endangering them." This ensures the most common visitor behavior (landing page only) still conveys the paper's message.

### 2. Add tooltips to the map and mechanism diagram
**Impact: High | Effort: Medium**
Map choke points should show name + context on hover. Conflict dots should show event count and approximate location. Mechanism diagram arrows should show brief labels. These interactions transform passive viewing into active exploration.

### 3. Fix mobile responsiveness for the mechanism diagram and regression tables
**Impact: High | Effort: Medium**
The mechanism diagram needs responsive coordinate scaling (calculate positions as percentages of viewBox dimensions rather than hardcoded pixels). The regression tables need horizontal scroll wrappers for mobile viewports.

### 4. Add narrative transitions between pages
**Impact: Medium-High | Effort: Low**
End each page with a 1-2 sentence forward-looking transition that connects to the next page's content. This converts a collection of pages into a story.

### 5. Add Open Graph metadata and a summary image
**Impact: Medium | Effort: Low**
Add `og:title`, `og:description`, `og:image`, and `twitter:card` tags in `_quarto.yml`. Create or designate a 1200x630px summary image (the slider chart at the tipping point would work well). This dramatically improves how the site appears when shared on social media, Slack, or email.

---

## Overall Grade: **B+**

The site achieves its primary goal: it transforms a static PNAS paper into an interactive, explorable experience that is substantially more engaging and comprehensible than reading the original PDF. The slider page is a standout, the narrative structure is sound, and the visual design is professional. The "Through the Lens of 2026" section adds genuine contemporary value.

The grade is held back from an A by the absence of hover interactions, mobile responsiveness issues, the thin Home page, and missing accessibility infrastructure. These are all addressable with moderate effort. The foundations are strong -- the data pipeline is clean, the OJS code is well-structured, and the SCSS theme is coherent. What remains is the polish pass that separates a good demo from a publication-quality interactive article.

For a site built in ~20 minutes as a workshop demonstration, this is impressive work. For a site intended to be the definitive interactive companion to a PNAS paper, the top 5 improvements above would meaningfully close the gap.

---

*Review conducted 2026-02-28. All file references use absolute paths from the project root at `c:\Users\qgallea\Dropbox\PhD\gallea-rohner-interactive\site\`.*
