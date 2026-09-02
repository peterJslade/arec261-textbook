# Section 4 SK ranking — E31-E35 vs N31-N35 (fable)

1. E35 — Fullest coverage of the section's skills in one question (filter, group_by, summarise with n(), arrange, save, write_csv) plus the Unit-column trap, which makes the interpretation part real analysis rather than a recitation.
2. E34 — The filter-mutate-summarise chain is a genuine multi-step pipeline, and part (c) (why summarise before mutate would fail) is the best conceptual check in the block: second-person, anchored to the student's own pipeline, tests order-of-operations understanding directly.
3. N34 — Only question combining mutate with group_by (revenue per acre by year), a four-step pipeline no existing question exercises; the "say what each step hands to the next" comment tests pipeline comprehension well, though it overlaps E34's order theme.
4. E33 — Clean filter-then-group yearly means with a drought interpretation that connects the number to something a student knows; concise, distinct role as the pure group_by question.
5. E32 — Simple but does distinct work: summarise with n() and the why-report-the-count rationale, a habit the rest of the block builds on; light on multi-step depth.
6. N35 — The ascending arrange (worst-first, contrasting desc) and write_csv are good touches, but yearly canola means duplicate E33's core and the write_csv role duplicates E35's; useful mainly as a variant draw.
7. E31 — No summarise or group_by, so weakest on the section's headline skills, but the only select-based pipeline and the read-your-pipeline-aloud check tests the "take the data, then..." mental model the section is built on; fully distinct in the block.
8. N33 — Three statistics in one summarise() with a good sd-across-RMs interpretation, but structurally it is E32 with sd added and no new pipeline skill; the sd interpretation leans back toward Section 2 territory.
9. N31 — Near-duplicate of E35: crop-level means with n(), sorted, topped by the same Unit-column trap and the same "which bushel crop really leads" question; only the all-years scope differs, and it drops write_csv.
10. N32 — Near-duplicate of E33 beat for beat: yearly means of one crop, report best and worst, comment on whether 2021 looks like the drought; swapping canola for barley changes nothing a student learns or a grader sees.

RANKING: E35,E34,N34,E33,E32,N35,E31,N33,N31,N32
