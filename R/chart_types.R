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

# --- 1b. the same bar chart, vertical -------------------------------------
# Uses the barley varieties, whose names are long enough to show the problem:
# vertical bars force the labels to rotate, overlap, or be truncated.
fig_bar_vertical <- function() {
  d <- malting
  d$Variety <- factor(d$Variety, levels = d$Variety[order(-d$Yield)])
  ggplot(d, aes(x = Variety, y = Yield)) +
    geom_col(fill = prairie, width = 0.68) +
    labs(title = "A. Vertical", x = NULL, y = "Yield (bu/ac)") +
    theme_arec() +
    theme(axis.text.x = element_text(angle = 45, hjust = 1, size = 8))
}

fig_bar_horizontal <- function() {
  d <- malting
  d$Variety <- factor(d$Variety, levels = d$Variety[order(d$Yield)])
  ggplot(d, aes(x = Yield, y = Variety)) +
    geom_col(fill = prairie, width = 0.68) +
    scale_x_continuous(expand = expansion(mult = c(0, 0.08))) +
    labs(title = "B. Horizontal", x = "Yield (bu/ac)", y = NULL) +
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
      labs(title = "A. Pie chart") +
      theme_void(base_size = 10) +
      theme(plot.title = element_text(colour = ink, size = 10, face = "bold"),
            legend.title = element_blank(),
            legend.text = element_text(size = 8),
            legend.key.size = unit(0.72, "lines"))
  } else {
    ggplot(d, aes(x = Share, y = factor(Party, levels = rev(levels(Party))),
                  fill = Party)) +
      geom_col(width = 0.68, show.legend = FALSE) +
      geom_text(aes(label = sprintf("%.1f", Share)), hjust = -0.22,
                colour = ink, size = 3) +
      scale_fill_manual(values = cols) +
      scale_x_continuous(expand = expansion(mult = c(0, 0.16))) +
      labs(title = "B. Bar chart", x = "Share of the popular vote (%)", y = NULL) +
      theme_arec() +
      theme(panel.grid.major.y = element_blank(),
            axis.text.y = element_text(size = 8))
  }
}

# --- annotation -----------------------------------------------------------
# One line, with a short note naming the thing the reader would otherwise have
# to ask about: the 2021 drought. The annotation is the only text on the plot
# beyond the axis labels, which is the point -- one note that answers the
# obvious question, not a commentary on every feature.
fig_annotated <- function(d, annotate = TRUE) {
  a <- by_crop_year(d)
  a <- a[a$Crop == "Spring wheat", ]
  p <- ggplot(a, aes(x = Year, y = Yield)) +
    geom_line(colour = prairie, linewidth = 0.8) +
    geom_point(colour = prairie, size = 1.8) +
    scale_x_continuous(breaks = sort(unique(a$Year)),
                       expand = expansion(mult = c(0.08, 0.08))) +
    scale_y_continuous(limits = c(30, 70)) +
    labs(x = NULL, y = "Yield (bu/ac)") +
    theme_arec()

  if (annotate) {
    y21 <- a$Yield[a$Year == 2021]
    p <- p +
      annotate("curve", x = 2021.72, xend = 2021.06, y = y21 + 8.5, yend = y21 + 1.6,
               curvature = 0.3, linewidth = 0.3, colour = muted,
               arrow = arrow(length = unit(0.055, "in"), type = "closed")) +
      annotate("text", x = 2021.80, y = y21 + 9.6, hjust = 0, vjust = 0.5,
               label = "2021: worst drought\nin over 30 years",
               colour = muted, size = 3, lineheight = 0.95)
  }
  p
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
    labs(title = "A. Cluttered", x = "Year", y = "Yield (bu/ac)") +
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
    labs(title = "B. Decluttered", x = NULL, y = "Yield (bu/ac)") +
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
    labs(title = "A. Patterned fills", x = NULL, y = "Yield (bu/ac)") +
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
    labs(title = "B. Flat fills", x = "Yield (bu/ac)", y = NULL) +
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
