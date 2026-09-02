# Module 1 answer-workbook check — Questions 11-15 (Saskatchewan RM Crop Yields)

Checked against `practice/module01_bank.qmd`; workbooks opened read-only with openpyxl (formulas + fills), Data sheets compared cell-by-cell against `practice/data/rm_yields_1990plus.csv`, expected statistics recomputed independently in Python using Excel conventions (sample SD, PERCENTILE.INC/QUARTILE.INC interpolation). No files were modified.

One global observation, not a defect: none of the five workbooks stores cached formula results (openpyxl-written), so every numeric claim below was verified by independent recomputation rather than by reading a stored value. Excel and Excel for the web recalculate on open, so students see the numbers.

## Question 11 — q011.xlsx: OK

- Data sheet: 289 values in A2:A290 exactly match the 289 non-blank 2023 Canola yields from the CSV, in file order. Header labelled.
- Part (a): `=AVERAGE(Data!$A$2:$A$290)` and `=MEDIAN(...)` over the full data range; recomputed mean 33.88, median 35.50 — the note's quoted 33.9 and 35.5 are right.
- Part (d): `=STDEV.S(...)` (sample SD, correct convention) and IQR as `QUARTILE.INC(...,3)-QUARTILE.INC(...,1)`; recomputed SD 13.33, IQR 22.30.
- Part (b) note: mean below median, longer left tail — correct direction. Part (c) note: median, "mean dragged 1.6 bushels below" — 35.50 − 33.88 = 1.62, correct.
- Colour-coding coherent: yellow (a), green (b), blue (c), red (d); legend A10:A13 matches the fills used.
- Nit (bank text, not the workbook): part (c) asks students to justify "using your answers to parts a-d", but (c) comes before (d). The answer's (c) note uses only the mean/median from (a)-(b) and never invokes the SD or IQR, which is defensible but not literally what the prompt asks. Consider reordering the bank's parts or changing "a-d" to "a-b".

## Question 12 — q012.xlsx: OK

- Data sheet: column A = 289 non-blank 2023 Canola values, column B = 285 non-blank 2023 Barley values, both matching the CSV in order. (Blanks are dropped, so the two columns are compacted to different lengths and rows no longer correspond to the same RM — harmless here since every part is per-column, and the notes make no cross-row claim.)
- Part (a): AVERAGE and STDEV.S with correct per-column ranges (A2:A290, B2:B286). Recomputed: canola 33.88 / 13.33; barley 54.56 / 24.60 — the note's 33.9, 13.3, 54.6, 24.6 all match.
- Part (b) note: "nearly twice" is right (24.60/13.33 = 1.85), and the scale argument is the intended answer.
- Parts (c)-(d): CV as `=B3/B2`, `=C3/C2`; recomputed 0.394 vs 0.451, so barley more variable relative to its average — note's 0.39 vs 0.45 and conclusion correct.
- Part (e) sentence quotes 45% and 39%, both correct and not misleading.
- All five parts answered; legend A11:A15 lists (a)-(e) in the matching fills.

## Question 13 — q013.xlsx: OK

- Data sheet: column A = 290 non-blank 2019 Canola values, column B = 290 non-blank 2021 values, both matching the CSV in order, headers "Canola 2019"/"Canola 2021".
- Part (a): AVERAGE/MEDIAN over A2:A291 and B2:B291. Recomputed: 2019 mean 40.78, median 42.10; 2021 mean 21.86, median 22.80.
- Part (b): STDEV.S and CV formulas correct. Recomputed SDs 8.17 vs 8.14 (note's "about 8.2" for both is fair), CVs 0.200 vs 0.373 — note's 0.20 vs 0.37 correct.
- Part (c) note picks 2021 on CV grounds with near-identical SDs — the intended reasoning, and the numbers support it.
- Wording nit: "2021's average is barely half of 2019's" — 21.86/40.78 = 54%, so it is slightly *more* than half. "About half" would be accurate; "barely half" faintly suggests under half. Trivial.
- Colours and legend (A10:A12) coherent for parts (a)-(c).

## Question 14 — q014.xlsx: OK

- Data sheet: 200 values in A2:A201 exactly match the 200 non-blank 2023 Oats yields (95 of 295 RMs report no oats; dropping blanks is correct).
- Part (a): AVERAGE, MEDIAN, `PERCENTILE.INC(...,0.9)` over the full range. Recomputed: mean 71.14, median 75.90, P90 116.72 — the notes' 71.1, 75.9, and "about 117" all match.
- Part (c): Q1/Q3 via QUARTILE.INC, IQR `=B5-B4`. Recomputed 44.98 / 96.50 / 51.53.
- Part (b) note ("ninety percent of RMs at or below about 117") is the right reading of PERCENTILE.INC. Strictly it is 90% of the 200 oat-reporting RMs, not all 295 — too pedantic to require a fix.
- Part (d) note: mean (71.1) below median (75.9), left-skewed — correct direction and correct numbers.
- Colours and legend (A12:A15) coherent for parts (a)-(d).

## Question 15 — q015.xlsx: OK

- Data sheet: 286 values in A2:A287 exactly match the 286 non-blank 2024 Spring Wheat yields, in order.
- Part (a): `PERCENTILE.INC` at 0.1 / 0.5 / 0.9 as the question specifies. Recomputed: P10 25.65, P50 50.30, P90 62.90.
- Part (c): gap `=B3-B1` — recomputed 37.25; note quotes 37.3, correct.
- Part (d): range `=MAX(...)-MIN(...)` — recomputed 79.8 − 11.7 = 68.1, matching the note; "almost twice the 90-10 gap" is right (68.1/37.25 = 1.83), and the reasoning for preferring the 90-10 gap is sound.
- Part (b) note ("out-yielded only one in ten RMs, about 26 bu/ac") is a correct plain-language reading of the 10th percentile.
- Colours and legend (A11:A14) coherent for parts (a)-(d).

## Summary

No errors found in Questions 11-15. All Data sheets are exact filters of the source CSV (right year, right crop, right counts and values), all formulas use the correct Excel functions and ranges, every quoted number in the notes matches independent recomputation, skew/variability claims are directionally correct, and colour legends match the parts. Two minor flags: the bank's Q11 part (c) references "parts a-d" although (d) follows it (bank wording, not the workbook), and Q13's "barely half" slightly understates a 54% ratio.
