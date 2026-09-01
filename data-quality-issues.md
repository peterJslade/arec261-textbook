# Common Data-Quality Issues

The following are common data-quality issues. Whenever you open a new dataset, you should check for these problems.

## 1. Awkward column names

In R, you will refer to column names constantly, so consistency matters. If you sometimes use `SpringWheat`, other times `Spring Wheat`, and still other times `spring-wheat`, you will continually have to remember which convention you chose.

A common best practice is **snake case**: use lowercase letters and replace spaces with underscores. For example, use `spring_wheat`.

Column names should be descriptive without becoming unnecessarily long. Whether you choose `yield` or `yield_bu_ac` depends on the dataset. If it contains several yield measures, names such as `yield_bu_ac` and `yield_kg_ha` clearly distinguish their units. If there is only one yield column, the simpler name `yield` may be sufficient.

## 2. Text in a numeric column

Sometimes units or other text are included with numeric values. For example, a weight column might contain `38.2 t`, `42.1 t`, and `37.8 t`.

Excel or R will usually interpret such a column as text, preventing you from performing calculations such as finding the mean or standard deviation. You will need to separate the units from the values and convert the values to numbers. Ideally, the units should be recorded in the column name—for example, `weight_t`.

## 3. Duplicate observations

A dataset may contain duplicate rows. These can arise from data-entry mistakes, combining files more than once, or recording the same observation in multiple systems.

Duplicates are often data-quality problems, but identical rows are not necessarily errors. Two producers, fields, or transactions may legitimately have the same recorded values. Before removing duplicates, determine what uniquely identifies an observation and investigate why the duplication occurred.

## 4. Missing values

Ideally, missing values are stored as blank cells or as `NA`. However, they may instead be represented by codes such as `-99`, `N/A`, `missing`, or `9999`.

You need to identify these codes and convert them to a consistent missing-value representation. Be careful: a code such as `0` may indicate a missing value in one dataset but a genuine observation in another. Consult the dataset's documentation whenever possible.

## 5. Impossible or implausible values

A dataset may contain values that are impossible, such as negative yields, or highly implausible, such as a wheat yield of 1,250 bu/acre.

Examining the minimum and maximum of each numeric variable is a quick way to identify potential problems. Histograms and other graphs can also reveal unusual observations. These values should be investigated before being corrected or removed; an unusual value is not necessarily an error.

## 6. Mixed units

A column may contain values recorded in different units. For example, some weights might be reported in tonnes and others in kilograms.

A histogram can help identify mixed units. Suppose you plot nitrogen application rates and find that 30% of observations fall below 1 while the remaining 70% are above 100. This pattern may indicate that some producers recorded tonnes per hectare while others recorded kilograms per hectare.

Once you identify mixed units, convert all observations to a common unit and record that unit clearly in the column name or dataset documentation.

## 7. Inconsistent categories

Data based on individual reporting often contain categories recorded in inconsistent ways. For example, the same wheat variety might appear as `Brandon`, `AAC Brandon`, `Brandon AAC`, and `Brndon`.

Listing the unique categories and counting the number of observations in each is a useful way to find these inconsistencies. You can then standardize the different versions under a single category, such as `AAC Brandon`.

## 8. Dates

Dates are formatted in many different ways, including `Sep-01-2026`, `09-01-2026`, `2026-09-01`, and `2026/09/01`.

When a dataset is opened in Excel or imported into R, the software will try to determine the date format. If it guesses incorrectly, the dates may be misinterpreted or stored as text, preventing them from being sorted, grouped, or used in calculations.

Numeric dates can be especially ambiguous. For example, `09-01-2026` could mean September 1 or January 9. When possible, use the unambiguous international format `YYYY-MM-DD`, such as `2026-09-01`.
