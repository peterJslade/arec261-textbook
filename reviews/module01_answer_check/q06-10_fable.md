# Module 1 answer-workbook check — Questions 6-10

Checked against `practice/module01_bank.qmd`; workbooks opened with openpyxl (formulas + fills), expected values recomputed independently in Python. No files were modified.

## Question 6 — s1_q13.xlsx: OK

- All four parts answered. D2:D6 `=C2-B2` formatted as plain number (fmt `0`), matching part (a)'s formatting requirement. Recomputed days: Sandhill 129, Tamarack 120, Upland 133, Verdant 136, Westgate 133.
- G1 `=MIN(D2:D6)` -> 120 and G2 `=MAX(D2:D6)` -> 136 correct; note A8 correctly names Tamarack (120) and Verdant (136).
- G3 `=AVERAGE(D2:D6)` -> 130.2 correct.
- Part (d) note (A9) is factually right: a 125-day difference auto-formatted as a date displays as 04-May-1900 (Excel serial 125, phantom 1900 leap day included), and the fix (reformat as Number/General) is the correct advice.
- Colour-coding coherent: yellow (a) on D2:D6, green (b) on MIN/MAX and the A8 note, blue (c) on the average, red (d) on the A9 note; legend A12:A15 lists parts (a)-(d) in the matching fills.

## Question 7 — s1_q15.xlsx: OK

- Part (a): D2:D4 `=B*C` (18,414.00 / 11,524.00 / 4,407.50), totals B5 `=SUM(B2:B4)` = 2,510 and D5 `=SUM(D2:D4)` = 34,345.50 — all correct.
- Part (b): B7 `=D5/B5` -> 13.6835 ($13.684 at the $0.000 format). Part (c): B8 `=SUMPRODUCT(B2:B4,C2:C4)/SUM(B2:B4)` gives the same value in one cell, as asked.
- Part (d): B9 `=AVERAGE(C2:C4)` -> 13.00; note A11 correctly identifies the blended price (~$13.68) as what the farm received and explains the divergence via unequal tonnage weighting.
- Colours and legend (A14:A17) coherent for parts (a)-(d).

## Question 8 — s1_q21.xlsx: OK

- E2:E4 `=B*C` -> 596.40 / 459.25 / 380.80; F2:F4 `=E-D` -> 181.40 / 139.25 / 95.80; G2:G4 `=F/E` -> 30.4% / 30.3% / 25.2%, formatted `0.0%` as part (c) requires. All match recomputation.
- Question has only parts (a)-(c); legend (A7:A9) lists exactly those three, colours match the columns.

## Question 9 — s1_q24.xlsx: OK

- Part (a): E2:E6 row sums -> 560 / 640 / 440 / 480 / 400. Part (b): B7:D7 column sums -> 960 / 960 / 600. Part (c): G2 `=SUM(B2:D6)` -> 2,520. All correct.
- Part (d) note (A9) is exactly right: `=SUM(B2:B6, D2:D6)` gives 1,560 (Canola + Peas) and misses all 960 Wheat acres in column C.
- Colours and legend (A12:A15) coherent for parts (a)-(d).

## Question 10 — s1_q26.xlsx: OK

- Data faithfully reproduces the table (B3 and B7 genuinely empty, B5 holds the text `rejected`).
- Part (a): E1 `=COUNT(B2:B8)` -> 4, E2 `=COUNTA(B2:B8)` -> 5, E3 `=SUM(B2:B8)` -> 111.0. Part (b): E4 `=AVERAGE(B2:B8)` -> 27.75. All confirmed.
- Note A10 (part c) is correct on every claim: COUNT = 4 numerics, COUNTA = 5 non-empty (4 numbers + "rejected"), SUM = 111.0, why none is 7, and that AVERAGE used the same 4 numeric loads. Note A11 (part d) correctly attributes the COUNT/COUNTA gap to the text cell.
- Colours and legend (A14:A17) coherent for parts (a)-(d).

## Summary

No issues found in Questions 6-10. All formulas are correct Excel for their parts, all recomputed values match, written notes are factually accurate and responsive, and colour legends match the parts each question actually has.
