# Module 1 answer-workbook check — Questions 26-30 (Manitoba Wheat Variety)

Checked against `practice/module01_bank.qmd` (lines 635-733). Workbooks opened read-only with openpyxl (formulas, fills, number formats, merges, cached values); every expected figure recomputed independently from `practice/data/mb_wheat_reported_2020_2025.csv` in Python. No files were modified.

**Data sheets:** all five workbooks (`q054`, `q057`, `q058`, `q029`, `q031`) hold an exact copy of the source CSV — 2,398 data rows under the seven expected headers, zero cell mismatches on a full row-by-row comparison of all 2,398 x 7 values. `Year`, `Farms`, `Acres`, `Yield_bu_ac` are stored as numbers (so the numeric `COUNTIFS` year criteria work), `Reported` as the text `"TRUE"`. No blank yields or acres. Neither `SY MANNESS` nor `AAC BRANDON (BW 932)` is a prefix of any other variety name, so the exact-match text criteria are unambiguous.

**Cached values:** none of the five workbooks stores calculated results — every formula cell reads back empty under `data_only=True`. Values below are my Python recomputations of what the formulas will produce when Excel opens them. (Consistent with the rest of the bank; noted for the record, not as a fault.)

---

## Question 26 — q054.xlsx: OK, one cosmetic mismatch

- All parts present. B2:G2 `=COUNTIF(Data!$F$2:$F$2399,">40")` … `">90"` over the full yield column; B3:G3 divide by `COUNT(Data!$F$2:$F$2399)`. Recomputed: 2259 / 1984 / 1387 / 569 / 97 / 17, giving 94.2% / 82.7% / 57.8% / 23.7% / 4.0% / 0.7%. Header row B1:G1 labels the thresholds `>40`…`>90`.
- Using `COUNT(...)` rather than a hard-coded 2398 as the denominator is the better teaching choice and is right here (all 2,398 yields are numeric).
- **Minor — note rounds against the sheet's own display.** Expected: quoted figures match the `0.0%` cells the student sees. Found: A5 says "58% above 60 to 24% above 70 and 4% above 80" while row 3 renders 57.8%, 23.7%, 4.0%. Only the third agrees. Not wrong, but a student comparing note to cell sees three numbers that do not line up.
- **Minor — legend lists a colour it never uses.** Expected: legend entries correspond to fills on the sheet. Found: A9 "Part (b)" is green `D9EAD3`, but no answer cell is green — parts (a) and (b) are both the yellow `FFF2CC` count row (correctly, since row 2 answers both, and A2 is labelled "Count (a/b)"). The green swatch points at nothing.

## Question 27 — q057.xlsx: OK

- Parts (a)-(e) all answered. B2/C2 `AVERAGEIF(Data!$C$2:$C$2399,"<variety>",Data!$F$2:$F$2399)` and B3/C3 the matching `COUNTIF` on the same criteria range. Recomputed: SY Manness 72.1213 over 108 rows; AAC Brandon 59.6222 over 519 rows. The `0.00` and `0` formats display 72.12 / 59.62 and 108 / 519.
- Note A5 (part c) — "SY Manness has the higher average (72.1 vs 59.6); AAC Brandon has far more data (519 rows vs 108)" — correct on all four numbers and both claims.
- Note A6 (part d) — "about a fifth as many results" — 108/519 = 20.8%, accurate.
- Note A7 (part e) is a sound one-sentence answer.
- Colour-coding coherent: yellow (a) on the averages, green (b) on the counts, blue/red/purple on the (c)/(d)/(e) notes, legend A10:A14 matches all five fills.

## Question 28 — q058.xlsx: OK, one accuracy slip in the note

- Part (a): B2:G2 `=COUNTIFS(Data!$C$2:$C$2399,"AAC BRANDON (BW 932)",Data!$A$2:$A$2399,<year>)` for 2020-2025. Recomputed: 94, 90, 87, 84, 83, 81 — a strictly monotone decline. Header row carries the years.
- Part (b) note A4 identifies 2020 (94) as the peak and 81 as the 2025 value: both correct.
- Part (c) note A5 matches Peter's own answer sketch in the bank (profit-oriented growers move to newer varieties; composition change, not just popularity) and is appropriately hedged as "a defensible reading".
- **Minor — "slips every year" overstates by one step.** Expected: the note describes the actual series. Found: A4 says the count "then slips every year to 81 by 2025", but 2023→2024 is 84→83 and 2024→2025 is 83→81, so the drop stalls from a 3-4/year decline to 1-2/year. "Slips every year" is literally true (each year is lower than the last) but reads as a steady fall; the last three years are near-flat. Worth softening if you want the note to survive a student plotting the series.
- **Minor — the question says "these five years", the data span six.** Expected: consistent framing. Found: bank part (c) asks about "these five years" while parts (a)/(b) cover 2020-2025 inclusive, which is six years. This is a bank-text issue, not a workbook one; the workbook correctly answers over all six. Flagged because a careful student may wonder which window is meant.
- Colour-coding coherent: yellow (a) on row 2, green (b) on A4, blue (c) on A5; legend A8:A10 matches.

## Question 29 — q029.xlsx: OK

- Part (a): B2/C2 `SUMIFS(Data!$E$2:$E$2399, variety, Year>=2020, Year<=2025)`. Recomputed acres: Brandon 6,741,112.4; Manness 389,027. The `#,##0` format shows 6,741,112 and 389,027.
- Part (b): B3/C3 the parallel `AVERAGEIFS` on column F, same three criteria — 59.62 and 72.12, matching Q27.
- The `>=2020` / `<=2025` year bounds are redundant (the file contains only 2020-2025) but are exactly what the question asks for and are the right habit to teach; both criteria are correctly written as quoted comparison strings.
- Note A5 (part c): "about 6.7 million against 0.39 million" and "59.6 vs 72.1" are both accurate, and the logic — higher yield does not explain lower acreage, so something else is driving it — correctly answers "does (b) explain (a)?" with a well-argued no.
- Colour-coding coherent: yellow (a), green (b), blue (c) note; legend A8:A10 matches.

## Question 30 — q031.xlsx: OK, one legend mismatch

- Part (a): B2/C2 three-condition `COUNTIFS(variety, Year=2023, Yield>60)`. Recomputed: Brandon 46, Manness 8.
- Part (b): B3/C3 two-condition 2023 totals — Brandon 84, Manness 11 — and B4/C4 `=B2/B3`, `=C2/C3` formatted `0.0%`, giving 54.8% and 72.7%.
- Part (c) is handled by putting Manness in column C alongside Brandon rather than as a separate block; the row labels say "(a/c)" and "(b/c)", so it is clear, though a student following the parts in order has to notice that (c) is answered sideways.
- Note A6 (part d) correctly names SY Manness as the more frequent 60+ variety and, better, flags that its 73% rests on 11 results against Brandon's 84 — the right caveat and the same lesson as Q27.
- **Minor — quoted percentages rounded away from the displayed cells.** Expected: 72.7% and 54.8% as B4/C4 will render. Found: A6 says "73%" and "55%". Same issue as Q26; less jarring here since it is only one significant digit of drift.
- **Minor — legend has a colour with no matching cell.** Expected: every legend swatch appears on the sheet. Found: A11 "Part (c)" is blue `CFE2F3`, but no answer cell is blue — part (c) is folded into the yellow/green C column. Meanwhile B4/C4 (part b's fraction) share green with B3/C3, which is right. The blue swatch is orphaned, in the same way Q26's green is.

---

## Summary

Six issues, all minor; no formula errors, no wrong numbers in any computed cell, and no data corruption in any of the five Data sheets.

1. **q054 (Q26)** — note quotes 58% / 24% / 4% where the sheet displays 57.8% / 23.7% / 4.0%.
2. **q054 (Q26)** — legend lists a green "Part (b)" swatch that appears on no answer cell.
3. **q031 (Q30)** — legend lists a blue "Part (c)" swatch that appears on no answer cell.
4. **q031 (Q30)** — note quotes 73% / 55% where the sheet displays 72.7% / 54.8%.
5. **q058 (Q28)** — "slips every year to 81" reads as a steady decline; 2023-2025 is 84/83/81, nearly flat.
6. **q058 (Q28)** — bank text says "these five years" for a 2020-2025 (six-year) window. Bank-side wording, not a workbook fault.

The two orphaned legend swatches (1-2 above, items 2 and 3) are the ones most likely to confuse a student, since they promise a colour to hunt for that is not on the sheet. Both arise from the same cause: the question has more lettered parts than the workbook has distinct answer blocks, and the legend was written from the question rather than from the sheet.
