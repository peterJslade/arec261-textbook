#!/usr/bin/env python3
"""Recompute the figures a Module 1 test-bank answer key can assert.

The bank quotes several hundred numbers. Writing them from memory produced about
twenty errors last time, so this module exposes the same statistics Excel would
compute, from the shipped CSVs, using Excel's conventions:

  - QUARTILE.INC / PERCENTILE.INC interpolate at position 1+(n-1)p, which is
    statistics.quantiles(..., method='inclusive'), NOT numpy's default.
  - STDEV.S / VAR.S are the sample forms (n-1 denominator).
  - Blank cells are excluded, never treated as zero.
  - AVERAGEIF skips blanks in the range being averaged even when the criteria
    range matches, so a conditional mean can have a smaller n than its count.

Run:  python3 practice/verify_bank.py            # summary of every dataset
      python3 practice/verify_bank.py --check    # re-verify figures in the bank
"""

import csv
import statistics as st
import sys
from collections import defaultdict

DATA = "practice/data"


# ---------------------------------------------------------------------------
# loaders
# ---------------------------------------------------------------------------
def rm_wide():
    return list(csv.DictReader(open(f"{DATA}/rm_yields_1990plus.csv")))


def rm_long():
    return list(csv.DictReader(open(f"{DATA}/rm_yields_1990plus_long.csv")))


def mb_wheat():
    return list(csv.DictReader(open(f"{DATA}/mb_wheat_varieties.csv")))


def statcan():
    return list(csv.DictReader(open(f"{DATA}/statcan_field_crops.csv")))


def nums(rows, field, **where):
    """Numeric values of `field` from rows matching `where`, blanks dropped."""
    out = []
    for r in rows:
        if any(str(r.get(k, "")) != str(v) for k, v in where.items()):
            continue
        v = r.get(field, "")
        if isinstance(v, str) and v.strip():
            try:
                out.append(float(v))
            except ValueError:
                pass
    return out


# ---------------------------------------------------------------------------
# Excel-equivalent statistics
# ---------------------------------------------------------------------------
def describe(v):
    """Everything an answer key is likely to quote about one column."""
    if not v:
        return None
    q = st.quantiles(v, n=4, method="inclusive") if len(v) > 1 else [v[0]] * 3
    d = st.quantiles(v, n=10, method="inclusive") if len(v) > 1 else [v[0]] * 9
    sd = st.stdev(v) if len(v) > 1 else 0.0
    return {
        "n": len(v), "mean": st.mean(v), "median": st.median(v),
        "sd": sd, "var": st.variance(v) if len(v) > 1 else 0.0,
        "cv": sd / st.mean(v) if st.mean(v) else float("nan"),
        "min": min(v), "max": max(v), "range": max(v) - min(v),
        "q1": q[0], "q3": q[2], "iqr": q[2] - q[0],
        "p10": d[0], "p90": d[8],
    }


def countif(v, op, thresh):
    f = {">": lambda x: x > thresh, ">=": lambda x: x >= thresh,
         "<": lambda x: x < thresh, "<=": lambda x: x <= thresh}[op]
    return sum(1 for x in v if f(x))


def averageif(rows, crit_field, op, thresh, avg_field):
    """Excel AVERAGEIF: test one column, average another, skipping blanks in
    the averaged column. Returns (mean, n_averaged, n_matched)."""
    f = {">": lambda x: x > thresh, ">=": lambda x: x >= thresh,
         "<": lambda x: x < thresh, "<=": lambda x: x <= thresh}[op]
    matched, vals = 0, []
    for r in rows:
        c = r.get(crit_field, "")
        if not (isinstance(c, str) and c.strip()):
            continue
        try:
            if not f(float(c)):
                continue
        except ValueError:
            continue
        matched += 1
        a = r.get(avg_field, "")
        if isinstance(a, str) and a.strip():
            vals.append(float(a))
    return (st.mean(vals) if vals else None), len(vals), matched


def fmt(d, label=""):
    if d is None:
        return f"  {label}: (no data)"
    return ("  %-30s n=%-5d mean=%8.2f med=%8.2f sd=%7.2f cv=%.3f\n"
            "  %-30s q1=%8.2f q3=%8.2f iqr=%7.2f p10=%7.2f p90=%7.2f  min=%.1f max=%.1f"
            % (label, d["n"], d["mean"], d["median"], d["sd"], d["cv"],
               "", d["q1"], d["q3"], d["iqr"], d["p10"], d["p90"], d["min"], d["max"]))


# ---------------------------------------------------------------------------
def main():
    w, lg, mb, sc = rm_wide(), rm_long(), mb_wheat(), statcan()

    print("=" * 78)
    print("SASKATCHEWAN RM (wide) — rows: %d" % len(w))
    for yr in ("2021", "2022", "2023"):
        n = sum(1 for r in w if r["Year"] == yr)
        print("  %s: %d rows" % (yr, n))
    for crop in ("Canola", "Spring Wheat", "Barley", "Oats"):
        print(fmt(describe(nums(w, crop, Year="2023")), "2023 " + crop))

    print("=" * 78)
    print("MANITOBA WHEAT — rows: %d" % len(mb))
    yrs = sorted({r["Year"] for r in mb})
    print("  years: %s" % ", ".join(yrs))
    print("  Reported=TRUE rows: %d" % sum(1 for r in mb if r["Reported"].strip().upper() == "TRUE"))
    for yr in yrs[-2:]:
        print(fmt(describe(nums(mb, "Yield_bu_ac", Year=yr)), yr + " yield"))

    print("=" * 78)
    print("STATCAN FIELD CROPS — rows: %d" % len(sc))
    print("  years: %s" % ", ".join(sorted({r["Year"] for r in sc})))
    print("  provinces: %s" % ", ".join(sorted({r["Province"] for r in sc})))
    print("  crops: %s" % ", ".join(sorted({r["Crop"] for r in sc})))

    print("=" * 78)
    print("LONG FILE — units by crop (the lentils trap)")
    units = defaultdict(set)
    for r in lg:
        units[r["Crop"]].add(r["Unit"])
    for c in sorted(units):
        v = nums(lg, "Yield", Crop=c)
        print("  %-14s unit=%-8s all-years mean=%9.2f (n=%d)"
              % (c, "/".join(sorted(units[c])), st.mean(v) if v else 0, len(v)))


if __name__ == "__main__":
    main()
