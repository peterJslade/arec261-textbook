# Answer workbook check: Questions 21-25 (Saskatchewan RM Crop Yields)

Checked read-only with openpyxl against `practice/data/rm_yields_1990plus.csv` (10,649 data rows, 1990-2025). All five workbooks have a Data sheet that matches the source CSV exactly: full cell-by-cell comparison of all 10 columns x 10,649 rows found zero mismatches in every workbook, headers identical. All formula ranges correctly span rows 2-10650. Expected values recomputed independently in Python from the CSV.

General note (applies to all five): the workbooks carry no cached formula results (normal for openpyxl-written files); Excel and the SharePoint embed recalculate on open, so this is not an error.

## Q21 (q043.xlsx) -- two-criteria XLOOKUP

**Verdict: PASS**

- Formulas correct. B1 `=XLOOKUP(1&"|"&2023, Data!$B$2:$B$10650&"|"&Data!$A$2:$A$10650, Data!$E$2:$E$10650)` builds the RM|Year key in the same order as the lookup array (B=RM, A=Year) and returns Canola (col E). B2 mirrors it for RM 100 / Spring Wheat (col C). Expected results: canola RM 1 2023 = 36.8; spring wheat RM 100 2023 = 52.9. The `|` delimiter is safe here (4-digit years, integer RMs).
- Minor wording nitpick in the (c) note: "Each RM appears once per year, so an RM number alone matches 36 different rows." True for RM 1 and for 293 of 299 RMs, but 6 RMs have fewer than 36 rows (e.g. RM 521 appears once, RM 408 nine times). No RM ever appears twice in a year, so the pedagogical point stands; "up to 36" would be exact.
- Colour-coding coherent: parts (a)/(b)/(c) filled yellow/green/blue, legend matches.

## Q22 (q044.xlsx) -- COUNTIFS / COUNTIF

**Verdict: PASS**

- Formulas correct: COUNTIFS on canola ">40" AND wheat ">45" over the right columns (E and C); COUNTIF canola ">40". Blank cells in the CSV are stored as genuinely empty cells, so the ">" criteria exclude them correctly.
- Note's numbers all verified: joint count 1,204; canola-only count 1,483; difference 279. The subset logic in the (c) explanation is sound.
- Colour-coding coherent, legend matches.

## Q23 (q047.xlsx) -- AVERAGEIF, 2015 vs 2019

**Verdict: PASS with one cosmetic issue**

- Legend/colour mismatch (cosmetic): the legend lists Part (b) in green (D9EAD3), but no cell in the sheet is green. The part (b) answers (barley averages C2:C3) are filled yellow, the part (a) colour, and the row labels say "(a/b)". Either colour the barley column green or drop the Part (b) legend entry.
- Formulas and numbers all correct. AVERAGEIF conditions on Year (col A) returning Canola (E) and Barley (F). Recomputed: canola 2015 = 36.06, 2019 = 40.78 (change +4.72, +13.1%); barley 2015 = 55.25, 2019 = 68.59 (change +13.34, +24.2%). Note's "4.7 bu/ac (13%)" and "13.3 bu/ac (24%)" match, and the conclusion (barley grew more on both measures) is right.

## Q24 (q048.xlsx) -- nested IF labels + COUNTIF/COUNTIFS

**Verdict: PASS**

- Nested IF correct and complete: K2:K10650 all carry `=IF(E2="","",IF(E2<20,"Low",IF(E2<=40,"Medium","High")))` with row references filled down properly; blanks stay blank; the boundary handling (<20 Low, 20-40 inclusive Medium, >40 High) matches the question. The A5 note quotes the formula exactly as it appears in the sheet.
- Counts verified: whole dataset Low 2,037 / Medium 6,519 / High 1,483 over 10,039 labelled rows (610 blanks); 2023 Low 57 / Medium 118 / High 114 over 289 labelled rows. Note's "about 15%" High overall (actual 14.8%), "39% (114 of 289)" (actual 39.4%), and "Low stays near 20%" (19.7% vs 20.3% overall) all check out.
- Colour-coding coherent, including the K column on the Data sheet filled yellow to match the Part (a) legend entry; four-part legend matches the four fills used.

## Q25 (q050.xlsx) -- AVERAGEIF + COUNTIFS, 2021 vs 2023

**Verdict: PASS with one cosmetic issue**

- Legend/colour mismatch (cosmetic): the legend lists Part (c) in blue (CFE2F3), but no cell in the sheet is blue. The part (c) answer (C3, the 2023 count) is green, the part (b) colour, and the row label says "(b/c)". Same fix options as Q23.
- Formulas and numbers all correct. Averages: canola 2021 = 21.86, 2023 = 33.88. Counts below 20 bu/ac: 2021 = 120, 2023 = 57. The (d) note's "120 against 57 -- more than twice as many" is exact, and the drought interpretation (2021) is consistent with the numbers.
