# Module 01 bank — answer-workbook check, Questions 16–20

Dataset: `practice/data/mb_wheat_reported_2020_2025.csv` (2,398 data rows + header; `Reported` is `TRUE` on every row, so no pre-filter is implied).
Method: openpyxl read-only inspection of each workbook (nothing modified), with every Data column compared value-by-value against the CSV and every quoted figure recomputed in Python.

Recomputed reference values:

| filter | n | mean | median | SD (sample) | CV |
|---|---|---|---|---|---|
| all rows | 2398 | 61.156 | 62.20 | 12.383 | 0.2025 |
| 2021 | 396 | 49.640 | 50.55 | 12.200 | 0.2458 |
| 2023 | 423 | 61.417 | 61.90 | 11.274 | 0.1836 |
| AAC BRANDON (BW 932) | 519 | 59.622 | 61.00 | 11.116 | 0.1864 |
| SY MANNESS | 108 | 72.121 | 73.25 | 11.493 | 0.1594 |

All-rows QUARTILE.INC: Q1 = 53.9, Q3 = 69.6, IQR = 15.70. Acreage-weighted mean = 62.583.

---

## Question 16 — `q021.xlsx`

**Verdict: correct on data and numbers; one blocking formula-syntax defect (shared with the whole bank), one interpretation wording to tighten.**

- **`_xlfn.` prefix on `STDEV.S` and `QUARTILE.INC` will break in Excel.** The sheet XML literally contains `<f>_xlfn.STDEV.S(Data!$A$2:$A$2399)</f>` and `<f>_xlfn.QUARTILE.INC(...)</f>`. `_xlfn.` is the marker for functions *newer* than the file's declared Excel version; `STDEV.S` and `QUARTILE.INC` both shipped in Excel 2010 and are native, so Excel does not strip the prefix — it shows `#NAME?` (or the literal text `_xlfn.STDEV.S`) in B3, B4 and, by dependency, B5. Expected: `=STDEV.S(Data!$A$2:$A$2399)`. Found: `=_xlfn.STDEV.S(...)`. This makes B3/B4/B5 unusable as a displayed answer key, which matters because these workbooks are embedded for students to read.
  - Scope: not local to Q16. Across `practice/answers/` the prefix appears on `STDEV.S` (28×), `QUARTILE.INC` (14×) and `PERCENTILE.INC` (5×) in 25 workbooks. Source is `practice/build_answers.py` lines 28–31 (`QI`, `PI`, `SD`, `VR` constants). Note that the sibling constants that *do* need the prefix — `FT = "_xlfn.FORMULATEXT"` and `_xlfn.XLOOKUP` (10×) — are correct and must be left alone. Only `QUARTILE.INC`, `PERCENTILE.INC`, `STDEV.S`, `VAR.S` should lose it.
- **(b) calls the distribution "slight left skew" on a mean-vs-median gap of 1.04 bu/ac, then hedges to "roughly symmetric" in the same sentence.** The direction is defensible (mean 61.16 < median 62.20, and Fisher skewness is −0.54, genuinely left-skewed), so the answer is not wrong. But it asserts and retracts in one breath, which is confusing as a key a TA grades against — a student who wrote only "symmetric" and a student who wrote only "left skew" can both point at this note. Worth deciding which answer earns the mark. The moment-based skewness (−0.54) supports "left skew" as the intended answer.
- **(a)/(c) formulas, ranges and cached values check out.** `Data!$A$2:$A$2399` is exactly the 2,398 yields; all 2,398 values match the CSV in order, no gaps, no extras. Mean/median/SD/IQR/CV all recompute to the quoted figures.
- **(b) quotes 61.2 and 62.2, (d) quotes 0.20 vs 0.39 — all correct.** The CV rounds to 0.2025, and "wanders about half as much" is a fair reading of 0.20 vs 0.39.
- **Colour legend is coherent.** Cream = (a) on B1:B2, green = (b) on the A7 note, blue = (c) on B3:B5, pink = (d) on A8; legend A11:A14 matches, and matches the bank-wide convention used in q011–q019.
- Minor: the Data sheet header is `Yield (bu/ac)`, not the CSV's `Yield_bu_ac`. Harmless, but it is the only workbook of the five that renames the column rather than carrying the source name.

## Question 17 — `q023.xlsx`

**Verdict: numbers correct; the workbook contradicts the question's own instruction about worksheet layout.**

- **`_xlfn.STDEV.S` in B4 and C4** — same blocking defect as Q16. Expected `=STDEV.S(Data!$A$2:$A$397)`.
- **The question tells students to put each year "into a worksheet of its own", and the key puts both years side by side in two columns of one `Data` sheet.** The bank text even explains *why* ("`MEDIAN` and `STDEV.S` have no conditional versions, so each year needs its own copy of the data") — a rationale about needing separate copies, which two columns on one sheet also satisfies, so the instruction's stated reason does not actually require separate sheets. A student who follows the instruction literally and a student who mirrors the key will produce structurally different workbooks. Either relax the question to "its own column or worksheet", or split the key into `2021`/`2023` sheets. As it stands the key models something the question forbids.
- **Ragged column lengths are handled correctly but silently.** 2021 has 396 values (A2:A397) and 2023 has 423 (B2:B424), so column A is blank from row 398 to 424. The formulas use the correct short range for A and long range for B, and `AVERAGE`/`MEDIAN`/`STDEV.S` would ignore the blanks anyway — but a student copying the key's *layout* and dragging one range across both columns gets a wrong-looking-but-actually-identical answer, and there is no note explaining the differing end rows. A one-line note ("2021 has 396 rows, 2023 has 423") would prevent a graded dispute.
- **Data verified:** column A is exactly the 396 `Year == 2021` yields in CSV order; column B is exactly the 423 `Year == 2023` yields. No stray values.
- **(c) "about 49.6 bu/ac against 61.4 in 2023, roughly 12 bushels (about a fifth) lower" — correct.** Difference is 11.78 bu/ac; 11.78/61.42 = 19.2%, so "about a fifth" is right (relative to the 2023 base, which is the natural reading).
- **(d) "CV is 0.25 in 2021 against 0.18 in 2023" — correct** (0.2458 and 0.1836). Claim that the drought year was also more variable in relative terms holds.
- **Colour legend coherent:** cream (a) on row 2–3, green (b) on rows 4–5, blue (c) on A7, pink (d) on A8, legend matches.

## Question 18 — `q024.xlsx`

**Verdict: data and numbers correct; the answer note is circular about the figure the question asks students to compare against.**

- **`_xlfn.STDEV.S` in B3** — same blocking defect.
- **(c) compares this variety's CV to "the all-varieties figure (0.20)" — but 0.20 *is* the all-varieties CV computed in Q16 from the same workbook family, and the gap the note makes an argument about is 0.186 vs 0.2025, i.e. 0.016.** The note's reasoning ("the pooled spread contains everything Brandon's does plus the differences between varieties themselves, so a single variety should be a little less variable") is sound economics and the direction is right. The problem is that at two decimal places both round to 0.19/0.20 and the difference is well inside what a student would consider noise, so a student who answers "they're basically the same" is not wrong and the key gives the TA no guidance on that. Worth either quoting the all-varieties CV to three decimals in the question stem (0.203, not "about 0.20") so the comparison has room, or acknowledging in the key that the gap is small.
- **Data verified:** 519 values in A2:A520, exactly the `AAC BRANDON (BW 932)` rows in CSV order. Note this is a *literal* variety-string match — the CSV has no other Brandon spellings, so the filter is unambiguous.
- **(a)/(b) figures correct:** mean 59.62, median 61.00, SD 11.12, CV 0.1864 → the note's "0.186" is right.
- **Colour legend: minor inconsistency.** B3 (standard deviation) is filled cream and labelled "Standard deviation (a)". That is correct per the *question* — Q18(a) asks for mean, median and SD together — but every other workbook in this group uses green for the second-listed computation, and a reader scanning the five sheets will read cream-B1:B3 / green-B4 here against cream-B1:B2 / blue-B3:B5 in Q16 and wonder whether one is mis-tagged. Not an error; just the one place where the colour does not mean the same thing across the set. Legend A9:A11 is internally consistent with the fills used.

## Question 19 — `q025.xlsx`

**Verdict: correct throughout; the strongest of the five. One blocking formula defect and one framing quibble.**

- **`_xlfn.STDEV.S` in B3 and C3** — same blocking defect.
- **(d) says "Brandon is the riskier yielder", which is right on CV but the note leads with the wrong statistic for a grower's actual decision.** Brandon has both the *higher* CV (0.186 vs 0.159) and the *lower* mean (59.6 vs 72.1) — it is worse on both axes, so no risk-return tradeoff exists here and the "riskier" framing undersells the finding. A grower choosing between these two is not trading yield for stability; Manness dominates on this data. The note gets to the right conclusion but frames it as a CV comparison when the mean gap (12.5 bu/ac, 21%) is the larger fact. Expected emphasis: Manness yields more *and* varies less.
- **The sample-size caution in (d) is good and should be kept** — "108 vs 519" is exactly right (108 SY MANNESS rows, 519 Brandon rows), and it is the kind of caveat the rest of the bank does not bother with.
- **Data verified:** column A = the 108 `SY MANNESS` yields, column B = the 519 `AAC BRANDON (BW 932)` yields, both in CSV order. Ranges A2:A109 and B2:B520 are exactly right and correctly differ in length.
- **All quoted figures correct:** means 72.1 / 59.6, CVs 0.16 / 0.19 (0.1594 and 0.1864). SDs are 11.49 and 11.12, i.e. nearly identical in absolute terms — which is the real reason the CVs differ, and the note does not say so. Optional addition: the two varieties have almost the same absolute spread, so the whole CV difference comes from the mean.
- **Colour legend coherent:** cream (a), green (b), blue (c), pink (d) on A6, legend A9:A12 matches.

## Question 20 — `q020.xlsx`

**Verdict: fully correct — the only one of the five with no formula defect. One claim in the note overstates what the data shows.**

- **No `_xlfn.` problem here** — `AVERAGE`, `SUMPRODUCT` and `SUM` are all legacy functions, so this workbook opens clean.
- **(d) claims "the widely grown rows yield a little better than the small ones" — this is weakly supported.** The correlation between `Acres` and `Yield_bu_ac` is only 0.089. The weighted mean does exceed the plain mean (62.58 vs 61.16, a 1.43 bu/ac gap), so the *direction* of the statement is right and it is the correct explanation in kind, but "yield a little better" invites a student to think there is a real acreage-yield relationship when the association is close to nil. Expected: something like "the rows carrying the most acres happen to average slightly higher, so weighting pulls the figure up" — a statement about this particular weighting, not a general tendency. As written it is the most misleading sentence in the five workbooks.
- **Data sheet verified row-by-row:** all 2,398 rows × 7 columns match the CSV exactly, including `Acres` decimals (e.g. 21956.5) and the `Reported` column carried as the text `TRUE`. Full table, as the question requires.
- **(b) SUMPRODUCT is correct and correctly ranged:** `=SUMPRODUCT(Data!$F$2:$F$2399,Data!$E$2:$E$2399)/SUM(Data!$E$2:$E$2399)` — yield in F, acres in E, both over the full 2,398 rows. Recomputes to 62.5833; the note's "62.6" is right, as is "61.2" for the plain average and the claim that weighted is higher.
- **(d)'s main explanation is good.** "It counts every acre once… the plain average counts every row once, so a variety grown on 200 acres in one municipality weighs as much as one grown on 20,000" is the right teaching point and is concretely put.
- **Colour legend coherent:** cream (a), green (b), blue (c) on A4, pink (d) on A5, legend A8:A11 matches.

---

## Cross-cutting

1. **`_xlfn.` prefix (blocking, 4 of 5 workbooks here, 25 bank-wide).** Fix in `practice/build_answers.py` lines 28–31 by dropping the prefix from `QI`, `PI`, `SD`, `VR`, then regenerate. Leave `FT`/`FORMULATEXT` and `XLOOKUP` prefixed — those genuinely require it. Regeneration must not touch the pivot workbooks q071–q100.
2. **No workbook carries cached formula results.** Every formula cell is stored formula-only, so `data_only=True` returns `None` throughout. Excel and the SharePoint embed will both calculate on open, so this is not user-visible — but it does mean the embedded viewer shows blanks until it recalculates, and it means the `_xlfn.` breakage above was never going to surface in a file-level check. Worth writing cached values on the next regeneration.
3. **Neither Data sheet nor Answer sheet uses freeze panes**, so scrolling a 2,398-row Data sheet loses the header. Cosmetic, consistent across all five.
4. **No sheet states the row count or the filter applied.** Q17's two unequal columns are the case where this actually costs the reader something; a `n = 396` / `n = 519` line on each Answer sheet would make the ranges self-checking.
