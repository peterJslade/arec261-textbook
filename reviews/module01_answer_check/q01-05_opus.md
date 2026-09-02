# Module 1 bank -- answer workbook check, Questions 1-5

Checked by opus, 2026-09-01. Workbooks opened read-only with openpyxl; every formula
re-evaluated in Python against the data printed in the question table. No files were
modified.

Mapping used: Q1 = `s1_q01.xlsx`, Q2 = `s1_q02.xlsx`, Q3 = `s1_q04.xlsx`,
Q4 = `s1_q07.xlsx`, Q5 = `s1_q09.xlsx`.

## Verdicts

- **Question 1 -- OK (one minor note)**
- **Question 2 -- OK (two minor notes)**
- **Question 3 -- issues (one substantive, one minor)**
- **Question 4 -- OK (one minor note)**
- **Question 5 -- OK (two minor notes)**

---

## Question 3 (`s1_q04.xlsx`) -- issues

- **Part (c) undercounts the intent of the question, or the question's own numbers
  contradict its part (d).** The contract "pays a premium on loads above 13.5% protein".
  D2:D6 use `=IF(B2>0.135,"Yes","No")`, which flags C (0.1401) and E (0.1356) only --
  `COUNTIF` in D9 returns **2**. That is the correct reading of "above". But part (d)
  then says the column "reads 13.42%", i.e. it singles out load A (0.1342) as the
  motivating case, and load A is *below* the threshold and is flagged `No`. A student
  reading (d) will reasonably expect load A to be near the boundary in an interesting
  way; it is not, and the worked answer never resolves that. Either the (d) prompt should
  cite a load that actually sits above 13.5% (C at 14.01%, or E at 13.56%), or the answer
  note should say explicitly that load A reads 13.42% and is therefore *not* flagged.
  As it stands the pairing is confusing.
- **Part (a) links rather than copies.** C2:C6 contain `=B2` … `=B6`, not pasted values.
  The question says "Copy the protein column into a new column and format it as a
  percentage." A live link gives the same displayed result and is defensible, but it is
  not a copy, and a student who copy-pastes values (as instructed) will produce a
  different-looking sheet from the answer key. Worth a one-line note in the workbook
  saying either form is accepted.
- Verified numerics, all correct as computed: `AVERAGE` in B8 = 0.13164, C8 displays
  13.16%; `COUNTIF` in D9 = 2; flags No/No/Yes/No/Yes for loads A-E.
- Colour coding is coherent: four fills in use (`FFF2CC` a, `D9EAD3` b, `CFE2F3` c,
  `F4CCCC` d) and the legend at A14:A17 lists exactly those four parts.
- Part (b)'s point is left implicit. B8 (General, 0.13164) and C8 (0.00%, 13.16%) sit
  side by side but nothing says they are the same number displayed two ways -- which is
  the whole reason the question asks for both. One sentence would close the loop, and it
  would also set up part (d).

---

## Question 1 (`s1_q01.xlsx`) -- OK

All four parts present and correct.

- (a) D2:D6 `=C2*$H$2` etc., format `$#,##0.00`. Expected $585.04, $548.12, $636.16,
  $512.62, $566.58 -- correct.
- (b) E2:E6 `=D2*B2`, format `$#,##0` (currency, thousands separator, no decimals, as
  asked). Expected $70,205 / $131,549 / $60,435 / $158,912 / $99,152 (unrounded
  $70,204.80 etc.) -- correct.
- (c) B8 `=SUM(B2:B6)` = 940 acres; F8 `=SUM(F2:F6)` = 36,637.5 bu; E8 `=SUM(E2:E6)` =
  $520,252.50. All three totals asked for are present. Correct.
- (d) The note in A10 is factually right and answers the right question (why the price
  reference needs `$` and the same-row references do not).
- Legend at A13:A16 matches the four fills actually used.

Minor note: the "Bushels" helper column F is created only to serve part (c) and is
filled with the part (c) colour, which is coherent -- but it sits to the *right* of the
part (b) column, so the sheet reads a-b-c left to right while the question introduces
bushels only in (c). Not wrong, just worth confirming it reads clearly on screen.

---

## Question 2 (`s1_q02.xlsx`) -- OK

All five parts present and correct.

- (a) F2:H6 all `=B2*B$8` filled down and across -- a single formula, mixed reference,
  exactly as the question demands. Recomputed values match.
- (b) Note in A11 correctly identifies the row as locked and the column as free.
- (c) Note in A12 correctly describes the `$B$8` failure mode.
- (d) F9:H9 `=AVERAGE(F2:F6)` etc. Expected $569.70 (canola), $427.02 (wheat),
  $347.54 (barley) -- correct.
- (e) Note in A13 says canola about $570/ac, roughly $143/ac over wheat at about
  $427/ac, barley third at about $348/ac. Matches the recomputation exactly.
- Legend at A16:A20 lists five parts and five distinct fills are in use.

Minor notes:

- The question's part (c) names `$A$8` as the example cell ("where canola price was
  saved in cell A8"), but the answer workbook puts prices in B8:D8 and the note talks
  about `$B$8`. Internally consistent, but a student comparing the two will hit a
  moment's friction. Consider aligning the question's example cell with the layout the
  answer uses, or phrasing the question's example generically.
- The price row (8) sits immediately above the averages row (9) with no blank between,
  and the averages are labelled in E9 while the prices are labelled in A8. The block is
  a little cramped for something students are told to imitate for presentation marks.

---

## Question 4 (`s1_q07.xlsx`) -- OK

All four parts present and correct.

- (a) F2:F5 `MIN`/`MAX`/`AVERAGE`/`MEDIAN` over B2:B8. Expected 39.5 / 61.8 / 50.9 /
  50.3 -- correct.
- (b) F6 `=F3-F2` = 22.3. Correct, and building the range from the MAX and MIN cells
  rather than re-typing is the better habit to model.
- (c) Column C copies the yields with B changed to 91.8; G2:G6 recompute. Expected
  39.5 / 91.8 / 55.2 / 50.3 / 52.3 -- correct. The note in A10 reports max, mean and
  range as changed and min and median as unchanged, which is right.
- (d) Note in A11 is correct, including the arithmetic: the mean rises by 30/7 = 4.29
  bu/ac, and the note says "about 4.3 bu/ac".
- Legend at A14:A17 matches the four fills in use.

Minor note: C2:C8 are typed constants, not `=B2` links. That is the right choice here
(the whole point is that one value differs), but it means the sheet will not update if
the source data changes. Fine for an answer key; no action needed.

---

## Question 5 (`s1_q09.xlsx`) -- OK

All three parts present and correct.

- (a) Limit 14.5 lives on its own in F2 and C2:C7 use `=IF(B2>$F$2,"Wet","Dry")` with an
  absolute reference to it, as asked. Expected Dry / Wet / Wet / Dry / Wet / Wet --
  correct.
- (b) C9 `=COUNTIF(C2:C7,"Wet")/COUNT(B2:B7)` = 4/6 = 0.6667, formatted `0%` so it
  displays 67%. Correct, and it uses both required functions.
- (c) Lower limit 13.5 in F4, D2:D7 relabel against it, D10 gives 5/6 = 0.8333 → 83%.
  Correct.
- Legend at A13:A15 lists three parts and three fills are in use.

Minor notes:

- **The `0%` number format rounds 66.67% to 67% and 83.33% to 83%.** With six loads the
  fractions are never round, so the displayed figures are visibly approximate. `0.0%`
  would show 66.7% and 83.3% and would better model the habit of not hiding precision.
  Not wrong -- the question only says "format it as a percentage" -- but for six trucks
  it reads oddly.
- Part (c) asks for "a new column that calculates the fraction of loads that would be
  wet". The workbook interprets this as a new label column (D2:D7) plus a single fraction
  cell (D10), which is the sensible reading, but the question's wording ("a column that
  calculates the fraction") could be read as asking for the fraction itself in a column.
  The answer is fine; the *question* is the ambiguous half. Worth tightening the bank
  wording to "add a new column of labels and recompute the fraction".
- No written note anywhere in this workbook. The other four all carry at least one
  explanation cell. Q5 has no part that demands prose, so this is consistent with the
  question -- flagged only so it is not mistaken for an omission.

---

## Cross-cutting observations

- The four-colour scheme (`FFF2CC` / `D9EAD3` / `CFE2F3` / `F4CCCC`, plus `D9D2E9` for a
  fifth part) is used consistently across all five workbooks and every legend matches the
  fills actually present. No mismatches found.
- Every workbook has a single sheet named `Answer`. The bank tells students their
  submission should have "a separate worksheet for each question ... clearly labelled
  with the question number". These per-question answer keys are one question each, so a
  sheet named `Answer` is reasonable, but naming it `Q1`, `Q2`, ... would model the
  submission convention the bank asks for.
- All workbooks store live formulas with no cached values, so anything opened in a viewer
  that does not recalculate (some embed viewers, some previewers) will show blanks or
  zeros rather than results. If these are the files behind the `embedview` iframes in
  `practice/module01_bank.qmd`, the embeds should be spot-checked in a signed-out browser
  to confirm Excel for the web recalculates them.
