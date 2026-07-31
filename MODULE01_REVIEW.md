# Review: Module 1 — "Describing Data in Excel" (`module01.qmd`)

Reviewed against the companion test bank (`practice/module01_practice.qmd`) and the course context (first module, beginner/international audience, later modules cover probability/regression/inference).

---

## Executive Summary

This is a strong first chapter. The voice is engaging without being flippant (mostly), the sequencing is logical (mechanics → statistics → conditionals → lookups → data shape → PivotTables → charts → worked example), and the statistical content is essentially sound: sample vs. population SD is handled correctly, Bessel's correction is explained at the right depth, the CV's failure mode near zero is a genuinely good inclusion, and the wide-vs-long section is excellent and directly sets up the test bank's PivotTable questions.

The three most important problems:

1. **A correctness error in the percentile-interpolation example** — the "nine values" illustration describes what `QUARTILE.EXC` (or the (n+1) method) does, not what `QUARTILE.INC` does, and the course mandates `.INC`. Students who check the example against Excel will get a contradiction.
2. **A dangerous silence about filters and formulas.** The chapter says filtering "just hides" rows but never warns that `AVERAGE`, `MEDIAN`, `STDEV.S`, etc. **still include hidden rows**. The test bank's entire Type 1 workflow is "filter to 2023, then compute" — a student who follows the chapter literally will compute 1990–2025 statistics and get every answer wrong. This is the single highest-stakes gap.
3. **Several skills the bank tests are not taught**: two-criteria lookups (bank 2A-d, 2B-d), dynamic criteria like `">"&AVERAGE(...)` (bank 2A-e, 2B-e, and the chapter's *own* sample question 4), `COUNT` vs. `COUNTA` and blank-cell behaviour, and — most pedagogically important — the words "left-skewed"/"right-skewed" and the mean-vs-median skew heuristic, which the bank asks about directly (1A-f, 4A) but the chapter only implies.

With those fixed, the chapter prepares students well for the test bank. Nothing here requires restructuring; it is all additive or local.

---

## Correctness Issues

Ordered roughly by importance.

### C1. The nine-value percentile example contradicts `QUARTILE.INC` (§ Measures of Location, ¶2)

> "For example, if we have nine values, then the 25th percentile would lie somewhere between the second and third smallest values. Generally, we would interpolate between these two values."

With the `.INC` method the course tells students to use ("For this course use `.INC`"), the position of the p-th percentile is $1 + (n-1)p = 1 + 8(0.25) = 3$ — **exactly the third-smallest value, no interpolation**. The "between the 2nd and 3rd" answer is what `QUARTILE.EXC` / the $(n+1)p$ textbook method gives ($10 \times 0.25 = 2.5$). A student who tests the example in Excel with `.INC` will see the book is wrong.

**Fix**: either change the example so it interpolates under `.INC` (e.g., "with ten values, the 25th percentile under Excel's `.INC` method lands at position $1 + 9(0.25) = 3.25$, one-quarter of the way from the 3rd to the 4th value"), or soften to "different software uses slightly different interpolation rules; Excel's `.INC` method places the 25th percentile of nine values exactly at the 3rd-smallest value, while other conventions interpolate between the 2nd and 3rd."

### C2. No warning that ordinary formulas ignore filters (§ Sorting and Filtering)

> "Filtering does not delete rows; it just hides them."

True — but the chapter never says the corollary that matters: **`AVERAGE`, `SUM`, `MEDIAN`, `STDEV.S`, `QUARTILE.INC`, etc. include hidden rows.** Filtering to 2023 and then writing `=AVERAGE(E2:E10650)` averages *all* years. The test bank's Type 1 instructions ("first filter the data to that year... or copy the year's rows to a new sheet, then compute") depend on students knowing this pitfall; the bank's answer key even lists the wrong-answer symptom ("you get the 1990–2025 average ≈28.3, not the 2023 average"). The chapter must own this warning.

**Fix**: add 2–3 sentences: filters hide rows from *you*, not from formulas; to compute statistics on a filtered subset, either (a) copy the visible rows to a new sheet and compute there (the recommended workflow for this course), or (b) use `SUBTOTAL`/`AGGREGATE`, which respect filters (optional mention). Repeat the warning in the Worked Example, which currently sidesteps it only by luck (the whole 200-row dataset is one year).

### C3. "z-scores (which you will meet in AREC 262)" (§ Standard Deviation, last ¶)

The project's course plan (CLAUDE.md) places z-scores and t-tests in **Module 12 of AREC 261** ("formal inference (z-scores, t-tests)"), while `module12.qmd` as written is bootstrap-focused and defers the classical $\bar{x} \pm 1.96 \cdot SE$ machinery to AREC 262. So the sentence matches the current Module 12 draft but contradicts the course plan. One of the two is stale.

**Fix**: decide where z-scores actually live and make this pointer (and Module 12) consistent. The `@sec-module12` reference for confidence intervals is correct as-is (verified: `module12.qmd` covers bootstrap CIs).

### C4. Variance described as "the average of the squared deviations" but the formula divides by n−1 (§ Variance)

> "The **variance** is the average of the squared deviations from the mean."

Immediately followed by a formula with $\frac{1}{n-1}$. Dividing by $n-1$ is not an average of $n$ things. The chapter does explain Bessel's correction two paragraphs later, but the opening definition is literally inconsistent with the displayed formula, and sharp students notice.

**Fix**: "The variance is (roughly) the average of the squared deviations from the mean — with one small adjustment to the denominator that we explain below."

### C5. `.xlsx` bullet implies it can contain macros (§ File Formats)

> "**`.xlsx`** — ... Can contain multiple worksheets, formulas, formatting, charts, PivotTables, macros (in `.xlsm`)."

`.xlsx` files **cannot** contain macros; that is the entire point of the `.xlsm` distinction. The parenthetical is doing the right work but the sentence structure puts "macros" inside the `.xlsx` capability list.

**Fix**: "...charts, and PivotTables. (A variant, `.xlsm`, additionally allows macros.)"

### C6. `2026-09-15` listed as an example of *text* (§ Cells, References, and Formulas)

> "- Text: `Canola`, `2026-09-15`, `North field`
> - A date (internally stored as a number): `2026-09-15`"

The same string appears as both a text example and a date example. If you type `2026-09-15` into Excel it is parsed as a date, not text — so it is a misleading example of text, and having it in both bullets will confuse beginners.

**Fix**: drop it from the text bullet (use `Field 7` or `N/A` instead) and keep it under dates. Optionally add the genuinely useful nuance: text can be *forced* with a leading apostrophe (`'2026-09-15`).

### C7. Nested-IF boundary description is imprecise (§ The IF Function)

> "`=IF(B2<40, "Low", IF(B2<60, "Medium", "High"))` ... labels values under 40 as "Low", values from 40 to 59 as "Medium", and 60+ as "High"."

For non-integer data (yields are non-integer), `B2 = 59.5` is "Medium," so "from 40 to 59" is wrong; the true interval is $[40, 60)$.

**Fix**: "values from 40 up to (but not including) 60 as 'Medium'."

### C8. Excel's Box & Whisker defaults differ from `QUARTILE.INC` (§ Box and Whisker Plots)

The description of the box plot (median, Q1/Q3, 1.5×IQR whiskers, outlier dots) is correct as a general convention. But two Excel-specific behaviours are worth a sentence because students will cross-check the chart against their `QUARTILE.INC` formulas:

- Excel's Box & Whisker chart uses the **exclusive** median calculation by default (right-click the series → Format Data Series → "Inclusive median" to match `QUARTILE.INC`), so the box edges may not equal the students' computed Q1/Q3.
- Excel also displays the **mean as an "×" marker** by default — students will ask what it is.

**Fix**: add a short "In Excel specifically..." note covering both.

### C9. Minor definitional nuance on percentiles (§ Measures of Location)

> "The **$p$-th percentile** is the value below which $p\%$ of the observations fall."

Fine as a first-week definition, but strictly no single value satisfies it for most datasets (hence interpolation), and "at or below" is the more defensible phrasing. Low priority — a parenthetical "(approximately — see below)" is enough, and it dovetails with the C1 fix.

### C10. Windows-only keyboard shortcuts stated as universal (§ References; § Sorting and Filtering)

`F4` (cycle reference types) and `Ctrl+Shift+L` (toggle filters) are Windows shortcuts. On Mac Excel these are **⌘T** (or fn+F4) and **⌘⇧F**. A material fraction of students will be on Macs.

**Fix**: give both, e.g. "`F4` on Windows, `⌘T` on Mac."

### What checks out (verified, no action needed)

- Mean/median/mode definitions, formulas, and Excel functions (`AVERAGE`, `MEDIAN`, `MODE.SNGL`/`MODE.MULT`).
- $s^2$ with $n-1$; `VAR.S`/`VAR.P`, `STDEV.S`/`STDEV.P` and the guidance to default to `.S`.
- `PERCENTILE.INC(range, 0.9)` for the 90th percentile; quartile naming; IQR $= Q_3 - Q_1$; IQR's outlier-robustness vs. the range.
- CV $= s/\bar{x}$, the "CV of 0.1 means SD is 10% of the mean" reading, and the near-zero-mean failure mode (a genuinely good caveat).
- `IF`/`IFS` syntax including the `TRUE` catch-all; `COUNTIF`/`SUMIF`/`AVERAGEIF` argument orders; the correct observation that the sum range moves to the *front* in `SUMIFS`/`AVERAGEIFS`.
- `VLOOKUP` semantics: first-column-only search, the `TRUE` default and its dangers, exact-match advice; `XLOOKUP` signature and `if_not_found`; `INDEX`/`MATCH` pattern.
- 1.5×IQR whisker convention; y-axis-at-zero rule for bars; ~8% red-green colour-blindness in men; √n bin rule of thumb; named-range rules.
- Cross-references `@sec-module3`, `@sec-module12`, `@sec-percentiles`, `@sec-charts` all resolve (verified against the module files).

---

## Scope Problems

The chapter is disciplined overall — no reliance on the normal distribution, probability, sampling, or significance. Remaining items:

1. **"regressions"** (§ Workbook Structure, analysis-sheet bullet: "Summary statistics, pivot tables, regressions"). Regression is Module 6. Harmless as a word, but a week-1 student doesn't know it; either cut it or say "and later, regressions."
2. **z-scores / confidence intervals pointer** (§ Standard Deviation). Forward *pointers* are fine pedagogy and the chapter doesn't rely on them — but see C3 for the wrong-course attribution.
3. **"bimodal"** (§ Histograms: "roughly symmetric, skewed, bimodal, or has outliers"). Used without definition. Since the bank asks students to describe histogram shape, this vocabulary belongs *in this module* — define it in one clause ("bimodal — two separate humps") rather than removing it. Same for skew direction (see G4 below).
4. **"join with other tables"** (§ What Is Excel, Really?). "Join" is database jargon; fine, but a parenthetical "(combine, as we do with lookups later in this module)" would help beginners and internationals.

No forward-reference is load-bearing; scope discipline is a strength of this chapter.

---

## Clarity / Accessibility Issues

1. **The CV wheat/barley example is garbled** (§ Coefficient of Variation): "average wheat and barley yields are very different, so we would expect barley to be more variable in absolute terms" — the reader hasn't been told which crop yields more, so "so" doesn't follow; and the punchline ("wheat yields are more variable than barley yields even if the absolute standard deviation of wheat is smaller") asks the reader to juggle two hypothetical inequalities with no numbers. **Fix**: use concrete numbers, e.g. "Barley: mean 55 bu/ac, SD 11 (CV = 0.20). Wheat: mean 40 bu/ac, SD 10 (CV = 0.25). Wheat's SD is *smaller* in absolute terms, but relative to its mean, wheat is *more* variable."
2. **"Just for you" structure contradiction** (§ Workbook Structure): "Here is a structure I recommend for a workbooks that are just for you" — but the five-sheet structure that follows (README "gift to future-you," outputs "formatted for presentation") is explicitly what the preceding audience discussion says you *don't* need for scratch work, and the closing paragraph says it's "the minimum" for "anything you will hand to someone else." The intro sentence contradicts the section. **Fix**: "Here is a structure I recommend for any workbook that will be shared or revisited" (also fixes the "a workbooks" grammar error).
3. **Elon Musk example says "income" but means wealth** (§ Median): "the average income of the customers is \$100,000. Elon Musk walks in. The average income is now \$500 million." For the arithmetic to work, this is a wealth/net-worth example (the classic version uses Bill Gates and wealth). Using "income" invites a numerate student to object. **Fix**: change to "wealth," or scale the numbers to plausible incomes.
4. **"because Microsoft hates you"** (§ COUNTIF/SUMIF/AVERAGEIF): funny, but in a required textbook read by international students it can land as confusing or unprofessional. Stylistic call — flagging, not insisting. ("...for historical reasons — an inconsistency you just have to memorize" keeps the sympathy without the snark.)
5. **"killer app," "chart junk," "small multiples," "RM"**: "killer app" and "small-multiples" are idioms/jargon worth one defining clause each for international students. "RM" appears in the wide/long tables with no expansion — Saskatchewan students may know "Rural Municipality," but internationals will not. Define at first use.
6. **"eight separate columns" vs. the four-column example table** (§ Wide vs. Long): "the crops are eight separate columns, so 'crop' isn't a field you can drag anywhere" — but the wide table shown in the chapter has four crop columns (the *full dataset* has eight). Either show all eight, or say "the crops are separate columns (four here, eight in the full file)."
7. **`MODE.MULT` needs a version note** (§ Mode): it spills multiple results only in modern (dynamic-array) Excel; in older Excel it required Ctrl+Shift+Enter. One clause avoids confusion in the lab.
8. **XLOOKUP's exact-match default is worth stating** (§ XLOOKUP): after warning at length that `VLOOKUP` defaults to approximate match, the chapter never mentions that `XLOOKUP` defaults to *exact* match — a strong point in XLOOKUP's favour and one less thing to memorize. One sentence.

---

## Coverage Gaps vs. the Test Bank

The bank's four types are: (1) descriptive stats + interpretation, (2) conditional functions + lookups, (3) PivotTables with wide/long logic, (4) charts with interpretation. Gaps, worst first:

- **G1. Two-criteria lookups — not taught at all.** Bank 2A-d and 2B-d require looking up a value by RM *and* Year, with answer-key formulas like `=XLOOKUP(1&"|"&2023, B2:B10650&"|"&A2:A10650, E2:E10650)`. The chapter teaches only single-criterion lookups. The concatenated-key technique (and why the `"|"` separator prevents false matches like `11&2` vs `1&12`) needs a subsection under Lookup Functions, or the bank questions need a hint-box that teaches it.
- **G2. Dynamic criteria (`">"&AVERAGE(...)`) — not taught, but tested twice and used in the chapter's own sample test.** Chapter sample question 4 ("count how many values in `A2:A100` are greater than the mean of `A2:A100`") and bank 2B-e require `=COUNTIF(range, ">"&AVERAGE(range))`. The `&` operator is in the operator table, but building a criterion string is a non-obvious leap. Add an example in the COUNTIF section.
- **G3. Filter-then-compute workflow** — see C2. The bank's Type 1 instructions assume it; the chapter must teach it.
- **G4. Skew direction and the mean-vs-median heuristic — implied, never stated.** Bank 1A-f asks "Is the mean or the median higher? What does this tell you about the shape?" and the key answers "median > mean ⇒ left (negative) skew." Bank 4A asks students to classify a histogram as left- or right-skewed. The chapter's farm-income discussion *implies* mean-above-median-under-right-skew, but never defines "right-skewed"/"left-skewed" or states the heuristic (or its caveats — it's a rule of thumb, not a law). Add a short "Shape of a distribution" passage (natural home: end of the Median section or the Histogram section), with a small labelled sketch if possible.
- **G5. `COUNT` vs. `COUNTA` and blank-cell behaviour — not taught.** Bank 1B-e and 2B-a hinge on `COUNT` skipping blanks; the key warns against `COUNTA` and against filling blanks with 0 (which corrupts `AVERAGE`). The chapter never mentions `COUNT`, `COUNTA`, or that `AVERAGE`/`STDEV.S` skip blanks but include zeros. Two short paragraphs; also relevant to real agricultural data (unreported crops).
- **G6. Units awareness in comparisons.** Bank Type 3 is built around the lentils-in-lb/ac trap ("check units before comparing"). The chapter never raises units as a comparison hazard. One sentence in the PivotTable or worked-example section ("before comparing categories, confirm they share a unit") would plant the seed.
- **G7. Chart titles and axis labels — demanded by the bank, not demonstrated by the chapter.** Every Type 4 question requires "a descriptive title, labelled axes." The chapter's principles cover direct labeling and clutter but never say "always add a title and axis labels" nor show *how* in Excel (Chart Design → Add Chart Element). Given that presentation is graded, add it to the Principles list and to the worked example (Step 4 sets a title but no axis labels).
- **G8. The 1.5×IQR rule is only a parenthetical.** The bank asks students to spot outliers on histograms and box plots. The chapter states the convention in one clause but never shows a computation (fences at $Q_1 - 1.5\,\text{IQR}$ and $Q_3 + 1.5\,\text{IQR}$). A two-line worked computation in the box-plot section would secure it.

Adequately covered (no action): quartiles/percentile formulas, sample SD and variance units (bank 1B-b matches the chapter's "squared units" discussion), `AVERAGEIF`/`COUNTIFS`, wide-vs-long reasoning ("a PivotTable can only group by a field that lives in its own column" is exactly the sentence the bank leans on), PivotTable mechanics and aggregation switching, histogram binning, box-plot comparison across categories, pie-chart critique (sample question 7).

---

## Pedagogical Notes

- **Ordering is sound.** Mechanics before statistics, references before conditionals, conditionals before lookups, wide/long immediately before PivotTables (this placement is the chapter's best structural decision — it makes the bank's Type 3 questions teachable). No concept is used before it is introduced, with the trivial exceptions in the Scope section.
- **The audience-first framing (§ Workbook Structure) is excellent** and unusual for an intro text; keep it. Fix only the "just for you" contradiction (Clarity 2).
- **The worked example is the right capstone** and mirrors the bank's task types almost one-to-one. Two improvements: (a) show a 5-row preview of the dataset so `E2:E201` means something; (b) since the bank's real data is multi-year, add a step that filters/copies a subset — which would also motivate the C2 fix.
- **The "Test Bank Sample" section slightly under-represents the real bank.** It has no wide-vs-long question and no interpretation question of the "is the mean or median higher, and what does that tell you" form, both of which the bank emphasizes. Consider swapping one in.
- **Practice Exercises still say "[TBD dataset]" twice** even though the bank now ships real files (`rm_yields_1990plus.csv`, `rm_yields_1990plus_long.csv`). Link them.
- **Learning objective 7 omits pie charts**, which the chapter then teaches (mostly to warn against them). Either add "and understand why pie charts are usually a poor choice" to the objective or leave as-is deliberately.
- Redundancy is minimal; the mean/median farm-income motif recurs three times (mean section, median section, practice exercise 2), which reads as deliberate reinforcement rather than repetition. Fine.

---

## Writing / Formatting Nits

1. § Workbook Structure: "a structure I recommend for **a workbooks** that are just for you" — grammar (see Clarity 2 for the substantive fix).
2. § Median: "**To returen** to our previous example" → "To return".
3. § Median: '"what a typical farm earns?"' — the quoted phrase is not a question as embedded; drop the question mark or rephrase: 'a more honest answer to "what does a typical farm earn?"'.
4. § Workbook Structure: stray double blank line after the opening paragraph (line ~54); § Mode and § IQR each have doubled blank lines before the next heading. Cosmetic.
5. § Coefficient of Variation: raw `--` used as a dash ("in other contexts -- particularly...") while the rest of the chapter uses `—`. Quarto's smart punctuation will render it, but make it consistent.
6. Trailing double spaces at several line ends (e.g., end of the mean paragraph, the quartile-interpolation paragraph, README bullet). Harmless in HTML output; tidy if convenient.
7. No residual LaTeX artifacts found (`\emph{}`, stray `\%` — none present; the `\$` escapes in the Musk paragraph are correct and necessary). All `$...$`/`$$...$$` math is well-formed. All four cross-references resolve. Markdown tables are well-formed.
8. § Named Ranges: "to the left of the formula bar" — correct; no issue (checked deliberately since UI descriptions often rot).

---

## Prioritized Fix List

1. **Add the filters-don't-affect-formulas warning** (§ Sorting and Filtering + worked example) and the copy-to-new-sheet workflow. Without it, the bank's Type 1 workflow produces wrong answers for students who follow the chapter literally. (C2/G3)
2. **Fix the nine-value percentile example** to match `QUARTILE.INC`, or explicitly contrast interpolation methods. It is currently checkably wrong under the course's mandated function. (C1)
3. **Teach the two-criteria lookup** (concatenated-key `XLOOKUP` / `INDEX`+`MATCH`) — the bank tests it in both Type 2 variants and the chapter never mentions it. (G1)
4. **Add a "shape of a distribution" passage** defining left/right skew and the mean-vs-median heuristic (with its rule-of-thumb caveat) — asked verbatim in bank 1A-f and 4A. (G4)
5. **Teach `">"&AVERAGE(...)` dynamic criteria** in the COUNTIF section — needed for the chapter's own sample question 4 and two bank questions. (G2)
6. **Teach `COUNT` vs. `COUNTA` and blank-handling** (blanks skipped, zeros not; never fill blanks with 0). (G5)
7. **Resolve the z-score attribution** (AREC 262 vs. Module 12) consistently with the course plan. (C3)
8. **Add explicit "title + axis labels, and here's how" guidance** to the chart principles and worked example; add a 1.5×IQR fence computation to the box-plot section. (G7, G8)
9. **Fix the local errors**: `.xlsx`/macros parenthetical (C5), `2026-09-15`-as-text example (C6), "average of squared deviations" wording (C4), "40 to 59" boundary (C7), Mac shortcut equivalents (C10), Excel box-plot inclusive/exclusive-median note (C8).
10. **Clarity pass**: rewrite the CV example with concrete numbers, fix the "just for you" framing, change Musk "income" to "wealth", define RM/bimodal/killer app at first use, reconcile "eight columns" with the four-column example table.
11. **Housekeeping**: replace the two "[TBD dataset]" placeholders with links to the shipped `rm_yields` files; fix the typos ("returen", "a workbooks"); add a units-awareness sentence near PivotTables. (G6)
