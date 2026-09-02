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
from openpyxl.chart import BarChart, LineChart, Reference
from openpyxl.styles import Font, PatternFill, Alignment

DATA, OUT = "practice/data", "practice/answers"
FILES = {"rm_long": "rm_yields_1990_2025.csv",
         "mb":      "mb_wheat_varieties.csv",
         "sc":      "statcan_field_crops.csv"}
NUMCOL = {"rm_long": {"Yield"},
          "mb":      {"Farms", "Acres", "Yield_bu_ac"},
          "sc":      {"Seeded_acres", "Yield_bu_ac"}}
VALFIELD = {"rm_long": "Yield", "mb": "Yield_bu_ac", "sc": "Yield_bu_ac"}
AGGFMT = {"Average": "0.00", "Count": "#,##0", "Sum": "#,##0", "Min": "0.00"}

HEAD = PatternFill("solid", fgColor="4A7C59")
f_h = Font(name="Arial", size=10, bold=True, color="FFFFFF")
f_b = Font(name="Arial", size=10, color="24302A")
f_t = Font(name="Arial", size=12, bold=True, color="4A7C59")
CEN = Alignment(horizontal="center")


def write_data(path, ds, years=None, crop=None, unit_bu=False,
               varieties=None, min_variety_count=None,
               sort_varieties_by_average=False, nonblank_field=None):
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
    if nonblank_field:
        rows = [r for r in rows if str(r.get(nonblank_field, "")).strip()]
    if varieties:
        keep = set(varieties)
        rows = [r for r in rows if r.get("Variety") in keep]
    if min_variety_count:
        counts = {}
        for r in rows:
            if str(r.get("Yield_bu_ac", "")).strip():
                v = r.get("Variety")
                counts[v] = counts.get(v, 0) + 1
        keep = {v for v, count in counts.items() if count >= min_variety_count}
        rows = [r for r in rows if r.get("Variety") in keep]
    if sort_varieties_by_average:
        totals, counts = {}, {}
        for r in rows:
            value = str(r.get("Yield_bu_ac", "")).strip()
            if value:
                v = r.get("Variety")
                totals[v] = totals.get(v, 0.0) + float(value)
                counts[v] = counts.get(v, 0) + 1
        averages = {v: totals[v] / counts[v] for v in totals}
        rows.sort(key=lambda r: -averages.get(r.get("Variety"), float("-inf")))
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
    n, cols = write_data(
        path, ds, spec.get("years") or None, spec.get("crop"),
        spec.get("unit_bu", False), spec.get("varieties"),
        spec.get("min_variety_count"),
        spec.get("sort_varieties_by_average", False),
        spec.get("nonblank_field")
    )

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

    chart_type = spec.get("chart")
    if chart_type:
        # A pivot with multiple value fields inserts an extra "Values" row, so
        # locate the real row-label header instead of assuming it is row 3.
        header_row = next(
            row for row in range(2, ws.max_row + 1)
            if ws.cell(row, 1).value in {"Row Labels", rows[0]}
            and ws.cell(row, 2).value is not None
        )
        last_row = ws.max_row
        for row in range(header_row + 1, ws.max_row + 1):
            if ws.cell(row, 1).value == "Grand Total":
                last_row = row - 1
                break

        # Use a small hidden chart source.  It keeps the displayed PivotTable
        # live while allowing the ranked bar chart to be ordered by its value.
        chart_rows = [
            (ws.cell(row, 1).value, ws.cell(row, 2).value)
            for row in range(header_row + 1, last_row + 1)
        ]
        if chart_type == "bar" and spec.get("sort_varieties_by_average"):
            chart_rows.sort(key=lambda pair: pair[1], reverse=True)
        chart_ws = wb.create_sheet("_ChartData")
        chart_ws.sheet_state = "hidden"
        chart_ws.append([ws.cell(header_row, 1).value,
                         ws.cell(header_row, 2).value])
        for pair in chart_rows:
            chart_ws.append(pair)

        chart = LineChart() if chart_type == "line" else BarChart()
        if chart_type == "bar":
            chart.type = "bar"
            chart.style = 10
        data = Reference(chart_ws, min_col=2, min_row=1,
                         max_row=len(chart_rows) + 1)
        cats = Reference(chart_ws, min_col=1, min_row=2,
                         max_row=len(chart_rows) + 1)
        chart.add_data(data, titles_from_data=True)
        chart.set_categories(cats)
        chart.title = spec.get("chart_title", "PivotChart")
        if chart_type == "bar":
            # In openpyxl's horizontal bar chart, x_axis is the category
            # (vertical) axis and y_axis is the value (horizontal) axis.
            chart.x_axis.title = spec.get("y_axis_title", "")
            chart.y_axis.title = spec.get("x_axis_title", "")
        else:
            chart.x_axis.title = spec.get("x_axis_title", "")
            chart.y_axis.title = spec.get("y_axis_title", "")
        chart.legend = None
        chart.height = 9
        chart.width = 16
        ws.add_chart(chart, "E3")
    wb.save(path)
    return path, n, rows, kcols, filters, spec.get("aggs", ["Average"])


if __name__ == "__main__":
    spec = json.load(open(os.path.join(os.path.dirname(__file__), "pivot_spec.json")))
    requested = set(sys.argv[1:])
    todo = {k: v for k, v in spec.items()
            if not v.get("skip") and (not requested or k in requested)}
    print("  building %d pivot answer workbooks\n" % len(todo))
    for q in sorted(todo, key=int):
        p, n, r, c, f, a = build(q, todo[q])
        print("   q%-4s %-8s rows=%-14s cols=%-8s filt=%-10s %s (%d src rows)"
              % (q, todo[q]["ds"], ",".join(r)[:14], ",".join(c)[:8],
                 ",".join(f)[:10], "+".join(a), n))
