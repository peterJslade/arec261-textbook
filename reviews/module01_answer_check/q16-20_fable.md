# Answer-workbook check: Questions 16-20 (Manitoba Wheat Variety)

Checked 2026-09-01 against `practice/data/mb_wheat_reported_2020_2025.csv` (2,398 data rows, all `Reported = TRUE`). Workbooks read with openpyxl, read-only; expected values recomputed in Python (STDEV.S = sample sd, QUARTILE.INC = linear interpolation).

## Question 16 — q021.xlsx

**Verdict: Correct.**

- Data sheet: 2,398 yields, exact match to the CSV yield column in order.
- Formulas: `AVERAGE`, `MEDIAN`, `STDEV.S`, `QUARTILE.INC(...,3)-QUARTILE.INC(...,1)`, CV `=B3/B1`, all over `Data!$A$2:$A$2399`. Ranges correct.
- Expected: mean 61.156, median 62.20, sd 12.383, IQR 15.70, CV 0.2025. Notes quote 61.2, 62.2, and 0.20 -- all right; the "slight left skew, roughly symmetric" reading of mean < median is right; "about half" of the 0.39 canola CV is fair.
- Colour legend coherent (yellow a, green b, blue c, red d; each note/formula carries its part's fill).

## Question 17 — q023.xlsx

**Verdict: Correct, one layout deviation from the question's own instruction.**

- The question says to copy each year's yields "into a worksheet of its own"; the workbook instead puts both years side by side as two columns of one Data sheet (A = 2021, B = 2023). The statistics are unaffected, and two columns work just as well for `MEDIAN`/`STDEV.S`, but the answer does not model the layout the question describes, and the question's stated rationale for separate sheets reads oddly against it. Low severity; consider either relaxing the question wording or splitting the sheet.
- Data: 2021 column has 396 values, 2023 has 423 -- exact match to the CSV year filters, values in order.
- Formulas reference `A2:A397` and `B2:B424` -- correct extents for the unequal column lengths.
- Expected: 2021 mean 49.640, median 50.55, sd 12.200, CV 0.2458; 2023 mean 61.417, median 61.90, sd 11.274, CV 0.1836. Notes quote 49.6 vs 61.4 ("roughly 12 bushels, about a fifth" -- diff is 11.78, a fifth of 61.4 is 12.3, fine) and CVs 0.25 vs 0.18 -- all right.
- Colour legend coherent.

## Question 18 — q024.xlsx

**Verdict: Correct.**

- Data sheet: 519 AAC BRANDON (BW 932) yields, exact match to the CSV filter (no stray variety variants exist in the file).
- Formulas over `Data!$A$2:$A$520` -- correct; `STDEV.S` used; CV `=B3/B1`.
- Expected: mean 59.622, median 61.00, sd 11.116, CV 0.1864. Note quotes 0.186 against the all-varieties 0.20 (actual 0.2025) -- right, and the direction of the comparison and its explanation are sound.
- Colour legend coherent (three parts, sd correctly coloured as part (a) per the question wording).

## Question 19 — q025.xlsx

**Verdict: One misleading claim in the (d) note; numbers and formulas otherwise correct.**

- **Note (d) says Manness "varies less around its mean." In absolute terms it does not.** Expected sds: SY MANNESS 11.493, AAC BRANDON 11.116 -- Manness's standard deviation is *higher*. Manness varies less only *relative to its mean* (CV 0.159 vs 0.186). Since part (b) has the two sds sitting right above the note showing Brandon's is smaller, the sentence contradicts the student's own worksheet. It should say "varies less relative to its average" or lean only on the CV.
- Data: A = 108 SY MANNESS yields, B = 519 AAC BRANDON yields, both exact matches to the CSV filters.
- Formulas reference `A2:A109` and `B2:B520` -- correct extents.
- Expected: Manness mean 72.121, sd 11.493, CV 0.1594; Brandon mean 59.622, sd 11.116, CV 0.1864. Note's quoted 72.1 vs 59.6, CV 0.19 vs 0.16, and counts 108 vs 519 are all right.
- Colour legend coherent.

## Question 20 — q020.xlsx

**Verdict: Correct.**

- Data sheet: full 7-column table, all 2,398 rows match the CSV cell for cell (Reported kept as text "TRUE", consistent with the source).
- Formulas: plain `AVERAGE(Data!$F$2:$F$2399)` and `SUMPRODUCT(Data!$F$2:$F$2399,Data!$E$2:$E$2399)/SUM(Data!$E$2:$E$2399)` -- F is Yield_bu_ac and E is Acres, so the weighting is the right way round and the ranges are correct.
- Expected: plain 61.156, weighted 62.583. Notes quote 61.2 and 62.6 and correctly say the weighted average is higher; the (d) explanation (every acre counts once vs every row counts once, widely grown rows yield a little better) matches the data.
- Colour legend coherent.

## Cross-cutting observations

- No formula cell in any of the five workbooks carries a cached value (the files were script-written and never opened in Excel). Excel and Excel-for-web recalculate on open, so students see numbers, but anything reading the files programmatically (data_only) sees blanks. Not a defect, just worth knowing.
- `STDEV.S`/`QUARTILE.INC` are stored with the `_xlfn.` prefix -- the correct internal form; they display normally in Excel.
