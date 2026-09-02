# Section 3 SK — ranking of E21-E25 against N21-N25

Criteria: (a) fit to the question-writing rules in CLAUDE.md; (b) coverage of Section 3's skills
(`filter` with `==`, comparisons, `&` `|` `!` `%in%`, `select` including `-` and `:`, `rename`,
`mutate`, `arrange`/`desc`); (c) distinctness within the block; (d) usability as an 8-10 minute
question gradable from a submitted script; (e) pedagogical value.

All ten were checked against `rm_yields_1990_2025.csv`; every stated filter returns a sensible,
non-empty result and every "top row" is unique except E22's, which is a genuine tie.

1. E23 — Four operators in one arc (`>=`, `&`, a chained re-filter, `select`, `arrange(desc())`) closing on a verbal `!` rewrite; widest skill coverage in the block and every part does distinct work.
2. N22 — Filter, `mutate` with an external price, sort, mean, and a (d) on why revenue rank equals yield rank; the deepest conceptual part in either set, and the only one reaching for a genuinely economic idea.
3. E22 — The `|` / `%in%` equivalence plus the `&`-returns-nothing trap is exactly the contrast the section teaches; docked slightly because the 165.1 bu/ac tie makes the "top row" answer two-valued.
4. E25 — One `mutate()` adding two columns, then "without running anything, what is the ratio of the means" — a model predict-part; loses only for echoing the sample test's conversion question.
5. E24 — The only question anywhere in the block exercising `select` with `-` and with the `:` range, both named in the vocabulary note; part (a) is dense, packing three versions and a comparison into one instruction.
6. E21 — Clean and correctly scoped, and its (c) targets the section's central misconception (filter and select leave the original alone), but it drives only two verbs and no comparison operators.
7. N21 — Two-sided range comparison (`>= & <=`) appears nowhere else, and the "what would `|` return" what-if is sound; the parenthetical hands over the whole answer to (a), against "ask for the quantity, not the recipe".
8. N24 — Tests `rename` properly (four columns at once) and the reversed-argument what-if states a rule worth stating, but it is all column names: no comparison, no `mutate`, no sort, and short of eight minutes.
9. N23 — `%in%` on years with an ascending sort and a nice drought check, but (b) and (c) ask the same thing twice, and (c) is answerable from the stem without running the code.
10. N25 — Structurally a near-clone of E23 (filter a crop, re-filter on a threshold, sort, report) with strictly less coverage, and "report the top three years you see in the table" is vague to grade.

RANKING: E23,N22,E22,E25,E24,E21,N21,N24,N23,N25
