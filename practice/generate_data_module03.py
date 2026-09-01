#!/usr/bin/env python3
"""Generate the small teaching dataset for Module 3 (Transforming Data in R).

Module 3's dplyr examples all assume a field-level data frame called
`yields` with columns field_id, region, variety, acres, yield_bu_acre,
year, seeding_date, and units. This script writes a small synthetic CSV
with exactly those columns so a student can load it and follow every
example in the module hands-on.

It is intentionally SYNTHETIC and small (~60 fields) — this is a teaching
dataset for practising R verbs, not a data source for analysis. It also
deliberately includes a few missing yields (blank cells) and a mix of
units so the missing-value and case_when() examples have something to work
on.

Deterministic (fixed seed).

Output: data/field_yields.csv
"""

import csv
import os
import random
from datetime import date, timedelta

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
os.makedirs(DATA, exist_ok=True)
OUT = os.path.join(DATA, "field_yields.csv")

random.seed(263)

REGIONS = ["South", "Central", "North"]
VARIETIES = ["InVigor", "DKTC", "Clearfield"]
MISSING_YIELD = {7, 22, 41}   # field numbers with a blank yield

rows = []
for i in range(1, 61):
    region = random.choice(REGIONS)
    variety = random.choice(VARIETIES)
    acres = int(round(random.uniform(60, 480), 0))
    base = {"South": 42, "Central": 47, "North": 45}[region]
    var_adj = {"InVigor": 3, "DKTC": 1, "Clearfield": 0}[variety]
    yield_bu = round(max(15, base + var_adj + random.gauss(0, 5)), 1)
    year = random.choice([2024, 2025])
    seed_day = date(year, 4, 20) + timedelta(days=random.randint(0, 35))
    rows.append({
        "field_id": f"F{i:03d}",
        "region": region,
        "variety": variety,
        "acres": acres,
        "yield_bu_acre": "" if i in MISSING_YIELD else yield_bu,
        "year": year,
        "seeding_date": seed_day.isoformat(),
        "units": "bu/ac",
    })

with open(OUT, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

missing = sum(1 for r in rows if r["yield_bu_acre"] == "")
print(f"Wrote {len(rows)} rows to {OUT}")
print(f"  Columns: {', '.join(rows[0].keys())}")
print(f"  Missing-yield rows (for the NA examples): {missing}")
