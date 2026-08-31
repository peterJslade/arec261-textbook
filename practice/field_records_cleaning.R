# ---
# Title: Checking and cleaning the field records
# Author: Your Name
# Date: 2026-08-31
# Description:
#   Checks data/field_records_messy.csv for the eight data-quality issues
#   from Module 3, fixes each one, and writes the cleaned file to
#   output/field_records_clean.csv.
# ---

# Load packages
library(tidyverse)
library(janitor)

# ============================================================
# Read
# ============================================================

# Read the file, declaring the missing-value codes up front
records <- read_csv(
  "data/field_records_messy.csv",
  na = c("", "N/A", "missing")
)

# ============================================================
# Check
# ============================================================

# Column names and types as they arrived
glimpse(records)

# Summary of every column: the min and max expose the planted problems
summary(records)

# Count the categories: the same variety appears under four spellings
records |>
  count(VARIETY_NAME, sort = TRUE)

# Count exact duplicate rows: 38 rows but only 36 distinct
nrow(records)
nrow(distinct(records))

# ============================================================
# Clean
# ============================================================

records_clean <- records |>
  # Issue 3: drop the exact duplicate rows
  distinct() |>
  # Issue 1: every column name to snake case
  clean_names() |>
  # Clearer names, with units where they matter
  rename(
    variety = variety_name,
    weight_t = harvest_weight,
    n_rate_kg_ha = n_rate,
    moisture_pct = moisture_percent
  ) |>
  mutate(
    # Issue 7: one spelling for the Brandon variety
    variety = if_else(variety %in% c("Brandon", "Brandon AAC", "Brndon"),
                      "AAC Brandon", variety),
    # Issue 8: parse the mixed date formats (year-first, then month-first)
    seeded_date = coalesce(ymd(seeded_date, quiet = TRUE),
                           mdy(seeded_date, quiet = TRUE)),
    # Issues 4 and 5: the -99 code, the negative and the 20x yield to NA
    yield_bu_ac = if_else(yield_bu_ac <= 0 | yield_bu_ac > 200,
                          NA, yield_bu_ac),
    # Issue 2: strip the unit from the weights and make them numeric
    weight_t = parse_number(weight_t),
    # Issue 6: rates below 1 are t/ha; convert them to kg/ha
    n_rate_kg_ha = if_else(n_rate_kg_ha < 1,
                           n_rate_kg_ha * 1000, n_rate_kg_ha),
    # Issue 4: the 9999 moisture code to NA
    moisture_pct = if_else(moisture_pct > 100, NA, moisture_pct)
  )

# ============================================================
# Check again
# ============================================================

# The same checks on the cleaned data: sane ranges, one variety spelling
summary(records_clean)
records_clean |>
  count(variety, sort = TRUE)

# ============================================================
# Write
# ============================================================

# Save the cleaned file; the raw file is never edited
write_csv(records_clean, "output/field_records_clean.csv")
