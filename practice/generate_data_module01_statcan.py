#!/usr/bin/env python3
"""Build the Canada-wide crop dataset for Module 1 practice from StatsCan.

Source: Statistics Canada, Table 32-10-0359-01 ("Estimated areas, yield,
production, average farm price and total farm value of principal field
crops, in metric and imperial units"), product ID 32100359.

Full-table download (English):
    https://www150.statcan.gc.ca/n1/tbl/csv/32100359-eng.zip

The raw table is ~390k rows in StatsCan's standard long format: every
combination of REF_DATE x GEO x "Harvest disposition" (the measure) x
"Type of crop" x unit is one row, with the number in the VALUE column and
a STATUS/SYMBOL column carrying data-quality flags. It goes back to 1908
and mixes provinces with national/regional aggregates and many units.

We filter and reshape it to a clean, teaching-friendly table:
  * Years 2015-2025.
  * The 10 provinces only (drop Canada / East / West / Prairie provinces /
    Maritime provinces aggregates).
  * The major field crops that report yield in BUSHELS per acre, so units
    are consistent (this excludes hay [tons], potatoes [cwt], and the
    small-seeded pulses/oilseeds like lentils/chickpeas/mustard, which
    StatsCan reports in lb/ac).
  * Two measures pivoted into columns: Seeded area (acres) and Average
    yield (bushels per acre).

Output:
    statcan_field_crops.csv
    [A] Year  [B] Province  [C] Crop  [D] Seeded_acres  [E] Yield_bu_ac

A cell is blank when StatsCan did not publish that value (crop not grown in
that province/year, or suppressed). Blanks are real non-observations --
never fill them with 0.

Usage:
    python3 generate_data_module01_statcan.py
    (Reads the already-downloaded 32100359.csv in practice/data_raw/. If it
     is not present, re-download the zip from the URL above and unzip it
     there first.)
"""

import csv
import os
from collections import defaultdict

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_PATH = os.path.join(BASE_DIR, "data_raw", "32100359.csv")
OUT_PATH = os.path.join(DATA_DIR, "statcan_field_crops.csv")

PROVINCES = {
    "Newfoundland and Labrador", "Prince Edward Island", "Nova Scotia",
    "New Brunswick", "Quebec", "Ontario", "Manitoba", "Saskatchewan",
    "Alberta", "British Columbia",
}

# Major field crops reported in bushels/acre. We keep the top-level crop
# categories and drop the granular wheat sub-classes (CWRS, CNHR, ...) and
# near-duplicate roll-ups ("Wheat, all excluding durum") to keep it clean.
CROP_MAP = {
    "Wheat, all": "Wheat (all)",
    "Wheat, spring": "Spring wheat",
    "Wheat, durum": "Durum wheat",
    "Wheat, winter remaining": "Winter wheat",
    "Barley": "Barley",
    "Canola (rapeseed)": "Canola",
    "Oats": "Oats",
    "Peas, dry": "Dry peas",
    "Flaxseed": "Flax",
    "Rye, all": "Rye",
    "Corn for grain": "Corn for grain",
    "Soybeans": "Soybeans",
    "Mixed grains": "Mixed grains",
}

SEEDED = "Seeded area (acres)"
YIELD = "Average yield (bushels per acre)"


def main():
    # (Year, Province, Crop) -> {"seeded": value, "yield": value}
    table = defaultdict(dict)
    with open(RAW_PATH, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            year = r["REF_DATE"]
            if not (year.isdigit() and 2015 <= int(year) <= 2025):
                continue
            if r["GEO"] not in PROVINCES:
                continue
            crop = CROP_MAP.get(r["Type of crop"])
            if crop is None:
                continue
            disp = r["Harvest disposition"]
            if disp == SEEDED:
                key = "seeded"
            elif disp == YIELD:
                key = "yield"
            else:
                continue
            value = r["VALUE"].strip()
            table[(year, r["GEO"], crop)][key] = value

    # Emit one row per (Year, Province, Crop) that has at least one measure.
    # Treat 0 seeded acres and 0 yield as missing: StatsCan uses 0 for
    # negligible/placeholder cases (e.g. Newfoundland canola), and a genuine
    # "0 bu/ac on 0 acres" is a non-observation, not real data.
    def blank_if_zero(v):
        try:
            return "" if float(v) == 0 else v
        except (ValueError, TypeError):
            return v

    out_rows = []
    for (year, prov, crop), meas in table.items():
        seeded = blank_if_zero(meas.get("seeded", ""))
        yld = blank_if_zero(meas.get("yield", ""))
        if seeded == "" and yld == "":
            continue
        out_rows.append({
            "Year": year, "Province": prov, "Crop": crop,
            "Seeded_acres": seeded, "Yield_bu_ac": yld,
        })

    # Sort for a stable, human-readable file: year, province, crop.
    out_rows.sort(key=lambda d: (d["Year"], d["Province"], d["Crop"]))

    fieldnames = ["Year", "Province", "Crop", "Seeded_acres", "Yield_bu_ac"]
    with open(OUT_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    years = sorted({r["Year"] for r in out_rows})
    provs = sorted({r["Province"] for r in out_rows})
    crops = sorted({r["Crop"] for r in out_rows})
    with_yield = sum(1 for r in out_rows if r["Yield_bu_ac"] != "")
    print(f"Wrote {len(out_rows)} rows to {OUT_PATH}")
    print(f"  Years:      {years[0]}-{years[-1]}")
    print(f"  Provinces:  {len(provs)}")
    print(f"  Crops:      {len(crops)} -> {', '.join(crops)}")
    print(f"  Rows with a published yield: {with_yield}")


if __name__ == "__main__":
    main()
