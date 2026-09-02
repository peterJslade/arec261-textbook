# Module 1 answer-workbook check — Questions 21-25

Checked against `practice/module01_bank.qmd` (Section 3, Conditional Functions & Lookups, Saskatchewan RM Crop Yields). Workbooks opened read-only with openpyxl (formulas, fills, number formats, merges, row heights) plus raw XML inspection of the sheet parts; expected values recomputed independently from `practice/data/rm_yields_1990plus.csv` in Python. No files were modified.

Mapping: Q21 = `q043.xlsx`, Q22 = `q044.xlsx`, Q23 = `q047.xlsx`, Q24 = `q048.xlsx`, Q25 = `q050.xlsx`.

**Data-sheet verification passed for all five.** Each holds the full source dataset: header row plus 10,649 data rows (A2:J10650), matching the CSV cell-for-cell in the original row order. All 106,490 value cells were compared against the CSV in every workbook; zero mismatches. Blank CSV cells are genuinely empty cells rather than zeros or empty strings, which matters for the `IF(E2="","",...)` label in Q24 and for `AVERAGEIF`/`COUNTIF` blank-skipping throughout — all of it behaves correctly. `q048.xlsx` carries the extra label column K (`Canola label (a)`) as described.

None of the five store cached formula results (every `<v>` is empty), but all five set `fullCalcOnLoad="1"`, so Excel and the web viewer recalculate on open. Every figure quoted in the written notes was checked against recomputation.

Common formatting: column A width 36, B:G width 13, notes merged across A:F with `wrap_text` and a 64-point row height, legend block at the bottom. Consistent with Q11-20.

---

## Question 21 — q043.xlsx: OK

- Both lookups correct. B1 `=_xlfn.XLOOKUP(1&"|"&2023,Data!$B$2:$B$10650&"|"&Data!$A$2:$A$10650,Data!$E$2:$E$10650)` -> canola, RM 1, 2023 = **36.8**. B2 the same shape against `$C` (Spring Wheat) with key `100&"|"&2023` -> **52.9**. Recomputed from the CSV: RM 1 / 2023 canola is exactly 36.8, RM 100 / 2023 spring wheat is exactly 52.9. Both are unique single rows, as the question assumes.
- The concatenated-key construction is the right pattern for the question, and the `"|"` separator is the right defensive choice — without it, `1&2023` and `12&023` style collisions are possible in principle. Good that the model answer shows the separator rather than a bare `&`.
- Lookup arrays span `$2:$10650` on both the key components and the return column, and the three ranges are the same length. Absolute references throughout.
- The `_xlfn.XLOOKUP` prefix is correct openpyxl encoding, and the formula is stored as a plain `<f>` (not a legacy CSE array formula). In current Excel the range concatenation evaluates as an implicit dynamic array and returns the scalar correctly. Flagging only so it is on record: in a pre-dynamic-array Excel this would need Ctrl+Shift+Enter. Not a problem for the course's target version, and not worth changing.
- Part (c) note is correct and well aimed: "an RM number alone matches 36 different rows". Verified — RM 1 appears in exactly 36 rows and the dataset spans exactly 36 distinct years (1990-2025). The claim that a single-criterion `XLOOKUP` returns whichever row it hits first is accurate for default (first-match) mode.
- Number format `0.0` on B1:B2 displays 36.8 and 52.9 exactly; no rounding loss.
- Colour-coding and legend coherent: yellow (a) on B1, green (b) on B2, blue (c) on the merged note; legend A7:A9 lists (a)-(c) in matching fills. Every legend colour is used exactly once on the sheet.

## Question 22 — q044.xlsx: OK

- B1 `=COUNTIFS(Data!$E$2:$E$10650,">40",Data!$C$2:$C$10650,">45")` -> **1,204**. B2 `=COUNTIF(Data!$E$2:$E$10650,">40")` -> **1,483**. Both recomputed from the CSV and both match. Correct columns (E = Canola, C = Spring Wheat), correct criteria, matching range lengths.
- Part (c) note is correct on all three of its numbers: 1,204, 1,483, and the 279-row difference (1483 - 1204 = 279). The stated reason — that the (a) set is a subset of the (b) set because (a) adds a condition to the same rows — is the right explanation and is stated without hand-waving.
- The "279 rows grew canola above 40 without wheat above 45" phrasing is worth a second's thought and survives it: those 279 rows have canola > 40 and *fail* wheat > 45, which includes rows where spring wheat is blank. Verified that the arithmetic identity holds regardless, since `COUNTIFS` treats a blank wheat cell as failing `">45"`. The sentence is accurate as written.
- Number format `0` on both counts is right for integers.
- Colour-coding and legend coherent: yellow (a), green (b), blue (c) on the note; legend A7:A9 matches, each colour used once.

## Question 23 — q047.xlsx: legend advertises a part (b) colour that appears nowhere on the sheet

- **Legend lists three colours but the sheet uses only two.** Expected: each legend entry maps to at least one filled cell. Found: legend A10 yellow = Part (a), A11 green = Part (b), A12 blue = Part (c) — but green `00D9EAD3` is used on *no cell* in the sheet. The four `AVERAGEIF` cells B2:C3 are all yellow and are labelled `Average 2015 (a/b)` / `Average 2019 (a/b)`, collapsing parts (a) and (b) into one colour. A student reading the legend will look for the green part-(b) cells and not find them. Either give the barley column (C2:C3, which *is* part b) the green fill and leave canola yellow — which is what the row labels imply the design intended — or drop the green entry from the legend. The first fix is better: part (b) is specifically the barley calculation, and colouring it makes the sheet self-explanatory.
- Everything else is correct. All four `AVERAGEIF` formulas use the right shape, `=AVERAGEIF(Data!$A$2:$A$10650,<year>,Data!$E$ or $F$...)`, with E = Canola and F = Barley, criteria ranges and average ranges the same length. Recomputed: canola 2015 = 36.0602 (n=291), canola 2019 = 40.7831 (n=290), barley 2015 = 55.2499 (n=288), barley 2019 = 68.5910 (n=288). `AVERAGEIF` skips blanks, which is what these n's reflect.
- Derived cells correct: B4 `=B3-B2` -> 4.7229, C4 `=C3-C2` -> 13.3411, B5 `=(B3-B2)/B2` -> 13.10%, C5 `=(C3-C2)/C2` -> 24.15%.
- Part (c) note's numbers all check: "Canola rose 4.7 bu/ac (13%); barley rose 13.3 bu/ac (24%)". Exact values 4.72 / 13.10% and 13.34 / 24.15%. The conclusion — barley grew more on both measures — is right, and the note is explicit that it holds on *both* measures, which is the point of asking for absolute and percentage side by side.
- Number formats sensible: `0.00` on levels and absolute change, `0.0%` on percentage change.
- Minor: canola's n differs between the two years (291 in 2015, 290 in 2019) while barley's is 288 in both. Nothing on the sheet signals that the two years cover slightly different RM sets. Not an error — the question asks for the average of what is there — but the same observation was made about Q12, and a one-line note would pre-empt a student who counts rows.

## Question 24 — q048.xlsx: OK

- Part (a) is implemented as a real filled-down formula column on the Data sheet, not just described. K2 `=IF(E2="","",IF(E2<20,"Low",IF(E2<=40,"Medium","High")))`, filled to K10650, with header `Canola label (a)` in K1. Spot-checked K2, K3, K4 and K10650 — all correctly relative-referenced to their own row.
- The boundary handling matches the question exactly: below 20 = Low, 20 to 40 inclusive = Medium (`E2<=40`), above 40 = High. Blanks return `""` and are excluded from all three counts, which is the "leaving blanks blank" the question asks for. Verified that the 610 blank-canola rows are genuinely empty cells, so the `E2=""` test fires correctly on them.
- Part (b) counts correct: B2/C2/D2 `=COUNTIF(Data!$K$2:$K$10650,"Low"/"Medium"/"High")` -> **2,037 / 6,519 / 1,483**. Recomputed from the CSV and all three match; they sum to 10,039 labelled rows out of 10,649, leaving exactly the 610 blanks.
- Part (c) counts correct: B3/C3/D3 `=COUNTIFS(Data!$A$2:$A$10650,2023,Data!$K$2:$K$10650,"Low"/"Medium"/"High")` -> **57 / 118 / 114**. Recomputed and matching; they sum to 289 of the 295 rows dated 2023, leaving 6 blanks.
- Part (d) note's figures are all correct: "about 15% of RM-years are High (1,483 of 10,039)" — exact 14.77%; "in 2023 the High share is 39% (114 of 289)" — exact 39.45%; "Low stays near 20%" — 20.29% overall against 19.72% in 2023, so the claim that Low is essentially unchanged is right. The conclusion that 2023 was strong specifically at the top end, with the shift coming out of Medium rather than out of Low, is the correct reading and is a genuinely useful thing to point out.
- Note that the note computes shares against *labelled* rows (10,039 and 289), not against all rows. That is the right denominator given blanks are excluded, and the note says "labelled rows" explicitly. Good.
- Colour-coding and legend coherent, and better than the other four: yellow (a) fills the whole K column on the Data sheet *and* the A5 note, so the legend's part-(a) entry maps to something visible in both places; green (b) on row 2, blue (c) on row 3, red (d) on the A6 note. Legend A9:A12 lists all four in matching fills, each used.
- Minor: neither Data sheet has frozen panes, so scrolling column K on a 10,650-row sheet loses the header. Applies to all five workbooks equally; cosmetic.

## Question 25 — q050.xlsx: legend advertises a part (c) colour that appears nowhere on the sheet

- **Same legend defect as Q23, one row down.** Expected: each legend entry maps to a filled cell. Found: legend A8 yellow = (a), A9 green = (b), A10 blue = (c), A11 red = (d) — but blue `00CFE2F3` is used on no cell. Parts (b) and (c) are the two cells B3 and C3 on one row labelled `RMs below 20 (b/c)`, both green. Since (b) is the 2021 count and (c) is the 2023 count, the clean fix is green on B3 and blue on C3, which makes the legend true and the row self-documenting. Alternatively drop the blue entry.
- All formulas correct. B2/C2 `=AVERAGEIF(Data!$A$2:$A$10650,2021 or 2023,Data!$E$2:$E$10650)` -> **21.8583** and **33.8810**. B3/C3 `=COUNTIFS(Data!$A$2:$A$10650,2021 or 2023,Data!$E$2:$E$10650,"<20")` -> **120** and **57**. All four recomputed from the CSV and matching.
- Part (d) note's numbers are right: 120 versus 57, and "more than twice as many" (120/57 = 2.11). The substantive claim — that the average alone understates what happened, because the low tail thickened — is correct and is the point of the question.
- One wording flag, not a numeric error: the note says "**The drought** did not just lower the average". The question never mentions drought and the workbook never establishes one; the note introduces outside knowledge about 2021 as though the data showed it. It is true that 2021 was a drought year in Saskatchewan, but a model answer that a student is meant to imitate should either say why the data is consistent with a drought or say "2021" instead of "the drought". As written, a student learns to assert a cause from two counts. Suggest "2021 did not just lower the average" and, if the causal point is wanted, a separate clause naming it as outside context.
- Second wording flag, same sentence: "outright crop failure territory" for canola below 20 bu/ac is a stronger claim than the threshold supports — 20 bu/ac canola is a bad year, not a failure, and the 20 cut-off came from the question rather than from agronomy. Softening to "well below normal" would keep the point without the overstatement.
- Also minor: the row label reads `RMs below 20 (b/c)` but `COUNTIFS` counts *rows*, which here are RM-years. Within a single year one row is one RM, so "RMs" is accurate for this question. No change needed; noting only because the same label copied to a multi-year context would be wrong.
- Number formats sensible: `0.00` on the averages, `0` on the counts.

---

## Summary of issues, most serious first

1. **q047 (Q23)** — legend lists a part (b) green that no cell uses; parts (a) and (b) share yellow. Fix by colouring the barley column C2:C3 green.
2. **q050 (Q25)** — legend lists a part (c) blue that no cell uses; parts (b) and (c) share green. Fix by colouring C3 blue.
3. **q050 (Q25)** — part (d) note asserts "the drought" as the cause and calls sub-20 canola "outright crop failure territory". Both go beyond what the two counts show; reword.
4. **q047 (Q23)** — canola n differs between 2015 (291) and 2019 (290) with no note; harmless here, but the sheet gives no signal that the two years cover different RM sets.
5. **All five** — Data sheets have no frozen header row, so headers scroll away on a 10,650-row sheet. Cosmetic, and consistent across the whole bank.
6. **q043 (Q21)** — the array-concatenation `XLOOKUP` is stored as a non-array formula. Correct in current Excel with dynamic arrays; would need Ctrl+Shift+Enter in a pre-2021 build. Recorded, not a defect for this course.

All Data sheets, all formulas, all recomputed values, and every number quoted in the notes are correct. The issues above are presentation and wording, not arithmetic.
