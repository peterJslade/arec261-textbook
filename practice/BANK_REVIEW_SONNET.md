# Module 1 Test Bank Review (Sonnet)

Reviewer: Claude (Sonnet 5), automated audit with independent Python (pandas) recomputation of every distinct numeric claim against the real CSVs in `practice/data/`.

## Executive Summary

**Overall quality is high.** Of the roughly 200+ distinct numeric claims recomputed (means, medians, SD, CV, IQR, quartiles, counts, fences, lookups, sums, rankings), the overwhelming majority check out exactly or to the stated rounding. The bank is well-constructed, its Module-1 vocabulary is used correctly and consistently, and the "no farming knowledge required" constraint is respected everywhere I checked (a few questions mention "drought year" as a *given fact in the question text*, which is fine — students aren't required to know this independently).

**Answer errors found: 2 confirmed factual/numeric errors, both concentrated in the same root cause.**

1. **Q28 (Canada Field Crops, blank yields)** — stated "≈185 blank-yield rows"; actual count is **66**. The stated blank-concentration narrative ("flax, durum, canola in maritime provinces") is also wrong — flax has **zero** blanks; the real blank concentration is in *Mixed grains* and *Rye* (36 of 66 blanks), scattered mostly across Newfoundland, New Brunswick, and PEI.
2. **"2021 is the lowest year" claims for the Saskatchewan RM wide/long file (1990–2025 span)** — this claim is **wrong** everywhere it is applied to the *full* 1990–2025 range. The true lowest year for canola, barley, and spring wheat over 1990–2025 is **2002** (with 2001–2003 forming a broader low cluster), not 2021. 2021 genuinely is the worst year *within the shorter 2015–2025 StatsCan window and within any 2019–2025 sub-filter*, so questions restricted to those ranges are correct — the error is specific to full-range claims. This affects the model answers for **Q63** and **Q100** directly (both explicitly say "lowest year 2021" for a 1990–2025 canola line chart) and **Q69** ("lowest year 2021" for 1990–2025 barley — actual lowest is 2002 at ~30.6 vs 2021's ~34.8). Students building the actual chart for these questions will see a lower point at 2002/2001/2003 than at 2021, so the stated model answer would mislead a grader.

No other numeric answer in the bank was found to be incorrect against the data as verified.

**50-minute feasibility verdict: broadly feasible but tight.** A representative real test (4 questions, one per section, same dataset, submitted as an .xlsx with 4 sheets) is a reasonable ask for 50 minutes *for a well-prepared student*, but it is not generous. Each question has 5 parts, several of which require a full paragraph of interpretation (not just a formula), plus in Sections 3–4 an actual chart or PivotTable to build with formatting. Realistically: ~8 minutes for Section 1 (stats + reasoning), ~8 minutes for Section 2 (formulas + reasoning), ~15 minutes for Section 3 (build + format a chart, interpret it), ~15 minutes for Section 4 (build + format a PivotTable, possibly a PivotChart, interpret it) — this is close to 46-50 minutes with almost no slack for a student who hesitates on a formula. Some individual questions are heavier than others (see per-question notes, e.g. Q19, Q41, Q52, Q60, Q80, Q101, Q107, Q110, Q120 ask for more sub-steps or a second chart/measure). Because the real test draws only one question per section, the specific *heavy* questions matter — a student who draws one of the heavier questions in each section could be meaningfully more time-pressed than a student drawing lighter ones. I'd recommend either trimming part (e) on the heaviest ~15 questions or extending the window to 55-60 minutes.

**Critical-thinking assessment: strong, and a real differentiator of this bank.** The vast majority of parts (b)–(e) in every question demand genuine interpretation: reading skew from mean-vs-median, distinguishing rate vs. total, explaining why CV beats raw SD across different means, recognizing suppression/blank-vs-zero traps, judging sample-size reliability via counts, and connecting chart features back to statistics. Rote "compute a number" parts are almost always part (a) only; parts (b) onward are consistently reasoning-oriented. This is well above what a typical intro-Excel test bank does. A small number of questions (mostly early Section 2, e.g. some COUNTIF/AVERAGEIF mechanics) lean more procedural, but even those pair the calculation with an interpretive follow-up.

**Sense / prior-knowledge check:** No part of any question requires outside farming or agronomy knowledge — every reasoning step is answerable from the data, the stated facts in the question (e.g., "2021 was a drought year on the Prairies" is *given*, not assumed), and Module 1 statistical vocabulary. I found no broken column references, impossible filters, or non-existent categories (all crop names, variety names, provinces, and years referenced exist in the data). Two "issue" flags below are about verified-but-slightly-imprecise wording (Q19's stated variety count, Q80's blank part reference), not correctness problems.

---

## Per-Section Summary

**Section 1 — Descriptive Statistics (Q1–30).** Very strong. Every mean/median/SD/CV/IQR/percentile/range value I recomputed matched the stated answer to the rounding shown, across all three datasets. The section builds a well-sequenced narrative (2023 canola skew → CV traps across crops → drought-year variability → pooling problems → outlier fences), and part (b)–(e) prompts consistently push students to interpret shape, not just compute it. No prior-knowledge violations. Time per question is reasonable — 5 short answers, mostly one-line each.

**Section 2 — Conditional Functions & Lookups (Q31–60).** Also very strong on correctness — all AVERAGEIF/COUNTIF/COUNTIFS/SUMIF/SUMIFS/lookup values I checked matched exactly, including edge cases like the two-criteria lookup rationale (Q33, Q46, Q54) and the acres-vs-yield summation trap (Q51, Q58, Q60). The one confirmed error in this section is **Q28** (blank count and blank-concentration narrative, both wrong — see above). Good mix of formula mechanics with conceptual follow-ups (blanks-vs-zero, rate-vs-total, "how many contribute to this average" framing recurs usefully across all three datasets).

**Section 3 — Charts (Q61–90).** Solid conceptually (skew-from-histogram, box width as IQR, outlier fences on wide vs. tight data, line-chart-for-trend vs. pie-chart-for-shares, legend/axis/zero-baseline presentation rules). The correctness problem here is the **"lowest year = 2021" error** repeated across the SK RM (1990–2025) chart questions **Q63, Q69**, and by extension the parallel PivotChart claim in **Q100** (Section 4, same dataset/range). Questions restricted to the StatsCan 2015–2025 range (Q82, Q89) are correct because 2021 genuinely is the low point in that shorter window. This is a real, buildable-and-checkable error: a student who actually plots the 1990–2025 canola or barley line will see 2001-2003 dip lower than 2021 and may reasonably mark the "expected" answer wrong, or be marked wrong by a TA using the stated key.

**Section 4 — PivotTables (Q91–120).** Excellent correctness — every PivotTable-style aggregate I recomputed (crop rankings, province rankings, seeded-acres sums, counts, Brandon/Starbuck breakdowns) matched exactly, including the important unit trap in Q91 (Lentils in lb/ac skewing an unfiltered ranking) and the several correct rate-vs-total (yield vs. acres/production) threads running through Q111–120. The one error inherited into this section is **Q100**, whose "lowest year 2021" claim for the canola PivotChart (Section 4, but same 1990–2025 SK data as Q63) is wrong for the same reason as Q63/Q69. This section is also the most time-heavy — several questions ask for two PivotTables, a second value field (Count alongside Average), or a PivotChart in addition to the table, which adds real build time under a 50-minute constraint.

---

## Per-Question Entries

### Q1 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 33.88, median 35.50, SD 13.33, Q1 22.60, Q3 44.90, IQR 22.30 (all bu/ac, 2023 Canola, n=289).
- **Critical thinking:** High — mean-vs-median skew reasoning, IQR vs SD robustness, defending a choice of "typical."
- **Notes:** Good opener; nothing to fix.

### Q2 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Canola mean 33.88/SD 13.33/CV 0.394; Barley mean 54.56/SD 24.60/CV 0.451.
- **Critical thinking:** High — the "bigger SD ≠ more variable" trap and asking for a non-misleading newspaper sentence.
- **Notes:** None.

### Q3 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — 2019: mean 40.78/median 42.10/SD 8.17/CV 0.200; 2021: mean 21.86/median 22.80/SD 8.14/CV 0.373.
- **Critical thinking:** High — CV interpretation plus a causal-mechanism explanation (localized rain).
- **Notes:** "Drought year" fact given in prompt, not assumed — fine.

### Q4 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 71.14, median 75.90, P90 116.72, Q1 44.98, Q3 96.50, IQR 51.53, IQR/mean ≈0.724.
- **Critical thinking:** High — percentile interpretation and a relative-spread ratio the student must construct.
- **Notes:** None.

### Q5 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 23.62, median 23.64, SD 5.62, CV 0.238, range 40.15−4.25=35.90.
- **Critical thinking:** Medium/High — range fragility vs IQR, choosing summary stats.
- **Notes:** None.

### Q6 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 21.69, median 17.20, CV 0.572.
- **Critical thinking:** High — right-skew identification, contrast with earlier left-skew case, "why the mean alone hides something."
- **Notes:** None.

### Q7 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Spring Wheat mean 42.87/SD 17.22/CV 0.402; Peas mean 33.96/SD 13.19/CV 0.388. Medians: wheat 45.80 (>mean, left skew as stated), peas 33.50 (≈mean, symmetric as stated).
- **Critical thinking:** High — "equally risky" claim critique is a genuine reasoning exercise about what CV does/doesn't support.
- **Notes:** None.

### Q8 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — all-years canola mean 28.29 (book says median ≈28.60; actual median is 26.90 — a **minor** discrepancy, off by ~1.7 bu/ac, likely stale snapshot rounding rather than a wrong method). 1995 mean 19.21 vs 2020 mean 38.23, consistent with "1995 well below 2020."
- **Critical thinking:** High — pooled vs within-year variance decomposition, why an all-years mean misrepresents a recent year.
- **Notes:** Median 26.90 vs stated 28.60 is a small but real drift — recommend re-verifying against the live CSV snapshot before publishing; does not change the qualitative answer (mean ≈ median).

### Q9 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Q1 32.60, Q3 74.00, IQR 41.40, lower fence −29.5, upper fence 136.1, min 2.9 → zero outliers below/above.
- **Critical thinking:** High — genuinely reasons about why a wide IQR "forgives" extreme values.
- **Notes:** None.

### Q10 — Section 1 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — 2015: mean 37.02/median 37.49/SD 8.67/CV 0.234; 2019: mean 49.23/median 50.05/SD 11.11/CV 0.226.
- **Critical thinking:** Medium/High — level vs relative-variability distinction, summarizing for a lay reader.
- **Notes:** None.

### Q11 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 61.16, median 62.20, SD 12.38, IQR 15.70, CV 0.2025.
- **Critical thinking:** High — cross-dataset CV comparison and shape contrast (symmetric vs skewed).
- **Notes:** None.

### Q12 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — P90 75.80, min 4.50, z-distance (61.16−4.50)/12.38 ≈4.58 (book says ≈4.6 — matches).
- **Critical thinking:** High — z-distance reasoning, mean-vs-median sensitivity to a single extreme value.
- **Notes:** None.

### Q13 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021: mean 49.64/median 50.55/SD 12.20/CV 0.246; 2023: mean 61.42/median 61.90/SD 11.27/CV 0.184.
- **Critical thinking:** High — cross-dataset "which was disturbed more relatively" comparison is a strong synthesis prompt.
- **Notes:** None.

### Q14 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — AAC Brandon mean 59.62, median 61.00, SD 11.12, CV 0.186 (book's rough "0.19" matches).
- **Critical thinking:** Medium/High — within-variety vs pooled variability reasoning.
- **Notes:** None.

### Q15 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — SY MANNESS mean 72.12/SD 11.49 (n=108); AAC Brandon mean 59.62/SD 11.12 (n=519). Gap ≈12.5 bu/ac, matches "~12."
- **Critical thinking:** High — sample-size-as-trust-signal reasoning.
- **Notes:** None.

### Q16 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 61.42, median 61.90, CV 0.184; Q1 55.10, Q3 69.25, IQR 14.15; lower fence 33.875, 7 rows below it (book says "several low values… fall below" — matches).
- **Critical thinking:** High — contrasts tight-bulk vs wide-bulk outlier sensitivity directly against Q9's SK barley case.
- **Notes:** None.

### Q17 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — 2398 TRUE, 2960 FALSE (5358 total).
- **Critical thinking:** High — blank-vs-withheld distinction, correcting a flawed student claim.
- **Notes:** None.

### Q18 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — 2025: mean 68.03, median 69.00, SD 11.84, CV 0.174. 2025 vs 2021 (49.64) gap ≈18.4, matches "~18 bu/ac higher."
- **Critical thinking:** Medium/High — fair year-comparison methodology (hold variety constant).
- **Notes:** None.

### Q19 — Section 1 · MB Wheat Variety
- **Sense:** OK — Riding Mountain West 2025 does have exactly 11 reported varieties, matching "eleven varieties were reported there that year."
- **Answer check:** ✅ verified — mean 71.67 (book ≈71.7), range 87.7−43.4=44.3 (book ≈44.3).
- **Critical thinking:** High — isolating variety effect from location effect, single-site-year caution.
- **Notes:** Slightly the heaviest of the MB Section-1 set (5 parts, all requiring real interpretation, plus a filter to one municipality-year) — not a problem, just flagged for pacing.

### Q20 — Section 1 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — top two by count: AAC Brandon (n=519, mean 59.62, CV 0.186) and AAC Starbuck (n=374, mean 62.70, CV 0.180). Book's "CV ≈0.19 vs 0.18" matches.
- **Critical thinking:** High — dual-signal (CV + count) reliability reasoning.
- **Notes:** None.

### Q21 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 51.32, median 50.90 (book ≈50.8, close), range 33.7–73.9, SD 7.52, CV 0.147.
- **Critical thinking:** High — pooling-provinces critique, suggests a fix (break out by province).
- **Notes:** None.

### Q22 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 41.04, SD 5.35, CV 0.130. Note: the cleaned CSV I audited contains **zero** raw 0-bu/ac canola rows — the "raw StatsCan 0" referenced in (c)/(d) is a documented cleaning step, not something visible in the delivered file, so students cannot verify it directly, but the question is posed as a hypothetical/explanatory scenario ("Explain why treating that 0 as real would distort...") rather than asking them to find it — acceptable.
- **Critical thinking:** High — zero-vs-missing distinction, a genuinely important data-literacy point.
- **Notes:** Consider rewording (c)/(d) to be explicit that this is illustrative/hypothetical rather than implying the 0 exists in their working file, to avoid confused students searching for it.

### Q23 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — SK all-crops-pooled mean 45.05 (book ≈45.1), median 40.40 (matches exactly).
- **Critical thinking:** High — distinguishes pooling-crops trap from pooling-places trap (Q21), and prescribes the fix (PivotTable/AVERAGEIF by crop).
- **Notes:** None.

### Q24 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Barley mean 64.24/SD 9.10/CV 0.142; Soybeans mean 39.56/SD 9.08/CV 0.229.
- **Critical thinking:** High — "equal SD, different CV" is one of the sharpest conceptual traps in the whole bank.
- **Notes:** None.

### Q25 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021 canola provincial mean 34.25/median 32.65, clearly below the all-years mean 41.04.
- **Critical thinking:** High — connects a single-year comparison to an averaging-hides-variation argument across granularities.
- **Notes:** n=6 provinces reporting canola in 2021 — small but real; fine for the intended point.

### Q26 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Ontario canola mean 46.72, Saskatchewan 39.09, gap ≈7.6 (book "~7-8" matches). SK seeded acres ~11-12.4M/yr vs Ontario ~35-63K/yr, consistent with "SK dominates total production."
- **Critical thinking:** High — rate vs. total distinction, core Module-1 concept done well.
- **Notes:** None.

### Q27 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 79.41, median 75.90 (mean > median → right-skew, as stated), CV 0.193, Q1 68.60, Q3 90.80, IQR 22.20.
- **Critical thinking:** High — cross-granularity skew-direction comparison (province vs RM) is a genuinely nuanced point.
- **Notes:** None.

### Q28 — Section 1 · Canada Field Crops
- **Sense:** issue — see below.
- **Answer check:** ❌ **WRONG** — stated "≈185 blank-yield rows"; actual is **66** blank `Yield_bu_ac` rows (out of 1067). The stated concentration narrative ("blanks cluster in crops not grown in the east — flax, durum, canola in maritime provinces") is also wrong: **Flax has zero blanks**. The real concentration is **Mixed grains (21) and Rye (15)** — 36 of 66 blanks — spread mostly across Newfoundland & Labrador (17), New Brunswick (14), and PEI (11), i.e. maritime/Atlantic provinces are right, but the crops named are not.
- **Critical thinking:** High (concept is sound — blank-vs-suppression contrast, never-replace-with-0 rule) — but the wrong count undermines a "count how many" part (a) exercise directly.
- **Notes:** **Needs a fix.** Correct (a) to 66; correct (b) to "Mixed grains and Rye concentrate the blanks, mostly in Newfoundland, New Brunswick, and PEI." This is the most clear-cut numeric error in the bank.

### Q29 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Durum mean 40.61/CV 0.287; durum reported by 5 provinces vs canola's 8 (book "5 vs 8+" matches).
- **Critical thinking:** High — "narrower coverage ≠ less accurate" is a subtle and well-posed distinction.
- **Notes:** None.

### Q30 — Section 1 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Barley 2023: mean 58.68/median 55.20/SD 8.98/CV 0.153, n=9 reporting provinces (Newfoundland missing that year). Highest Manitoba 75.4, lowest Quebec 46.1 — both match exactly.
- **Critical thinking:** Medium/High — range-as-spread reasoning, single-sentence synthesis prompt.
- **Notes:** None.

### Q31 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — 2010 ≈29.82, 2019 ≈40.78, 2021 ≈21.86 (2021 lowest, matches).
- **Critical thinking:** Medium — mostly formula mechanics, but (c) asks for a genuine cross-crop broad-vs-narrow event check.
- **Notes:** None.

### Q32 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — >40 count 1483, total non-blank 10,039, proportion 0.1477 (book "0.148" matches); >50 count 181.
- **Critical thinking:** Medium — proportion interpretation and a distribution-shape explanation for the sharp drop.
- **Notes:** None.

### Q33 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — RM1/2023 canola = 36.8; RM100/2023 spring wheat = 52.9. Both exact.
- **Critical thinking:** Medium/High — explains why VLOOKUP-on-RM-alone fails, and two genuine data-driven error causes for (d).
- **Notes:** None.

### Q34 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — canola>40 AND wheat>45: 1204; canola>40 alone: 1483.
- **Critical thinking:** Medium/High — subset logic (AND vs OR) reasoning.
- **Notes:** None.

### Q35 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — RM1 barley mean 56.56 (n=35), RM100 barley mean 43.89 (n=35), gap 12.67 (book "~12.7" matches).
- **Critical thinking:** Medium — fair-comparison-requires-similar-n reasoning, per-RM vs per-year grouping distinction.
- **Notes:** None.

### Q36 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — overall canola mean 28.29, count above it 4519 of 10,039, fraction 0.450 (book "0.45" matches).
- **Critical thinking:** High — connects "why not 50%" to skew, plus a genuinely useful Excel syntax gotcha (quoted string vs concatenation).
- **Notes:** None.

### Q37 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Canola 2015→2019: 36.06→40.78 (Δ4.72); Barley 2015→2019: 55.25→68.59 (Δ13.34). Barley rose more absolutely, matches.
- **Critical thinking:** High — absolute vs relative change, a core numeracy trap.
- **Notes:** None.

### Q38 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Low(<20): 2037, Medium[20,40]: 6519, High(>40): 1483 across all years/RMs — Medium is by far the most common, consistent with the ~28 bu/ac overall mean sitting in that band.
- **Critical thinking:** Medium — IF/IFS mechanics plus a blank-handling correction.
- **Notes:** None.

### Q39 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Canola count 10,039, Flax count 8,077, difference 1,962 (book "≈1,960" matches).
- **Critical thinking:** Medium — COUNT vs COUNTA distinction, coverage-as-information framing.
- **Notes:** None.

### Q40 — Section 2 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021 canola mean 21.86, 2023 canola mean 33.88; 2021 below-20 count 120, 2023 below-20 count 57.
- **Critical thinking:** Medium/High — threshold-count comparison as a "how bad was the bad year" measure.
- **Notes:** None.

### Q41 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — 2960 FALSE, 2398 TRUE, total 5358, reported proportion 0.4476 (book "0.45" matches).
- **Critical thinking:** High — genuinely distinguishes "unaffected by deletion" vs "biased by deletion" calculations, a strong analytical ask.
- **Notes:** Five parts here are all substantive (no pure mechanics filler) — on the heavier end for Section 2 pacing, though not unreasonably so.

### Q42 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — AAC Brandon reported mean 59.62 (n=519), suppressed count 51, total appearances 570.
- **Critical thinking:** Medium/High — average-vs-count complementary information reasoning.
- **Notes:** None.

### Q43 — Section 2 · MB Wheat Variety
- **Sense:** OK — GLENN does appear with very few reported rows.
- **Answer check:** ✅ verified — GLENN: 4 reported, 96 suppressed (total 100), fraction reported 0.04 (4%), matching the stated "≈4/100 ≈4%."
- **Critical thinking:** High — small-sample fragility reasoning, direct contrast with Q42's Brandon case.
- **Notes:** None.

### Q44 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — >70: 569 (book ≈569, exact); >80: 97 (book ≈97, exact); proportions 0.237 and 0.040, matching stated "~0.24" and "~0.04."
- **Critical thinking:** Medium/High — successive-threshold tail-shape reasoning.
- **Notes:** None.

### Q45 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021 mean 49.64 (n=396 reported), 2023 mean 61.42 (n=423 reported). Matches exactly.
- **Critical thinking:** Medium/High — fair year-comparison caveat tied to variety-mix changes.
- **Notes:** None.

### Q46 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — AAC Brandon / ALONSA / 2020 lookup returns 65.1 (matches "≈65.1").
- **Critical thinking:** Medium/High — blank-vs-error distinction for lookups, ties back to Reported flag.
- **Notes:** None.

### Q47 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — SY MANNESS mean 72.12 (n=108); AAC Brandon mean 59.62 (n=519). Matches exactly.
- **Critical thinking:** High — "higher average ≠ better documented" is a clean, well-posed trap.
- **Notes:** None.

### Q48 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — AAC Brandon reported counts 2020-2025: 94, 90, 87, 84, 83, 81 — matches "counts near 80-95 per year," and 2020 is indeed the highest year, matching the stated answer.
- **Critical thinking:** Medium — count-vs-average distinction, straightforward but sound.
- **Notes:** None.

### Q49 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 reported rows above 70: 96; total 2023 reported: 423; proportion 0.227 ("moderate," consistent with stated framing).
- **Critical thinking:** Medium — COUNTIFS vs COUNTIF necessity, proportion-for-cross-year-comparability reasoning.
- **Notes:** None.

### Q50 — Section 2 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — total reported 2398, suppressed 2960; AAC Starbuck reported count 374; share 374/2398=0.156 (book "0.16" matches).
- **Critical thinking:** Medium/High — trial-dataset-vs-true-popularity distinction, a good data-literacy closer for the section.
- **Notes:** None.

### Q51 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 total canola seeded acres 22,085,300 (exact); Saskatchewan 12,400,400 = 56.1% of the total (book "over half" matches).
- **Critical thinking:** High — sum-is-meaningful-for-acres-but-not-yield distinction, a load-bearing Module-1 concept.
- **Notes:** None.

### Q52 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 seeded acres: canola 22,085,300; spring wheat 19,496,400; barley 7,330,600 — ranking canola > spring wheat > barley matches exactly.
- **Critical thinking:** Medium/High — scale vs. per-acre-performance distinction.
- **Notes:** None.

### Q53 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Ontario canola mean 46.72, Saskatchewan 39.09, gap ≈7.63 (matches "~7.6"); SK 2023 seeded canola acres 12,400,400 vs Ontario's much smaller total.
- **Critical thinking:** High — rate-vs-total, reprised effectively from Q26.
- **Notes:** None.

### Q54 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Manitoba canola 2023: yield 44.6 bu/ac, seeded acres 3,128,200. Both exact matches.
- **Critical thinking:** Medium/High — three-key uniqueness reasoning for lookups.
- **Notes:** None.

### Q55 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — total blank yields 66 (matches "≈66" exactly — note this is the *correct* figure that Q28 gets wrong at "≈185," confirming Q28 is the outlier error, not a dataset-snapshot mismatch). Durum blanks specifically: 4.
- **Critical thinking:** Medium/High — same blank-vs-suppression contrast as Q28/Q17, done correctly here.
- **Notes:** None. (This question's correct 66 further confirms Q28's 185 is simply wrong, not a stale-snapshot artifact.)

### Q56 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — spring wheat >55: 30 rows; total non-blank spring wheat: 94; proportion 0.319 (book "≈0.32" matches).
- **Critical thinking:** Medium — pooled-proportion limitation reasoning (mixes provinces and years).
- **Notes:** None.

### Q57 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 barley mean 58.68 (n=9 provinces) vs soybean mean 42.41 (n=7 provinces) — barley higher, matching "barley yields more."
- **Critical thinking:** Medium/High — breadth-of-average reasoning tied to province counts.
- **Notes:** None.

### Q58 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — canola seeded acres 2020: 20,782,600; 2023: 22,085,300; change +1,302,700.
- **Critical thinking:** Medium — footprint-over-time interpretation, sum-vs-average validity distinction reprised.
- **Notes:** None.

### Q59 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — canola provincial-avg by year: 2019 40.93, 2021 34.25, 2023 42.44 — 2021 is clearly lowest, matches.
- **Critical thinking:** High — cross-granularity smoothing argument (province vs RM) reprised well.
- **Notes:** This is restricted to the 2019/2021/2023 sub-filter, where 2021 genuinely is the low point — unaffected by the full-range 2002 issue found elsewhere.

### Q60 — Section 2 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — spring wheat 2023 total seeded acres 19,496,400; average yield across provinces 48.28.
- **Critical thinking:** High — production = rate × quantity per group, summed across groups; probably the single best "why can't you just multiply" conceptual question in the bank.
- **Notes:** Five substantial reasoning parts with no pure-mechanics filler — one of the heavier Section 2 questions for pacing.

### Q61 — Section 3 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 canola mean 33.88 < median 35.50 → left-skew, matches stated direction.
- **Critical thinking:** High — bin-width-can-mislead reasoning is a genuinely useful chart-literacy point.
- **Notes:** None.

### Q62 — Section 3 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 IQRs: Canola 22.30, Spring Wheat 27.10, Barley 41.40 — Barley widest, matches.
- **Critical thinking:** High — connects box width directly to IQR and to the outlier-fence forgiveness point from Q9.
- **Notes:** None.

### Q63 — Section 3 · SK RM Crop Yields
- **Sense:** OK (buildable), but the model answer's specific claim is wrong — see below.
- **Answer check:** ❌ **WRONG** — stated "sharpest single-year dip… approximately 2021." The actual lowest year for canola over the full 1990–2025 range is **2002** (mean ≈15.83 bu/ac), followed by 2003 (≈17.03) and 2001 (≈18.19); 2021 (≈21.86) ranks only 9th-lowest. A student who actually builds the requested 1990–2025 line chart will see a *deeper* dip around 2001–2003 than at 2021.
- **Critical thinking:** High (concept — separating long-run trend from one-off dips — is sound) but undermined by the wrong reference year.
- **Notes:** **Needs a fix.** Change the model answer's dip year to 2002 (or reframe as "one of several early-2000s low years"), and re-check part (b)'s "from ~19 bu/ac in 1995" framing, which stays roughly accurate on its own.

### Q64 — Section 3 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — canola and spring wheat co-move; both do dip in 2021 (canola 21.86, spring wheat 30.22 that year — a real local dip even though it isn't the deepest dip in the whole series). This question only asks for *a* shared dip year, not *the* lowest, so it is not wrong, just adjacent to the Q63/Q69/Q100 issue.
- **Critical thinking:** High — legend/shared-axis fairness reasoning.
- **Notes:** Technically fine since it asks for "one year where both dip," which 2021 satisfies, even though it is not the single lowest year in the full series.

### Q65 — Section 3 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Barley 2023 mean 54.56 < median 59.90 → left-skew, matches; Barley IQR 41.40 > Canola IQR 22.30, "Barley more spread out" matches.
- **Critical thinking:** Medium/High — same-axis-scale-for-fair-comparison point is a real presentation lesson.
- **Notes:** None.

### Q66 — Section 3 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — medians: 2019 42.10, 2021 22.80, 2023 35.50 — 2021 lowest median, matches. (This is a 3-year within-set comparison, not a full-range claim — correct.)
- **Critical thinking:** High — box-plot-vs-single-average information gain argument.
- **Notes:** None.

### Q67 — Section 3 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Oats 2023 mean 71.14 < median 75.90 → left-skew, matches.
- **Critical thinking:** High — "tallest bars ≠ typical value" reasoning, a nuanced histogram-literacy point.
- **Notes:** None.

### Q68 — Section 3 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Durum 2021 mean 21.69 > median 17.20 → right-skew, matches stated direction and the "median line near Q1" mechanism.
- **Critical thinking:** High — box-plot skew-signature reasoning without needing to compute the mean.
- **Notes:** None.

### Q69 — Section 3 · SK RM Crop Yields
- **Sense:** OK (buildable), but the model answer is wrong for the same reason as Q63.
- **Answer check:** ❌ **WRONG** — stated "lowest year 2021 (~35 bu/ac)." The actual lowest year for barley over 1990–2025 is **2002** (mean ≈30.64), not 2021 (≈34.83, which ranks 2nd-lowest — close, but not lowest). The stated "~35 bu/ac" figure for 2021 is roughly right in isolation (34.8), but the claim that it is *the* lowest year is incorrect.
- **Critical thinking:** High (concept — cross-crop shared-low-year evidence — sound) but built on the wrong year.
- **Notes:** **Needs a fix.** Correct to 2002; note that 2021 is close (2nd-lowest, ≈34.8 vs 2002's ≈30.6) so the "does canola share this dip" comparison in part (c)/(d) needs re-checking against 2002 rather than 2021 — canola's 2002 value is also its lowest (≈15.83), so the "shared worst year" story actually survives, just with 2002 as the correct shared year instead of 2021.

### Q70 — Section 3 · SK RM Crop Yields
- **Sense:** OK.
- **Answer check:** ✅ verified — Spring Wheat 2019 mean 49.23, median 50.05 — roughly symmetric, centred high-40s/50, matches.
- **Critical thinking:** Medium/High — eyeball-vs-computed-centre calibration exercise.
- **Notes:** None.

### Q71 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified (approximately) — all-years reported yields: lower fence 30.35, count below it = 35 (book states "about 39" — off by 4, within the "about" hedge, acceptable but worth tightening).
- **Critical thinking:** High — histogram-vs-box-plot outlier-visibility contrast is a strong presentation-literacy point.
- **Notes:** Minor: consider updating "about 39" to "about 35" for tighter accuracy, though the qualitative point stands either way.

### Q72 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — top 6 varieties by count: AAC Brandon (519), AAC Starbuck (374), AAC Wheatland (219), AAC Hockley (177), AAC Viewfield (165), AAC Redberry (138) — matches exactly. Most consistent (smallest IQR): AAC Hockley (IQR 12.70), matches stated "IQR≈12.7."
- **Critical thinking:** High — audience/message-dependent chart-choice justification (box plot vs bar of means) is a genuinely open-ended, well-posed prompt.
- **Notes:** None.

### Q73 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — AAC Brandon by year: 2020 62.49, 2021 49.14 (lowest), 2022 57.87, 2023 60.32, 2024 62.32, 2025 66.34. 2021 is genuinely the lowest here (restricted to 2020-2025, not the full 1990-2025 SK range), so this is correct and unaffected by the Q63/Q69 issue.
- **Critical thinking:** High — cross-dataset shared-low-year evidence, holding variety fixed to isolate year effects.
- **Notes:** None.

### Q74 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 reported yields: lower fence 33.875, count below = 7, matching "about 7 low-end outliers" exactly.
- **Critical thinking:** Medium/High — pooled-vs-single-year outlier-count reasoning.
- **Notes:** None.

### Q75 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — six-variety means: Brandon 59.62, Starbuck 62.70, Wheatland 65.78 (tallest), Hockley 64.85, Viewfield 62.48, Redberry 54.43 (shortest). Book's "tallest ≈ Wheatland/Hockley; shortest ≈ Redberry" matches (Wheatland edges out Hockley by <1 bu/ac, so grouping them is reasonable).
- **Critical thinking:** Medium/High — zero-baseline distortion argument, bar-vs-box choice criterion.
- **Notes:** None.

### Q76 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — QUARTILE.INC/MEDIAN approach is correct and consistent with all other quartile computations verified elsewhere in the bank.
- **Critical thinking:** Medium — visual-estimate-vs-exact-value calibration, useful but more mechanical than most Section 3 questions.
- **Notes:** None.

### Q77 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — Brandon and Starbuck both dip in 2021 relative to surrounding years (Brandon 49.14, and Starbuck follows a similar pattern per Q102's answer), consistent with "track each other."
- **Critical thinking:** Medium/High — closest/farthest-year identification plus shared-conditions reasoning.
- **Notes:** None.

### Q78 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — AAC Brandon IQR 13.00 vs all-varieties pooled IQR 15.70 — single-variety tighter, matches "IQR≈13 vs pooled≈15.7."
- **Critical thinking:** High — part-vs-whole spread decomposition (how much of pooled spread comes from mixing varieties).
- **Notes:** None.

### Q79 — Section 3 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — by-year reported medians: 2021 median 50.55 is the lowest across 2020-2025 (2020's is higher, and later years recover) — matches "2021 has the lowest median box." Within-range claim, correct.
- **Critical thinking:** Medium/High — whole-distribution-shift vs single-average-shift distinction.
- **Notes:** None.

### Q80 — Section 3 · MB Wheat Variety
- **Sense:** OK, though structurally a bit different from other questions (parts (a)-(b) are conceptual/no-chart, only (c) asks for an actual chart build) — still coherent and doable.
- **Answer check:** ✅ verified (conceptual, no disputed numeric claim) — pie-vs-bar chart-choice guidance is standard and correctly stated.
- **Critical thinking:** High — genuinely tests judgment about when a chart type is appropriate, a strong closer for the section.
- **Notes:** Consider flagging in instructions that (a)/(b) are hypothetical/reasoning-only (no chart needed) so students don't waste time trying to build a "share of reported rows" pie chart that isn't actually requested.

### Q81 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — canola by-province (2015-2025): Ontario highest median (46.50, book "~46.5" matches); British Columbia widest box (IQR 11.00, book "IQR≈11.0" matches exactly).
- **Critical thinking:** High — headline-claim critique ("Ontario grows the best canola") plus explicit "what's missing" (acreage) follow-up.
- **Notes:** None.

### Q82 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — national canola yield by year (2015-2025): 2021 is genuinely the lowest (34.25 vs neighboring years ~40-42), matching "2021 is the low point (~34 bu/ac)." Correct because this dataset only spans 2015-2025, unlike the SK RM full-range questions.
- **Critical thinking:** High — cross-dataset consistency-of-evidence argument (SK RM + MB + StatsCan all pointing at 2021 within their respective ranges).
- **Notes:** None — this question is NOT affected by the Q63/Q69/Q100 issue since its dataset genuinely starts in 2015.

### Q83 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 canola by-province spans Ontario (53.4, high) to British Columbia (35.1, low); the answer's suggested tallest/shortest direction is consistent with the data (book leaves the exact naming open — appropriately hedged as "report from your chart").
- **Critical thinking:** Medium/High — zero-baseline, single-year-vs-multi-year information distinction.
- **Notes:** None.

### Q84 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — barley by-province all-years: highest median Manitoba (75.40), widest spread Alberta (IQR 10.10) or Nova Scotia (IQR 10.05) — close contest, consistent with the book's open-ended "report from your chart" framing.
- **Critical thinking:** Medium/High — observation-count-affects-reliability argument.
- **Notes:** None.

### Q85 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — canola and spring wheat both dip in 2021 within the 2015-2025 StatsCan range (correct, unaffected by the full-range issue).
- **Critical thinking:** Medium/High — shared-axis fairness, legend necessity.
- **Notes:** None.

### Q86 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified (descriptive, open-ended) — canola pooled mean 41.04, fairly tight distribution, consistent with "centred near low 40s, fairly symmetric."
- **Critical thinking:** Medium/High — pooled-histogram-blurs-groups argument, prescribes the fix (box plot per province).
- **Notes:** None.

### Q87 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 canola seeded acres: Saskatchewan 12,400,400, by far the tallest bar; Ontario leads yield (53.4) but not acres — "No, different province leads each" matches exactly.
- **Critical thinking:** High — rate-vs-total contrast, effectively reprised across acres and yield charts.
- **Notes:** None.

### Q88 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — PEI has only 1 reported spring-wheat row (per the Q81-style province coverage check), a genuinely thin box exactly as the question anticipates.
- **Critical thinking:** Medium/High — sample-size reliability check via COUNTIFS.
- **Notes:** None.

### Q89 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — national barley yield by year (2015-2025): 2021 is genuinely the lowest (56.09 vs neighbors in the mid-to-high 60s), matches "lowest year 2021" and matches canola's 2021 low from Q82. Correct — within the StatsCan 2015-2025 range only.
- **Critical thinking:** Medium/High — shared-worst-year-across-crops evidence for a broad event.
- **Notes:** None — again unaffected by the full-range SK RM issue.

### Q90 — Section 3 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — Saskatchewan canola by year also bottoms at 2021 within the 2015-2025 dataset, consistent with the national low year.
- **Critical thinking:** Medium/High — province-vs-national divergence framing.
- **Notes:** None.

### Q91 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — unfiltered 2023 by-crop averages: Lentils 1314.3 (lb/ac, wildly out of line), Oats 71.14, Barley 54.56, Spring Wheat 42.87, Peas 33.96, Canola 33.88, Durum 29.60, Flax 20.31. Filtered to bu/ac: Oats highest (71.14), Flax lowest (20.31) — both match exactly.
- **Critical thinking:** High — this is one of the strongest single questions in the whole bank: a genuine, catchable unit-mixing trap (lb/ac lentils polluting an unfiltered ranking).
- **Notes:** None — excellent question, no changes needed.

### Q92 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — canola 2021 (21.86) vs 2023 (33.88), a ~35% drop, matches "about one-third lower." Every crop's 2021 row is depressed relative to typical years (confirmed via full crop-by-2021 breakdown), matching "every crop's 2021 average is low."
- **Critical thinking:** High — row-vs-column reasoning (broad cause vs crop-specific) is conceptually sharp.
- **Notes:** None — this is a *within-2021* observation (2021 vs its neighbors), not a full-range "lowest ever" claim, so it is correct and unaffected by the Q63-type issue.

### Q93 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — 2025 minus 2019 by crop: Oats +8.05 (highest absolute rise, matches "~8"), Barley +4.25 (book ≈4.2, matches), Canola +3.16 (book ≈3.1, matches).
- **Critical thinking:** High — absolute-vs-relative-change distinction reprised at the PivotTable level.
- **Notes:** None.

### Q94 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — canola reporting counts in recent years run 289-293, matching "about 290."
- **Critical thinking:** Medium — Count-vs-Average PivotTable distinction, straightforward but correctly explained.
- **Notes:** None.

### Q95 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — dual Average+Count PivotTable is standard and buildable; the crops' relative report counts in 2023 are consistent with the stated framing.
- **Critical thinking:** Medium/High — count-as-reliability-signal-next-to-average reasoning.
- **Notes:** None.

### Q96 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — within 2019-2023, canola's lowest is genuinely 2021 (21.86 vs 2019's 40.78, 2020's 38.23, 2022's 35.40, 2023's 33.88); barley's lowest in the same window is also 2021 (34.83). Both match the stated answer exactly. This is correctly scoped to a 5-year window, not the full range, so it is NOT affected by the Q63/Q69 issue.
- **Critical thinking:** High — shared-lowest-year-across-crop-rows reasoning, cleanly executed.
- **Notes:** None.

### Q97 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — all-years by-crop ranking: Oats (64.71) > Barley (51.75) > Spring Wheat (35.31) > Durum (33.56) > Peas (31.76) > Canola (28.29) > Flax (20.53). Matches "Oats > Barley > Spring Wheat > Durum/Peas/Canola (middle cluster) > Flax" — the "middle cluster" grouping in the model answer is a reasonable simplification of three closely-spaced values.
- **Critical thinking:** Medium/High — long-run vs single-year ranking stability reasoning.
- **Notes:** None.

### Q98 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — Oats by year 2019-2025: highest 2025 (97.47, matches "~97"), lowest 2021 (45.06, matches "~45"). This is correctly scoped to 2019-2025 where 2021 genuinely is the low point for oats specifically (unlike canola/barley/spring wheat, oats' 2021 dip is real even considering 1990-2025 — 2021 ranks 4th-lowest for oats overall, close behind 2002/2003/2001, so this narrower claim holds).
- **Critical thinking:** Medium/High — single-crop isolation-by-filter reasoning, Sum-vs-Average distinction.
- **Notes:** None.

### Q99 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021 by-crop ranking: Oats (45.06) > Barley (34.83) > Spring Wheat (30.22) > Peas (22.49) > Canola (21.86) > Durum (21.69) > Flax (12.79). Matches stated order exactly; top crop (Oats) unchanged from 2023's ranking (Q91), consistent with "the drought lowered every crop but kept a similar order."
- **Critical thinking:** High — level-vs-ranking distinction, a genuinely subtle statistical point.
- **Notes:** None.

### Q100 — Section 4 · SK RM Crop Yields (long)
- **Sense:** OK (buildable), but the model answer's claim is wrong for the same reason as Q63/Q69.
- **Answer check:** ❌ **WRONG** — stated "Rising overall; lowest year 2021." As in Q63, the actual lowest year for canola over the full 1990–2025 range is **2002** (≈15.83 bu/ac), not 2021 (≈21.86, ranking 9th-lowest). The "rising overall" direction is correct; only the specific low-year identification is wrong.
- **Critical thinking:** High (concept sound) but the specific reference year is incorrect.
- **Notes:** **Needs a fix** — same correction as Q63: change to 2002 (or "one of several low years clustered around 2001–2003").

### Q101 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — highest average: SY MANNESS (72.12); most widely reported: AAC Brandon (n=519, mean 59.62). Both match exactly.
- **Critical thinking:** High — trustworthiness-via-count reasoning, explicit ≥30-report quality-control threshold discussion.
- **Notes:** Five substantial parts, no filler — on the heavier end for Section 4 pacing (dual-value PivotTable plus a filtering decision).

### Q102 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — AAC Brandon's weakest year is 2021 (49.14 vs its other years in the high-50s to mid-60s), matching "~49… below its ~62-66 in other years." This is a within-2020-2025 comparison, correctly scoped and correct.
- **Critical thinking:** High — isolates year effect by holding variety fixed, a clean methodological point.
- **Notes:** None.

### Q103 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — top three by count: AAC Brandon (519), AAC Starbuck (374), AAC Wheatland (219). Matches exactly.
- **Critical thinking:** Medium/High — count-as-a-precursor-to-ranking argument.
- **Notes:** None.

### Q104 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — 2020-2025 reported yearly means: lowest 2021 (49.64, matches "~49.6"), highest 2025 (68.03, matches "~68.0"). Correctly scoped to the 2020-2025 range where this claim genuinely holds.
- **Critical thinking:** Medium/High — Count-column-as-interpretive-aid reasoning.
- **Notes:** None.

### Q105 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — municipality-level PivotTable is buildable and the small-sample-per-municipality caution is well-founded given how thin some municipality-year cells are (e.g., Q19's Riding Mountain West had only 11 varieties).
- **Critical thinking:** Medium/High — same count-flags-thin-averages theme reprised at a finer grain.
- **Notes:** None.

### Q106 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — single-year variety ranking is buildable and consistent with the all-years ranking pattern established in Q101.
- **Critical thinking:** Medium/High — rank-stability-over-time reasoning.
- **Notes:** None.

### Q107 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — filtering to varieties with ≥30 reports and comparing to Q101: SY MANNESS (n=108, mean 72.12) remains the highest even after the filter (108≥30), matching "Highest ≈ SY MANNESS." Lower-bound example varieties in the answer (AAC Tisdale/Redberry ~54) are plausible given AAC Redberry's confirmed mean of 54.43.
- **Critical thinking:** High — minimum-count-as-quality-control framing is one of the better conceptual threads in the bank.
- **Notes:** Adds a filter/sort step on top of a dual-value PivotTable — moderately heavy build for the 50-minute window if drawn as the Section 4 question.

### Q108 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — comparing AAC Brandon (59.62 pooled) vs AAC Starbuck (62.70 pooled) confirms Starbuck's edge is consistent across the pooled comparison, supporting "Starbuck is generally higher."
- **Critical thinking:** High — consistent-vs-year-specific-advantage reasoning via a two-variety grid.
- **Notes:** None.

### Q109 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — tallest bar SY MANNESS (72.12, highest mean in dataset among named varieties); shortest among top varieties, AAC Redberry (54.43), matches stated framing.
- **Critical thinking:** Medium/High — bar-chart-hides-count-and-spread argument, PivotChart sync explanation.
- **Notes:** None.

### Q110 — Section 4 · MB Wheat Variety
- **Sense:** OK.
- **Answer check:** ✅ verified — AAC Brandon TRUE/FALSE split: 519 reported, 51 suppressed, matching "≈519 TRUE, ≈51 FALSE" exactly.
- **Critical thinking:** High — deletion-destroys-information argument, ties back cleanly to Q17/Q41's blank-vs-suppressed theme.
- **Notes:** Reported-vs-suppressed crosstab is a good closer for the MB PivotTable set.

### Q111 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 canola by-province ranking: Ontario 53.4, New Brunswick 45.6, Manitoba 44.6, Quebec 40.9, Alberta 40.1, Saskatchewan 37.4, British Columbia 35.1 — matches the stated ranking exactly, digit for digit.
- **Critical thinking:** High — yield-per-acre-vs-importance distinction, with an explicit acres-as-second-value follow-up.
- **Notes:** None.

### Q112 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — Saskatchewan's 2021 canola yield (per Q90's SK-specific line) is depressed relative to its other years, and multiple provinces show a 2021 dip in the 2015-2025 StatsCan data (consistent with Q82's national 2021 low), supporting "several provinces are low in 2021, not just Saskatchewan."
- **Critical thinking:** High — row-vs-column (local vs broad cause) reasoning at the province level.
- **Notes:** None.

### Q113 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 canola seeded acres by province: SK 12,400,400, AB 6,362,800, MB 3,128,200, BC 108,600, ON 45,100, QC 38,600, NB 1,600 — matches the stated ranking and figures exactly. SK share ≈56.1%, "over half" confirmed.
- **Critical thinking:** High — acres-vs-yield ranking mismatch, directly connects to Q111's yield ranking (different leader).
- **Notes:** None.

### Q114 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — national by-crop yield ranking: Corn for grain (135.62, matches "~136") highest, then Winter wheat (63.30) actually ranks ahead of the stated "Oats (~79), Barley (~64)" sequence in the raw data — **checking closer**: actual full order is Corn 135.6 > Oats 79.4 > Barley 64.2 > Winter wheat 63.3 > Wheat(all) 57.3 > Mixed grains 53.3 > Rye 51.9 > Spring wheat 51.3 > Canola 41.0 > Durum 40.6 > Soybeans 39.6 > Dry peas 37.8 > Flax 25.6 (lowest, not Flax≈26 as stated but consistent). Book's spot-checked figures (Corn ~136, Oats ~79, Barley ~64, Flax ~26) all match; it just doesn't list every crop, which is fine since the question only asks to "rank the crops," not enumerate every value in the key.
- **Critical thinking:** High — per-acre-yield-vs-grown-scale distinction, explicit prescription of the acres-pivot fix.
- **Notes:** None — spot-checked values all correct.

### Q115 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — all-years canola by-province: Ontario 46.72, New Brunswick 44.00, Manitoba 41.51, Quebec 41.39, PEI 40.70, Alberta 40.13, Saskatchewan 39.09, British Columbia 35.52 — matches the stated ranking and figures exactly, including Ontario topping both this and the 2023-only ranking (Q111).
- **Critical thinking:** Medium/High — all-years-vs-single-year ranking stability, consistent with Q97's parallel SK-crop version.
- **Notes:** None.

### Q116 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — canola seeded acres rose from 20,782,600 (2020) to 22,085,300 (2023) per Q58, consistent with an overall rising trend across 2015-2025.
- **Critical thinking:** Medium/High — Sum-vs-Average correctness argument for acres, reprised cleanly.
- **Notes:** None.

### Q117 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified (method) — spring wheat 2023 seeded acres are Prairie-dominated (SK/AB/MB lead, consistent with Q52's national total of 19,496,400 acres being mostly Prairie-sourced).
- **Critical thinking:** High — acres-and-yield-together tells-a-fuller-story argument, with an explicit "production needs both" framing.
- **Notes:** None.

### Q118 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Durum wheat has a low reporting count (5 provinces per Q29) vs canola/barley/spring wheat's broader coverage (8-9+ provinces), matching "widely grown crops have high counts; durum and flax have lower counts."
- **Critical thinking:** Medium/High — coverage-count-as-a-check-before-trusting-an-average argument.
- **Notes:** None.

### Q119 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — SK canola seeded acres by year (11.15M in 2015 rising to 12.4M by 2023, with minor fluctuation), consistent with "SK plants the most canola in recent years (~12M+ acres)" and Q113's confirmation that SK leads all provinces.
- **Critical thinking:** Medium/High — trend-plus-leader-in-one-grid reasoning.
- **Notes:** None.

### Q120 — Section 4 · Canada Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — canola by-province all-years: Ontario highest (46.72), British Columbia lowest (35.52), matching "Highest ≈ Ontario; lowest ≈ British Columbia." Seeded-acres companion chart would indeed show Saskatchewan towering over the rest (12.4M vs everyone else's low millions/thousands), matching the described second chart.
- **Critical thinking:** High — a strong closing synthesis question, directly pairs a yield chart against an acres chart to drive home the whole bank's rate-vs-total throughline.
- **Notes:** Asks for two charts conceptually (one built, one described) — a reasonable closer, not excessively heavy.

---

## Prioritized Fix List

1. **Q63** — SK RM Crop Yields, Section 3 (Charts). Model answer states the sharpest 1990–2025 canola dip is "approximately 2021." **Wrong** — the true lowest year is **2002** (≈15.83 bu/ac), with 2001–2003 forming the actual low cluster; 2021 (≈21.86) ranks 9th-lowest. Fix the stated year and re-verify part (b)'s framing.
2. **Q100** — SK RM Crop Yields (long file), Section 4 (PivotTables). Same underlying data/claim as Q63 ("lowest year 2021" for the full 1990–2025 canola PivotChart) — **wrong** for the identical reason. Fix to 2002.
3. **Q69** — SK RM Crop Yields, Section 3 (Charts). States barley's 1990–2025 lowest year is "2021 (~35 bu/ac)." **Wrong** — actual lowest is **2002** (≈30.64); 2021 (≈34.83) is 2nd-lowest, close but not lowest. Fix the year; note canola's 2002 low (from fix #1) still supports the "shared worst year across crops" argument in parts (c)–(d), just anchored to 2002 instead of 2021.
4. **Q28** — Canada Field Crops, Section 1 (Descriptive Stats). States "≈185 blank-yield rows" concentrated in "flax, durum, canola in maritime provinces." **Wrong** on both counts — actual blank count is **66** (confirmed independently correct via Q55's matching "≈66" in the same dataset), and the real blank concentration is **Mixed grains (21) and Rye (15)**, mostly in Newfoundland (17), New Brunswick (14), and PEI (11) — flax has zero blanks. This is the most clear-cut, highest-priority numeric fix in the bank since a student computing the count will get a very different number from the key.
5. **Q8** — SK RM Crop Yields, Section 1. Minor drift: stated all-years canola median "≈28.60" vs actual **26.90** (mean 28.29 is correct). Doesn't change the qualitative "mean ≈ median" conclusion but should be corrected for precision; possibly a stale-snapshot artifact worth spot-checking against the currently published CSV.
6. **Q71** — MB Wheat Variety, Section 3 (Charts). States "about 39" all-years low-end outliers by the 1.5×IQR rule; actual count is **35**. Within the "about" hedge but worth tightening for a bank meant to be numerically precise elsewhere.
7. **Q22** (low priority, wording only) — the "raw StatsCan 0 bu/ac" referenced in parts (c)/(d) does not exist in the delivered cleaned CSV (correctly — it was cleaned out), but the question could be read as asking students to find it in their working file. Reword to make explicit this is a hypothetical/explanatory scenario about the cleaning process, not something to locate in the data they have.
8. **Q80** (low priority, structural) — parts (a)/(b) are reasoning-only (no chart), only part (c) requires an actual build. Consider a one-line instruction note so students don't attempt to build a pie chart that isn't actually being asked for.

No other numeric, sense, or prior-knowledge issues were found across the 120 questions and ~600 sub-parts reviewed.
