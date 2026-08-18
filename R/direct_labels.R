# =============================================================================
# Script: R/direct_labels.R
# Purpose: Matched pair illustrating direct labelling vs. a legend. Both panels
#          plot the identical data -- western Canadian barley variety acreage
#          shares, 2008-2025 -- so the only thing that changes is how the
#          reader gets from a band of colour to a variety name.
#
# Inputs:
#   - Barley_project/output/provincial_barley_acreage.csv
#   - Barley_project/output/cgc_variety_info.csv
#
# Outputs:
#   - images/variety_shares_direct_labels.png
#   - images/variety_shares_legend.png
#
# Notes:
#   - Varieties below 2% share in BOTH 2008 and 2024 are collapsed into
#     "Other varieties". This keeps the named set small enough that the legend
#     version is a fair comparison rather than a strawman.
#   - Palette is the module 3 palette from R/chart_types.R.
# =============================================================================

library(data.table)
library(ggplot2)
library(ggrepel)

BARLEY_DIR <- file.path(
  "/Users/pjs998/Library/CloudStorage/OneDrive-UniversityofSaskatchewan",
  "Advising/Dallas/Barley_project"
)
OUT_DIR <- file.path(
  "/Users/pjs998/Library/CloudStorage/OneDrive-UniversityofSaskatchewan",
  "Teaching/261/2026/textbook_261/images"
)

## Threshold for keeping a variety named rather than folding it into "Other".
SHARE_CUTOFF <- 0.02
CUTOFF_YEARS <- c(2008, 2024)

ink <- "#24302a"; muted <- "#5c6b62"

theme_arec <- function(base = 12) {
  theme_minimal(base_size = base) +
    theme(
      panel.grid.minor    = element_blank(),
      panel.grid.major.x  = element_blank(),
      panel.grid.major.y  = element_line(colour = "grey88", linewidth = 0.3),
      axis.title          = element_text(colour = muted, size = base - 1),
      plot.title          = element_text(colour = ink, size = base, face = "bold"),
      plot.title.position = "plot",
      legend.position     = "none"
    )
}

# ==============================================================================
# 1. Variety shares by year
# ==============================================================================

prov <- fread(file.path(BARLEY_DIR, "output/provincial_barley_acreage.csv"))
prov <- prov[year >= 2008 & year <= 2025]

var_info <- fread(file.path(BARLEY_DIR, "output/cgc_variety_info.csv"))
MALT_VARS <- var_info[is_malt == 1, variety_code]

## Institution prefixes stripped so "AAC Synergy" and "synergy" match the
## malt classification table.
norm_name <- function(v) {
  v <- tolower(trimws(v))
  codes <- c("aac", "cdc", "ab", "ac", "sy", "kws", "sw", "lg", "as", "rgt")
  v <- gsub(paste0("^(", paste(codes, collapse = "|"), ") "), "", v)
  v <- gsub(paste0(" (", paste(codes, collapse = "|"), ")$"), "", v)
  gsub(" ", "", v)
}

total_by_year <- prov[, .(total_acres = sum(acres_inflated)), by = year]
var_by_year <- prov[, .(var_acres = sum(acres_inflated)), by = .(year, variety)]
var_by_year <- merge(var_by_year, total_by_year, by = "year")
var_by_year[, share := var_acres / total_acres]
var_by_year[, vc := norm_name(variety)]
var_by_year[, type := fifelse(vc %in% MALT_VARS, "malt", "feed")]

# ==============================================================================
# 2. Collapse minor varieties into "Other"
# ==============================================================================

## A variety stays named if it cleared the cutoff in either bookend year --
## that keeps both the varieties on their way out (big in 2008) and the ones
## on their way in (big in 2024).
endpoint_share <- var_by_year[year %in% CUTOFF_YEARS,
  .(max_endpoint_share = max(share)), by = variety]
named <- endpoint_share[max_endpoint_share >= SHARE_CUTOFF, variety]

var_by_year[, var_display := fifelse(variety %in% named, variety, "other")]
var_shares <- var_by_year[, .(share = sum(share), type = type[1]),
  by = .(year, var_display)]

var_shares[var_display != "other" & type == "malt",
  variety_label := paste0(var_display, " (malt)")]
var_shares[var_display != "other" & type == "feed",
  variety_label := paste0(var_display, " (feed)")]
var_shares[var_display == "other", variety_label := "Other varieties"]

# ==============================================================================
# 3. Stack order and colours
# ==============================================================================

## Order the stack by when each variety first became visible, so the bands
## read left-to-right as a succession of varieties.
first_significant <- var_shares[variety_label != "Other varieties" & share > 0.02,
  .(first_yr = min(year)), by = variety_label]
setorder(first_significant, first_yr)
stack_levels <- c("Other varieties", first_significant$variety_label)
n_var <- length(first_significant$variety_label)

var_shares[, variety_label := factor(variety_label, levels = stack_levels)]

all_combos <- CJ(year = sort(unique(var_shares$year)),
  variety_label = factor(stack_levels, levels = stack_levels))
var_shares <- merge(all_combos, var_shares,
  by = c("year", "variety_label"), all.x = TRUE)
var_shares[is.na(share), share := 0]
setorder(var_shares, year, variety_label)

var_shares[, cumshare := cumsum(share * 100), by = year]
var_shares[, ymax := cumshare]
var_shares[, ymin := ymax - share * 100]
var_shares[, ymid := (ymin + ymax) / 2]

cols <- colorRampPalette(c("#E3F2FD", "#90CAF9", "#42A5F5",
  "#1565C0", "#6A1B9A", "#311B92"))(n_var)
names(cols) <- first_significant$variety_label
color_map <- c("Other varieties" = "#EDEDED", cols)

min_yr <- min(var_shares$year)
max_yr <- max(var_shares$year)

# ==============================================================================
# 4A. Direct labels
# ==============================================================================

## Varieties already present in the first year get labelled on the left, the
## rest on the right, so each label sits at the end of its own band.
vars_at_start <- var_shares[year == min_yr & share > 0.001,
  as.character(variety_label)]
right_vars <- setdiff(as.character(stack_levels), vars_at_start)

left_labels <- var_shares[year == min_yr &
  as.character(variety_label) %in% vars_at_start & share > 0.001,
  .(variety_label, y = ymid)]
right_labels <- var_shares[year == max_yr &
  as.character(variety_label) %in% right_vars & share > 0.001,
  .(variety_label, y = ymid)]

fig_direct <- ggplot(var_shares,
    aes(x = year, ymin = ymin, ymax = ymax, fill = variety_label)) +
  geom_ribbon(color = "white", linewidth = 0.4) +
  scale_fill_manual(values = color_map) +
  scale_y_continuous(labels = function(x) paste0(x, "%"),
    expand = expansion(mult = c(0, 0))) +
  scale_x_continuous(breaks = seq(2008, 2024, 4),
    limits = c(min_yr - 9, max_yr + 9),
    expand = expansion(mult = c(0, 0))) +
  geom_text_repel(data = left_labels,
    aes(x = min_yr, y = y, label = variety_label),
    inherit.aes = FALSE, hjust = 1, size = 3.6,
    direction = "y", nudge_x = -1,
    xlim = c(min_yr - 9, min_yr),
    segment.size = 0.25, segment.color = "grey50",
    min.segment.length = 0, force = 3, max.overlaps = 30) +
  geom_text_repel(data = right_labels,
    aes(x = max_yr, y = y, label = variety_label),
    inherit.aes = FALSE, hjust = 0, size = 3.6,
    direction = "y", nudge_x = 1,
    xlim = c(max_yr, max_yr + 9),
    segment.size = 0.25, segment.color = "grey50",
    min.segment.length = 0, force = 3, max.overlaps = 30) +
  labs(title = "A. Direct labels", x = NULL, y = "Share of barley acreage") +
  theme_arec() +
  theme(panel.grid.major.y = element_blank()) +
  coord_cartesian(clip = "off")

# ==============================================================================
# 4B. Legend
# ==============================================================================

## Same bands, same colours; the reader now has to match each band to a swatch.
## Legend order is reversed so it runs top-to-bottom in the same order the
## bands stack on the plot.
fig_legend <- ggplot(var_shares,
    aes(x = year, ymin = ymin, ymax = ymax, fill = variety_label)) +
  geom_ribbon(color = "white", linewidth = 0.4) +
  scale_fill_manual(values = color_map, breaks = rev(stack_levels)) +
  scale_y_continuous(labels = function(x) paste0(x, "%"),
    expand = expansion(mult = c(0, 0))) +
  scale_x_continuous(breaks = seq(2008, 2024, 4),
    expand = expansion(mult = c(0, 0))) +
  labs(title = "B. Legend", x = NULL, y = "Share of barley acreage") +
  theme_arec() +
  theme(
    panel.grid.major.y = element_blank(),
    legend.position = "right",
    legend.title = element_blank(),
    legend.text = element_text(size = 9),
    legend.key.size = unit(0.85, "lines")
  )

# ==============================================================================
# 5. Save
# ==============================================================================

ggsave(file.path(OUT_DIR, "variety_shares_direct_labels.png"), fig_direct,
  width = 9, height = 5.5, dpi = 300)
ggsave(file.path(OUT_DIR, "variety_shares_legend.png"), fig_legend,
  width = 9, height = 5.5, dpi = 300)

message(sprintf("Named varieties (>= %.0f%% in %s): %d",
  SHARE_CUTOFF * 100, paste(CUTOFF_YEARS, collapse = " or "), n_var))
message(paste(" -", first_significant$variety_label, collapse = "\n"))
message("Saved images/variety_shares_direct_labels.png and images/variety_shares_legend.png")

# sessionInfo()
