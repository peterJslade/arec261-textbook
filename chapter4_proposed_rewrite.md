# Proposed rewrite: Chapter 4 --- Getting Started with R

This document proposes replacement text for **every section** of Chapter
4. I have kept the chapter's basic structure and examples, but tightened
the prose, reduced a few technical side paths, and tried to make the
conceptual progression more explicit:

**R as a calculator → objects → scripts → vectors/data frames/functions
→ reproducible scripts.**

I would also remove square-bracket data-frame indexing from this
chapter. Students learn `filter()` and `select()` shortly afterward, and
`$` is enough base-R extraction for now.

------------------------------------------------------------------------

# 4 Getting Started with R

In the first three chapters, we used Excel to enter, organize,
summarize, and visualize data. We now turn to **R**, a programming
language built for working with data.

R requires a different way of working. In Excel, you usually manipulate
data by clicking on cells, menus, and buttons. In R, you write
instructions as code. That takes some getting used to, but it has an
important advantage: the instructions themselves become a record of
exactly what you did.

This chapter introduces the basic mechanics. We will use R as a
calculator, save values as **objects**, write and run an **R script**,
and introduce the two data structures we will use most often:
**vectors** and **data frames**.

## Learning Objectives

By the end of this chapter you should be able to:

1.  Explain why we use R alongside Excel.
2.  Install R and Positron and run R code.
3.  Save values as objects and use functions to work with them.
4.  Explain the difference between a vector and a data frame.
5.  Write and save an R script that can be run again from scratch.

------------------------------------------------------------------------

# 4.1 Why R? (And Why Also Excel?)

You just spent several chapters getting comfortable with Excel. Now I am
going to ask you to learn another tool.

Why?

The short answer is that **Excel and R are good at different things**.

Excel is excellent when you want to see the data directly, make quick
calculations, explore a relatively small dataset, or share a workbook
with someone who does not program. We will continue to use it.

But Excel becomes awkward when an analysis gets larger or needs to be
repeated. R has several important advantages:

-   **Reproducibility.** In R, the steps in an analysis are written down
    as code. Run the same code again and you repeat the same analysis.
    In Excel, many steps --- sorting, filtering, copying, clicking
    through menus --- leave little or no record of what you did.

-   **Scale.** Excel worksheets are limited to a little over one million
    rows, and large workbooks can become slow and difficult to manage. R
    is designed to work with much larger datasets.

-   **Repetition.** Suppose you need to perform the same analysis on 15
    files. In Excel, that may mean repeating the same sequence of clicks
    15 times. In R, you can write the instructions once and reuse them.

-   **Statistical analysis.** Excel handles basic descriptive statistics
    and regression reasonably well. R can do those things too, but it
    also gives us access to thousands of packages for more advanced
    statistical and data-analysis tasks.

R is a **programming language for statistical computing and data
analysis**. Instead of choosing an operation from a menu, you write an
instruction telling R what to do.

That makes R more difficult to learn initially than Excel. It also makes
it much more flexible.

AI changes the way we will use programming, but it does not eliminate
the value of understanding it. AI tools can generate R code remarkably
well. To use that code effectively, however, you still need to
understand the problem you are trying to solve, recognize what the code
is doing, and decide whether the result makes sense. We will return to
AI tools later in the book.

The goal of this course is therefore **not to replace Excel with R**. It
is to become comfortable choosing between them --- and, increasingly,
using them together.

> **Other resources --- why R?**
>
> -   *R for Data Science (2nd ed.)* --- a free textbook by Hadley
>     Wickham, Mine Çetinkaya-Rundel, and Garrett Grolemund. Its
>     workflow --- import, tidy, transform, visualize, model,
>     communicate --- is close to the one we will follow.
> -   *R Programming 101: Why you should use R* --- a short
>     beginner-friendly introduction.

------------------------------------------------------------------------

# 4.2 Installing R and Positron

To work with R in this course, you need two pieces of software:

1.  **R** --- the programming language and the software that actually
    runs your R code. Download and install R from CRAN, the
    Comprehensive R Archive Network.

2.  **Positron** --- the program we will use to write and run our R
    code. Download Positron after installing R.

It helps to distinguish the language from the program used to write it.

Think about a web page. The page may be written in HTML, but you can
view it in Safari, Chrome, Firefox, or another browser. The language and
the program displaying it are different things.

The same idea applies here. **R is the language. Positron is the editor
we will use to work with that language.** Other editors, including
RStudio and VS Code, can also run R code.

We will use Positron because it provides a convenient environment for
writing code, viewing data, and using modern AI coding tools.

When you first open Positron, you will see a Welcome screen similar to
Figure 4.1.

**Figure 4.1:** The Positron Welcome screen.

> **Other resources --- installing R and Positron**
>
> -   Positron documentation --- installers and setup instructions for
>     Windows, macOS, and Linux.
> -   *Getting Started with Positron: A Quick Tour* --- a short tour of
>     the interface.

------------------------------------------------------------------------

# 4.3 The Console

At the bottom of Positron is the **console**. The console lets you give
R a command and immediately see the result.

At first, you can think of R as a fancy calculator. Type:

``` r
2 + 3
```

and press Enter. R evaluates the expression and prints the answer.

R follows the usual order of operations, so you can type more
complicated expressions as well:

``` r
(12 + 8) / 4
3^2
```

**Figure 4.2:** Doing arithmetic directly in the console. Type an
expression, press Enter, and R prints the result on the next line.

You will notice that R often puts `[1]` before its output:

``` text
[1] 5
```

The `[1]` does **not** mean that the answer is 1. It tells you that the
first value shown on that line is the first value in the result. This
becomes useful when R prints a long sequence of values across several
lines. For a single number, you can simply ignore it.

## Saving answers as objects

A calculator gives you an answer and then forgets it. In R, we often
want to save a result so that we can use it again.

We do this by creating an **object**.

``` r
a <- 4
```

Read this as:

> **save 4 as `a`**

The symbol `<-` is called the **assignment operator**. It assigns the
value on the right to the name on the left.

We can then use `a` in another calculation:

``` r
b <- a * 2
b
```

After these commands, `a` contains 4 and `b` contains 8. Positron also
shows these objects in the Variables pane.

**Figure 4.3:** Saving objects in the console with `<-`. Objects appear
in the Variables pane after they are created.

R also allows `=` for assignment in many situations. In this book,
however, we will use `<-` for assignment. This makes assignment visually
distinct from `=` when we name arguments inside functions and from `==`,
which we will later use to test whether two values are equal.

Objects can hold much more than one number. For example:

``` r
yields <- c(48, 52, 47, 55, 50)
```

The function `c()` **combines** these five numbers into a sequence
called a **vector**. We can save that vector as `yields` and then use
another function to calculate its mean:

``` r
mean(yields)
```

which gives:

``` text
[1] 50.4
```

This simple example contains the basic pattern we will use throughout R:

1.  **store data or results in objects;**
2.  **use functions to do things to those objects;**
3.  **save new results when we want to use them later.**

For now we are typing commands directly into the console. That is useful
for experimenting, but it is not how we should save an analysis.

------------------------------------------------------------------------

# 4.4 R Scripts

Suppose you calculate a mean in the console today and want to repeat the
calculation next week with new data. Unless you remember exactly what
you typed, the console is not much help.

For any analysis that you want to **save, repeat, check, share, or hand
in**, write your code in an **R script**.

An R script is simply a plain-text file containing R code. R scripts end
in `.R`.

Think of the script as the **recipe for your analysis**. The data are
the ingredients; the script records the instructions. If the recipe is
complete, you --- or someone else --- should be able to run it later and
reproduce the analysis.

## Creating and running a script

In Positron, choose:

**File → New File → R File**

and save the file as `hello.R`.

**Figure 4.4:** Creating a new R file in Positron.

Now type:

``` r
# My first R script
# Author: your name
# Date: 2026-09-15

print("Hello, world!")

2 + 2

x <- c(1, 2, 3, 4, 5)
mean(x)
```

There is an important distinction here:

> **Writing code does not run code.**

At this point the instructions exist in the script, but R has not
executed them. The console remains unchanged and the object `x` does not
yet exist.

**Figure 4.5:** Code written in a script but not yet run. Writing an
instruction and executing it are two different things.

To run code from the script, you can:

1.  use the **Run** controls in Positron; or
2.  place your cursor on a line (or select several lines) and press
    **Cmd+Enter** on a Mac or **Ctrl+Enter** on Windows.

After the code runs, the results appear in the console and objects such
as `x` appear in the Variables pane.

**Figure 4.6:** After running the script, results appear in the console
and created objects appear in the Variables pane.

Let's look at what the script contains.

``` r
# My first R script
```

A line beginning with `#` is a **comment**. R ignores comments. They are
notes for the person reading the code.

``` r
print("Hello, world!")
```

`print()` is a **function**. Here it tells R to print the text
`"Hello, world!"`.

``` r
2 + 2
```

This is an expression. R evaluates it just as it did when we typed
directly into the console.

``` r
x <- c(1, 2, 3, 4, 5)
```

This creates a vector containing five numbers and saves it as the object
`x`.

``` r
mean(x)
```

This runs the function `mean()` on `x`.

The important difference from our earlier console work is that **the
instructions are now saved**. Close R, come back tomorrow, open
`hello.R`, and the code is still there. Run it again and R repeats the
same steps.

From this point onward, most code in this book will be shown as script
code rather than screenshots of Positron.

> **Other resources --- R scripts**
>
> -   *Writing and running code: script vs console* --- an introduction
>     to the distinction between interactive console work and saved
>     scripts.
> -   *The Basics of Scripts in R* --- a short introduction to creating
>     and running scripts.

------------------------------------------------------------------------

# 4.5 R Basics: Types, Vectors, Data Frames, and Functions

We now have enough mechanics to introduce the basic pieces of R that we
will use for data analysis.

R stores things as **objects**. An object might contain a single number,
a sequence of numbers, a table of data, a statistical model, or even a
graph.

For now, we need to understand two important kinds of objects:

-   **vectors**, which hold a sequence of values; and
-   **data frames**, which hold data in rows and columns.

Values in R also have a **type**. The three types you will encounter
most often are:

-   **numeric** --- numbers such as `48`, `3.7`, or `-2`;
-   **character** --- text such as `"wheat"` or `"Saskatoon"`;
-   **logical** --- the values `TRUE` and `FALSE`.

You do not need to memorize a taxonomy of R objects and types. The
important thing for now is to recognize what kind of information you are
working with.

## Vectors

A **vector** is a sequence of values of the same type.

We have already created one:

``` r
yields <- c(48, 52, 47, 55, 50)
```

Here `yields` is a numeric vector.

Vectors can also contain text:

``` r
varieties <- c("InVigor", "DK", "Clearfield", "InVigor", "DK")
```

or logical values:

``` r
is_irrigated <- c(TRUE, FALSE, FALSE, TRUE, FALSE)
```

Notice that character values are placed inside quotation marks, while
numbers and the logical values `TRUE` and `FALSE` are not.

One reason vectors are so useful is that R can perform an operation on
every value at once.

Suppose the five yields are measured in bushels per acre and we want to
convert them to tonnes per hectare:

``` r
yields <- c(48, 52, 47, 55, 50)

yields * 0.0560
```

R multiplies **every value in the vector** by `0.0560`:

``` text
[1] 2.688 2.912 2.632 3.080 2.800
```

We do not need to write the calculation five times.

This is called **vectorized** calculation, and it is one of the basic
ways R works with data.

## Data Frames

A vector is useful for one variable. Real datasets usually contain many
variables.

In R, a table of data is called a **data frame**.

A data frame should already look familiar from Excel:

-   each **row** is an observation;
-   each **column** is a variable.

For example, suppose we have five fields:

``` r
fields <- data.frame(
  field_id = c("F01", "F02", "F03", "F04", "F05"),
  region = c("South", "South", "Central", "North", "North"),
  yield = c(48, 52, 47, 55, 50)
)

fields
```

R prints:

``` text
  field_id  region yield
1      F01   South    48
2      F02   South    52
3      F03 Central    47
4      F04   North    55
5      F05   North    50
```

Here:

-   a **row** represents a field;
-   `field_id`, `region`, and `yield` are **variables**;
-   each column is itself a vector.

We created this small data frame manually so that you can see how it is
constructed. In practice, you will usually read a data frame from a file
rather than type it into R. That is the subject of the next chapter.

To refer to one column in a data frame, use `$`:

``` r
fields$yield
```

Read this as:

> **the `yield` column of `fields`**

Because that column is a numeric vector, we can use it in calculations:

``` r
mean(fields$yield)
```

which gives:

``` text
[1] 50.4
```

This connection is worth remembering:

> **A data frame is a table, and its columns are vectors.**

In the next chapters we will learn much more convenient tools for
choosing rows and columns, creating new variables, and summarizing data
frames.

## Functions

Most of our work in R consists of applying **functions** to objects.

A function is an instruction that takes some input, does something with
it, and returns a result.

We have already used several functions:

``` r
c()
mean()
print()
data.frame()
```

For example:

``` r
mean(fields$yield)
```

asks the function `mean()` to calculate the mean of the vector
`fields$yield`.

The information supplied to a function is called an **argument**. In
this example, `fields$yield` is the argument supplied to `mean()`.

Many of the descriptive statistics from the previous chapter have
straightforward R functions:

``` r
mean(fields$yield)                 # Mean
median(fields$yield)               # Median
max(fields$yield) - min(fields$yield)  # Range
var(fields$yield)                  # Variance
sd(fields$yield)                   # Standard deviation
sd(fields$yield) / mean(fields$yield)  # Coefficient of variation
```

Some functions need more than one argument.

For example, `quantile()` can calculate a percentile. To find the 25th
percentile of `fields$yield`, we need to tell R both **which data** to
use and **which percentile** we want:

``` r
quantile(fields$yield, 0.25)
```

Here the arguments are supplied in the order that `quantile()` expects
them.

We can also name the arguments:

``` r
quantile(x = fields$yield, probs = 0.25)
```

Named arguments are particularly useful when a function has several
options because the code tells the reader what each value means.

You will see this pattern constantly in R:

``` r
function(argument1, argument2)
```

You do **not** need to memorize every function or every argument. When
you need help with a function, type `?` followed by its name:

``` r
?mean
```

R opens the function's documentation. The documentation can look
intimidating at first, but it tells you what the function does, what
arguments it accepts, and what it returns.

Knowing how to find that information is more important than memorizing
it.

> **Other resources --- vectors, data frames, and functions**
>
> -   *Hands-On Programming with R* --- introductory chapters on
>     objects, vectors, data frames, and functions.
> -   *R Programming 101: Using functions and objects in R*.
> -   *Introduction to vectors in R*.

------------------------------------------------------------------------

# 4.6 Writing Good R Scripts

At this point you know enough R to write a small analysis. Before we
move on to real datasets, it is worth establishing a few habits.

The goal is simple:

> **Someone should be able to open your script, understand what it does,
> and run it from beginning to end.**

Here are five habits that will help.

### 1. Give the script a short header

At the top, record what the script is for. For course work, your name
and a brief description are usually enough. For a larger project, you
may also want to record the expected inputs and outputs.

### 2. Use comments to explain decisions

Comments begin with `#`.

Do not comment every obvious line:

``` r
mean_yield <- mean(yields)  # calculate mean yield
```

The code already tells us that.

Comments are more useful when they explain **why** something was done:

``` r
# Weight by acres because fields differ substantially in size
weighted_yield <- sum(yields * acres) / sum(acres)
```

### 3. Use descriptive object names

Prefer:

``` r
mean_yield
total_acres
wheat_fields
```

to:

``` r
x
a
data2
```

A slightly longer name is usually worth it if it makes the code easier
to understand.

### 4. Break an analysis into understandable steps

You do not need to cram an entire analysis into one line. Saving
intermediate results can make code much easier to inspect and debug.

### 5. Make the script runnable from the beginning

This is the most important habit.

A good script should not depend on commands that you happened to type
into the console earlier. If you restart R and run the script from top
to bottom, it should reproduce the analysis.

Here is a small example:

``` r
# ---
# Title: Farm yield summary
# Author: Your Name
# Date: 2026-09-22
# Description:
#   Computes total production and the acreage-weighted
#   average yield for five wheat fields.
# ---

# 1. Data

yields <- c(48, 52, 47, 55, 50)  # bushels per acre
acres <- c(310, 220, 95, 180, 150)

# 2. Production by field

production <- yields * acres

# 3. Total production

total_bu <- sum(production)

# 4. Farm average yield, weighted by acres

weighted_yield <- total_bu / sum(acres)

total_bu
weighted_yield
```

There is nothing sophisticated about this script. That is the point.

It contains the data, records every calculation, uses meaningful names,
and can be run from beginning to end. Six months from now, you could
open it and understand exactly what you did.

That is one of the central advantages of working in R.

In the next chapter, we will stop creating tiny datasets by hand and
learn how to bring real data into R.

> **Other resources --- writing good R scripts**
>
> -   *The tidyverse style guide* --- a useful reference for naming,
>     spacing, and readable R code.
> -   Riffomonas Project --- videos on writing clear, reproducible R
>     code.

------------------------------------------------------------------------

# Notes on the rewrite

## Main changes I would make relative to the current version

1.  **Make the chapter's conceptual spine more explicit.** The rewritten
    sections repeatedly reinforce the sequence: objects → functions →
    scripts → vectors → data frames.

2.  **Remove square-bracket indexing.** `fields[1, ]`, `fields[, 1]`,
    etc. are legitimate R, but students do not need them yet. Chapter 6
    gives them `filter()` and `select()`, which are the tools you
    actually want them to use.

3.  **Do not demonstrate overwriting `fields$yield`.** The current
    example changes the yield values from 48--55 to 58--65. That means
    the descriptive-statistics examples later in the section operate on
    different data from the data frame students were originally shown.
    It adds unnecessary state to keep track of.

4.  **Clarify `<-`, `=`, and `==`.** Rather than saying `=` should be
    reserved for "other operations," explain the convention students
    will actually encounter: `<-` for assignment, `=` for named function
    arguments, and `==` for equality tests.

5.  **Simplify the object/type explanation.** Beginners mainly need to
    know that values have types, vectors contain one type, and
    data-frame columns can have different types.

6.  **Explain vectorization explicitly.** The unit-conversion example is
    a good opportunity to name an important feature of R rather than
    presenting it as a one-off trick.

7.  **Strengthen the connection between vectors and data frames.** "A
    data frame is a table, and its columns are vectors" is probably the
    single most useful conceptual sentence in Section 4.5.

8.  **Make functions less abstract.** Frame a function as an instruction
    that takes input and returns a result, then introduce "argument" as
    the name for the input supplied to it.

9.  **Reduce the sense that students should memorize syntax.**
    Explicitly tell them that knowing how to inspect documentation is
    more important than memorizing every function and argument.

10. **Give the final script a visible result.** The revised example
    saves and prints both `total_bu` and `weighted_yield`, so the
    chapter ends with a small but complete analysis rather than an
    expression left unsaved.

11. **Keep the tone informal but slightly tighten the prose.** I would
    preserve lines such as "Now I am going to ask you to learn another
    tool" and the recipe analogy. They make the chapter sound like an
    instructor speaking to students rather than software documentation.

12. **Keep the chapter deliberately small.** I would resist adding
    factors, lists, matrices, environments, working directories,
    packages, tibbles, pipes, or tidyverse syntax here. The chapter's
    job is to make the basic R mental model feel manageable; the next
    two chapters can build on it.
