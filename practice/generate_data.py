#!/usr/bin/env python3
"""Generate synthetic agricultural datasets for Module 1 practice questions.

Deterministic (fixed seed) so the same data is produced every time.
Also prints the exact answers to each of the ten practice questions.
"""

import csv
import os
import random
import statistics
from datetime import date, timedelta

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(261)

# =============================================================================
# DATASET 1: canola_yields_2025.csv
# 50 fields of canola grown in Saskatchewan in 2025
# Columns: field_id, region, variety, acres, yield_bu_ac, fertilizer_kg_ha, irrigated
# =============================================================================

REGIONS = ["South", "Central", "North"]
VARIETIES = ["InVigor L345PC", "DKTC 9105", "PV 581 GC", "Liberty 6060"]

yields_rows = []
for i in range(1, 51):
    region = random.choice(REGIONS)
    variety = random.choice(VARIETIES)
    acres = round(random.uniform(60, 420), 0)
    # Yield depends a bit on region, variety, fertilizer, and noise
    base = {"South": 42, "Central": 46, "North": 44}[region]
    var_adj = {"InVigor L345PC": 3, "DKTC 9105": 1, "PV 581 GC": 0, "Liberty 6060": 2}[variety]
    fert = round(random.uniform(50, 160), 0)
    fert_adj = (fert - 100) * 0.08
    noise = random.gauss(0, 4)
    yield_bu = round(max(15, base + var_adj + fert_adj + noise), 1)
    irrigated = random.random() < 0.2  # 20% irrigated
    yields_rows.append({
        "field_id": f"F{i:03d}",
        "region": region,
        "variety": variety,
        "acres": int(acres),
        "yield_bu_ac": yield_bu,
        "fertilizer_kg_ha": int(fert),
        "irrigated": "TRUE" if irrigated else "FALSE",
    })

with open(os.path.join(DATA_DIR, "canola_yields_2025.csv"), "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=list(yields_rows[0].keys()))
    writer.writeheader()
    writer.writerows(yields_rows)

# =============================================================================
# DATASET 2: farm_costs_2025.csv
# Supplier-level input cost records for a grain farm
# Columns: order_id, order_date, supplier, product, price_per_unit, quantity, unit
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
for i in range(1, 41):
    product, base_price, unit = random.choice(PRODUCTS)
    supplier = random.choice(SUPPLIERS)
    # Price varies a bit around the base
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
# ANSWER KEY — print the expected answers for each of the 10 questions
# =============================================================================

yields_bu = [r["yield_bu_ac"] for r in yields_rows]
acres_list = [r["acres"] for r in yields_rows]

print("=" * 60)
print("ANSWER KEY")
print("=" * 60)

# Q1: mean yield
print(f"Q1  mean_yield_bu_ac        = {statistics.mean(yields_bu):.3f}")

# Q2: median yield
print(f"Q2  median_yield_bu_ac      = {statistics.median(yields_bu):.3f}")

# Q3: sample standard deviation
print(f"Q3  stdev_yield_bu_ac       = {statistics.stdev(yields_bu):.3f}")

# Q4: 90th percentile (linear interpolation, matches Excel PERCENTILE.INC)
def percentile_inc(data, p):
    data = sorted(data)
    n = len(data)
    rank = p * (n - 1)
    lo = int(rank)
    hi = min(lo + 1, n - 1)
    frac = rank - lo
    return data[lo] + frac * (data[hi] - data[lo])

print(f"Q4  p90_yield_bu_ac         = {percentile_inc(yields_bu, 0.90):.3f}")

# Q5: count of fields with yield > 48
q5 = sum(1 for y in yields_bu if y > 48)
print(f"Q5  count_yield_gt_48        = {q5}")

# Q6: average yield for fields in the South region
south = [r["yield_bu_ac"] for r in yields_rows if r["region"] == "South"]
print(f"Q6  avg_yield_south          = {statistics.mean(south):.3f}")

# Q7: total acres of canola by variety (highest)
from collections import defaultdict
var_acres = defaultdict(int)
for r in yields_rows:
    var_acres[r["variety"]] += r["acres"]
best = max(var_acres.items(), key=lambda x: x[1])
print(f"Q7  variety_w_most_acres    = {best[0]} ({best[1]} acres)")

# Q8: total production (bushels) of canola across all fields
# Note: bu/ac * acres = bushels
total_bu = sum(r["yield_bu_ac"] * r["acres"] for r in yields_rows)
print(f"Q8  total_production_bu     = {total_bu:.1f}")

# Q9: total spending with "Prairie Ag Supply"
prairie_total = sum(r["price_per_unit"] * r["quantity"] for r in costs_rows
                    if r["supplier"] == "Prairie Ag Supply")
print(f"Q9  prairie_total_spend     = ${prairie_total:.2f}")

# Q10: highest price per unit of Urea
urea_prices = [r["price_per_unit"] for r in costs_rows if r["product"] == "Urea"]
if urea_prices:
    print(f"Q10 max_urea_price          = ${max(urea_prices):.2f}")
else:
    print("Q10 no urea orders")

print("=" * 60)
print(f"Generated {len(yields_rows)} rows -> canola_yields_2025.csv")
print(f"Generated {len(costs_rows)} rows -> farm_costs_2025.csv")
