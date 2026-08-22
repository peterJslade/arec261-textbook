# Figures for Module 4, chapter 12 (AI Tools).
# Palette and theme match R/chart_types.R.

library(ggplot2)
suppressMessages(library(dplyr))

prairie <- "#4a7c59"; ink <- "#24302a"; muted <- "#5c6b62"; wheat <- "#b7973f"
sky <- "#3d6b8c"; clay <- "#a85b3c"

theme_arec <- function(base = 10) {
  theme_minimal(base_size = base) +
    theme(
      panel.grid.minor   = element_blank(),
      panel.grid.major.x = element_blank(),
      panel.grid.major.y = element_line(colour = "grey88", linewidth = 0.3),
      axis.title         = element_text(colour = muted, size = base - 1),
      plot.title         = element_text(colour = ink, size = base, face = "bold"),
      plot.title.position = "plot",
      legend.position    = "none"
    )
}

CROPS <- c("Wheat - Hard Red Spring", "Canola/Rapeseed", "Barley", "Oats")

# The 2025 slice both the join figure and the units figure work from.
join_data <- function() {
  d <- read.csv("practice/data/sask_variety_yields.csv")
  p <- read.csv("practice/data/crop_prices.csv")
  d25 <- d |> filter(Year == 2025, Crop %in% CROPS, !is.na(Yield), Acres > 0)
  list(yields = d25, prices = p,
       joined = d25 |> left_join(p, by = "Crop") |>
                mutate(Revenue = Yield * Price_per_bu))
}

# --- 1. what the join silently threw away -----------------------------------
# Rows by crop, coloured by whether the naive join found a price. Barley and
# Oats match by luck; the two biggest crops do not, because the price table
# calls them "Canola" and "Spring wheat".
fig_join_loss <- function() {
  j <- join_data()$joined
  s <- j |>
    group_by(Crop) |>
    summarise(rows = n(), priced = !all(is.na(Price_per_bu)), .groups = "drop") |>
    mutate(short = case_match(
             Crop,
             "Wheat - Hard Red Spring" ~ "Spring wheat",
             "Canola/Rapeseed" ~ "Canola",
             .default = Crop),
           label = ifelse(priced, "matched a price", "silently dropped"))
  s$short <- factor(s$short, levels = s$short[order(s$rows)])

  ggplot(s, aes(x = rows, y = short, fill = label)) +
    geom_col(width = 0.66) +
    geom_text(aes(label = paste0(rows, " rows")), hjust = -0.12,
              colour = ink, size = 3) +
    scale_fill_manual(values = c("matched a price" = prairie,
                                 "silently dropped" = clay)) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.22))) +
    labs(x = "Rows in the 2025 data", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank(),
          legend.position = "top",
          legend.title = element_blank(),
          legend.text = element_text(size = 8),
          legend.key.size = unit(0.7, "lines"))
}

# --- 2. how loudly each failure announces itself ----------------------------
# The chapter's five failures placed on one axis: does R stop you, or not?
fig_failure_spectrum <- function() {
  f <- data.frame(
    x = c(0.06, 0.17, 0.28, 0.72, 0.92),
    lab = c("invented\nfunction", "wrong column\nname (dplyr)",
            "out-of-date\nargument", "confidently\nwrong number",
            "the silent\njoin"),
    y = c(0.32, -0.32, 0.32, 0.32, -0.32),
    loud = c(TRUE, TRUE, TRUE, FALSE, FALSE)
  )

  ggplot(f, aes(x = x, y = 0)) +
    annotate("segment", x = 0, xend = 1, y = 0, yend = 0,
             colour = "grey75", linewidth = 0.5) +
    geom_point(aes(colour = loud), size = 3.4) +
    geom_segment(aes(xend = x, yend = y * 0.45, colour = loud), linewidth = 0.3) +
    geom_text(aes(y = y, label = lab, colour = loud), size = 2.9,
              lineheight = 0.95, vjust = 0.5) +
    annotate("text", x = 0, y = 0.78, hjust = 0, size = 3, colour = prairie,
             fontface = "bold", label = "R stops you") +
    annotate("text", x = 1, y = 0.78, hjust = 1, size = 3, colour = clay,
             fontface = "bold", label = "nothing stops you") +
    scale_colour_manual(values = c("TRUE" = prairie, "FALSE" = clay)) +
    scale_y_continuous(limits = c(-0.62, 0.92)) +
    scale_x_continuous(limits = c(-0.04, 1.04)) +
    theme_void(base_size = 10) +
    theme(legend.position = "none")
}

# --- 3. one yield, three units ----------------------------------------------
# The same 2025 canola yield in the three units it gets quoted in. Canola is
# 50 lb/bu; an acre is 0.4047 ha.
fig_units <- function() {
  j <- join_data()$yields
  c25 <- j |> filter(Crop == "Canola/Rapeseed")
  bu <- weighted.mean(c25$Yield, c25$Acres)

  u <- data.frame(
    unit = c("bushels per acre", "pounds per acre", "kilograms per hectare"),
    value = c(bu, bu * 50, bu * 50 * 0.453592 / 0.404686)
  )
  u$unit <- factor(u$unit, levels = rev(u$unit))

  ggplot(u, aes(x = value, y = unit)) +
    geom_col(fill = prairie, width = 0.6) +
    geom_text(aes(label = format(round(value), big.mark = ",")),
              hjust = -0.15, colour = ink, size = 3.1) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.16))) +
    labs(x = "The same 2025 canola crop, three ways", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank())
}

# --- 4. how much data is missing, by year (Module 4, chapter 14) ------------
# Recorded vs missing yields per year. Half of 2021 is missing and almost none
# of 2025, so a year filter changes coverage far more than students expect.
fig_missing_by_year <- function() {
  d <- read.csv("practice/data/sask_variety_yields.csv")
  s <- d |>
    group_by(Year) |>
    summarise(recorded = sum(!is.na(Yield)),
              missing  = sum(is.na(Yield)), .groups = "drop") |>
    tidyr::pivot_longer(c(recorded, missing), names_to = "kind", values_to = "n")

  ggplot(s, aes(x = factor(Year), y = n, fill = kind)) +
    geom_col(width = 0.66) +
    scale_fill_manual(values = c("recorded" = prairie, "missing" = "grey78")) +
    labs(x = NULL, y = "Rows") +
    theme_arec() +
    theme(legend.position = "top", legend.title = element_blank(),
          legend.text = element_text(size = 8),
          legend.key.size = unit(0.7, "lines"))
}
