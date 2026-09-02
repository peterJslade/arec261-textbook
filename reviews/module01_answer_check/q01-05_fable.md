# Module 1 bank — answer workbook check, Questions 1–5

Checked with openpyxl (read-only, formulas inspected, results recomputed in Python). Workbooks: Q1=s1_q01.xlsx, Q2=s1_q02.xlsx, Q3=s1_q04.xlsx, Q4=s1_q07.xlsx, Q5=s1_q09.xlsx.

## Question 1 (s1_q01.xlsx) — OK

- All parts answered. (a) `=C2*$H$2` filled D2:D6, currency `$#,##0.00`; recomputed rev/ac 585.04 / 548.12 / 636.16 / 512.62 / 566.58 match. (b) `=D2*B2` in E2:E6, `$#,##0` (thousands separator, no decimals) as asked. (c) totals B8=SUM acres (940), F8=SUM bushels via helper column F `=B2*C2` (36,637.5), E8=SUM revenue (520,252.5). (d) note in A10 is correct: the $ locks the single price cell during fill-down; part (b)'s operands are row-aligned so relative references shift correctly.
- Colour coding coherent: yellow=a, green=b, blue=c, red=d; legend A13:A16 lists parts (a)–(d), matching the fills used.
- Trivial: the bushels helper column F carries only the header "Bushels" — its part-(c) fill is the only thing tying it to part (c). Fine, since the totals row is labelled "Totals (c)".

## Question 2 (s1_q02.xlsx) — OK

- (a) single mixed-reference formula `=B2*B$8` filled through F2:H6 — correct (column free for fill-across to wheat/barley prices, row locked for fill-down). Currency 2-decimal format applied.
- (b) note A11 correctly identifies the locked row (the 8) and free column.
- (c) note A12 is correct: a fully absolute `$B$8` would make every copy use the canola price, so the wheat and barley revenue columns would be wrong with no error shown.
- (d) `=AVERAGE(...)` in F9:H9; recomputed 569.70 / 427.02 / 347.54 match.
- (e) note A13's numbers check out: canola ≈ $570/ac, ≈ $143/ac over wheat (≈ $427), barley ≈ $348 (computed gap 142.68).
- Colour coding coherent; legend A16:A20 lists (a)–(e) and the fills match (d=red on the average row, e=purple on the note).
- Trivial mismatch with the question text: part (c) of the question hypothesises the canola price in A8 (`$A$8`); in the workbook it sits in B8 and the note uses `$B$8`. Internally consistent, so not misleading.

## Question 3 (s1_q04.xlsx) — OK

- (a) column C is `=B2`… formatted `0.00%` (displays 13.42% etc.). (b) `=AVERAGE` on both columns, B8 general and C8 percent; recomputed mean 0.13164 / 13.16%. (c) `=IF(B2>0.135,"Yes","No")` and `=COUNTIF(D2:D6,"Yes")` — loads C (0.1401) and E (0.1356) flag Yes, count 2, matches recomputation. (d) note A11 correctly explains stored proportions vs. displayed percent.
- Colour coding coherent; legend lists (a)–(d) matching the fills.
- Minor: part (a) says "copy the protein column into a new column", but the workbook links it with `=B2` formulas rather than pasted values. Displays identically and the (b) averages agree, but a student who literally copy-pastes will have static values where the answer key shows formulas. Worth a thought, not an error.

## Question 4 (s1_q07.xlsx) — OK

- (a) MIN/MAX/AVERAGE/MEDIAN on B2:B8 in F2:F5 — recomputed 39.5 / 61.8 / 50.9 / 50.3, match. (b) range `=F3-F2` = 22.3. (c) updated column C with B3=91.8 as a value column, stats recomputed in G2:G6: min 39.5, max 91.8, mean 55.2, median 50.3, range 52.3 — all match; note A10 correctly reports max, mean and range changed, min and median did not. (d) note A11 correct, including the mean rising by "about 4.3 bu/ac" (computed 4.29 = 30/7).
- Colour coding coherent; legend lists (a)–(d) matching the fills (the updated stats in G are part-(c) blue, which is right since they are the recalculation).
- Pedantic point only: the question's (d) asks why the median "moved so little" when in this data it does not move at all; the note says so explicitly, which is the honest answer.

## Question 5 (s1_q09.xlsx) — OK

- (a) limit in its own labelled cell F2 (14.5), `=IF(B2>$F$2,"Wet","Dry")` filled C2:C7 — Trucks 2, 3, 5, 6 read Wet, matching recomputation. (b) `=COUNTIF(C2:C7,"Wet")/COUNT(B2:B7)` = 4/6 = 66.7%, formatted `0%` (shows 67%). (c) new column D against a second labelled limit cell F4 (13.5) plus the fraction in D10 = 5/6 = 83%, matching recomputation.
- Colour coding coherent; legend lists (a)–(c), matching the fills, and no part needs a written note.
- Trivial: the `0%` format rounds 66.67% to 67% on screen; acceptable, though `0.0%` would show the fraction less bluntly.

## Summary

No wrong formulas, no wrong numbers, no missing parts, no legend mismatches across the five workbooks. Three trivial observations (Q2 A8-vs-B8 wording, Q3 formula-link vs. literal copy, Q5 percent rounding), none of which would mislead a student.
