#!/usr/bin/env python3
"""Build mod01_references.xlsx — the Module 1 worksheet for relative vs absolute
cell references.

The concept is about what happens when a formula is COPIED, so every block pairs a
live formula with a FORMULATEXT column: the reader watches which part of a reference
moves and which part stays locked.

Run:  python3 textbook_examples/build_mod01_references.py
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side

# --- palette (matches the other Module 1 teaching workbooks) ----------------
PRAIRIE = "4A7C59"   # header fill
PALE    = "EEF4EF"   # section banner fill
INK     = "24302A"   # body text
MUTED   = "5C6B62"   # notes
WHEAT   = "B7973F"   # the "locked assumption" cell
FORMULA = "2F5D46"   # the FORMULATEXT column

# FORMULATEXT is an Excel-2013 function: openpyxl must write the _xlfn. prefix
# or Excel shows #NAME?.
FT = "_xlfn.FORMULATEXT"

head_fill = PatternFill("solid", fgColor=PRAIRIE)
band_fill = PatternFill("solid", fgColor=PALE)
lock_fill = PatternFill("solid", fgColor="F6EFD9")     # pale wheat

f_title = Font(name="Arial", size=14, bold=True, color=PRAIRIE)
f_sub   = Font(name="Arial", size=10, color=MUTED)
f_head  = Font(name="Arial", size=11, bold=True, color="FFFFFF")
f_band  = Font(name="Arial", size=10, bold=True, color=INK)
f_body  = Font(name="Arial", size=10, color=INK)
f_bold  = Font(name="Arial", size=10, bold=True, color=INK)
f_note  = Font(name="Arial", size=10, color=MUTED)
f_form  = Font(name="Consolas", size=10, color=FORMULA)
f_formsm= Font(name="Consolas", size=9, color=FORMULA)

centre = Alignment(horizontal="center")
left   = Alignment(horizontal="left")

wb = Workbook()
ws = wb.active
ws.title = "References"

# Track every row we write to, so we can set heights at the end.
touched = set()


def put(r, c, value, font=f_body, fill=None, fmt=None, align=None):
    cell = ws.cell(r, c, value)
    cell.font = font
    if fill:  cell.fill = fill
    if fmt:   cell.number_format = fmt
    if align: cell.alignment = align
    touched.add(r)
    return cell


def banner(r, text, width=6):
    for c in range(1, width + 1):
        ws.cell(r, c).fill = band_fill
    put(r, 1, text, font=f_band, fill=band_fill)


def header(r, labels):
    for i, lab in enumerate(labels, start=1):
        put(r, i, lab, font=f_head, fill=head_fill,
            align=left if i in (1, len(labels)) else centre)


def prose(r, text, width=6):
    put(r, 1, text, font=f_sub)
    ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=width)


# =========================================================================
# Title
# =========================================================================
put(1, 1, "Relative and Absolute References").font = f_title
prose(2, "A reference like B6 MOVES when you copy a formula. Put a $ in front of a "
         "column letter or row number and that part stays put. Column D shows the "
         "formula that produced column C, so you can watch which parts move.")

# =========================================================================
# Block 1 — the assumption cell
# =========================================================================
banner(4, "1 · Put an assumption in one labelled cell")
LOCK_ROW = 5
put(LOCK_ROW, 1, "Tonnes per bushel (wheat)", font=f_bold)
put(LOCK_ROW, 2, 0.027216, font=f_bold, fill=lock_fill, fmt="0.00000", align=centre)
put(LOCK_ROW, 3, "← every formula below points at this one cell", font=f_note)

# =========================================================================
# Block 2 — a relative reference works fine
# =========================================================================
banner(7, "2 · A relative reference is usually what you want")
header(8, ["Load", "Bushels", "Tonnes", "The formula in C", "What happened"])
B2_FIRST = 9
loads = [("Load A", 500), ("Load B", 1000), ("Load C", 2500), ("Load D", 5000)]
for i, (name, bu) in enumerate(loads):
    r = B2_FIRST + i
    put(r, 1, name)
    put(r, 2, bu, fmt="#,##0", align=centre)
    put(r, 3, f"=B{r}*0.027216", fmt="#,##0.0", align=centre)
    put(r, 4, f"={FT}(C{r})", font=f_form)
put(B2_FIRST, 5, "B9 → B10 → B11 → B12: the reference", font=f_note)
put(B2_FIRST + 1, 5, "moves down with the formula, which", font=f_note)
put(B2_FIRST + 2, 5, "is exactly what we want here.", font=f_note)

# =========================================================================
# Block 3 — the failure: the factor reference drifts
# =========================================================================
# The formula in C uses a RELATIVE reference to the factor cell (B5). Copied
# down, it drifts B5 -> B6 -> B7 -> B8, landing on cells that fail in three
# visibly different ways. Those landing cells are asserted below.
banner(15, "3 · The same formula, but pointing at the factor cell — and it breaks")
header(16, ["Load", "Bushels", "Tonnes — BROKEN", "The formula in C", "What went wrong"])
B3_FIRST = 17
# The first row of this block points at the factor cell RELATIVELY, so copying
# down walks the reference forward one row at a time. We choose the starting
# target so the drift lands on: the factor (correct), an empty cell (silent 0),
# the block's own header text (#VALUE!), and finally a BUSHELS number — the
# plausible-but-badly-wrong case that is the whole point of this block.
DRIFT_START = LOCK_ROW               # B5 = the factor
drift_notes = [
    "Correct — B5 really does hold the factor.",
    "B6 is empty → 0 tonnes. No error at all.",
    "B7 is empty too → 0 tonnes.",
    "B8 is the word 'Bushels' → #VALUE!",
]
for i, (name, bu) in enumerate(loads):
    r = B3_FIRST + i
    drift_target = DRIFT_START + i
    put(r, 1, name)
    put(r, 2, bu, fmt="#,##0", align=centre)
    put(r, 3, f"=B{r}*B{drift_target}", fmt="#,##0.0", align=centre)
    put(r, 4, f"={FT}(C{r})", font=f_form)
    put(r, 5, drift_notes[i], font=f_note)

# A fifth row, to show the worst case: the reference reaches a NUMBER that is
# not a factor, so the result looks like a real tonnage but is wildly wrong.
r = B3_FIRST + len(loads)
put(r, 1, "Load E")
put(r, 2, 8000, fmt="#,##0", align=centre)
put(r, 3, f"=B{r}*B{DRIFT_START + len(loads)}", fmt="#,##0.0", align=centre)
put(r, 4, f"={FT}(C{r})", font=f_form)
put(r, 5, f"B{DRIFT_START+len(loads)} is BUSHELS, not a factor —", font=f_note)
put(r + 1, 5, "a number, so no error. Wrong by ~18,000×.", font=f_note)

# Assert the drift lands where the notes claim. If a row is ever inserted above,
# this fails loudly instead of quietly teaching the wrong thing.
assert ws.cell(LOCK_ROW, 2).value == 0.027216,          "factor cell moved"
assert ws.cell(DRIFT_START + 1, 2).value is None,       "expected an empty cell"
assert ws.cell(DRIFT_START + 2, 2).value is None,       "expected an empty cell"
assert ws.cell(DRIFT_START + 3, 2).value == "Bushels",  "expected the header text"
assert isinstance(ws.cell(DRIFT_START + 4, 2).value, int), "expected a bushels number"

# =========================================================================
# Block 4 — the fix
# =========================================================================
banner(23, "4 · Lock the factor with $ — =B24*$B$5")
header(24, ["Load", "Bushels", "Tonnes — FIXED", "The formula in C", "Note"])
B4_FIRST = 25
for i, (name, bu) in enumerate(loads):
    r = B4_FIRST + i
    put(r, 1, name)
    put(r, 2, bu, fmt="#,##0", align=centre)
    put(r, 3, f"=B{r}*$B${LOCK_ROW}", fmt="#,##0.0", align=centre)
    put(r, 4, f"={FT}(C{r})", font=f_form)
put(B4_FIRST, 5, "$B$5 never moves, however far you", font=f_note)
put(B4_FIRST + 1, 5, "copy. Type B5 then press F4 (Win)", font=f_note)
put(B4_FIRST + 2, 5, "or ⌘T (Mac) to add the $ signs.", font=f_note)

# =========================================================================
# Block 5 — the 4x4 grid: why MIXED references exist
# =========================================================================
banner(31, "5 · Copy across AND down — where $A5 and B$4 earn their keep")
prose(32, "Bushels to tonnes for four crops. ONE formula, =$A35*B$34, copied across and "
          "down. It must find its quantity to the LEFT (column A) and its factor ABOVE "
          "(row 34) — so each needs a different half locked.")

CROP_ROW = 34                                    # the factor row
QTY_COL  = 1                                     # the quantity column
crops   = [("Wheat", 0.027216), ("Barley", 0.021772),
           ("Oats", 0.017237), ("Canola", 0.022680)]
qtys    = [500, 1000, 2500, 5000]

put(CROP_ROW, 1, "bu ↓   crop →", font=f_bold, align=centre)
for j, (crop, fac) in enumerate(crops):
    put(CROP_ROW - 1, 2 + j, crop, font=f_head, fill=head_fill, align=centre)
    put(CROP_ROW, 2 + j, fac, font=f_bold, fill=lock_fill, fmt="0.00000", align=centre)

GRID_FIRST = CROP_ROW + 1
for i, q in enumerate(qtys):
    r = GRID_FIRST + i
    put(r, 1, q, font=f_bold, fill=lock_fill, fmt="#,##0", align=centre)
    for j in range(len(crops)):
        c = 2 + j
        put(r, c, f"=$A{r}*{chr(65+c-1)}${CROP_ROW}", fmt="#,##0.0", align=centre)

# mirror grid: the same formulas as text, so the $ pattern is visible at once
MIRROR_FIRST = GRID_FIRST + len(qtys) + 2
prose(MIRROR_FIRST - 1, "The same cells, showing their formulas. Read ACROSS: $A stays, "
      "the column letter moves. Read DOWN: $34 stays, the row number moves.")
for i in range(len(qtys)):
    r = MIRROR_FIRST + i
    for j in range(len(crops)):
        c = 2 + j
        put(r, c, f"={FT}({chr(65+c-1)}{GRID_FIRST+i})", font=f_formsm, align=centre)
    put(r, 1, f"row {GRID_FIRST+i}", font=f_note, align=centre)

# the two wrong lockings
WRONG = MIRROR_FIRST + len(qtys) + 1
banner(WRONG, "What the wrong lockings do")
put(WRONG + 1, 1, "All relative", font=f_bold)
put(WRONG + 1, 2, f"=A{GRID_FIRST}*B{CROP_ROW}", fmt="#,##0.0", align=centre)
put(WRONG + 1, 3, f"={FT}(B{WRONG+1})", font=f_form)
put(WRONG + 1, 5, "Wanders diagonally off the table when copied.", font=f_note)
put(WRONG + 2, 1, "All absolute", font=f_bold)
put(WRONG + 2, 2, f"=$A${GRID_FIRST}*$B${CROP_ROW}", fmt="#,##0.0", align=centre)
put(WRONG + 2, 3, f"={FT}(B{WRONG+2})", font=f_form)
put(WRONG + 2, 5, "Every cell returns the same number — nothing moves.", font=f_note)

# =========================================================================
# Block 6 — the four forms, as a reference card
# =========================================================================
CARD = WRONG + 4
banner(CARD, "6 · The four forms")
header(CARD + 1, ["Form", "What is locked", "Copied down", "Copied across", "Use it when"])
forms = [
    ("B5",     "nothing",        "row changes", "column changes",
     "each row does its own arithmetic"),
    ("$B$5",   "column and row", "no change",   "no change",
     "one assumption cell — a rate, a price"),
    ("B$5",    "the row",        "no change",   "column changes",
     "a header ROW of factors above a grid"),
    ("$B5",    "the column",     "row changes", "no change",
     "a header COLUMN of values beside a grid"),
]
for i, (form, locked, down, across, use) in enumerate(forms):
    r = CARD + 2 + i
    put(r, 1, form, font=f_form, align=centre)
    put(r, 2, locked, font=f_note)
    put(r, 3, down,   font=f_note, align=centre)
    put(r, 4, across, font=f_note, align=centre)
    put(r, 5, use,    font=f_note)

# =========================================================================
# Layout
# =========================================================================
for col, w in [("A", 22), ("B", 15), ("C", 18), ("D", 24), ("E", 40), ("F", 12)]:
    ws.column_dimensions[col].width = w

# The embed viewer clips text in short rows: set an explicit height everywhere.
for r in range(1, CARD + 8):
    ws.row_dimensions[r].height = 18

ws.freeze_panes = "A4"
ws.sheet_view.showGridLines = True     # headers/gridlines stay ON for this sheet

out = "textbook_examples/mod01_references.xlsx"
wb.save(out)
print(f"wrote {out}")
print(f"  factor cell B{LOCK_ROW}; broken block starts row {B3_FIRST}; "
      f"grid at row {GRID_FIRST}; card at row {CARD}")
