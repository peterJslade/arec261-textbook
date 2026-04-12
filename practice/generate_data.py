#!/usr/bin/env python3
"""Generate synthetic agricultural datasets for Module 1 practice questions.

Deterministic (fixed seed) so the same data is produced every time.
Also prints the exact answers to each practice question.
"""

import csv
import os
import random
import statistics
from collections import defaultdict
from datetime import date, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(261)

# =============================================================================
# DATASET 1: sask_canola_2025.csv
# 120 fields of canola across 3 regions, 4 varieties, some irrigated
# Columns: field_id, region, variety, acres, yield_bu_ac, fertilizer_kg_ha,
#          irrigated, seeding_date
# =============================================================================

REGIONS = ["South", "Central", "North"]
VARIETIES = ["InVigor L345PC", "DKTC 9105", "PV 581 GC", "Liberty 6060"]

yields_rows = []
for i in range(1, 121):
    region = random.choice(REGIONS)
    variety = random.choice(VARIETIES)
    acres = round(random.uniform(60, 500), 0)
    base = {"South": 42, "Central": 46, "North": 44}[region]
    var_adj = {"InVigor L345PC": 3, "DKTC 9105": 1, "PV 581 GC": 0, "Liberty 6060": 2}[variety]
    fert = round(random.uniform(50, 160), 0)
    fert_adj = (fert - 100) * 0.08
    noise = random.gauss(0, 5)
    yield_bu = round(max(15, base + var_adj + fert_adj + noise), 1)
    irrigated = random.random() < 0.2
    # Seeding date: mid-April to late May
    seed_day = date(2025, 4, 15) + timedelta(days=random.randint(0, 40))
    yields_rows.append({
        "field_id": f"F{i:03d}",
        "region": region,
        "variety": variety,
        "acres": int(acres),
        "yield_bu_ac": yield_bu,
        "fertilizer_kg_ha": int(fert),
        "irrigated": "TRUE" if irrigated else "FALSE",
        "seeding_date": seed_day.isoformat(),
    })

with open(os.path.join(DATA_DIR, "sask_canola_2025.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(yields_rows[0].keys()))
    writer.writeheader()
    writer.writerows(yields_rows)

# =============================================================================
# DATASET 2: farm_costs_2025.csv  (same as before but larger)
# 60 input-cost orders
# =============================================================================

SUPPLIERS = ["Prairie Ag Supply", "NorthField Inputs", "Western Seed Co", "GrainLand Services"]
PRODUCTS = [
    ("Urea", 0.85, "kg"),
    ("Canola Seed", 12.50, "lb"),
    ("Glyphosate", 9.75, "L"),
    ("Diesel", 1.35, "L"),
    ("Phosphate", 0.95, "kg"),
]

start_date = date(2025, 3, 1)
costs_rows = []
for i in range(1, 61):
    product, base_price, unit = random.choice(PRODUCTS)
    supplier = random.choice(SUPPLIERS)
    price = round(base_price * random.uniform(0.9, 1.15), 2)
    quantity = random.choice([50, 100, 200, 500, 1000, 2000])
    offset_days = random.randint(0, 180)
    order_date = start_date + timedelta(days=offset_days)
    costs_rows.append({
        "order_id": f"O{i:04d}",
        "order_date": order_date.isoformat(),
        "supplier": supplier,
        "product": product,
        "price_per_unit": price,
        "quantity": quantity,
        "unit": unit,
    })

with open(os.path.join(DATA_DIR, "farm_costs_2025.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(costs_rows[0].keys()))
    writer.writeheader()
    writer.writerows(costs_rows)


# =============================================================================
# ANSWER KEY
# =============================================================================

def percentile_inc(data, p):
    data = sorted(data)
    n = len(data)
    rank = p * (n - 1)
    lo = int(rank)
    hi = min(lo + 1, n - 1)
    frac = rank - lo
    return data[lo] + frac * (data[hi] - data[lo])


yields_bu = [r["yield_bu_ac"] for r in yields_rows]
acres_list = [r["acres"] for r in yields_rows]

print("=" * 70)
print("DATASET 1: sask_canola_2025.csv  ({} rows)".format(len(yields_rows)))
print("=" * 70)

# --- TYPE 1: Descriptive stats ---
print("\n--- TYPE 1: DESCRIPTIVE STATISTICS ---")
print(f"  mean_yield           = {statistics.mean(yields_bu):.2f}")
print(f"  median_yield         = {statistics.median(yields_bu):.2f}")

# Mode (might not exist for continuous data — check)
from collections import Counter
yield_counts = Counter(yields_bu)
mode_val = yield_counts.most_common(1)[0]
print(f"  mode_yield           = {mode_val[0]} (count: {mode_val[1]})")

print(f"  stdev_yield (sample) = {statistics.stdev(yields_bu):.2f}")
print(f"  variance (sample)    = {statistics.variance(yields_bu):.2f}")
print(f"  range                = {max(yields_bu) - min(yields_bu):.1f}  (min={min(yields_bu)}, max={max(yields_bu)})")
print(f"  Q1                   = {percentile_inc(yields_bu, 0.25):.2f}")
print(f"  Q3                   = {percentile_inc(yields_bu, 0.75):.2f}")
print(f"  IQR                  = {percentile_inc(yields_bu, 0.75) - percentile_inc(yields_bu, 0.25):.2f}")
print(f"  p90                  = {percentile_inc(yields_bu, 0.90):.2f}")
print(f"  mean_acres           = {statistics.mean(acres_list):.2f}")
print(f"  median_acres         = {statistics.median(acres_list):.2f}")

# --- TYPE 2: Conditional functions ---
print("\n--- TYPE 2: CONDITIONAL FUNCTIONS ---")
count_gt50 = sum(1 for y in yields_bu if y > 50)
print(f"  count yield > 50     = {count_gt50}")

south = [r["yield_bu_ac"] for r in yields_rows if r["region"] == "South"]
central = [r["yield_bu_ac"] for r in yields_rows if r["region"] == "Central"]
north = [r["yield_bu_ac"] for r in yields_rows if r["region"] == "North"]
print(f"  avg yield South      = {statistics.mean(south):.2f}  (n={len(south)})")
print(f"  avg yield Central    = {statistics.mean(central):.2f}  (n={len(central)})")
print(f"  avg yield North      = {statistics.mean(north):.2f}  (n={len(north)})")

irrigated = [r["yield_bu_ac"] for r in yields_rows if r["irrigated"] == "TRUE"]
not_irrigated = [r["yield_bu_ac"] for r in yields_rows if r["irrigated"] == "FALSE"]
print(f"  avg yield irrigated  = {statistics.mean(irrigated):.2f}  (n={len(irrigated)})")
print(f"  avg yield non-irrig  = {statistics.mean(not_irrigated):.2f}  (n={len(not_irrigated)})")

total_prod = sum(r["yield_bu_ac"] * r["acres"] for r in yields_rows)
print(f"  total production bu  = {total_prod:.1f}")

south_prod = sum(r["yield_bu_ac"] * r["acres"] for r in yields_rows if r["region"] == "South")
central_prod = sum(r["yield_bu_ac"] * r["acres"] for r in yields_rows if r["region"] == "Central")
north_prod = sum(r["yield_bu_ac"] * r["acres"] for r in yields_rows if r["region"] == "North")
print(f"  total prod South     = {south_prod:.1f}")
print(f"  total prod Central   = {central_prod:.1f}")
print(f"  total prod North     = {north_prod:.1f}")

# Lookup: match field IDs to varieties via the same dataset
# (simulating a two-table lookup)
print(f"  F001 variety         = {yields_rows[0]['variety']}")
print(f"  F050 variety         = {yields_rows[49]['variety']}")
print(f"  F100 variety         = {yields_rows[99]['variety']}")

# --- TYPE 3: PivotTable answers ---
print("\n--- TYPE 3: PIVOTTABLE ---")
# Average yield by region and variety
region_var = defaultdict(list)
for r in yields_rows:
    region_var[(r["region"], r["variety"])].append(r["yield_bu_ac"])

print("  Avg yield by region x variety:")
for (reg, var), vals in sorted(region_var.items()):
    print(f"    {reg:10s} x {var:20s}: {statistics.mean(vals):6.2f}  (n={len(vals)})")

# Total acres by variety
var_acres = defaultdict(int)
for r in yields_rows:
    var_acres[r["variety"]] += r["acres"]
print("  Total acres by variety:")
for v, a in sorted(var_acres.items(), key=lambda x: -x[1]):
    print(f"    {v:20s}: {a}")

# Count by region
reg_count = Counter(r["region"] for r in yields_rows)
print("  Count by region:")
for reg, cnt in sorted(reg_count.items()):
    print(f"    {reg}: {cnt}")

# --- TYPE 4: Chart data ---
print("\n--- TYPE 4: CHART DATA ---")
print("  Histogram: yield_bu_ac column, 120 values")
print(f"  Min={min(yields_bu)}, Max={max(yields_bu)}")
print("  Box plot by region: South/Central/North")
for reg_name, reg_data in [("South", south), ("Central", central), ("North", north)]:
    q1 = percentile_inc(reg_data, 0.25)
    med = statistics.median(reg_data)
    q3 = percentile_inc(reg_data, 0.75)
    print(f"    {reg_name}: Q1={q1:.1f}, Med={med:.1f}, Q3={q3:.1f}, "
          f"Min={min(reg_data)}, Max={max(reg_data)}")

# --- COSTS DATASET ---
print("\n" + "=" * 70)
print("DATASET 2: farm_costs_2025.csv  ({} rows)".format(len(costs_rows)))
print("=" * 70)

prairie_total = sum(r["price_per_unit"] * r["quantity"] for r in costs_rows
                    if r["supplier"] == "Prairie Ag Supply")
print(f"  Prairie Ag total spend = ${prairie_total:.2f}")

urea_prices = [r["price_per_unit"] for r in costs_rows if r["product"] == "Urea"]
print(f"  Max urea price         = ${max(urea_prices):.2f}" if urea_prices else "  No urea orders")
print(f"  Avg urea price         = ${statistics.mean(urea_prices):.2f}" if urea_prices else "")

# Total spend by supplier
sup_spend = defaultdict(float)
for r in costs_rows:
    sup_spend[r["supplier"]] += r["price_per_unit"] * r["quantity"]
print("  Total spend by supplier:")
for s, total in sorted(sup_spend.items(), key=lambda x: -x[1]):
    print(f"    {s:25s}: ${total:,.2f}")

# Total spend by product
prod_spend = defaultdict(float)
for r in costs_rows:
    prod_spend[r["product"]] += r["price_per_unit"] * r["quantity"]
print("  Total spend by product:")
for p, total in sorted(prod_spend.items(), key=lambda x: -x[1]):
    print(f"    {p:15s}: ${total:,.2f}")

print("\n" + "=" * 70)
print("Done.")
