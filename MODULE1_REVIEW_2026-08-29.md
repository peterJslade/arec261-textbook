# Module 1 review -- 2026-08-29

Three Fable reviewers over module01a/b/c as committed today (all videos placed, workbooks with embedded practice sheets, mod01_descriptives.xlsx): one on content, one on aesthetics (rendered pages at desktop 1280px and mobile 390px, every tile read), one on embeds, videos and download links.

## Combined must-fix list

1. **Every SharePoint embed shows a Microsoft sign-in wall to anonymous visitors** -- all 9 unique embed URLs, including the Module 4 one whose anonymous link was verified working on Aug 24, so this looks account/tenant-level (USask may have expired or disabled "Anyone" links), not per-workbook. First step: open one embedview URL in a fresh incognito window; if walled, recreate the Anyone/Can-view links or accept USask sign-in as course policy. Until embeds render, SharePoint staleness against the updated local workbooks is unverifiable.
2. **Prose formulas are offset three rows from every workbook** (text says rows 5-9; workbooks hold data in rows 2-6): module01a Ranges, module01b Conditional and Lookup, module01c Weighted Average, plus stale explanation cells inside mod01_sum and mod01_references.
3. **mod01_descriptives.xlsx Centre tab G4 displays 0**: `=C34/B34` references an empty cell (the production total is in D34).
4. **module01c hail example numbers do not match the figure's data** (recomputed: range 7.5 to 41.3, IQR 2.8 to 3.0 -- not 8.9/40.6/3.4/3.6).
5. **`=MODE.SNGL(A1:A5)` returns `#N/A`** on the chapter's running example (no repeated value).
6. **Display equations overflow the mobile viewport in module01c**, forcing sideways scroll on every page of the chapter (CSS fix: overflow-x auto on display MathJax containers).
7. **The italic "I suggest videos over text for this section!!" note** opening PivotTables reads as a draft annotation left in the published page.

---

# Content review

## Verdicts

**module01a (Getting Started with Excel).** The Excel mechanics are essentially all correct (references, $-locking, formats, PEMDAS, COUNT/COUNTA, menu paths), and the pacing suits a true beginner. Its biggest defect is that every range formula in the Ranges and Functions section cites rows 5-9 while the actual `mod01_sum.xlsx` data sits in rows 2-6, so nothing a student reads matches what they see in the embedded sheet. There is also a verbatim-duplicated COUNT/COUNTA passage and a couple of typos.

**module01b (Working with Data).** Function semantics (IF, COUNTIF family, argument order of the plural forms, XLOOKUP first-match behaviour, filter/formula interaction, sort behaviour, shortcuts) are all factually right, and the pivot workbook genuinely matches the prose (14,700 rows, Barley + Risk_Zone filters, Average of Yield by Variety x Year). The same row-offset disease infects the conditional and lookup sections, including a flatly wrong "rows 15-20" pointer, and the sorting workbook has grown a duplicate row that contradicts both the prose and the screenshots. A few voice-rule violations (unspaced em-dashes, one pull-quote closer) need sanding.

**module01c (Describing Data).** The statistics are conceptually sound -- weighted average, .INC percentile interpolation, n-1 variance, CV caveats, and the mean/median skew heuristic are all correctly stated, and the 52.5 vs 52.0 weighted-average numbers verify against the workbook data. But three numeric/functional errors will bite students directly: the workbook's weighted-average cell computes 0 (`=C34/B34` references an empty cell), the hail-example range/IQR numbers don't match the figure's actual data, and `=MODE.SNGL(A1:A5)` returns `#N/A` on the running example. The descriptives workbook also uses legacy function names the text explicitly tells students not to use, and carries several garbled explanation cells.

## Findings

1. **[must-fix] All three chapters, multiple sections -- prose formulas are offset three rows from every workbook.** The workbooks put data in rows 2-n; the prose was written for data starting in row 5. Concretely: module01a Ranges (`=SUM(B5:B9)`, `=AVERAGE(B5:B9)`, `=SUM(B5:B9,40)`, `=SUM(B5:D5)` vs. workbook `B2:B6`/`B2:D2`); module01b Conditional (`B5:B12`, `C5:C12`, `D5:D12`, "if B6 and B8 both contain Canola" vs. workbook `B2:B9` with Canola in B2/B4/B7); module01b Lookup (`=XLOOKUP(B11, $A$5:$A$7, $B$5:$B$7)` vs. workbook `=XLOOKUP(B8,$A$2:$A$4,$B$2:$B$4)`); module01c Weighted Average ("acres in `B5:B9` and yields in `C5:C9`", `=SUMPRODUCT(C5:C9, B5:B9)/SUM(B5:B9)` vs. `B2:B6`/`C2:C6`). Two workbook explanation cells carry the same stale offset: `mod01_sum.xlsx` E13 says "Straight across row 5" for `=SUM(B2:D2)`, and `mod01_references.xlsx` "Rel ref" A8 says "write B5*C5 in cell D5 and copy into D6-D9" when the formulas are in D2-D6. Fix: pick one convention (workbooks as-built) and rewrite every prose/explanation range to match.

2. **[must-fix] module01c Central Tendency workbook -- the Wtd Average cell computes 0.** `mod01_descriptives.xlsx`, Centre tab, G4 is `=C34/B34`, but C34 is empty (the production total is in D34), so the displayed weighted average is 0 and contradicts the SUMPRODUCT version directly below it in G5. Fix: change G4 to `=D34/B34`.

3. **[must-fix] module01c Range -- the hail-example numbers don't match the figure's data.** Prose: "increases the range from 8.9 to 40.6 bu/ac -- more than quadrupling it" and IQR "from 3.4 to 3.6". Recomputing from `R/strip_plot.R` (seed 262, `head(sort(yields_tight), -1)` plus the highlight at 3): range goes 7.5 to 41.3, IQR 2.8 to 3.0. Fix: recompute and replace all four numbers ("more than quintupling", strictly).

4. **[must-fix] module01c Mode -- the given Excel formula errors on the running example.** The chapter's A1:A5 dataset (48, 52, 47, 55, 50) has no repeated value, so `=MODE.SNGL(A1:A5)` returns `#N/A`. A student who tries the formula on the data just used for AVERAGE and MEDIAN gets an error. Fix: switch the mode example to a small dataset with a repeat, or state that this particular dataset has no mode and show what `#N/A` means.

5. **[should-fix] module01b Sorting -- `mod01_sorting_filtering.xlsx` contains a duplicated data row.** Rows 6 and 10 of both sheets are identical (Rented, Wheat, 400, 61.3), giving nine rows where the prose says "the same eight fields as before" and where the screenshots (`sort_result.png`, `filter_applied.png`) show eight. Fix: delete row 10 in both sheets.

6. **[should-fix] module01c Weighted Average -- claim about mod01_sum is false.** "The workbook in @sec-sum already does this the simple way, dividing total bushels by total acres" -- `mod01_sum.xlsx` totals acres (B7) and bushels (D7) but has no cell dividing them. Fix: add a `=D7/B7` weighted-yield cell to the workbook, or drop the sentence.

7. **[should-fix] module01c -- descriptives workbook uses legacy function names the text forbids.** The text teaches `MODE.SNGL`, `STDEV.S`, `QUARTILE.INC` and says "(the one we use in this course)" about `.INC`, but the Centre/Spread tabs use `=MODE(...)`, `=STDEV(...)`, `=QUARTILE(...)` -- and the FORMULATEXT columns display those legacy names to the student. Fix: update the workbook formulas to the modern names.

8. **[should-fix] module01c -- garbled and mislabeled workbook text.** Location tab E2 is headed "Central tendecy of yields" (wrong heading and typo -- should be "Location of yields"); Location E8: "These numbers represent is the location..."; Location E14/Spread E10: "casuation", "the type of farmers that grown them", "But is could also be due"; Centre F2 repeats "tendecy". Also `mod01_cell_formatting.xlsx` has a stale note (D6: "The cell holds 1000..." when the cell holds 0.5), row labels "B12*2" for formulas that are `=B6*2`, and "mutiplty"; `mod01_references.xlsx` Contents has "Spreadseet". Fix: sweep the explanation cells.

9. **[should-fix] module01a/b -- prose typos.** module01a line 3 "licesned", line 20 "everythign"; module01b line 25 "seperated".

10. **[should-fix] module01a Ranges and Functions -- the COUNT/COUNTA point is made twice.** Lines 211-214 and 231-234 duplicate each other -- a say-it-once violation and an editing leftover. Fix: merge into one paragraph (keep the blank-cell-is-not-zero point, which appears only in the second).

11. **[should-fix] module01b Conditional -- "Examples of these functions are in rows 15-20 of the workbook above."** They are in rows 12-16 of `mod01_conditional.xlsx`. Fix the row numbers (or say "under the table").

12. **[should-fix] module01c Percentiles -- the fences formula range matches nothing.** `=QUARTILE.INC(D5:D40,1) - 1.5*(...)` references D5:D40 (36 cells) with no accompanying dataset; the workbook's barley yields are in C2:C33 (32 values). Fix: use C2:C33 so a student can paste it into the Location tab and get an answer.

13. **[consider] module01b PivotTables -- cross-reference points at the wrong content.** "Give it a title and label the axes as you would any chart (@sec-charts)" -- @sec-charts is module01c's histogram section, which teaches neither. Point at the Module 4 charts chapter or drop the parenthetical.

14. **[consider] Voice: em/en-dashes.** module01b line 135 unspaced em-dashes; line-175 heading "Other resources—lookup functions" breaks the spaced pattern; module01c lines 339 and 359 use spaced en-dashes. Per CLAUDE.md, use spaced `--`.

15. **[consider] Voice: pull-quote closer and a "trips-up" tell in module01b.** "An average of four observations and an average of four hundred look identical until you show the count" is the punchy final one-liner the guide bans. "The argument order is different from `AVERAGEIF`, which catches people out" -- delete the warm-up clause and state the order.

16. **[consider] module01b IF -- the opening example undercuts itself.** `=IF(D5>50, D6, "No")` returns a number when true and text when false, then the next sentence says the workbook labels fields "Yes"/"No" -- and the workbook formula is `=IF(D2>50,"Yes","No")`. Use the Yes/No formula as the first example and show the cell-reference return as a noted variant.

17. **[consider] module01c Standard Deviation -- a non sequitur and a blurred definition.** "This means that roughly on average the yields of any given variety are around 8 bu/acre different from the mean" -- "variety" appears from nowhere, and the sentence restates the MAD interpretation for the SD right after the chapter distinguished the two. Rewrite hedged about the region's yields, or cut.

18. **[consider] module01c Spread -- "all five measures" miscounts.** The section presents six measures (range, IQR, MAD, variance, SD, CV); the Spread tab shows five (no MAD). The learning objectives also omit IQR and MAD. Say "the five measures Excel computes directly" and add IQR to the objectives.

Verified as correct (no action needed): the 188-acre mean, 52.5 vs 52.0 weighted average, 87 grade example, `1+(n-1)p` .INC position and the 3.25 worked case, the CV comparison numbers, fig-shape's identical means/ranges, the pivot workbook's structure against the prose, the three histogram charts, Ctrl+Shift+L / Cmd-Shift-F, and the Data > Get Data > From Text/CSV advice.

---

# Aesthetics review

Method note: the apparent "chapter restarts mid-page" in the mobile captures of 01b/01c was a screenshot-stitching artifact -- scroll-position screenshots confirm the real pages are continuous, so it is not reported. All 60 tiles reviewed (desktop and mobile, three chapters); tiles kept in the session scratchpad (m1review/).

## Verdicts

**module01a.** Desktop is the cleanest of the three: strong heading hierarchy, comfortable measure, workbook frames and callouts in a steady rhythm, and the two-panel Figure 1.1 sits well. Mobile reflows correctly with no overflow; the only weak spot is the Format Cells dialog screenshot, which shrinks into illegibility because it carries so much empty spreadsheet around the dialog. Ship-ready visually.

**module01b.** Desktop reads well and the six Excel screenshots in the sorting/filtering section are sharp and legible at column width, though that section is figure-dense while every other section is iframe-based -- two visual dialects in one chapter. The italic author's note opening PivotTables looks like a draft annotation left in the published page. On mobile, full-window Excel screenshots compress to ~340px and their toolbars/data become unreadable, and several long formula code lines clip mid-token.

**module01c.** Desktop is good -- equations well set, dot-plot figures clean, callout/workbook rhythm matches 01a. Mobile has the module's only real breakage: display equations overflow the viewport (content 506px wide in a 390px viewport), so the entire page scrolls sideways with a dead white gutter. Orphaned "(a)"/"(b)" subcaptions under panels already titled "A."/"B." add clutter under Figures 3.1 and 3.3.

## Findings

1. **[must-fix] module01c, Mean section and notation aside (mobile).** Display MathJax overflows the mobile viewport (DOM-verified 506px vs 390px), forcing whole-page horizontal scroll chapter-wide. Fix in CSS: `mjx-container[display="true"] { overflow-x: auto; overflow-y: hidden; max-width: 100%; }`, and/or break the two long worked equations into two display lines each.

2. **[must-fix] module01b, PivotTables opening.** Italic note "Note that PivotTables are something that is best understood by seeing it in action -- I suggest videos over text for this section!!" reads as a draft margin-note accidentally published. Delete or recast as a normal sentence pointing at the video callout.

3. **[should-fix] module01c, Figures 3.1 and 3.3.** Panels carry their own in-image titles ("A. Yields spread widely") while Quarto adds orphaned "(a)"/"(b)" sub-labels -- double labeling plus a stray centered "(a)" line. Drop the empty fig-subcap entries or move the titles into real subcaptions.

4. **[should-fix] all chapters, workbook link blocks.** The download/open-online block under the iframes takes three visibly different shapes (single line with dots; stacked lines; single line plus tab name plus trailing sentence), sometimes within one chapter. Standardize one pattern, ideally styled as a footer row of the workbook frame.

5. **[should-fix] section endings.** Most sections end with a four-element stack: tall workbook frame, link lines, video callout bar, resources callout bar. The two near-identical one-line bars back-to-back read as clutter. Consider folding the video into the workbook callout's footer, or combining video + resources into one collapsed callout.

6. **[should-fix] module01b sorting/filtering figures on mobile.** Figures 2.1-2.6 are full Excel-window captures; at 340px the ribbon and cell values are illegible. Re-crop to the data range plus the open menu/panel -- also enlarges the useful pixels on desktop.

7. **[consider] module01a Figure 1.1 panel (b).** The Format Cells dialog is embedded in a mostly-empty spreadsheet window; small on desktop, unreadable on mobile. Crop to the dialog.

8. **[consider] long code lines on mobile (01b IF/AVERAGEIFS examples, 01c fences formula).** Blocks scroll horizontally but clip mid-token with no visible scrollbar. Add a scroll affordance or shorten example ranges so key formulas fit a phone width.

9. **[consider] resource-callout title punctuation.** One bar uses an unspaced em-dash ("Other resources—lookup functions") against the spaced pattern everywhere else.

10. **[consider] module01c dot plots on mobile.** Figures 3.1-3.2 shrink to ~340px; the "mean = 40" annotation and ticks drop below legibility. Re-export with larger relative text or a narrower aspect.

Aside (typos spotted while tiling): "licesned" and "everythign" in module01a's opening; "seperated" in module01b's IF section.

---

# Embeds, videos and downloads review

## Summary table

| Workbook (chapter) | Embed status (anonymous) | SharePoint fresh/stale | Video walkthrough | Download link |
|---|---|---|---|---|
| mod01_excel_operations (01a, Cells & Formulas) | **Sign-in wall** | unverifiable (wall) | **none** | 200 OK |
| mod01_references (01a) | **Sign-in wall** | unverifiable | "Referencing in Excel default" (Peter S) | 200 OK |
| mod01_cell_formatting (01a) | **Sign-in wall** | unverifiable | "Cell formatting" (Peter S) | 200 OK |
| mod01_sum (01a, Ranges & Functions) | **Sign-in wall** | unverifiable | "Functions with ranges" (Peter S) | 200 OK |
| mod01_conditional (01b) | **Sign-in wall** | unverifiable | "Conditional functions in Excel" (Peter S) | 200 OK |
| mod01_lookup (01b) | **Sign-in wall** | unverifiable | "Lookup table explainer" (Peter S) | 200 OK |
| mod01_sorting_filtering (01b) | **no embed at all** | n/a | "Sorting filtering" (Peter S) | 200 OK |
| mod01_wide_long (01b) | **Sign-in wall** | unverifiable | **none** | 200 OK |
| mod01_pivot (01b) | **Sign-in wall** | unverifiable | "PivotTable" (Peter S) | 200 OK |
| mod01_descriptives (01c, x4 embeds) | **Sign-in wall** | unverifiable | 4 videos: "Centrality", "Location", "Spread of data", "histogram" (all Peter S) | 200 OK (was 404; fixed by CI run mid-audit) |

All 11 walkthrough videos resolve via oEmbed and are on the Peter S channel; no duplicate URLs. All 21 external "Other resources" videos also resolve. All 10 download URLs on agdataanalytics.com return 200.

## Findings

1. **[must-fix] All chapters -- every SharePoint embed and "Open online" link shows a Microsoft 365 sign-in wall to anonymous visitors.** Headless Chrome loaded each embedview URL directly (9s wait, screenshot): all 9 unique URLs show "Please sign in to view this file." Critically, the Module 4 graphing embed, whose anonymous link was created 2026-08-24 and verified working then, also shows the wall -- so this is account/tenant-level (USask may have disabled or expired anonymous "Anyone" links), not any one workbook's re-upload. Consequence: sheet-tab freshness of every SharePoint copy is unverified. Fix: confirm in a fresh incognito window; if walled there too, recreate the Anyone/Can-view links and regenerate embed codes, or decide the course accepts USask sign-in. Re-check staleness after.

2. **[should-fix] module01b Sorting and Filtering -- malformed workbook section.** A video callout titled "Video walkthrough of this workbook" with no workbook callout, no embed, no "Open online" link, and the bare download line after the video -- reversing the order used everywhere else. Restructure to match the other sections. (Note: the no-embed layout was a deliberate choice; the ordering inconsistency is the reviewable part.)

3. **[should-fix] Two workbooks with no video walkthrough:** mod01_excel_operations (the first workbook students meet) and mod01_wide_long. Both callouts also use the compact single-line link form without the practice-sheet sentence -- consistent for wide_long (no practice sheet in the file), missing for excel_operations.

4. **[should-fix] All 9 iframes use fixed `width="402"`.** Project convention is `width="100%"`. 402px is especially poor for mod01_pivot (14,700-row Data sheet, years across columns) and the descriptives tabs.

5. **[consider] Repo hygiene:** `textbook_examples/mod01_sort_filter.xlsx` (superseded) and `textbook_examples/mod01_excel_operations - Copy.xlsx` are tracked and deployed with nothing referencing them. `mod01_descriptives.xlsx` has an uncommitted local modification.

6. **[consider] module01c Other resources (Spread):** the "Khan Academy" variance/SD video (WBIRh6F4eaA) is a re-upload on channel "ailabhcmus", not official Khan Academy; mirrors get taken down. Swap for the official upload. (The mean/median/mode link is official.)

7. **[consider] YouTube titles on the channel:** "Referencing in Excel default" carries a stray "default"; "histogram" is lowercase. Cosmetic renames on YouTube; the qmd callout titles follow the convention consistently.

8. **[resolved during audit]** mod01_descriptives.xlsx download 404'd at audit start; a CI run landed mid-audit and it now returns 200. No leftover references to removed practice-twin files.

---

