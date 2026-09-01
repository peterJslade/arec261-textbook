#!/usr/bin/env python3
"""Build the small demo dataset for Peter's Module 1 video walk-through.

This is deliberately SEPARATE from the test-bank datasets, so students who
watch the video and then work the bank are practising transfer, not
replaying the same numbers.

Base data is a small, real slice of Statistics Canada Table 32-10-0359
(the same source as statcan_field_crops.csv): 5 major crops x 5 provinces
x 2 years = 49 rows. Small enough to show on screen, but with two
categorical columns (Crop, Province), a Year column, and two numeric
columns (seeded acres, yield) so the video can demo every Module 1 topic:

  * descriptive stats (mean/median/SD/percentiles) on Yield_bu_ac
  * conditional functions (AVERAGEIF by crop/province, COUNTIF, SUMIF)
  * rate vs total: Production = Yield_bu_ac x Seeded_acres
  * PivotTables by Crop and Province, and by Year
  * charts: histogram of yields, box plot by crop, bar chart by province
  * one real blank (Alberta soybeans 2024) for the missing-data lesson

A SECOND file, crop_prices.csv, is a small lookup table (Crop -> price per
bushel + unit) so the video can demo VLOOKUP / XLOOKUP and then compute
revenue (Production x price). Prices are round, illustrative figures for
teaching — not official market data.

Output:
  data/farm_demo_2023_2024.csv   (49 rows: Year, Province, Crop, Seeded_acres, Yield_bu_ac)
  data/crop_prices.csv           (5 rows: Crop, Price_per_bu, Unit)

Usage: python3 generate_data_module01_demo.py
"""

import csv
import os

BASE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(BASE, "data")
SRC = os.path.join(DATA, "statcan_field_crops.csv")
OUT = os.path.join(DATA, "farm_demo_2023_2024.csv")
OUT_PRICES = os.path.join(DATA, "crop_prices.csv")

CROPS = ["Canola", "Spring wheat", "Barley", "Oats", "Soybeans"]
PROVINCES = ["Manitoba", "Saskatchewan", "Alberta", "Ontario", "Quebec"]
YEARS = ["2023", "2024"]

# Illustrative teaching prices ($/bushel). Round numbers on purpose.
CROP_PRICES = {
    "Canola": 14.00,
    "Spring wheat": 8.00,
    "Barley": 5.50,
    "Oats": 4.50,
    "Soybeans": 13.00,
}


def main():
    rows = []
    with open(SRC, encoding="utf-8-sig") as f:
        for r in csv.DictReader(f):
            if (r["Crop"] in CROPS and r["Province"] in PROVINCES
                    and r["Year"] in YEARS):
                rows.append({
                    "Year": r["Year"],
                    "Province": r["Province"],
                    "Crop": r["Crop"],
                    "Seeded_acres": r["Seeded_acres"],
                    "Yield_bu_ac": r["Yield_bu_ac"],
                })

    # Stable, readable order: year, then province, then crop.
    rows.sort(key=lambda d: (d["Year"], d["Province"], d["Crop"]))

    with open(OUT, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "Year", "Province", "Crop", "Seeded_acres", "Yield_bu_ac"])
        w.writeheader()
        w.writerows(rows)

    with open(OUT_PRICES, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["Crop", "Price_per_bu", "Unit"])
        w.writeheader()
        for crop in CROPS:
            w.writerow({"Crop": crop,
                        "Price_per_bu": f"{CROP_PRICES[crop]:.2f}",
                        "Unit": "$/bushel"})

    blanks = [r for r in rows if not r["Yield_bu_ac"].strip()]
    print(f"Wrote {len(rows)} rows to {OUT}")
    print(f"  Crops: {', '.join(CROPS)}")
    print(f"  Provinces: {', '.join(PROVINCES)}")
    print(f"  Years: {', '.join(YEARS)}")
    print(f"  Blank-yield rows (missing-data teaching point): {len(blanks)}"
          + (f" -> {blanks[0]['Year']} {blanks[0]['Province']} {blanks[0]['Crop']}" if blanks else ""))
    print(f"Wrote {len(CROPS)} rows to {OUT_PRICES} (lookup table)")


if __name__ == "__main__":
    main()
