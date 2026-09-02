# Section 2 — Manitoba Wheat Variety: ranking of E16–E20 vs N16–N20

Criteria: (a) fit to the question-writing rules in CLAUDE.md; (b) coverage of Section 2's
skills (project folders, relative paths, `read_csv`, `glimpse`/`summary`, `$`-statistics,
inspection habits); (c) distinctness within the block; (d) usability as an 8–10 minute
question graded from a submitted script; (e) pedagogical value.

1. **E16** — Widest skill coverage of any question in the block (folder layout, relative-path read, `nrow`/`ncol`/`names`, what a row represents), it is the question that anchors the read for the whole block, and the row-meaning part is the single most valuable habit in Section 2.
2. **E20** — The canonical `$`-statistics question: four statistics, `range()`, and a skew interpretation that is genuinely interesting here because this file skews *left*, the opposite of the canola block, so it cannot be answered by pattern-matching.
3. **N16** — Same statistical machinery pointed at `Acres` instead of yield, where the right skew is a real structural feature of the data (a few huge variety-municipality blocks); the 90th-percentile interpretation part is concrete and the whole thing is comfortably distinct from E20.
4. **E19** — The block's `summary()` question, and the only one that walks the module's inspection checklist end to end; part (c) on whether 4.5 bu/ac is an error teaches "extreme is not wrong", which is the most durable idea in the section.
5. **E18** — The only `glimpse()`/column-type question in the block, so it is close to irreplaceable for type coverage, and it uses the dataset's distinctive `Reported` column well; marked down only because it is nearly all prose with one line of code.
6. **N17** — Best pedagogy of the new candidates: the farm count as a reliability weight beside an average is a real analyst's habit and specific to this dataset; held back by very thin computation (three one-line statistics) for a 8–10 minute slot.
7. **E17** — Strong, distinct path-debugging content (absolute path, spaces, working directory), but every part is a comment and the whole question yields one line of runnable code, which makes it light for the time and awkward to give follow-through marks on.
8. **N19** — Correct and cleanly written, but it is E20's territory with quartiles substituted for mean/median; in a block that already has two centre-and-spread questions it adds the least new skill of the defensible candidates.
9. **N20** — Largely E16 and E17 recombined: relative-path read plus a spaces-in-the-filename hypothetical that duplicates E17(a) almost exactly, then `nrow`/`ncol`, which duplicates E16(c). Little that is not already covered better elsewhere.
10. **N18** — Part (c) rests on a false premise: the same physical acre *does* appear more than once, in a different year, so the reconciliation it asks for cannot be given as stated. Parts (a) and (b) are also the block's weakest, duplicating E16(c) and adding a `sum(Acres)` whose interpretation is unclear.

RANKING: E16,E20,N16,E19,E18,N17,E17,N19,N20,N18
