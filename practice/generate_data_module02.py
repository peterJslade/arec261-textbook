#!/usr/bin/env python3
"""Generate the synthetic dataset for Module 2 (Introduction to R) practice.

Module 2 teaches R/Positron: reading CSVs, vectors/data frames/functions,
summary statistics in R, and na.rm. The dataset therefore deliberately
includes a handful of missing (NA / blank) values so that questions can
exercise na.rm = TRUE.

Deterministic (fixed seed) so the same data is produced every time.
Prints the exact answer key for each practice question, computed the way
R computes them (sample sd/var; type-7 quantiles, which is R's default and
matches Excel's PERCENTILE.INC / QUARTILE.INC).
"""

import csv
import os
import random
import statistics
from collections import Counter, defaultdict
from datetime import date, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(262)  # different seed from Module 1 so the data is distinct

# =============================================================================
# DATASET: sask_wheat_2025.csv
# 150 spring-wheat fields across 3 soil zones and 3 varieties.
# Columns: field_id, soil_zone, variety, acres, yield_bu_ac,
#          protein_pct, seeded_rate_lb_ac
# A small number of yield_bu_ac and protein_pct values are left BLANK
# (missing) on purpose, to exercise na.rm = TRUE in R.
# =============================================================================

SOIL_ZONES = ["Brown", "Dark Brown", "Black"]
VARIETIES = ["AAC Brandon", "CDC Landmark", "AAC Viewfield"]

# Indices (1-based field numbers) that will have a MISSING yield value.
MISSING_YIELD_FIELDS = {17, 58, 96, 133}
# Indices that will have a MISSING protein value.
MISSING_PROTEIN_FIELDS = {23, 71, 110}

rows = []
for i in range(1, 151):
    zone = random.choice(SOIL_ZONES)
    variety = random.choice(VARIETIES)
    acres = int(round(random.uniform(80, 640), 0))
    # Black soil yields more than Dark Brown, which yields more than Brown.
    base = {"Brown": 38, "Dark Brown": 44, "Black": 50}[zone]
    var_adj = {"AAC Brandon": 2, "CDC Landmark": 3, "AAC Viewfield": 0}[variety]
    seed_rate = int(round(random.uniform(90, 140), 0))
    rate_adj = (seed_rate - 115) * 0.04
    noise = random.gauss(0, 5)
    yield_bu = round(max(12, base + var_adj + rate_adj + noise), 1)
    # Protein is loosely (negatively) related to yield, plus noise.
    protein = round(max(9.0, 15.5 - (yield_bu - 45) * 0.06 + random.gauss(0, 0.8)), 1)

    rows.append({
        "field_id": f"W{i:03d}",
        "soil_zone": zone,
        "variety": variety,
        "acres": acres,
        "yield_bu_ac": "" if i in MISSING_YIELD_FIELDS else yield_bu,
        "protein_pct": "" if i in MISSING_PROTEIN_FIELDS else protein,
        "seeded_rate_lb_ac": seed_rate,
    })

with open(os.path.join(DATA_DIR, "sask_wheat_2025.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    writer.writeheader()
    writer.writerows(rows)


# =============================================================================
# ANSWER KEY
# =============================================================================

def quantile_type7(data, p):
    """R's default quantile (type 7) == Excel PERCENTILE.INC."""
    data = sorted(data)
    n = len(data)
    rank = p * (n - 1)
    lo = int(rank)
    hi = min(lo + 1, n - 1)
    frac = rank - lo
    return data[lo] + frac * (data[hi] - data[lo])


# Non-missing numeric vectors (this is what R computes with na.rm = TRUE).
yields = [r["yield_bu_ac"] for r in rows if r["yield_bu_ac"] != ""]
protein = [r["protein_pct"] for r in rows if r["protein_pct"] != ""]
acres = [r["acres"] for r in rows]
seed_rate = [r["seeded_rate_lb_ac"] for r in rows]

n_total = len(rows)
n_yield = len(yields)
n_missing_yield = n_total - n_yield
n_missing_protein = n_total - len(protein)

print("=" * 72)
print(f"DATASET: sask_wheat_2025.csv  ({n_total} rows, {len(rows[0])} columns)")
print("=" * 72)
print(f"  Columns: {', '.join(rows[0].keys())}")
print(f"  Missing yield_bu_ac values:  {n_missing_yield}  "
      f"(fields {sorted('W%03d' % i for i in MISSING_YIELD_FIELDS)})")
print(f"  Missing protein_pct values:  {n_missing_protein}")

# --- TYPE 1: Reading data & exploring ---
print("\n--- TYPE 1: READING DATA & EXPLORING ---")
print(f"  nrow(wheat)          = {n_total}")
print(f"  ncol(wheat)          = {len(rows[0])}")
print(f"  names(wheat)         = {list(rows[0].keys())}")
print(f"  # of NA in yield     = {n_missing_yield}")
print(f"  # distinct soil zones= {len(set(r['soil_zone'] for r in rows))} "
      f"({sorted(set(r['soil_zone'] for r in rows))})")
print(f"  # distinct varieties = {len(set(r['variety'] for r in rows))}")

# --- TYPE 2: Vectors & functions ---
print("\n--- TYPE 2: VECTORS & FUNCTIONS ---")
demo = [48, 52, 47, 55, 50]
print(f"  Demo vector v <- c(48,52,47,55,50)")
print(f"    mean(v)            = {statistics.mean(demo)}")
print(f"    sd(v)              = {statistics.stdev(demo):.4f}")
print(f"    median(v)          = {statistics.median(demo)}")
print(f"    length(v)          = {len(demo)}")
print(f"    v * 2 first elem   = {demo[0]*2}")
a = [10, 20, 30]
b = [1, 2, 3]
print(f"    c(10,20,30)+c(1,2,3) = {[x+y for x, y in zip(a, b)]}  (element-wise)")
print(f"    sum(c(10,20,30))   = {sum(a)}")

# --- TYPE 3: Summary statistics in R (with na.rm) ---
print("\n--- TYPE 3: SUMMARY STATISTICS IN R (na.rm = TRUE) ---")
print(f"  mean(yield, na.rm=T)   = {statistics.mean(yields):.2f}")
print(f"  median(yield, na.rm=T) = {statistics.median(yields):.2f}")
print(f"  sd(yield, na.rm=T)     = {statistics.stdev(yields):.2f}")
print(f"  var(yield, na.rm=T)    = {statistics.variance(yields):.2f}")
print(f"  min / max yield        = {min(yields)} / {max(yields)}")
print(f"  IQR(yield, na.rm=T)    = "
      f"{quantile_type7(yields, 0.75) - quantile_type7(yields, 0.25):.2f}")
print(f"  Q1 / Q3 yield          = "
      f"{quantile_type7(yields, 0.25):.2f} / {quantile_type7(yields, 0.75):.2f}")
print(f"  quantile(yield, 0.90)  = {quantile_type7(yields, 0.90):.2f}")
print(f"  mean(protein, na.rm=T) = {statistics.mean(protein):.2f}")
print(f"  mean(acres)            = {statistics.mean(acres):.2f}")
print(f"  NOTE: mean(yield) WITHOUT na.rm returns NA (because of {n_missing_yield} NAs).")

# Mean yield by soil zone (na.rm), foreshadowing dplyr in Module 3.
print("\n  Mean yield by soil zone (na.rm = TRUE):")
zone_yields = defaultdict(list)
for r in rows:
    if r["yield_bu_ac"] != "":
        zone_yields[r["soil_zone"]].append(r["yield_bu_ac"])
for z in SOIL_ZONES:
    vals = zone_yields[z]
    print(f"    {z:12s}: mean = {statistics.mean(vals):6.2f}  (n = {len(vals)})")

# Mean yield by variety
print("  Mean yield by variety (na.rm = TRUE):")
var_yields = defaultdict(list)
for r in rows:
    if r["yield_bu_ac"] != "":
        var_yields[r["variety"]].append(r["yield_bu_ac"])
for v in VARIETIES:
    vals = var_yields[v]
    print(f"    {v:14s}: mean = {statistics.mean(vals):6.2f}  (n = {len(vals)})")

# --- TYPE 4: scripting / reproducibility / AI is conceptual, no numeric key ---
print("\n--- TYPE 4: SCRIPTING, REPRODUCIBILITY & AI ---")
print("  (Conceptual / short-answer — see qmd for model answers.)")

print("\n" + "=" * 72)
print("Done.")
