#!/usr/bin/env python3
"""Generate answer workbooks for Sections 2 and 3 (descriptive + conditional).

Each workbook carries the data extract the question works on, and an Answer tab
whose formulas point at it, so opening the file recomputes the answer key.
PivotTable questions are skipped -- openpyxl cannot create a real pivot.
"""
import json, sys, os
sys.path.insert(0, 'practice')
from build_answers import (load, book, data_tab, stat_block, note, widths,
                           heights, save, put, header, CORE, f_bold, f_form,
                           f_note, lock_fill, centre, FT, QI, PI, SD, VR)
from openpyxl.utils import get_column_letter

RM_COLS = ["Year","RM","Spring Wheat","Durum","Canola","Barley","Oats","Peas","Lentils","Flax"]
MB_COLS = ["Year","Municipality","Variety","Farms","Acres","Yield_bu_ac","Reported"]
SC_COLS = ["Year","Province","Crop","Seeded_acres","Yield_bu_ac"]

FILES = {"rm": ("rm_yields_1990plus.csv", RM_COLS, None),
         "mb": ("mb_wheat_varieties.csv", MB_COLS, "Yield_bu_ac"),
         "sc": ("statcan_field_crops.csv", SC_COLS, "Yield_bu_ac")}

CONDITIONAL = [
    ("Count of all values",      "=COUNT(@)",                    "#,##0"),
    ("Count above 40",           '=COUNTIF(@,">40")',            "#,##0"),
    ("Count 40 or below",        '=COUNTIF(@,"<=40")',           "#,##0"),
    ("Sum of those above 40",    '=SUMIF(@,">40")',              "#,##0.0"),
    ("Mean of those above 40",   '=AVERAGEIF(@,">40")',          "0.00"),
    ("Count above the mean",     '=COUNTIF(@,">"&AVERAGE(@))',   "#,##0"),
    ("Mean of all values",       "=AVERAGE(@)",                  "0.00"),
]


def build(qno, spec):
    ds = spec["ds"]
    fname, cols, default_col = FILES[ds]
    rows = load(fname)

    years = spec["years"]
    if years:
        rows = [r for r in rows if r["Year"] in years]
    yr_label = ", ".join(years) if years else "all years"

    # which column carries the numbers this question is about
    if ds == "rm":
        col = spec["crops"][0] if spec["crops"] else "Canola"
    else:
        col = default_col

    if not rows:
        return None

    title = f"Q{qno} — {col}, {yr_label}"
    sub = (f"The {yr_label} rows are on the **Data** tab. Every figure here is a live "
           f"formula pointing at the {col} column there, so the sheet recomputes "
           f"rather than repeating a number someone typed in.")
    wb, ws = book(title, sub)
    sheet, first, last = data_tab(wb, rows, cols, title)
    letter = get_column_letter(cols.index(col) + 1)

    items = CORE if spec["sec"] == 2 else CONDITIONAL
    put(ws, 4, 1, f"{col} — {yr_label}", font=f_bold)
    end = stat_block(ws, 5, sheet, letter, first, last, items)

    if spec["sec"] == 3:
        note(ws, end + 2,
             "The thresholds here are the ones the question uses; change the number "
             "inside the quotation marks to test a different one. Note the last row: "
             'to compare against a computed value you must join the operator on with '
             '&, because anything inside quotes is treated as literal text.', 4)
    else:
        note(ws, end + 2,
             "Blank cells are skipped by every one of these functions, so the count "
             "is the number of RMs that reported -- not the number of rows.", 4)

    widths(ws, [("A", 26), ("B", 14), ("C", 40), ("D", 4)])
    heights(ws, end + 3)
    return wb


if __name__ == "__main__":
    spec = json.load(open('/tmp/spec.json'))
    made = skipped = 0
    for qno, sp in sorted(spec.items(), key=lambda x: int(x[0])):
        if sp["pivot"]:
            skipped += 1
            continue
        wb = build(qno, sp)
        if wb is None:
            print("  !! no rows for Q%s" % qno); continue
        save(wb, int(qno)); made += 1
    print("  built %d workbooks, skipped %d pivot questions" % (made, skipped))
