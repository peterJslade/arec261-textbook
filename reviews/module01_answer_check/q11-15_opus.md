# Module 1 answer-workbook check — Questions 11-15

Checked against `practice/module01_bank.qmd` (Section 2, Saskatchewan RM Crop Yields). Workbooks opened read-only with openpyxl (formulas, fills, number formats, merges); expected values recomputed independently from `practice/data/rm_yields_1990plus.csv` in Python, using Excel conventions (`STDEV.S` = sample sd, `PERCENTILE.INC`/`QUARTILE.INC` = linear interpolation on `(n-1)p`). No files were modified.

Data-sheet verification passed for all five: every Data column matches the correct year/crop filter of the source CSV, in CSV row order, with the right count and identical values (Q11 canola 2023 n=289; Q12 canola 2023 n=289 + barley 2023 n=285; Q13 canola 2019 n=290 and canola 2021 n=290; Q14 oats 2023 n=200; Q15 spring wheat 2024 n=286). Blank CSV cells are genuinely absent rather than zero-filled, so `AVERAGE`/`STDEV.S` skip them correctly.

None of the five workbooks store cached formula results (all `<v>` elements empty), but every one sets `fullCalcOnLoad="1"`, so Excel recalculates on open. Not an issue for Excel or the web viewer; it does mean the numbers quoted in the notes are the only figures a reader sees if the file is parsed rather than opened. All quoted figures were checked against recomputation and are right.

## Question 11 — q011.xlsx: OK

- All four parts present and correct. B1 `=AVERAGE(Data!$A$2:$A$290)` -> 33.881, B2 `=MEDIAN(...)` -> 35.5, B3 `=STDEV.S(...)` -> 13.3346, B4 `=QUARTILE.INC(...,3)-QUARTILE.INC(...,1)` -> 44.9 - 22.6 = 22.3. Ranges cover exactly A2:A290, the full 289 values.
- Note quotes: mean 33.9, median 35.5, gap 1.6 — all match (exact gap 1.619). Skew direction is right: mean below median is left skew / longer left tail, and the note says so.
- Colour-coding and legend coherent: yellow (a) on the mean/median, red (d) on sd/IQR, green (b) and blue (c) on the two merged notes; legend A10:A13 lists (a)-(d) in matching fills.
- Minor, worth noting rather than fixing: part (c) as written in the bank says "using your answers to parts a-d", but the question only has parts (a)-(d) with (d) placed *after* (c). The answer's (c) note leans only on the mean/median, not the sd/IQR it is pointed at. This is a bank-ordering wrinkle, not a workbook error — the answer is defensible as it stands.

## Question 12 — q012.xlsx: barley formula ranges stop one row short of the header block (harmless here, but wrong as written)

- **Barley formulas reference `Data!$B$2:$B$286`, not `$B$2:$B$290`.** Expected: the same row span as the canola column, `$B$2:$B$290`. Found: C2 `=AVERAGE(Data!$B$2:$B$286)` and C3 `=STDEV.S(Data!$B$2:$B$286)`. The barley column happens to have exactly 285 values ending at B286, with B287:B290 empty, so the computed numbers are identical either way (mean 54.5639, sd 24.6032, CV 0.4509) — but the reference is a hand-trimmed range, not the block a student would select. Two problems for a model answer: it silently teaches "shorten the range to where the data stops" rather than "select the column and let Excel skip blanks", and it is inconsistent with the canola column two cells to its left, which a student reading the sheet will notice and be confused by. Recommend `$B$2:$B$290` for both.
- Everything else correct. B2 -> 33.881, B3 -> 13.3346, B4 `=B3/B2` -> 0.3936; C4 `=C3/C2` -> 0.4509. Note figures (24.6, 13.3, 54.6, 33.9, 0.45, 0.39, "about 45%", "about 39%") all match recomputation.
- Part (b) reasoning is correct and is the point of the question: a bigger sd does not by itself establish more meaningful variability when the scale differs. Part (d) correctly names barley on the CV. Part (e) is a fair newspaper sentence.
- Colour-coding coherent, with one inconsistency: **the legend has five entries (a)-(e) but the sheet uses part (a) yellow for both the means and the standard deviations, which is correct, while part (c) blue sits on the CV row and part (d) red sits on the (d) note — so every legend colour is used exactly once except (a). That is fine.** The real wrinkle is that the CV row (blue, part c) and the part (d) note (red) are adjacent and read as if the note explains the blue cells above it. Not wrong, just slightly harder to follow than Q11's layout.
- Q12 also has no explanatory header over the Data sheet columns beyond "Canola 2023"/"Barley 2023" — fine, but note that barley's 4 missing RMs are invisible; a student comparing n=289 to n=285 gets no signal from the sheet that the two columns cover different RM sets. Worth a one-line note in the Answer sheet, since the question is explicitly about comparing the two crops.

## Question 13 — q013.xlsx: OK

- All parts present. Ranges `$A$2:$A$291` and `$B$2:$B$291` both cover exactly the 290 values in each column, with no blanks — consistent between the two years, unlike Q12.
- Recomputed: 2019 mean 40.7831, median 42.1, sd 8.1679, CV 0.2003; 2021 mean 21.8583, median 22.8, sd 8.1445, CV 0.3726. Note quotes "about 8.2" for both sds (correct: 8.168 and 8.145), "barely half" for the 2021 mean (21.86 vs 40.78 — correct), CV 0.37 vs 0.20 (correct).
- Part (c)'s answer is the right one and for the right reason: near-identical absolute spread, very different relative spread, so the CV is what settles it.
- Colour-coding coherent: yellow (a) on mean/median, green (b) on sd/CV, blue (c) on the note; legend A10:A12 matches.

## Question 14 — q014.xlsx: OK

- All parts present. B1 -> 71.136, B2 -> 75.9, B3 `=PERCENTILE.INC(...,0.9)` -> 116.72, B4 `=QUARTILE.INC(...,1)` -> 44.975, B5 -> 96.5, B6 `=B5-B4` -> 51.525. All correct on `.INC` interpolation.
- Note figures: mean 71.1, median 75.9 — correct. Skew call is right (mean below median -> left-skewed, low-yield tail pulling the mean down), and 2023 oats are genuinely left-tailed (min 1.0 against a median of 75.9).
- Part (b)'s plain-language reading of the 90th percentile says "at or below about 117 bu/ac" against a computed 116.72 — correct and correctly hedged. Phrasing "only the top tenth of RMs did better" is the right gloss for `PERCENTILE.INC`.
- Colour-coding and legend (A12:A15) coherent for (a)-(d): yellow (a) on the three part-a statistics, blue (c) on Q1/Q3/IQR, green (b) and red (d) on the notes.

## Question 15 — q015.xlsx: OK, with one loose number in a note

- All parts present. B1 `=PERCENTILE.INC(...,0.1)` -> 25.65, B2 -> 50.3, B3 -> 62.9, B4 `=B3-B1` -> 37.25, B5 `=MAX(...)-MIN(...)` -> 68.1 (max 79.8, min 11.7). All correct.
- **Part (b)'s note says "about 26 bu/ac" where the computed 10th percentile is 25.65.** Rounds to 25.7, or 25.65 exactly; "about 26" is defensible as a rounded gloss but is the only figure in the five workbooks stated less precisely than the sheet computes it, and it will not visibly match the `0.00`-formatted 25.65 in B1 that a student is looking at. Recommend "about 25.7".
- Part (d) note quotes range 68.1 and gap 37.3 (computed 37.25) — correct — and says the range is "almost twice" the gap; the ratio is 1.83, so that holds.
- Part (d) reasoning is sound: the range depends on the two extreme RMs, the 90-10 gap is robust, so the gap is the better spread measure across RMs.
- Colour-coding coherent, but **the legend is slightly out of step with the sheet**: part (d) red is used on both B5 (the range, a part-d computation) and the A8 note, while part (c) blue sits only on B4. That is correct as far as it goes. The confusion is that B4 ("90th minus 10th", part c) and B5 ("Range", part d) are adjacent rows in different colours computing the same kind of quantity — a reader may take the colour change as meaning something statistical rather than a part boundary. Same pattern as Q12; harmless but worth a consistent convention across the section.

## Cross-cutting notes

- Formula spelling: every modern-function formula is stored with the `_xlfn.` prefix (`_xlfn.STDEV.S`, `_xlfn.QUARTILE.INC`, `_xlfn.PERCENTILE.INC`). This is correct OOXML for these functions and Excel displays them as `STDEV.S` etc. Only flagging it so a future script-based check does not misread the prefix as a defect.
- Q12 is the only workbook whose formula ranges differ between two parallel columns. Everything else uses whole-block, fully-anchored references.
- No workbook computes a statistic the question did not ask for, and no question part is unanswered.
