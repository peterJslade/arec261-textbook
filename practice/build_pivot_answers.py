#!/usr/bin/env python3
"""Answer workbooks for the PivotTable questions.

openpyxl cannot create a pivot, so these are built with the excel-pivot-tables
skill, which writes the OOXML cache/table parts directly and also fills in the
result cells. Excel opens them with a live field list.

Each workbook carries the source data on a Data tab and the finished pivot on a
PivotTable tab, so a student can see the input and the output together.

The per-question pivot spec (axes, value field, aggregation, crop/year filters)
lives in practice/pivot_spec.json. Edit that, not this file, to change a pivot.

Run:  python3 practice/build_pivot_answers.py
"""
import csv, json, os, shutil, sys
sys.path.insert(0, os.path.expanduser("~/.claude/skills/excel-pivot-tables/scripts"))
from xlsx_pivot import add_pivot_table
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

DATA, OUT = "practice/data", "practice/answers"
FILES = {"rm_long": "rm_yields_1990_2025.csv",
         "mb":      "mb_wheat_varieties.csv",
         "sc":      "statcan_field_crops.csv"}
NUMCOL = {"rm_long": {"Yield"},
          "mb":      {"Farms", "Acres", "Yield_bu_ac"},
          "sc":      {"Seeded_acres", "Yield_bu_ac"}}
VALFIELD = {"rm_long": "Yield", "mb": "Yield_bu_ac", "sc": "Yield_bu_ac"}
AGGFMT = {"Average": "0.00", "Count": "#,##0", "Sum": "#,##0"}

HEAD = PatternFill("solid", fgColor="4A7C59")
f_h = Font(name="Arial", size=10, bold=True, color="FFFFFF")
f_b = Font(name="Arial", size=10, color="24302A")
f_t = Font(name="Arial", size=12, bold=True, color="4A7C59")
CEN = Alignment(horizontal="center")


def write_data(path, ds, years=None, crop=None, unit_bu=False):
    rows = list(csv.DictReader(open(f"{DATA}/{FILES[ds]}")))
    # A question about one crop ships that crop only, so the pivot the student
    # builds from this Data tab reproduces the answer key exactly.
    if crop:
        rows = [r for r in rows if r.get("Crop", "").strip().lower() == crop.lower()]
    # several questions say "bu/ac" -- the long file also carries lentils in lb/ac,
    # which would sit at the top of any yield ranking as a pure unit artefact
    if unit_bu:
        rows = [r for r in rows if r.get("Unit", "bu/ac").strip() == "bu/ac"]
    # The long RM file is 71k rows and the pivot cache copies every record, so a
    # question about two named years ships those years only -- both to keep the
    # workbook small and because that is the slice the question is about.
    if years:
        rows = [r for r in rows if r.get("Year") in years]
    cols = list(rows[0].keys())
    num = NUMCOL[ds]
    wb = Workbook(); ws = wb.active; ws.title = "Data"
    for j, h in enumerate(cols, 1):
        c = ws.cell(1, j, h); c.font = f_h; c.fill = HEAD
    for i, r in enumerate(rows, 2):
        for j, h in enumerate(cols, 1):
            v = r[h]
            if h in num and str(v).strip():
                try: v = float(v)
                except ValueError: pass
            c = ws.cell(i, j, v if str(v).strip() else None)
            c.font = f_b
            if h in num: c.alignment = CEN
    for j, h in enumerate(cols, 1):
        ws.column_dimensions[chr(64 + j)].width = max(11, min(20, len(h) + 4))
    ws.freeze_panes = "A2"
    wb.save(path)
    return len(rows), cols


def build(qno, spec):
    ds = spec["ds"]
    path = f"{OUT}/q{int(qno):03d}.xlsx"
    n, cols = write_data(path, ds, spec.get("years") or None,
                         spec.get("crop"), spec.get("unit_bu", False))

    vf = spec.get("valfield") or VALFIELD[ds]
    values = [{"field": vf, "agg": a.lower(),
               "name": f"{a} of {vf}", "num_format": AGGFMT.get(a, "0.00")}
              for a in spec.get("aggs", ["Average"])]

    # the spec omits empty keys so it diffs cleanly; default them here
    rows = [r for r in spec.get("rows", []) if r in cols]
    kcols = [c for c in spec.get("cols", []) if c in cols]
    filters = [f for f in spec.get("filters", []) if f in cols and f not in rows + kcols]
    if not rows and not kcols:
        rows = [c for c in cols if c not in NUMCOL[ds]][:1]

    add_pivot_table(path, source_sheet="Data", dest_sheet="PivotTable",
                    rows=rows, cols=kcols, values=values, filters=filters,
                    output_path=path)

    wb = load_workbook(path)
    ws = wb["PivotTable"]
    ws.insert_rows(1)
    lab = f"Q{qno} — {' × '.join(rows + kcols)}"
    if spec.get("crop"): lab += f" — {spec['crop']} only"
    if spec.get("years"): lab += f" ({', '.join(spec['years'])})"
    c = ws.cell(1, 1, lab + (
                      f"{' (filter: ' + ', '.join(filters) + ')' if filters else ''}"))
    c.font = f_t
    wb.save(path)
    return path, n, rows, kcols, filters, spec.get("aggs", ["Average"])


if __name__ == "__main__":
    spec = json.load(open(os.path.join(os.path.dirname(__file__), "pivot_spec.json")))
    todo = {k: v for k, v in spec.items() if not v.get("skip")}
    print("  building %d pivot answer workbooks\n" % len(todo))
    for q in sorted(todo, key=int):
        p, n, r, c, f, a = build(q, todo[q])
        print("   q%-4s %-8s rows=%-14s cols=%-8s filt=%-10s %s (%d src rows)"
              % (q, todo[q]["ds"], ",".join(r)[:14], ",".join(c)[:8],
                 ",".join(f)[:10], "+".join(a), n))
