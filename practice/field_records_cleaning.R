# ---
# Title: Checking and cleaning the field records
# Author: Your Name
# Date: 2026-09-04
# Description:
#   Checks data/field_records_messy.csv for the data-quality issues
#   from Module 3, fixes each one, and writes the cleaned file to
#   output/field_records_clean.csv.
# ---

# Load packages
library(tidyverse)
library(janitor)

# ============================================================
# Read
# ============================================================

# Read the file
records <- read_csv("data/field_records_messy.csv")

# ============================================================
# Check
# ============================================================

# Column names and types as they arrived: harvest weight and moisture
# are text when they should be numeric, and the names are a mess
glimpse(records)

# Summary of every column: yield and N rate have suspicious extremes
summary(records)

# Histogram of the nitrogen rate: two clusters, two units
hist(records$`N rate`, breaks = 20)

# Count the categories: the same variety appears under four spellings
records |>
  count(VARIETY_NAME, sort = TRUE)

# Count the rows, then the distinct rows: the difference is the duplicates
nrow(records)
nrow(distinct(records))

# ============================================================
# Clean
# ============================================================

records_clean <- records |>
  clean_names() |>   # issue 1: every column name to snake case
  rename(variety = variety_name) |>
  distinct() |>      # issue 3: drop the exact duplicate rows

  mutate(
    # Issue 2: strip the unit text from the weights and make them numeric
    harvest_weight = parse_number(harvest_weight),
    # Issues 4, 5 and 8: the -99 code, the negative and the 1250 all become NA
    yield_bu_ac = if_else(yield_bu_ac <= 0 | yield_bu_ac > 200,
                          NA,
                          yield_bu_ac),
    # Issue 6: rates below 1 are t/ha, so convert them to kg/ha
    n_rate = if_else(n_rate < 1,
                     n_rate * 1000,
                     n_rate),
    # Issue 7: one spelling for the Brandon variety
    variety = if_else(variety %in% c("Brandon", "Brandon AAC", "Brndon"),
                      "AAC Brandon",
                      variety),
    # Issue 9: moisture has text values
    moisture_percent = parse_number(moisture_percent),
    # Issue 10: change moisture values above 100 to NA
    moisture_percent = if_else(moisture_percent > 100,
                               NA,
                               moisture_percent)
  )

# ============================================================
# Check again, then save
# ============================================================

# The same checks on the cleaned data
summary(records_clean)

records_clean |>
  count(variety, sort = TRUE)

# Save the cleaned file to output; the raw file is never edited
write_csv(records_clean, "output/field_records_clean.csv")
