### Question 71

*Using the Manitoba Wheat Variety dataset.*

**(a)** Build a histogram of all reported wheat yields, titled with labelled axes.

**(b)** Describe the shape in Module-1 terms.

**(c)** The Saskatchewan RM canola yields for a single year are noticeably left-skewed (a long tail of low-yielding RMs). Contrast the shape of this Manitoba wheat histogram with that.

**(d)** This data has genuine low-end outliers by the 1.5×IQR rule (about 35 of them across all years). Explain how a *box plot* of the same data would display them.

**(e)** Explain why a histogram alone might not lead you to call those low values "outliers," whereas a box plot would flag them explicitly.

<details><summary>Answer</summary>

- (a) Histogram, titled/labelled.
- (b) **Roughly symmetric and fairly tight** (bulk ~54–70; mean 61.2 ≈ median 62.2).
- (c) The SK canola histogram was left-skewed and wider; this one is more symmetric and concentrated.
- (d) A box plot marks values below Q1 − 1.5×IQR (below ≈ 30.4) as individual dots beyond the lower whisker.
- (e) A histogram shows only a thin low tail, leaving "outlier" a judgment call; the box plot applies the 1.5×IQR rule and flags them as points.
</details>

### Question 72

*Using the Manitoba Wheat Variety dataset.*

**(a)** Build a box plot comparing the yield distributions of three widely-grown varieties — `AAC BRANDON (BW 932)`, `AAC STARBUCK <SECAN>`, and `AAC REDBERRY` (one box each) — titled with labelled axes.

**(b)** Explain what a reader learns from this box plot that a simple bar chart of *average* yield per variety would hide.

**(c)** Identify, from your chart, which of the three varieties looks the most consistent (least spread), and say how you can tell.

**(d)** You want to show a general audience that "these varieties yield similarly." Would you choose the box plot or a bar chart of means? Justify it in terms of audience and message.

**(e)** Explain one way an unlabelled or poorly titled version of your chart could mislead a reader.

<details><summary>Answer</summary>

- (a) Box plot, three named varieties, titled/labelled.
- (b) Spread and consistency (some varieties more variable) plus outliers — a bar of means hides all of that.
- (c) The variety with the narrowest box/shortest whiskers is most consistent (AAC Brandon and AAC Redberry both have IQR ≈ 13, tighter than AAC Starbuck's ≈ 14). Credit any answer that reads the box widths correctly.
- (d) Defensible either way if justified: a bar-of-means is cleaner for a lay audience whose takeaway is "similar averages"; the box plot is right if the message is consistency.
- (e) A missing y-axis label or a truncated axis could exaggerate small differences between varieties.
</details>

### Question 73

*Using the Manitoba Wheat Variety dataset.*

**(a)** Build a line chart of `AAC BRANDON (BW 932)`'s average yield by year, 2020–2025, titled with labelled axes.

**(b)** Identify the year with the lowest average and describe the size of the dip.

**(c)** Saskatchewan RM canola's sharpest single-year drop is into 2021. Does this Manitoba variety show its lowest year in the same year? What would that suggest about the cause?

**(d)** Explain what it means that a single variety, tracked across years, shows the same low year as an entirely different dataset.

**(e)** Explain why holding the variety fixed and reading across years lets the chart show *year* effects clearly.

<details><summary>Answer</summary>

- (a) Line chart, six points (2020–2025), titled/labelled.
- (b) **2021** is lowest (~49 bu/ac, down from ~62 in 2020).
- (c) Yes — both bottom out in 2021.
- (d) The same low year in two independent datasets points to a shared, region-wide cause that year.
- (e) With the variety fixed, differences between years cannot be due to variety, so the chart isolates the year-to-year effect.
</details>

### Question 74

*Using the Manitoba Wheat Variety dataset.*

**(a)** Filter reported yields to `Year = 2023` and build a histogram, titled with labelled axes.

**(b)** Describe the shape in Module-1 terms.

**(c)** By the 1.5×IQR rule, 2023 has about 7 low-end outliers. Describe where they would appear on a box plot of this year.

**(d)** Explain why the count of flagged outliers is smaller for a single year (2023) than it is when all years are pooled together into one dataset.

**(e)** Explain, in one sentence, how pooling more years can change how many points get flagged as outliers.

<details><summary>Answer</summary>

- (a) Histogram, titled/labelled.
- (b) Roughly symmetric, tight (mean 61.4 ≈ median 61.9).
- (c) As individual dots below the lower whisker (below ≈ 33.9 for 2023).
- (d) 2023 alone has fewer rows and a slightly tighter spread than the pooled data, so fewer points fall beyond its fences.
- (e) Pooling years changes the quartiles and IQR, moving the fences and therefore the number of flagged outliers.
</details>

### Question 75

*Using the Manitoba Wheat Variety dataset.*

**(a)** Build a bar chart of the average reported yield for the six most-reported varieties (one bar each), titled with labelled axes.

**(b)** Identify the tallest and shortest bars.

**(c)** Explain what this bar chart of average yields shows well, and what it hides compared with a box plot of the same varieties (which would show each variety's spread and outliers).

**(d)** Explain why the bars should start at zero, and how a non-zero baseline could mislead a reader about the differences between varieties.

**(e)** State, in one sentence, when a bar chart of means is the right choice and when a box plot is better.

<details><summary>Answer</summary>

- (a) Bar chart, six varieties, titled/labelled.
- (b) Tallest ≈ AAC Wheatland/Hockley (~66–67 median area); shortest ≈ AAC Redberry (~54).
- (c) It shows the averages clearly but hides spread, consistency, and outliers.
- (d) A zero baseline keeps bar heights proportional to the values; a truncated baseline exaggerates small gaps between varieties.
- (e) A bar-of-means suits a simple "compare averages" message; a box plot is better when spread or consistency matters.
</details>

### Question 76

*Using the Manitoba Wheat Variety dataset.*

**(a)** Build a box plot of all reported yields for a single year of your choice with many reports (e.g. 2025), titled with labelled axes.

**(b)** Read the median, Q1, and Q3 directly off the box.

**(c)** Compute the same three numbers in Excel and compare them to what you read off the chart.

**(d)** Explain why reading quartiles off a box plot is quick but approximate, and when you would want the exact numbers instead.

**(e)** State, in one sentence, what the box (not the whiskers) of a box plot represents.

<details><summary>Answer</summary>

- (a) Box plot for 2025, titled/labelled.
- (b) Read median, Q1, Q3 off the box edges and centre line.
- (c) Compute with `MEDIAN`, `QUARTILE.INC(...,1)`, `QUARTILE.INC(...,3)` and compare.
- (d) The chart is a visual estimate; use the exact functions when you need precise values (e.g. to report or compute IQR).
- (e) The box spans Q1 to Q3 — the middle 50% of the data, with the median marked inside.
</details>

### Question 77

*Using the Manitoba Wheat Variety dataset.*

**(a)** Build a line chart comparing two varieties' average yields by year (e.g. `AAC BRANDON (BW 932)` and `AAC STARBUCK <SECAN>`), 2020–2025, with a legend, titled with labelled axes.

**(b)** Describe whether the two varieties track each other across years.

**(c)** Identify any year where the two lines are closest and any where they are farthest apart.

**(d)** Explain what it means when two varieties rise and fall together across years (think about what they share: the same years/conditions).

**(e)** Explain why a legend is essential on a two-line chart.

<details><summary>Answer</summary>

- (a) Two-line chart with legend, titled/labelled.
- (b) They largely track each other — both dip in 2021, both recover after.
- (c) Report the closest and farthest years from your chart.
- (d) Sharing the same years means both face the same growing conditions, so common year effects move them together; gaps between them reflect variety differences.
- (e) Without a legend the reader cannot tell which line is which variety.
</details>

### Question 78

*Using the Manitoba Wheat Variety dataset.*

**(a)** Build a histogram of reported yields for the single variety `AAC BRANDON (BW 932)` (all years), titled with labelled axes.

**(b)** Describe the shape and estimate the centre by eye.

**(c)** The histogram of *all* reported wheat yields (every variety pooled) has an IQR of about 16 bu/ac. Compare this single variety's spread to that. Which is tighter, and why might that be?

**(d)** Explain why one variety's yields might spread less than the pooled mix of all varieties.

**(e)** State, in one sentence, why comparing a part (one variety) to the whole (all varieties) can reveal how much of the spread comes from mixing varieties.

<details><summary>Answer</summary>

- (a) Histogram, titled/labelled.
- (b) Roughly symmetric, centred ~60 bu/ac.
- (c) The single-variety histogram is slightly tighter (IQR ≈ 13 vs the pooled ≈ 15.7).
- (d) One variety removes between-variety differences, leaving mostly site and year variation, so it can spread a little less.
- (e) If the pooled data is much wider than one variety, variety differences add to the spread; if similar, most spread is site/year, not variety.
</details>

### Question 79

*Using the Manitoba Wheat Variety dataset.*

**(a)** Build a box plot comparing reported yields across the years 2020–2025 (one box per year), titled with labelled axes.

**(b)** Identify the year with the lowest median box.

**(c)** Describe how the 2021 box compares to the others in position.

**(d)** Explain what this by-year box plot shows about the drought year that a single line of yearly averages would not.

**(e)** State, in one sentence, why a box plot per year is a good way to show both the level and the spread changing over time.

<details><summary>Answer</summary>

- (a) Box plot, six years, titled/labelled.
- (b) **2021** has the lowest median box.
- (c) The 2021 box sits clearly below the others.
- (d) It shows how the *whole distribution* dropped in 2021 (lower quartiles, more low outliers), not just the average.
- (e) Each year's box shows its centre and spread together, so the chart tracks both across time.
</details>

### Question 80

*Using the Manitoba Wheat Variety dataset.*

**(a)** Suppose someone hands you a pie chart showing the "share of reported rows" for the top varieties. Explain why a pie chart is a poor choice for comparing these varieties' *yields*.

**(b)** State what a pie chart *can* legitimately show for this dataset (think counts/shares, not yields).

**(c)** Build the more appropriate chart — a bar chart of counts of reported rows for the top six varieties — titled with labelled axes.

**(d)** Explain why a bar chart lets a reader compare the categories more accurately than a pie chart.

**(e)** State, in one sentence, the module's guidance on when a pie chart is acceptable.

<details><summary>Answer</summary>

- (a) A pie shows parts of a whole (shares), not a numeric variable like yield; it cannot display yields at all.
- (b) It can show each variety's *share of reported rows* (a count-based part-of-whole), though a bar chart does that better.
- (c) Bar chart of reported-row counts for the six varieties, titled/labelled.
- (d) Readers compare bar lengths accurately, but judge pie angles/areas poorly.
- (e) A pie chart is acceptable only to emphasise that one slice is roughly a simple fraction (e.g. about half) of the whole.
</details>

## Questions 81–90 · Canada Field Crops

### Question 81

*Using the Canada Field Crops dataset.*

**(a)** Build a box plot comparing canola yield across provinces (one box per province), using all years 2015–2025, titled with labelled axes.

**(b)** Identify which province sits highest and which shows the widest box.

**(c)** Explain what "spread" (box width) means for a single province's box here.

**(d)** A headline claims "Ontario grows the best canola." Explain what your box plot supports about that claim.

**(e)** Explain what the box plot does *not* show that you would need before agreeing Ontario is the most important canola province (think scale of production, not yield).

<details><summary>Answer</summary>

- (a) Box plot, province on the category axis.
- (b) **Ontario** highest median (~46.5); **British Columbia** widest box (IQR ≈ 11.0).
- (c) The box width is the range/IQR of that province's year-to-year yields; wider = more variable across years.
- (d) It supports "higher **yield per acre** in Ontario."
- (e) It says nothing about **how many** acres each province grows; Saskatchewan produces far more overall despite lower per-acre yield.
</details>

### Question 82

*Using the Canada Field Crops dataset.*

**(a)** Build a line chart of national average canola yield by year, 2015–2025, titled with labelled axes.

**(b)** Identify the lowest year on the chart.

**(c)** Connect that low year to what you have seen in the Saskatchewan and Manitoba datasets.

**(d)** Explain why a line chart is the right tool for a "yield over time" story.

**(e)** Explain why a pie chart would be the wrong tool here.

<details><summary>Answer</summary>

- (a) Line chart, year on x, average yield on y, titled/labelled.
- (b) **2021** is the low point (~34 bu/ac, down from ~41 around it).
- (c) The same 2021 drought appears in the SK RM data and the Manitoba varieties — cross-dataset consistency.
- (d) A line chart shows change over an ordered variable (time), making the trend and dip visible.
- (e) A pie chart shows parts of a whole at one moment and cannot show a trend.
</details>

### Question 83

*Using the Canada Field Crops dataset.*

**(a)** Build a bar chart of average canola yield by province for a single year (e.g. 2023), one bar per province, titled with labelled axes.

**(b)** Identify the tallest and shortest bars.

**(c)** Explain why the bars should start at zero.

**(d)** Explain what this single-year bar chart shows well, and what a box plot of the same crop's yields across many years would add that the bar chart cannot.

**(e)** State, in one sentence, the difference between what a single-year bar chart and a multi-year box plot tell you about a province.

<details><summary>Answer</summary>

- (a) Bar chart, provinces, titled/labelled.
- (b) Report tallest/shortest from the 2023 rows (e.g. Ontario high, BC/SK lower).
- (c) A zero baseline keeps bar heights proportional; a truncated baseline exaggerates province gaps.
- (d) The bar chart shows one year's averages; the box plot shows each province's spread across many years.
- (e) The bar chart is a snapshot of one year; the box plot shows the range and consistency over time.
</details>

### Question 84

*Using the Canada Field Crops dataset.*

**(a)** Build a box plot comparing **Barley** yields across provinces (all years), titled with labelled axes.

**(b)** Identify the province with the highest median and the one with the widest spread.

**(c)** Explain how you read a province's median and IQR off its box.

**(d)** Explain why comparing provinces with a box plot is fairer than comparing single years, when provinces report different numbers of years.

**(e)** State, in one sentence, why the box plot's whiskers and outlier dots matter when comparing provinces.

<details><summary>Answer</summary>

- (a) Box plot, provinces, titled/labelled.
- (b) Report the highest-median and widest-box provinces from your chart.
- (c) The median is the line in the box; the IQR is the box height (Q3 − Q1).
- (d) A box plot summarises each province's whole distribution, so uneven year counts still yield comparable centre/spread pictures.
- (e) Whiskers and outlier dots show each province's extremes, revealing unusually good or bad years the box alone hides.
</details>

### Question 85

*Using the Canada Field Crops dataset.*

**(a)** Build a line chart with two lines — national average canola yield and national average spring wheat yield by year, 2015–2025 — with a legend, titled with labelled axes.

**(b)** Describe whether the two crops' national averages move together across years.

**(c)** Identify a year where both dip.

**(d)** Explain why plotting both on the same bu/ac axis is a fair comparison here.

**(e)** Explain why a legend is required and what would happen to interpretation without it.

<details><summary>Answer</summary>

- (a) Two-line chart with legend, titled/labelled.
- (b) They broadly move together across years.
- (c) **2021** — both national averages dip.
- (d) Both are measured in bu/ac, so a shared axis compares like with like.
- (e) The legend maps each line to its crop; without it the two series cannot be told apart.
</details>

### Question 86

*Using the Canada Field Crops dataset.*

**(a)** Build a histogram of all canola yields (all provinces, all years) pooled, titled with labelled axes.

**(b)** Describe the shape in Module-1 terms.

**(c)** Explain why pooling provinces and years into one histogram can blur the picture, using the idea that different provinces have different typical yields.

**(d)** Suggest a better chart than one pooled histogram for showing how canola yield differs *by province*.

**(e)** State, in one sentence, when a single pooled histogram is useful and when it hides structure.

<details><summary>Answer</summary>

- (a) Histogram, titled/labelled.
- (b) Describe the shape you observe (roughly centred near the low 40s, fairly symmetric).
- (c) Mixing high- and low-yielding provinces stacks several different centres into one histogram, blurring where any single province sits.
- (d) A box plot with one box per province, which separates the provinces instead of pooling them.
- (e) A pooled histogram is useful for the overall spread of all values, but hides differences between the groups it pools.
</details>

### Question 87

*Using the Canada Field Crops dataset.*

**(a)** Build a bar chart of total canola **seeded acres** by province for 2023 (one bar per province), titled with labelled axes.

**(b)** Identify the province with the tallest bar.

**(c)** On a *yield-per-acre* bar chart, Ontario leads canola. Does the same province lead this *seeded-acres* chart? Explain what the difference reveals about yield versus total production.

**(d)** Explain how a province can lead in seeded acres but not in yield per acre, using rate vs. total.

**(e)** State, in one sentence, why you might show both an acres chart and a yield chart to describe a crop's provincial picture.

<details><summary>Answer</summary>

- (a) Bar chart of seeded acres, provinces, titled/labelled.
- (b) **Saskatchewan** has by far the tallest bar (~12.4M acres).
- (c) No — Saskatchewan leads seeded acres, but Ontario leads yield per acre.
- (d) Seeded acres is a total (land planted); yield is a rate (per acre) — a province can plant the most land yet not have the highest per-acre yield.
- (e) Acres show scale and yield shows productivity; together they give a complete picture that either alone would distort.
</details>

### Question 88

*Using the Canada Field Crops dataset.*

**(a)** Build a box plot comparing spring wheat yields across provinces (all years), titled with labelled axes.

**(b)** Identify any province whose box is noticeably higher or lower than the rest.

**(c)** Explain why a province with only a few reported years will have a box built from few points, and why that box is less reliable.

**(d)** Explain how you could tell, from the dataset, that a province's box rests on few observations.

**(e)** State, in one sentence, why the number of observations behind a box matters when comparing provinces.

<details><summary>Answer</summary>

- (a) Box plot, provinces, titled/labelled.
- (b) Report the standout province(s) from your chart.
- (c) Few years means few data points, so its quartiles and whiskers are estimated from little data and can shift with one value.
- (d) Count the non-blank spring wheat rows for that province (e.g. with `COUNTIFS`).
- (e) A box from many years is more trustworthy than one from a handful; the observation count sets how much to trust the box.
</details>

### Question 89

*Using the Canada Field Crops dataset.*

**(a)** Build a line chart of national average **barley** yield by year, 2015–2025, titled with labelled axes.

**(b)** Identify the lowest year.

**(c)** National average canola yield bottoms out in 2021. Is barley's lowest year the same? What does two crops sharing their worst national year suggest about the cause?

**(d)** Explain what it means when two crops share their worst national year.

**(e)** Explain why viewing several crops' line charts together is stronger evidence of a broad event than any one chart.

<details><summary>Answer</summary>

- (a) Line chart, titled/labelled.
- (b) Report the lowest year (2021 is expected).
- (c) Same year (2021) as canola's low.
- (d) Both crops falling in the same year points to a shared, broad cause rather than a crop-specific one.
- (e) A single crop's dip could be crop-specific; several crops dipping together in one year indicates a wide-reaching event.
</details>

### Question 90

*Using the Canada Field Crops dataset.*

**(a)** Choose one province with many reported years (e.g. Saskatchewan) and build a line chart of its canola yield by year, 2015–2025, titled with labelled axes.

**(b)** Identify the lowest year for that province.

**(c)** The *national* average canola yield has its low point in 2021. Compare this province's low year to that national low year — do they coincide, and what would it mean if a province's dip were deeper or shallower than the national one?

**(d)** Explain how a single province's line can differ from the national line, even though both cover the same years.

**(e)** State, in one sentence, why showing one province's line alongside the national line helps a reader see whether that province followed or bucked the national pattern.

<details><summary>Answer</summary>

- (a) Line chart for one province, titled/labelled.
- (b) Report that province's lowest year (2021 expected for SK).
- (c) Compare to the national low (2021); they typically coincide but the province's dip may be deeper or shallower.
- (d) The national line averages all provinces, so one province can dip more or less than the national average in a given year.
- (e) Overlaying the two lines shows at a glance whether the province tracked the national trend or diverged from it.
</details>

---
