# Module 1 bank — answer workbook check, Questions 6–10

Checked with openpyxl (read-only; no workbook or bank file was modified). Every formula was read from the file and its result recomputed independently in Python from the question tables. Workbooks: Q6=s1_q13.xlsx, Q7=s1_q15.xlsx, Q8=s1_q21.xlsx, Q9=s1_q24.xlsx, Q10=s1_q26.xlsx. All five have a single sheet named `Answer`.

## Question 6 (s1_q13.xlsx) — OK, one wording issue

- (a) `=C2-B2` filled D2:D6, number format `0`. Recomputed day counts 129 / 120 / 133 / 136 / 133 — match. (b) G1 `=MIN(D2:D6)` = 120, G2 `=MAX(D2:D6)` = 136, both format `0`; the fields are named in the A8 note (Tamarack shortest, Verdant longest) and both are correct. (c) G3 `=AVERAGE(D2:D6)` format `0.0` = 130.2, correct. (d) note in A9.
- The A9 answer to part (d) is technically correct and I verified the arithmetic: `04-May-1900` is serial 125 in Excel's 1900 date system (accounting for the phantom 29-Feb-1900), so a result of 125 days displayed as a date does read as 04-May-1900. The advice — reformat the column to Number or General — is the right fix.
- **Wording, part (d):** the note opens "Her subtraction worked -- Excel just formatted the result as a date". This is the correct diagnosis for the *symptom the question describes*, but the question says she reports "subtracting dates doesn't work for her", which a student could equally read as her *inputs* being text-dates rather than her *output* being date-formatted. The note never acknowledges the other common cause (dates stored as text, where the subtraction returns `#VALUE!`). Since the question hands the student the string `04-May-1900` as the thing she sees, the key's reading is the intended one, but the note would be sturdier if it said explicitly that the `04-May-1900` she is looking at is the *answer cell*, not a date in her data. As written a student can finish the question still unsure which cell is misformatted.
- Colour coding coherent: yellow=(a) on D2:D6, green=(b) on G1:G2 and the A8 note, blue=(c) on G3, red=(d) on the A9 note. Legend A12:A15 lists parts (a)–(d) and every listed colour is actually used.
- Trivial: `Days to harvest (a)` in D1 is the only header carrying a part tag; F1/F2/F3 labels carry theirs too, so the sheet is consistently labelled.

## Question 7 (s1_q15.xlsx) — OK

- (a) `=B2*C2` in D2:D4 (`$#,##0.00`); recomputed 18,414.00 / 11,524.00 / 4,407.50. Totals B5 `=SUM(B2:B4)` = 2,510 t and D5 `=SUM(D2:D4)` = $34,345.50 — both `SUM` as the question requires, and both correct.
- (b) B7 `=D5/B5` = 13.6835. (c) B8 `=SUMPRODUCT(B2:B4,C2:C4)/SUM(B2:B4)` = 13.6835, identical, and it is genuinely a single cell using both named functions as asked. Both formatted `$0.000`, so they display $13.683 and agree visibly — good, since the point of (c) is that it reproduces (b).
- (d) B9 `=AVERAGE(C2:C4)` = 13.000 exactly, and the A11 note's figures ("about $13.68/t" and "about $13.00/t") match. The explanation correctly identifies the blended price as what the farm received and correctly attributes the gap to unequal tonnage across grades.
- Colour coding coherent: yellow=(a), green=(b), blue=(c), red=(d) on both B9 and the A11 note. Legend A14:A17 lists (a)–(d), all used.

## Question 8 (s1_q21.xlsx) — OK

- (a) `=B2*C2` in E2:E4 (`$#,##0.00`); recomputed 596.40 / 459.25 / 380.80. (b) `=E2-D2` in F2:F4; 181.40 / 139.25 / 95.80. (c) `=F2/E2` in G2:G4 formatted `0.0%`; recomputed 30.4% / 30.3% / 25.2%. All correct, and (c) is genuinely formatted as a percentage rather than multiplied by 100, which is what the question asks for.
- Question 8 has only three parts, and all three are answered. Colour coding coherent: yellow=(a) on column E, green=(b) on column F, blue=(c) on column G. Legend A7:A9 lists exactly (a)–(c) — correctly *not* listing a part (d), unlike the four-part questions.
- No written note, and none is needed: no part of Q8 asks for an explanation.

## Question 9 (s1_q24.xlsx) — OK, one placement issue

- (a) `=SUM(B2:D2)` filled E2:E6; recomputed field totals 560 / 640 / 440 / 480 / 400 — match. (b) `=SUM(B2:B6)` etc. in B7:D7; crop totals 960 / 960 / 600 — match. (c) G2 `=SUM(B2:D6)` = 2,520, a single `SUM` over the whole numeric block exactly as asked, and it equals both the row-total and column-total sums (verified: 2,520 three ways).
- (d) note A9 is correct in every particular I could check: `=SUM(B2:B6, D2:D6)` gives 1,560 (960 canola + 600 peas, recomputed), and the missing acres are the 960 wheat acres in column C. The explanation of *why* — two arguments naming two column ranges, skipping the column between — is right.
- **Placement, part (c):** the grand total sits in G2 with its label `All acres (c)` in G1, i.e. in the header row of the data table, two columns right of the field totals. A student reading the sheet sees a bold header-row label that is not a column header for anything. It would read more clearly one row down or below the table. Cosmetic, not wrong, but it is the one spot in these five workbooks where the layout could mislead someone skimming.
- Colour coding coherent: yellow=(a) on E2:E6, green=(b) on B7:D7, blue=(c) on G2, red=(d) on the A9 note. Legend A12:A15 lists (a)–(d), all used.

## Question 10 (s1_q26.xlsx) — issues

- Formulas all correct. (a) E1 `=COUNT(B2:B8)` = 4, E2 `=COUNTA(B2:B8)` = 5, E3 `=SUM(B2:B8)` = 111.0 (`0.0`). (b) E4 `=AVERAGE(B2:B8)` = 27.75 (`0.00`). Recomputed from 24.8 + 31.2 + 28.6 + 26.4: sum 111.0, count 4, mean 27.75 — all match. The data block is faithful to the question: B3 and B7 are genuinely empty cells (not blank strings), B5 holds the text `rejected`.
- **Part (c) does not name the loads it was asked to name.** The question asks "which loads `AVERAGE` used"; the A10 note answers "AVERAGE used the same 4 numeric loads as COUNT". That is true but it never says *which* — Loads 1, 3, 5 and 7. A student grading themselves against this key cannot tell whether naming the loads was required, and the answer key is the one place the expected level of specificity should be visible. Expected: an explicit "Loads 1, 3, 5 and 7". Found: a back-reference to COUNT.
- **Part (c) calls `SUM` a count.** The question says "explain what each of your counts in part a counted, why none equals seven". The A10 note follows that framing and reports SUM inside the same list ("SUM added the 4 numbers (111.0)"), which is fine, but then the note's "None equals seven" clause now covers SUM too — and SUM's result, 111.0, is a tonnage, not a count, so "equals seven" is not a meaningful comparison for it. The question itself is the source of this looseness (it calls all three "counts"), but the key inherits it rather than quietly fixing it. Cleanest fix is in the key: state the two counts against seven, and note separately that SUM is a total, not a count.
- **Part (c)'s reason for "none equals seven" is incomplete for COUNTA.** The note gives one combined reason: "two loads have no entry at all and one was rejected without a weight". That explains COUNT = 4. For COUNTA = 5 the reason is different and narrower — only the two empty cells are missing, because the `rejected` text *is* counted. As written, a student can come away thinking the rejected load is excluded from COUNTA as well, which directly contradicts part (d)'s note two rows below. The two notes are individually correct and jointly confusing.
- Part (d)'s A11 note is correct and clear: COUNT counts numbers only, COUNTA counts every non-empty cell, so the text entry puts COUNTA at 5 against COUNT's 4.
- Colour coding coherent: yellow=(a) on E1:E3, green=(b) on E4, blue=(c) on the A10 note, red=(d) on the A11 note. Legend A14:A17 lists (a)–(d), all used.
- Minor: E3's `SUM` result carries part-(a) yellow and the label `SUM (a)`, which is right, but it sits directly above the `AVERAGE (b)` cell in the same column with only the fill distinguishing them. Fine given the labels.

## Cross-cutting notes

- No cached values in any of the five files (as expected). Every figure above was recomputed in Python from the question tables, not read from the workbook.
- All five legends match the fills actually used, and the palette is consistent across the set: `FFF2CC` = (a), `D9EAD3` = (b), `CFE2F3` = (c), `F4CCCC` = (d). Q8, which has no part (d), correctly stops its legend at (c).
- All long note cells have wrap-text on with a 64-point row height, so they display without manual resizing.
- None of the five workbooks has a frozen header row. Irrelevant at these table sizes.
- Number formats are appropriate throughout: currency where dollars, `0.0%` for the margin, plain `0` for day counts.
