# Section 4 — Saskatchewan RM Crop Yields: ranking of E31-E35 vs N31-N35

Criteria: (a) fit to the question-writing rules; (b) coverage of Section 4's skills -- the pipe, `summarise` with `n()`, `group_by`, multi-step pipelines, `write_csv`; (c) distinctness within the block; (d) usability as an 8-10 minute question gradable from a submitted script; (e) pedagogical value.

1. **E35** — The block's capstone: filter, group_by, summarise with `n()`, arrange and `write_csv` in one chain, and the only question whose interpretive part teaches something the data itself hides (lentils in lb/ac make the first-place row incomparable). Covers the most skills and asks for the quantity, not the recipe.
2. **E34** — filter, mutate, summarise, with the best conceptual part in the block: why `summarise()` before `mutate()` fails. That part tests whether the student understands a pipeline as an ordered handoff rather than a pile of verbs, and it is graded from a written comment.
3. **N34** — The most complete non-`write_csv` pipeline on offer: filter, `mutate()` a revenue column, `group_by(Year)`, summarise. Distinct from E34 (which is ungrouped) and from E33 (which has no mutate); the price hook is agricultural rather than decorative, and part (c) makes the student trace what each step hands to the next.
4. **E33** — Grouped means by year with a genuine external check: 2021 was a real Saskatchewan drought, and the data agrees, so part (c) is an interpretation with a right answer. Clean, tight, well-sized.
5. **N33** — filter then a single `summarise()` carrying mean, sd and `n()`. Part (c) -- variation across what units, over what period -- forces the student to say what one row represents, which is the concept Section 4 actually turns on. Loses ground only because it repeats E32's ungrouped-summarise shape.
6. **E31** — The block's on-ramp: filter, select, arrange with a comment per step and a "take the data, then..." read-aloud. Valuable as the pipe-mechanics question, but it never reaches `summarise` or `group_by`, so it tests less than the others.
7. **E32** — filter then `summarise(mean, n())`, with the count-alongside-the-mean lesson stated well. Sound but thin for 8-10 minutes, and part (b) ("add `n()` to the same summarise") is closer to a recipe than a quantity.
8. **N35** — `group_by(Year)`, summarise, ascending arrange, `write_csv`, and the worst-years question has a real answer (2001-2003 cluster, a genuine drought). But it duplicates E33's grouped-year-canola shape while carrying none of E35's units lesson, so as the block's `write_csv` slot it is the weaker of the two.
9. **N32** — Grouped means by year with the 2021 drought check, barley instead of canola. The numbers work (2021 at 34.8 against 55-73 elsewhere), but it is E33 with the crop swapped and the year window widened -- a near-duplicate that adds no skill.
10. **N31** — Strictly inside E35: same `group_by(Crop)`, same `summarise(mean, n())`, same arrange, same lentils-are-in-pounds insight, minus the year filter and minus `write_csv`. The weaker copy of the block's strongest question, and too short to fill the slot.

RANKING: E35,E34,N34,E33,N33,E31,E32,N35,N32,N31
