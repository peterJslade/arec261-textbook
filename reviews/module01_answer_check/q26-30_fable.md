# Answer-workbook check: Questions 26-30 (Manitoba Wheat Variety)

Checked 2026-09-01 against `practice/data/mb_wheat_reported_2020_2025.csv` (2,398 data rows). Workbooks read with openpyxl, read-only; expected values recomputed in Python. All five Data sheets hold the full 7-column dataset (2,398 rows + header), spot-checked at five positions each -- all exact matches. Year is stored numeric, so both the numeric year criteria (`2023`) and the text bounds (`">=2020"`) evaluate correctly. None of the five workbooks carries cached formula results (script-written, never recalculated by Excel); every expected value below was recomputed from the CSV, and the notes' quoted numbers were checked against those. The embedded Excel Online viewer recalculates on open, but a one-time visual check of each embed would confirm the counts display.

## Question 26 — q054.xlsx

**Verdict: Correct; legend lists a part (b) colour no cell uses.**

- Legend says green = Part (b), but no cell on the sheet is green. The part (b) counts (C2:G2, thresholds 50-90) share part (a)'s yellow, and the row label "Count (a/b)" is the only signal. Either colour C2:G2 green or drop the green legend row. Cosmetic, but the legend as written is wrong about its own sheet. (The fractions row is blue = part (c), which is right.)
- Formulas: `COUNTIF(Data!$F$2:$F$2399,">40")` through `">90"`, fractions `=B2/COUNT(Data!$F$2:$F$2399)`. Ranges and denominator (2,398) correct.
- Expected counts: >40 = 2259, >50 = 1984, >60 = 1387, >70 = 569, >80 = 97, >90 = 17; fractions 94.2%, 82.7%, 57.8%, 23.7%, 4.0%, 0.7%.
- Note (c) quotes "58% above 60, 24% above 70, 4% above 80" -- all match. "Most of the distribution sits between 50 and 70" -- the 50-70 band holds 59.0% of rows, so "most" is fair.

## Question 27 — q057.xlsx

**Verdict: Correct.**

- Formulas: `AVERAGEIF(Data!$C$2:$C$2399,"SY MANNESS",Data!$F$2:$F$2399)` and the `AAC BRANDON (BW 932)` twin; `COUNTIF` on the same variety column. Ranges and criteria exact (full variety string used, matching the CSV).
- Expected: Manness average 72.12 over 108 rows; Brandon 59.62 over 519 rows. Note (c) quotes "72.1 vs 59.6" and "519 rows vs 108" -- right on both facts and on which variety holds which.
- Note (d)'s "about a fifth as many results" -- 108/519 = 0.208, fine. Note (e) is a reasonable one-sentence answer.
- Colour legend coherent: five parts, five colours, each used exactly where its part's answer sits.

## Question 28 — q058.xlsx

**Verdict: Correct.**

- Formulas: `COUNTIFS` on variety = `AAC BRANDON (BW 932)` and Year = 2020...2025, one column per year, correct ranges.
- Expected counts: 94, 90, 87, 84, 83, 81 for 2020-2025. Note (b) says 2020 has the most (94) and the count "slips every year to 81 by 2025" -- both claims match (the sequence is strictly decreasing).
- Note (c) matches Peter's answer sketch in the bank (profit-oriented growers moving to newer varieties, composition warning for later-year averages).
- Colour legend coherent (yellow a, green b, blue c).
- Bank-side aside, not a workbook issue: question (c) says "these five years" but parts (a)/(b) cover 2020-2025, six years. Not edited per instructions.

## Question 29 — q029.xlsx

**Verdict: Correct.**

- Formulas: `SUMIFS` on Acres (col E) and `AVERAGEIFS` on Yield (col F), each conditioned on variety plus `">=2020"` and `"<=2025"` on Year. Ranges correct; the year bounds are redundant (the file only spans 2020-2025) but they follow the question's wording and evaluate correctly against the numeric Year column.
- Expected: Brandon 6,741,112 acres, average 59.62; Manness 389,027 acres, average 72.12.
- Note (c) quotes "about 6.7 million against 0.39 million" and "59.6 vs 72.1" -- both match, and the conclusion (yield cannot be driving the acreage gap; the higher-yielding variety has far fewer acres) is sound.
- Colour legend coherent.

## Question 30 — q031.xlsx

**Verdict: Correct; legend lists a part (c) colour no cell uses.**

- Legend says blue = Part (c), but no cell on the sheet is blue. Part (c) is the Manness column, and its cells take part (a)'s yellow (C2) and part (b)'s green (C3, C4); the row labels "(a/c)" and "(b/c)" carry the mapping instead. Either drop the blue legend row or recolour column C. Cosmetic, same pattern as Q26.
- Formulas: three-condition `COUNTIFS` (variety, Year = 2023, `">60"` on Yield) in row 2; two-condition `COUNTIFS` totals in row 3; fractions `=B2/B3`, `=C2/C3` formatted 0.0%. Ranges and criteria exact.
- Expected: Brandon 46 of 84 above 60 (54.8%); Manness 8 of 11 (72.7%).
- Note (d) quotes "73% against Brandon's 55%" and "11 results against Brandon's 84" -- all match, and flagging the Manness figure as resting on 11 rows is a good caution.
