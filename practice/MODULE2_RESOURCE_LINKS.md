# Module 2 — "Introduction to R and Positron": Other Resources (verified)

**Summary:** All 9 topics have at least one verified YouTube video URL (video URLs taken from live search results returning real `youtube.com/watch?v=...` links with confirmed titles/channels; one item is offered as a search term where no single beginner video was a clean fit). All free-book/doc URLs below were fetched and confirmed to resolve (no 404), with section titles verified: R for Data Science 2e (intro, ch. 7 Data import, ch. 3 Data transformation), Hands-On Programming with R (ch. 2 The Very Basics), Positron docs (home, Download), readr docs, dplyr docs, and the tidyverse style guide.

> Note on video links: YouTube video pages return only footer navigation when fetched directly, so titles/channels were verified through search-result metadata rather than page fetch. Every video URL below appeared verbatim in live search results with a matching title. Preview each once before publishing to be safe.

---

## 1. Why R? / R vs Excel / why learn R
- **Statistics with R, Ep 01: Why YOU should learn R!** — StatQuest with Josh Starmer — https://www.youtube.com/watch?v=mmwKdy15XTU  (short, upbeat motivational pitch for learning R; good first-day hook.)
- **Introduction — R for Data Science (2e)** — Wickham, Çetinkaya-Rundel & Grolemund — https://r4ds.hadley.nz/intro.html  (the book's welcome/intro: what data science is and the import→tidy→transform→visualize→model→communicate workflow.)

## 2. Installing R and Positron
- **Download Positron** — Posit (official docs) — https://positron.posit.co/download.html  (installers for Windows/macOS/Linux plus the "Optional language setup" step for installing R 4.2+.)
- **Positron (documentation home)** — Posit — https://positron.posit.co/  (overview + Guides/Features/Tutorials navigation for first-time setup.)
- **Getting Started with Positron: A Quick Tour** — YouTube — https://www.youtube.com/watch?v=mru9z50IOhI  (short guided tour of the Positron interface for new users.)

## 3. The R console / arithmetic and assignment (`<-`)
- **The R Console: Your First Steps in R** — YouTube — https://www.youtube.com/watch?v=64FgvzqlRD4  (running commands in the console, basic calculations, interacting with R directly.)
- **Getting started with R: Basic Arithmetic and Coding in R (R Tutorial 1.3)** — MarinStatsLectures — https://www.youtube.com/watch?v=UYclmg1_KLk  (using R as a calculator; classic beginner series.)
- **The Very Basics — Hands-On Programming with R** — Grolemund — https://rstudio-education.github.io/hopr/basics.html  (opens with R as a calculator, then objects and the `<-` assignment operator; ideal for absolute beginners.)

## 4. R scripts / writing and running scripts
- **Writing and Running code: Script vs Console (Getting Started with R & RStudio)** — YouTube — https://www.youtube.com/watch?v=2zXg0Pxapjs  (explains the difference between typing in the console vs saving/running code in a script.)
- **The Basics of Scripts in R** — YouTube — https://www.youtube.com/watch?v=NVglx_rthuM  (short intro to what an R script is and how to run it.)

## 5. R basics: vectors, data frames, functions
- **R programming for beginners: using functions and objects in R** — YouTube — https://www.youtube.com/watch?v=hvFBDmT4bdY  (applying functions to objects; beginner-friendly.)
- **Introduction to Vectors in R Programming and RStudio** — YouTube — https://www.youtube.com/watch?v=DUWnw8G4udM  (creating vectors, selecting/labelling elements, calculations with vectors.)
- **The Very Basics — Hands-On Programming with R** — Grolemund — https://rstudio-education.github.io/hopr/basics.html  (objects, vectors, and writing/using functions.)
- **R Objects — Hands-On Programming with R** — Grolemund — https://rstudio-education.github.io/hopr/r-objects.html  (atomic vectors, matrices, and data frames in depth.)
- **Data transformation — R for Data Science (2e)** — Wickham et al. — https://r4ds.hadley.nz/data-transform.html  (introduces tibbles/data frames as the core data structure you'll work with.)

## 6. Reading data from CSV (`read_csv`) and the working directory
- **Read and Load CSV Files into R and RStudio (Data Analysis in R for Beginners)** — YouTube — https://www.youtube.com/watch?v=B30wv33QzNY  (loading a CSV into R step by step for beginners.)
- **Data import — R for Data Science (2e)** — Wickham et al. — https://r4ds.hadley.nz/data-import.html  (ch. 7: reading rectangular files with `read_csv()`, column types, common import problems.)
- **readr (package documentation)** — tidyverse — https://readr.tidyverse.org/  (reference home for `read_csv()` and friends.)
- **Working Directory & Path Errors — "Mastering R Through Errors and Warnings"** — bookdown — https://bookdown.org/guokai8/mastering-r-through-errors/docs/working-directory-paths.html  (explains `getwd()`/`setwd()` and the "cannot open the connection / file does not exist" error beginners hit constantly.)

## 7. Summary statistics in R (mean, median, sd, summary)
- **R Basics 20: Descriptive Statistics using the summary function** — YouTube — https://www.youtube.com/watch?v=rPSKX6460gY  (short walkthrough of the `summary()` function.)
- **Gentle R #4: Basic Summary Statistics in R with RStudio** — YouTube — https://www.youtube.com/watch?v=8XFmPP93w_Y  (mean, median, sd, and the five/six-number summary.)

## 8. dplyr verbs and the pipe
- **Dplyr Essentials (easy data manipulation in R): select, mutate, filter, group_by, summarise & more** — Equitable Equations (Andrew Gard) — https://www.youtube.com/watch?v=Gvhkp-Yw65U  (single clear intro covering all the core verbs; strong beginner fit.)
- **Data transformation — R for Data Science (2e)** — Wickham et al. — https://r4ds.hadley.nz/data-transform.html  (ch. 3: `filter`, `select`, `mutate`, `summarize`, `group_by`, `arrange`, and the pipe.)
- **dplyr (package documentation) — A Grammar of Data Manipulation** — tidyverse — https://dplyr.tidyverse.org/  (reference home listing all the main verbs.)

## 9. Writing good/reproducible R scripts / R style
- **The tidyverse style guide** — Wickham (tidyverse) — https://style.tidyverse.org/  (the standard reference for naming, spacing, pipes, and readable R code.)
- **Keeping R Code DRY with Functions: Don't Repeat Yourself! (CC096)** — Riffomonas Project (Pat Schloss) — https://www.youtube.com/watch?v=XSRO4VKD-pc  (good-habits video on avoiding repetition; part of a reproducible-research series.)
