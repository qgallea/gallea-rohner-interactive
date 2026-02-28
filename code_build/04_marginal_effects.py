"""
04_marginal_effects.py
Pre-computes the marginal effects curve.
Source: Gallea & Rohner (2021), Figure 3 regression VCV (delta-method SEs from Stata margins).
"""
import json
import math
import os

beta1 = 0.0148
se_beta1 = 0.001040
beta2 = -0.0277
se_beta2 = 0.001751
cov_beta12 = -0.000001507
baseline = 0.015
crossover = -beta1 / beta2

curve = []
for i in range(251):
    trade = 0.35 + i * 0.001
    me = beta1 + beta2 * trade
    se = math.sqrt(se_beta1**2 + trade**2 * se_beta2**2 + 2 * trade * cov_beta12)
    curve.append({
        "trade": round(trade, 3),
        "me": round(me, 6),
        "se": round(se, 6),
        "ci90_lo": round(me - 1.645 * se, 6),
        "ci90_hi": round(me + 1.645 * se, 6),
        "ci99_lo": round(me - 2.576 * se, 6),
        "ci99_hi": round(me + 2.576 * se, 6),
    })

result = {
    "beta1": beta1, "se_beta1": se_beta1,
    "beta2": beta2, "se_beta2": se_beta2,
    "baseline": baseline,
    "crossover": round(crossover, 4),
    "curve": curve
}

out_path = os.path.join(os.path.dirname(__file__), '..', 'site', 'data', 'marginal_effects.json')
with open(out_path, 'w') as f:
    json.dump(result, f, indent=2)

print(f"Wrote marginal effects curve ({len(curve)} points) to {out_path}")
