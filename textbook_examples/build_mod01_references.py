#!/usr/bin/env python3
"""Build the three small Module 1 worksheets on cell references.

Each workbook makes ONE point and fits on screen in the 700px embed (no scrolling):

  mod01_ref_relative.xlsx  — a relative reference: everything moves together
  mod01_ref_absolute.xlsx  — one crop, one factor cell, locked with $B$4
  mod01_ref_multiple.xlsx  — three crops, factors in row 4, locked with C$4

Every sheet pairs a live formula with a FORMULATEXT column so the reader can see
which part of a reference moved and which part stayed put.

Run:  python3 textbook_examples/build_mod01_references.py
"""

from openpyxl import Workbook, load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

# --- palette (matches the other Module 1 teaching workbooks) ----------------
PRAIRIE = "4A7C59"   # header fill
PALE    = "EEF4EF"   # banner fill
INK     = "24302A"   # body text
MUTED   = "5C6B62"   # notes
FORMULA = "2F5D46"   # the FORMULATEXT column
LOCKFIL = "F6EFD9"   # pale wheat, for the locked factor cells

# FORMULATEXT is an Excel-2013 function: openpyxl must write the _xlfn. prefix
# or Excel renders #NAME?.
FT = "_xlfn.FORMULATEXT"

# bushel weights (lb/bu) / 2.20462 / 1000  ->  tonnes per bushel
WHEAT_F, BARLEY_F, OATS_F = 0.027216, 0.021772, 0.017237

head_fill = PatternFill("solid", fgColor=PRAIRIE)
lock_fill = PatternFill("solid", fgColor=LOCKFIL)

f_title = Font(name="Arial", size=14, bold=True, color=PRAIRIE)
f_sub   = Font(name="Arial", size=10, color=MUTED)
f_head  = Font(name="Arial", size=11, bold=True, color="FFFFFF")
f_body  = Font(name="Arial", size=10, color=INK)
f_bold  = Font(name="Arial", size=10, bold=True, color=INK)
f_note  = Font(name="Arial", size=10, color=MUTED)
f_form  = Font(name="Consolas", size=10, color=FORMULA)

centre = Alignment(horizontal="center")
left   = Alignment(horizontal="left")
wrap   = Alignment(horizontal="left", vertical="top", wrap_text=True)

LOADS = [500, 1000, 2500, 5000, 8000]


def new_sheet(title, subtitle, name, width=6):
    wb = Workbook()
    ws = wb.active
    ws.title = name
    ws.cell(1, 1, title).font = f_title
    c = ws.cell(2, 1, subtitle); c.font = f_sub; c.alignment = wrap
    ws.merge_cells(start_row=2, start_column=1, end_row=2, end_column=width)
    ws.row_dimensions[2].height = 30
    return wb, ws


def put(ws, r, c, v, font=f_body, fill=None, fmt=None, align=None):
    cell = ws.cell(r, c, v)
    cell.font = font
    if fill:  cell.fill = fill
    if fmt:   cell.number_format = fmt
    if align: cell.alignment = align
    return cell


def header(ws, r, labels):
    for i, lab in enumerate(labels, start=1):
        put(ws, r, i, lab, font=f_head, fill=head_fill,
            align=left if i == 1 else centre)


def footnote(ws, r, text, width):
    c = put(ws, r, 1, text, font=f_note)
    c.alignment = wrap
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=width)
    ws.row_dimensions[r].height = 32


def finish(ws, widths, last_row, freeze):
    for col, w in widths:
        ws.column_dimensions[col].width = w
    for r in range(1, last_row + 2):
        if ws.row_dimensions[r].height is None:
            ws.row_dimensions[r].height = 18
    ws.freeze_panes = freeze
    ws.sheet_view.showGridLines = True   # headers/gridlines ON: the reader needs
                                         # to see which cell is which


# ==========================================================================
# 1 — RELATIVE: every part of the reference moves
# ==========================================================================
wb, ws = new_sheet(
    "Relative references",
    "The formula in column D multiplies the two cells beside it. Copy it down and "
    "BOTH references move with it — row 5 uses row 5, row 6 uses row 6.",
    "Relative", width=5)

header(ws, 4, ["Load", "Bushels", "Price ($/bu)", "Value ($)", "The formula in D"])
FIRST = 5
prices = [7.50, 7.50, 8.10, 8.10, 7.95]
for i, bu in enumerate(LOADS):
    r = FIRST + i
    put(ws, r, 1, f"Load {chr(65+i)}")
    put(ws, r, 2, bu, fmt="#,##0", align=centre)
    put(ws, r, 3, prices[i], fmt='"$"#,##0.00', align=centre)
    put(ws, r, 4, f"=B{r}*C{r}", fmt='"$"#,##0', align=centre)
    put(ws, r, 5, f"={FT}(D{r})", font=f_form)
LAST = FIRST + len(LOADS) - 1

footnote(ws, LAST + 2,
         "Read column E downwards: B5*C5, then B6*C6, then B7*C7. Both references "
         "step down one row at a time — each load uses its own bushels and its own "
         "price. This is what a reference does if you leave it alone.", 5)

finish(ws, [("A", 12), ("B", 12), ("C", 14), ("D", 12), ("E", 26)], LAST + 2, "A5")
wb.save("textbook_examples/mod01_ref_relative.xlsx")
print("wrote mod01_ref_relative.xlsx")

# ==========================================================================
# 2 — ABSOLUTE, one crop: one factor cell, locked with $B$4
# ==========================================================================
wb, ws = new_sheet(
    "Absolute references — one crop",
    "Here the conversion factor lives in ONE cell (B4). Every formula has to point "
    "at that same cell, so we lock it with dollar signs: $B$4.",
    "Absolute", width=4)

FACTOR_ROW = 4
put(ws, FACTOR_ROW, 1, "Tonnes per bushel (wheat)", font=f_bold)
put(ws, FACTOR_ROW, 2, WHEAT_F, font=f_bold, fill=lock_fill, fmt="0.00000", align=centre)
put(ws, FACTOR_ROW, 3, "← every formula points here", font=f_note)

header(ws, 6, ["Load", "Bushels", "Tonnes", "The formula in C"])
FIRST = 7
for i, bu in enumerate(LOADS):
    r = FIRST + i
    put(ws, r, 1, f"Load {chr(65+i)}")
    put(ws, r, 2, bu, fmt="#,##0", align=centre)
    put(ws, r, 3, f"=B{r}*$B${FACTOR_ROW}", fmt="#,##0.0", align=centre)
    put(ws, r, 4, f"={FT}(C{r})", font=f_form)
LAST = FIRST + len(LOADS) - 1

footnote(ws, LAST + 2,
         "Read column D downwards: the B7 part steps down to B8, B9 … but $B$4 never "
         "changes. Without the dollar signs it would drift to B5, B6, B7 and the "
         "answers would be wrong. Type B4 and press F4 (Windows) or ⌘T (Mac) to add "
         "the dollar signs.", 4)

finish(ws, [("A", 24), ("B", 12), ("C", 12), ("D", 24)], LAST + 2, "A7")
wb.save("textbook_examples/mod01_ref_absolute.xlsx")
print("wrote mod01_ref_absolute.xlsx")

# ==========================================================================
# 3 — ABSOLUTE, several crops: factors along row 4, locked with C$4
# ==========================================================================
wb, ws = new_sheet(
    "Absolute references — several crops",
    "Each crop has its own factor, side by side in row 4. One formula fills all three "
    "columns: lock the ROW so it always looks up to row 4, but leave the column free "
    "so each column finds its own crop.",
    "Several crops", width=6)

FACTOR_ROW = 4
put(ws, FACTOR_ROW, 1, "Tonnes per bushel →", font=f_bold)
put(ws, FACTOR_ROW, 2, "", font=f_body)
for j, fac in enumerate([WHEAT_F, BARLEY_F, OATS_F]):
    put(ws, FACTOR_ROW, 3 + j, fac, font=f_bold, fill=lock_fill,
        fmt="0.00000", align=centre)

header(ws, 6, ["Load", "Bushels", "wheat_tons", "barley_tons", "oats_tons",
               "The formula in C"])
FIRST = 7
for i, bu in enumerate(LOADS):
    r = FIRST + i
    put(ws, r, 1, f"Load {chr(65+i)}")
    put(ws, r, 2, bu, fmt="#,##0", align=centre)
    for j in range(3):
        col = 3 + j
        letter = chr(64 + col)          # C, D, E
        put(ws, r, col, f"=$B{r}*{letter}${FACTOR_ROW}", fmt="#,##0.0", align=centre)
    put(ws, r, 6, f"={FT}(C{r})", font=f_form)
LAST = FIRST + len(LOADS) - 1

footnote(ws, LAST + 2,
         "The one formula is =$B7*C$4, filled across and down. $B keeps every column "
         "looking left to the bushels. C$4 keeps every row looking up to row 4 — and "
         "because the column letter is free, wheat reads C4, barley D4, oats E4.", 6)

finish(ws, [("A", 12), ("B", 11), ("C", 13), ("D", 13), ("E", 12), ("F", 22)],
       LAST + 2, "A7")
wb.save("textbook_examples/mod01_ref_multiple.xlsx")
print("wrote mod01_ref_multiple.xlsx")

# --- sanity checks ---------------------------------------------------------
print()
for f in ("mod01_ref_relative.xlsx", "mod01_ref_absolute.xlsx",
          "mod01_ref_multiple.xlsx"):
    s = load_workbook(f"textbook_examples/{f}").active
    bare = sum(1 for row in s.iter_rows() for c in row
               if isinstance(c.value, str) and "FORMULATEXT" in c.value
               and "_xlfn." not in c.value)
    pop = {c.row for row in s.iter_rows() for c in row if c.value is not None}
    missing = [r for r in pop if s.row_dimensions[r].height is None]
    print(f"  {f:28} {max(pop):2} rows  bare-FT={bare}  no-height={len(missing)}")
    assert bare == 0,        f"{f}: unprefixed FORMULATEXT"
    assert not missing,      f"{f}: rows without an explicit height"
    assert max(pop) <= 16,   f"{f}: {max(pop)} rows is too tall for the embed"
print("\nall three fit on screen in the 700px embed (~29 rows visible)")
