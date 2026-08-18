# Figures for Module 3: the common chart types, each drawn from the same
# Saskatchewan variety data so students can compare the shapes directly.
# Palette matches R/strip_plot.R.

library(ggplot2)

prairie <- "#4a7c59"; ink <- "#24302a"; muted <- "#5c6b62"; wheat <- "#b7973f"
sky <- "#3d6b8c"; clay <- "#a85b3c"

# A quiet theme: no gridlines beyond a faint horizontal set, no chart junk.
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

# --- the data -------------------------------------------------------------
# Provincial averages by crop and year, built the same way as the PivotTable
# workbook: roll the risk zones up to a provincial figure first, weighting by
# acres, so we are not averaging zones that farm wildly different acreages.
load_yields <- function(path = "practice/data/sask_variety_yields.csv") {
  d <- read.csv(path, stringsAsFactors = FALSE)
  d <- d[!is.na(d$Acres) & !is.na(d$Yield) & d$Acres > 0, ]
  keep <- c("Wheat - Hard Red Spring", "Canola/Rapeseed", "Barley", "Oats")
  d <- d[d$Crop %in% keep, ]
  d$Crop <- c("Wheat - Hard Red Spring" = "Spring wheat",
              "Canola/Rapeseed" = "Canola",
              "Barley" = "Barley", "Oats" = "Oats")[d$Crop]
  d
}

# Weighted mean yield by crop x year
by_crop_year <- function(d) {
  agg <- aggregate(cbind(num = d$Acres * d$Yield, den = d$Acres),
                   by = list(Crop = d$Crop, Year = d$Year), FUN = sum)
  agg$Yield <- agg$num / agg$den
  agg[order(agg$Crop, agg$Year), c("Crop", "Year", "Yield")]
}

# --- 1. bar chart: comparing categories -----------------------------------
fig_bar <- function(d) {
  a <- by_crop_year(d)
  a <- aggregate(Yield ~ Crop, data = a, FUN = mean)
  a$Crop <- factor(a$Crop, levels = a$Crop[order(a$Yield)])
  ggplot(a, aes(x = Yield, y = Crop)) +
    geom_col(fill = prairie, width = 0.68) +
    geom_text(aes(label = round(Yield)), hjust = -0.25,
              colour = ink, size = 3.1) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.12))) +
    labs(title = "Average yield by crop, 2021-2025",
         x = "Yield (bu/ac)", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank())
}

# --- 2. line chart: change over time --------------------------------------
fig_line <- function(d) {
  a <- by_crop_year(d)
  ends <- a[a$Year == max(a$Year), ]
  ggplot(a, aes(x = Year, y = Yield, colour = Crop)) +
    geom_line(linewidth = 0.8) +
    geom_point(size = 1.7) +
    geom_text(data = ends, aes(label = Crop), hjust = -0.12,
              size = 3.1, show.legend = FALSE) +
    scale_colour_manual(values = c("Spring wheat" = prairie, "Canola" = wheat,
                                   "Barley" = sky, "Oats" = clay)) +
    scale_x_continuous(breaks = sort(unique(a$Year)),
                       expand = expansion(mult = c(0.03, 0.22))) +
    labs(title = "Average yield by year", x = NULL, y = "Yield (bu/ac)") +
    theme_arec()
}

# --- 3. scatter plot: relationship between two variables ------------------
# Barley against spring wheat, one point per risk zone. Both crops face the same
# weather in a given zone, so the question is whether a zone that grows good
# wheat also grows good barley -- a relationship a reader can see immediately.
fig_scatter <- function(d) {
  yr <- max(d$Year)
  s  <- d[d$Year == yr & d$Crop %in% c("Spring wheat", "Barley"), ]
  z  <- aggregate(cbind(num = s$Acres * s$Yield, den = s$Acres),
                  by = list(Zone = s$Risk_Zone, Crop = s$Crop), FUN = sum)
  z$Yield <- z$num / z$den
  w <- merge(z[z$Crop == "Spring wheat", c("Zone", "Yield")],
             z[z$Crop == "Barley",       c("Zone", "Yield")],
             by = "Zone", suffixes = c("_wheat", "_barley"))

  ggplot(w, aes(x = Yield_wheat, y = Yield_barley)) +
    geom_point(colour = prairie, alpha = 0.75, size = 2.4) +
    labs(title = paste0("Zones that grow good wheat also grow good barley (", yr, ")"),
         x = "Spring wheat yield (bu/ac)", y = "Barley yield (bu/ac)") +
    theme_arec() +
    theme(panel.grid.major.x = element_line(colour = "grey92",
                                            linewidth = 0.3))
}

# --- 4. stacked bar: parts of a whole, over time --------------------------
fig_stacked <- function(d) {
  a <- aggregate(Acres ~ Crop + Year, data = d, FUN = sum)
  a$Acres <- a$Acres / 1e6
  ggplot(a, aes(x = factor(Year), y = Acres, fill = Crop)) +
    geom_col(width = 0.66) +
    scale_fill_manual(values = c("Spring wheat" = prairie, "Canola" = wheat,
                                 "Barley" = sky, "Oats" = clay)) +
    labs(title = "Acres seeded by crop (millions)",
         x = NULL, y = "Acres (millions)") +
    theme_arec() +
    theme(legend.position = "right",
          legend.title = element_blank(),
          legend.key.size = unit(0.8, "lines"))
}

# --- truncated vs zero baseline -------------------------------------------
# Malting barley variety trial results, Saskatchewan Seed Guide. The spread is
# only 11 bu/ac on yields of about 110, so a truncated axis exaggerates it
# dramatically -- which is exactly why seed marketing charts look the way they do.
malting <- data.frame(
  Variety    = c("AAC Connect", "AAC Synergy", "CDC Churchill",
                 "CDC Copeland", "CDC Fraser"),
  SiteYears  = c(46, 105, 46, 46, 43),
  Yield      = c(109, 114, 114, 103, 110)
)

#' @param ymin where the y axis starts: 100 for the misleading version, 0 honest.
fig_truncated <- function(ymin = 100, title = NULL) {
  d <- malting
  d$Variety <- factor(d$Variety, levels = d$Variety)
  ggplot(d, aes(x = Variety, y = Yield)) +
    geom_col(fill = prairie, width = 0.66) +
    geom_text(aes(label = Yield), vjust = -0.5, colour = ink, size = 3.1) +
    coord_cartesian(ylim = c(ymin, max(d$Yield) * 1.06)) +
    labs(title = title, x = NULL, y = "Yield (bu/ac)") +
    theme_arec() +
    theme(axis.text.x = element_text(size = 8.2))
}

# --- 5. the pie chart, and the same data as a bar -------------------------
# Drawn as a matched pair so the comparison is direct: identical numbers, and
# the bar version is the one you can actually read.
fig_pie_vs_bar <- function(d) {
  a <- aggregate(Acres ~ Crop, data = d, FUN = sum)
  a$share <- a$Acres / sum(a$Acres) * 100
  a$Crop <- factor(a$Crop, levels = a$Crop[order(-a$share)])
  cols <- c("Spring wheat" = prairie, "Canola" = wheat,
            "Barley" = sky, "Oats" = clay)

  pie <- ggplot(a, aes(x = "", y = share, fill = Crop)) +
    geom_col(width = 1) +
    coord_polar(theta = "y") +
    scale_fill_manual(values = cols) +
    labs(title = "A. As a pie chart") +
    theme_void(base_size = 10) +
    theme(plot.title = element_text(colour = ink, size = 10, face = "bold"),
          legend.title = element_blank(),
          legend.key.size = unit(0.8, "lines"))

  bar <- ggplot(a, aes(x = share, y = factor(Crop, levels = rev(levels(Crop))))) +
    geom_col(fill = prairie, width = 0.66) +
    geom_text(aes(label = paste0(round(share), "%")), hjust = -0.25,
              colour = ink, size = 3.1) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.15))) +
    labs(title = "B. As a bar chart", x = "Share of acres (%)", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank())

  list(pie = pie, bar = bar)
}
