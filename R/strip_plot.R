# Figures for Module 1: one-dimensional "strip plots" of farm yields.
# Used by the Spread and Visualizing sections. ggplot2-based so the source
# matches the tools taught in Module 4.

library(ggplot2)

prairie <- "#4a7c59"; ink <- "#24302a"; muted <- "#5c6b62"; wheat <- "#b7973f"

#' One-dimensional strip plot: every observation on a single line, drawn
#' semi-transparent so overlapping points darken where the data is dense.
strip_plot <- function(x, title, xlim = c(0, 65), mean_at = NULL,
                       highlight = NULL, highlight_label = NULL) {
  m  <- if (is.null(mean_at)) mean(x) else mean_at
  df <- data.frame(yield = x, kind = "obs")
  if (!is.null(highlight)) {
    df <- rbind(df, data.frame(yield = highlight, kind = "highlight"))
  }

  p <- ggplot(df, aes(x = yield, y = 0)) +
    geom_vline(xintercept = m, linetype = "dashed",
               colour = ink, alpha = 0.55, linewidth = 0.4) +
    annotate("text", x = m, y = 0.62,
             label = paste0("mean = ", format(round(m, 1), nsmall = 0)),
             colour = ink, size = 3.2) +
    geom_point(aes(colour = kind, alpha = kind), size = 5) +
    scale_colour_manual(values = c(obs = prairie, highlight = wheat)) +
    scale_alpha_manual(values = c(obs = 0.35, highlight = 0.85)) +
    scale_x_continuous(limits = xlim) +
    scale_y_continuous(limits = c(-0.35, 0.95)) +
    labs(title = title, x = "Yield (bu/ac)", y = NULL) +
    theme_minimal(base_size = 11) +
    theme(
      legend.position   = "none",
      panel.grid        = element_blank(),
      axis.text.y       = element_blank(),
      axis.ticks.y      = element_blank(),
      axis.line.x       = element_line(colour = "#cfe0d4"),
      axis.text.x       = element_text(colour = muted),
      axis.title.x      = element_text(colour = ink, margin = margin(t = 6)),
      plot.title        = element_text(colour = prairie, face = "bold",
                                       size = 11, hjust = 0,
                                       margin = margin(b = 10))
    )

  if (!is.null(highlight) && !is.null(highlight_label)) {
    p <- p +
      annotate("segment", x = highlight + 11, xend = highlight + 1.2,
               y = 0.42, yend = 0.08, colour = wheat, linewidth = 0.5,
               arrow = arrow(length = unit(0.06, "inches"))) +
      annotate("text", x = highlight + 12, y = 0.48, label = highlight_label,
               colour = wheat, size = 3.2, hjust = 0)
  }
  p
}

# --- the teaching datasets, built reproducibly from fixed seeds --------------
# Two sets of 30 yields with an identical mean but very different spread.
make_yields <- function(n = 30, sd, mean_target = 40, seed) {
  set.seed(seed)
  x <- rnorm(n, mean_target, sd)
  x <- round(x - (mean(x) - mean_target), 1)   # force the mean exactly
  round(x - (mean(x) - mean_target), 1)
}

yields_wide  <- make_yields(sd = 8.5, seed = 261)
yields_tight <- make_yields(sd = 2.5, seed = 262)

# Two sets of 60 yields sharing a mean and a range, but with different shapes.
make_shapes <- function(n = 60, lo = 26, hi = 54, mean_target = 40) {
  half     <- n / 2
  bimodal  <- c(seq(-1.2, -0.8, length.out = half),
                seq( 0.8,  1.2, length.out = half))
  unimodal <- qnorm((seq_len(n) - 0.5) / n)
  rescale  <- function(z) {
    z <- (z - min(z)) / (max(z) - min(z)) * (hi - lo) + lo
    round(z - (mean(z) - mean_target), 1)
  }
  list(bimodal = rescale(bimodal), unimodal = rescale(unimodal))
}
shapes <- make_shapes()
