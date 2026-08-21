# console(): render R code as a clean listing plus a full console session.
#
# Usage in a module (the chunk itself shows nothing, so use echo: false):
#
#   ```{r}
#   #| eval: true
#   #| echo: false
#   console('
#   fields$yield
#   mean(fields$yield)
#   ')
#   ```
#
# The code is emitted twice: once as an ordinary ```r block students can copy,
# and once as a console session — each expression echoed at R's "> " prompt
# with its printed result underneath, the way it looks in Positron.
# console-fold.html collapses the session into a <details>.
#
# Why a function rather than a knitr hook? Quarto installs its own knit hooks
# after a document's setup chunk runs, so a custom `source`/`output` hook is
# silently discarded. A plain function call is just evaluation, which nothing
# overrides. It also lets R decide visibility (assignments print nothing,
# expressions do) — a distinction the HTML gives no way to recover afterwards.
#
# The code is evaluated ONCE, in the caller's environment, so objects carry
# over between chunks and side effects do not happen twice.

# echo = FALSE emits only the console transcript, without the copyable code
# listing above it — for when the code was already shown (e.g. a script
# listing) and repeating it would separate the output from the original.
console <- function(code, envir = parent.frame(), echo = TRUE) {
  lines <- strsplit(code, "\n", fixed = TRUE)[[1]]
  # Drop the blank first/last lines produced by writing console('
  # ...code... ') across multiple lines.
  while (length(lines) && !nzchar(trimws(lines[1]))) lines <- lines[-1]
  while (length(lines) && !nzchar(trimws(lines[length(lines)]))) lines <- lines[-length(lines)]

  transcript <- character(0)
  buf <- character(0)

  for (ln in lines) {
    buf <- c(buf, ln)
    expr <- tryCatch(parse(text = paste(buf, collapse = "\n")),
                     error = function(e) NULL)
    if (is.null(expr)) next          # incomplete expression — keep reading

    # Echo the author's own lines: "> " on the first, "+ " on continuations.
    transcript <- c(transcript, paste0("> ", buf[1]))
    if (length(buf) > 1) transcript <- c(transcript, paste0("+ ", buf[-1]))

    for (e in expr) {
      # Capture messages (e.g. read_csv's column note), warnings, and printing
      # done as a side effect during evaluation (e.g. glimpse(), which cat()s
      # to stdout and returns invisibly) into the transcript, the way a real
      # console interleaves them with results. Without the stdout capture,
      # side-effect printing leaks into knitr's chunk output and Quarto places
      # it before the code block, orphaned from the code that produced it.
      msgs <- character(0)
      res <- NULL
      side <- utils::capture.output(
        res <- tryCatch(
          withCallingHandlers(
            withVisible(eval(e, envir)),
            message = function(m) {
              msgs <<- c(msgs, strsplit(sub("\n$", "", conditionMessage(m)), "\n", fixed = TRUE)[[1]])
              invokeRestart("muffleMessage")
            },
            warning = function(w) {
              msgs <<- c(msgs, paste0("Warning: ", conditionMessage(w)))
              invokeRestart("muffleWarning")
            }
          ),
          error = function(err) list(err = conditionMessage(err)))
      )
      transcript <- c(transcript, side, msgs)
      if (!is.null(res$err)) {
        transcript <- c(transcript, paste0("Error: ", res$err))
      } else if (isTRUE(res$visible)) {
        transcript <- c(transcript, utils::capture.output(print(res$value)))
      }
    }
    buf <- character(0)
  }

  # Anything left never parsed; show it rather than dropping it silently.
  if (length(buf)) transcript <- c(transcript, paste0("> ", buf))

  code_block <- if (echo) {
    paste0("``` r\n", paste(lines, collapse = "\n"), "\n```\n\n")
  } else ""
  knitr::asis_output(paste0(
    code_block,
    "::: {.console-transcript}\n```\n",
    paste(transcript, collapse = "\n"),
    "\n```\n:::\n"
  ))
}
