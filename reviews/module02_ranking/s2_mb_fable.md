# Section 2 MB (Manitoba Wheat Variety) — ranking, E16–E20 vs N16–N20

1. E16 — The canonical Section 2 question: folder sketch, relative-path read_csv, nrow/ncol/names, and a "what is one row" comment; hits the section's most distinctive skills cleanly and grades directly from the script.
2. E18 — glimpse plus column types, the TRUE-only logical tied to the file's name, and the chr-instead-of-dbl diagnostic; the best pure inspection-habits question in either set, fully distinct.
3. E19 — summary() read-off, the module's plausibility/missing-value inspection questions, and the "is 4.5 bu/ac an error?" judgment call; strong pedagogy, second-person, gradable comments.
4. E17 — The absolute-path/spaces failure diagnosed and rewritten, plus the first-thing-to-check debugging comment; deep on the working-directory friction point, and framed as "your script", within the no-fictional-students rule.
5. E20 — mean/median/sd/var via $ plus range(), with the mean-below-median skew interpretation in Module 1 language; solid $-statistics coverage, stem gives the gap direction so it grades cleanly.
6. N19 — quantile(probs = c(.25, .5, .75)) and IQR are the one vocabulary gap the E block leaves open; part (c)'s "where wheat is dependable" reading stretches what an all-municipality IQR shows, but the question is distinct and worth keeping.
7. N17 — min/mean/max of Farms with a what-is-counted comment and the why-farm-counts-matter reflection; genuinely distinct data-literacy angle that fits this dataset's suppression story, though part (c)'s stem is wordier than the rules want.
8. N16 — Competent $-statistics on Acres with a 90th percentile, but part (b) is the same mean-vs-median skew interpretation as E20(b) with the sign flipped; near-duplicate within the block, so it ranks low despite being usable.
9. N20 — Parts (a) and (c) restate E16 and part (b) restates E17's renaming point, so it duplicates two existing questions at once; worse, the read_csv line for the nonexistent spaces-name file would error in a script that must run top to bottom.
10. N18 — head/names/sum are thin work, and part (c)'s premise is wrong for this file: Acres is summed across 2020–2025, so the same physical acre appears in the total up to six times; the reconciliation the student is asked to write is not true of the data.

RANKING: E16,E18,E19,E17,E20,N19,N17,N16,N20,N18
