# ---
# Title: Derived data files for the Module 2 test bank
# Description:
#   Section 2 of the Module 2 bank needs single-crop, NA-free files so
#   summary statistics are meaningful before filter() is taught.
#   Each file is derived from a Module 1 bank dataset. Rerunnable.
# ---

suppressMessages(library(tidyverse))

# RM yields: canola rows only (all bu/ac, no NAs in the long file)
read_csv("data/rm_yields_1990_2025.csv", show_col_types = FALSE) |>
  filter(Crop == "Canola") |>
  write_csv("data/rm_canola_yields_1990_2025.csv")

# Manitoba wheat: reported rows only (suppressed rows carry NAs)
read_csv("data/mb_wheat_varieties.csv", show_col_types = FALSE) |>
  filter(Reported == TRUE) |>
  write_csv("data/mb_wheat_reported_2020_2025.csv")

# StatCan field crops: spring wheat only (the one crop with no NAs)
read_csv("data/statcan_field_crops.csv", show_col_types = FALSE) |>
  filter(Crop == "Spring wheat") |>
  write_csv("data/statcan_spring_wheat_2015_2025.csv")
