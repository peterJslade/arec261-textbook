# Feedback on Chapters 4--6 of *Agricultural Data Analytics*

## Overall assessment

These three chapters work well as a transition from Excel into R. The
sequence is sensible:

1.  **Chapter 4:** what R is and the basic mechanics;
2.  **Chapter 5:** how to organize and bring real data into R;
3.  **Chapter 6:** how to actually manipulate data.

The strongest feature is that the chapters are not trying to turn
students into programmers before letting them do useful work. The
agricultural examples are concrete, the prose is generally direct, and
there is a strong emphasis on reproducibility and good habits from the
beginning.

My main concern is **cognitive load, especially in Chapter 5**. For an
introductory applied-data audience, Chapters 4 and 6 have fairly clear
narratives, while Chapter 5 currently contains several different ideas
that are individually worthwhile but collectively make it feel like the
densest of the three. I would simplify some material rather than add
much more.

------------------------------------------------------------------------

# Chapter 4 --- Getting Started with R

## What works especially well

### 1. The opening motivation is strong

The contrast with Excel is exactly the right way to introduce R after
students have just learned Excel. The categories --- reproducibility,
scale, composability, and advanced statistics --- give students concrete
reasons for tolerating the initial inconvenience of programming.

I especially like the point that AI makes programming knowledge *more*
useful rather than obsolete because somebody still needs to formulate
the problem and evaluate the output. That is a good framing for the
course.

### 2. Console → objects → scripts is a good progression

Starting with R as a calculator makes the console unintimidating, and
the transition from a calculator that forgets its answer to objects that
preserve values is intuitive.

The explanation of `[1]` is also exactly the kind of tiny detail that
prevents beginners from wondering whether they have done something
wrong.

### 3. The treatment of scripts is excellent

The sentence describing a script as the "permanent recipe for your
analysis" is particularly effective. The before/after Positron
screenshots should help students understand a distinction that is
surprisingly difficult for beginners: **writing code is not the same as
executing code**.

The early insistence that substantive work belongs in a script rather
than the console is also a very good habit to establish.

### 4. The vectors/data-frame discussion is pitched at about the right level

I like that you introduce only vectors and data frames rather than
giving students the traditional tour of vectors, matrices, arrays,
lists, factors, etc. Most of that would be noise at this stage.

The progression

`vector → vectorized arithmetic → data frame → column as vector → functions`

is coherent and sets up `dplyr` nicely.

## Things I would change

### 1. Reconsider the explanation of `<-` versus `=`

The current statement says that `=` can be used for assignment but that
it is good practice to reserve it for other operations. I would make the
explanation slightly more precise because Chapter 6 later says that `=`
is used for assigning values and naming arguments.

Something like:

> R allows both `<-` and `=` for assignment in many contexts. In this
> book we will use `<-` for assignment because it makes assignment
> visually distinct from `=` inside function calls and `==` for
> comparisons.

That gives students a convention without implying that `=` is inherently
bad R.

### 2. The object/type paragraph could still confuse beginners

The distinction is technically fine, but the sentence about "components
of an object" having different types may invite students to think that a
data frame itself has a simple type in the same sense that a vector
does.

I would simplify:

> Every value in R has a type. A vector contains values of one type,
> while a data frame can contain several columns of different types.

That is probably all they need here.

### 3. Square-bracket indexing may be expendable

The section showing

`fields[1, ]`, `fields[, 1]`, and `fields[2, 3]`

is correct, but I am not sure it earns its cognitive cost at this point.
Chapter 6 immediately teaches `filter()` and `select()`, which are the
operations you actually want students using.

I would consider either:

-   removing bracket indexing entirely; or
-   putting it in a short "Useful to recognize" note rather than the
    main conceptual path.

For this audience, `$` is useful immediately; `[row, column]` is much
less important.

### 4. The chapter could end with one tiny "you can now do data analysis" payoff

The final script-writing section is good, but the chapter finishes
primarily on coding discipline. A tiny final example combining a data
frame and a meaningful agricultural question could give students more of
a sense of accomplishment.

For example: create five fields, calculate production for each, then
calculate total production. You already essentially do this in the
script template, so this may simply require framing it as the
culmination of the chapter.

## Bottom line on Chapter 4

This is the strongest of the three chapters structurally. I would mostly
**trim technical side paths rather than add material**. The goal should
be for a student to leave thinking:

> "R stores things as objects; data usually lives in data frames;
> functions do things to those objects; and I should save my work in a
> script."

If they understand that, Chapter 4 has succeeded.

------------------------------------------------------------------------

# Chapter 5 --- Working with Data in R

## What works especially well

### 1. Starting with project organization is a very good choice

This is unusual in introductory material, but I think it is exactly
right. Students otherwise develop terrible path and file-management
habits and then have to unlearn them.

The three principles are memorable:

-   project is self-contained;
-   raw data is never edited;
-   outputs are disposable.

Those are arguably more valuable professional habits than several
individual R commands.

### 2. The treatment of `setwd()` and relative paths is excellent

The concrete contrast between

`/Users/peter/Documents/...`

and

`data/canola_trial.csv`

makes portability immediately obvious. This is much better than teaching
`setwd()` as introductory R textbooks often do.

### 3. Install versus load is explained very clearly

This is one of the most common beginner confusions, and the "once per
computer" versus "once per script" distinction is effective.

The note about red installation output not necessarily being an error is
also exactly the sort of practical reassurance students need.

### 4. Data Explorer is integrated appropriately

I like the bridge back to Excel: students can still *look* at their data
in a spreadsheet-like interface, but the Data Explorer is for viewing
rather than manually altering the source data. That reinforces the
reproducibility message without unnecessarily rejecting the visual
advantages of spreadsheets.

### 5. Missing values are introduced at the right moment

Showing that `mean()` produces `NA` and then explaining `na.rm = TRUE`
gives students an actual reason to care about missing values.

I especially like the explanation that R's default is deliberate rather
than simply annoying. It communicates an important analytical principle:
missing data should not disappear silently.

## Main concern: this chapter is doing too much

Chapter 5 currently contains:

-   project folders;
-   paths;
-   filenames;
-   packages;
-   tidyverse;
-   reading CSVs;
-   Data Explorer;
-   summary statistics;
-   missing values;
-   tidy data;
-   `pivot_longer`;
-   `pivot_wider`;
-   renaming columns.

That is a lot of conceptually distinct material between "I just learned
what a data frame is" and "now I am ready for dplyr."

I would seriously consider making the chapter's central story:

> **Get a real dataset into R, inspect it, and make sure it is ready for
> analysis.**

Everything should be judged against that narrative.

## Specific changes I would consider

### 1. Move or reduce the file-naming discussion

The advice is good, but it interrupts the path → package → read-data
progression. It could be a short callout rather than its own numbered
section.

### 2. Consider postponing `pivot_longer()` and `pivot_wider()`

This is the biggest structural question.

Tidy data is important, but pivoting is the first genuinely abstract
transformation students encounter. At this point they have not yet
learned `filter`, `select`, `mutate`, pipes, or `group_by`.

I see a strong case for:

-   keeping the **concept of tidy data** here;
-   showing a visual wide-versus-long example;
-   postponing the actual `pivot_longer()` / `pivot_wider()` syntax
    until the later data-cleaning chapter.

That would make Chapter 5 substantially lighter.

On the other hand, if students need pivoting immediately for course
assignments, the current explanation is quite good. I would then keep it
but make clear that they do not need to memorize the argument syntax.

### 3. `rename()` is probably better after `dplyr`

Teaching `rename()` immediately before the chapter explicitly devoted to
dplyr feels slightly out of sequence. You could simply say that awkward
names can be fixed and promise to show how shortly.

Alternatively, `janitor::clean_names()` is attractive for beginners
because it solves many real-world naming problems in one operation,
although introducing another package has its own cost.

### 4. Be careful with "Always run `summary()`"

I like encouraging students to inspect every dataset, but `summary()`
becomes less useful with very large or heavily categorical datasets. At
this level that is not a major problem, but I might phrase the principle
more generally:

> Before doing any analysis, inspect the dimensions, column names and
> types, missingness, and plausible ranges of important variables.

Then `glimpse()` and `summary()` are tools for doing that rather than
rituals.

## Possible streamlined Chapter 5

If simplification is the priority, I would organize it as:

1.  One folder per project
2.  Relative paths
3.  Packages and the tidyverse
4.  Reading a CSV
5.  Looking at your data
6.  Summary statistics and missing values
7.  What tidy data looks like
8.  Brief practice

Then move pivoting and perhaps renaming into the cleaning material
later.

## Bottom line on Chapter 5

The content is good; the issue is **quantity rather than quality**. This
is the chapter where I would be most aggressive about asking, "Does a
student need this *right now*?"

------------------------------------------------------------------------

# Chapter 6 --- The `dplyr` Verbs

## What works especially well

### 1. Organizing around verbs is exactly right

This chapter has a strong conceptual hook: data manipulation is mostly a
sequence of a small number of actions.

`filter`, `select`, `mutate`, and `arrange` are a very manageable first
set.

The verbs also map naturally onto questions students understand:

-   Which rows?
-   Which columns?
-   What new variable?
-   In what order?

I might even state that mapping explicitly near the beginning.

### 2. The explanation of `==` is timely

This is exactly where students will make the mistake, so this is where
the explanation belongs.

The simultaneous reminder that quoted `"South"` is text while unquoted
`South` is interpreted as an object name is useful and concise.

### 3. Introducing verbs before the pipe is pedagogically excellent

This is one of my favorite choices in these chapters.

Students first see functions in conventional form:

`filter(yields, ...)`

and only after understanding several functions do they learn that the
pipe is a way of composing them. That makes the pipe feel like a
convenience rather than mysterious syntax.

The nested-function example is particularly effective because it creates
the problem that the pipe solves.

### 4. "Read `|>` as then" is an excellent mental model

This should probably be emphasized typographically because it is the
core idea:

> Take `yields`, **then** filter..., **then** select..., **then**
> arrange....

That is much more intuitive than explaining pipes formally.

### 5. `summarise()` followed by `group_by()` is the right progression

First showing that `summarise()` turns many rows into one row, then
adding `group_by()` to produce one row per group, makes the logic
transparent.

The connection to an Excel PivotTable is especially valuable given the
sequence of the book. It tells students that they already understand the
*analytical operation*; they are merely learning R syntax for it.

## Things I would change

### 1. I would reconsider teaching `ungroup()` as routinely necessary after `summarise()`

Modern `dplyr` often drops the final grouping level after `summarise()`,
and `.groups = "drop"` gives explicit control. The current advice that
it is good practice to `ungroup()` after summarising may leave students
adding `ungroup()` mechanically everywhere.

For introductory students, I might instead say:

> Grouping can persist after some operations. If later steps should
> operate on the whole data frame, use `ungroup()` (or
> `.groups = "drop"` in `summarise()`).

Then demonstrate it when it actually matters.

### 2. The `case_when()` unit-conversion example may be more advanced than the learning objective requires

The simple conversion using `mutate()` is excellent. The mixed-units
version is realistic, but now students must simultaneously understand:

-   `mutate`;
-   `case_when`;
-   conditions;
-   `~`;
-   `NA_real_`;
-   unit conversion.

That is a lot of syntax.

I would either label this explicitly as an **advanced example** or
postpone `case_when()` until the cleaning chapter. A simple `if_else()`
example might also be easier if you want conditional transformation
here.

### 3. The final combined pipeline jumps considerably in difficulty

The culminating example is analytically interesting, but it introduces
`dense_rank()` and grouped `mutate()` while asking students to integrate
everything else.

That is probably fine as a demonstration of what is possible, but I
would distinguish:

**Core material students should be able to write themselves**

from

**A more complex example students should be able to read and explain.**

That distinction becomes increasingly important in an AI-assisted coding
course. Students do not need to memorize every function; they need to
understand the pipeline well enough to verify generated code.

### 4. Add one explicit debugging strategy for pipelines

This would be very useful pedagogically.

For example:

> If a pipeline gives the wrong answer, run it one step at a time. Put
> the cursor after each `|>` step (or temporarily delete later steps)
> and inspect the intermediate result. Find the first point where the
> data stop looking the way you expect.

That teaches a transferable programming skill and reinforces the idea
that each verb performs one comprehensible operation.

------------------------------------------------------------------------

# The progression across Chapters 4--6

The overall architecture is strong:

**Chapter 4:** objects and functions\
↓\
**Chapter 5:** real data frames from files\
↓\
**Chapter 6:** sequences of transformations

I would preserve this.

The biggest opportunity is to make the division of labor between
Chapters 5 and 6 even sharper:

### Chapter 4: Learn the language

Students should leave knowing what objects, vectors, data frames,
functions, and scripts are.

### Chapter 5: Get data into the language

Students should leave knowing how to organize a project, read data,
inspect it, and recognize whether its structure is sensible.

### Chapter 6: Do things to the data

Students should leave knowing how to filter, select, create variables,
sort, group, summarize, and chain those operations.

Under that framing, actual reshaping (`pivot_*`), extensive renaming,
and conditional cleaning arguably belong later.

------------------------------------------------------------------------

# A broader pedagogical suggestion

One thing I would lean into even more is the relationship with the Excel
chapters.

Rather than presenting R as a wholly new collection of ideas, repeatedly
tell students:

> **You already know the data operation. Now you are learning another
> way to express it.**

For example:

  Excel idea                R equivalent
  ------------------------- -----------------------------------------
  Filter rows               `filter()`
  Keep/delete columns       `select()`
  Formula in a new column   `mutate()`
  Sort                      `arrange()`
  PivotTable                `group_by()` + `summarise()`
  `AVERAGE`                 `mean()`
  `COUNT`                   `n()` / `length()` depending on context

That continuity could substantially reduce the perceived difficulty of
R.

I would not necessarily add a large table like this to every chapter,
but small "You already did this in Excel" callouts would work very well.

------------------------------------------------------------------------

# Priority edits

If I were revising these chapters now, my priorities would be:

1.  **Lighten Chapter 5.** Strongly consider moving `pivot_longer()`,
    `pivot_wider()`, and possibly `rename()` to the cleaning material.
2.  **De-emphasize base-R bracket indexing in Chapter 4.** Students are
    about to learn clearer tools for rows and columns.
3.  **Clarify `<-`, `=`, and `==`.** Establish the book's convention
    without overstating what R permits.
4.  **Make the Excel → R parallels more explicit.** This is one of the
    major pedagogical advantages of the book's ordering.
5.  **Separate "write this yourself" from "be able to read this" in
    Chapter 6.** The final pipeline and `case_when()` are useful but
    represent a noticeable complexity jump.
6.  **Add pipeline debugging advice.** Running a pipeline incrementally
    is a simple habit with very high payoff.
7.  **Resist adding more R syntax.** These chapters already contain
    enough for a first encounter. Depth of understanding is more
    valuable here than broader coverage.

## Overall verdict

I think Chapters 4--6 are in good shape. Chapter 4 is particularly
clean, and Chapter 6 gives students a useful payoff quickly. Chapter 5
is the one I would revisit structurally, mainly to make the first
encounter with real R data feel less like a checklist of everything one
should know about data organization.

The tone throughout is appropriate for the book: practical without being
purely procedural, and opinionated about good practice without turning
into a software-engineering text. The agricultural examples also feel
natural rather than pasted onto generic programming examples.

My main recommendation is therefore **subtraction and sequencing, not
expansion**.
