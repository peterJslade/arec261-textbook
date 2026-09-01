# Re-audit — Module 1 bank + chapter (verification pass)

**VERDICT: All fixes confirmed correct. 0 errors remaining. 1 trivial wording nit (Q75, optional).**

All values below were recomputed in Python (pandas/numpy, Excel conventions: ddof=1, linear/INC percentiles, blanks skipped) against the three CSVs in `practice/data/`.

## 1. Fixes confirmed (Priority 1)

- ✅ **Q8** — canola all-years mean 28.29, **median 26.90** (fixed); pooled SD **10.06**, which falls **between** 1995 within-year SD (4.48) and 2023 within-year SD (13.33), exactly as the answer now states. (d) 1995 ≈ 19.2 vs 2020 ≈ 38.2 also verified.
- ✅ **Q28** — statcan blank-yield rows = **66 exactly** (was 185). Blanks concentrate in **Mixed grains (21)** and **Rye (15)**, and in **NL (17), NB (14), PEI (11)**. Flax has **0** blanks. All match the answer.
- ✅ **Q63 / Q69 / Q100** — drop-vs-level distinction is correct and correctly worded in all three. Canola: sharpest one-year drop is into **2021** (38.2 → 21.9, −16.4); lowest *level* is **2002 at 15.83** (answer's "~16" ✓). Barley: sharpest drop also into **2021** (68.3 → 34.8, answer's "~68 to ~35" ✓); barley's lowest level is 2002 at 30.64. Q63's parenthetical note and Q100's are both accurate; Q69(c)'s cross-reference to Q63 ("same year — 2021") is correct.
- ✅ **Q101** — unfiltered highest average = **AAC WESTKING, 79.2 on n=17** ✓; top among ≥30 reports = **SY MANNESS, 72.1 (n=108)** ✓; most-reported = **AAC BRANDON (BW 932), n=519, mean 59.6** ✓.
- ✅ **Q46 & Q54** — both now say a lookup onto an empty/suppressed cell returns **0**, which is correct Excel behaviour, and the two questions use the same framing. Q46(a) lookup value 65.1 ✓ (AAC BRANDON / ALONSA / 2020). All 2,960 Reported=FALSE rows have blank yields, so Q46(b) works as written. Q54: MB canola 2023 yield **44.6**, seeded acres **3,128,200** ✓.
- ✅ **Q13(e)** — SK 2021 canola CV = **0.373 ≈ 0.37** (fixed from 0.39). MB 2021 CV 0.246 and 2023 CV 0.184 in parts (a)-(d) also verified.
- ✅ **Q71** — low-end outliers by 1.5×IQR = **35 exactly** (was 39). Lower fence = 30.35 (answer's "≈ 30.4" ✓); Q1 53.9, Q3 69.6, IQR 15.7. Part (b)'s mean 61.2 / median 62.2 ✓.
- ✅ **Q72** — three named varieties verified: AAC BRANDON IQR 13.0, AAC REDBERRY IQR 12.98 ("both ≈ 13" ✓), AAC STARBUCK IQR 14.38 ("≈ 14" ✓). Part (c)'s "Brandon and Redberry tighter than Starbuck" is right, and the "credit any correct reading" hedge covers the Brandon/Redberry near-tie.
- ✅ **Q93** — Crop×Year pivot (Unit = bu/ac filter correctly excludes lb/ac lentils): Oats 89.42→97.47 (+8.05), Barley 68.59→72.84 (+4.25), Canola 40.78→43.94 (+3.16). **Oats** is indeed the largest absolute riser among bu/ac crops ✓.
- ✅ **Q109** — with the "≥30 reports, ranked by average" spec, **SY MANNESS (72.1)** is legitimately the tallest bar; shortest among well-reported ≈ AAC Tisdale (53.9) / AAC Redberry (54.4) ✓. Consistent with Q75 (which uses the *six most-reported* varieties — SY MANNESS, n=108, is not among them, so no contradiction) and with Q107's identical Tisdale/Redberry figures.

## 2. New issues introduced (Priority 2)

**None found.** Specifically checked:

- Structural scan: all 120 questions have exactly parts (a)-(e), one `<details>` answer block, and five matching answer bullets. No dangling text or broken sentences detected in the edited regions.
- Cross-references all consistent: Q63↔Q69 (both 2021 sharpest drop), Q75↔Q109 (different selection rules, no conflict), Q46↔Q54 (same returns-0 framing), Q82↔Q89↔Q90 (statcan 2021 low: national canola 34.2, barley 56.1, SK canola 25.8 — all 2021 ✓), Q71(c)↔Q61 (Q61 is 2023-only canola: mean 33.88 < median 35.5, genuinely left-skewed, so "left-skewed and wider" stands), Q14(c)↔Q11, Q11(d)/Q12 "0.39" references are the *2023* canola CV (0.394 ✓) — distinct from the fixed 2021 figure, not stale text.
- Other "lowest year" answers are all span-restricted and correct: Q31 (2010/2019/2021), Q76 (MB 2021 low 49.6 vs 2020's 62.4), Q97 (2019–2023 grid: canola low 2021 at 21.9, barley same), Q98 (oats 2019–2025: high 2025 at 97.5, low 2021 at 45.1), Q91 (2023 crop ranking: Lentils 1314 lb/ac artifact, Oats 71.1, Flax 20.3 — all match), Q30 (2023 barley: MB 75.4 high, QC 46.1 low ✓).
- **One trivial nit (optional):** Q75(b) answer reads "Tallest ≈ AAC Wheatland/Hockley (~66–67 median area)". Actual means: Wheatland 65.8 (tallest), Hockley 64.9. The identification is right but "~66–67" slightly overstates and "median area" is odd phrasing for a bar-of-means chart. Suggested: "Tallest ≈ AAC Wheatland (~66; Hockley close behind at ~65); shortest ≈ AAC Redberry (~54)." Not a factual error requiring a fix.

## 3. Chapter new-passage checks (module01.qmd)

- ✅ Filter warning (lines ~405–414): correct — ordinary functions (AVERAGE, SUM, MEDIAN, STDEV.S, QUARTILE.INC) ignore filters; SUBTOTAL/AGGREGATE are correctly named as the exceptions; copy-visible-rows workflow is accurate (Excel copies only visible cells from a filtered range).
- ✅ QUARTILE.INC/percentile passage (line ~199): position formula 1+(n−1)p is correct; for n=10, p=0.25 → 1+9×0.25 = **3.25** ✓, interpolation description accurate.
- ✅ Two-key lookup (lines ~374–392): the "|" separator example is correct, and the collision illustration is right — (1, 12) and (11, 2) both concatenate to "112" without a separator.
- ✅ `">"&AVERAGE(...)` dynamic-criterion passage (lines ~318–321): correct.
- ✅ COUNT vs COUNTA (lines ~323–328): correct (COUNT = numbers only; COUNTA = any non-empty), and the blanks-are-not-zero warning is accurate.
- ✅ 1.5×IQR fence example (line ~565): Q1=40, Q3=60, IQR=20 → fences 40−30=**10** and 60+30=**90** ✓; the "wide box pushes fences out" caveat is statistically sound.
- ✅ CV example (line ~264): barley 11/55 = **0.20**, wheat 10/40 = **0.25** ✓; interpretation correct.
- ✅ Excel box-plot quirks (line ~569): Excel's Box & Whisker does default to the *exclusive* median method, and the "×" marker is the mean — both claims correct.

## 4. Priority-3 confirmations

- ✅ **No agronomy prerequisite**: contextual facts needed for answers (e.g., "2021 was a drought year") are stated within the questions themselves; everything else is computable from the CSVs.
- ✅ **Vocabulary**: no occurrences of "bimodal", "normal distribution", "correlation", "regression", "probability", or "sampling" anywhere in the bank.
- ✅ **Numbering**: clean 1–120, sequential, no gaps or duplicates; 120 `<details>` answer blocks.
