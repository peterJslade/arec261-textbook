#!/usr/bin/env python3
"""Compute verified answer-key values for the Module 1 test bank.

Every numeric answer in the 120-question bank must be checked against the
real cleaned data, never guessed. This script prints a block of statistics
for each of the three datasets, organised by the section that uses them:
  1. Descriptive Statistics
  2. Conditional Functions & Lookups
  3. Charts (distribution shape, box-plot five-number summaries)
  4. PivotTables (by-group averages, crop/variety/province rankings)

Run it and copy values into the .qmd answer keys. Re-run after any data
refresh; values are stated in the bank as "as of the current snapshot".

Datasets:
  data/rm_yields_1990plus.csv       (wide)  — SK RM crop yields
  data/rm_yields_1990_2025.csv  (long)  — same, stacked by crop
  data/mb_wheat_varieties.csv               — MB wheat by variety
  data/statcan_field_crops.csv              — Canada field crops by province
"""

import csv
import os
import statistics as st

BASE = os.path.dirname(os.path.abspath(__file__))
D = os.path.join(BASE, "data")


def load(name):
    with open(os.path.join(D, name), encoding="utf-8-sig") as f:
        return list(csv.DictReader(f))


def nums(rows, col, where=None):
    out = []
    for r in rows:
        if where and not where(r):
            continue
        v = (r.get(col) or "").strip()
        if v == "":
            continue
        try:
            out.append(float(v))
        except ValueError:
            pass
    return out


def qinc(data, p):
    """Excel PERCENTILE.INC / QUARTILE.INC (== R type 7)."""
    d = sorted(data)
    n = len(d)
    if n == 0:
        return float("nan")
    rank = p * (n - 1)
    lo = int(rank)
    hi = min(lo + 1, n - 1)
    frac = rank - lo
    return d[lo] + frac * (d[hi] - d[lo])


def describe(label, vals):
    if not vals:
        print(f"  {label}: (no data)")
        return
    mean = st.mean(vals)
    med = st.median(vals)
    sd = st.stdev(vals) if len(vals) > 1 else 0.0
    cv = sd / mean if mean else float("nan")
    print(f"  {label}: n={len(vals)} mean={mean:.2f} median={med:.2f} "
          f"sd={sd:.2f} CV={cv:.3f}")
    print(f"    min={min(vals)} max={max(vals)} range={max(vals)-min(vals):.1f} "
          f"Q1={qinc(vals,.25):.2f} Q3={qinc(vals,.75):.2f} "
          f"IQR={qinc(vals,.75)-qinc(vals,.25):.2f} "
          f"P90={qinc(vals,.90):.2f}")
    # simple skew signal usable in Module 1 terms
    shape = ("mean>median -> right/high tail" if mean > med + 0.05
             else "mean<median -> left/low tail" if mean < med - 0.05
             else "mean~median -> roughly symmetric")
    print(f"    shape: {shape}")
    # 1.5*IQR outlier fences
    q1, q3 = qinc(vals, .25), qinc(vals, .75)
    iqr = q3 - q1
    lo_f, hi_f = q1 - 1.5 * iqr, q3 + 1.5 * iqr
    outliers = [v for v in vals if v < lo_f or v > hi_f]
    print(f"    outlier fences: [{lo_f:.1f}, {hi_f:.1f}] -> {len(outliers)} outliers "
          f"({sorted(outliers)[:6]}{'...' if len(outliers)>6 else ''})")


def by_group(rows, group_col, val_col, where=None, top=None):
    groups = {}
    for r in rows:
        if where and not where(r):
            continue
        g = r.get(group_col, "")
        v = (r.get(val_col) or "").strip()
        if v == "":
            continue
        try:
            groups.setdefault(g, []).append(float(v))
        except ValueError:
            pass
    ranked = sorted(groups.items(), key=lambda kv: -st.mean(kv[1]))
    if top:
        ranked = ranked[:top]
    return ranked


def hr(title):
    print("\n" + "=" * 74)
    print(title)
    print("=" * 74)


# ============================ SK RM YIELDS ============================
hr("DATASET 1 — SK RM crop yields (wide + long)")
wide = load("rm_yields_1990plus.csv")
lng = load("rm_yields_1990_2025.csv")

print("\n[Sec 1 Descriptive] Canola 2023 (wide col E):")
describe("Canola 2023", nums(wide, "Canola", lambda r: r["Year"] == "2023"))
print("\n[Sec 1 Descriptive] Spring Wheat 2023:")
describe("SpringWheat 2023", nums(wide, "Spring Wheat", lambda r: r["Year"] == "2023"))
print("\n[Sec 1 Descriptive] Canola vs Barley 2023 CV compare:")
describe("Barley 2023", nums(wide, "Barley", lambda r: r["Year"] == "2023"))

print("\n[Sec 2 Conditional] counts across all years:")
can = nums(wide, "Canola")
print(f"  canola > 40 (all years): {sum(1 for v in can if v > 40)}")
print(f"  canola blank cells 2023: "
      f"{sum(1 for r in wide if r['Year']=='2023' and r['Canola'].strip()=='')}")
print(f"  avg canola 2010: {st.mean(nums(wide,'Canola',lambda r:r['Year']=='2010')):.2f}")
print(f"  avg canola 2021 (drought): {st.mean(nums(wide,'Canola',lambda r:r['Year']=='2021')):.2f}")
print(f"  avg canola 2023: {st.mean(nums(wide,'Canola',lambda r:r['Year']=='2023')):.2f}")

print("\n[Sec 4 Pivot] avg yield by crop, 2023 (long):")
for c, v in by_group(lng, "Crop", "Yield", lambda r: r["Year"] == "2023"):
    print(f"    {c:14s} {st.mean(v):7.2f}  (n={len(v)}, unit={'lb/ac' if c=='Lentils' else 'bu/ac'})")
print("  canola 2021 vs 2023 (long):")
for yr in ("2021", "2023"):
    v = nums(lng, "Yield", lambda r: r["Crop"] == "Canola" and r["Year"] == yr)
    print(f"    {yr}: {st.mean(v):.2f} (n={len(v)})")


# ============================ MB WHEAT VARIETIES ============================
hr("DATASET 2 — MB red spring wheat by variety")
mb = load("mb_wheat_varieties.csv")
rep = [r for r in mb if r["Reported"] == "TRUE"]

print("\n[Sec 1 Descriptive] all reported yields:")
describe("MB yields (all)", nums(mb, "Yield_bu_ac"))
print("\n[Sec 1 Descriptive] 2023 only:")
describe("MB 2023", nums(mb, "Yield_bu_ac", lambda r: r["Year"] == "2023"))

print("\n[Sec 2 Conditional] reported/suppressed:")
print(f"  total rows={len(mb)} reported={len(rep)} suppressed={len(mb)-len(rep)}")
print(f"  yields > 70: {sum(1 for v in nums(mb,'Yield_bu_ac') if v>70)}")

print("\n[Sec 4 Pivot] avg yield by variety (>=30 obs), top & bottom:")
ranked = [(k, v) for k, v in by_group(rep, "Variety", "Yield_bu_ac") if len(v) >= 30]
for k, v in ranked[:5]:
    print(f"    {k[:34]:34s} {st.mean(v):5.1f}  (n={len(v)})")
print("    ...")
for k, v in ranked[-3:]:
    print(f"    {k[:34]:34s} {st.mean(v):5.1f}  (n={len(v)})")
mostv = max(by_group(rep, "Variety", "Yield_bu_ac"), key=lambda kv: len(kv[1]))
print(f"  most-grown variety: {mostv[0]} n={len(mostv[1])} mean={st.mean(mostv[1]):.1f}")
print("  AAC BRANDON (BW 932) by year:")
for yr in ("2020", "2021", "2022", "2023", "2024", "2025"):
    v = nums(rep, "Yield_bu_ac", lambda r: r["Variety"] == "AAC BRANDON (BW 932)" and r["Year"] == yr)
    if v:
        print(f"    {yr}: {st.mean(v):.1f} (n={len(v)})")


# ============================ STATCAN FIELD CROPS ============================
hr("DATASET 3 — Canada field crops by province (StatsCan)")
sc = load("statcan_field_crops.csv")

print("\n[Sec 1 Descriptive] spring wheat yields, all prov 2015-2025:")
describe("SpringWheat all", nums(sc, "Yield_bu_ac", lambda r: r["Crop"] == "Spring wheat"))
print("\n[Sec 1 Descriptive] canola yields, all prov 2015-2025:")
describe("Canola all", nums(sc, "Yield_bu_ac", lambda r: r["Crop"] == "Canola"))

print("\n[Sec 2 Conditional] blanks & sums:")
print(f"  rows with blank yield: {sum(1 for r in sc if r['Yield_bu_ac'].strip()=='')}")
tot = sum(nums(sc, "Seeded_acres", lambda r: r["Crop"] == "Canola" and r["Year"] == "2023"))
print(f"  total canola seeded acres 2023 (all prov): {tot:,.0f}")

print("\n[Sec 4 Pivot] avg canola yield by province, 2023:")
for p, v in by_group(sc, "Province", "Yield_bu_ac", lambda r: r["Crop"] == "Canola" and r["Year"] == "2023"):
    print(f"    {p:26s} {st.mean(v):.1f}")
print("  avg canola yield by province, 2015-2025:")
for p, v in by_group(sc, "Province", "Yield_bu_ac", lambda r: r["Crop"] == "Canola"):
    print(f"    {p:26s} {st.mean(v):.1f} (n={len(v)})")

print("\nDone.")
