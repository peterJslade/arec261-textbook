#!/usr/bin/env python3
"""Generate the deliberately messy delivery file for Module 3 (Working With Real Data).

Module 3 teaches cleaning and validation, so this file contains, on purpose,
every problem the chapter asks students to find:

  * duplicated rows (the same delivery recorded twice)
  * a duplicated ticket ID carrying DIFFERENT values (worse: which is right?)
  * inconsistent category spellings: "Canola", "canola", "CANOLA", " Canola"
  * mixed units in one column: most moisture in %, a few as decimals
  * impossible values: a negative weight, a moisture of 250
  * missing values, blank strings, and the literal text "N/A"
  * a column of numbers stored as text because one entry has a unit in it
  * dates in two different formats

The clean underlying data is a set of grain deliveries. Nothing here is
random noise for its own sake -- each defect maps to a section of the chapter.

Deterministic (fixed seed) so the same file is produced every time.
"""

import csv
import os
import random

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

random.seed(20260818)

CROPS = ["Canola", "Spring wheat", "Barley", "Peas"]
# The messy variants students must reconcile.
CROP_VARIANTS = {
    # Note the TRAILING space: readr strips a leading one on import, but keeps
    # a trailing one, so this is the variant that actually reaches the student.
    "Canola": ["Canola", "canola", "CANOLA", "Canola "],
    "Spring wheat": ["Spring wheat", "spring wheat", "Spring Wheat"],
    "Barley": ["Barley", "barley"],
    "Peas": ["Peas", "peas"],
}

rows = []
for i in range(1, 61):
    crop = random.choice(CROPS)
    weight = round(random.gauss(38, 7), 1)          # tonnes
    moisture = round(random.gauss(9.5, 1.4), 1)     # percent
    rows.append({
        "ticket_id": f"T{i:04d}",
        "delivery_date": f"2025-{random.randint(9,11):02d}-{random.randint(1,28):02d}",
        "crop": random.choice(CROP_VARIANTS[crop]),
        "weight_tonnes": f"{weight}",
        "moisture_pct": f"{moisture}",
        "grade": random.choice(["1", "2", "3"]),
    })

# --- Now introduce the defects, at known positions -------------------------

# 1. An exact duplicate row (same delivery entered twice).
rows.insert(12, dict(rows[11]))

# 2. A repeated ticket_id with DIFFERENT values -- a genuine conflict.
conflict = dict(rows[30])
conflict["weight_tonnes"] = str(round(float(conflict["weight_tonnes"]) + 4.2, 1))
rows.insert(31, conflict)

# 3. Impossible values.
rows[5]["weight_tonnes"] = "-12.4"      # negative weight
rows[18]["moisture_pct"] = "250"        # moisture over 100%
rows[44]["weight_tonnes"] = "0"         # a delivery of nothing

# 4. Mixed units: a few moisture readings recorded as decimals, not percent.
for idx in (9, 27, 51):
    rows[idx]["moisture_pct"] = str(round(float(rows[idx]["moisture_pct"]) / 100, 4))

# 5. Missing values in three different disguises.
rows[7]["moisture_pct"] = ""
rows[22]["grade"] = "N/A"
rows[35]["moisture_pct"] = "NA"

# 6. A weight with the unit typed into the cell. This is what actually forces
#    a numeric column to import as text -- readr parses a quoted "1,204.5"
#    happily, but it cannot make a number of "38.2 t".
rows[40]["weight_tonnes"] = "38.2 t"

# 7. Two rows using a different date format.
rows[3]["delivery_date"] = "15/10/2025"
rows[48]["delivery_date"] = "03/11/2025"

out = os.path.join(DATA_DIR, "grain_deliveries_messy.csv")
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]))
    w.writeheader()
    w.writerows(rows)

print(f"wrote {out}  ({len(rows)} rows)")
print()
print("Planted defects, for the answer key:")
print("  exact duplicate row          : ticket", rows[11]["ticket_id"])
print("  conflicting duplicate id     : ticket", conflict["ticket_id"])
print("  negative weight              : row 6")
print("  moisture = 250               : row 19")
print("  zero weight                  : row 45")
print("  moisture as decimal          : 3 rows")
print("  missing moisture ('' NA)     : 3 rows, three spellings")
print("  weight with unit '38.2 t'    : 1 row -> column imports as text")
print("  date in d/m/Y format         : 2 rows")
print("  crop spelling variants       :",
      sorted({r["crop"] for r in rows}))
