#!/usr/bin/env python3
"""Clean the Manitoba red spring wheat varietal-yield data for Module 1 practice.

The raw source file (dropped in the repo as MB_2020_2025_wheat_varieties.csv)
is a Manitoba Agricultural Services Corporation (MASC) export of red spring
wheat yields by variety, municipality, and year (2020-2025). It is messy in
several instructive ways:

  * It is TAB-separated despite the .csv name.
  * The header splits the yield columns: "Yield/Acre" + "(Metric)" and
    "Yield/Acre" + "(Imperial)" are four physical fields, and each data row
    repeats the unit words ("Tonnes", "Bushels").
  * Many rows read "Below Minimum Tolerance" instead of a yield: MASC
    suppresses a variety's yield in a municipality when too few farms grew
    it (a privacy threshold). This is a DIFFERENT kind of missing data than
    "not grown" -- the crop was grown, the number is just withheld.
  * Numbers carry thousands separators ("1,411.0").
  * There are stray junk rows (a "Summary" year, blank lines).

This script produces a clean, comma-separated, one-observation-per-row file:

    mb_wheat_varieties.csv
    [A] Year  [B] Municipality  [C] Variety  [D] Farms  [E] Acres
    [F] Yield_bu_ac  [G] Reported

  * Yield_bu_ac is blank when the yield was suppressed.
  * Reported is TRUE when a real yield is present, FALSE when suppressed --
    so students can COUNT/filter on data availability, and see that a blank
    here means "withheld for privacy," not "zero" and not "not grown."

Only red spring wheat is in the source, so Crop is dropped (constant).
Metric (tonnes) yield is dropped; we keep bushels/acre to match the rest of
the course.

Usage:
    python3 generate_data_module01_mb.py
"""

import csv
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
# The raw MASC export lives alongside the cleaner, in practice/data_raw/.
RAW_PATH = os.path.join(BASE_DIR, "data_raw", "MB_2020_2025_wheat_varieties.csv")
OUT_PATH = os.path.join(DATA_DIR, "mb_wheat_varieties.csv")

VALID_YEARS = {"2020", "2021", "2022", "2023", "2024", "2025"}


def clean_number(text):
    """Strip thousands separators; return '' if not a number."""
    t = text.replace(",", "").strip()
    if t == "":
        return ""
    try:
        float(t)
        return t
    except ValueError:
        return ""


def tidy_variety(text):
    """Normalise the variety string: collapse internal whitespace, trim."""
    return " ".join(text.split()).strip()


def main():
    out_rows = []
    with open(RAW_PATH, encoding="utf-8-sig") as f:
        f.readline()  # discard the messy header
        for line in f:
            cells = line.rstrip("\n").split("\t")
            if len(cells) < 5:
                continue  # blank / junk line
            year = cells[0].strip()
            if year not in VALID_YEARS:
                continue  # drops the "Summary" row and blanks

            municipality = cells[1].strip()
            variety = tidy_variety(cells[3])
            farms_raw = cells[4].strip()

            # Suppressed rows have "Below" in the Farms column
            # ("Below" / "Minimum" / "Tolerance" spread across cells).
            if farms_raw == "Below":
                out_rows.append({
                    "Year": year, "Municipality": municipality,
                    "Variety": variety, "Farms": "", "Acres": "",
                    "Yield_bu_ac": "", "Reported": "FALSE",
                })
                continue

            farms = clean_number(cells[4])
            acres = clean_number(cells[5])
            # Imperial yield is physical column index 8 (0-based).
            yield_bu = clean_number(cells[8]) if len(cells) > 8 else ""
            if yield_bu == "":
                # No usable number -> treat as suppressed/unreported.
                out_rows.append({
                    "Year": year, "Municipality": municipality,
                    "Variety": variety, "Farms": "", "Acres": "",
                    "Yield_bu_ac": "", "Reported": "FALSE",
                })
                continue

            out_rows.append({
                "Year": year, "Municipality": municipality,
                "Variety": variety, "Farms": farms, "Acres": acres,
                "Yield_bu_ac": yield_bu, "Reported": "TRUE",
            })

    fieldnames = ["Year", "Municipality", "Variety", "Farms", "Acres",
                  "Yield_bu_ac", "Reported"]
    with open(OUT_PATH, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(out_rows)

    reported = [r for r in out_rows if r["Reported"] == "TRUE"]
    years = sorted({r["Year"] for r in out_rows})
    munis = sorted({r["Municipality"] for r in out_rows})
    varieties = sorted({r["Variety"] for r in out_rows})
    print(f"Wrote {len(out_rows)} rows to {OUT_PATH}")
    print(f"  Reported (real yield): {len(reported)}")
    print(f"  Suppressed:            {len(out_rows) - len(reported)}")
    print(f"  Years:                 {years[0]}-{years[-1]}")
    print(f"  Municipalities:        {len(munis)}")
    print(f"  Varieties:             {len(varieties)}")


if __name__ == "__main__":
    main()
