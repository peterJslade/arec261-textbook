# Figures for Module 4: the common chart types, each drawn from the same
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
    labs(title = NULL, x = "Yield (bu/ac)", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank())
}

# --- 1b. the same bar chart, vertical -------------------------------------
# Uses the barley varieties, whose names are long enough to show the problem:
# vertical bars force the labels to rotate, overlap, or be truncated.
fig_bar_vertical <- function() {
  d <- malting
  d$Variety <- factor(d$Variety, levels = d$Variety[order(-d$Yield)])
  ggplot(d, aes(x = Variety, y = Yield)) +
    geom_col(fill = prairie, width = 0.68) +
    labs(title = NULL, x = NULL, y = "Yield (bu/ac)") +
    theme_arec() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 8))
}

fig_bar_horizontal <- function() {
  d <- malting
  d$Variety <- factor(d$Variety, levels = d$Variety[order(d$Yield)])
  ggplot(d, aes(x = Yield, y = Variety)) +
    geom_col(fill = prairie, width = 0.68) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.08))) +
    labs(title = NULL, x = "Yield (bu/ac)", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank(),
          axis.text.y = element_text(size = 8))
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
    labs(title = NULL,
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

# --- encoding a third variable --------------------------------------------
# Wheat yield against barley yield by risk zone (as fig_scatter), with acres
# seeded encoded as the size of the point. Three variables, one plot, and the
# third one is read from an aesthetic the eye handles well enough for ranking.
fig_bubble <- function(d) {
  yr <- max(d$Year)
  s  <- d[d$Year == yr & d$Crop %in% c("Spring wheat", "Barley"), ]
  z  <- aggregate(cbind(num = s$Acres * s$Yield, den = s$Acres),
                  by = list(Zone = s$Risk_Zone, Crop = s$Crop), FUN = sum)
  z$Yield <- z$num / z$den
  w <- merge(z[z$Crop == "Spring wheat", c("Zone", "Yield", "den")],
             z[z$Crop == "Barley",       c("Zone", "Yield")],
             by = "Zone", suffixes = c("_wheat", "_barley"))
  w$Acres <- w$den / 1e3

  ggplot(w, aes(x = Yield_wheat, y = Yield_barley, size = Acres)) +
    geom_point(colour = prairie, alpha = 0.5) +
    scale_size_area(max_size = 8, name = "Wheat acres\n(thousands)") +
    labs(x = "Spring wheat yield (bu/ac)", y = "Barley yield (bu/ac)") +
    theme_arec() +
    theme(panel.grid.major.x = element_line(colour = "grey92", linewidth = 0.3),
          legend.position = "right",
          legend.title = element_text(colour = muted, size = 8),
          legend.text = element_text(size = 8))
}

# --- the dual axis --------------------------------------------------------
# Canola acres and canola yield share an x axis but nothing else. The right
# axis is scaled arbitrarily, so where the lines cross -- and which appears to
# lead the other -- is a choice the chart's author made, not a fact.
fig_dual_axis <- function(d, scale_hi = TRUE) {
  a <- by_crop_year(d)
  a <- a[a$Crop == "Canola", c("Year", "Yield")]
  ac <- aggregate(Acres ~ Year, data = d[d$Crop == "Canola", ], FUN = sum)
  m <- merge(a, ac, by = "Year")
  m$AcresM <- m$Acres / 1e6

  # the arbitrary choice: how to map acres onto the yield axis
  rng <- if (scale_hi) c(42, 52) else c(18, 30)
  rescale <- function(x) {
    (x - min(m$AcresM)) / diff(range(m$AcresM)) * diff(rng) + rng[1]
  }
  inv <- function(y) {
    (y - rng[1]) / diff(rng) * diff(range(m$AcresM)) + min(m$AcresM)
  }

  ggplot(m, aes(x = Year)) +
    geom_line(aes(y = Yield), colour = prairie, linewidth = 0.9) +
    geom_line(aes(y = rescale(AcresM)), colour = clay, linewidth = 0.9,
              linetype = "longdash") +
    scale_y_continuous(
      name = "Yield (bu/ac)",
      sec.axis = sec_axis(~ inv(.), name = "Acres (millions)")) +
    scale_x_continuous(breaks = sort(unique(m$Year))) +
    labs(x = NULL) +
    theme_arec() +
    theme(axis.title.y.left  = element_text(colour = prairie),
          axis.title.y.right = element_text(colour = clay))
}

# --- when not to use a chart ----------------------------------------------
# World wheat production, 2024/25 marketing year, million tonnes. Approximate
# USDA WASDE figures -- close enough for the teaching point, which is about
# whether a chart earns its place, not about the exact tonnages.
wheat_world <- data.frame(
  Country = c("China", "India", "Russia", "United States", "Australia",
              "Canada", "Pakistan", "Ukraine", "Turkey", "Argentina",
              "Germany", "France", "Kazakhstan", "United Kingdom", "Poland"),
  Production = c(140.1, 113.3, 81.5, 53.7, 34.1, 34.9, 31.6, 22.4, 21.0,
                 17.5, 20.8, 25.4, 15.0, 11.1, 12.2)
)

#' @param n how many countries to show. n = 2 gives the Canada/US comparison
#'   that does not need a chart; n = 15 gives the one that does.
fig_wheat <- function(n = 15) {
  d <- wheat_world
  if (n == 2) {
    d <- d[d$Country %in% c("Canada", "United States"), ]
  } else {
    d <- d[order(-d$Production), ][seq_len(n), ]
  }
  d$Country <- factor(d$Country, levels = d$Country[order(d$Production)])
  ggplot(d, aes(x = Production, y = Country,
                fill = Country == "Canada")) +
    geom_col(width = 0.68, show.legend = FALSE) +
    scale_fill_manual(values = c("TRUE" = prairie, "FALSE" = "grey72")) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.1))) +
    labs(x = "Production (million tonnes)", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank(),
          axis.text.y = element_text(size = 8))
}

# --- pie vs bar: 2021 Canadian federal election ---------------------------
# Popular vote shares, Elections Canada official results. The Conservatives
# outpolled the Liberals by about 0.6 points -- invisible as two adjacent
# wedges, obvious as two bars.
election <- data.frame(
  Party = c("Conservative", "Liberal", "NDP", "Bloc Québécois",
            "People's Party", "Green", "Other"),
  Share = c(33.7, 32.6, 17.8, 7.6, 4.9, 2.3, 1.1)
)

fig_vote <- function(kind = c("pie", "bar")) {
  kind <- match.arg(kind)
  d <- election
  d$Party <- factor(d$Party, levels = d$Party)
  cols <- c("Conservative" = "#1f4e8c", "Liberal" = "#c0392b",
            "NDP" = "#e08214", "Bloc Québécois" = "#5aa5d6",
            "People's Party" = "#4d4d9e", "Green" = "#4a7c59",
            "Other" = "grey75")

  if (kind == "pie") {
    ggplot(d, aes(x = "", y = Share, fill = Party)) +
      geom_col(width = 1, colour = "white", linewidth = 0.3) +
      coord_polar(theta = "y", direction = -1) +
      scale_fill_manual(values = cols) +
      labs(title = NULL) +
      theme_void(base_size = 10) +
      theme(legend.title = element_blank(),
            legend.text = element_text(size = 8),
            legend.key.size = unit(0.72, "lines"))
  } else {
    ggplot(d, aes(x = Share, y = factor(Party, levels = rev(levels(Party))),
                  fill = Party)) +
      geom_col(width = 0.68, show.legend = FALSE) +
      scale_fill_manual(values = cols) +
      scale_x_continuous(expand = expansion(mult = c(0, 0.06))) +
      labs(title = NULL, x = "Share of the popular vote (%)", y = NULL) +
      theme_arec() +
      theme(panel.grid.major.y = element_blank(),
            axis.text.y = element_text(size = 8))
  }
}

# --- annotation: nitrogen fertilizer prices -------------------------------
# Approximate US Gulf urea price, USD per tonne, annual average. Indicative
# figures assembled from published price commentary rather than a single
# series -- the shape (2008 spike, 2020 trough, 2022 record) is what the
# example needs, not the exact monthly numbers.
urea <- data.frame(
  Year  = 2000:2025,
  Price = c(110, 125, 105, 150, 180, 230, 245, 310, 495, 250,
            290, 400, 415, 340, 320, 275, 205, 215, 250, 235,
            215, 480, 700, 380, 350, 365)
)

#' @param level "heavy" annotates everything; "light" annotates the one thing
#'   a reader would actually stop at.
fig_fertilizer <- function(level = c("light", "heavy")) {
  level <- match.arg(level)
  d <- urea
  p <- ggplot(d, aes(x = Year, y = Price)) +
    geom_line(colour = prairie, linewidth = 0.8) +
    scale_x_continuous(breaks = seq(2000, 2025, 5)) +
    scale_y_continuous(limits = c(0, 900),
                       labels = function(x) paste0("$", x)) +
    labs(x = NULL, y = "Urea price (USD/tonne)") +
    theme_arec()

  note <- function(p, x, y, lab, xend, yend, curv = 0.25, hj = 0, sz = 2.7) {
    p +
      annotate("curve", x = x, xend = xend, y = y, yend = yend,
               curvature = curv, linewidth = 0.25, colour = muted,
               arrow = arrow(length = unit(0.05, "in"), type = "closed")) +
      annotate("text", x = x, y = y, label = lab, hjust = hj, vjust = 0.5,
               colour = muted, size = sz, lineheight = 0.95)
  }

  if (level == "heavy") {
    p <- note(p, 2001.2, 330, "prices drift\nthrough the\nearly 2000s", 2002.6, 140, 0.3)
    p <- note(p, 2004.4, 430, "steady climb\nbegins",            2005.4, 250, -0.3)
    p <- note(p, 2006.0, 620, "2008: demand and\nenergy costs spike", 2007.9, 505, -0.3)
    p <- note(p, 2009.6, 120, "crash after the\nfinancial crisis", 2009.2, 235, 0.3)
    p <- note(p, 2012.4, 560, "second peak",                     2012.0, 428, -0.3)
    p <- note(p, 2015.5, 105, "long slide as new\ncapacity comes on", 2016.4, 192, 0.3)
    p <- note(p, 2018.6, 430, "gentle recovery",                 2018.2, 262, -0.3)
    p <- note(p, 2020.0, 60,  "COVID low",                       2020.2, 200, 0.3)
    p <- note(p, 2013.6, 800, "2022: gas prices and\nthe war in Ukraine", 2021.7, 715, -0.18)
    p <- note(p, 2017.4, 610, "falls back, but not\nto 2020 levels", 2023.6, 395, 0.22)
  } else {
    p <- note(p, 2002.0, 640, "2022: European gas prices\nand the war in Ukraine push\nurea to a record",
              2021.6, 700, -0.20, sz = 2.9)
  }
  p
}

# --- a few extras ---------------------------------------------------------

# Shaded range: the spread of zone-level yields behind the provincial average.
# geom_ribbon draws the band; the line sits on top of it.
fig_ribbon <- function(d) {
  s <- d[d$Crop == "Spring wheat", ]
  z <- aggregate(cbind(num = s$Acres * s$Yield, den = s$Acres),
                 by = list(Zone = s$Risk_Zone, Year = s$Year), FUN = sum)
  z$Yield <- z$num / z$den
  b <- do.call(rbind, lapply(split(z, z$Year), function(g) data.frame(
    Year = g$Year[1], lo = quantile(g$Yield, 0.1), hi = quantile(g$Yield, 0.9),
    mid = mean(g$Yield))))

  ggplot(b, aes(x = Year)) +
    geom_ribbon(aes(ymin = lo, ymax = hi), fill = prairie, alpha = 0.18) +
    geom_line(aes(y = mid), colour = prairie, linewidth = 0.8) +
    scale_x_continuous(breaks = sort(unique(b$Year))) +
    labs(x = NULL, y = "Yield (bu/ac)") +
    theme_arec()
}

# Trend line: the same scatter with a fitted straight line through it.
fig_trend <- function(d) {
  yr <- max(d$Year)
  s  <- d[d$Year == yr & d$Crop %in% c("Spring wheat", "Barley"), ]
  z  <- aggregate(cbind(num = s$Acres * s$Yield, den = s$Acres),
                  by = list(Zone = s$Risk_Zone, Crop = s$Crop), FUN = sum)
  z$Yield <- z$num / z$den
  w <- merge(z[z$Crop == "Spring wheat", c("Zone", "Yield")],
             z[z$Crop == "Barley",       c("Zone", "Yield")],
             by = "Zone", suffixes = c("_wheat", "_barley"))

  ggplot(w, aes(x = Yield_wheat, y = Yield_barley)) +
    geom_smooth(method = "lm", se = TRUE, colour = clay, fill = clay,
                alpha = 0.12, linewidth = 0.6, formula = y ~ x) +
    geom_point(colour = prairie, alpha = 0.75, size = 2.2) +
    labs(x = "Spring wheat yield (bu/ac)", y = "Barley yield (bu/ac)") +
    theme_arec() +
    theme(panel.grid.major.x = element_line(colour = "grey92", linewidth = 0.3))
}

# Reference line: a horizontal average with the bars read against it.
fig_refline <- function(d) {
  a <- by_crop_year(d)
  a <- a[a$Crop == "Canola", ]
  m <- mean(a$Yield)
  ggplot(a, aes(x = factor(Year), y = Yield)) +
    geom_col(fill = prairie, width = 0.66) +
    geom_hline(yintercept = m, linetype = "dashed", colour = clay,
               linewidth = 0.5) +
    annotate("text", x = 0.62, y = m + 2.4, hjust = 0,
             label = paste0("five-year average, ", round(m), " bu/ac"),
             colour = clay, size = 2.9) +
    labs(x = NULL, y = "Canola yield (bu/ac)") +
    theme_arec()
}

# Waterfall: how a starting figure becomes an ending one through gains and
# losses. Built by hand -- ggplot has no waterfall geom, and Excel does.
fig_waterfall <- function() {
  d <- data.frame(
    Item  = c("Gross revenue", "Seed", "Fertilizer", "Chemical",
              "Machinery", "Land", "Other", "Net margin"),
    Value = c(560, -55, -140, -60, -95, -120, -35, 55),
    Kind  = c("total", rep("cost", 6), "total")
  )
  d$Item <- factor(d$Item, levels = d$Item)
  # running position of each floating bar
  end <- cumsum(ifelse(d$Kind == "total" & seq_len(nrow(d)) > 1, 0, d$Value))
  d$ymax <- ifelse(d$Kind == "total" & seq_len(nrow(d)) > 1, d$Value, end)
  d$ymin <- ifelse(d$Kind == "total", 0, end - d$Value)

  ggplot(d, aes(x = Item, fill = Kind)) +
    geom_rect(aes(xmin = as.numeric(Item) - 0.34,
                  xmax = as.numeric(Item) + 0.34,
                  ymin = ymin, ymax = ymax)) +
    scale_fill_manual(values = c("total" = prairie, "cost" = clay)) +
    scale_y_continuous(labels = function(x) paste0("$", x)) +
    labs(x = NULL, y = "Per acre") +
    theme_arec() +
    theme(axis.text.x = element_text(angle = 40, hjust = 1, size = 7.6),
          legend.position = "none")
}

# --- clutter vs clean -----------------------------------------------------
# The same line chart drawn twice. The cluttered version collects the defaults
# and decorations Excel offers: heavy gridlines both ways, a tick every year on
# both axes, a boxed legend, a drop shadow behind each line, markers on every
# point, and a background fill. Nothing here adds information.
fig_clutter <- function(d) {
  a <- by_crop_year(d)
  ggplot(a, aes(x = Year, y = Yield, colour = Crop, shape = Crop)) +
    # a "drop shadow": the same line offset and greyed, as Excel would draw it
    geom_line(aes(x = Year + 0.04, y = Yield - 1.1), colour = "grey55",
              linewidth = 1.4, alpha = 0.5, show.legend = FALSE) +
    geom_line(linewidth = 1.1) +
    geom_point(size = 2.6, fill = "white", stroke = 1) +
    scale_shape_manual(values = c(21, 22, 23, 24)) +
    scale_colour_manual(values = c("Spring wheat" = "#c0392b", "Canola" = "#e67e22",
                                   "Barley" = "#8e44ad", "Oats" = "#16a085")) +
    scale_x_continuous(breaks = seq(2021, 2025, 1),
                       minor_breaks = seq(2021, 2025, 0.25)) +
    scale_y_continuous(breaks = seq(20, 120, 5),
                       minor_breaks = seq(20, 120, 2.5)) +
    labs(title = NULL, x = "Year", y = "Yield (bu/ac)") +
    theme_grey(base_size = 10) +
    theme(
      panel.background  = element_rect(fill = "#eef0f4", colour = NA),
      panel.grid.major  = element_line(colour = "grey55", linewidth = 0.45),
      panel.grid.minor  = element_line(colour = "grey70", linewidth = 0.3),
      axis.ticks        = element_line(colour = "grey30", linewidth = 0.5),
      axis.ticks.length = unit(3.5, "pt"),
      legend.position   = "right",
      legend.title      = element_blank(),
      legend.background = element_rect(fill = "white", colour = "grey40"),
      legend.key.size   = unit(0.8, "lines"),
      plot.title        = element_text(size = 10, face = "bold", colour = ink),
      plot.title.position = "plot"
    )
}

fig_declutter <- function(d) {
  a <- by_crop_year(d)
  ends <- a[a$Year == max(a$Year), ]
  ggplot(a, aes(x = Year, y = Yield, colour = Crop)) +
    geom_line(linewidth = 0.8) +
    geom_text(data = ends, aes(label = Crop), hjust = -0.12, size = 3.1) +
    scale_colour_manual(values = c("Spring wheat" = prairie, "Canola" = wheat,
                                   "Barley" = sky, "Oats" = clay)) +
    scale_x_continuous(breaks = seq(2021, 2025, 2),
                       expand = expansion(mult = c(0.03, 0.34))) +
    labs(title = NULL, x = NULL, y = "Yield (bu/ac)") +
    theme_arec()
}

# --- patterned fills ------------------------------------------------------
# Hatched fills date from monochrome printing, where they were the only way to
# tell series apart. On screen they vibrate and hide the data. ggplot2 has no
# pattern fill, so the hatching is drawn as line segments clipped to each bar.
fig_pattern <- function(d) {
  a <- by_crop_year(d)
  a <- aggregate(Yield ~ Crop, data = a, FUN = mean)
  a <- a[order(-a$Yield), ]
  a$i <- seq_len(nrow(a))

  # diagonal hatching: for bar i, a fan of segments across its width
  hatch <- do.call(rbind, lapply(seq_len(nrow(a)), function(k) {
    h <- a$Yield[k]; x0 <- a$i[k] - 0.33; x1 <- a$i[k] + 0.33
    # spacing alternates per bar, as clip-art patterns do
    step <- c(3.2, 5.0, 2.4, 4.0)[((k - 1) %% 4) + 1]
    offs <- seq(-h, h, by = step)
    data.frame(x = pmax(x0, x0), xend = x1,
               y = pmin(pmax(offs, 0), h),
               yend = pmin(pmax(offs + (x1 - x0) * 26, 0), h))
  }))
  hatch <- hatch[hatch$yend > hatch$y, ]

  ggplot(a, aes(x = i, y = Yield)) +
    geom_col(fill = "grey82", colour = "grey20", width = 0.66, linewidth = 0.5) +
    geom_segment(data = hatch, aes(x = x, xend = xend, y = y, yend = yend),
                 colour = "grey25", linewidth = 0.3, inherit.aes = FALSE) +
    geom_col(fill = NA, colour = "grey20", width = 0.66, linewidth = 0.5) +
    scale_x_continuous(breaks = a$i, labels = a$Crop) +
    scale_y_continuous(breaks = seq(0, 100, 10),
                       minor_breaks = seq(0, 100, 5)) +
    labs(title = NULL, x = NULL, y = "Yield (bu/ac)") +
    theme_grey(base_size = 10) +
    theme(
      panel.background = element_rect(fill = "#f2f2f2", colour = NA),
      panel.grid.major = element_line(colour = "grey60", linewidth = 0.4),
      panel.grid.minor = element_line(colour = "grey75", linewidth = 0.25),
      axis.ticks       = element_line(colour = "grey30"),
      axis.text.x      = element_text(size = 8),
      plot.title       = element_text(size = 10, face = "bold", colour = ink),
      plot.title.position = "plot"
    )
}

fig_flat <- function(d) {
  a <- by_crop_year(d)
  a <- aggregate(Yield ~ Crop, data = a, FUN = mean)
  a$Crop <- factor(a$Crop, levels = a$Crop[order(a$Yield)])
  ggplot(a, aes(x = Yield, y = Crop)) +
    geom_col(fill = prairie, width = 0.66) +
    geom_text(aes(label = round(Yield)), hjust = -0.25, colour = ink, size = 3.1) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.14))) +
    labs(title = NULL, x = "Yield (bu/ac)", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank(),
          axis.text.y = element_text(size = 8))
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

#' @param ymin   where the y axis starts: 100 for the misleading version, 0 honest.
#' @param labels print the value above each bar. Off for the truncated version:
#'   without the numbers there is nothing to check the bar heights against, which
#'   is how these charts usually appear in the wild.
fig_truncated <- function(ymin = 100, labels = TRUE, title = NULL) {
  d <- malting
  d$Variety <- factor(d$Variety, levels = d$Variety)
  p <- ggplot(d, aes(x = Variety, y = Yield)) +
    geom_col(fill = prairie, width = 0.66)
  if (labels) {
    p <- p + geom_text(aes(label = Yield), vjust = -0.5, colour = ink, size = 3.1)
  }
  p +
    coord_cartesian(ylim = c(ymin, max(d$Yield) * 1.06)) +
    labs(title = title, x = NULL, y = "Yield (bu/ac)") +
    theme_arec() +
    theme(axis.text.x = element_text(size = 8.2))
}

# --- grouped bars ---------------------------------------------------------
# The same acres data as fig_stacked(), with the crops side by side instead of
# stacked. Every bar now sits on the baseline, but there are 20 of them and the
# reader has to decide which comparison the chart is for: across crops within a
# year, or across years within a crop. Neither reads cleanly.
fig_grouped <- function(d) {
  a <- aggregate(Acres ~ Crop + Year, data = d, FUN = sum)
  a$Acres <- a$Acres / 1e6
  ggplot(a, aes(x = factor(Year), y = Acres, fill = Crop)) +
    geom_col(position = position_dodge(width = 0.78), width = 0.72) +
    scale_fill_manual(values = c("Spring wheat" = prairie, "Canola" = wheat,
                                 "Barley" = sky, "Oats" = clay)) +
    labs(title = NULL, x = NULL, y = "Acres (millions)") +
    theme_arec() +
    theme(legend.position = "right",
          legend.title = element_blank(),
          legend.key.size = unit(0.8, "lines"))
}

# The same numbers again, small multiples: one panel per crop. Each panel is a
# simple line, so "how did canola move?" is answered without any decoding.
fig_facet <- function(d) {
  a <- aggregate(Acres ~ Crop + Year, data = d, FUN = sum)
  a$Acres <- a$Acres / 1e6
  ggplot(a, aes(x = Year, y = Acres)) +
    geom_line(colour = prairie, linewidth = 0.7) +
    geom_point(colour = prairie, size = 1.4) +
    facet_wrap(~ Crop, nrow = 1) +
    scale_x_continuous(breaks = c(2021, 2025), expand = expansion(mult = 0.14)) +
    labs(title = NULL, x = NULL, y = "Acres (millions)") +
    theme_arec() +
    theme(strip.text = element_text(colour = ink, size = 9),
          panel.grid.major.x = element_blank(),
          panel.spacing.x = unit(1.1, "lines"))
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
    geom_text(
      aes(label = paste0(Crop, "\n", round(share), "%")),
      position = position_stack(vjust = 0.5),
      colour = ink,
      size = 2.7
    ) +
    coord_polar(theta = "y") +
    scale_fill_manual(values = cols) +
    labs(title = NULL) +
    theme_void(base_size = 10) +
    theme(legend.position = "none")

  bar <- ggplot(a, aes(x = share, y = factor(Crop, levels = rev(levels(Crop))))) +
    geom_col(fill = prairie, width = 0.66) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.06))) +
    labs(title = NULL, x = "Share of acres (%)", y = NULL) +
    theme_arec() +
    theme(panel.grid.major.y = element_blank())

  list(pie = pie, bar = bar)
}
