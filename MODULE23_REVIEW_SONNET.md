# Module 2 & 3 Review — Cold-Beginner Lens

Reviewer persona: a student who has never opened R, RStudio, or Positron, never written a line of code in any language, is not a programmer, and knows only basic Excel from Module 1. Central question throughout: **would this student get started and follow along, or would they hit a wall?**

Files reviewed:
- `module02.qmd` — "Introduction to R and Positron"
- `module03.qmd` — "Transforming Data in R"

---

## Executive Summary

**Module 2: mostly yes, with real friction.** The prose is warm, well-paced, and the recently-added "Objects and Functions" and "Script vs Console" primers do their job — they land before the first script and genuinely help. But the installation section is too thin for a true cold start (no screenshots, no verification step, no troubleshooting), and several pieces of essential mechanical knowledge — what a **working directory** is, that a **package must be installed before `library()` will find it**, what an **error actually looks like** — are never explicitly taught even though the student is walked right up to the cliff edge of each one. The single biggest barrier: **the CSV-reading section (`read_csv("canola_yields_2025.csv")`) never explains where that file has to physically live relative to the script**, and "working directory" is never defined anywhere in the module. This is the single highest-probability first real error a beginner will hit, and the text gives them no tool to diagnose or fix it.

**Module 3: mostly yes, assuming Module 2 landed.** The six-verb walkthrough is genuinely well-built for beginners — short, one-idea-per-subsection, good use of "read it left to right." The pipe is reused (not re-taught, which is correct — Module 2 introduced it). The biggest barrier here is the **"Combining It All" pipeline** (@sec-dplyr-combining), which jumps from single-verb examples to an 8-step, 3-group_by pipeline with no intermediate scaffolding — a beginner who was following along will lose the thread here, particularly the `group_by() |> mutate()` (not `summarise()`) trick, which is conceptually the hardest idea in the whole module and gets one parenthetical sentence.

**Overall verdict: with an instructor or TA present in the room (which the course philosophy assumes — small-group instruction replaces lectures), this is workable.** As a pure read-alone document for a student with zero support, several of the gaps below (working directory, package-not-installed errors, quote/case-sensitivity errors) would strand a student for an hour with no path forward. None of these are hard to fix — they're additions, not rewrites.

---

## "First Wall" Analysis

Walking through Module 2 exactly as a cold beginner would experience it:

1. **§Installing R and Positron (~line 41–70).** Student downloads R from CRAN, "installs with the defaults" — fine, this generally works unattended on both Mac and Windows. Downloads Positron — fine. **First soft friction:** step 3 of "Setting Up Positron" says "When prompted, select R as your interpreter. Positron should auto-detect your R installation." A student who doesn't see a prompt, or sees multiple R versions listed, or is on a machine where auto-detection fails (common on Mac if R was installed somewhere non-standard, or if multiple R versions exist) has **no fallback instructions**. This is a plausible early stall, but recoverable via search/TA.

2. **§Setting Up Positron, step 4 (line 61): "try typing `mean(1:10)`. Run it with Cmd+Enter."** This is presented as the very first hands-on action — but at this point in the document the student has **not yet been told what a function is, what an argument is, or what `1:10` means** (the colon-range shorthand is never explained anywhere in either module). It "just works" if they type it verbatim and see `[1] 5.5`, but if anything goes even slightly wrong (typo, wrong pane focus, R not yet finished initializing), they have zero conceptual grounding to debug it. This is the **first real wall**: an unexplained smoke-test dropped before the mental model (which arrives promptly afterward at §The Big Idea, line 74) has been given. It's low-risk because it's optional/quick, but it is code used before any concept is explained.

3. **§Your First R Script → §Writing and Running the Script (line 113 onward).** This is where the real first wall sits. The instructions say "create a new file called `hello.R`... and paste the following," then "Save the file, then run it." Nothing in the module tells the student:
   - **Where** to save `hello.R` — what folder, and why it matters. (This matters immediately afterward when CSVs enter the picture.)
   - That Positron will ask them to choose a save location and they need to remember/note it.
   - What "run the whole file" actually looks like the first time — is there a confirmation dialog, does a new pane open, is there a delay.

   Most students will get through this fine since there's no external file dependency yet — but the **habit of not thinking about file location** is being formed right here, which sets up the bigger wall in §Reading Data from CSV.

4. **§Reading Data from CSV (line 222–264) — the real first wall.** The line `yields <- read_csv("canola_yields_2025.csv")` is presented with the one-line tip "Put the CSV file in the same folder as your script, or use an absolute path." This is the *only* sentence in either module that touches on working directory / file location, and it:
   - Never defines "working directory" as a term (it appears unglossed in the Test Bank at line 440: "You have a file called `yields.csv` in your working directory" — a term the module never actually introduces or explains).
   - Never explains **how** to verify where the script is saved, how to check Positron's current working directory, or what `getwd()` / `setwd()` do (not mentioned at all) or how project-relative paths work.
   - Never shows what the error looks like when this goes wrong. A student who saves `hello.R` on the Desktop and the CSV in Downloads will get `Error: 'canola_yields_2025.csv' does not exist in current working directory (...)`, a message a first-time programmer cannot parse (what's a "current working directory"? what does "does not exist in" mean when the file obviously exists somewhere?).

   This is the highest-probability, highest-severity wall in the module, and it is essentially unaddressed. Given the Worked Example (§sec-module2-example) explicitly has the student "Create a new folder... Save the CSV file in it... Create a new file... in the same folder" — the *procedure* is right, but the *why* and the *recovery-if-wrong* are both missing.

5. **§Reading Data from CSV, package install (line 226–236).** `install.packages("tidyverse")` and `library(tidyverse)` are presented back to back with "you only need to do this once per computer" — good, that's the right instruction. But **the distinction between install (once) and library (every session) is stated, not explained**, and the module never shows what happens if a student calls `library(tidyverse)` without having installed it first (`Error in library(tidyverse) : there is no package called 'tidyverse'`). This is an extremely common beginner error — they'll re-open Positron a week later, run their script, and hit this because they don't understand *why* `library()` is needed every time when `install.packages()` isn't. Not fatal, but a very likely second wall, immediately following the first.

**Summary of the walk-through:** the path from "open Positron for the first time" to "successfully read a CSV and get summary stats" has two real structural walls (working directory; install-vs-library confusion) and one soft one (the ungrounded `mean(1:10)` smoke test). Everything else in Module 2 is paced appropriately for a beginner.

---

## Onboarding Gaps (install / setup / working directory / packages)

This is the most important section, per the assignment brief.

1. **No verification step after installation.** After "install R" and "install Positron," there's no "here's how to confirm it worked" — e.g., open the console, type `R.version.string`, or confirm Positron shows a green "R" in the bottom bar. A student whose install silently failed (permissions issue, antivirus blocking, wrong architecture on Mac ARM vs Intel) won't find out until much later and won't know why things aren't working.

2. **"Working directory" is never defined, but is used as if known.** It appears in the Test Bank (line 440) unglossed, and is the crux of the CSV-reading section without ever being named or explained there. This is the single most important missing concept in the module. A beginner needs, at minimum: what it is, how to check it in Positron (e.g., via the Console tab / Files pane, or `getwd()`), and that saving the script and the data file in the same new folder sidesteps the whole problem (which the Worked Example does implicitly but doesn't explain *why* that step matters).

3. **No explanation that a package must be installed before `library()` works.** Both commands are shown correctly and in the right order, but the causal relationship — and what happens if you get it backwards or skip install — is not spelled out. See wall #5 above.

4. **No screenshots or visual anchors anywhere.** For a true cold beginner, "select R as your interpreter" or "click the Run button in the top right" are text descriptions of a GUI the student has never seen. Given the book format (Quarto/Markdown), even one or two annotated screenshots of the Positron layout (script pane, console, Environment pane, Run button) would remove a lot of anxiety. The text acknowledges Positron changes fast ("If something in the screenshots or menus... doesn't match"), suggesting screenshots were originally planned but aren't present in this draft — worth confirming.

5. **No troubleshooting / "if this doesn't work" pathway anywhere in Module 2.** Given the audience, at least a short "common installation problems" callout (Mac Gatekeeper blocking the installer, Windows needing admin rights, R and Positron versions mismatching) would catch a meaningful fraction of students before they need a TA.

6. **File location / project folder concept is implicit, never explicit.** The Worked Example (line 420–434) has the right procedure (make a folder, put the CSV and script in it) but this is presented as exercise instructions, not taught as a concept earlier where it's needed (§Reading Data from CSV). A student doing the CSV section for the first time, before reaching the Worked Example, has no reason to know this discipline matters.

7. **GitHub Copilot install (line 62) is "optional" and mentioned in passing** — "This requires a free student account" with no link to the GitHub Student Developer Pack or explanation of how a student would get one. Minor, since it's explicitly optional, but a curious student could stall here looking for the sign-up path.

---

## Undefined Jargon

| Term | Where first used | Defined at first use? | Suggested fix |
|---|---|---|---|
| function | Learning Objectives line 12 ("Use AI tools... to help write R code"); real use starts line 88 | Yes, defined well at §The Big Idea (line 88) — good | None needed; ordering is correct |
| argument | line 91 comment "run the 'mean' function on the object" implies it; explicit at line 173 "writing its name followed by parentheses with arguments" | Defined, but late relative to first implicit use (line 91: `mean(yield_farm)`) | Minor: could gloss "argument" briefly in the §Big Idea function bullet |
| object | line 78, §The Big Idea | Yes, defined clearly and immediately | None needed |
| assignment / `<-` | line 78 | Yes, defined immediately, with the "let the name on the left be the thing on the right" framing — good | None needed |
| vector | line 82 (used in code comment), formally defined line 152 | Comment-level use precedes formal definition by ~70 lines, but the comment itself glosses it ("a vector: several numbers") so it's soft-introduced, not cold | Acceptable as is |
| data frame | line 83 (comment), formally defined line 193 | Same pattern as vector — soft-introduced via comment first | Acceptable as is |
| string | Used implicitly via `"Hello, world!"` (line 122) and `varieties <- c("InVigor", ...)` (line 156); never explicitly named/defined as a term anywhere in Module 2 | **No** | Add one sentence defining "string" (text in quotes) at first use, e.g. in the vectors section where `varieties` (all strings) appears |
| boolean / logical | `is_irrigated <- c(TRUE, FALSE, ...)` line 157; also `is.na()` returns "a logical vector" line 201 (Module 3) | Named "logical" at line 201 (M3) but `TRUE`/`FALSE` in M2 line 157 are never labeled as a type at all | Add a one-line gloss in M2 §Vectors: "TRUE/FALSE values are called logicals or booleans" |
| package / library | `install.packages("tidyverse")` line 229; `library(tidyverse)` line 235 | Described functionally ("a collection of packages...that has become the standard") but the word "package" itself and the distinction from "library" (confusingly, the function is `library()` but the *thing* is a *package*) is not disambiguated | Add a short clarifying note: "Confusingly, R calls the *thing* you install a 'package' but the *command* you run to load it `library()`. Both refer to the same thing here." |
| console vs script | Explicitly and well covered, line 102–111 | Yes — this is one of the best-explained concepts in the module | None needed |
| pipe (`|>`) | First appears line 302, defined immediately in the same paragraph | Yes, defined at first use, with a worked example and plain-English reading immediately after | None needed |
| tidyverse | line 224, "a collection of packages for data manipulation that has become the standard" | Yes, adequately defined | None needed |
| CSV | line 205, 222 — used freely, assumed known | **Not explicitly defined**, though it's a fairly safe assumption post-Excel (Module 1) that students have seen `.csv` before | Low priority — one clause ("a CSV — a plain-text spreadsheet file, Comma-Separated Values") would fully close the gap for ESL/international students who may know the concept but not the acronym |
| path (file path) / working directory | "absolute path" line 248; "working directory" Test Bank line 440 | **No** — neither term is ever defined | High priority — see Onboarding Gaps #2 above |
| `NA` | line 283, Module 2; expanded properly in Module 3 §Handling Missing Values | Reasonably defined at first substantive use (line 283: "missing values (coded as NA in R)") | None needed, though Module 3's treatment is more thorough and could be forward-referenced from M2 |
| comment (`#`) | line 118 (in code) and named explicitly line 140 ("Comments start with #") | Yes | None needed |
| `1:10` (colon/range shorthand) | line 61, in the very first hands-on instruction | **No** — never explained anywhere in either module | Add a one-clause gloss where first used, or replace with something already-understood like `c(1,2,3)` to avoid introducing unexplained syntax in the very first interactive moment |
| environment (R environment / Environment pane) | "Environment pane" line 86; "R environment (all the objects in memory)" line 335 | Loosely defined via context both times; acceptable but a formal one-liner would help | Low priority |
| interpreter | "select R as your interpreter" line 60 | **No** — used in setup instructions with no explanation of what an interpreter is | Low-medium priority; a beginner can usually get through the wizard without understanding the word, but it's jargon dropped cold in the very first setup step |
| `%in%` operator | Module 3, line 65 | Introduced with a working example and the gloss "a shortcut for 'in this set of values'" | Yes, adequately defined |
| `case_when` | Module 3, line 176 | Yes, well explained with the "R analogue of nested IFs" framing, defined right after first use | None needed |
| `ungroup()` | Module 3, line 147 | Yes, explained ("otherwise the grouping persists and can surprise you later") | None needed |
| `.groups = "drop"` argument | Module 3, line 280, used in the big combining pipeline | **No** — appears once, unexplained, in the hardest example in the module | Add a short gloss; see Correctness/Clarity notes below |
| `dense_rank()` | Module 3, line 276 | **No** — used with zero explanation in the combining example | Should be defined or avoided; see below |

---

## Ordering / Prerequisite Issues

1. **`mean(1:10)` (M2, line 61) precedes any explanation of functions, arguments, or the colon shorthand.** This is code used cold, before the "Big Idea" primer that immediately follows it. Low-stakes (it's a single smoke-test line) but technically the one clear violation of "nothing is used before it's explained" in Module 2's early flow. Recommend either moving this step to after §The Big Idea, or swapping it for something that doesn't require unexplained syntax (e.g., have them type `2 + 2` here instead, and save `mean()` for its proper introduction).

2. **Module 3's running-example columns are inconsistent, which reads as material used before it's defined.** §The Six Core Verbs (line 44) establishes the dataset has columns `field_id`, `region`, `variety`, `acres`, `yield_bu_acre`. Everything through §Handling Missing Values correctly uses `yield_bu_acre`. Then §Unit Conversion's `case_when` example (line 174–182) suddenly references a column called plain `yield` (not `yield_bu_acre`) and a `units` column that was never mentioned in the schema at line 44. A beginner following along literally will wonder where `units` came from and why the column is suddenly named differently. This isn't a made-up dataset problem in principle (real data is messy) but as *written continuity* within one running example, it's a discontinuity that will confuse, not illuminate. **Fix:** either add a sentence noting "imagine a different, messier version of the dataset that also has a `units` column," or rename consistently.

3. **`dense_rank()` and `.groups = "drop"` in the "Combining It All" pipeline (M3, line 264–293) are used with zero prior introduction anywhere in either module.** This is the clearest prerequisite violation in Module 3. The surrounding prose ("Don't panic... notice how each step does one thing") acknowledges the pipeline is dense, and the six-step breakdown helps, but it glosses over exactly the two unfamiliar functions a beginner would stumble on. `dense_rank(desc(variety_total)) <= 3` in particular requires understanding ranking-with-ties semantics that were never taught. **Fix:** add one clause each — "`dense_rank()` ranks values, giving ties the same rank" and "`.groups = \"drop\"` here is a tidier way to ungroup automatically after summarising, avoiding the extra `ungroup()` step you saw above."

4. **The `group_by() |> mutate()` pattern (M3, line 273–274, `mutate(variety_total = sum(total_tonnes, na.rm = TRUE))` after grouping) is arguably the single hardest concept in Module 3** — that `mutate` after `group_by` keeps all rows but computes the aggregate per group, as opposed to `summarise` which collapses rows — and it gets exactly one parenthetical sentence: "(`group_by` + `mutate` instead of `summarise` keeps all the rows but adds a column.)" Given that `group_by`+`summarise` was carefully built up over several prior subsections with worked examples, this variant deserves its own short example before being deployed inside the hardest pipeline in the module.

5. **Module 2's `dplyr` preview (§sec-dplyr-verbs, line 291–319) uses `filter`, `group_by`, `summarise`, `arrange`, and the pipe in a full worked pipeline — all before Module 3 formally teaches any of them.** This is explicitly flagged in the text as intentional ("You will meet them properly in Module 3, but I want to give you a taste now") and is followed by a plain-English translation of the pipeline. This is a reasonable pedagogical choice (preview → deep dive), not a genuine ordering bug, but it's worth the authors double-checking that students are told clearly enough not to worry about full mastery here. The text does this adequately ("For now, just recognize that this is where we are heading") — no fix needed, just noting it's intentional and works.

---

## Correctness Issues

1. **Real numerical error: the canola bu/ac → t/ha conversion factor is self-contradicting.** M3, line 158–169:

   > $$\text{yield (t/ha)} = \text{yield (bu/ac)} \times 0.0628$$
   > (This factor comes from: 1 bushel of canola ≈ 22.68 kg, and 1 acre ≈ 0.4047 ha, so 1 bu/ac ≈ 22.68/0.4047/1000 ≈ 0.056 t/ha... okay, I lied; the exact conversion depends on the bushel weight you use. For this class use 0.0628.)

   I verified the arithmetic: 22.68 / 0.4047 / 1000 = **0.05604**, not 0.0628. The text's own worked math produces ~0.056, then instructs students to use 0.0628 instead — a ~12% discrepancy — with a jokey "okay, I lied" that doesn't actually explain where 0.0628 comes from. This is presented as a worked example of "look it up carefully and cite your source," which makes the internal inconsistency worse, not better — it's modeling exactly the sloppiness it warns against. **Fix:** either correct the shown arithmetic to actually produce 0.0628 (find the bushel-weight assumption that yields that number, e.g. a heavier bushel-weight standard) or change the instructed factor to match the shown math (~0.0560), and drop the "I lied" aside once the numbers agree. As written, this is the kind of thing a sharp student *will* catch and lose confidence in the material over.

2. **Minor/cosmetic: `read.csv` vs `read_csv` row-printing claim needs a caveat.** M2 line 255: `yields  # prints the data frame (first 10 rows)`. This is correct **only** for a tibble (i.e., only if `yields` was read with `read_csv`, the tidyverse function, which is what the surrounding code does). I confirmed base R's `read.csv` + auto-print instead prints **all rows** with no truncation and no column-type header. Since Module 2 does consistently use `read_csv` by this point, the claim is technically accurate in context — but earlier in the same module (line 83, 86) `read.csv` (base R) is shown first before the text says "later we switch to the tidyverse's `read_csv`." A student who is still using base `read.csv` out of habit and then reads "(first 10 rows)" later could be confused when they get all rows printed instead. **Fix:** add a one-clause note tying the "first 10 rows" behavior specifically to tibbles/`read_csv`, not data frames in general.

3. **Verified correct: the `hello.R` walkthrough output.** I ran the exact script from line 117–126 (`print("Hello, world!")`, `2 + 2`, `x <- c(1,2,3,4,5)`, `mean(x)`) through `Rscript` and confirmed the console output shown in the text (`[1] "Hello, world!"`, `[1] 4`, `[1] 3`) is exactly correct.

4. **Verified correct: `library(tidyverse)` auto-loads `lubridate`.** M3 line 226 claims lubridate "is loaded automatically with `library(tidyverse)` in recent versions." I confirmed this is true in a current tidyverse install (lubridate appears on the search path after `library(tidyverse)`). Accurate as written, and the hedge ("in recent versions... if not, load it explicitly") is appropriately cautious.

5. **Verified correct: `%in%`, `dense_rank()`, `replace_na()`, `case_when()` syntax** all run without error and produce the described behavior when tested.

6. **Verified correct: vector arithmetic example** (`a + b` line 163–167) produces exactly `[1] 11 22 33` as shown.

7. **No other function-name or syntax errors found.** `filter`, `select`, `mutate`, `arrange`, `summarise`, `group_by`, `ungroup`, `drop_na`, `is.na`, `rename`, `janitor::clean_names()`, `ymd/dmy/mdy`, `year/month/day/wday`, `ggsave`, `write_csv`, `save.image` are all used with correct names and plausible/correct argument shapes throughout.

8. **Small accuracy note on Excel row-limit claim** (M2, line 21): "Excel caps out at a bit over a million rows per sheet" — this is correct (1,048,576 rows in current Excel), no issue.

---

## Clarity / Accessibility Issues

1. **Tone is genuinely good for an intimidated beginner.** First-person asides ("Honest answer..."), the "Congratulations — you have run your first R script" moment, "Don't panic" before the hard pipeline, and the explicit reassurance in §A Word on AI Coding Assistants all read as encouraging rather than gatekeeping. This is a real strength to preserve.

2. **"I lied" (M3, line 164)** is a colloquial idiom that could read as confusing or oddly self-deprecating to an ESL reader — it's not literally a lie, it's an approximation. Low priority (context makes intent recoverable) but combined with the actual arithmetic error above (#1 in Correctness), this passage is the weakest spot in either module and worth a rewrite regardless of audience.

3. **"Don't get me started on leap seconds" (M3, line 224)** is an idiom ("don't get me started" = "I could go on about this at length") that a non-native English speaker may not parse. Low priority, but worth flagging since the persona explicitly includes international/ESL students.

4. **"the future of both" / "spiritual successor" (M2, line 48, 68)** — figurative language describing Positron. Understandable in context but adds a small parsing burden right at the point where the student is trying to figure out what software to install. Not a blocker.

5. **The "golden rule" framing (M2, line 111: "write your code in the script, not the console")** is excellent, concrete, memorable pedagogy — worth calling out as something that works well.

6. **Test Bank Q3 (M2, line 440) uses "working directory" without ever having taught the term** — this is the clearest case of a test question relying on a concept the chapter itself never explains. See Onboarding Gaps #2. This should be fixed regardless of whether the broader onboarding fix is made, since it's currently untestable material.

7. **"Real-world datasets often have terrible column names: `Yield (bu/ac)`, `REGION_NAME`, `X1`" (M3, line 297)** — `X1` as an example of a terrible column name is accurate (it's R's auto-generated placeholder for an unnamed column) but a beginner has no way to know that's what `X1` signifies; a half-clause ("R's auto-generated name for a column with no header") would help.

---

## Module 2 → Module 3 Handoff

Overall the handoff is good — Module 3 does not spring anything genuinely new-and-unexplained on the reader *except* where noted above. Specifics:

- **Pipe operator (`|>`):** Properly introduced in M2 (line 302, with definition and worked example) and correctly *reused without re-explanation* in M3. This is exactly right — M3 doesn't waste time re-teaching it, and doesn't assume more than M2 gave it.
- **`library(tidyverse)` / package loading:** M3 line 44 says "All code in this section assumes you have loaded the tidyverse" — reasonable, since M2 taught this. Not re-explained, correctly assumed as prior knowledge.
- **The six verbs themselves:** M2's §dplyr preview (line 291–301) lists all six verbs by name with one-line descriptions before M3 does the deep dive. This scaffolding works well — a student hitting M3 has seen the names before, even if not the mechanics.
- **Gap: M3 assumes a specific dataset schema (`field_id`, `region`, `variety`, `acres`, `yield_bu_acre`, line 44) that does not match the dataset used in M2's worked examples** (M2 uses `field_id`, `region`, `yield` — no `variety`, `acres`, or unit-suffixed column name; M2's dplyr preview uses `acres` and `region` and `yield`, without `yield_bu_acre`). This isn't fatal since both are presented as illustrative/hypothetical, but a careful student moving from M2 to M3 may notice the column names don't line up and wonder if they missed something. **Fix:** either use one consistent synthetic schema across both modules, or add a line in M3 noting explicitly "this is a new example dataset, not the same as Module 2's."
- **Gap: `NA` / missing values.** M2 introduces `NA` briefly and correctly (line 283–289) in the context of `na.rm = TRUE`. M3's §Handling Missing Values (line 186–220) builds on this well and doesn't repeat unnecessarily, while adding real depth (missingness mechanisms, `drop_na()`, `replace_na()`). This handoff works well.
- **Gap: dates are entirely new material in M3** with no M2 groundwork — that's fine, since M2 never claims to cover dates and the Learning Objectives correctly scope it to M3.
- **No handoff problem with `install.packages` vs `library`:** M3 doesn't re-teach this, correctly assuming M2 covered it — though see Correctness/Onboarding notes above about whether M2's coverage is sufficient in the first place.

---

## Prioritized Fix List

**Must fix (real blockers or errors):**

1. **Fix the bu/ac → t/ha conversion arithmetic (M3, line 158–169).** The shown math (0.056) doesn't match the instructed factor (0.0628). Reconcile the numbers; drop the "okay, I lied" aside once fixed. This is the one outright factual/internal-consistency error in either module.
2. **Define "working directory" explicitly, and add it to §Reading Data from CSV (M2, ~line 246–250).** Explain what it is, how to check/set it in Positron, and why "put the CSV in the same folder as your script" solves the problem. Show what the actual error message looks like when this goes wrong, so students can recognize and self-diagnose it. This is the highest-probability real-world stall point in the entire two-module sequence.
3. **Fix the M3 running-example column inconsistency** (`yield_bu_acre` vs. plain `yield` + unexplained `units` column in the `case_when` example, line 174–182). Either rename consistently or add one sentence flagging the schema change.
4. **Add explanation for `dense_rank()` and `.groups = "drop"`** before/within the "Combining It All" pipeline (M3, line 264–293), or replace them with already-taught alternatives (e.g., `arrange()` + `slice_head()`/`top_n()`-style approach, and an explicit `ungroup()` instead of `.groups = "drop"`) to avoid introducing new vocabulary in the hardest example of the module.

**Should fix (meaningfully reduces friction):**

5. **Explain the install-once-vs-load-every-session distinction for packages more explicitly** (M2, line 226–236), including what the "package not installed" error looks like.
6. **Give `group_by() |> mutate()` its own small worked example** before deploying it inside the big combining pipeline (M3, line 273–274) — it's the conceptually hardest single idea in Module 3 and currently gets one parenthetical.
7. **Define "string" and "boolean/logical" explicitly at first use** (M2, §Vectors, line 152–158) — both are used constantly afterward without ever being named as concepts.
8. **Reconcile M2 and M3's illustrative dataset schemas** (different column names for what's implied to be similar canola-yield data) or add a note that they're independent examples.
9. **Add a short "if installation doesn't work" / troubleshooting note** to M2's install section, and a "how to confirm it worked" verification step.

**Nice to have (polish):**

10. Move or replace the `mean(1:10)` smoke test (M2, line 61) so it doesn't rely on an unexplained function call and unexplained `1:10` shorthand before the "Big Idea" primer.
11. Gloss "CSV," "interpreter," and "path" briefly at first use for ESL accessibility.
12. Consider one or two annotated screenshots of the Positron interface (script pane, console, Run button, Environment pane) — described entirely in prose right now.
13. Soften idioms that may not land for ESL readers ("I lied," "don't get me started," "spiritual successor") — low priority, but consistent with the course's international-student audience.
14. Clarify that the "(first 10 rows)" tibble-printing behavior (M2, line 255) is specific to `read_csv`/tibbles, not `data.frame`/`read.csv`, given both are shown earlier in the module.
