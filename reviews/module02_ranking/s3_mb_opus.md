# Section 3 — Manitoba Wheat Variety: ranking of E26-E30 vs N26-N30

Criteria: (a) fit to the question-writing rules; (b) coverage of Section 3 skills
(`filter` with `==`, comparisons, `&` `|` `!` `%in%`, `select`, `rename`, `mutate`,
`arrange`/`desc`); (c) distinctness within the block *and* against the parallel
Saskatchewan block (Q21-25), since a test draws one question per type and near-clones
of the SK questions waste a slot; (d) usability as an 8-10 minute question gradable
from a submitted script; (e) pedagogical value.

1. **N28** — Compound `&` filter where both conditions mean something: the farm-count threshold is a reliability condition, not an arbitrary number, so the syntax is carrying an idea. Filter, `arrange(desc())`, and a comment part that asks what the second condition adds to a claim -- the most genuinely analytical understanding check in the block, and nothing like it in the SK block.

2. **N30** — The only question in either block that touches the suppressed rows the preamble takes a paragraph to explain. `Reported == FALSE` plus `select` on columns that are deliberately empty, and a comment about why the suppressed rows are kept rather than deleted. Teaches that absent data is itself data; wholly distinct from everything else.

3. **E30** — The strongest of the existing five. `total_bu = Acres * Yield_bu_ac` is a real derived quantity, and part (d) ("what does `total_bu` measure that `Yield_bu_ac` does not") is a properly formed understanding check anchored to the student's own column. Four parts that each do distinct work: mutate, compute, sort, interpret.

4. **N27** — E30's better sibling. `acres_per_farm` is a less obvious derived quantity than acres times yield, and the closing comment asks the student to distinguish two different facts about a variety rather than restate the arithmetic. Same skill coverage as E30 (mutate, arrange, mean, interpret) with a slightly sharper concept; ranks just below only because E30 is already drafted and the two overlap heavily.

5. **N29** — Uses `%in%` where it actually earns its keep (three varieties, not two), pairs it with `select`, and makes the `|` comparison a *verbal* counterfactual ("what would the same filter written as three `==` conditions return?") instead of making the student type the filter twice. That is the rules' preferred shape for a what-if.

6. **E26** — Does the block's necessary setup (`mb_rep`) and covers filter plus select cleanly. Part (c) is half a good idea -- "what happened to the suppressed rows" is worth asking -- and half a confirm-the-count part, which the rules flag as busywork. Solid but not distinctive.

7. **N26** — Clean, well-formed, and the "these rows share one municipality, so what differs between them" comment is a nice grain-of-the-data question. Thin for 8-10 minutes, though: one `filter` on a `==`, one `arrange`, and no second verb. Underweight against the section's "two or three functions in sequence" instruction.

8. **E27** — A near-verbatim clone of SK Q22 (`|`, then the same filter in `%in%`, then "what would `&` return"), with varieties substituted for crops. Part (b) is retyping the same filter a second way, and part (c)'s answer is identical to Q22's. Little new is tested if a student has seen either.

9. **E29** — Clone of SK Q24, and the weakest on the rules: part (a) is the "name what you keep, then drop what you don't, then confirm they match, then do a third range version" pile-up that is exactly the busywork the guidance says to cut. No interpretive part at all -- it ends on `names()`. It does own `rename`, which nothing else in the block covers, but at a poor return for the student's ten minutes.

10. **E28** — Weakest overall. Duplicates SK Q23's filter/re-filter/sort shape without Q23's `!` part, so it is the clone that dropped the one thing making the original worth keeping. Three mechanical parts, no comment part, nothing for the student to understand -- purely "can you run three verbs in order".

RANKING: N28,N30,E30,N27,N29,E26,N26,E27,E29,E28
