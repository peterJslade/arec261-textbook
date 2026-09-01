# Cold-Beginner Review: Modules 2 & 3

**Reviewer lens:** a student who has never opened R, Positron, or any code editor; has never written a line of code; knows basic Excel from Module 1; may be an international student with English as a second language.

**Files reviewed:**
- `module02.qmd` — "Introduction to R and Positron"
- `module03.qmd` — "Transforming Data in R"

---

## Executive Summary

**Can a cold beginner get started and follow along?** *Mostly, until they try to read a file.* Module 2's conceptual scaffolding is genuinely good — the "objects and functions" primer and the "script vs. console" section are exactly what a novice needs, and they arrive in the right order. The tone is warm and non-intimidating throughout. A motivated beginner can probably get from "download R" to "run hello.R" with some flailing at the CRAN website.

**The single biggest barrier in Module 2:** the **working directory is never explained** — not defined, not named until it appears cold in Test Bank question 3. The text says "Put the CSV file in the same folder as your script" (line ~248), which is *not sufficient*: `read_csv()` looks in the working directory, not the script's folder, and in a fresh Positron session those are usually different. The very first `read_csv("canola_yields_2025.csv")` a student runs will, more often than not, fail with `Error: 'canola_yields_2025.csv' does not exist in current working directory ('/Users/...')` — and nothing in the chapter equips them to understand or fix that error. This is *the* classic day-one R failure, and the chapter walks students straight into it.

**The single biggest barrier in Module 3:** there is **no runnable on-ramp**. The whole module operates on a `yields` data frame that the student is told to assume exists ("All code in this section assumes you have loaded the tidyverse and have a data frame called `yields`…"), with the dataset marked `[TBD]`. A beginner cannot type along with a single example in the entire module. Compounding this, the module never explains that `yields |> filter(...)` **does not change `yields`** — pipelines sometimes get assigned (`yields_converted <-`) and sometimes just print, with no explanation of the difference. A beginner will filter, then wonder why their data is unchanged.

**Overall verdict:** Strong pedagogical bones, especially Module 2's primer sections. But there are two hard blockers (working directory; no Module 3 dataset/on-ramp), a handful of correctness errors (including a wrong `sd` value and a unit-conversion factor that contradicts the chapter's own arithmetic), and a layer of unexplained jargon (`n()`, `NA_real_`, `.groups`, `::`, `dense_rank`, "string", "argument") that will make a non-programmer feel the book has quietly stopped talking to them.

---

## "First Wall" Analysis

Walking through Module 2 exactly as a cold novice would:

1. **Wall #1 — the CRAN homepage (§ Installing R, line ~45).** The instruction is one sentence: "Download from <https://cran.r-project.org/>. Pick the version for your operating system and install it with the defaults." The CRAN homepage is famously hostile to beginners: a wall of text, mirror links, and (on Windows) a path of *Download R for Windows → base → Download R x.y.z for Windows* that nothing on the page makes obvious. Mac users face a choice between an **Apple silicon (arm64)** and **Intel (x86_64)** installer with no guidance. Realistic outcome: a chunk of the class downloads the wrong thing or gives up and emails the TA. **Fix:** step-by-step per-OS instructions (or a short screenshot walkthrough / video), including the arm64-vs-Intel decision and the Windows "base" click.

2. **Wall #2 — first launch of Positron (Setting Up, step 3).** "When prompted, select R as your interpreter." A novice does not know the word *interpreter*, may not be prompted at all (Positron often auto-selects), and on macOS may first hit the OS security dialog about apps downloaded from the internet. If no prompt appears, the student is stuck at "it never asked me." **Fix:** say what the prompt looks like, what to do if it doesn't appear (the interpreter selector in the top-right corner), and reassure them auto-detection usually just works.

3. **Wall #3 — `mean(1:10)` before any concepts (Setting Up, step 4).** This appears *before* the objects-and-functions primer and before the console is explained. Two problems: (a) `1:10` colon notation is never explained anywhere in either module; (b) the student is not told *where* to look for the result or what it should be (`[1] 5.5`). If nothing visibly happens (unsaved file, focus issues), they have no way to know whether it worked. **Fix:** show the expected output right there, and either explain `1:10` in one clause ("the numbers 1 through 10") or use `mean(c(1, 2, 3))`.

4. **Wall #4 — the `[1]` in the output (line ~131).** The very first console output shown is `[1] "Hello, world!"`. No beginner knows what `[1]` means, and the text never says. It's a small thing, but it's the first output they ever see and it contains an unexplained mystery token. One sentence fixes it.

5. **Wall #5 — `install.packages("tidyverse")` (§ Reading Data, line ~229).** The instruction is correct, but nobody warns the student that (a) this takes several minutes, (b) it prints a torrent of red/technical text that *looks like errors but isn't*, and (c) on some setups R asks "Do you want to install from sources the package which needs compilation?" (answer: no). A beginner watching red text scroll for three minutes will assume they broke something. Also: the classic failure mode — calling `library(tidyverse)` before ever installing, or `read_csv()` before `library()` — produces `there is no package called 'tidyverse'` / `could not find function "read_csv"`, and neither error is shown or explained.

6. **THE WALL — `read_csv("canola_yields_2025.csv")` (line ~241).** As described in the executive summary: the working directory is never defined, and the advice given ("same folder as your script") does not actually make the file findable. The worked example (§ Worked Example) then instructs students to create a folder, put a CSV and a script in it, and run — which fails in a default Positron session unless the student happened to open that *folder* (not just the file) in Positron. Nothing tells them to do that. This is where the largest number of students will be dead in the water, with an error message the chapter never showed them.

7. **Wall #7 — the worked example dataset is `[TBD]`.** Even a student who survives everything above cannot do the capstone exercise, because the dataset placeholder is unfilled ("The dataset is [TBD: canola yields CSV, Module 2 version]"). Same for Practice Exercise 3 and Module 3 Practice Exercise 4.

---

## Onboarding Gaps (most important section)

### 1. Working directory — undefined, and the guidance given is wrong-in-practice
- The term appears exactly once in Module 2, cold, in **Test Bank question 3**: "You have a file called `yields.csv` in your working directory." A student cannot answer a test question using a concept the chapter never taught.
- Line ~248: "Put the CSV file in the same folder as your script, or use an absolute path." Neither half is usable: same-folder only works if the working directory *is* that folder, and "absolute path" is undefined (and a beginner doesn't know how to find one — on Windows, Explorer hides it).
- **Needed:** a short section — *Where R looks for files* — that (a) defines the working directory, (b) shows `getwd()`, (c) gives the one habit that makes the problem disappear: **File → Open Folder in Positron, and always open your module folder, not just the file**, and (d) shows the exact `does not exist in current working directory` error and what it means. This is the highest-value addition possible to Module 2.

### 2. "Package" never actually defined
Line 28 mentions "thousands of packages" and line ~224 defines the tidyverse as "a collection of packages," but *package* itself is never defined (an add-on toolbox of extra functions someone wrote, which you install once and load each session). The install-once vs. `library()`-every-script distinction *is* stated — good — but the mental model underneath it isn't, and the two signature errors (`there is no package called…`, `could not find function…`) are never shown. Practice Exercise 5 tells students to break a script and read the error, but the chapter never displays a single error message to calibrate against.

### 3. Getting the CSV file onto their computer
These are Excel students. "Save the CSV file in it" (Worked Example step 2) hides real hazards: browsers that open CSVs instead of downloading; students who open the CSV in Excel "to look at it" and re-save it (changing formats); Windows hiding file extensions so `data.csv` displays as `data`. One short callout ("download, don't open; if you peek in Excel, don't save") would prevent a recurring class of support requests. CSV itself is used from the learning objectives on and never defined in this module — fine *if* Module 1 defined it; worth verifying.

### 4. No error literacy
Neither module shows what an R error actually looks like. The four errors a beginner is statistically guaranteed to hit in weeks 2–3: file not found (working directory), `could not find function` (forgot `library()`), `object 'South' not found` (forgot quotes), `unexpected ','` / `unexpected symbol` (typo). Module 3 line ~68 comes closest (explaining that unquoted `South` "would cause an error") but never shows the error. Given the book's own advice to paste errors into AI assistants, showing 3–4 canonical errors with translations would be cheap and high-value.

### 5. Positron's actual layout never described in sequence
The chapter names the console ("the pane below your script") and mentions the Environment pane once (line ~86, "Positron's *Environment* pane" — note Positron calls it **Variables**, not Environment; see Correctness). A novice staring at Positron for the first time sees four panes and a lot of chrome. A single annotated screenshot — editor here, console here, variables here, files here — would do more than paragraphs of prose. The book has no screenshots at all in these modules.

---

## Undefined Jargon

| Term | Where first used | Defined at first use? | Suggested fix |
|---|---|---|---|
| **working directory** | M2 Test Bank q3 | **No — never defined anywhere** | Add a "Where R looks for files" section (see above). Highest priority. |
| **absolute path** | M2 line ~248 | No | Define alongside working directory; show one example per OS. |
| interpreter | M2 line ~60 ("select R as your interpreter") | No | Reword: "select R as the language Positron should run." |
| IDE | M2 line ~48 ("data science IDE") | No | Spell out: "IDE (integrated development environment — an editor with the tools built in)." |
| package | M2 line 28 | Weakly (only via "tidyverse = collection of packages") | One-sentence definition before `install.packages()`. |
| argument | M2 line ~173 ("parentheses with arguments") | No | One sentence: "the inputs you hand a function, inside the parentheses"; also explain the `name = value` form before `na.rm = TRUE` appears. |
| string | M2 line ~152 ("all numbers, or all strings") | No | "text in quotes — R calls this a *string* or *character* value." |
| logical / boolean | M2 line ~157 (`TRUE, FALSE` vector) | No | Name the type when the example appears: "TRUE/FALSE values (R calls these *logical*)." |
| `1:10` | M2 line ~61 (setup step 4) | Never explained in either module | Gloss it or avoid it. |
| `[1]` in output | M2 line ~131 | No | One sentence: it's R numbering the first element of the answer. |
| `NA` / `na.rm` | M2 line ~283 | **Yes** — NA defined well; but `na.rm` never unpacked as "NA-remove" | Add "(`na.rm` = 'remove NAs first')." |
| pipe `|>` | M2 line ~302 | Yes, one sentence — but see Handoff: too thin to carry Module 3 | Re-introduce properly at the start of M3. |
| `n()` | M2 line ~311 (`n = n()`) and M3 summarise | **No — never explained in either module** | One line: "`n()` counts the rows in each group." |
| `desc()` | M2 line ~312 | No (inferable) | Gloss at first M3 use: "descending." |
| tibble | Never in text — but `read_csv` output the student sees says "A tibble" | No | One parenthetical: "R will call it a *tibble* — that's just the tidyverse's flavour of data frame." |
| `%in%` | M3 line ~65 | Yes (glossed) | Fine. |
| `NA_real_` | M3 line ~179 | No (comment only) | Prefer plain `NA` (works in `case_when` since dplyr 1.1) or explain the typed-NA quirk. |
| `dense_rank()` | M3 line ~276 | No | Gloss in the step-by-step breakdown, or restructure to avoid it (see Fix list). |
| `.groups = "drop"` | M3 line ~280 | No — and it silently supersedes the `ungroup()` advice given 100 lines earlier | Explain it's the pipeline-native version of `ungroup()`, or use `ungroup()` for consistency. |
| `::` (`janitor::clean_names()`) | M3 line ~304 | No | Gloss: "`package::function` means 'the function from that package.'" |
| regex, boilerplate, scaffolding | M2 AI section (~397–400) | No | Low stakes, but "regex patterns" means nothing to this audience; say "text-matching patterns." |
| declarative | M2 line ~317 | Half-glossed | Fine as is. |

---

## Ordering / Prerequisite Issues

1. **`mean(1:10)` (M2 setup, line ~61) precedes the objects-and-functions primer** and the console explanation. The primer itself lands very well — but the setup checklist jumps the gun. Either move the "try typing" step to just after the primer, or make it fully self-contained (expected output shown, `1:10` glossed).
2. **The primer and script-vs-console sections are good and correctly placed** — nothing else in Module 2's main flow is used truly cold before its explanation. The one exception: `read.csv("yields.csv")` appears in the primer (line ~83) as an illustration before CSVs/reading are covered; it's clearly labelled as a preview, so acceptable, but the base-R `read.csv` vs tidyverse `read_csv` split (already footnoted, good) is subtle for beginners — consider using `read_csv` in the primer too and keeping one function throughout.
3. **Named arguments (`na.rm = TRUE`) and multi-argument calls (`quantile(yields, 0.25)`) are used before "argument" or the `name = value` convention is ever explained.** For a non-programmer, `mean(yields$yield, na.rm = TRUE)` is three unexplained syntaxes in one line (`$` is explained; the comma-separated second argument and `=` inside a call are not).
4. **Bracket indexing (M2 lines ~217–219):** `fields[1, ]` / `fields[, "yield"]` are shown without stating the `[row, column]` convention or what the "empty slot" means. Either explain the convention in two sentences or cut brackets entirely — the course is tidyverse-first and `$` plus dplyr covers everything students need in Modules 2–3.
5. **`filter(year == 2025, acres > 100)` (M3, Combining It All)** uses the comma-as-AND shorthand, but the filter section earlier taught only `&`. One line when it first appears: "a comma between conditions means *and*."
6. **`group_by()` + `mutate()` (M3, Combining It All)** — the module teaches `group_by` only paired with `summarise`, then the capstone pipeline leans on grouped `mutate` plus `dense_rank`, a genuinely advanced pattern. The step-by-step breakdown helps, but this jumps two difficulty levels at once (see Fix list).
7. **`=` vs `<-` messaging is contradictory across modules.** M2 (line ~143): "You can write `=` instead of `<-`." M3 (line ~68): "one equals sign would be assignment." Both statements are individually defensible but together they teach a beginner that `=` sometimes assigns, sometimes matches arguments, and sometimes is a bug — with no map. Recommend M2 simply say "always use `<-` in this course" without opening the `=` door, and M3 rephrase (see Correctness #6).

---

## Correctness Issues

1. **Wrong `sd` value (M2, line ~178).** For `yields <- c(48, 52, 47, 55, 50)`, the comment says `sd(yields)` is "about 3.05". Actual value: **3.209** (variance 10.3). A student who checks — as the AI section explicitly tells them to verify claims — gets a different number from the book on one of the first functions they run. Fix the comment to `# about 3.21`.

2. **Canola conversion factor contradicts the chapter's own arithmetic (M3, lines ~158–168).** The derivation shown (22.68 kg/bu ÷ 0.4047 ha/ac ÷ 1000) correctly gives **≈ 0.0560** t/ha per bu/ac — the standard canola factor (50 lb bushel; Canadian Grain Commission: 1 t canola = 44.092 bu). The chapter then says "use 0.0628", which corresponds to a **56 lb bushel (corn)**, not canola. The "okay, I lied" passage will genuinely confuse students (and ESL readers may take "I lied" literally). Recommend: use **0.0560** everywhere (it also appears in `mutate` examples at M3 lines ~88, ~97, ~168, ~178, ~271 and would ideally match whatever the Module test bank uses), and rewrite the aside straightforwardly ("the factor depends on the assumed bushel weight; for canola, 50 lb/bu gives 0.056").

3. **`summary()` overclaim (M2, line ~264).** "…and the counts of every level of every categorical column." Not true for the workflow being taught: `read_csv()` reads text columns as *character*, and `summary()` on a character column shows only `Length / Class / Mode` — no counts. (Counts appear only for factors, which base `read.csv` no longer creates by default either, since R 4.0.) Students will run it, see no counts, and think they did something wrong. Fix: soften the claim, or show `table(yields$region)` / `count(yields, region)` as the way to get counts.

4. **"Same folder as your script" (M2, line ~248) is functionally incorrect** as advice for making `read_csv()` work — see Onboarding Gaps #1. As written it's the kind of statement that is true only under an unstated condition (working directory = script folder) that beginners won't meet.

5. **Run-whole-file output may not match the book (M2, lines ~128–134).** The text promises that clicking **Run** on the whole file prints all three results. If Positron's whole-file run executes via `source()` (as its "Source R file" command does), bare expressions like `2 + 2` and `mean(x)` are **not** auto-printed — only the `print()` line appears. Students would see one line of output instead of three and conclude the script is broken. **Verify in current Positron**; if whole-file Run is source-based, either tell students to run line-by-line with Cmd/Ctrl+Enter for this exercise, or wrap the expressions in `print()`, or add a note.

6. **"one equals sign would be assignment" (M3, line ~68).** Inside `filter()`, a single `=` is *argument naming*, not assignment — `filter(region = "South")` errors with dplyr's "Did you mean `region == "South"`?" hint. The practical advice (always use `==` for comparison) is right; the stated reason is wrong and collides with M2's `=`-as-assignment aside. Suggest: "`==` (two equals signs) tests equality; a single `=` means something different in R and will give you an error here — dplyr will even suggest the fix."

7. **Minor — "Environment pane" (M2, line ~86).** Positron's pane is labelled **Variables** (RStudio's is Environment). Small, but this chapter is the student's map to the interface; the label should match what they see.

8. **Cosmetic — `write_csv(my_summary, …)` (M2, line ~326)** uses an object (`my_summary`) that no prior code created. Use `region_summary` (which the later template does create) for continuity.

Not errors, but worth a note: `NA_real_` in `case_when` (M3 ~179) is no longer required — plain `NA` works in dplyr ≥ 1.1 and is far friendlier; and the claim that lubridate loads with `library(tidyverse)` (M3 ~226) is correctly hedged (true since tidyverse 2.0, 2023).

---

## Clarity / Accessibility Issues

- **Tone: genuinely good.** "Congratulations — you have run your first R script," "This is a lot. Don't panic," the honest "Why not Python/RStudio" asides — encouraging without being condescending. Keep this voice.
- **Idioms that will trip ESL readers** (each fine alone; collectively a tax): "caps out," "slows to a crawl," "binary blobs," "poke at numbers," "spiritual successor," "rock solid," "polyglot workflows," "a `?` away," "Don't get me started on leap seconds," "sneaky," "boilerplate," "scaffolding," and especially **"okay, I lied"** (M3) — the one place where an idiom carries actual technical content and actively misleads. Recommend rewording "okay, I lied" and "polyglot"/"binary blobs" at minimum.
- **No visuals at all.** For a chapter whose job is orienting someone inside an unfamiliar application, zero screenshots is a real accessibility gap — especially for students who process English slowly. Three screenshots (CRAN download page, Positron layout annotated, the console after hello.R) would transform the onboarding.
- **The M3 "Combining It All" pipeline (lines ~269–282)** is honest about being hard ("This is a lot") and the numbered breakdown is good, but it stacks four never-explained elements (comma-AND, grouped mutate, `dense_rank`, `.groups`) on a reader four sections into their first dplyr exposure. Consider splitting into two shorter pipelines (compute variety totals; then join/filter) or deferring the top-3 twist to a "stretch" callout.
- **M2's Worked Example withholds the script deliberately** ("I will not spell out every line…"). Sound pedagogy *if* the on-ramp were solid; given the working-directory gap and TBD dataset, it currently means the first fully independent task combines the two least-supported skills. Once the WD section exists, this is fine — maybe add "if `read_csv` says the file doesn't exist, re-read §Where R looks for files."

---

## Module 2 → Module 3 Handoff

- **The pipe is under-carried.** M2 introduces `|>` in one sentence inside an explicitly preview-labelled section; M3 lists "chain operations with the pipe" as a learning objective but never re-explains it — first use is bare (`yields |> filter(...)`, line ~51). A cold beginner needs the pipe re-taught at the top of M3: what it does, the "and then" reading, and ideally the piped-vs-nested comparison (`filter(yields, ...)` vs `yields |> filter(...)`) — M3 never shows that dplyr verbs take the data frame as their first argument, which is what makes the pipe make sense.
- **Pipelines don't modify the data — never stated.** M3 alternates between unassigned pipelines (which just print) and assigned ones (`yields_converted <- …`) without ever saying that `yields |> filter(...)` leaves `yields` untouched and that you must assign to keep a result. This is the #1 conceptual bug beginners carry out of a dplyr intro. One prominent callout early in M3 fixes it.
- **No dataset, no setup block.** M3 line ~44 says "assumes you have loaded the tidyverse and have a data frame called `yields`" — but never shows the two lines (`library(tidyverse)`; `yields <- read_csv("...")`) that would make the module followable, and the practice dataset is TBD. M3 should open with a copy-pasteable setup chunk and a real (even synthetic) CSV in `practice/data/`.
- **Things M3 uses that M2 never taught (and M3 doesn't teach either):** `n()`, comma-as-AND in `filter`, `.groups = "drop"`, `dense_rank()`, `::`, `NA_real_`, grouped `mutate`. Listed individually above.
- **What hands off well:** `na.rm = TRUE` (taught in M2, used consistently in M3), `NA` semantics (M2's intro, M3's deeper section — nicely layered), `$` access, the summarise/PivotTable analogy (M3 line ~139 connects back to Module 1 — excellent), and the tidy-data section's forward reference to `pivot_longer` in Module 5 (properly labelled as future material).

---

## Prioritized Fix List (worst first)

1. **Add a "Where R looks for files / working directory" section to Module 2** before §Reading Data: define working directory, show `getwd()`, teach *File → Open Folder* as the standing habit, show the file-not-found error verbatim, define "absolute path." Also fix the misleading "same folder as your script" line. *(Blocker — this is where most of the class will actually get stuck.)*
2. **Give Module 3 a runnable on-ramp:** an opening setup chunk (`library(tidyverse)` + `read_csv` of a named file) and fill the `[TBD]` datasets in both modules (M2 worked example & practice ex. 3; M3 practice ex. 4). *(Blocker — without this, M3 is read-only.)*
3. **State in Module 3, prominently and early, that pipelines don't change the input** — assign to keep results. Re-introduce the pipe properly (including that verbs take the data frame as first argument).
4. **Fix the correctness errors:** `sd` ≈ 3.21 not 3.05 (M2); conversion factor 0.0560 for canola, rewrite the "okay, I lied" passage (M3); soften the `summary()` categorical-counts claim (M2); correct the `=`/assignment rationale in M3 §filter; "Variables" not "Environment" pane; `write_csv(region_summary, …)`.
5. **Expand the install instructions** into per-OS steps (CRAN navigation, Mac arm64 vs Intel, Windows "base" link, macOS security prompt, what "interpreter" means / what to do if not prompted) — ideally with screenshots.
6. **Add an "errors you will see" mini-section** (file not found, `could not find function`, `object not found` from missing quotes, syntax error) with plain-English translations; warn that `install.packages` is slow and prints scary-but-normal red text.
7. **Verify the whole-file Run behavior in Positron** (M2 hello.R): if it sources without echo, adjust the text or the script so the promised output matches reality.
8. **Gloss the stragglers at first use:** `n()`, `[1]`, `1:10`, "argument"/named arguments, "string", "package", comma-AND in filter, `.groups = "drop"` (or use `ungroup()` consistently), `desc()`, `::`; replace `NA_real_` with `NA`.
9. **Tame the M3 capstone pipeline:** split it or move the `dense_rank` top-3 step into a labelled stretch goal; gloss grouped `mutate` when it appears.
10. **ESL pass:** reword "okay, I lied," "polyglot workflows," "binary blobs," "spiritual successor"; keep the encouraging tone everywhere else — it's one of the chapters' best features.
