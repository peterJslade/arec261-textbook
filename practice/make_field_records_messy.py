# Generates data/field_records_messy.csv: one season of spring wheat field
# records constructed to contain every issue on the module03b data-quality
# list, one issue per column where possible.
#
#   1. Awkward column names   -- every column uses a different convention
#   2. Text in numeric column -- "harvest weight" carries a " t" unit suffix
#      (weights are derived from the TRUE yield x acres x 0.02722 t/bu with
#      ~3% noise, so the file is internally consistent even on rows whose
#      yield column carries a planted code or impossible value)
#   3. Duplicates             -- F002 and F005 appear twice, exactly, with
#                                both pairs inside the first eight rows
#   4. Missing-value codes    -- yield uses -99; moisture uses N/A, missing,
#                                a blank, and 9999
#   5. Impossible values      -- one yield of -12, one of 1250 bu/ac
#   6. Mixed units            -- "N rate" is mostly kg/ha; ~30% of rows are
#                                t/ha (values below 1)
#   7. Inconsistent categories-- AAC Brandon appears as four spellings
#
# A mixed-date-formats column existed in earlier versions but was cut as
# too much for students; its random draws are kept below so every other
# value in the file stays identical.
#
# Clean values are drawn with a fixed seed, so rerunning the script
# reproduces the file exactly.

import csv
import random

random.seed(261)

N = 36

varieties_clean = ["AAC Viewfield", "CDC Landmark"]
brandon_variants = ["AAC Brandon", "Brandon", "Brandon AAC", "Brndon"]

rows = []
for i in range(1, N + 1):
    field_id = f"F{i:03d}"

    # variety: about half the fields grow Brandon, spelled four ways
    if i % 2 == 0:
        variety = brandon_variants[(i // 2) % 4]
    else:
        variety = varieties_clean[i % 2 == 0 or (i // 3) % 2]

    # discarded draws from the cut date column, kept so the values below
    # stay identical to earlier versions of the file
    random.choice([0, 1, 2, 3])
    random.randint(1, 28)

    # field size: quarters and half-sections dominate
    acres = random.choice([80, 120, 160, 160, 160, 160, 240, 320])

    # yield: plausible spring wheat, with planted problems
    y = round(random.gauss(58, 8), 1)
    if i == 7:
        yield_val = "-12"        # impossible: negative
    elif i == 19:
        yield_val = "1250"       # implausible: 20x a real yield
    elif i in (4, 23, 31):
        yield_val = "-99"        # missing-value code
    else:
        yield_val = str(y)

    # harvest weight: derived from the TRUE yield, so the columns agree
    # (1 bu spring wheat = 60 lb = 0.02722 t), with a little noise
    w = y * acres * 0.02722 * random.uniform(0.97, 1.03)
    weight = f"{round(w, 1)} t"

    # nitrogen rate: kg/ha, except ~30% of producers reported t/ha
    n_kg = round(random.uniform(80, 145), 1)
    n_rate = str(round(n_kg / 1000, 3)) if i % 3 == 0 else str(n_kg)

    # moisture: percent, with a zoo of missing codes
    if i == 6:
        moisture = "N/A"
    elif i == 14:
        moisture = "missing"
    elif i == 22:
        moisture = ""
    elif i == 30:
        moisture = "9999"
    else:
        moisture = str(round(random.uniform(11.5, 16.5), 1))

    rows.append([field_id, variety, str(acres), yield_val, weight, n_rate, moisture])

# exact duplicates of two rows, placed so both pairs sit in the
# first eight rows of the file
rows.insert(3, rows[1])   # copy of F002 as the 4th row
rows.insert(7, rows[5])   # copy of F005 as the 8th row

with open("data/field_records_messy.csv", "w", newline="") as f:
    w = csv.writer(f)
    # issue 1: every column name uses a different convention
    w.writerow(["Field ID", "VARIETY_NAME", "Acres",
                "Yield (bu/ac)", "harvest weight", "N rate", "Moisture %"])
    w.writerows(rows)

print(f"wrote data/field_records_messy.csv with {len(rows)} rows")
