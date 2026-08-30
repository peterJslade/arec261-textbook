# Proposed rewrite: Chapter 5 --- Working with Data in R

This rewrite keeps the chapter's main purpose --- moving from toy
objects created inside R to real data stored in files --- but makes that
purpose more explicit throughout.

My main structural change is to **keep the concept of tidy data in
Chapter 5 but postpone the actual `pivot_longer()` / `pivot_wider()`
syntax**. Students have not yet learned the basic `dplyr` verbs or
pipes, and pivoting is the first transformation here whose syntax is
substantially more complicated than the underlying idea. I would
introduce the problem now and tell students that Chapter 9 will show
them how to fix it.

I would also shorten the material on file naming, avoid introducing
`janitor` here, and make the central workflow very explicit:

**open project → load package → read data → inspect data → check for
problems**

------------------------------------------------------------------------

# 5 Working with Data in R

In the last chapter, we created small datasets directly in R. Real data
analysis usually starts somewhere else: with a file.

That creates a few practical questions. Where should the file go? How
does R find it? How do we bring it into R? And once it is there, how do
we check that R has read it correctly?

This chapter develops a simple workflow for working with real data:

1.  Keep everything for an analysis in one **project folder**.
2.  Refer to files using **relative paths**.
3.  Use **packages** to add functions to R.
4.  Read data from a CSV file.
5.  Inspect the data before doing any analysis.
6.  Recognize whether the data are organized in a useful shape.

These habits are not exciting, but they prevent a remarkable number of
problems later.

## Learning Objectives

By the end of this chapter you should be able to:

1.  Set up a self-contained project folder for an analysis.
2.  Explain the difference between an absolute and a relative path.
3.  Install and load an R package, and explain the difference between
    the two.
4.  Read a CSV file into R as a data frame.
5.  Inspect a new dataset and identify common problems.
6.  Calculate basic summary statistics while handling missing values
    correctly.
7.  Explain what **tidy data** means and recognize data that need to be
    reshaped.

------------------------------------------------------------------------

# 5.1 One Folder Per Project

Before we read any data into R, we need somewhere to put it.

A good rule is:

> **Keep everything for one analysis inside one project folder.**

Suppose we are analyzing a canola variety trial. Our folder might look
like this:

``` text
canola-trial/
  data/
    canola_trial.csv
  R/
    01_clean.R
    02_analysis.R
  output/
    yield_by_variety.png
    summary_table.csv
  README.md
```

The top-level folder, `canola-trial/`, contains everything needed for
the analysis.

Inside it:

-   `data/` contains the original data;
-   `R/` contains our scripts;
-   `output/` contains tables, figures, and other results produced by
    those scripts;
-   `README.md` can contain notes explaining the project.

The exact folder names are less important than the principle: **the
project should be self-contained**.

If you zip the `canola-trial/` folder and send it to somebody else, they
should have everything they need to run your analysis.

## Keep the raw data raw

There is one especially important rule:

> **Do not manually edit the original data file.**

Suppose `canola_trial.csv` contains an obvious typo. You could open the
file in Excel, fix the cell, and save it.

The problem is that there is now no record of what you changed.

Instead, keep the original file exactly as you received it and make the
correction in your R script. Then the script records both **what
changed** and **how it changed**.

This is why we keep the original file in `data/`.

## Outputs should be reproducible

The opposite principle applies to `output/`.

Everything there should be something your scripts can recreate.

If you delete a graph from `output/`, you should be able to run the
analysis again and regenerate it. In fact, deleting the contents of
`output/` and seeing whether your scripts recreate everything is a
useful test of whether an analysis is reproducible.

## Open the project folder in Positron

At the start of a session, open the project folder itself in Positron:

**File → Open Folder...**

Choose the folder containing `data/`, `R/`, and `output/`.

R now treats this project folder as its starting point when it looks for
files.

That will make the paths in the next section much simpler.

> **Why this matters for AI**
>
> AI coding assistants also work better when the relevant scripts and
> files are organized together. When we use AI tools later in the book,
> a well-organized project gives the assistant useful context about the
> analysis.

------------------------------------------------------------------------

# 5.2 Paths, and Why `setwd()` Is a Trap

A **path** tells R where to find a file.

Suppose our data are stored here:

``` text
canola-trial/
  data/
    canola_trial.csv
```

There are two ways we could tell R where the file is.

An **absolute path** gives the file's complete location on one computer:

``` r
read_csv("/Users/peter/Documents/canola-trial/data/canola_trial.csv")
```

A **relative path** describes the location relative to the project
folder:

``` r
read_csv("data/canola_trial.csv")
```

The second version is much better.

Why?

The absolute path contains information specific to one computer: the
username `peter`, the location of the Documents folder, and the
operating system's folder structure.

If I send that script to you, you probably do not have:

``` text
/Users/peter/Documents/
```

But if we both have the same project folder, we both have:

``` text
data/canola_trial.csv
```

So the general rule is:

> **Open the project folder in Positron and use relative paths inside
> your scripts.**

## Why not `setwd()`?

R has a function called `setwd()` that changes the working directory:

``` r
setwd("/Users/peter/Documents/canola-trial")
```

You will see this in old scripts and online examples.

Do **not** put a command like this in a script you intend to share.

It solves the path problem on your computer by creating a path problem
on everybody else's.

Instead:

1.  open the project folder in Positron;
2.  use paths relative to that folder.

If you are ever unsure where R thinks it is, run:

``` r
getwd()
```

`getwd()` means **get working directory**. R will print the folder it is
currently treating as its starting point.

> **Windows note**
>
> Windows normally displays paths with backslashes:
>
> ``` text
> C:\Users\Peter\Documents
> ```
>
> Inside R strings, use forward slashes instead:
>
> ``` text
> C:/Users/Peter/Documents
> ```
>
> R understands them on Windows and they avoid problems caused by the
> special meaning of `\` inside text strings.

------------------------------------------------------------------------

# 5.3 File Names

Good file names make projects easier to work with.

Two simple rules are enough for now.

First, use short descriptive names without spaces or unusual
punctuation:

``` text
field_yields.csv
canola_prices.csv
yield_by_region.png
```

rather than:

``` text
Field Yields FINAL!!.csv
canola prices new.csv
```

Second, when a date belongs in a file name, write it as:

``` text
YYYY-MM-DD
```

For example:

``` text
2026-09-15_deliveries.csv
```

This format has a useful property: alphabetical order is also
chronological order.

You may eventually encounter projects full of files called:

``` text
analysis_final.R
analysis_final_v2.R
analysis_final_REAL.R
```

That is a sign that the project needs **version control**, rather than
increasingly creative file names. Git is the most common tool for doing
this, but we will not cover it in this book.

For this course, sensible file names and one clearly organized project
folder will take us a long way.

------------------------------------------------------------------------

# 5.4 Packages

R comes with hundreds of useful functions. Other people have written
thousands more and bundled them into **packages**.

A package is an add-on that gives R additional functions.

Using a package involves two different steps:

### Step 1: Install it

You install a package onto your computer with:

``` r
install.packages("tidyverse")
```

You normally do this **once per computer**.

Installation downloads the package from the internet and stores it on
your machine.

The first installation may take a few minutes and produce a lot of
messages in the console. Some messages may appear in red even when
nothing has gone wrong. What matters is whether R ultimately reports an
error.

### Step 2: Load it

Installing a package does not automatically make its functions available
every time you start R.

At the beginning of a script that uses the package, load it with:

``` r
library(tidyverse)
```

You normally do this **once per R session or script**.

A useful way to remember the distinction is:

> **Install once. Load whenever you use it.**

If you try to use a package function without loading the package, you
may see an error such as:

``` text
could not find function "read_csv"
```

That often means that the package containing the function has not been
loaded.

There is one small syntax difference worth noticing:

``` r
install.packages("tidyverse")
library(tidyverse)
```

The package name is in quotation marks when we install it, but not when
we load it.

Do not worry about why yet. Just recognize the pattern.

------------------------------------------------------------------------

# 5.5 The Tidyverse

The package we will use most often is actually a collection of packages
called the **tidyverse**.

Different tidyverse packages do different jobs. Four will be
particularly important in this book:

  Package     Main job
  ----------- -------------------
  `readr`     reading data
  `dplyr`     manipulating data
  `tidyr`     reshaping data
  `ggplot2`   making graphs

Installing the tidyverse installs these packages and several others:

``` r
install.packages("tidyverse")
```

Then:

``` r
library(tidyverse)
```

loads the core tidyverse packages.

Base R can do many of the same things. You will encounter base-R
functions in documentation, online examples, and AI-generated code.
There is nothing wrong with mixing the two.

This book emphasizes the tidyverse because its packages use a consistent
style and provide particularly convenient tools for working with tabular
data.

In this chapter we will use `readr` to bring data into R. In the next
chapter we will use `dplyr` to manipulate it.

> **Other resources --- packages and the tidyverse**
>
> -   *R for Data Science (2nd ed.)* introduces the tidyverse workflow:
>     import → tidy → transform → visualize → model → communicate.
> -   The tidyverse website lists the packages in the collection and
>     what each is designed to do.

------------------------------------------------------------------------

# 5.6 Reading Data from CSV

Now we are ready to work with a real dataset.

For this chapter and the next, we will use `field_yields.csv`. It
contains observations on 60 canola fields, including:

-   field ID;
-   region;
-   variety;
-   acres;
-   yield;
-   year;
-   seeding date;
-   units.

Download the file and place it in your project's `data/` folder:

``` text
your-project/
  data/
    field_yields.csv
  R/
  output/
```

Make sure you have opened `your-project/` itself in Positron.

Then start your script by loading the tidyverse:

``` r
library(tidyverse)
```

and read the file:

``` r
yields <- read_csv("data/field_yields.csv")
```

Read this line from right to left:

> **Read `field_yields.csv` from the `data` folder, and save the
> resulting data frame as `yields`.**

After running the line, `yields` is an object in R.

`read_csv()` also prints some information about the **column types** it
detected. For example, it may recognize a column as numeric, character,
or a date.

R is usually good at guessing column types, but it is not infallible.
That is one reason we always inspect a dataset after reading it.

## When R cannot find the file

A common beginner error looks something like this:

``` text
Error: 'data/field_yields.csv' does not exist
```

Do not start changing the code randomly. Check two things.

First, ask:

> **Did I open the correct project folder in Positron?**

The folder you opened should contain `data/`.

Second, run:

``` r
getwd()
```

and check where R thinks the project starts.

Then compare the folder structure with the path:

``` r
"data/field_yields.csv"
```

Starting from the folder printed by `getwd()`, can you go into a folder
called `data` and find a file called `field_yields.csv`?

If yes, the path should work.

## A few related functions

CSV means **comma-separated values**, but text data can be separated in
other ways.

For example:

``` r
read_csv("data/file.csv")
read_csv2("data/file.csv")
read_tsv("data/file.tsv")
```

`read_csv2()` is useful for files that use semicolons rather than
commas, while `read_tsv()` reads tab-separated files.

To write a data frame back to a CSV file, use:

``` r
write_csv(yields, "output/yields_clean.csv")
```

Notice the symmetry:

``` r
read_csv()
write_csv()
```

One brings data **into** R; the other writes data **out of** R.

------------------------------------------------------------------------

## Viewing and Inspecting the Data

Successfully reading a file does not mean we are ready to analyze it.

Before doing anything else, inspect it.

A few useful commands are:

``` r
yields
head(yields)
nrow(yields)
ncol(yields)
names(yields)
glimpse(yields)
summary(yields)
```

They answer different questions.

`nrow()` and `ncol()` tell us how many rows and columns we have:

``` r
nrow(yields)
ncol(yields)
```

`names()` shows the column names:

``` r
names(yields)
```

`glimpse()` gives a compact view of each column and its type:

``` r
glimpse(yields)
```

`summary()` gives a quick numerical description of the columns:

``` r
summary(yields)
```

For numeric variables, it reports quantities such as the minimum,
median, mean, maximum, and quartiles.

The goal is not to run these commands mechanically. The goal is to ask:

-   Did I get the number of observations I expected?
-   Are the variables I expected actually present?
-   Did R interpret numeric variables as numbers?
-   Are the values in plausible ranges?
-   Are there missing values?
-   Is anything obviously wrong?

That habit --- **look at the data before analyzing it** --- catches many
mistakes cheaply.

### Viewing Data in Positron

You can also inspect the data visually.

After reading the file, `yields` appears in Positron's Variables pane.
Click it to open the **Data Explorer**.

The Data Explorer looks somewhat like a spreadsheet. You can scroll
through rows and columns, sort and filter the display, and inspect
summaries of individual variables.

This is useful because some problems are much easier to notice by
looking at the data than by reading console output.

There is one important difference from Excel:

> **The Data Explorer is for viewing data, not manually fixing it.**

If you discover a problem, make the correction in your R script. That
way the change is reproducible.

A good workflow is therefore:

``` text
READ → INSPECT → CHECK → ANALYZE
```

Do not skip the middle two steps.

> **Other resources --- reading data**
>
> -   *R for Data Science (2nd ed.)*, "Data import," covers
>     `read_csv()`, column types, and common import problems.
> -   The `readr` documentation provides a reference for `read_csv()`
>     and related functions.

------------------------------------------------------------------------

# 5.7 Summary Statistics in R

Once the data are in R, we can calculate the same summary statistics we
used in Excel.

Suppose we want to describe `yield_bu_acre`.

Because `yield_bu_acre` is a column of the data frame `yields`, we refer
to it as:

``` r
yields$yield_bu_acre
```

Then:

``` r
mean(yields$yield_bu_acre)
median(yields$yield_bu_acre)
sd(yields$yield_bu_acre)
var(yields$yield_bu_acre)
min(yields$yield_bu_acre)
max(yields$yield_bu_acre)
range(yields$yield_bu_acre)
IQR(yields$yield_bu_acre)
```

For percentiles, use `quantile()`:

``` r
quantile(yields$yield_bu_acre, 0.25)
```

or calculate several at once:

``` r
quantile(yields$yield_bu_acre, c(0.25, 0.5, 0.75))
```

These functions should look familiar from the previous chapter. The
statistical ideas have not changed; only the way we ask the computer to
calculate them has.

## Missing values

Real datasets often contain missing observations.

R represents a missing value as:

``` r
NA
```

Suppose some fields are missing yield observations. Then this may
happen:

``` r
mean(yields$yield_bu_acre)
```

``` text
[1] NA
```

Why doesn't R simply average the values that are present?

Because doing so would silently discard information.

R instead forces you to make an explicit decision about the missing
observations.

If you want the mean of the available values, write:

``` r
mean(yields$yield_bu_acre, na.rm = TRUE)
```

Here `na.rm` means **remove NAs** before doing the calculation.

Compare:

``` r
mean(yields$yield_bu_acre)
mean(yields$yield_bu_acre, na.rm = TRUE)
```

The first says:

> Calculate the mean of these observations.

If one of those observations is unknown, R cannot calculate the mean and
returns `NA`.

The second says:

> Calculate the mean using the observations that are not missing.

That may be exactly what we want --- but now the decision is visible in
the code.

This is an important difference from Excel, where many functions ignore
blank cells automatically.

Neither behavior solves the underlying statistical problem of missing
data. For now, the important point is simply:

> **If R unexpectedly returns `NA`, check whether your data contain
> missing values.**

We will return to missing data when we clean datasets in Chapter 9.

------------------------------------------------------------------------

# 5.8 Tidy Data

Before analyzing a dataset, we also need to think about its **shape**.

The tidyverse is built around an idea called **tidy data**.

A dataset is tidy when:

1.  every **variable** has its own column;
2.  every **observation** has its own row;
3.  every **value** has its own cell.

For example, this dataset is tidy:

  region    crop       yield
  --------- -------- -------
  South     Canola        41
  South     Wheat         52
  South     Barley        64
  Central   Canola        44
  Central   Wheat         55
  Central   Barley        68

What is an observation here?

A **region--crop combination**.

What are the variables?

`region`, `crop`, and `yield`.

Each variable has a column and each observation has a row.

Now compare this version:

  region      Canola   Wheat   Barley
  --------- -------- ------- --------
  South           41      52       64
  Central         44      55       68

This table may be easier for a person to read, but it is not tidy.

Why?

`Canola`, `Wheat`, and `Barley` are not really three different
variables. They are three possible **values of the variable `crop`**.

The actual variables are:

``` text
region
crop
yield
```

This is the same **wide versus long** distinction we encountered in
Excel.

The wide table:

``` text
region    Canola    Wheat    Barley
```

can be transformed into the long table:

``` text
region    crop      yield
```

and vice versa.

For analysis in R, the long or tidy form is often much more convenient
because `crop` is now an ordinary variable. We can ask R to filter by
crop, group observations by crop, or compare crops.

## Recognizing untidy data

Here are some common warning signs.

### Values stored in column names

``` text
region    2024    2025    2026
```

If those columns contain annual yields, `2024`, `2025`, and `2026` are
values of a variable called `year`.

A tidy version would contain:

``` text
region    year    yield
```

### More than one variable in a column

Suppose a column called `region_variety` contains:

``` text
South_InVigor
North_DK
Central_Clearfield
```

That column contains two variables: `region` and `variety`.

### One observation spread over several rows

If price is stored in one row and quantity in another row for the same
market and year, a single observation may be split across rows.

The exact definition of an "observation" depends on the dataset and the
question being asked. But the basic test is always useful:

> **What does one row represent?**

You should be able to answer that question.

When you first open a dataset, ask:

-   What does one row represent?
-   What does each column represent?
-   Are some values hiding in column names?
-   Does one column contain several different variables?

If the answers reveal a problem, the data may need to be reshaped before
analysis.

We will learn the R functions for doing that --- including
`pivot_longer()` and `pivot_wider()` --- in Chapter 9. For now, the goal
is to **recognize the shape that analysis wants**.

> **Other resources --- tidy data**
>
> -   *R for Data Science (2nd ed.)*, "Data tidying," develops the
>     tidy-data idea and shows how datasets are reshaped between long
>     and wide forms.

------------------------------------------------------------------------

# 5.9 Column Names

Column names matter because we type them repeatedly in our code.

Real datasets sometimes arrive with names such as:

``` text
Yield (bu/ac)
REGION_NAME
Field ID Number
```

These are readable to a person, but inconvenient to use in R.

For this book, we will generally prefer names such as:

``` text
yield_bu_ac
region
field_id
```

A useful convention is:

-   use lowercase letters;
-   separate words with underscores;
-   keep names short but descriptive.

This style is often called **snake_case**.

You do not need to fix every imperfect column name immediately. But when
you inspect a new dataset with:

``` r
names(yields)
```

look for names that will make the analysis unnecessarily awkward.

In Chapter 6, after we introduce the `dplyr` verbs, we will see how to
rename columns in code. Chapter 9 will deal more broadly with cleaning
messy data.

For now, the important habit is simply:

> **Inspect your column names when you read a new dataset.**

------------------------------------------------------------------------

# 5.10 Putting the Workflow Together

We can now put the chapter into one short script.

Suppose our project contains:

``` text
field-yields/
  data/
    field_yields.csv
  R/
    01_explore.R
  output/
```

Open `field-yields/` in Positron and create `01_explore.R`:

``` r
# ---
# Title: Explore field yield data
# Author: Your Name
# ---

# Load packages
library(tidyverse)

# Read data
yields <- read_csv("data/field_yields.csv")

# Inspect structure
nrow(yields)
ncol(yields)
names(yields)
glimpse(yields)

# Inspect values
summary(yields)

# Summarize yield
mean(yields$yield_bu_acre, na.rm = TRUE)
median(yields$yield_bu_acre, na.rm = TRUE)
sd(yields$yield_bu_acre, na.rm = TRUE)
```

There is nothing complicated here, but notice what the script does
**not** contain.

It does not contain:

``` r
setwd("/Users/yourname/...")
```

It does not rely on manually edited data.

And it does not jump straight from reading the file to analysis without
checking what came in.

Instead, it follows a reproducible workflow:

``` text
OPEN PROJECT
     ↓
LOAD PACKAGES
     ↓
READ DATA
     ↓
INSPECT DATA
     ↓
CHECK FOR PROBLEMS
     ↓
ANALYZE
```

That is the habit to carry into the rest of the book.

In the next chapter, we will learn how to manipulate the data itself:
selecting columns, filtering rows, creating variables, sorting
observations, and calculating summaries for groups.

------------------------------------------------------------------------

# 5.11 Test Bank Sample

1.  **Project structure.** Why is it useful to keep the data, scripts,
    and outputs for an analysis inside one project folder?

2.  **Raw data.** A classmate notices three errors in a CSV file, fixes
    the cells manually in Excel, and saves over the original file. What
    is the problem with this approach?

3.  **Paths.** Explain the difference between an absolute path and a
    relative path. Which should normally appear in a shared R script?

4.  **Working directories.** Why is this line a bad idea in a script you
    plan to share?

    ``` r
    setwd("C:/Users/Peter/Documents/canola-project")
    ```

5.  **Packages.** Explain the difference between:

    ``` r
    install.packages("tidyverse")
    library(tidyverse)
    ```

6.  **Reading data.** A file called `yields.csv` is inside the `data/`
    folder of your project. Write one line of R that reads it into an
    object called `yields`.

7.  **Troubleshooting.** `read_csv("data/yields.csv")` says the file
    does not exist. What are the first two things you should check?

8.  **Inspecting data.** What do `names()`, `glimpse()`, and `summary()`
    help you learn about a newly imported dataset?

9.  **Missing values.** Why might:

    ``` r
    mean(yields$yield_bu_acre)
    ```

    return `NA`? What does `na.rm = TRUE` change?

10. **Tidy data.** A dataset has columns `region`, `2024`, `2025`, and
    `2026`, with yields stored under the three year columns. Explain why
    the dataset is not tidy and describe what the tidy version should
    look like.

11. **Shape.** What question should you be able to answer about every
    row in a dataset?

12. **Column names.** Which is generally easier to work with in R,
    `Yield (bu/ac)` or `yield_bu_ac`, and why?

------------------------------------------------------------------------

# 5.12 Practice Exercises

Use the `field_yields.csv` dataset for these exercises.

1.  Create a project folder with `data/`, `R/`, and `output/`
    subfolders. Put `field_yields.csv` in `data/` and open the project
    folder in Positron.

2.  Run:

    ``` r
    getwd()
    ```

    Explain what the result means.

3.  Create an R script in `R/` that loads the tidyverse and reads
    `field_yields.csv` using a relative path.

4.  Use `nrow()`, `ncol()`, `names()`, `glimpse()`, and `summary()` to
    inspect the dataset. Write down:

    -   what one row represents;
    -   how many observations there are;
    -   how many variables there are;
    -   which variables are numeric;
    -   whether you notice any missing values.

5.  Calculate the mean yield first with:

    ``` r
    mean(yields$yield_bu_acre)
    ```

    and then with:

    ``` r
    mean(yields$yield_bu_acre, na.rm = TRUE)
    ```

    Explain why the results differ.

6.  Calculate the median, standard deviation, minimum, maximum, and
    interquartile range of yield, ignoring missing values where
    necessary.

7.  Imagine a second dataset with this structure:

      region     2024   2025   2026
      -------- ------ ------ ------
      South        41     44     46
      North        38     40     43

    Explain:

    -   what the variables actually are;
    -   why the year columns make the table untidy;
    -   what one row would represent after the data were converted to
        tidy form.

8.  Close R and reopen the project. Run your script from the beginning.
    Does it reproduce your results without any commands typed manually
    into the console? If not, fix it.

------------------------------------------------------------------------

# Notes on the rewrite

## 1. The chapter now has one clearer job

The current chapter contains several worthwhile topics, but the central
story gets somewhat buried. I would make Chapter 5 explicitly about the
transition from **data on disk** to **a trustworthy data frame in R**.

The recurring workflow is:

> **open → read → inspect → check → analyze**

That gives students a mental model rather than a list of unrelated R
skills.

## 2. I would postpone `pivot_longer()` and `pivot_wider()`

This is the biggest change.

I would absolutely teach **tidy data** here. Students should understand
long versus wide data and be able to recognize when years, crops,
treatments, etc. are incorrectly stored as column names.

But I would not yet require:

``` r
pivot_longer(
  yields_wide,
  cols = c(Canola, Wheat, Barley),
  names_to = "crop",
  values_to = "yield"
)
```

At this point students have not learned `select()`, `filter()`,
`mutate()`, pipes, or tidy-selection syntax. `pivot_longer()` therefore
introduces several new syntactic ideas at once.

The concept is more important than the syntax here. Teach them to
recognize the problem now; teach them to fix it when they reach data
cleaning.

## 3. I would postpone `rename()` and `janitor::clean_names()`

The current section introduces a `dplyr` verb immediately before the
chapter devoted to `dplyr`, and then introduces another package solely
for `clean_names()`.

Neither is difficult, but together they add package and syntax overhead
to a chapter that already contains a lot.

I would teach the **column-naming convention** here and teach the
transformations later.

## 4. I would shorten the file-name section

The advice is good, particularly ISO-style dates. But this is supporting
material rather than a major learning objective, so I would keep it to a
few paragraphs.

## 5. I would slightly soften the claim about red package-installation text

Rather than saying red text is normal and not an error, I would say that
installation produces many messages and that **red text does not by
itself mean the installation failed**. Students should look for an
actual error message.

## 6. I would make data inspection purposeful rather than ritualistic

The current chapter says to always run `summary()`. I would instead
teach students what they are trying to discover:

-   dimensions;
-   variable names;
-   column types;
-   missingness;
-   implausible values.

Then `glimpse()`, `summary()`, and the Data Explorer become tools for
answering questions rather than commands students run because the book
told them to.

## 7. I would emphasize the Data Explorer

For students coming directly from Excel, the Data Explorer is a useful
bridge. It reassures them that using R does not mean giving up the
ability to actually **look at the table**.

The key contrast is worth emphasizing:

> Excel often combines viewing and editing.\
> In this workflow, Positron lets you view the data, while the script
> records the changes.

## 8. Missing values should remain here

I would definitely retain the current `NA` / `na.rm = TRUE` material. It
arises naturally from summary statistics and illustrates an important
difference between R and Excel.

The current chapter's explanation that R does not silently ignore
missing observations is particularly useful. I would preserve that idea.

## 9. The Excel connections should remain explicit

Students have already learned summary statistics and long versus wide
data in Excel. I would repeatedly remind them that the **statistical or
data-management idea has not changed**.

They are learning a new way to express an operation they already
understand.

## 10. I added a short "Putting the Workflow Together" section

I think the chapter benefits from ending with one complete but simple
script.

Students should see that a real R workflow is not a collection of
isolated console commands. It is a script that:

``` text
loads packages
→ reads data
→ inspects data
→ produces results
```

That also sets up Chapter 6 very naturally.

## 11. I would not make `write_csv()` a major concept

It is useful enough to mention because it mirrors `read_csv()`, but
students do not need to do much with it yet. Later chapters will give
them more meaningful reasons to export cleaned data or results.

## 12. I would keep `getwd()` but not dwell on working-directory mechanics

Students need `getwd()` mainly as a debugging tool. They do not need a
detailed mental model of R sessions and working directories beyond:

> Open the project folder; relative paths start there; `getwd()` tells
> you where R currently thinks "there" is.

That is sufficient for now.

## 13. I would make the transition to Chapter 6 explicit

Chapter 5 should end with students having successfully imported and
inspected a data frame but not yet knowing how to manipulate it.

That creates a natural question:

> "Okay --- I have the data in R. How do I actually do things to it?"

Chapter 6 then has a very clear answer: **the `dplyr` verbs**.

------------------------------------------------------------------------

# Recommended chapter architecture

If I were implementing the rewrite, I would use this final structure:

1.  **Working with Data in R**
2.  **Learning Objectives**
3.  **5.1 One Folder Per Project**
4.  **5.2 Paths, and Why `setwd()` Is a Trap**
5.  **5.3 File Names**
6.  **5.4 Packages**
7.  **5.5 The Tidyverse**
8.  **5.6 Reading Data from CSV**
    -   Viewing and Inspecting the Data
    -   Viewing Data in Positron
9.  **5.7 Summary Statistics in R**
    -   Missing Values
10. **5.8 Tidy Data**

-   Recognizing Untidy Data

11. **5.9 Column Names**
12. **5.10 Putting the Workflow Together**
13. **5.11 Test Bank Sample**
14. **5.12 Practice Exercises**

The principal subtraction is the actual pivoting syntax. Everything else
is mostly tightening, sequencing, and reinforcing the workflow.
