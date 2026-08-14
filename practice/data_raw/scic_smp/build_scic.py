#!/usr/bin/env python3
"""Download and parse SCIC 'Sask Management Plus' average-yield-by-variety PDFs.

Source: https://www.scic.ca/resources/sask-management-plus
One PDF per risk zone (1..21):
  https://www.scic.ca/uploads/resource-centre-files/ci-SMP-average-yield-risk-zone-N.pdf

Each PDF is a table: Crop | Variety | 5yr-avg-yield | then per year 2021..2025
a pair of (Acres, Yield). A dot '.' means no data. Crop is printed only on the
first row of each crop group (that row starts at the left margin); subsequent
variety rows are indented.

Output: one tidy long-format CSV, sask_variety_yields.csv, with columns
  Risk_Zone, Crop, Variety, Year, Acres, Yield
covering 2021-2025 across all 21 zones. (Yield units: bu/ac for most crops;
Canary Seed / lentils are reported in lb/ac — flagged by the Crop name.)

Requires poppler's `pdftotext` (already on this machine). SCIC blocks
non-browser user-agents, so downloads send a browser UA.

Run: python3 build_scic.py
"""

import csv
import os
import re
import subprocess
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_CSV = os.path.join(HERE, "..", "..", "data", "sask_variety_yields.csv")
UA = ("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
      "AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16 Safari/605.1.15")
URL = ("https://www.scic.ca/uploads/resource-centre-files/"
       "ci-SMP-average-yield-risk-zone-{}.pdf")
YEARS = ["2021", "2022", "2023", "2024", "2025"]

# Known SCIC crop-group labels (longest-first so multi-word / subtype match first).
CROPS = sorted([
    "Wheat - Hard Red Spring", "Wheat - Canada Prairie Spring",
    "Wheat - Canada Western Red Winter", "Wheat - Soft White Spring",
    "Wheat - Durum", "Wheat - Winter", "Wheat",
    "IP Canola/Rapeseed", "Canola/Rapeseed",
    "Lentils - Red", "Lentils - Large Green", "Lentils - Small Green",
    "Lentils - Medium Green", "Lentils",
    "Field Peas", "Fall Rye", "Spring Rye", "Rye",
    "Canary Seed", "Barley", "Oats", "Flax", "Soybean", "Soybeans",
    "Mustard - Yellow", "Mustard - Brown", "Mustard - Oriental", "Mustard",
    "Chickpeas - Desi", "Chickpeas - Kabuli", "Chickpeas", "Chickpea",
    "Sunflower", "Triticale",
    "Grain Corn", "Corn",
    "Hemp Grain", "Hemp",
    "Khorasan wheat/Kamut brand", "Khorasan",
    "Coriander", "Fababeans", "Faba Beans",
], key=len, reverse=True)

SKIP = re.compile(
    r"Average Yield by Variety|Crop Year|Minimum of|Saskatchewan Crop Insurance|"
    r"Bu\s+Bu|^Crop\s+Variety|5 year|Avg Bu|information reported|greater than zero|"
    r"Acres\s+Yield")


def download(zone):
    path = os.path.join(HERE, f"zone{zone}.pdf")
    if not os.path.exists(path) or os.path.getsize(path) < 5000:
        req = urllib.request.Request(URL.format(zone),
                                     headers={"User-Agent": UA,
                                              "Accept": "application/pdf,*/*"})
        with urllib.request.urlopen(req) as r:
            open(path, "wb").write(r.read())
    return path


def to_text(pdf):
    txt = pdf.replace(".pdf", ".txt")
    subprocess.run(["pdftotext", "-layout", pdf, txt],
                   check=True, capture_output=True)
    return txt


def split_crop_variety(text):
    for c in CROPS:
        if text == c or text.startswith(c + " "):
            return c, text[len(c):].strip()
    # fallback: first token is the crop
    parts = text.split()
    return parts[0], " ".join(parts[1:])


def clean(x):
    return "" if x == "." else x.replace(",", "")


def parse(txtfile, zone):
    rows = []
    crop = None
    for ln in open(txtfile, encoding="utf-8").read().split("\n"):
        if not ln.strip() or SKIP.search(ln):
            continue
        toks = ln.split()
        i = len(toks) - 1
        nums = []
        while i >= 0 and re.fullmatch(r"[\d,\.]+|\.", toks[i]):
            nums.insert(0, toks[i])
            i -= 1
        text = " ".join(toks[:i + 1])
        if len(nums) != 11 or not text:
            continue
        lead = len(ln) - len(ln.lstrip())
        if lead == 0:
            crop, variety = split_crop_variety(text)
        else:
            variety = text
        for yi, yr in enumerate(YEARS):
            rows.append({
                "Risk_Zone": zone, "Crop": crop, "Variety": variety,
                "Year": yr,
                "Acres": clean(nums[1 + yi * 2]),
                "Yield": clean(nums[2 + yi * 2]),
            })
    return rows


def main():
    all_rows = []
    for zone in range(1, 22):
        try:
            pdf = download(zone)
            txt = to_text(pdf)
            rows = parse(txt, zone)
            all_rows.extend(rows)
            nb = sum(1 for r in rows if r["Yield"])
            print(f"zone {zone:2d}: {len(rows)} rows ({nb} with yield), "
                  f"{len(set(r['Variety'] for r in rows))} varieties, "
                  f"{len(set(r['Crop'] for r in rows))} crops")
        except Exception as e:
            print(f"zone {zone:2d}: ERROR {type(e).__name__}: {e}")

    os.makedirs(os.path.dirname(OUT_CSV), exist_ok=True)
    with open(OUT_CSV, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=[
            "Risk_Zone", "Crop", "Variety", "Year", "Acres", "Yield"])
        w.writeheader()
        w.writerows(all_rows)
    print(f"\nWrote {len(all_rows)} rows to {OUT_CSV}")
    print(f"  Zones: {len(set(r['Risk_Zone'] for r in all_rows))}")
    print(f"  Crops: {sorted(set(r['Crop'] for r in all_rows))}")


if __name__ == "__main__":
    main()
