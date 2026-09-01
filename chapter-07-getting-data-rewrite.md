# 7 Getting Data

Every dataset used so far has arrived as a tidy table with sensible column names. Real data rarely arrives that way. It may be an Excel workbook sent by a colleague, a CSV behind a government dashboard, a collection of monthly files, or a response from an online service.

Getting the data is part of the analysis. A good acquisition process is repeatable, protects the original data, and records enough information for somebody else to retrieve or interpret the same dataset later.

This chapter follows one workflow:

> **Identify the source → acquire the data → preserve the raw copy → import it → validate it → document it**

The tools differ between Excel and R, but the workflow does not.

## Learning objectives

By the end of this chapter, you should be able to:

1. Identify authoritative sources of agricultural data.
2. Distinguish a manual download, a direct file link, a web API, and a package that wraps an online data service.
3. Explain the basic parts of an API request and response.
4. Use Power Query to import and refresh data from a file, folder, web link, or simple API.
5. Read delimited-text and Excel files into R with appropriate column types.
6. Use R to retrieve a file or make a simple API request.
7. Validate an import and document the source, units, parameters, and retrieval date.

## 7.1 Start with the data you need

Do not begin by downloading the largest file you can find. Begin by describing the table that would answer your question.

Suppose the question is:

> Do Saskatchewan canola yields move with growing-season precipitation?

Before searching for data, specify:

- **Unit of observation:** one rural municipality in one year
- **Measures:** canola yield and May–August precipitation
- **Geographic coverage:** Saskatchewan rural municipalities
- **Time coverage:** perhaps 2015–2025
- **Units:** bushels per acre and millimetres
- **Possible identifiers:** RM number, year, and weather-station identifier

This description tells you what to search for and whether a candidate dataset actually fits the question. It also anticipates the merge: yield and weather data will probably come from different sources and will need common identifiers.

When you find a dataset, inspect its documentation before importing it. Ask:

- What does one row represent?
- Who produced the data, and for what purpose?
- Are the values measured, reported, surveyed, or modelled?
- What are the units, geographic definitions, and reference periods?
- How are missing, suppressed, preliminary, or revised values marked?
- Is the dataset updated? Can historical values be revised?
- Are there licence, privacy, or attribution requirements?

A table can open perfectly and still be the wrong table.

## 7.2 Where agricultural data come from

Some data you create yourself through a field trial, survey, sensor, or business record. Some is supplied by a colleague or organization. Much of the remaining data is publicly available.

Useful starting points include:

- **[Statistics Canada](https://www.statcan.gc.ca/en/subjects-start/agriculture_and_food):** crop area, production and yield; livestock; prices; farm income; trade; and the Census of Agriculture.
- **Saskatchewan agriculture:** the provincial [crop report](https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/agribusiness-farmers-and-ranchers/market-and-trade-statistics/crops-statistics/crop-report), [crop planning guide](https://www.saskatchewan.ca/business/agriculture-natural-resources-and-industry/agribusiness-farmers-and-ranchers/farm-business-management/crop-planning-guide-and-crop-planner), [agriculture dashboard](https://dashboard.saskatchewan.ca/agriculture), and [Saskatchewan Crop Insurance Corporation](https://www.scic.ca/).
- **Weather and climate:** [Environment and Climate Change Canada](https://climate.weather.gc.ca/historical_data/search_historic_data_e.html) for observations from weather stations, and [Open-Meteo](https://open-meteo.com/en/docs/historical-weather-api) for gridded historical weather derived from reanalysis and other models.
- **Soils:** the [Saskatchewan Soil Information System](https://sksis.usask.ca/) and the federal [Canadian Soil Information Service](https://sis.agr.gc.ca/cansis/).
- **Markets and farm finance:** Agriculture and Agri-Food Canada's [market information](https://agriculture.canada.ca/en/market-information-system), [ICE canola futures](https://www.ice.com/products/251/Canola-Futures), and Farm Credit Canada's [farmland values reports](https://www.fcc-fac.ca/en/knowledge/economics/farmland-values-report).
- **Drought:** the [Canadian Drought Monitor](https://agriculture.canada.ca/en/agricultural-production/weather/canadian-drought-monitor).
- **International data:** USDA [Quick Stats](https://quickstats.nass.usda.gov/), [FAOSTAT](https://www.fao.org/faostat/en/), and [World Bank Open Data](https://data.worldbank.org/).

Prefer the organization that creates or officially publishes the data. A chart in a news article may help you discover a dataset, but the government table or agency download should normally be your source.

### Ways to obtain the data

The provider usually exposes either files, an API, or both. Websites, Power Query, and R packages are different ways of using those underlying services.

| Access route | What you do | Typical result | Best use |
|---|---|---|---|
| Manual download | Choose options on a website and click **Download** | CSV or Excel file | Exploration and one-time work |
| Direct file link | Give Excel or R the address of a published file | CSV, JSON, ZIP, or Excel file | Simple repeatable retrieval |
| Web API | Send a structured request to a server | Usually JSON, CSV, or XML | Selected, current, or automated data |
| Client package | Call an R function that builds requests and prepares the response | Data frame or other R object | Services with a well-maintained package |

A package such as `cansim` is not the Statistics Canada API. It is a **client** or **wrapper** that uses Statistics Canada's online data services on your behalf.

## 7.3 What an API does

An **application programming interface**, or **API**, is a documented way for one program to request data or an action from another program.

For a simple data API, your program sends a request and the server sends a response:

```text
client program → request → server
client program ← response ← server
```

The following request asks Open-Meteo for daily precipitation near Saskatoon from May 1 to May 5, 2024:

```text
GET https://archive-api.open-meteo.com/v1/archive
    ?latitude=52.13
    &longitude=-106.67
    &start_date=2024-05-01
    &end_date=2024-05-05
    &daily=precipitation_sum
    &timezone=America/Regina
```

The line breaks make the request easier to read. In a browser it would be one continuous address. You can [open the complete request](https://archive-api.open-meteo.com/v1/archive?latitude=52.13&longitude=-106.67&start_date=2024-05-01&end_date=2024-05-05&daily=precipitation_sum&timezone=America%2FRegina).

### Anatomy of the request

- **Method:** `GET` means retrieve information. Other APIs may use methods such as `POST` to submit information.
- **Endpoint:** `https://archive-api.open-meteo.com/v1/archive` identifies the service and operation.
- **Query parameters:** the names after `?` describe the requested coordinates, dates, variable, and time zone.
- **Headers:** optional information sent with the request, such as the desired response format or an authorization token.
- **Body:** data sent with some requests, especially `POST` requests. This simple `GET` request has no body.

If the request succeeds, the server returns a status code such as `200 OK` and a response body. Data APIs commonly return **JSON**, a structured text format. A shortened response looks like this:

```json
{
  "daily": {
    "time": ["2024-05-01", "2024-05-02"],
    "precipitation_sum": [0.0, 1.7]
  },
  "daily_units": {
    "precipitation_sum": "mm"
  }
}
```

The data is nested rather than arranged as rows and columns. Excel or R must turn the two arrays into a table.

### Authentication and other complications

Some APIs require an **API key** or token. This is a credential that identifies or authorizes the caller and may be tied to a usage quota. Do not paste a secret key into a workbook or script that will be shared. Store it in the credential manager supported by the tool, or in an environment variable or ignored configuration file.

Other complications include:

- **Pagination:** a server may return only the first page of results.
- **Rate limits:** a service may restrict the number of requests in a period.
- **Errors:** `400` usually indicates a bad request, `401` or `403` an authorization problem, `404` a missing resource, and `500` a server problem.
- **Changing schemas:** a provider may rename fields or add new levels.
- **Revisions:** rerunning the same request later may return revised data.

These details are why a package wrapper is useful. For example:

```r
library(cansim)

field_crops <- get_cansim("32-10-0359-01")
```

The `cansim` package constructs requests to Statistics Canada's services, downloads data and metadata, prepares an R object, and can cache the result. It hides much of the HTTP and file-handling work. That makes it excellent for obtaining data, although a raw request is better for learning how web APIs work.

## 7.4 Getting data into Excel

Excel can open files directly, but Power Query is usually the safer and more repeatable way to import external data.

### Excel and text-file formats

An `.xlsx` file can contain multiple worksheets, cell formatting, formulas, charts, and other workbook features. The older `.xls` format has the same general purpose but more limitations.

A **CSV** file is plain text. Each line represents a row, and commas separate the fields. CSV files do not preserve formulas, formatting, data types, or multiple sheets. A **TSV** uses tabs instead of commas. A `.txt` file may use tabs, semicolons, pipes, or another delimiter.

CSV is valuable precisely because it is simple and widely supported. That simplicity also means the importing program must guess how to interpret each field.

### Why double-clicking a CSV can damage data

Download [`elevator_tickets.csv`](https://agdataanalytics.com/practice/data/elevator_tickets.csv) and open one copy in a text editor and another by double-clicking it in Excel. Watch for:

- An identifier such as `00451` becoming `451`
- A long identifier being displayed in scientific notation and possibly losing digits
- A code such as `3-2` being converted to a date
- Dates being interpreted in the wrong day-month order
- Decimal and thousands separators being interpreted according to the computer's locale
- A semicolon-delimited file appearing entirely in column A

An identifier is not a quantity simply because it contains digits. RM numbers, ticket numbers, account numbers, postal codes, and product codes often need the **Text** type.

Keep the original file unchanged. If Excel guesses incorrectly and you save over the CSV, the original text may be lost.

### Use Power Query as the default import workflow

Power Query is Excel's data connection and preparation tool. It can import data, change its structure, record each transformation, and repeat those steps when the source is refreshed.

For a CSV or other delimited file:

1. Choose **Data → Get Data → From Text/CSV**. Menu wording varies slightly by Excel version and operating system.
2. Select the file and inspect the preview. Confirm the delimiter, character encoding, and header row.
3. Choose **Transform Data** rather than immediately loading the file.
4. Inspect the automatically generated steps, especially **Promoted Headers** and **Changed Type**.
5. Set identifiers to **Text**, measurements to an appropriate numeric type, and dates to **Date**.
6. Rename or remove unwanted columns only after confirming what they contain.
7. Choose **Close & Load** and save the workbook as `.xlsx` so the query is preserved.
8. Use **Refresh** when the source changes.

The important idea is not a particular button. It is that the import becomes a recorded recipe rather than a collection of manual fixes.

After loading, verify:

- The expected number of rows and columns arrived.
- Identifiers retained leading zeros and all digits.
- Dates cover the expected period.
- Numeric columns are numeric.
- Missing values were not silently converted to zero.
- Units and category labels match the source documentation.

### Power Query can connect to more than one file

The same workflow applies to several sources:

- **Local file:** use **From Text/CSV**, **From Workbook**, or the appropriate file connector.
- **Folder of repeated files:** use **From Folder** to apply one import recipe to files with the same structure. Keep the source filename as a column so each row remains traceable.
- **File on the web:** use **From Web** with the direct address of a CSV, JSON, or other supported file.
- **Database or organizational service:** choose the relevant connector and authentication method.
- **Simple web API:** use **From Web** with a public `GET` request, then transform the returned JSON.

Combining files or changing a data source can produce plausible but incorrect results. Refresh a query only after checking that the new source has the expected columns, units, and level of detail.

### A simple API in Power Query

For a public API, choose **Data → From Web** and provide the complete Open-Meteo request. The response initially appears as records and lists rather than a finished table. The Power Query interface can drill into the `daily` record and convert its arrays into columns.

The equivalent Power Query M code is shown below. It is not necessary to memorize M, but the code makes the recorded steps visible.

```powerquery
let
    Source = Json.Document(
        Web.Contents(
            "https://archive-api.open-meteo.com",
            [
                RelativePath = "v1/archive",
                Query = [
                    latitude = "52.13",
                    longitude = "-106.67",
                    start_date = "2024-05-01",
                    end_date = "2024-05-05",
                    daily = "precipitation_sum",
                    timezone = "America/Regina"
                ]
            ]
        )
    ),
    Daily = Source[daily],
    AsTable = Table.FromColumns(
        {Daily[time], Daily[precipitation_sum]},
        {"date", "precipitation_mm"}
    ),
    Typed = Table.TransformColumnTypes(
        AsTable,
        {{"date", type date}, {"precipitation_mm", type number}}
    )
in
    Typed
```

Power Query is a good way to demonstrate a simple public API. R or a dedicated connector is usually better when the service requires complex authentication, pagination, repeated requests, or detailed error handling.

### Text to Columns is a repair tool

If a delimited file is already open with all values in one column, **Data → Text to Columns** can split it. Choose the correct delimiter and use **Advanced** to set decimal and thousands separators. Set identifier columns to **Text**.

This fixes the current sheet but does not create a reusable import process. Prefer Power Query when the task will be repeated.

## 7.5 Getting data into R

R separates data acquisition from analysis. A script records the file path, source address, parameters, and import choices, so the process can be rerun.

### CSV, TSV, and other delimited files

The `readr` package supplies the main functions:

```r
library(tidyverse)

deliveries <- read_csv("data/deliveries.csv")
prices_tsv <- read_tsv("data/prices.tsv")
prices_semicolon <- read_delim(
  "data/prices_semicolon.txt",
  delim = ";",
  locale = locale(decimal_mark = ",")
)
```

`read_csv()` guesses a type for each column by inspecting a sample of values. Inspect those choices immediately:

```r
glimpse(deliveries)
spec(deliveries)
problems(deliveries)
```

- `glimpse()` displays the dimensions, column types, and sample values.
- `spec()` displays the parser's column specification.
- `problems()` reports values that could not be parsed as the assigned type.

For a file used repeatedly, specify important types explicitly:

```r
deliveries <- read_csv(
  "data/elevator_tickets.csv",
  col_types = cols(
    ticket_id = col_character(),
    permit_book = col_character(),
    lot_code = col_character(),
    delivery_date = col_date("%Y-%m-%d"),
    .default = col_guess()
  )
)

problems(deliveries)
```

If a value does not match an explicitly assigned type, `readr` normally inserts `NA`, issues a warning, and records a parsing problem. It does not necessarily stop the script. That is why `problems()` matters.

Use the `na` argument when the source has known missing-value codes:

```r
deliveries <- read_csv(
  "data/deliveries.csv",
  na = c("", "NA", "N/A", "..")
)
```

Do this only after confirming what the codes mean in the source documentation. A symbol may indicate suppression or unreliability rather than an ordinary missing value.

### Excel files

The `readxl` package reads `.xls` and `.xlsx` files. It is installed with many tidyverse setups but is not attached by `library(tidyverse)`, so load it separately.

```r
library(readxl)

excel_sheets("data/deliveries.xlsx")
```

Suppose the workbook contains:

```text
[1] "Notes" "2024" "2025" "Summary"
```

Select the data sheet explicitly:

```r
deliveries <- read_excel(
  "data/deliveries.xlsx",
  sheet = "2025"
)
```

If the sheet has a title and notes above the header, skip those rows:

```r
deliveries <- read_excel(
  "data/deliveries.xlsx",
  sheet = "2025",
  skip = 3
)
```

For a stable layout, a cell range is even more explicit:

```r
deliveries <- read_excel(
  "data/deliveries.xlsx",
  range = "2025!A4:F66"
)
```

Print or inspect the result. Column names such as `...2`, several empty columns, or a first row containing labels instead of observations indicate that the wrong sheet, header, or range was selected.

### Reading a file from the web

`read_csv()` can read a direct file URL:

```r
rm_yields_url <-
  "https://dashboard.saskatchewan.ca/export/rm-yields-data/4950.csv"

rm_yields <- read_csv(rm_yields_url)
glimpse(rm_yields)
```

This is convenient for exploration, but the result can change if the provider revises or replaces the file. For a reproducible project, preserve a dated raw copy:

```r
dir.create("data/raw", recursive = TRUE, showWarnings = FALSE)

raw_file <- file.path(
  "data",
  "raw",
  paste0("rm_yields_", Sys.Date(), ".csv")
)

download.file(
  rm_yields_url,
  destfile = raw_file,
  mode = "wb"
)

rm_yields <- read_csv(raw_file)
```

The raw file preserves what was available on that date. The script preserves how it was obtained. You need both.

The file may not contain its units, definitions, or revision notes. Record the page where the link was found, not only the download URL.

### Making an API request in R

The `httr2` package makes the parts of a request explicit. The following code sends the Open-Meteo request used earlier:

```r
library(httr2)
library(tidyverse)

weather_request <- request(
  "https://archive-api.open-meteo.com/v1/archive"
) |>
  req_url_query(
    latitude = 52.13,
    longitude = -106.67,
    start_date = "2024-05-01",
    end_date = "2024-05-05",
    daily = "precipitation_sum",
    timezone = "America/Regina"
  )

weather_response <- weather_request |>
  req_perform()

resp_status(weather_response)
```

A successful response should have status `200`. By default, `req_perform()` reports HTTP error responses such as `404` or `500` as R errors.

Parse the JSON and build a table:

```r
weather_json <- weather_response |>
  resp_body_json(simplifyVector = TRUE)

saskatoon_rain <- tibble(
  date = as.Date(weather_json$daily$time),
  precipitation_mm = weather_json$daily$precipitation_sum
)

glimpse(saskatoon_rain)
```

This example exposes the full sequence:

1. `request()` identifies the endpoint.
2. `req_url_query()` adds and safely encodes parameters.
3. `req_perform()` sends the request and receives a response.
4. `resp_status()` checks the HTTP status.
5. `resp_body_json()` parses the response body.
6. `tibble()` converts the relevant fields into an analysis table.

Every API has a different response structure. Inspect a new response with `str(weather_json)` and read the provider's documentation rather than guessing field names.

### Using a package that wraps a data service

Statistics Canada publishes table `32-10-0359-01`, *Estimated areas, yield, production, average farm price and total farm value of principal field crops, in metric and imperial units*. The `cansim` package can retrieve it by table number:

```r
library(cansim)

get_cansim_table_overview("32-10-0359")

field_crops <- get_cansim("32-10-0359-01")
glimpse(field_crops)
```

If you do not know the table number, search the catalogue:

```r
search_cansim_cubes("field crop yield")
```

`cansim` is a client package. Its functions form an easy R interface, while the package communicates with Statistics Canada's Web Data Service and bulk-download endpoints underneath.

The package improves repeatability because the table identifier appears in the script. It does **not** freeze the data permanently: Statistics Canada revises historical values, and rerunning the script later can retrieve a newer release. Save a dated raw extract when the exact version matters.

For large tables, avoid downloading more data than the computer can handle. Use table metadata, vectors, partial retrieval, or a local database connection where the package supports them.

The USDA's `rnassqs` package plays a similar role for the Quick Stats API. Quick Stats requires an API key. Store it in the `NASSQS_TOKEN` environment variable rather than writing the key into a script.

### Choosing Excel or R

| Situation | Recommended starting point |
|---|---|
| One-time inspection of a small file | Excel or R |
| Repeated Excel report or monthly folder import | Power Query |
| Simple public `GET` API used to teach the idea | Power Query or R |
| Authentication, pagination, retries, or many requests | R or a dedicated connector/package |
| Analysis already being conducted in R | Retrieve and import in R |
| Results must be refreshed by an Excel user | Power Query |

The goal is not to prove that one tool can do everything. Choose the tool that makes the complete workflow easiest to inspect, rerun, and maintain.

## 7.6 Validate every import

A successful import means the software read something. It does not mean the result is correct.

Use the following checklist after every import:

1. **Dimensions:** Are the numbers of rows and columns plausible?
2. **Unit of observation:** Does one row represent what you expected?
3. **Identifiers:** Are IDs complete, unique where expected, and stored as text when necessary?
4. **Types:** Are measures numeric and dates actually dates?
5. **Coverage:** Do dates, locations, crops, and categories cover the expected range?
6. **Missing values:** Were blanks, suppression codes, or footnotes handled correctly?
7. **Units:** Are yield, area, price, and weather units explicit?
8. **Duplicates:** Are repeated keys legitimate or accidental?
9. **Extreme values:** Do a few minimum and maximum values make sense?
10. **Source comparison:** Do several rows agree with the provider's displayed table or documentation?

In R, begin with:

```r
glimpse(deliveries)
problems(deliveries)
nrow(deliveries)
summary(deliveries)
```

Then inspect the variables that define the unit of observation. For example, if there should be one delivery per ticket:

```r
deliveries |>
  count(ticket_id) |>
  filter(n > 1)
```

In Excel, make the same checks using the table row count, filters, `COUNTBLANK`, duplicate highlighting, and a few comparisons against the source.

## 7.7 Preserve and document the source

Keep raw data separate from processed data:

```text
project/
├── data/
│   ├── raw/
│   └── processed/
├── R/
└── README.md
```

- **Raw data** is the unchanged file or API response as retrieved.
- **Processed data** is created by a script or recorded Power Query process.
- **Scripts or queries** explain how raw data became processed data.

Do not manually edit the only copy of a raw file. If a value must be corrected, make the correction in code or in a recorded query so that it is visible and repeatable.

Every project should have a short `README.md`. Record at least:

- Provider and dataset title
- Source page and direct download or API endpoint
- Table, vector, station, or product identifier
- Parameters or website selections
- Geographic and time coverage
- Units and important definitions
- Retrieval date
- File name of the preserved raw copy
- Any transformations already applied
- Known revision, suppression, licence, or quality notes

For example:

```markdown
# Canola yields and growing-season precipitation

Question: Do Saskatchewan canola yields move with May–August precipitation?

## Data

### data/raw/rm_yields_2026-08-21.csv

- Provider: Government of Saskatchewan agriculture dashboard
- Source page: https://dashboard.saskatchewan.ca/agriculture
- Direct file: https://dashboard.saskatchewan.ca/export/rm-yields-data/4950.csv
- Retrieved: 2026-08-21
- Unit of observation: rural municipality-year
- Yield units: bushels per acre; confirmed on source page
- Note: raw copy preserved without manual edits

### data/raw/saskatoon_weather_2026-08-21.json

- Provider: Open-Meteo Historical Weather API
- Endpoint: https://archive-api.open-meteo.com/v1/archive
- Parameters: latitude 52.13, longitude -106.67, daily precipitation,
  2024-05-01 to 2024-08-31, timezone America/Regina
- Retrieved: 2026-08-21
- Precipitation unit: millimetres
- Note: gridded reanalysis/model data, not a station observation

## Scripts

- R/01_get_data.R retrieves and preserves the source data
- R/02_prepare_data.R validates, reshapes, and combines the tables
```

The retrieval date is not clerical detail. Government agencies revise estimates, dashboards replace files, and APIs change. A script tells you how to retrieve data; a dated raw copy tells you exactly which data the analysis used.

## 7.8 Summary

- Begin with the desired unit of observation, measures, coverage, and units.
- Prefer authoritative providers and read their metadata.
- A direct download returns a file; an API returns a response to a structured request; a package wrapper makes those services easier to use.
- Use Power Query for repeatable Excel imports, especially files, folders, web files, and simple APIs.
- In R, make important column types explicit and inspect parsing problems.
- Use an HTTP package such as `httr2` when the goal is to understand or control an API request.
- Preserve raw data, validate every import, and record provenance.

## 7.9 Practice

### Exercise 1: Import a risky CSV

Import [`elevator_tickets.csv`](https://agdataanalytics.com/practice/data/elevator_tickets.csv) twice:

1. Open one copy directly in Excel.
2. Import another copy through Power Query.

Compare `ticket_id`, `permit_book`, `lot_code`, and any date columns. Explain which Power Query types protect the original values.

### Exercise 2: Import a locale-dependent file

Download [`elevator_tickets_semicolon.csv`](https://agdataanalytics.com/practice/data/elevator_tickets_semicolon.csv). Import it with the correct semicolon delimiter and decimal mark, first in Power Query and then with `read_delim()` in R.

### Exercise 3: Compare API tools

Retrieve five days of Open-Meteo precipitation for Saskatoon:

1. Use Power Query in Excel.
2. Use `httr2` in R.
3. Identify the endpoint, parameters, status code, JSON fields, and units.

Which tool makes the API mechanics easier to see? Which would be easier for an Excel user to refresh?

### Exercise 4: Use a package wrapper

Use `cansim` to find and retrieve a Statistics Canada crop table. Record:

- Search terms
- Table number and title
- Unit of observation
- Geography and period
- Units
- Retrieval date

Explain why `cansim` is an API client rather than the Statistics Canada API itself.

### Exercise 5: Create a data inventory

Create a `README.md` for a small project containing at least two data sources. Another student should be able to locate the sources, understand the units, and reproduce the acquisition without asking you what you clicked.

## Further reading

- [What is Power Query?](https://learn.microsoft.com/en-us/power-query/power-query-what-is-power-query)
- [Power Query Web connector](https://learn.microsoft.com/en-us/power-query/connectors/web/web)
- [`readr` column types](https://readr.tidyverse.org/articles/column-types.html)
- [`readxl::read_excel()`](https://readxl.tidyverse.org/reference/read_excel.html)
- [`httr2` documentation](https://httr2.r-lib.org/)
- [Statistics Canada Web Data Service](https://www.statcan.gc.ca/en/microdata/api)
- [`cansim` package documentation](https://mountainmath.github.io/cansim/)
- [`rnassqs` package documentation](https://docs.ropensci.org/rnassqs/)
