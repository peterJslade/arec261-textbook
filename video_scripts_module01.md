# Module 1 — Video Scripts

One video per major section of Module 1. Each is short and self-contained, so they can be re-recorded individually and knit into a full-chapter video.

**Datasets used (all in `practice/data/`):**

- **`video_barley.csv`** — the "teaching slice": Saskatchewan Risk Zone 6, **Barley only, 2025**. Just 9 varieties, three columns (`Variety`, `Acres`, `Yield_bu_ac`). Small enough to show the whole thing on screen. Used for the descriptive-statistics and cell-mechanics videos.
- **`video_full.csv`** — the "expanded slice": Zone 6, **all crops, all years 2021–2025** (385 rows, adds a `Year` and multiple `Crop`s). Used for PivotTables, charts, filtering, and wide-vs-long — the sections that need volume and categories to be meaningful.

*(Both are carved from the real SCIC "Sask Management Plus" variety data — `sask_variety_yields.csv`.)*

**The barley slice, for reference (you'll have this open):**

| Variety | Acres | Yield (bu/ac) |
|---------|------:|------:|
| ADVANTAGE AB | 406 | 58.4 |
| AUSTENSON CDC | 8,917 | 49.0 |
| CHAMPION | 1,056 | 51.6 |
| COPELAND CDC | 4,273 | 54.6 |
| COWBOY CDC | 1,069 | 26.3 |
| FRASER CDC | 1,286 | 77.1 |
| MAVERICK CDC | 7,154 | 35.4 |
| RENEGADE CDC | 2,540 | 31.7 |
| SYNERGY AAC | 18,677 | 48.5 |

**Key barley numbers (verified — read these off with confidence):**

- Total acres: **45,378** · Mean yield: **48.07** · Median yield: **49.0**
- Std dev (sample): **15.44** · Variance: **238.4** · CV: **0.32**
- Min **26.3** (COWBOY CDC) · Max **77.1** (FRASER CDC) · Range **50.8**
- Q1 **35.4** · Q3 **54.6** · IQR **19.2** · 90th percentile **~62**
- Total production (Σ yield×acres): **≈ 2,115,308 bu**

Each script below has: **① what's on screen**, **② the exact steps**, **③ the number that should appear**, and **④ what to say**. Timings are rough targets.

---

## Video 1 — What Is Excel, Really? *(~3–4 min, no data file needed)*

**On screen:** a blank Excel window; optionally the barley CSV opened at the end.

**Talk:**
- Frame Excel as three things at once: a **calculator**, a **database** (tables you can sort/filter/summarize), and a **little programming environment** (every formula is a tiny program).
- The one big idea: a cell holds either a **value** or a **formula** that computes from other cells — change an input, everything updates.
- Contrast with a paper ledger: before spreadsheets you re-did the whole calculation by hand.
- Set expectations for the course: Excel is great for small-to-medium, see-everything work; later we move to R for the heavy lifting.

**Do on screen:** type `=2+2` in a cell, hit enter, show it returns 4. Change a referenced cell and show a dependent formula update. That's the whole magic in 20 seconds.

---

## Video 2 — Files, Workbooks, and Structure *(~3–4 min)*

Covers: *File Formats & Management*, *File Naming Conventions*, *Workbook Structure*.

**On screen:** Excel's Save-As dialog; a workbook with a couple of tabs.

**Talk & do:**
- **File formats:** `.xlsx` is the default working format; `.csv` is plain text, no formulas/formatting — good for moving data between programs (open `video_barley.csv` to show a CSV *is* just text). Mention `.xlsm` only allows macros.
- **Naming:** show a good filename (`barley_yields_2025_v2.xlsx`) vs a bad one (`final FINAL (3).xlsx`). No spaces-if-you-can-help-it, dates in `YYYY-MM-DD`, version numbers.
- **Workbook structure:** demo the "sheets as rooms" idea — a `raw_data` sheet (untouched), a `clean_data` sheet (a copy you work on), an `analysis` sheet, a `README`. Point out: never work on your raw data directly.

**Do on screen:** import `video_barley.csv` via **Data → Get Data → From Text/CSV** (not double-click), landing it on a sheet you name `raw_data`; copy it to `clean_data`.

---

## Video 3 — Cells, References, and Formulas *(~5–6 min)*

Covers: *The Basics*, *Operators & Order of Operations*, *Relative & Absolute References*, *Named Ranges*. **Dataset: `video_barley.csv`.**

**On screen:** the barley data loaded, columns A (Variety), B (Acres), C (Yield).

**Steps & numbers:**
1. **Basics:** click a cell, type `=C2*B2` → shows ADVANTAGE AB's production (58.4 × 406 = **23,710.4 bu**). "A formula starts with `=` and can reference other cells by their address."
2. **Operators / order of operations:** in a spare cell type `=2+3*4` → **14** (multiplication first); then `=(2+3)*4` → **20**. "Excel follows the same PEMDAS you learned in school — use brackets to be explicit."
3. **Relative references:** put `=C2*B2` in a new column D, then **drag the fill handle down** — show each row auto-adjusts (C3*B3, C4*B4…). "That's a *relative* reference — it shifts as you copy."
4. **Absolute references:** put a price, say `5.50`, in a labelled cell (e.g. `F1`). In column E write `=D2*$F$1` and drag down — show `$F$1` stays fixed. "The dollar signs *lock* the reference. `F4` (⌘T on Mac) cycles the dollar signs."
5. **Named ranges:** select F1, name it `price` in the Name Box; rewrite the formula as `=D2*price`. "Named ranges make formulas read like sentences."

**Say:** the whole section is about *not* hard-coding numbers into formulas — put them in labelled cells and reference them.

---

## Video 4 — Measures of Central Tendency *(~5 min)*

Covers: *Mean*, *Median*, *Skew*, *Mode*. **Dataset: `video_barley.csv` (Yield column).**

**Steps & numbers** (yields in `C2:C10`):
1. **Mean:** `=AVERAGE(C2:C10)` → **48.07**. "The average yield across the nine barley varieties."
2. **Median:** `=MEDIAN(C2:C10)` → **49.0**. "The middle value when sorted — half above, half below."
3. **Compare them:** mean 48.07 vs median 49.0 — very close, so "this data is **roughly symmetric**." Then the rule of thumb: *mean below median → left-skewed; mean above median → right-skewed; mean ≈ median → symmetric.*
4. **Make skew concrete:** point at COWBOY CDC (26.3) — "if a few varieties had catastrophic yields, they'd pull the *mean* down but barely move the *median* — that's when the median is the more honest 'typical' value."
5. **Mode:** `=MODE.SNGL(C2:C10)` → returns `#N/A` (no repeated value). "Mode is for categorical or repeated data — for continuous yields, usually nothing repeats, so mode isn't useful here. It shines for 'most common *crop*' type questions."

**Say:** mean vs median is your first read on the *shape* of the data — you don't even need a chart yet.

---

## Video 5 — Percentiles and Quartiles *(~4 min)*

**Dataset: `video_barley.csv` (Yield column).**

**Steps & numbers:**
1. **Quartiles:** `=QUARTILE.INC(C2:C10,1)` → **Q1 ≈ 35.4**; `=QUARTILE.INC(C2:C10,3)` → **Q3 ≈ 54.6**. "A quarter of varieties are below 35, three-quarters below 55."
2. **A percentile:** `=PERCENTILE.INC(C2:C10,0.9)` → **≈ 62**. "90% of varieties yield about 62 or less; only the top 10% beat it."
3. **IQR:** `=QUARTILE.INC(C2:C10,3)-QUARTILE.INC(C2:C10,1)` → **19.2**. "The middle-50% spread — and it ignores the extremes, unlike the range."
4. Note the course uses **`.INC`** (not `.EXC`).

**Say:** percentiles describe *positions* in the data — crop insurance and 'top-quartile variety' talk are exactly this.

---

## Video 6 — Measures of Spread *(~5 min)*

Covers: *Variance*, *Standard Deviation*, *Coefficient of Variation*, *Range*. **Dataset: `video_barley.csv`.**

**Steps & numbers:**
1. **Range:** `=MAX(C2:C10)-MIN(C2:C10)` → **50.8** (77.1 − 26.3). "Simple, but one weird variety blows it up."
2. **Variance:** `=VAR.S(C2:C10)` → **≈ 238.4**. "Average of squared deviations — note the units are (bu/ac)², which is why we usually take the square root."
3. **Standard deviation:** `=STDEV.S(C2:C10)` → **15.44**. "Back in bu/ac. A typical variety sits about 15 bu/ac away from the mean of 48." Stress **`.S`** for a sample.
4. **Coefficient of variation:** `=STDEV.S(C2:C10)/AVERAGE(C2:C10)` → **≈ 0.32**. "SD as a fraction of the mean — lets you compare variability across crops with very different average yields. A CV of 0.32 means the SD is about a third of the mean — fairly variable."

**Say:** SD tells you the *absolute* spread; CV lets you compare spread *fairly* between, say, barley and canola.

---

## Video 7 — Conditional Functions *(~5–6 min)*

Covers: *IF*, *COUNTIF/SUMIF/AVERAGEIF*. **Dataset: `video_full.csv`** *(expand here — we need the Crop column and more rows).*

**Steps & numbers** (columns: Year, Crop, Variety, Acres, Yield_bu_ac):
1. **IF:** classify each yield: `=IF(E2<40,"Low",IF(E2<=55,"Medium","High"))`, drag down. "Nested IFs — first true condition wins."
2. **COUNTIF:** `=COUNTIF(B:B,"Barley")` → count of barley rows. Then `=COUNTIF(E:E,">50")` → how many variety-years yielded over 50.
3. **AVERAGEIF:** `=AVERAGEIF(B:B,"Canola",E:E)` → average canola yield across all its rows; repeat for Barley, Spring Wheat. "One formula, filtered by category — no manual sorting."
4. **SUMIF:** `=SUMIF(B:B,"Barley",D:D)` → total barley acres. Note the sum-range comes *last* here (and *first* in `SUMIFS`).
5. **Dynamic criteria:** `=COUNTIF(E:E,">"&AVERAGE(E:E))` → count above the overall average. "You can't quote the whole formula as text — you glue `>` to the computed number with `&`."

**Say:** these are the workhorses — "compute something, but only for the rows that match a condition."

---

## Video 8 — Lookup Functions *(~5–6 min)*

Covers: *VLOOKUP*, *XLOOKUP*, *INDEX/MATCH*, *two-key lookups*. **Dataset: `video_full.csv`** + a tiny second table.

**Setup on screen:** on a second sheet, make a little **crop → price** table (Canola 14, Barley 5.50, Spring Wheat 8, etc.).

**Steps:**
1. **XLOOKUP (the modern default):** `=XLOOKUP(B2, prices!A:A, prices!B:B)` → pulls the price for each row's crop. Then Revenue = `=E2*D2*price` (yield × acres × price). Note XLOOKUP defaults to *exact* match.
2. **VLOOKUP (older, still everywhere):** `=VLOOKUP(B2, prices!A:B, 2, FALSE)` — same result. Stress: **always pass `FALSE`** for exact match; the `TRUE` default burns people.
3. **INDEX/MATCH:** `=INDEX(prices!B:B, MATCH(B2, prices!A:A, 0))` — the pre-XLOOKUP way; still in lots of old files.
4. **Two-key lookup:** look a value up by **Crop AND Year** using a joined key: `=XLOOKUP(B2&"|"&A2, Crop&"|"&Year range, value range)`. "When one column doesn't uniquely identify a row, glue two together with a separator."

**Say:** a lookup pulls matching info from another table — the everyday 'join two spreadsheets' task.

---

## Video 9 — Sorting and Filtering *(~4 min)*

Covers: *Sort*, *Filter*, and the **critical filter-vs-formula warning**. **Dataset: `video_full.csv`.**

**Steps:**
1. **Sort:** Data → Sort, by Yield descending. Warn: select *all* columns first, or you'll scramble the correspondence between rows.
2. **Filter:** Data → Filter, filter Crop = Barley and Year = 2025. Show it just hides rows.
3. **⚠️ The big one:** with the filter active, type `=AVERAGE(E:E)` — show it returns the average of **all** rows, not the filtered ones. "Filters hide rows from *you*, not from your formulas." The fix: copy the visible rows to a new sheet, then compute there (or use `AVERAGEIF`/`SUBTOTAL`).

**Say:** this single misunderstanding causes more wrong answers than anything else in the module — internalize it.

---

## Video 10 — Wide vs. Long Data *(~4 min)*

**Dataset: `video_full.csv`** (which is long) + a wide version to contrast.

**Talk & show:**
- **Long** (what we have): one row per Variety-Year, with a `Year` column and a single `Yield` column.
- **Wide:** the same data with a column *per year* (2021, 2022, …). Show a small hand-made example side by side.
- The practical rule: **wide is handy for column-at-a-time math; long is what a PivotTable needs to group by a stacked variable.** A PivotTable can only group by something that lives in its own column.
- Honest note: neither is "wrong"; you reshape depending on the task. (Reshaping is a single function in R — a reason we move there later.)

**Say:** recognizing the shape of your data — and reshaping when needed — is half of real-world data work.

---

## Video 11 — PivotTables *(~6–7 min)*

Covers: *The Concept*, *Building One*, *Common Operations*, *PivotCharts*. **Dataset: `video_full.csv`** *(the star use-case for the full data).*

**Steps & numbers:**
1. **Build one:** click in the data → Insert → PivotTable → new sheet.
2. **Average yield by crop:** drag `Crop` to Rows, `Yield_bu_ac` to Values, switch Sum → **Average**. Read off the ranking (which crop yields most). "One drag-and-drop replaced all those AVERAGEIF formulas."
3. **Add a dimension:** drag `Year` to Columns → a crop × year grid. Point out the **2021 drought** — every crop's column dips that year.
4. **Change aggregation:** switch Values to **Count** (how many varieties per crop) and **Sum of Acres** (total acreage by crop).
5. **PivotChart:** Insert → PivotChart on the crop×year table → a quick visual of the trends.

**Say:** PivotTables are the single most valuable Excel skill for an analyst — summarize-by-category with no formulas.

---

## Video 12 — Charts *(~7 min)*

Covers: *Principles*, *Bar/Line/Pie*, *Histograms*, *Box Plots*. **Dataset: `video_full.csv`** (and the barley slice for the histogram).

**Steps:**
1. **Principles first (30 sec):** every chart needs a **title and labelled axes**; minimize clutter; start bar axes at zero; a chart should answer a question.
2. **Bar chart:** average yield by crop (from the pivot) → Insert → Bar. Title it, label axes.
3. **Line chart:** average yield by year → shows the time trend and the 2021 dip. "Line charts are for ordered things like time."
4. **Pie chart:** show share of acres by crop — then explain why a **bar chart is usually better** (humans read lengths better than angles). Use pie sparingly.
5. **Histogram:** on the **barley slice**, Insert → Statistical Chart → Histogram of the 9 yields → shape of the distribution. Adjust bins.
6. **Box plot:** Insert → Statistical Chart → Box & Whisker comparing yields **across crops** (from the full data) → medians, spread, outliers at a glance. Explain the box (middle 50%), whiskers, and the 1.5×IQR outlier dots.

**Say:** charts are how analysis *persuades* — a good one is worth a page of numbers; the presentation counts (and is graded).

---

## Video 13 — Wrap-Up & The Test Bank *(~2 min)*

**Talk:**
- Recap the arc: get data in cleanly → describe it (centre + spread) → slice it with conditionals and lookups → summarize with PivotTables → communicate with charts.
- Point students to the **test bank** (120 practice questions) and the practice quiz generator.
- Encourage them to *do* the questions in Excel, not just read them — and to write out their interpretation, because that's what the test rewards.

---

## Recording notes

- **Keep each video tight** — one section, one idea per clip. If you flub, re-record just that clip; they knit together.
- **Have the data open before you hit record** — the small barley slice fits on one screen; scroll is fine for the full slice.
- **The numbers above are verified**, so you can state them confidently — but if you refresh the SCIC data later, re-check them.
- **Zoom your Excel** (Ctrl/⌘ + scroll, or View → Zoom) so cells are readable on video.
- Consider a consistent intro/outro card ("AREC 261 · Module 1 · [Section]") so the knitted video flows.
