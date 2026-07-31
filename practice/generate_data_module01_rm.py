#!/usr/bin/env python3
"""Build the Module 1 practice dataset from Saskatchewan's real RM yield data.

Source (live, updated by the Government of Saskatchewan):
    https://dashboard.saskatchewan.ca/export/rm-yields-data/4950.csv

The raw file is large (26k+ rows, 1938-2025, 16 crops, many blank cells for
crops not grown in a given RM/year). For an introductory Excel module we
filter it down to:
  * Years 1990 onward (the modern, well-populated era), and
  * The 8 broadly-grown crops (each >= ~59% filled in 1990+):
    Spring Wheat, Durum, Canola, Barley, Oats, Peas, Lentils, Flax.

This writes TWO files, the same data in two shapes (see Module 1's
"Wide vs. Long Data" section):
  * rm_yields_1990plus.csv       — WIDE: one row per RM-year, each crop a
                                   column. Used for descriptive stats/lookups.
      [A] Year [B] RM [C] Spring Wheat [D] Durum [E] Canola
      [F] Barley [G] Oats [H] Peas [I] Lentils [J] Flax
  * rm_yields_1990plus_long.csv  — LONG: one row per RM-year-crop, with a
                                   Crop column and a Unit column. Used for
                                   PivotTables (grouping by crop). Blank
                                   (non-observed) cells become absent rows.
      [A] Year [B] RM [C] Crop [D] Yield [E] Unit

Blank cells are preserved (a crop not grown in that RM/year). This is real
data, so a handful of blanks remain even in the kept crops — that is a feature,
not a bug: it lets the practice questions exercise how Excel's AVERAGE/COUNT
handle blanks.

Because the source file is updated over time (new years added, historical
revisions), regenerate this file periodically. Exact numeric answers in the
practice bank are stated "as of the current snapshot" and the answer key
emphasises the METHOD (which filter + which formula), which stays correct.

Usage:
    python3 generate_data_module01_rm.py
"""

import csv
import os
import ssl
import urllib.request

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

SOURCE_URL = "https://dashboard.saskatchewan.ca/export/rm-yields-data/4950.csv"
OUT_PATH = os.path.join(DATA_DIR, "rm_yields_1990plus.csv")
OUT_PATH_LONG = os.path.join(DATA_DIR, "rm_yields_1990plus_long.csv")

MIN_YEAR = 1990
CROPS = [
    "Spring Wheat", "Durum", "Canola", "Barley",
    "Oats", "Peas", "Lentils", "Flax",
]
KEEP_COLUMNS = ["Year", "RM"] + CROPS

# Every crop is reported in bushels/acre except lentils (pounds/acre).
CROP_UNITS = {c: ("lb/ac" if c == "Lentils" else "bu/ac") for c in CROPS}


def main():
    print(f"Downloading {SOURCE_URL} ...")
    # Prefer certifi's CA bundle if available (avoids the macOS "certificate
    # verify failed" error where Python has no system trust store wired up).
    try:
        import certifi
        ctx = ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        ctx = ssl.create_default_context()
    with urllib.request.urlopen(SOURCE_URL, context=ctx) as resp:
        raw = resp.read().decode("utf-8-sig")

    reader = csv.DictReader(raw.splitlines())
    rows = [
        r for r in reader
        if r["Year"].strip().isdigit() and int(r["Year"]) >= MIN_YEAR
    ]

    # --- Wide format: one row per RM-year, each crop its own column. ---
    with open(OUT_PATH, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=KEEP_COLUMNS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    # --- Long format: one row per RM-year-crop. Blanks (non-observations)
    #     are dropped entirely, and a Unit column is added so lentils
    #     (lb/ac) are never silently compared against bu/ac crops. ---
    long_rows = []
    for r in rows:
        for crop in CROPS:
            value = r.get(crop, "").strip()
            if value == "":
                continue
            long_rows.append({
                "Year": r["Year"], "RM": r["RM"], "Crop": crop,
                "Yield": value, "Unit": CROP_UNITS[crop],
            })
    with open(OUT_PATH_LONG, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["Year", "RM", "Crop", "Yield", "Unit"])
        writer.writeheader()
        writer.writerows(long_rows)

    years = sorted({int(r["Year"]) for r in rows})
    rms = sorted({int(r["RM"]) for r in rows if r["RM"].strip().isdigit()})
    print(f"Wrote {len(rows)} rows to {OUT_PATH} (wide)")
    print(f"Wrote {len(long_rows)} rows to {OUT_PATH_LONG} (long)")
    print(f"  Years:   {years[0]}-{years[-1]}")
    print(f"  RMs:     {len(rms)} distinct")
    print(f"  Crops:   {', '.join(CROPS)}")


if __name__ == "__main__":
    main()
