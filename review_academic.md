# Academic Review Report

## Interactive Quarto Website: "Globalization Mitigates the Risk of Conflict Caused by Strategic Territory" (Gallea & Rohner, PNAS 2021)

**Reviewer**: Independent academic review (political economy, empirical conflict studies, econometrics, interactive data visualization)
**Date**: 2026-02-28
**Site reviewed**: `c:\Users\qgallea\Dropbox\PhD\gallea-rohner-interactive\site\`
**Live URL**: https://qgallea.github.io/gallea-rohner-interactive/

---

## 1. Accuracy of Statistical Claims

### 1.1 Core Coefficients (Table 2, Column 1)

The site reports the following values in `slider.qmd` (lines 35-38) and `evidence.qmd` (lines 83-98):

| Parameter | Site Value | CLAUDE.md Reference | Status |
|-----------|-----------|-------------------|--------|
| beta_proximity | 0.0148 | 0.0148 | CORRECT |
| SE(beta_proximity) | 0.0010 | 0.0010 | CORRECT |
| beta_proximity x trade | -0.0277 | -0.0277 | CORRECT |
| SE(beta_proximity x trade) | 0.008 | 0.008 | CORRECT |
| Baseline conflict rate | 0.015 | 0.015 | CORRECT |
| Observations | 1,944,540 | 1,944,540 | CORRECT |
| 1 SD proximity | 1,100 km | 1,100 km | CORRECT |

The `marginal_effects.json` data file stores `beta1 = 0.0148`, `se_beta1 = 0.001`, `beta2 = -0.0277`, `se_beta2 = 0.008`, `baseline = 0.015`, and `crossover = 0.5343`. All match the paper values.

### 1.2 Marginal Effect Formula

The site correctly specifies: `ME(trade) = 0.0148 + (-0.0277) x trade` (slider.qmd, line 43).

**Verification at key points**:

- At trade = 0.40: ME = 0.0148 - 0.0277 x 0.40 = 0.0148 - 0.01108 = 0.00372. The `marginal_effects.json` file shows `me = 0.00372` at `trade = 0.4`. **CORRECT.**
- At trade = 0.60: ME = 0.0148 - 0.0277 x 0.60 = 0.0148 - 0.01662 = -0.00182. The JSON shows `me = -0.00182` at `trade = 0.6`. **CORRECT.**
- Crossover: ME = 0 when trade = 0.0148 / 0.0277 = 0.53430... The JSON stores `crossover = 0.5343`, and the OJS code computes `crossover = -beta1 / beta2` (slider.qmd, line 40). **CORRECT.**

### 1.3 Percentage of Baseline Calculations

The "Two Worlds" comparison in `evidence.qmd` (lines 126-171) computes:

- Low trade (0.40): ME = 0.00372, pct = 0.00372 / 0.015 x 100 = 24.8%. The text says "+24.8%". **MATCHES CLAUDE.md reference exactly.**
- High trade (0.60): ME = -0.00182, pct = -0.00182 / 0.015 x 100 = -12.1%. The text says "-12.1%". **MATCHES CLAUDE.md reference exactly.**

### 1.4 Confidence Interval Formula

The slider chart in `slider.qmd` (lines 72-73) computes the standard error of the marginal effect as:

```javascript
const seVal = Math.sqrt(se_beta1**2 + t**2 * se_beta2**2);
```

This is the delta method formula: `SE(ME) = sqrt(Var(beta1) + trade^2 * Var(beta2))`.

**ISSUE (Minor)**: This formula omits the covariance term `2 * trade * Cov(beta1, beta2)`. The full formula should be:

`SE(ME) = sqrt(Var(beta1) + trade^2 * Var(beta2) + 2 * trade * Cov(beta1, beta2))`

Without the covariance term, the confidence intervals are approximate. If the covariance is negative (as is typical for an interaction term and its constituent), the reported intervals may be slightly too wide. If positive, they could be too narrow. This is a common simplification in interactive presentations, and the `marginal_effects.json` file appears to use the same formula (verified: at trade = 0.35, `se = 0.002973`, and `sqrt(0.001^2 + 0.35^2 * 0.008^2) = sqrt(0.000001 + 0.1225 * 0.000064) = sqrt(0.000001 + 0.00000784) = sqrt(0.00000884) = 0.002973`). **CONFIRMED: the JSON data is consistent with the simplified (no-covariance) formula.**

**Recommendation**: Add a footnote in `slider.qmd` or the callout box stating that confidence intervals are computed without the covariance term and are therefore approximate. Alternatively, if the covariance is available from the replication data, incorporate it for precision.

### 1.5 Index Page Numbers

`index.qmd` (lines 19-31) displays:
- "1.9M" observations (paper reports 1,944,540 -- correctly rounded)
- "30 Years (1989-2018)" -- this is 30 years inclusive. **CORRECT.**
- "64,818 Grid Cells (55 x 55 km each)" -- consistent with the paper and `evidence.qmd`. **CORRECT.**

### 1.6 Crossover Value Precision

Throughout the site, the crossover is reported in two ways:
- `slider.qmd` computes it dynamically as `-beta1 / beta2 = -0.0148 / -0.0277 = 0.53429...` and displays it via `crossover.toFixed(3)` = "0.534". **CORRECT.**
- `policy.qmd` (line 35) references "the 0.534 tipping point". **CONSISTENT.**
- CLAUDE.md says "trade ~ 0.534". **CONSISTENT.**
- The `marginal_effects.json` stores `crossover = 0.5343` (4 decimal places). **CONSISTENT** with the exact value 0.534296...

Note: CLAUDE.md separately says "TradeOpenness ~ 0.53" in the one-paragraph summary, which is a less precise rounding. The site uses the more precise 0.534 throughout, which is appropriate.

### 1.7 Standard Error Notation (Table 2)

In `evidence.qmd` line 93, the SE for the interaction term is reported as `(0.008)`. This is a three-digit representation. The paper's Table 2 Column 1 shows the SE of the interaction term. The CLAUDE.md reference value is `0.008`. **CONSISTENT**, though a reader might wonder whether this should be `0.0080` for consistency with the four-decimal coefficient reporting (0.0277). This is a cosmetic point.

### 1.8 Table 1 Values

Table 1 in `evidence.qmd` (lines 23-60) reports baseline proximity coefficients. These values (0.0031, 0.0022, 0.0002, 0.0007, 0.0013) with their standard errors are presented. **These should be verified against the original paper's Table 1.** The CLAUDE.md file does not include Table 1 values, so I cannot independently cross-check them from the materials provided. The reviewer flags this for author verification.

**POTENTIAL ISSUE**: In Table 1, the `ln(deaths+1)` coefficient is 0.0013 with SE (0.0012), which would not carry significance stars. The table shows no stars for this entry. **This is correctly handled** -- the coefficient is not statistically significant at conventional levels (t = 0.0013/0.0012 = 1.08), and the site correctly omits the stars.

---

## 2. Methodological Presentation

### 2.1 Fixed Effects Description

`evidence.qmd` explains fixed effects appropriately for a general audience (line 64): "FE stands for fixed effects -- statistical controls that account for differences across latitudes, countries, or years." This is a reasonable simplification.

**Issue**: Table 1 reports "Latitude FE" and "Year FE", while Table 2 adds "Country FE". This difference is correctly represented but not explicitly discussed. The shift from latitude-only to latitude+country FEs between tables could be highlighted, as it is methodologically significant (country FEs absorb time-invariant country-level confounders that may correlate with both proximity and conflict).

### 2.2 Interaction Term Explanation

The slider page (`slider.qmd`, lines 8-16) provides a clear, correct explanation of the interaction:

> "being near a choke point pushes conflict risk *up* (the positive term), but higher trade openness pushes it back *down* (the negative term)"

This accurately conveys the marginal effect logic.

### 2.3 Clustering

**Missing**: Neither the regression tables nor the explanatory text mention how standard errors are clustered. In conflict panel data, clustering choices (by grid cell, by country, by year) materially affect inference. The paper likely clusters at the grid-cell level or uses Conley standard errors for spatial correlation. This should be disclosed, at minimum in a footnote or the "Robustness" section.

### 2.4 Endogeneity and Identification

The site does not discuss the identification strategy in detail. The paper's use of proximity to choke points as a geographic variable is quasi-exogenous (geography is pre-determined), but the interaction with trade openness raises questions about potential confounders (countries near choke points may differ systematically from those far away). The "Robustness" paragraph in `evidence.qmd` (line 175) mentions cell fixed effects but does not elaborate. For a research showcase, this level of detail is acceptable, though a "Methodology" dropdown could strengthen credibility.

---

## 3. Data Integrity

### 3.1 Chokepoint Coordinates

The `chokepoints.json` file contains 12 choke points. Verification of geographic coordinates:

| Choke Point | Reported (lat, lng) | Expected (approx.) | Assessment |
|-------------|--------------------|--------------------|------------|
| Strait of Hormuz | (26.57, 56.25) | ~(26.6, 56.3) | CORRECT |
| Strait of Malacca | (2.5, 101.5) | ~(2.5, 101.5) | CORRECT |
| Suez Canal | (30.46, 32.35) | ~(30.5, 32.3) | CORRECT |
| Panama Canal | (9.08, -79.68) | ~(9.1, -79.7) | CORRECT |
| Strait of Gibraltar | (35.97, -5.5) | ~(36.0, -5.5) | CORRECT |
| Bab el-Mandeb | (12.58, 43.33) | ~(12.6, 43.3) | CORRECT |
| Strait of Taiwan | (24.0, 119.5) | ~(24.0, 119.5) | CORRECT |
| Cape of Good Hope | (-34.36, 18.47) | ~(-34.4, 18.5) | CORRECT |
| Strait of Dover | (51.05, 1.45) | ~(51.1, 1.4) | CORRECT |
| Turkish Straits | (41.12, 29.05) | ~(41.1, 29.0) | CORRECT |
| Strait of Kerch | (45.3, 36.6) | ~(45.3, 36.6) | CORRECT |
| Lombok Strait | (-8.47, 115.72) | ~(-8.5, 115.7) | CORRECT |

All 12 coordinates are geographically plausible. The selection includes the major maritime choke points discussed in the paper.

### 3.2 Trade Openness Time Series

The `trade_openness.json` file covers 1989-2018 (30 years, matching the paper's sample period). Key validation:

- Range: 0.3855 (1991) to 0.6090 (2008). This is within the CLAUDE.md range of [0.35, 0.60]. The maximum of 0.609 slightly exceeds the stated 0.60 upper bound, which is expected -- the CLAUDE.md range appears to be approximate.
- The 2008 peak followed by 2009 collapse (0.609 -> 0.524) correctly reflects the global financial crisis impact on trade.
- The steady rise from 1989-2008 is consistent with the "hyper-globalization" era documented in the trade literature.
- Post-2009 recovery to ~0.6 by 2011-2013, then slight decline, is consistent with World Bank data on trade-to-GDP ratios.

**Observation**: The data ends at 2018 (trade_openness = 0.5944). The policy page discusses post-2018 trends qualitatively but does not extend the data series. This is appropriate given the paper's sample period.

### 3.3 Marginal Effects JSON

The `marginal_effects.json` contains a precomputed curve with entries at 0.001 trade intervals from 0.35 to 0.60 (251 data points). Spot-checked values:

- trade = 0.35: me = 0.005105. Manual: 0.0148 - 0.0277 * 0.35 = 0.0148 - 0.009695 = 0.005105. **CORRECT.**
- trade = 0.50: me = 0.00095. Manual: 0.0148 - 0.0277 * 0.50 = 0.0148 - 0.01385 = 0.00095. **CORRECT.**
- trade = 0.534: me = 0.000008. Manual: 0.0148 - 0.0277 * 0.534 = 0.0148 - 0.0147918 = 0.0000082. **CORRECT** (matches the crossover point).
- trade = 0.60: me = -0.00182. Manual: 0.0148 - 0.0277 * 0.60 = 0.0148 - 0.01662 = -0.00182. **CORRECT.**

CI calculations (spot-checked at trade = 0.35):
- se = 0.002973 (verified above)
- ci90_lo = 0.005105 - 1.645 * 0.002973 = 0.005105 - 0.004891 = 0.000214. JSON: 0.000214. **CORRECT.**
- ci90_hi = 0.005105 + 1.645 * 0.002973 = 0.005105 + 0.004891 = 0.009996. JSON: 0.009996. **CORRECT.**
- ci99_lo = 0.005105 - 2.576 * 0.002973 = 0.005105 - 0.007658 = -0.002553. JSON: -0.002554. **CORRECT** (rounding).
- ci99_hi = 0.005105 + 2.576 * 0.002973 = 0.005105 + 0.007658 = 0.012763. JSON: 0.012764. **CORRECT** (rounding).

### 3.4 Conflict Events Data

The `conflict_events.json` file is 607 KB and contains grid-cell level conflict data with lat/lng coordinates, event counts, and a `high_trade` boolean flag. Due to the minified format, individual record-level verification was not possible within this review. The `map.qmd` code (line 41) filters on `d.high_trade === isHigh`, which implies a binary split (above/below some threshold). The state file notes "Trade openness median = 0.5177 (computed from data)," suggesting the high/low trade split uses the median of the trade openness distribution in the data.

**Note**: The map page says it toggles between "periods of high and low world trade," using the phrase "above/below median world trade openness" (line 54). This is a reasonable operationalization but differs from the regression framework (which uses the continuous trade variable). This distinction could be made clearer.

### 3.5 Regional Panels Data

The `regional_panels.json` file (158 KB) was too large to read in full. It appears to not be used by any of the seven .qmd files currently in the site. It may be reserved for future regional sub-analyses or was generated during the data pipeline but not yet incorporated. **This is not an error, but it represents unused data.**

---

## 4. Visualization Correctness

### 4.1 Slider Chart (slider.qmd)

The core interactive chart correctly implements:

- **Marginal effect line**: `me = beta1 + beta2 * t` for each trade value (line 71). **CORRECT.**
- **90% CI band**: `me +/- 1.645 * se` (lines 129-135). The z-value 1.645 for 90% CI is **CORRECT.**
- **99% CI band**: `me +/- 2.576 * se` (lines 121-126). The z-value 2.576 for 99% CI is **CORRECT.**
- **Background zones**: Red below crossover, green above (lines 94-104). **CORRECT.**
- **Zero line**: Dashed horizontal at ME = 0 (lines 144-147). **CORRECT.**
- **Crossover vertical line**: At `x(crossover)` (lines 150-158). **CORRECT.**
- **Dynamic dot**: Positioned at `(tradeOpenness, me)` with color switching at ME = 0 (lines 161-165). **CORRECT.**
- **Tipping point detection**: `Math.abs(tradeOpenness - crossover) < 0.005` triggers the discovery message (line 57). This is a UX choice (tolerance window), not an error.

### 4.2 Mechanism Diagram (mechanism.qmd)

The interactive causal diagram (lines 23-136) adjusts visual emphasis based on the trade slider:

- Arrow thickness scales with `t = (tradeLevel - 0.35) / (0.60 - 0.35)`, normalized to [0,1]. **CORRECT.**
- "Incentive to Fight" arrows thicken when trade is low (stroke-width = `2 + (1-t)*3`). **CORRECT** -- higher stroke at low t.
- "Major Power Intervention" arrows thicken when trade is high (stroke-width = `1 + t*4`). **CORRECT** -- higher stroke at high t.
- The threshold for "low" vs "high" regime is set at 0.534 (the exact crossover value). **CORRECT.**

**Minor cosmetic issue**: The mechanism diagram uses a fixed layout with hardcoded pixel coordinates. On narrow screens, the labels may overlap. The `viewBox` approach with responsive width helps, but the text is small (8-12px) for mobile viewing.

### 4.3 World Map (map.qmd)

The D3 map correctly:
- Uses Natural Earth projection (`d3.geoNaturalEarth1()`). **Appropriate choice.**
- Renders TopoJSON countries correctly via `topojson.feature()` and `topojson.mesh()`.
- Scales conflict dot size with `Math.sqrt(d.events) * 1.2`. Square-root scaling for proportional symbols is the **correct cartographic convention**.
- Sorts conflicts from largest to smallest (`sort((a, b) => b.events - a.events)`) to avoid large dots occluding small ones. **CORRECT** -- larger dots render first (behind).

**Wait -- this is actually reversed.** The sort places the *largest* events first in the selection, which means they are rendered *first* in SVG order and will appear *behind* smaller dots. This is actually the **correct** behavior for proportional symbol maps -- small dots should be on top so they remain visible. **CORRECT.**

### 4.4 Trade Openness Timeline (policy.qmd)

The time series chart (lines 67-196):
- Correctly colors dots green when above 0.534 and red when below (line 149).
- Marks the tipping point with a purple dashed line. **CORRECT.**
- Annotates the 1991 "End of Cold War," 2001 "China joins WTO," and 2008 "Financial crisis." These are historically accurate milestones.
- Uses `curveMonotoneX` for smooth interpolation. This is appropriate for time series data.

### 4.5 "Two Worlds" Comparison (evidence.qmd)

The OJS block (lines 126-171) correctly computes:
- `meLow = 0.0148 + (-0.0277) * 0.40 = 0.00372` **CORRECT.**
- `meHigh = 0.0148 + (-0.0277) * 0.60 = -0.00182` **CORRECT.**
- `pctLow = (0.00372 / 0.015 * 100) = 24.8` **CORRECT.**
- `pctHigh = (-0.00182 / 0.015 * 100) = -12.1333...` displayed as `Math.abs(pctHigh)` = "12.1". **CORRECT.**

---

## 5. Causal Language

### 5.1 Overall Assessment

The site generally handles causal language well, but there are notable exceptions.

**Appropriate hedging found**:
- `mechanism.qmd` line 8: "The paper uses game theory to formalize why trade changes conflict incentives." -- Describes the model, not causal claims about data. **Good.**
- `evidence.qmd` line 12: "Areas closer to maritime choke points face significantly higher conflict risk." -- Descriptive, not causal. **Good.**
- `policy.qmd` line 43: "The Houthi crisis both confirms and challenges the model... the model predicts *incentives* to intervene when trade stakes are high, not guaranteed success." **Excellent hedging.**

**Areas requiring more caution**:

1. **`index.qmd`, line 57**: "This research puts both views to the test. The answer? **It depends on how much trade is flowing.**" -- This implies a definitive causal answer. The research *documents a robust empirical pattern* consistent with the Montesquieu mechanism, but the phrase "puts both views to the test" and "the answer" implies a definitive verdict. **Recommendation**: Soften to "The evidence strongly suggests..." or "The data reveals a pattern consistent with..."

2. **`slider.qmd`, title "Explore the Effect"**: The word "effect" implies causation. The slider page consistently uses "marginal effect" language, which is standard econometric terminology for the partial derivative of E[Y|X], but a general audience may interpret "effect" as causal. **Recommendation**: Add a brief note that "effect" here refers to the estimated statistical association from the regression model.

3. **`policy.qmd`, line 24**: "The data shows that trade openness itself reduces conflict in strategic locations." The word "reduces" is causal. **Recommendation**: Change to "is associated with lower conflict" or "predicts lower conflict."

4. **`policy.qmd`, lines 31-35** ("Through the Lens of 2026"): "The paper's framework makes a clear prediction here: falling trade openness pushes the world back below the 0.534 tipping point, into the 'conflict zone' where proximity to choke points *increases* violence." The verb "increases" is causal and the prediction framework is applied out-of-sample. This is a reasonable extrapolation of the model's logic, but should be flagged as a *model prediction*, not an established fact. The language "where proximity to choke points increases violence" should read "where the estimated association between proximity and conflict turns positive."

### 5.2 The Tipping Point Framing

The "conflict zone" and "peace zone" labels on the slider chart (slider.qmd, lines 111, 117) are evocative but somewhat misleading. They suggest a binary regime, when in reality the marginal effect changes continuously. At trade = 0.53 vs. 0.54, the marginal effect is nearly zero in both cases -- the practical difference is trivial. **Recommendation**: Retain the labels for pedagogical impact but add a note that the transition is gradual, not a sharp threshold.

---

## 6. The "Through the Lens of 2026" Section

This section in `policy.qmd` (lines 27-54) is one of the most distinctive and ambitious parts of the site. It applies the paper's framework to current events.

### 6.1 Tariffs and Deglobalization (lines 31-35)

**Claims made**:
- "In 2025, the United States imposed sweeping tariffs -- a 145% tariff on Chinese goods, a 25% tariff on imports from Canada and Mexico, and a baseline 10% tariff on most other countries."
- WTO's Global Trade Outlook (April 2025) projects global merchandise trade volumes will decline by 0.2% in 2025.
- North American trade growth dropping by 1.7 percentage points.

**Assessment**: The 145% tariff on Chinese goods is consistent with publicly reported tariff escalation under the second Trump administration. The WTO April 2025 projection is cited with a specific URL. The specific numbers (145%, 25%, 10%) should be verified against the exact tariff schedule, as tariff rates fluctuated and had various exemptions. The broad claim of deglobalization is directionally sound.

**POTENTIAL ISSUE**: The 145% figure on Chinese goods may combine base tariffs with additional duties. The exact number has been reported variably across sources. A note acknowledging the complexity of the tariff regime (exemptions, categories, retaliatory adjustments) would strengthen this section.

**Link between tariffs and the framework**: The logic is sound -- if tariffs depress trade openness, and the model predicts that lower trade openness increases the marginal effect of proximity on conflict, then tariffs indirectly increase conflict risk near choke points. However, this is a **chain of predictions** with uncertainty at each link, and the site presents it with considerable confidence.

### 6.2 Red Sea Crisis / Bab el-Mandeb (lines 37-44)

**Claims made**:
- "Since November 2023, Houthi forces in Yemen have launched over 190 attacks on commercial shipping."
- "Traffic through the Suez Canal dropped by roughly 75%."
- Rerouting costs "approximately $1 million in fuel per voyage and 11,000 extra nautical miles."
- UNCTAD Global Trade Update (January 2026) estimates "over $1 trillion in goods were disrupted."
- US-led Operation Prosperity Guardian and EU's EUNAVFOR Aspides are named.

**Assessment**: The number "over 190 attacks" is broadly consistent with widely reported figures, though the exact count varies by source and date. The 75% Suez Canal traffic drop is consistent with reporting from early-mid 2024. The $1 million rerouting cost and 11,000 nm extra distance are widely cited estimates. The UNCTAD reference is cited with a URL. Operation Prosperity Guardian and EUNAVFOR Aspides are correctly named.

**The analytical framing is excellent**: "The Houthi crisis both confirms and challenges the model." This nuanced treatment avoids triumphalism and honestly acknowledges that intervention did not stop attacks. The warning callout box (lines 41-44) is the strongest piece of analytical writing on the site.

### 6.3 Strait of Hormuz (lines 46-50)

**Claims made**:
- "In February 2026, Iran conducted live fire naval drills and briefly closed the Strait of Hormuz on February 17."
- A specific URL to The National News is provided.
- "Joint Iran-Russia naval exercises took place at the port of Bandar Abbas."
- "20-30% of the world's daily oil consumption transits through Hormuz."
- The US responded by boosting naval presence.
- France-Netherlands EMASOH mission has maintained patrols since 2020.

**Assessment**: These claims reference very recent events (February 2026). The 20-30% oil transit figure is consistent with longstanding estimates (EIA cites ~20% of global petroleum liquids). The EMASOH mission is correctly described.

**CAUTION**: The claim that Iran "briefly closed the Strait of Hormuz on February 17" is a very specific factual assertion about a very recent event. If this did not happen exactly as described, or if it was a partial restriction rather than a closure, this could undermine the site's credibility. **Recommendation**: Verify this claim carefully. If it is based on a single news report, note the source more carefully and use softer language ("reportedly restricted passage" rather than "closed").

### 6.4 Model Predictions (lines 52-54)

The claim that "if tariffs and deglobalization continue to depress world trade openness, the framework predicts a dangerous trajectory" is a reasonable conditional statement. The qualification "if" is important and appropriate.

**ISSUE**: The text implies a direct mapping from the model's in-sample predictions to out-of-sample forecasting. The model was estimated on 1989-2018 data. Structural changes in global governance, military technology, and the geopolitical landscape since 2018 could alter the relationship. The site should note this caveat explicitly.

---

## 7. Missing Caveats and Limitations

The following important limitations are not mentioned (or insufficiently discussed) on the site:

### 7.1 Omitted from the Site

1. **Clustering of standard errors**: No mention of how standard errors are clustered. This is a critical methodological detail for panel data with spatial structure.

2. **Endogeneity of trade openness**: While proximity to choke points is plausibly exogenous, world trade openness is an aggregate variable that may correlate with many unobserved factors (global GDP growth, technological change, political institutions). The interaction could capture the effect of economic development broadly, not just trade per se.

3. **Out-of-sample validity**: The model is estimated on 1989-2018 data. The "Through the Lens of 2026" section applies the framework to the post-sample period without discussing structural break risk.

4. **Ecological fallacy risk**: The model uses grid-cell data aggregated at the 55x55 km level. Conflict dynamics at the micro level may differ from the grid-level associations.

5. **Alternative explanations for the interaction**: The negative interaction could reflect that during periods of high global trade, global governance institutions are stronger and economic conditions are better generally (not just through the trade-protection mechanism).

6. **The conflict measure**: The binary conflict indicator treats all conflict events equally. A single skirmish and a major battle both count as "1." The logged deaths measure partially addresses this, but the headline results (Table 2, Column 1) use the binary indicator.

7. **Spatial autocorrelation**: Adjacent grid cells are likely correlated. If Conley standard errors or spatial HAC are not used, the reported significance levels may be inflated.

8. **Missing covariance term in SE calculation** (noted in Section 1.4 above).

### 7.2 Partially Addressed

1. **Robustness checks**: Mentioned in one paragraph (`evidence.qmd`, line 175) but not shown interactively. Given the site's emphasis on exploration, a dropdown showing alternative specifications would strengthen the evidence section considerably.

2. **Data sources and processing**: The about page mentions UCDP and World Bank, but the specific processing steps (aggregation method for conflict events to grid cells, how proximity is measured) are not described.

---

## 8. Additional Observations

### 8.1 Accessibility

- **Alt text**: No alt text is provided for any of the SVG visualizations generated by OJS/D3. Screen readers will not be able to convey the content of the map, slider chart, mechanism diagram, or trade timeline. This is a significant accessibility gap. **The CLAUDE.md explicitly lists accessibility as a non-negotiable rule (Rule 9).**
- **Keyboard navigation**: The OJS `Inputs.range()` and `Inputs.radio()` controls should be keyboard-accessible by default, which is good. However, the D3 map has no keyboard interaction.
- **Color contrast**: The map uses red dots on light blue ocean, which should pass WCAG contrast requirements. The regression table highlighting (orange background with dark text) appears adequate.

### 8.2 Citation Footer

The `_quarto.yml` footer correctly includes "Gallea & Rohner, *PNAS* 2021" with links to the paper and replication data on every page. This satisfies CLAUDE.md Rule 6.

### 8.3 Performance Considerations

The `conflict_events.json` (607 KB) is the largest data file. On slow connections, the map page may load slowly. The `world-110m.json` (105 KB) is a lightweight TopoJSON, which is a good choice. The use of Natural Earth 110m (low resolution) is appropriate for a world overview.

### 8.4 Unused Data Files

`regional_panels.json` (158 KB) is generated but not used by any page. It should either be removed to reduce repository size or incorporated into a future regional analysis page.

### 8.5 Code Quality

The OJS code is clean, well-structured, and follows good practices:
- All code chunks use `//| echo: false` to hide code from end users.
- D3 visualizations use the `create()` -> `return .node()` pattern correctly.
- Color coding is consistent throughout (red = conflict, green = peace, orange = choke points, purple = crossover).

---

## 9. Summary and Recommendations

### Strengths

1. **Statistical accuracy**: All core coefficients, marginal effects, and computed values are correct. The slider math faithfully implements the paper's interaction model.
2. **Pedagogical clarity**: The progression from map (where) to mechanism (why) to slider (how much) to evidence (proof) to policy (so what) is logically compelling and well-structured.
3. **The "Through the Lens of 2026" section**: The application to current events (Houthi crisis, Hormuz tensions, tariffs) transforms a static paper into a living analytical framework. The nuanced treatment of the Red Sea crisis is particularly strong.
4. **Visual design**: The SCSS theme is professional, the color palette is consistent and meaningful, and the typography (Playfair Display for headings, Source Sans for body) gives it an editorial quality.
5. **Interactivity**: The trade openness slider is the centerpiece and works as intended -- it makes the abstract concept of an interaction effect tangible.
6. **Data integrity**: All JSON data files that could be verified are internally consistent and match the reported formulas.

### Weaknesses

1. **Missing confidence interval covariance term**: The SE formula omits `Cov(beta1, beta2)`, making CIs approximate.
2. **No accessibility for visualizations**: All SVG charts lack alt text, violating the project's own stated rules.
3. **Clustering not disclosed**: The standard error clustering method is never mentioned.
4. **Causal language slips**: Several instances of causal language ("reduces," "increases," "the answer") that should be hedged.
5. **Out-of-sample prediction caveat missing**: The 2026 analysis applies in-sample estimates to post-sample conditions without discussing this limitation.
6. **February 2026 Hormuz claim**: The very specific claim about Iran closing the Strait on February 17 needs careful source verification.

### Specific Recommendations

| Priority | File | Recommendation |
|----------|------|---------------|
| HIGH | `slider.qmd` | Add footnote about approximate CIs (missing covariance term) |
| HIGH | All chart pages | Add meaningful alt text for SVG visualizations |
| HIGH | `policy.qmd` | Add caveat about out-of-sample prediction validity |
| HIGH | `policy.qmd` | Verify the February 17 Hormuz closure claim; soften language if needed |
| MEDIUM | `evidence.qmd` | Disclose SE clustering method |
| MEDIUM | `policy.qmd`, line 24 | Change "reduces" to "is associated with lower" |
| MEDIUM | `slider.qmd` | Note that "CONFLICT ZONE"/"PEACE ZONE" labels represent a continuous transition |
| LOW | `evidence.qmd` | Discuss the shift from latitude FE (Table 1) to latitude+country FE (Table 2) |
| LOW | site/data/ | Remove `regional_panels.json` if not used, or build a page for it |
| LOW | `index.qmd` | Soften "puts both views to the test" language |

---

## 10. Overall Grade

### Grade: A-

This is an impressive, well-executed interactive research showcase. The statistical content is accurate down to the fourth decimal place. The visualizations faithfully implement the paper's core model. The pedagogical structure is thoughtful, and the "Through the Lens of 2026" section elevates the site from a static reproduction to a living analytical tool.

The grade reflects the following deductions from a potential A+:
- The missing covariance term in confidence intervals, while a common simplification, should be disclosed for a research-quality presentation.
- The absence of alt text for all visualizations is a notable gap for a project that lists accessibility as a core requirement.
- Several instances of unhedged causal language need correction, particularly in the policy section.
- The specific factual claims about February 2026 events need verification.

None of these are fatal flaws. With the recommended corrections, this site would merit an A or A+. In its current state, it is a strong, credible, and engaging presentation of an important research finding.

---

*Review conducted 2026-02-28. All file references use absolute paths from the project root at `c:\Users\qgallea\Dropbox\PhD\gallea-rohner-interactive\site\`.*
