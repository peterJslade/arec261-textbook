#!/usr/bin/env python3
"""Generate the synthetic canola fertilizer trial for Module 5.

Module 5 (Relationships Between Variables) teaches correlation, simple
linear regression, and multiple regression. The dataset is built with a
KNOWN structure so the module can show students what the right answer is:

    yield = 22 + 0.14*fertilizer + 0.055*rainfall + variety effect + noise

The important teaching feature is a deliberate CONFOUND. Fertilizer is not
assigned at random: farmers on better-watered land also fertilize more
heavily (a real behaviour -- you invest inputs where you expect a return).
So fertilizer and rainfall are positively correlated, which means:

  * a SIMPLE regression of yield on fertilizer overstates the fertilizer
    effect, because fertilizer is partly standing in for rainfall;
  * adding rainfall to the model pulls the fertilizer coefficient back
    toward its true value of 0.14.

That contrast is the point of the multiple-regression section, and it gives
the "correlation is not causation" discussion something concrete to bite on.

(An earlier version added diminishing returns to the fertilizer response, but
the curvature pulled the fitted slope below the true value and obscured the
confound, which is the actual lesson. The response is kept linear.)

Deterministic (fixed seed) so the same data is produced every time.
"""

import csv
import os
import random
import statistics

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(20260818)

N = 120

# True coefficients used to build the data.
B0 = 22.0            # intercept (bu/ac)
B_FERT = 0.14        # bu/ac per kg/ha of N
B_RAIN = 0.055       # bu/ac per mm of growing-season rain
VARIETY_EFFECT = {"InVigor": 2.5, "DEKALB": 1.2, "Clearfield": 0.0}
DIMINISHING = 0.0        # keep the response linear; curvature masked the confound

rows = []
for i in range(1, N + 1):
    # Growing-season rainfall, mm. Roughly the Saskatchewan range.
    rainfall = random.gauss(230, 45)
    rainfall = max(120, min(340, rainfall))

    # THE CONFOUND: fertilizer rate rises with rainfall. Farmers on better
    # land apply more N. Correlation between the two ends up near 0.5.
    fert_mean = 40 + 0.32 * (rainfall - 230)
    fertilizer = random.gauss(fert_mean + 90, 22)
    fertilizer = max(0, min(190, fertilizer))

    variety = random.choice(list(VARIETY_EFFECT))

    yield_bu = (
        B0
        + B_FERT * fertilizer
        + DIMINISHING * fertilizer ** 2
        + B_RAIN * rainfall
        + VARIETY_EFFECT[variety]
        + random.gauss(0, 3.2)
    )

    rows.append({
        "field_id": f"C{i:03d}",
        "fertilizer_kg_ha": round(fertilizer, 1),
        "rainfall_mm": round(rainfall, 1),
        "variety": variety,
        "yield_bu_acre": round(yield_bu, 1),
    })

# Three fields lost their rain-gauge readings (the Module 5 missing-data
# example). Blank them in the file; the report below uses complete cases,
# which is also what cor(use = "complete.obs") and lm() see.
MISSING_RAIN_IDS = {"C012", "C047", "C088"}
for r in rows:
    if r["field_id"] in MISSING_RAIN_IDS:
        r["rainfall_mm"] = ""

out = os.path.join(DATA_DIR, "canola_trial.csv")
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

# ---- Report the structure, so the module's prose can quote real numbers ----

def col(name):
    return [r[name] for r in rows]

def corr(a, b):
    ma, mb = statistics.mean(a), statistics.mean(b)
    num = sum((x - ma) * (y - mb) for x, y in zip(a, b))
    den = (sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b)) ** 0.5
    return num / den

def ols(y, xs):
    """Plain OLS via normal equations; xs is a list of predictor columns."""
    n = len(y)
    X = [[1.0] + [xs[j][i] for j in range(len(xs))] for i in range(n)]
    k = len(X[0])
    XtX = [[sum(X[i][a] * X[i][b] for i in range(n)) for b in range(k)] for a in range(k)]
    Xty = [sum(X[i][a] * y[i] for i in range(n)) for a in range(k)]
    # Gaussian elimination
    M = [XtX[r][:] + [Xty[r]] for r in range(k)]
    for c in range(k):
        p = max(range(c, k), key=lambda r: abs(M[r][c]))
        M[c], M[p] = M[p], M[c]
        for r in range(k):
            if r != c:
                f = M[r][c] / M[c][c]
                for cc in range(c, k + 1):
                    M[r][cc] -= f * M[c][cc]
    return [M[r][k] / M[r][r] for r in range(k)]

# Complete cases only: what cor(use = "complete.obs") and lm() operate on.
cc = [r for r in rows if r["rainfall_mm"] != ""]
fert = [r["fertilizer_kg_ha"] for r in cc]
rain = [r["rainfall_mm"] for r in cc]
y = [r["yield_bu_acre"] for r in cc]

print(f"wrote {out}  ({len(rows)} rows)")
print()
print("Structure the module can quote:")
print(f"  cor(fertilizer, rainfall) = {corr(fert, rain):.3f}   <- the confound")
print(f"  cor(fertilizer, yield)    = {corr(fert, y):.3f}")
print(f"  cor(rainfall, yield)      = {corr(rain, y):.3f}")
print()
b = ols(y, [fert])
print(f"  simple   yield ~ fertilizer          slope = {b[1]:.3f}  (overstated)")
b2 = ols(y, [fert, rain])
print(f"  multiple yield ~ fertilizer+rainfall slope = {b2[1]:.3f}  (true value 0.14)")
print(f"                                    rainfall = {b2[2]:.3f}  (true value 0.055)")
