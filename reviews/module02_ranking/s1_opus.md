# Module 2, Section 1 — ranking of E1-E10 and N1-N10

Criteria: fit to the question-writing rules; coverage of Section 1 skills (vectors, objects, data frames, `$`, basic stats, scripts); distinctness; usability as an 8-10 minute question gradable from a submitted script; pedagogical value.

1. E1 — Data described with units up front, four parts that each do different work (build, vectorise, summarise, weight), and the weighted-vs-plain-mean idea is the best single payload in the section.
2. N4 — Same weighted-average payload as E1 but routed through `data.frame()` and `$`, so it tests object construction and column access too; the closing part is a genuine second-person comparison, not a recall prompt.
3. E2 — The only question that makes students confront units and scale before comparing spreads, and the CV part gives the comparison a real answer; four statistics is honest work for 8-10 minutes.
4. N2 — Mean-vs-median under one hailed field, the central Module 1 idea in R form; part c (recompute without the outlier, compare against the original median) is a concrete second operation rather than a definition check.
5. N8 — Two aligned vectors, elementwise difference and percentage change in one line each, closing on a real judgment about which measure travels across crops; nothing else in the section does change over time.
6. E3 — Students choose the type for each variable rather than being handed it, then assemble a data frame; the quotes question is the type misconception that actually bites.
7. N7 — Run-order failure in a fresh session is exactly what the 20% presentation mark grades, and the rewrite part exercises header-and-comment style; framing is neutral ("here is a script"), not a fictional erring student.
8. E10 — Script rewriting with header and comments plus a spread comparison; solid and directly aligned to the presentation criterion, but the analysis half is a lighter rerun of E2's ground.
9. E8 — Clean data frame build with `nrow`/`ncol`/`names` and `$` access; unglamorous coverage of the inspection verbs, though every part is mechanical with no interpretation.
10. N3 — Price-and-conversion held in named objects, with a verbal what-if about a price change; a better-motivated version of E7, but it and E7 cannot both sit in a ten-question bank.
11. E4 — `quantile()` with a vector of probabilities and the median identity check; correct and useful, but three parts of light work for a full test slot.
12. N6 — Diagnosing a missing-comma syntax error and the quoted-numbers trap; real failures students hit, and it asks only for the corrected line, so the submitted script still runs.
13. E9 — Display-versus-save distinction, which is worth one question in the section; loses ground on the fictional-student framing and on being the third code-reading question here.
14. N9 — `summary()` behaving differently by column type is a good thing to notice, but part c leans on `sum()` of a logical vector, which the bank's vocabulary note does not list.
15. E7 — The price-in-one-object lesson, done more plainly than N3 and without the unit conversion; keep one of the two, and N3 is the fuller version.
16. E5 — Three unrelated lines read for what they print; the `mean(x = ...)` argument-naming point is worth making, but it duplicates E6 and the question is entirely comment-writing with no computation.
17. N10 — `sum(yields * acres)` against `mean(yields) * sum(acres)` is a sharp misconception, but it is E1 part d re-asked as a discussion, and parts b and c both answer "the fields differ in size".
18. N5 — Quartiles then `IQR()`, with a closing part whose answer is "half, by definition"; almost entirely contained in E4 and shorter than a test slot warrants.
19. E6 — Argument naming again after E5, `?sd` as trivia, and part c has the student run `Mean()` deliberately, which halts the very script the presentation mark requires to run top to bottom.
20. N1 — Built on logical-vector comparison and `sum()` of TRUEs, neither in the bank's stated Module 2 vocabulary, and the final part asks the student to restate a definition.

RANKING: E1,N4,E2,N2,N8,E3,N7,E10,E8,N3,E4,N6,E9,N9,E7,E5,N10,N5,E6,N1
