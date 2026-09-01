# Module 1 Test Bank — Audit Review

*Audit of `module01_bank.qmd` (120 questions). Every distinct numeric claim was recomputed in Python (pandas) against the three CSVs in `practice/data/`, using Excel conventions (STDEV.S = ddof 1; QUARTILE.INC/PERCENTILE.INC = linear interpolation).*

## Executive Summary

**Overall quality is high.** The bank is well structured, questions are clear and consistently answerable from the data alone, and the overwhelming majority of stated answers are numerically correct — roughly 110 of 120 questions verified clean. The interpretation parts (b)–(e) are the bank's real strength: nearly every question pairs Excel mechanics with a genuine reasoning task.

**Questions with issues: 5 hard answer errors, ~6 minor numeric imprecisions, ~6 ambiguity/sense flags.**

The most important problems:

1. **Q69 and Q100 state the wrong "lowest year."** For the full 1990–2025 SK RM series, the lowest average-yield year for both canola and barley is **2002** (canola 15.8, barley 30.6 bu/ac), not 2021 (canola 21.9, barley 34.8). 2021 is only the *sharpest one-year drop*. Q63's "sharpest dip" wording survives, but Q69(b–c) and Q100(b) are flatly wrong, and Q73(c) inherits the confusion.
2. **Q8 is broken.** The stated all-years canola median (28.60) is wrong (actual 26.90), and the central premise of parts (b)–(c) — that the pooled SD exceeds any single year's SD — is false: pooled SD = 10.06, but 2022 (12.38) and 2023 (13.33) both exceed it.
3. **Q28's blank count is wrong (185 vs actual 66)** and contradicts Q55, which correctly says 66. Q28(b)'s claim that blanks concentrate in "flax, durum, canola" is also wrong — flax has **zero** blank-yield rows (its eastern rows simply don't exist); blanks actually concentrate in Mixed grains (21) and Rye (15).
4. **Q101(b) names the wrong variety.** With no minimum-count filter (the filter only appears in part (e)), the highest average is **AAC WESTKING (79.2 bu/ac, n=17)**, not SY MANNESS (72.1, n=108).
5. **Excel XLOOKUP gotcha (Q46, Q54):** XLOOKUP on an empty return cell returns **0**, not a blank — the stated answers say "returns a blank," which is exactly the blank-vs-zero trap the bank elsewhere teaches students to avoid.

**50-minute feasibility: feasible but tight.** A typical draw (one question per section = 20 parts) is ~40–50 minutes for a student who knows the datasets: Section 1 questions run ~10–12 min, Section 2 ~8–10, Section 3 ~12–15 (chart building + prose), Section 4 ~10–12. However, several questions are disproportionately heavy — **Q72** (find top-6 varieties by count, then a 6-box box plot), **Q93** (two pivots plus per-crop change for 7 crops), **Q16/Q9** (fences plus outlier counting), **Q38** (nested IF/IFS plus three counts) — and an unlucky draw combining two of these would exceed 50 minutes. Recommend either trimming one written part from the heavy questions or balancing draws so at most one heavy question appears.

**Critical thinking: strong.** Very few questions are pure formula application. The recurring motifs — mean vs median under skew, CV vs raw SD, rate vs total, blank ≠ zero, count-backs-the-average, outlier fences depend on spread — are exactly the right ones and every one is testable from the data. The weakness is repetition: rate-vs-total appears ~8 times and blank-vs-zero ~7 times across datasets, so within one dataset's column the draw stays varied, but a student practicing the whole bank sees the same (e) sentence many times.

**Prior-knowledge constraint: satisfied.** No part requires farming/agronomy knowledge. Drought years are always identified *in the question text*, and mechanism questions (Q3d, Q10d) include the needed hint in parentheses. Q3(d) is the closest borderline case (reasoning about localized rainfall) but the hint makes it answerable by pure logic.

## Per-Section Summaries

**Section 1 — Descriptive Statistics (Q1–30).** The strongest section. All core statistics verified to the decimal except Q8 (wrong median; false pooled-SD premise) and Q28 (wrong blank count and wrong crops). Questions consistently pair computation with shape/spread interpretation, and the cross-dataset CV comparisons (Q11, Q13) are excellent — though Q13(e) misquotes the SK 2021 canola CV as 0.39 (actual 0.37; 0.39 is the 2023 value). Time load is moderate: 4–6 statistics plus three short-answer parts each.

**Section 2 — Conditional Functions & Lookups (Q31–60).** Clean numerically — all counts, AVERAGEIF/COUNTIFS/SUMIFS results verified (Q32's 1483/10039/181, Q34's 1204, Q41's 2960/2398, Q51's 22,085,300, etc.). Two systematic quibbles: several stems say `AVERAGEIF`/`SUMIF`/`COUNTIF` where the task needs the plural-S versions (Q51, Q56, Q57, Q59 — the answers quietly switch to `SUMIFS`/`AVERAGEIFS`), and the XLOOKUP-returns-0-on-blank behaviour contradicts the stated answers in Q46/Q54. Critical-thinking level is good but slightly below Section 1 — more parts are "explain the function's behaviour."

**Section 3 — Charts (Q61–90).** Well designed: every question demands a built chart *plus* reading it. Numeric anchors verified (Q62 IQRs 41.4/27.1/22.3; Q71 fence 30.35; Q81 Ontario median 46.5, BC IQR 11.0; Q82/89 national 2021 lows). The section's one real defect is the "lowest year" error in Q69 (2002, not 2021), which also muddies Q63(c)/Q73(c). Q72 is the heaviest single question in the bank. Chart questions carry the most fixed time cost; two prose-light parts each would still test the same skills.

**Section 4 — PivotTables (Q91–120).** Excellent, especially Q91 (the lentils lb/ac unit trap — the single best critical-thinking question in the bank) and the yield-vs-acres pairs (Q111/113/120). All pivot values verified (Q91 lentils 1314; Q97 ranking; Q111/115 provincial orders exact; Q113 acres exact). Errors: Q100's "lowest year 2021" (actual 2002) and Q101's highest-average variety. Q109's "top varieties" is ambiguous and its stated answer (SY MANNESS tallest) contradicts Q75's top-6-by-count framing (where AAC Wheatland is tallest).

---

## Per-Question Review

### Q1 — Descriptive · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 33.88, median 35.50, SD 13.33, IQR 22.30 (Q1 22.60, Q3 44.90), min 3.4.
- **Critical thinking:** High — mean-vs-median skew inference, robust-spread choice, defending a "typical RM" statistic.
- **Notes:** Model question for the section.

### Q2 — Descriptive · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — Canola 33.88/13.33 (CV 0.394); Barley 54.56/24.60 (CV 0.451).
- **Critical thinking:** High — the raw-SD-vs-CV trap plus a plain-language communication task.
- **Notes:** —

### Q3 — Descriptive · SK RM
- **Sense:** OK — drought/normal years stated in the question.
- **Answer check:** ✅ verified — 2019: 40.78/42.10, SD 8.17, CV 0.200; 2021: 21.86/22.80, SD 8.14, CV 0.373.
- **Critical thinking:** High — same SD, very different CV: a genuinely instructive contrast.
- **Notes:** (d) is the bank's closest brush with agronomy, but the parenthetical hint ("which RMs get rain") makes it pure reasoning. No violation.

### Q4 — Descriptive · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 71.14, median 75.90, P90 116.72, Q1 44.98, Q3 96.50, IQR 51.52, ratio 0.72.
- **Critical thinking:** Medium — mostly computation; (b)/(e) interpretation is solid.
- **Notes:** (a) and (d) both ask for mean and median — redundant; drop from one part.

### Q5 — Descriptive · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 23.62, median 23.64, SD 5.62, CV 0.238, range 40.15−4.25=35.9, IQR 6.98 (≈7.0).
- **Critical thinking:** Medium-High — fragility of the range, scale-fair comparison.
- **Notes:** —

### Q6 — Descriptive · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 21.69, median 17.20, CV 0.572.
- **Critical thinking:** High — right-skew contrast with Q1's left skew; "what the mean hides" is a strong prompt.
- **Notes:** (d)'s "one of the highest CVs of any crop-year" is plausible but unverified as a superlative; soften to "a very high CV."

### Q7 — Descriptive · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — Wheat 42.87/17.22 (CV 0.402), Peas 33.96/13.19 (CV 0.388); wheat median 45.80 (> mean → left skew), peas median 33.50 (≈ mean).
- **Critical thinking:** High — (e)'s "what the CV does and does not support about risk" is excellent.
- **Notes:** —

### Q8 — Descriptive · SK RM
- **Sense:** Issue — part (c)'s premise ("pooled SD is larger than the SD within any single year") is factually false in this data.
- **Answer check:** ❌ WRONG — (a) median stated ≈28.60, actual **26.90** (mean 28.29 ✅). ❌ (b)/(c): pooled SD = **10.06**, which is *smaller* than 2022's (12.38) and 2023's (13.33) within-year SDs. (d) verified: 1995 = 19.21, 2020 = 38.23.
- **Critical thinking:** High in intent (decomposing pooled spread) — but the data doesn't cooperate.
- **Notes:** Rewrite (b)/(c): either compare pooled SD to a *low-spread* year (e.g. 2019, SD 8.17), or reframe as "why pooling adds a between-year component" without claiming pooled SD exceeds every year.

### Q9 — Descriptive · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — Q1 32.60, Q3 74.00, IQR 41.40, fences −29.5 / 136.1, **0** outliers, min 2.9.
- **Critical thinking:** High — the "genuinely low value not flagged" insight is the best outlier question in the bank.
- **Notes:** Moderately heavy (fences + a count over 285 rows); fine alone, watch pairings.

### Q10 — Descriptive · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — 2015: 37.02/37.49, SD 8.67, CV 0.234; 2019: 49.23/50.05, SD 11.11, CV 0.226.
- **Critical thinking:** Medium — (d) "name one factor" is generic; the rest is standard.
- **Notes:** —

### Q11 — Descriptive · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 61.16, median 62.20, SD 12.38, IQR 15.70, CV 0.203; SK 2023 canola CV 0.394 for the cross-reference.
- **Critical thinking:** High — cross-dataset CV comparison with a "cite the numbers" requirement.
- **Notes:** —

### Q12 — Descriptive · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — P90 75.8, min 4.5, (61.16−4.5)/12.38 = 4.58 ≈ 4.6 SDs.
- **Critical thinking:** High — z-distance of an extreme, mean-vs-median sensitivity.
- **Notes:** —

### Q13 — Descriptive · MB Wheat
- **Sense:** Minor issue — (e) states the SK canola CV "jumped to about 0.39 in the 2021 drought"; the 2021 CV is **0.37** (0.39 is the *2023* value).
- **Answer check:** ✅ core figures verified — 2021: 49.64/50.55, SD 12.20, CV 0.246; 2023: 61.42/61.90, SD 11.27, CV 0.184. ❌ the 0.39-in-2021 premise (actual 0.373).
- **Critical thinking:** High — relative disturbance comparison across datasets.
- **Notes:** Change "0.39" to "0.37" in the stem and answer (conclusion unchanged).

### Q14 — Descriptive · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 59.62, median 61.0, SD 11.12, CV 0.186 (≈0.19); pooled CV 0.203.
- **Critical thinking:** Medium-High — within- vs between-variety spread.
- **Notes:** —

### Q15 — Descriptive · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — SY MANNESS 72.12 (SD 11.49, n 108); AAC Brandon 59.62 (SD 11.12, n 519); gap 12.5.
- **Critical thinking:** High — sample-size-vs-average reasoning; foreshadows inference nicely.
- **Notes:** —

### Q16 — Descriptive · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 61.42, median 61.90, CV 0.184; Q1 55.10, Q3 69.25, IQR 14.15; lower fence 33.88; **7** values below (4.5, 18.7, 22.0, 25.6, 29.4, 32.6, 33.1).
- **Critical thinking:** High — the tight-bulk-vs-wide-bulk outlier contrast with Q9 is excellent.
- **Notes:** Slightly heavy (fence + identifying the 7 values).

### Q17 — Descriptive · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — 2398 TRUE, 2960 FALSE, 5358 total.
- **Critical thinking:** High — data-literacy question (suppression vs measurement) done entirely from the file.
- **Notes:** —

### Q18 — Descriptive · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — 2025: 68.03/69.00, SD 11.84, CV 0.174; 2021 49.64 → gap ≈18.4.
- **Critical thinking:** Medium-High — composition-change caveat in (d)/(e) is good.
- **Notes:** —

### Q19 — Descriptive · MB Wheat
- **Sense:** OK — the "(eleven varieties…)" parenthetical helpfully confirms the filter worked.
- **Answer check:** ✅ verified — n=11, mean 71.67, range 87.7−43.4 = 44.3.
- **Critical thinking:** High — holding environment constant to isolate variety differences.
- **Notes:** —

### Q20 — Descriptive · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — Brandon n 519, mean 59.62, CV 0.186; Starbuck n 374, mean 62.70, CV 0.180.
- **Critical thinking:** Medium-High — separates precision (count) from representativeness (CV).
- **Notes:** —

### Q21 — Descriptive · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 51.32, median 50.90 (stated 50.8 — trivial rounding), range 33.7–73.9, SD 7.52, CV 0.147.
- **Critical thinking:** High — "a mean that describes no actual province" is a strong idea.
- **Notes:** —

### Q22 — Descriptive · Field Crops
- **Sense:** OK — (c)/(d) rest on a stated premise about the raw table (not checkable by students, but answerable as given).
- **Answer check:** ✅ verified — mean 41.04, SD 5.35, CV 0.130; spring wheat CV 0.147 for the comparison.
- **Critical thinking:** High — zero-vs-missing is a core data-quality lesson.
- **Notes:** —

### Q23 — Descriptive · Field Crops
- **Sense:** OK — deliberately meaningless mean, clearly signposted.
- **Answer check:** ✅ verified — mean 45.05, median 40.40.
- **Critical thinking:** High — "what must be held constant before an average means anything."
- **Notes:** —

### Q24 — Descriptive · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Barley 64.24/9.10 (CV 0.142); Soybeans 39.56/9.08 (CV 0.229). The near-identical SDs are a genuinely lucky teaching accident.
- **Critical thinking:** High — the cleanest same-SD/different-CV demonstration possible.
- **Notes:** One of the best questions in the bank.

### Q25 — Descriptive · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021 mean 34.25, median 32.65; below the all-years 41.04. Note only 6 provinces report canola in 2021.
- **Critical thinking:** Medium-High — aggregation-smoothing insight in (d)/(e).
- **Notes:** Answer (a) gives no number ("below the long-run figure") — students may want the value (34.3) to check against.

### Q26 — Descriptive · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Ontario 46.72, Saskatchewan 39.09 (gap 7.6); SK 2023 acres 12,400,400 vs ON 45,100.
- **Critical thinking:** High — the rate-vs-total flagship.
- **Notes:** —

### Q27 — Descriptive · Field Crops
- **Sense:** Minor ambiguity — (c) says "compare to what you saw for oats in the Saskatchewan RM data" without specifying the year. SK 2023 oats are left-skewed (71.1 < 75.9) as the answer assumes, but SK oats *pooled across all years* are right-skewed (64.7 > 61.8).
- **Answer check:** ✅ verified — mean 79.41, median 75.90, CV 0.193; Q1 68.60, Q3 90.80, IQR 22.20.
- **Critical thinking:** High — aggregation level changing apparent shape is subtle and good.
- **Notes:** Pin (c) to "the 2023 SK oats data (Question 4)."

### Q28 — Descriptive · Field Crops
- **Sense:** Issue — answer contradicts Q55 (which correctly says 66).
- **Answer check:** ❌ WRONG — (a) stated ≈185 blank-yield rows; actual **66**. ❌ (b) blanks do NOT concentrate in "flax, durum, canola": actual counts are Mixed grains 21, Rye 15, Dry peas 7, Oats 5, Corn 5, Durum 4, Barley 3, Canola 1, **Flax 0**. (Provinces are right: NL 17, NB 14, PEI 11 lead.) Flax/durum eastern rows are *absent from the file*, not blank — a distinction worth teaching explicitly.
- **Critical thinking:** High in intent — blank-vs-absent-row is a great lesson once the numbers are fixed.
- **Notes:** Fix both numbers; consider adding "note that crops never grown in a province may have no row at all."

### Q29 — Descriptive · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 40.61, CV 0.287; **5** provinces report durum (AB, BC, MB, QC, SK) vs 8 for canola.
- **Critical thinking:** High — "how many contribute to the average" honesty check.
- **Notes:** —

### Q30 — Descriptive · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 58.68, median 55.20 (9 provinces), SD 8.98, CV 0.153; highest Manitoba 75.4, lowest Quebec 46.1, gap 29.3.
- **Critical thinking:** Medium — mostly reading and restating; (e) is a good communication close.
- **Notes:** —

### Q31 — Conditional · SK RM
- **Sense:** OK — 2023 does have 6 blank canola cells (295 rows, 289 reported), so (d)'s premise holds.
- **Answer check:** ✅ verified — 2010: 29.82, 2019: 40.78, 2021: 21.86.
- **Critical thinking:** High — (c)'s "design the data check" is a genuinely good investigative prompt.
- **Notes:** —

### Q32 — Conditional · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — >40: 1483; non-blank: 10,039; proportion 0.148; >50: 181.
- **Critical thinking:** Medium-High — threshold counts as a tail description; reported-only caveat.
- **Notes:** —

### Q33 — Conditional · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — RM 1 / 2023 canola = 36.8; RM 100 / 2023 spring wheat = 52.9; RM 1 appears in 36 years.
- **Critical thinking:** Medium-High — composite-key logic; (d)'s two data reasons is good.
- **Notes:** —

### Q34 — Conditional · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — both conditions: 1204; canola alone: 1483.
- **Critical thinking:** Medium — joint-vs-marginal counting; conceptually solid, mechanically light.
- **Notes:** —

### Q35 — Conditional · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — RM 1: 56.56, RM 100: 43.89 (gap 12.7); both report 35 years of barley.
- **Critical thinking:** Medium-High — grouping-direction awareness (per-RM vs per-year).
- **Notes:** —

### Q36 — Conditional · SK RM
- **Sense:** Minor — (d) asks about left-skew logic but the pooled canola column is *right*-skewed (mean 28.29 > median 26.90), so the observed fraction (0.45) illustrates the opposite case. The answer acknowledges this but reads awkwardly.
- **Answer check:** ✅ verified — overall mean 28.29; count above 4519; fraction 0.450.
- **Critical thinking:** High — "above the mean ≠ 50%" plus the `">"&AVERAGE()` syntax trap.
- **Notes:** Reword (d) to "for a skewed distribution, explain why the fraction above the mean is not one-half, and state which side this data lands on."

### Q37 — Conditional · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — canola 36.06 → 40.78 (+4.72); barley 55.25 → 68.59 (+13.34).
- **Critical thinking:** Medium-High — absolute vs relative change.
- **Notes:** —

### Q38 — Conditional · SK RM
- **Sense:** OK — boundary conventions (20 and 40 inclusive to Medium) match the answer formula.
- **Answer check:** ✅ verified — Low (<20): 2037; Medium (20–40): 6519; High (>40): 1483; Medium most common, consistent with mean 28.3.
- **Critical thinking:** Medium — formula construction plus one interpretive link.
- **Notes:** Heaviest formula-writing question (nested IF/IFS + blank guard + three counts); watch pairings.

### Q39 — Conditional · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — canola 10,039; flax 8,077; difference 1,962.
- **Critical thinking:** Medium — coverage as a statistic; COUNT vs COUNTA rationale.
- **Notes:** (a) wording "Use COUNTIF to count non-blank cells… (`COUNT` on each column)" is self-contradictory — just say COUNT.

### Q40 — Conditional · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021: 21.86, 2023: 33.88; below-20 counts: 2021 = **120** of 290 (41%), 2023 = **57**. Minor: answer calls 120/290 "roughly a third" — it is over 40%.
- **Critical thinking:** Medium-High — fixed-threshold comparison logic.
- **Notes:** Change "roughly a third" to "about 40%".

### Q41 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — 2960 FALSE, 2398 TRUE, 2398/5358 = 0.448.
- **Critical thinking:** High — (e)'s "one calculation unaffected / one conclusion biased" is a great design.
- **Notes:** —

### Q42 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 59.62; 519 reported; 51 suppressed; 570 total.
- **Critical thinking:** Medium-High — average-vs-coverage separation.
- **Notes:** —

### Q43 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — GLENN: 4 reported, 96 suppressed, exactly 4/100 = 4%.
- **Critical thinking:** High — fragility of a 4-observation average.
- **Notes:** The clean 4/96/100 split is a nice accident.

### Q44 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — >70: 569 (0.237); >80: 97 (0.040); total 2398.
- **Critical thinking:** Medium-High — sketching a tail with threshold counts.
- **Notes:** —

### Q45 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021: 49.64 (n 396); 2023: 61.42 (n 423).
- **Critical thinking:** Medium-High — composition caveat for year comparisons.
- **Notes:** —

### Q46 — Conditional · MB Wheat
- **Sense:** Issue — Excel behaviour. `XLOOKUP` (and `INDEX/MATCH`) on an *empty* return cell returns **0**, not a blank. The stated answer to (b) ("returns a blank … no number") is wrong in real Excel, and ironically the returned 0 is the exact blank-read-as-zero trap the bank teaches against.
- **Answer check:** ✅ (a) verified — Brandon/ALONSA/2020 = 65.1. ❌ (b) as stated: a suppressed lookup displays **0** unless wrapped (e.g. `IF(cell="","",…)`).
- **Critical thinking:** High — checking `Reported` before trusting a lookup is a great habit; even better once the 0-return is taught.
- **Notes:** Rewrite (b)/(c) around the 0-return behaviour — it makes the question *stronger*.

### Q47 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — SY MANNESS 72.12 (108); Brandon 59.62 (519).
- **Critical thinking:** Medium — near-duplicate of Q15's reasoning with different functions.
- **Notes:** —

### Q48 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — counts 2020–2025: 94, 90, 87, 83–84, 83, 81; highest 2020.
- **Critical thinking:** Medium — (d) is slightly confusingly worded (the answer explains averages already normalize by count).
- **Notes:** Six COUNTIFS = a bit repetitive; consider asking for three years.

### Q49 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 >70: 96 of 423 (0.23).
- **Critical thinking:** Medium — proportion-vs-count comparability.
- **Notes:** Answer (a) says only "a moderate count" — state 96 so students can self-check.

### Q50 — Conditional · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — Starbuck 374 reported; 374/2398 = 0.156.
- **Critical thinking:** High — trial-share ≠ acreage-share is a sharp external-validity point.
- **Notes:** —

### Q51 — Conditional · Field Crops
- **Sense:** Minor — stem says `SUMIF` but the task needs two criteria (Crop AND Year); the answer correctly says SUMIFS/filter.
- **Answer check:** ✅ verified — 2023 canola total 22,085,300; SK 12,400,400 (56%).
- **Critical thinking:** High — (d) "acres add, yields don't" is essential; (e) previews weighted averages.
- **Notes:** Say `SUMIFS` in the stem.

### Q52 — Conditional · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — canola 22,085,300; spring wheat 19,496,400; barley 7,330,600.
- **Critical thinking:** Medium-High — scale vs productivity.
- **Notes:** —

### Q53 — Conditional · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Ontario 46.72, SK 39.09; SK 2023 acres 12,400,400 vs ON 45,100.
- **Critical thinking:** Medium-High — rate-vs-total again (near-duplicate of Q26 with different functions).
- **Notes:** —

### Q54 — Conditional · Field Crops
- **Sense:** Minor — same XLOOKUP-blank-returns-0 issue as Q46 in part (d) ("returns a blank yield").
- **Answer check:** ✅ verified — MB canola 2023: 44.6 bu/ac; 3,128,200 acres.
- **Critical thinking:** Medium-High — three-key uniqueness logic.
- **Notes:** Reword (d) to "returns 0 or an error."

### Q55 — Conditional · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — **66** blank-yield rows; durum blanks = 4. (This is the correct figure that Q28 contradicts.)
- **Critical thinking:** Medium-High — blank taxonomy across datasets.
- **Notes:** (b)'s answer slightly overstates ("durum blanks fall in the many provinces that do not grow it" — most such provinces have *no row*; only 4 blanks exist).

### Q56 — Conditional · Field Crops
- **Sense:** OK — "on spring wheat rows" implies filtering first; fine.
- **Answer check:** ✅ verified — 30 above 55, of 94 non-blank (0.319).
- **Critical thinking:** Medium — pooling caveat, refine-by-province.
- **Notes:** —

### Q57 — Conditional · Field Crops
- **Sense:** Minor — stem says `AVERAGEIF` but needs Crop AND Year (`AVERAGEIFS`); answer switches silently.
- **Answer check:** ✅ verified — barley 2023: 58.68 over 9 provinces; soybeans 2023: 42.41 over 7 provinces.
- **Critical thinking:** Medium-High — breadth-of-average interpretation.
- **Notes:** Answer gives no soybean number ("report your values") — fine by design, but state the check values (58.7 / 42.4) for practice use.

### Q58 — Conditional · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2020: 20,782,600; 2023: 22,085,300; change +1,302,700.
- **Critical thinking:** Medium — extensive-vs-rate quantity logic (repeat of Q51d/e).
- **Notes:** —

### Q59 — Conditional · Field Crops
- **Sense:** Minor — `AVERAGEIF` in stem, needs `AVERAGEIFS`.
- **Answer check:** ✅ verified — 2019: 40.93, 2021: 34.25, 2023: 42.44; 2021 lowest.
- **Critical thinking:** Medium-High — aggregation-smoothing (province vs RM).
- **Notes:** —

### Q60 — Conditional · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — total 19,496,400 acres; unweighted 2023 average yield 48.28.
- **Critical thinking:** High — why average × total ≠ production; the weighted-average idea without the formula.
- **Notes:** Excellent capstone for the section.

### Q61 — Charts · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — mean 33.88 < median 35.50 (left skew); low tail to 3.4.
- **Critical thinking:** High — shape → statistic choice → bin-width reasoning.
- **Notes:** —

### Q62 — Charts · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — IQRs: barley 41.4 (widest), spring wheat 27.1, canola 22.3; confirmed **zero** 1.5×IQR outliers for all three crops in 2023 (canola fences −10.85/78.35, wheat −12.15/96.25, barley −29.5/136.1).
- **Critical thinking:** High — connects box geometry to the fence arithmetic.
- **Notes:** —

### Q63 — Charts · SK RM
- **Sense:** Minor ambiguity — (c) asks for "the sharpest single-year dip." The largest one-year *drop* is 2021 (−16.4, from 38.2 to 21.9) ✅, but the *lowest point* on the chart is **2002** (15.8). Students reading "dip" as "lowest notch" will answer 2002 and be marked against the key.
- **Answer check:** ✅ verified — 1995 ≈ 19.2 rising to 43.9 by 2025; 2021 is the biggest single-year drop.
- **Critical thinking:** High — trend vs one-off separation.
- **Notes:** Add "(the largest one-year fall, not the lowest point)" or accept both 2021 and 2002.

### Q64 — Charts · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — canola and spring wheat yearly averages co-move; both dip sharply in 2021.
- **Critical thinking:** Medium-High — co-movement reading, shared-axis fairness.
- **Notes:** —

### Q65 — Charts · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — barley 2023 mean 54.56 < median 59.90 (left skew); IQR 41.4 vs canola 22.3.
- **Critical thinking:** Medium-High — visual spread comparison and the shared-scale rule.
- **Notes:** —

### Q66 — Charts · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021 lowest (median 22.8 vs 42.1 in 2019, 35.5 in 2023).
- **Critical thinking:** Medium-High — distribution-vs-mean comparison across years.
- **Notes:** —

### Q67 — Charts · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — oats 2023 mean 71.14 < median 75.90; left tail.
- **Critical thinking:** Medium-High — tallest-bars-vs-typical-value trap.
- **Notes:** —

### Q68 — Charts · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — durum 2021 mean 21.69 > median 17.20 → right skew; median line sits low in the box.
- **Critical thinking:** High — reading skew from box geometry without computing the mean.
- **Notes:** —

### Q69 — Charts · SK RM
- **Sense:** OK question; wrong key.
- **Answer check:** ❌ WRONG — (b) states the lowest year is 2021 (~35); the actual lowest barley year is **2002 (30.6 bu/ac)**; 2021 (34.8) is second. ❌ (c) "both canola and barley bottom out in 2021" — both actually bottom out in **2002** (canola 15.8). The "same year" conclusion survives, but the year is wrong.
- **Critical thinking:** High — multi-crop corroboration logic is great once the year is fixed.
- **Notes:** Either fix the key to 2002, or restrict the chart to 2015–2025 where 2021 genuinely is the low.

### Q70 — Charts · SK RM
- **Sense:** OK.
- **Answer check:** ✅ verified — spring wheat 2019 mean 49.23, median 50.05; roughly symmetric near 50.
- **Critical thinking:** Medium — eyeball-then-verify workflow; good habit, light reasoning.
- **Notes:** —

### Q71 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ mostly verified — lower fence 30.35 ✅; low-end outliers = **35** (stated "about 39" — 39 is the total including 4 high-end outliers). Minor.
- **Critical thinking:** High — histogram-vs-boxplot outlier framing.
- **Notes:** Say "about 35 low (39 total)".

### Q72 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — top six by count: Brandon 519, Starbuck 374, Wheatland 219, Hockley 177, Viewfield 165, Redberry 138; Hockley smallest IQR (12.7).
- **Critical thinking:** High — box-vs-bar audience judgment in (d) is excellent.
- **Notes:** **Heaviest question in the bank**: find top-6 by count (needs a pivot), then build a 6-category box plot. Consider pre-naming the six varieties in the stem.

### Q73 — Charts · MB Wheat
- **Sense:** Minor — (c) compares to "the low year in the SK canola line chart (Q63)"; over the full 1990–2025 SK chart the lowest year is 2002, so "same year" is only true under Q63's sharpest-drop framing.
- **Answer check:** ✅ verified — Brandon by year: 62.5, 49.1, 57.9, 60.3, 62.3, 66.3; 2021 lowest.
- **Critical thinking:** High — cross-dataset corroboration with the variety held fixed.
- **Notes:** Rephrase (c) to "the year of the sharpest dip in Q63."

### Q74 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023: 7 low outliers below fence 33.88; pooled data flags more (35).
- **Critical thinking:** Medium-High — pooling changes the fences.
- **Notes:** —

### Q75 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — among top six by count, means: Wheatland 65.8 (tallest), Hockley 64.9, Starbuck 62.7, Viewfield 62.5, Brandon 59.6, Redberry 54.4 (shortest). Answer's "~66–67" mixes in medians but names the right varieties.
- **Critical thinking:** Medium-High — zero-baseline reasoning.
- **Notes:** Note the inconsistency with Q109's answer (which crowns SY MANNESS — not in this top six).

### Q76 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ no fixed numeric claims (2025 reference values: median 69.0, Q1 61.2, Q3 75.98).
- **Critical thinking:** Medium — chart-reading vs exact computation.
- **Notes:** —

### Q77 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — Brandon and Starbuck co-move; both dip 2021 (49.1 / 51.3); Starbuck above in all six years.
- **Critical thinking:** Medium-High — shared-conditions reasoning.
- **Notes:** —

### Q78 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — Brandon IQR 13.0 vs pooled 15.7; centre ≈ 60.
- **Critical thinking:** High — part-vs-whole spread decomposition.
- **Notes:** —

### Q79 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — yearly medians: 63.7, **50.6 (2021 lowest)**, 60.8, 61.9, 66.2, 69.0.
- **Critical thinking:** Medium-High — distribution-over-time vs a line of means.
- **Notes:** —

### Q80 — Charts · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ conceptual; count data verified (top-six counts as in Q72).
- **Critical thinking:** High — chart-choice justification, pie-chart limits.
- **Notes:** —

### Q81 — Charts · Field Crops
- **Sense:** OK — note PEI has very few canola observations (IQR 0.0), a good live example for (e)-style caveats.
- **Answer check:** ✅ verified — Ontario highest median (46.5); BC widest IQR (11.0).
- **Critical thinking:** High — headline-evaluation ("best canola") plus the missing-scale caveat.
- **Notes:** —

### Q82 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — national canola by year dips to 34.2 in 2021 (≈40–42 around it).
- **Critical thinking:** Medium-High — cross-dataset triangulation of 2021.
- **Notes:** —

### Q83 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023: Ontario 53.4 tallest; BC 35.1 shortest (SK 37.4 near bottom).
- **Critical thinking:** Medium — baseline rule plus snapshot-vs-distribution contrast.
- **Notes:** —

### Q84 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ no fixed numeric claims; data supports the task (9–10 provinces report barley).
- **Critical thinking:** Medium-High — reliability of a box built on few points.
- **Notes:** —

### Q85 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — national spring wheat also bottoms in 2021 (45.7); canola 34.2. Both dip 2021.
- **Critical thinking:** Medium — co-movement plus legend/axis discipline.
- **Notes:** —

### Q86 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — pooled canola mean 41.04, median 41.65 (roughly symmetric, low 40s).
- **Critical thinking:** Medium-High — pooling-blurs-structure.
- **Notes:** —

### Q87 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — SK 12.4M acres towers; Ontario leads yield; leaders differ.
- **Critical thinking:** High — rate-vs-total in chart form.
- **Notes:** —

### Q88 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ no fixed numeric claims; COUNTIFS check described correctly.
- **Critical thinking:** Medium-High — observation-count skepticism.
- **Notes:** —

### Q89 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — national barley lowest 2021 (56.1) within 2015–2025; same low year as canola. (No 2002 problem here — this dataset starts in 2015.)
- **Critical thinking:** Medium — repeat of the shared-worst-year motif.
- **Notes:** —

### Q90 — Charts · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — SK canola lowest 2021 (25.8), a deeper dip than the national 34.2.
- **Critical thinking:** Medium-High — province-vs-national divergence.
- **Notes:** —

### Q91 — Pivot · SK RM (long)
- **Sense:** OK. (Note: the dataset blurb at the top of the bank says the wide file is "bu/ac for eight crops" — lentils are lb/ac; fix the blurb so it doesn't spoil or contradict this question.)
- **Answer check:** ✅ verified — 2023 averages: Lentils 1314.3 (lb/ac!), Oats 71.1, Barley 54.6, Spring Wheat 42.9, Peas 34.0, Canola 33.9, Durum 29.6, Flax 20.3; filtered to bu/ac: Oats highest, Flax lowest.
- **Critical thinking:** High — the best unit-trap question in the bank; no ag knowledge needed (the anomaly is 18× out of line).
- **Notes:** Flagship question — keep.

### Q92 — Pivot · SK RM (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — canola 21.9 (2021) vs 33.9 (2023), a 35% drop; entire 2021 row depressed (barley 34.8, oats 45.1, wheat 30.2, flax 12.8…).
- **Critical thinking:** High — row-vs-cell causal reading is excellent.
- **Notes:** —

### Q93 — Pivot · SK RM (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — 2019→2025 changes: Oats +8.05 (97.5−89.4), Barley +4.25 (72.8−68.6), Canola +3.16 (43.9−40.8); Oats largest absolute rise (Flax +6.1 is second — worth noting since its *relative* rise is the largest, which strengthens (d)).
- **Critical thinking:** High — absolute-vs-relative change with real numbers.
- **Notes:** Heavy: two pivots plus differences over 7 crops. Consider limiting to 3 named crops.

### Q94 — Pivot · SK RM (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — recent-year canola counts: 289–293 (≈290).
- **Critical thinking:** Medium — Count-vs-Average distinction.
- **Notes:** —

### Q95 — Pivot · SK RM (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 counts: Canola 289 (most), SW/Barley 285, Peas 282, Oats 200, Durum 173, Flax 164 (fewest). Minor: the answer's example ("Spring Wheat/Barley high") skips that canola is actually the most-reported.
- **Critical thinking:** Medium-High — reliability weighting via a Count column.
- **Notes:** Update the answer example to "Canola/Spring Wheat/Barley high; Flax fewest."

### Q96 — Pivot · SK RM (long)
- **Sense:** OK — the 2019–2023 window dodges the 2002 problem correctly.
- **Answer check:** ✅ verified — within 2019–2023 both canola (21.9) and barley (34.8) bottom in 2021.
- **Critical thinking:** Medium-High — grid-scanning for a broad event.
- **Notes:** —

### Q97 — Pivot · SK RM (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — all-years ranking: Oats 64.7 > Barley 51.8 > Spring Wheat 35.3 > Durum 33.6 > Peas 31.8 > Canola 28.3 > Flax 20.5; 2023 order shuffles Durum/Peas/Canola in the middle.
- **Critical thinking:** Medium-High — stability of long-run vs single-year rankings.
- **Notes:** —

### Q98 — Pivot · SK RM (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — oats 2019–2025: highest 2025 (97.5), lowest 2021 (45.1).
- **Critical thinking:** Medium-High — (d)/(e) "why not Sum" is a key pivot lesson.
- **Notes:** —

### Q99 — Pivot · SK RM (long)
- **Sense:** OK.
- **Answer check:** ✅ verified — 2021 ranking exactly as stated: Oats 45.1 > Barley 34.8 > SW 30.2 > Peas 22.5 > Canola 21.9 > Durum 21.7 > Flax 12.8; Oats top in both years.
- **Critical thinking:** High — level-vs-ranking distinction is subtle and well posed.
- **Notes:** —

### Q100 — Pivot · SK RM (long)
- **Sense:** OK question; wrong key.
- **Answer check:** ❌ WRONG — (b) states the lowest year is 2021; over the full 1990–2025 series the lowest canola year is **2002 (15.8 bu/ac)**; 2021 is 21.9. (2001: 18.2 and 2003: 17.0 are also below 2021.)
- **Critical thinking:** Medium — PivotChart mechanics plus trend reading.
- **Notes:** Fix key to 2002, or scope the chart to 2015–2025.

### Q101 — Pivot · MB Wheat
- **Sense:** Minor structural issue — the min-count filter arrives only in (e), so (b)'s "highest average" is over *all* varieties.
- **Answer check:** ❌ WRONG — (b) highest average is **AAC WESTKING (79.2 bu/ac, n=17, 2025 only)**, not SY MANNESS (72.1, n=108). Also above SY MANNESS: CDC GO 77.5 (n=1) and AAC SPIKE 73.2 (n=2). Most-reported = AAC Brandon (519, mean 59.6) ✅.
- **Critical thinking:** High — and the *actual* data makes the point even better: the unfiltered "winner" rests on 17 reports from a single year.
- **Notes:** Fix the key — or embrace it: "the top of the unfiltered list is a variety with 17 reports from one year; explain why (e)'s filter dethrones it."

### Q102 — Pivot · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — Brandon 2021 = 49.1 vs 57.9–66.3 in other years; Starbuck 2021 = 51.3 (also its low).
- **Critical thinking:** High — isolating year effects by fixing variety.
- **Notes:** Answer's "~62–66 in other years" glosses 2022's 57.9; harmless.

### Q103 — Pivot · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — top three counts: Brandon 519, Starbuck 374, Wheatland 219.
- **Critical thinking:** Medium — coverage-first workflow.
- **Notes:** —

### Q104 — Pivot · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — yearly means 62.4, 49.6 (lowest 2021), 59.8, 61.4, 64.7, 68.0 (highest 2025).
- **Critical thinking:** Medium-High — composition caveat plus Count column.
- **Notes:** —

### Q105 — Pivot · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ no fixed numeric claims; data confirms the lesson vividly (2023 "top" municipality ALEXANDER 84.2 rests on n=1; "bottom" WEST INTERLAKE 22.0 also n=1).
- **Critical thinking:** High — thin-average trap materializes perfectly in the real data.
- **Notes:** Consider adding those two n=1 municipalities to the answer as worked examples.

### Q106 — Pivot · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ no fixed numeric claims (2025 leaders among n≥5: WESTKING 79.2, Viewfield 73.5, SY MANNESS 72.6).
- **Critical thinking:** Medium — ranking stability, repeat of Q97's motif.
- **Notes:** —

### Q107 — Pivot · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — with n≥30: highest SY MANNESS 72.1; lowest AAC Tisdale 53.9 / Redberry 54.4.
- **Critical thinking:** High — the filter-as-quality-control idea; pairs perfectly with (a corrected) Q101.
- **Notes:** —

### Q108 — Pivot · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — Starbuck beats Brandon in **all six** years (70.7/62.5, 51.3/49.1, 61.9/57.9, 63.8/60.3, 66.2/62.3, 68.4/66.3).
- **Critical thinking:** High — consistent-advantage vs one-year-fluke logic; a quiet preview of inference.
- **Notes:** —

### Q109 — Pivot · MB Wheat
- **Sense:** Issue — "top varieties" is undefined. If it means top-6 by count (as in Q72/Q75), SY MANNESS is excluded and the tallest bar is AAC Wheatland (65.8); the stated answer (tallest = SY MANNESS) implicitly uses a different set, contradicting Q75's answer.
- **Answer check:** ⚠️ conditional — correct only if SY MANNESS is included in the chosen set; wrong under the top-6-by-count reading.
- **Critical thinking:** Medium — repeat of Q75's content in PivotChart form.
- **Notes:** Define the set in the stem ("the six most-reported varieties" → tallest Wheatland, shortest Redberry — and update the key).

### Q110 — Pivot · MB Wheat
- **Sense:** OK.
- **Answer check:** ✅ verified — Brandon: 519 TRUE / 51 FALSE.
- **Critical thinking:** High — (d) "impossible if you deleted the rows" is a clever design lesson.
- **Notes:** —

### Q111 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified exactly — 2023 canola: Ontario 53.4, NB 45.6, MB 44.6, QC 40.9, AB 40.1, SK 37.4, BC 35.1; SK acres 12.4M vs ON 45,100.
- **Critical thinking:** High — yield-vs-importance with a two-value pivot.
- **Notes:** —

### Q112 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — SK 2021 canola 25.8 (vs 37.4–44.4 other years); the 2021 column is low across the 6 reporting provinces (mean 34.25).
- **Critical thinking:** High — local-vs-broad diagnosis from a grid.
- **Notes:** —

### Q113 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified exactly — SK 12,400,400 (56%), AB 6,362,800, MB 3,128,200, BC 108,600, ON 45,100, QC 38,600, NB 1,600.
- **Critical thinking:** Medium-High — rate-vs-total (third pivot repetition of the motif).
- **Notes:** —

### Q114 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — Corn for grain 135.6 highest, Oats 79.4, Barley 64.2, … Flax 25.6 lowest.
- **Critical thinking:** Medium-High — per-acre productivity ≠ scale.
- **Notes:** —

### Q115 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified exactly — ON 46.7, NB 44.0, MB 41.5, QC 41.4, PEI 40.7, AB 40.1, SK 39.1, BC 35.5; Ontario tops both all-years and 2023.
- **Critical thinking:** Medium — ranking stability repeat.
- **Notes:** —

### Q116 — Pivot · Field Crops
- **Sense:** OK — genuinely open (b): the honest description is "roughly flat, fluctuating 20.8–23.0M with no clear trend," which itself is a fine answer.
- **Answer check:** ✅ verified — yearly totals range 20.78M (2015/16/20) to 23.01M (2017).
- **Critical thinking:** Medium-High — Sum-vs-Average aggregation choice.
- **Notes:** Answer could state the flat-trend conclusion so TAs grade consistently.

### Q117 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — 2023 spring wheat acres: SK 9.14M > AB 6.80M > MB 3.17M; yields: ON 64.7 and MB 62.8 top, SK mid-pack (46.9) — SK is the natural "high acres, not high yield" example.
- **Critical thinking:** Medium-High — contribution = acres × yield.
- **Notes:** —

### Q118 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ mostly verified — high counts: Oats 101, Barley 99, Wheat (all) 99, Spring wheat 94; low: Durum 34, Flax 39. Minor: the answer lists **canola** among the high-count crops, but canola is mid-pack (74).
- **Critical thinking:** Medium — coverage check before trusting averages.
- **Notes:** Swap "canola" for "oats" in the answer's examples.

### Q119 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — SK leads every recent year (~12M+); SK's row fluctuates 10.9–12.4M-ish with no dramatic trend.
- **Critical thinking:** Medium — grid reading; Sum-vs-Average repeat.
- **Notes:** —

### Q120 — Pivot · Field Crops
- **Sense:** OK.
- **Answer check:** ✅ verified — highest Ontario (46.7), lowest BC (35.5); SK towers on the companion acres chart.
- **Critical thinking:** High — the two-chart storytelling close is a strong capstone.
- **Notes:** —

---

## Prioritized Fix List

1. **Q69 (Charts · SK RM)** — ❌ Lowest barley year is **2002 (30.6)**, not 2021 (34.8); and both crops bottom in 2002, not 2021. Fix the key or restrict the chart window to 2015–2025.
2. **Q100 (Pivot · SK RM)** — ❌ Lowest canola year is **2002 (15.8)**, not 2021 (21.9). Same fix options as Q69.
3. **Q8 (Descriptive · SK RM)** — ❌ Median is **26.90**, not 28.60; and the (b)/(c) premise is false (pooled SD 10.06 < 2022's 12.38 and 2023's 13.33). Rewrite (b)/(c) around a low-spread comparison year (e.g. 2019, SD 8.17).
4. **Q28 (Descriptive · Field Crops)** — ❌ Blank-yield rows = **66** (not 185; contradicts Q55); blanks concentrate in **Mixed grains (21) and Rye (15)** — flax has zero blanks. Rework (b) and consider teaching blank-cell vs absent-row.
5. **Q101 (Pivot · MB Wheat)** — ❌ Unfiltered highest average is **AAC WESTKING (79.2, n=17)**, not SY MANNESS. Fix the key, or rewrite (b) to exploit the thin-data winner deliberately.
6. **Q46 and Q54 (Conditional)** — XLOOKUP on an empty cell returns **0**, not blank; the stated answers are wrong in real Excel. Rewriting around the 0-return makes both questions stronger.
7. **Q63 (Charts · SK RM)** — Clarify "sharpest single-year dip" (2021, the −16.4 drop) vs the lowest point (2002); accept both or specify. Also touch Q73(c), which inherits the framing.
8. **Q109 (Pivot · MB Wheat)** — Define "top varieties"; under the top-6-by-count reading the tallest bar is **AAC Wheatland**, contradicting the stated SY MANNESS and Q75's key.
9. **Q13 (Descriptive · MB Wheat)** — (e)'s quoted SK 2021 canola CV should be **0.37**, not 0.39 (0.39 is 2023).
10. **Q72 and Q93** — Not errors, but the two heaviest questions; trim (pre-name the six varieties in Q72; limit Q93 to three crops) to protect the 50-minute budget.
11. **Small answer-text touch-ups** — Q40 ("roughly a third" → "about 40%": 120/290), Q71 ("about 39 low-end" → 35 low, 39 total), Q95 (canola is the most-reported 2023 crop), Q118 (canola is mid-count, not high), Q21 (median 50.9), Q36 (reword (d) — pooled canola is right-skewed here), Q27 (pin the SK oats comparison to 2023/Q4), Q39 (say COUNT, not COUNTIF, in (a)), Q51/Q57/Q59 (say SUMIFS/AVERAGEIFS in stems), dataset blurb (wide file is *not* all bu/ac — lentils are lb/ac; don't contradict Q91).
