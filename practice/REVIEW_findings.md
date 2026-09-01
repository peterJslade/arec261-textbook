# Module 1 test bank — agent review findings

Eight agents (Fable and Sonnet on each of the four sections) reviewed the bank
against three criteria: 8–10 minutes per question, coverage of the module
material, and nothing tested that isn't taught. Answer correctness was
deliberately out of scope.

Everything below marked **verified** was checked mechanically against the
chapter sources, not taken on the agents' word.

## Blocking — questions test material Module 1 never teaches

**16 questions use the plural `-IFS` functions.** *(verified: zero occurrences
of `COUNTIFS`, `SUMIFS`, `AVERAGEIFS`, `IFS(` or `COUNTBLANK` across
module01a/b/c; the bank's own vocabulary note at line 20 lists only the singular
forms.)*

Q44, 48, 50, 52, 53, 58, 59, 60, 61, 62, 65, 66, 67, 68, 69, 70

Three sub-cases, in increasing order of seriousness:

1. **Asked outright** (62, 68, 70) — the question text names `SUMIFS`/`AVERAGEIFS`.
2. **Built into the reasoning** (44, 48, 50, 52, 53, 58, 59, 60, 65, 66) — e.g.
   Q59(d) asks the student to explain *why* `COUNTIFS` is needed.
3. **Question says the taught form, answer key silently swaps** (61, 67, 69) —
   the worst case. A student who correctly avoids the untaught function has no
   legal route to the answer, because the task genuinely needs two criteria
   ("canola" AND "2023") and a single-criterion `-IF` cannot do it.

Q48 additionally uses `IFS()`, a different untaught function, where module01b
teaches nested `IF`.

**Two questions use the 1.5×IQR outlier rule.** *(verified: no occurrence of
"1.5" in any Module 1 chapter; module01c covers IQR only as a spread measure.)*
Q19, Q26.

**One question uses z-score reasoning** — Q22(c), "how many standard deviations
the minimum sits below the mean." That is Module 12 material.

**Three questions require building a PivotChart.** *(verified: "PivotChart"
appears zero times in module01a/b/c — the only chart taught anywhere in Module 1
is the histogram.)* Q80, Q89, Q100. Q89 also asks for a chart title and labelled
axes; chart construction is never taught.

**Three questions require a Value Filter** ("varieties with at least 30
reports"). Module01b teaches the Filters box, not value filters on a row field.
Q81, Q87, Q89.

**One question uses concatenated criterion syntax** — Q46, `">"&AVERAGE(E:E)`.
*(verified: zero occurrences in any chapter.)* Q46(e) makes this syntax the
explicit subject of the part.

**Seven questions put two fields into Values at once** (Average + Count
side-by-side): Q75, 81, 84, 85, 87, 91, 97. Module01b shows dragging *a*
variable into Values and changing Summarize Values By, never adding a second.
A small step, but load-bearing in seven questions — one paragraph in module01b
would settle it.

Fixing case 3 needs a design decision, not an edit: either teach `-IFS` in
module01b, or rewrite the tasks so one criterion suffices (pre-filter to a year
on a copied sheet, then plain `AVERAGEIF` — the workaround the module itself
prescribes).

## Coverage gaps — taught but never tested

*(all verified by grepping the bank)*

| Concept | Where taught | Bank |
|---|---|---|
| `ROUND` | module01a:142–149, with a worked example | **0 uses** |
| `COUNT` / `COUNTA` | module01a:182–224 | 3 uses, none in Section 1 |
| Histograms, bin width | module01c `@sec-charts`, a full section | **0 uses** |
| Mean absolute deviation | module01c, named concept | **0 uses** |
| Variance as its own quantity (`VAR.S`) | module01c, taught before SD | **0 uses** |
| Mode | module01c | 4 passing mentions |
| Weighted average | module01c worked example | Section 1 Q5 only |
| Show Values As | module01b:263 | **0 uses** |
| Drill-down (double-click a value) | module01b:264 | **0 uses** |
| Swapping rows/columns | module01b, the defining pivot idea | **0 uses** |
| Order of operations | promised in the Section 1 intro | **0 uses** |
| Nested `IF` | module01b worked example | 0 (Q48 uses `IFS` instead) |
| Sorting | module01b, full subsection | 0 in Section 3 |
| **Filters hide rows from you, not your formulas** | module01b:182, its own section | **0 questions test it** |
| Single-key `XLOOKUP` (the taught core case) | module01b | 0 — all three lookup questions jump to combined keys |
| Wide vs long as a reasoning task | module01b | 0 |

The filtering gap is the one worth pausing on. Module01b gives
"Filters hide rows from *you*, not from your formulas" its own section heading —
it is the most distinctive point in the chapter — and no question in the bank
tests it. Both Section 3 reviewers flagged it independently.

`ROUND` is worth singling out: it was added to module01a at your request, and
the bank never followed.

## Over-representation

*(verified by counting questions, not mentions)*

- **CV** — 18 of 30 Section 2 questions. The chapter itself says to use it with
  caution; the bank makes it the star.
- **Mean-vs-median skew** — 19 of 30 Section 2 questions, usually as the same
  opening move.
- **"Count validates a thin average"** — 7 of the 10 Manitoba questions.
- **"Rate vs total"** — 7 of the 10 Canada Field Crops questions.
- **"Blank ≠ zero"** — 7 questions in Section 3.

## Balance of doing vs explaining

Parts asking the student to explain/state/describe, against parts asking them to
compute something:

| Section | Prose | Compute | % prose |
|---|---|---|---|
| 1 — Building a Worksheet | 5 | 20 | 20% |
| 2 — Descriptive Statistics | 81 | 69 | 54% |
| 3 — Conditional & Lookups | 89 | 61 | 59% |
| 4 — PivotTables | 91 | 59 | 60% |

Both Section 4 reviewers raised this independently. The shape is uniform: build
one pivot, then write four short essays. The prose parts recur near-verbatim
across questions, and several model answers are generic enough to write without
having built the pivot correctly — so roughly 80% of the marks in Section 4
reward reasoning that isn't PivotTable-specific.

This is a question for you rather than a defect: the prose parts may be doing
exactly the work you want, given the course's emphasis on interpretation. But
Section 4 currently tests pivot *construction* in one sub-part out of five.

## Timing outliers

**Too heavy (>12 min):** 13, 18 (worst — four separate filter passes), 20, 23,
30, 43, 58, 64, 91, 93, 97, 100

**Too light (<6 min):** 1, 5, 21, 27, 29, 33, 35, 49, 65, 74, 78, 96, 99

Both Section 1 reviewers flagged Q1 and Q5 sharing a dataset — *(verified: nine
of ten numbers identical)*, so Q5(a)–(b) re-answers Q1(c), and the shipped
answer workbook makes it partly copyable.

## Two decisions only you can make

Most of the fixes above are mechanical once these two are settled, and both
could go either way.

**1. Teach the `-IFS` functions, or rewrite around them?**

Teaching them is the cheaper fix and arguably the honest one: the Canada file is
long-format, so "average canola yield in Ontario" is inherently a two-criterion
problem, and the singular forms genuinely cannot express it. A short passage in
module01b would legitimise 16 questions at a stroke.

Rewriting keeps Module 1's function list small, which was a deliberate choice.
It means reworking the Canada block (61–63, 65–70) around helper columns or the
wide file, and stripping `-IFS` from the rest.

The same question applies, smaller, to PivotCharts (3 questions), value filters
(3), two value fields (7), and concatenated criteria (1).

**2. Is Section 4 meant to test PivotTable skill, or interpretation?**

At 60% prose it currently tests interpretation, and both reviewers judged that
the pivot-building step — one sub-part in five, with the field placement handed
to the student in the question text — is not really assessed. If that is what
you want, the section is fine and the "too light" flags mostly dissolve. If you
want construction assessed, the fix is to stop dictating the recipe: ask for
"average yield by crop for 2023" and let choosing Rows/Filters/aggregation be
the graded skill.

I have not changed anything in the bank. Once these two are settled the rest
follows: remove the 1.5×IQR rule from Q19/Q26 and the z-score from Q22(c), close
the `ROUND`/`COUNT`/histogram/filtering gaps by converting the lightest
questions rather than adding new ones, and give Q5 its own dataset.
