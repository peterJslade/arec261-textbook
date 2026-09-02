#!/usr/bin/env python3
"""Generate the per-question datasets for the Module 3 test bank.

Sixty questions, one small dataset each (about 20 rows), written to
practice/data/module03/. Every planted problem -- a delimiter, a missing-value
code, a duplicated row, a key that does not match -- is deliberate, so the
answer to each question is known and countable.

The files share one farm world (the same field names, crops, varieties,
elevators and weather stations) so they read as one place rather than sixty
unrelated tables.

Sections:
  1  Reading data       q01-q15   delivery tickets in awkward formats
  2  Data shape         q16-q30   wide and long tables to reshape
  3  Cleaning data      q31-q45   field records with planted problems
  4  Merging data       q46-q60   two or three small tables to join

Deterministic (fixed seed): rerunning reproduces every file exactly.
Edit this script, not the CSVs it writes. The answer keys in
module03_bank.qmd are computed from these files at render time.

Run:  python3 practice/generate_data_module03_bank.py
"""

import csv
import os
import random
import zipfile

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "data", "module03")
os.makedirs(OUT, exist_ok=True)

random.seed(263)

# ---------------------------------------------------------------------------
# Shared vocabulary
# ---------------------------------------------------------------------------
FIELDS = ["Home", "Kestrel", "Meadowvale", "Nightjar", "Rented", "Coulee",
          "Ridge", "Slough", "Northeast", "Southwest", "Bluff", "Creek",
          "Ravine", "Hilltop", "Bottom", "Corner", "Railway", "School",
          "Church", "Quarter"]
# bu/ac ranges, except lentils in lb/ac
CROP_RANGE = {"Canola": (28, 55), "Spring Wheat": (38, 72), "Durum": (32, 62),
              "Barley": (52, 92), "Oats": (70, 125), "Peas": (32, 62),
              "Flax": (16, 36), "Lentils": (1200, 2300)}
CROPS_BU = ["Canola", "Spring Wheat", "Barley", "Oats", "Peas"]
VARIETIES = ["AAC Brandon", "AAC Viewfield", "CDC Landmark", "SY Manness",
             "AAC Starbuck"]
ELEVATORS = ["Rosetown", "Kindersley", "Davidson", "Outlook", "Biggar"]
STATIONS = ["Saskatoon", "Rosetown", "Kindersley", "Outlook", "Swift Current"]
POSTAL = ["S0L 2V0", "S0L 1S0", "S0G 1B0", "S0L 2N0", "S0K 0M0", "S7K 3J7"]
PRICES = {"Canola": 14.20, "Spring Wheat": 8.10, "Barley": 5.40, "Oats": 4.60,
          "Peas": 10.30, "Durum": 9.20, "Flax": 17.50}


def r1(x):
    return round(x + 1e-9, 1)


def r2(x):
    return round(x + 1e-9, 2)


def yld(crop):
    lo, hi = CROP_RANGE[crop]
    return r1(random.uniform(lo, hi))


def acres():
    return random.choice([80, 120, 160, 160, 160, 240, 320, 320])


def write(name, header, rows, delimiter=",", preamble=None, ext="csv"):
    """Write a delimited text file. preamble is a list of raw lines written
    before the header (for the skip-rows questions)."""
    path = os.path.join(OUT, f"{name}.{ext}")
    with open(path, "w", newline="") as f:
        if preamble:
            for line in preamble:
                f.write(line + "\n")
        w = csv.writer(f, delimiter=delimiter, lineterminator="\n")
        w.writerow(header)
        for r in rows:
            w.writerow(r)
    print(f"  wrote {os.path.relpath(path, BASE)}  ({len(rows)} rows)")
    return path


# ---------------------------------------------------------------------------
# Section 1: delivery tickets
# ---------------------------------------------------------------------------
TICKET_HEADER = ["ticket_id", "permit_book", "lot_code", "delivery_date",
                 "crop", "weight_tonnes", "moisture_pct", "elevator",
                 "postal_code"]


def tickets(n=20, start_id=1, crops=None, year=2025):
    """n delivery tickets. Identifiers carry leading zeros and sixteen-digit
    permit-book numbers, so reading them as numbers destroys them."""
    crops = crops or ["Canola", "Spring Wheat", "Barley", "Peas", "Oats"]
    rows = []
    for i in range(n):
        crop = random.choice(crops)
        month = random.choice([8, 9, 9, 10, 10, 11])
        day = random.randint(1, 28)
        rows.append([
            f"{start_id + i:05d}",
            "4520" + "".join(str(random.randint(0, 9)) for _ in range(12)),
            f"{random.randint(1, 9)}-{random.randint(1, 15)}",
            f"{year}-{month:02d}-{day:02d}",
            crop,
            r1(random.uniform(18, 44)),
            r1(random.uniform(7.5, 15.5)),
            random.choice(ELEVATORS),
            random.choice(POSTAL),
        ])
    return rows


print("Section 1: reading")
# q01: plain csv; identifiers must survive
write("q01_tickets", TICKET_HEADER, tickets(20, 1))

# q02: same shape; the Excel double-click question
write("q02_tickets", TICKET_HEADER, tickets(20, 101))

# q03: semicolon delimiter with decimal commas
rows = tickets(20, 201)
rows_sc = [[str(v).replace(".", ",") if j in (5, 6) else v
            for j, v in enumerate(r)] for r in rows]
write("q03_tickets_semicolon", TICKET_HEADER, rows_sc, delimiter=";")

# q04: tab-separated
write("q04_tickets", TICKET_HEADER, tickets(20, 301), delimiter="\t", ext="tsv")

# q05: missing-value codes in moisture
rows = tickets(20, 401)
for i in random.sample(range(20), 3):
    rows[i][6] = "-99"
for i in random.sample([k for k in range(20) if rows[k][6] != "-99"], 2):
    rows[i][6] = "n/a"
write("q05_tickets_na", TICKET_HEADER, rows)

# q06: three lines of notes above the header
write("q06_tickets_notes", TICKET_HEADER, tickets(20, 501),
      preamble=["Rosetown elevator -- fall 2025 deliveries",
                "Exported from the ticket system on 2025-12-01",
                ""])

# q07: a units row under the header
rows = tickets(20, 601)
write("q07_tickets_units", TICKET_HEADER,
      [["", "", "", "yyyy-mm-dd", "", "t", "%", "", ""]] + rows)

# q08: bushels with thousands separators and a unit suffix (text column)
rows = []
for i, r in enumerate(tickets(20, 701)):
    bu = int(r[5] * random.choice([36.74, 44.09, 45.93, 36.74]))  # rough t->bu
    rows.append([r[0], r[3], r[4], f"{bu:,} bu", r[7]])
write("q08_tickets_bushels", ["ticket_id", "delivery_date", "crop", "bushels", "elevator"], rows)

# q09: one stray text value makes a numeric column character
rows = tickets(20, 801)
rows[7][6] = "tr"
write("q09_tickets_stray", TICKET_HEADER, rows)

# q10: read directly from a URL (this file is served from the site)
write("q10_tickets", TICKET_HEADER, tickets(20, 901))

# q11-q14 use openmeteo and cansim; no files.

# q15: provenance and a processed copy
write("q15_tickets", TICKET_HEADER, tickets(20, 1501))

# ---------------------------------------------------------------------------
# Section 2: shape
# ---------------------------------------------------------------------------
print("Section 2: shape")


def wide_fields(fields, crops, blanks=0):
    rows = [[f] + [yld(c) for c in crops] for f in fields]
    cells = [(i, j) for i in range(len(rows)) for j in range(1, len(crops) + 1)]
    for i, j in random.sample(cells, blanks):
        rows[i][j] = ""
    return rows


# q16: wide, no blanks
write("q16_field_crops_wide", ["field"] + CROPS_BU, wide_fields(FIELDS[:8], CROPS_BU))

# q17: wide with blanks
write("q17_field_crops_wide", ["field"] + CROPS_BU, wide_fields(FIELDS[:8], CROPS_BU, blanks=6))

# q18: long, to widen
rows = []
for f in FIELDS[:10]:
    for c in random.sample(CROPS_BU, 3):
        rows.append([f, c, yld(c)])
write("q18_field_crops_long", ["field", "crop", "yield_bu_ac"], rows)

# q19: years as columns
years = [2021, 2022, 2023, 2024, 2025]
rows = [[f] + [yld("Canola") for _ in years] for f in FIELDS[:8]]
write("q19_canola_years_wide", ["field"] + [f"yield_{y}" for y in years], rows)

# q20: crop and year in one column name
cols = [f"{c}_{y}" for c in ["canola", "wheat"] for y in [2024, 2025]]
rows = [[f] + [yld("Canola"), yld("Canola"), yld("Spring Wheat"), yld("Spring Wheat")]
        for f in FIELDS[:8]]
write("q20_crop_year_wide", ["field"] + cols, rows)

# q21: monthly precipitation by station
months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
base = [14, 10, 15, 22, 40, 68, 60, 42, 30, 20, 14, 15]
rows = [[s] + [r1(b * random.uniform(0.55, 1.5)) for b in base] for s in STATIONS]
write("q21_precip_wide", ["station"] + months, rows)

# q22: variety by year, long
rows = [[v, y, yld("Spring Wheat")] for v in VARIETIES[:4] for y in [2022, 2023, 2024, 2025]]
write("q22_variety_long", ["variety", "year", "yield_bu_ac"], rows)

# q23: three measures stacked in one column
rows = []
for f in FIELDS[:8]:
    a = acres()
    rows.append([f, "yield_bu_ac", yld("Spring Wheat")])
    rows.append([f, "acres", a])
    rows.append([f, "moisture_pct", r1(random.uniform(11, 15))])
write("q23_measures_long", ["field", "measure", "value"], rows)

# q24: prices, crops by elevator
rows = [[c] + [r2(PRICES[c] * random.uniform(0.94, 1.06)) for _ in ELEVATORS]
        for c in ["Canola", "Spring Wheat", "Barley", "Oats", "Peas", "Durum"]]
write("q24_prices_wide", ["crop"] + ELEVATORS, rows)

# q25: three id columns, four crop columns, a few blanks
rows = []
for farm in ["Slade", "Braun"]:
    for f in FIELDS[:5]:
        for y in [2024, 2025]:
            rows.append([farm, f, y] + [yld(c) for c in ["Canola", "Spring Wheat", "Barley", "Peas"]])
for i, j in random.sample([(i, j) for i in range(20) for j in range(3, 7)], 5):
    rows[i][j] = ""
write("q25_farm_fields_wide", ["farm", "field", "year", "Canola", "Spring Wheat", "Barley", "Peas"], rows)

# q26: long with absent combinations
rows = []
for f in FIELDS[:8]:
    for c in random.sample(["Canola", "Spring Wheat", "Barley", "Peas"], random.choice([2, 3, 4])):
        rows.append([f, c, yld(c)])
write("q26_field_crops_long", ["field", "crop", "yield_bu_ac"], rows)

# q27: soil test, nutrients as columns
rows = [[f, random.randint(8, 60), random.randint(5, 30), random.randint(150, 600)] for f in FIELDS[:10]]
write("q27_soil_wide", ["field", "n_ppm", "p_ppm", "k_ppm"], rows)

# q28: round trip with blanks
write("q28_field_crops_wide", ["field"] + CROPS_BU[:4], wide_fields(FIELDS[:6], CROPS_BU[:4], blanks=4))

# q29: tonnes delivered per crop per month
mons = ["sep", "oct", "nov", "dec"]
rows = [[c] + [r1(random.uniform(20, 240)) for _ in mons] for c in ["Canola", "Spring Wheat", "Barley", "Oats", "Peas"]]
write("q29_deliveries_wide", ["crop"] + mons, rows)

# q30: variety trial, sites as columns
sites = ["Outlook", "Scott", "Indian Head", "Swift Current"]
rows = [[v] + [yld("Spring Wheat") for _ in sites] for v in VARIETIES]
write("q30_trial_wide", ["variety"] + sites, rows)

# ---------------------------------------------------------------------------
# Section 3: cleaning
# ---------------------------------------------------------------------------
print("Section 3: cleaning")
MESSY_HEADER = ["Field ID", "VARIETY_NAME", "Acres", "Yield (bu/ac)",
                "Harvest Weight", "N Rate", "Moisture %"]


def records(n=20, variety_pool=None, weight_unit=False):
    """Spring wheat field records, clean. Returned as lists so a question can
    plant its own problems before writing."""
    variety_pool = variety_pool or VARIETIES[:3]
    rows = []
    for i in range(n):
        a = acres()
        y = yld("Spring Wheat")
        wt = r1(y * a * 0.02722)  # bu -> tonnes
        rows.append([f"F{i + 1:03d}", random.choice(variety_pool), a, y,
                     f"{wt} t" if weight_unit else wt,
                     r1(random.uniform(85, 135)), r1(random.uniform(11.5, 15.5))])
    return rows


def dup(rows, k):
    """Append k exact duplicates of randomly chosen rows, at random positions."""
    for i in random.sample(range(len(rows)), k):
        rows.insert(random.randint(0, len(rows)), list(rows[i]))
    return rows


# q31: awkward names + 3 exact duplicates
write("q31_records", MESSY_HEADER, dup(records(20), 3))

# q32: units typed into the weight cells
write("q32_records", MESSY_HEADER, records(20, weight_unit=True))

# q33: -99 missing code in yield
rows = records(20)
for i in random.sample(range(20), 4):
    rows[i][3] = -99
write("q33_records", MESSY_HEADER, rows)

# q34: impossible yields
rows = records(20)
i, j = random.sample(range(20), 2)
rows[i][3] = -8
rows[j][3] = 1250
write("q34_records", MESSY_HEADER, rows)

# q35: N rate in two units
rows = records(20)
for i in random.sample(range(20), 5):
    rows[i][5] = round(rows[i][5] / 1000, 3)
write("q35_records", MESSY_HEADER, rows)

# q36: one variety, four spellings
rows = records(20, variety_pool=["AAC Brandon", "CDC Landmark"])
spellings = ["Brandon", "Brandon AAC", "Brndon"]
brandon = [k for k, r in enumerate(rows) if r[1] == "AAC Brandon"]
for k, sp in zip(random.sample(brandon, min(6, len(brandon))), spellings * 2):
    rows[k][1] = sp
write("q36_records", MESSY_HEADER, rows)

# q37: crop names with case and trailing space
rows = []
for i in range(20):
    crop = random.choice(["Canola", "Spring Wheat", "Barley"])
    rows.append([f"F{i + 1:03d}", crop, acres(), yld(crop)])
variants = {"Canola": ["canola", "CANOLA", "Canola "], "Spring Wheat": ["spring wheat", "Spring wheat"],
            "Barley": ["barley", "Barley "]}
for crop, vs in variants.items():
    ks = [k for k, r in enumerate(rows) if r[1] == crop]
    for k, v in zip(random.sample(ks, min(len(vs), len(ks) - 1)), vs):
        rows[k][1] = v
write("q37_field_crops", ["field_id", "crop", "acres", "yield_bu_ac"], rows)

# q38: non-identical duplicates (same id, different yield)
rows = records(20)
orig = list(rows)
for i in random.sample(range(20), 2):
    r = list(orig[i])   # copy from the untouched list so the two picks are two fields
    r[3] = r1(r[3] + random.choice([-4.2, 3.7]))
    rows.insert(random.randint(0, len(rows)), r)
write("q38_records", MESSY_HEADER, rows)

# q39: production inconsistent with yield x acres
rows = []
for i in range(20):
    a = acres()
    y = yld("Spring Wheat")
    rows.append([f"F{i + 1:03d}", a, y, round(a * y)])
# one row about 40% low, one about 30% high, one ten times too high
for i, factor in zip(random.sample(range(20), 3), [0.62, 1.31, 10]):
    rows[i][3] = round(rows[i][3] * factor)
write("q39_production", ["field_id", "acres", "yield_bu_ac", "production_bu"], rows)

# q40: moisture typo and a 9999 code
rows = records(20)
i, j, k = random.sample(range(20), 3)
rows[i][6] = 145
rows[j][6] = 9999
rows[k][6] = 9999
write("q40_records", MESSY_HEADER, rows)

# q41: zeros with a status column
rows = []
for i in range(20):
    a = acres()
    status = random.choice(["harvested"] * 7 + ["hailed out", "not reported"])
    y = yld("Canola") if status == "harvested" else 0
    rows.append([f"F{i + 1:03d}", a, y, status])
write("q41_canola_status", ["field_id", "acres", "yield_bu_ac", "status"], rows)

# q42: all seven issues in one small file
rows = records(20, variety_pool=["AAC Brandon", "AAC Viewfield", "CDC Landmark"], weight_unit=True)
brandon = [k for k, r in enumerate(rows) if r[1] == "AAC Brandon"]
for k, sp in zip(random.sample(brandon, min(3, len(brandon))), ["Brandon", "Brandon AAC", "Brndon"]):
    rows[k][1] = sp
picks = random.sample(range(20), 7)
rows[picks[0]][3] = -99
rows[picks[1]][3] = -99
rows[picks[2]][3] = 1250
rows[picks[3]][5] = round(rows[picks[3]][5] / 1000, 3)
rows[picks[4]][5] = round(rows[picks[4]][5] / 1000, 3)
rows[picks[5]][6] = "N/A"
rows[picks[6]][6] = 9999
write("q42_records", MESSY_HEADER, dup(rows, 2))

# q43: messy grade column
rows = []
grades = ["1", "2", "3", "Feed"]
for i, r in enumerate(tickets(20, 4301)):
    rows.append([r[0], r[4], r[5], random.choice(grades)])
for k, g in zip(random.sample(range(20), 5), ["feed", "FEED", "No. 1", "No. 2", " 3"]):
    rows[k][3] = g
write("q43_tickets_grade", ["ticket_id", "crop", "weight_tonnes", "grade"], rows)

# q44: flag rather than delete
rows = records(20)
i, j, k = random.sample(range(20), 3)
rows[i][3] = 4.1
rows[j][3] = 138.0
rows[k][3] = 97.5
write("q44_records", MESSY_HEADER, rows)

# q45: an outlier that is real and one that is not
rows = []
for i in range(20):
    crop = random.choice(["Oats", "Spring Wheat", "Canola"])
    rows.append([f"F{i + 1:03d}", crop, acres(), yld(crop)])
oats = [k for k, r in enumerate(rows) if r[1] == "Oats"]
wheat = [k for k, r in enumerate(rows) if r[1] == "Spring Wheat"]
rows[oats[0]][3] = 138.5   # high but real for oats
rows[wheat[0]][3] = 210.0  # not real for wheat
write("q45_field_crops", ["field_id", "crop", "acres", "yield_bu_ac"], rows)

# ---------------------------------------------------------------------------
# Section 4: merging
# ---------------------------------------------------------------------------
print("Section 4: merging")


def field_table(n=20, crops=None, name="field"):
    crops = crops or ["Canola", "Spring Wheat", "Barley", "Oats", "Peas"]
    return [[FIELDS[i], random.choice(crops), acres(), None] for i in range(n)]


def fill_yield(rows):
    for r in rows:
        r[3] = yld(r[1])
    return rows


FIELD_HEADER = ["field", "crop", "acres", "yield_bu_ac"]

# q46: complete price lookup
write("q46_fields", FIELD_HEADER, fill_yield(field_table()))
write("q46_prices", ["crop", "price_per_bu"], [[c, PRICES[c]] for c in ["Canola", "Spring Wheat", "Barley", "Oats", "Peas"]])

# q47: lookup missing one crop (Flax)
write("q47_fields", FIELD_HEADER, fill_yield(field_table(crops=["Canola", "Spring Wheat", "Barley", "Flax", "Peas"])))
write("q47_prices", ["crop", "price_per_bu"], [[c, PRICES[c]] for c in ["Canola", "Spring Wheat", "Barley", "Peas"]])

# q48: one-to-one, different key names
rows = fill_yield(field_table())
write("q48_fields", ["field_id", "crop", "acres", "yield_bu_ac"], rows)
zones = ["Brown", "Dark Brown", "Black"]
soil = [[r[0], random.choice(zones), r1(random.uniform(2.5, 6.5))] for r in rows]
random.shuffle(soil)
write("q48_soil", ["Field", "soil_zone", "organic_matter_pct"], soil)

# q49: two-column key through a station lookup
yrs = [2023, 2024, 2025]
rows = [[f, y, yld("Canola")] for f in FIELDS[:10] for y in yrs]
write("q49_yields", ["field", "year", "yield_bu_ac"], rows)
write("q49_stations", ["field", "station"], [[f, random.choice(STATIONS[:3])] for f in FIELDS[:10]])
write("q49_rain", ["station", "year", "precip_may_aug_mm"],
      [[s, y, r1(random.uniform(120, 320))] for s in STATIONS[:3] for y in yrs])

# q50: duplicated key in the lookup (two price years)
write("q50_fields", FIELD_HEADER, fill_yield(field_table()))
rows = []
for c in ["Canola", "Spring Wheat", "Barley", "Oats", "Peas"]:
    rows.append([c, 2024, r2(PRICES[c] * 0.93)])
    rows.append([c, 2025, PRICES[c]])
write("q50_prices", ["crop", "year", "price_per_bu"], rows)

# q51: case mismatch in the key
rows = fill_yield(field_table())
for k in random.sample([k for k, r in enumerate(rows) if r[1] == "Canola"], 3):
    rows[k][1] = "canola"
write("q51_fields", FIELD_HEADER, rows)
write("q51_prices", ["crop", "price_per_bu"], [[c, PRICES[c]] for c in ["Canola", "Spring Wheat", "Barley", "Oats", "Peas"]])

# q52: two years of field lists
f24 = FIELDS[:16]
f25 = FIELDS[3:20]
write("q52_fields_2024", ["field", "crop_2024", "acres"], [[f, random.choice(CROPS_BU), acres()] for f in f24])
write("q52_fields_2025", ["field", "crop_2025", "acres"], [[f, random.choice(CROPS_BU), acres()] for f in f25])

# q53: many-to-many, buyers by crop
write("q53_fields", FIELD_HEADER, fill_yield(field_table()))
rows = []
for c in ["Canola", "Spring Wheat", "Barley", "Oats", "Peas"]:
    for e in random.sample(ELEVATORS, random.choice([2, 3])):
        rows.append([c, e, r2(PRICES[c] * random.uniform(0.93, 1.07))])
write("q53_buyers", ["crop", "elevator", "price_per_bu"], rows)

# q54-q55 use the chapter's real files (rm_yields_2015_2024, rm_lookup, station_precip).

# q56: deliveries to fields
fields = fill_yield(field_table())
write("q56_fields", FIELD_HEADER, fields)
rows = []
for i in range(30):
    f = random.choice(fields)
    rows.append([f"{5601 + i:05d}", f[0], r1(random.uniform(18, 44))])
write("q56_deliveries", ["ticket_id", "field", "weight_tonnes"], rows)

# q57: deliveries with mistyped field names
fields = fill_yield(field_table())
write("q57_fields", FIELD_HEADER, fields)
rows = []
for i in range(30):
    f = random.choice(fields)
    rows.append([f"{5701 + i:05d}", f[0], r1(random.uniform(18, 44))])
for k, bad in zip(random.sample(range(30), 3), ["Kestral", "Meadow Vale", "home"]):
    rows[k][1] = bad
write("q57_deliveries", ["ticket_id", "field", "weight_tonnes"], rows)

# q58: prices missing two crops
write("q58_fields", FIELD_HEADER, fill_yield(field_table()))
write("q58_prices", ["crop", "price_per_bu"], [[c, PRICES[c]] for c in ["Canola", "Spring Wheat", "Barley"]])

# q59: units lookup with a conversion factor to kg/ha
rows = fill_yield(field_table(crops=["Canola", "Spring Wheat", "Barley", "Oats", "Lentils"]))
write("q59_fields", ["field", "crop", "acres", "yield"], rows)
write("q59_units", ["crop", "unit", "kg_ha_per_unit"],
      [["Canola", "bu/ac", 56.0], ["Spring Wheat", "bu/ac", 67.25], ["Barley", "bu/ac", 53.8],
       ["Oats", "bu/ac", 38.1], ["Lentils", "lb/ac", 1.12]])

# q60: three tables, two joins
rows = []
for i in range(20):
    v = random.choice(VARIETIES[:4])
    rows.append([FIELDS[i], v, acres(), yld("Spring Wheat"), random.choice(ELEVATORS[:4])])
write("q60_fields", ["field", "variety", "acres", "yield_bu_ac", "elevator"], rows)
write("q60_seed", ["variety", "seed_cost_per_ac"], [[v, r2(random.uniform(28, 42))] for v in VARIETIES[:4]])
write("q60_elevators", ["elevator", "wheat_price_per_bu"], [[e, r2(8.10 * random.uniform(0.95, 1.05))] for e in ELEVATORS[:4]])

# ---------------------------------------------------------------------------
# Zip of everything, for a single download
# ---------------------------------------------------------------------------
zpath = os.path.join(OUT, "module03_bank_data.zip")
with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED) as z:
    for fn in sorted(os.listdir(OUT)):
        if fn.endswith((".csv", ".tsv")):
            z.write(os.path.join(OUT, fn), arcname=f"module03/{fn}")
print(f"  wrote {os.path.relpath(zpath, BASE)}")
