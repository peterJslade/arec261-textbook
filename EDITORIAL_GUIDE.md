# Editorial Guide for the AREC 261 Textbook

This guide defines the teaching, organization and prose style of the AREC 261 textbook. It is intended for human and AI writers, reviewers and editors. Read it together with the project instructions in `../CLAUDE.md`. The project instructions govern files, Quarto, code execution and other implementation details; this guide governs what a chapter should teach and how it should read.

The best current models are Chapters 1--6, especially:

- the "Measures of Spread" section in `module01c.qmd` for Peter's explanatory voice;
- "Ranges and Functions" in `module01a.qmd` for moving from a simple problem to a workbook;
- the openings of `module03c.qmd`, `module04a.qmd` and `module05a.qmd` for establishing a concrete analytical problem;
- the silent join failure in `module05a.qmd` for teaching through a plausible mistake;
- `module06b.qmd` for reader-centred organization and economical examples.

These chapters are reference points, not untouchable templates. Copy their teaching choices, not every sentence or structural habit.

## 1. Purpose and reader

The book replaces traditional lectures in a first undergraduate course in agricultural data analysis. A student should be able to learn from it while working at a computer, without an instructor narrating every page.

Assume that the reader:

- has limited experience with data analysis;
- may have used Excel but does not understand it systematically;
- is new to R and programming;
- knows some agriculture, but not every crop, institution or unit used in an example;
- wants to know what to do, but also needs to understand why the procedure answers the question;
- will be assessed on calculation, interpretation and communication.

Write to a capable student who is stuck. Do not write to an imagined careless student who must be persuaded to pay attention.

The book should help students develop four habits:

1. Start with a question or decision, not a software feature.
2. Inspect data and calculations rather than trusting plausible output.
3. Keep work reproducible and understandable to another person.
4. Explain the result in plain language, with the relevant limits.

## 2. The organizing principle

Organize material around the work of analysis:

> question or problem -> data -> method -> check -> interpretation -> communication

Not every chapter needs every stage, but the sequence should remain visible across the book. Excel and R are tools within this process, not two separate subjects.

Before drafting a chapter, write a brief containing:

- **Chapter promise:** one sentence stating what problem the chapter helps the student solve.
- **Before and after:** what the student can do before the chapter and what they can do afterward.
- **Essential ideas:** no more than four.
- **Anchor task:** the dataset, question, decision or product that carries the chapter.
- **Required artifacts:** data, workbook, R script, figures and console output.
- **Boundaries:** material deliberately left to another chapter.
- **Connections:** what the chapter uses from earlier chapters and what later work depends on it.

Resolve the brief and section order before drafting full prose. If a section cannot be connected to the chapter promise, move it, cut it or change the promise.

## 3. Two useful chapter shapes

Do not impose one rigid template on every topic. Chapters 1--6 use two shapes particularly well.

### Concept or judgment chapter

Use this for statistics, graphing principles, AI judgment, reporting and similar subjects.

1. Present a concrete comparison, result or failure.
2. Name the concept needed to understand it.
3. Explain the concept in ordinary language.
4. Show how it changes an interpretation or decision.
5. Give the calculation, code or workbook when needed.
6. State the important limitation or failure case.
7. Let the section stop when the explanation is complete.

The opening of `module04a.qmd` is a useful model. It shows two charts, explains what each permits the reader to see, and arrives at two jobs of a chart: make comparison easy and represent the data honestly. It does not begin with a list of chart types or a claim that graphing is important.

The "Measures of Spread" section in `module01c.qmd` follows the same logic. Two sets of yields have the same mean but look different. That creates a need for a measure of spread before the measures are introduced.

### Tool or workflow chapter

Use this for Excel functions, importing data, `dplyr`, joins and similar procedures.

1. State the task in terms of the data.
2. Show the input and desired result.
3. Introduce the smallest tool that performs the task.
4. Work through a tested example.
5. Show the actual result.
6. Check for the error most likely to remain unnoticed.
7. Connect the procedure to the larger analytical workflow.

The opening of `module03c.qmd` is a useful model: yield and precipitation arrive in different tables, and answering one question requires two merges. The chapter then names the tables, keys and sequence of operations. The software follows the problem.

When both Excel and R appear, organize them around the same analytical task. Make the relationship explicit: what remains the same, what differs, and what each implementation lets the student inspect. Avoid writing two independent tutorials that happen to share a chapter.

## 4. Voice

The register is an instructor explaining something to a student across a desk. It is direct, slightly informal and willing to express a real judgment. It is not promotional, literary or relentlessly polished.

### Write plainly

Prefer short, undecorated sentences and familiar verbs. Technical terms are necessary; ornamental language is not.

Good:

> The range is easy to understand, but it is very sensitive to extreme values -- a single unusual observation can change it dramatically.

Avoid converting this into a more polished sentence with heightened adjectives, a metaphor or a memorable final beat.

### Explain before naming every detail

Begin with what the student is trying to understand. Introduce terminology when it gives the student a useful name for an idea already in view.

Good:

> Two datasets can have the same mean but look very different.

The sentence creates the problem that measures of spread solve. "This section introduces measures of spread" merely announces the section.

### Use first person only for Peter's real views

First person is welcome when it reflects an opinion, experience or decision Peter actually holds. Examples from his writing include "This course is my attempt to help you" and "I have always found that data analysis is best learnt by doing."

An AI writer must not invent confessions, preferences or stories for him. Draft the underlying point without first person and let Peter decide whether to own it.

### Allow ordinary endings

End a section on its final piece of substance. "Use the coefficient of variation with caution" is enough. Do not add a short sentence designed to sound conclusive.

Read every final sentence by itself. If it resembles a slogan or pull-quote, cut it.

### Say things once

Do not preview a point, explain it, restate it and summarize it. Repetition is useful when a presentation audience cannot reread, or when a difficult idea is being approached in a genuinely different way. It is not a default chapter structure.

### Preserve some looseness

Clarity matters more than symmetry. Do not balance every sentence, turn every set into three items or polish all variation out of the prose. Correct typos and unclear syntax, but do not imitate Peter's typos in an effort to imitate his voice.

## 5. What the prose should do

Each paragraph should normally do one of the following:

- establish a problem or question;
- explain one concept;
- interpret an example or output;
- contrast two choices;
- identify a check, assumption or limitation;
- connect the current task to the analysis around it.

If a paragraph only announces that material is important, congratulates the reader, narrates the existence of the section or repeats its preceding paragraph, delete it.

Use examples to carry explanation. A good example includes enough context to interpret the result: crop or operation, place or population when relevant, year, units and whether the data are observed, illustrative or synthetic.

Agricultural context must affect the analysis. A dataset is not meaningfully agricultural merely because its columns have been renamed `Crop`, `Yield` and `Rainfall`. Use real features of the setting: area-weighted yield, mismatched crop names, rural municipalities, weather-station coverage, mixed units, insured acres, missing harvests or a decision faced by a producer or analyst.

Do not invent current agricultural facts, prices, policies or agency practices. Use a traceable source or clearly label values as synthetic or illustrative. Separate a teaching result from a claim about Saskatchewan agriculture.

## 6. Examples, mistakes and checks

Prefer one continuing example over several disposable examples. Reusing a dataset reduces setup and lets the analytical problem become richer across sections.

A worked example should answer four questions:

1. What are we trying to find out or produce?
2. What does the code, formula or operation do?
3. What result did it produce?
4. How do we know the result answers the intended question?

Teach failures that produce plausible output, not only syntax errors. The silent join failure in `module05a.qmd` is a strong model: the code runs, the number looks reasonable, and most acres disappear because crop names do not match. The lesson is carried by row counts, unmatched keys and the consequence for the reported mean.

Where appropriate, include an explicit check:

- row counts before and after a join;
- missing-value counts before using `na.rm = TRUE`;
- units and category values;
- the range or distribution of a variable;
- several records checked against the source;
- a result calculated a second way;
- formula cells distinguished from typed constants.

Explain what a successful check establishes. "Inspect the data" is not enough; say what the student should inspect and what would indicate a problem.

## 7. Excel

The workbook is part of the teaching, not an attachment added after the prose.

Build and test the workbook before writing the explanation around it. Put worksheet mechanics in the worksheet whenever the student can learn them better there. A worked sheet should normally include:

- a clear purpose or explanation near the top;
- descriptive headings with units;
- formulas visible in their cells;
- a `FORMULATEXT` column when seeing copied formulas is part of the lesson;
- notes beside steps that require explanation;
- consistent distinction among inputs, calculations and outputs;
- source and update information when the workbook uses external data;
- a blank practice version when students are expected to reproduce the work.

The surrounding prose should explain what problem the workbook solves, what to notice and how to interpret or check the result. It should not narrate every click or cell entry already visible in the workbook.

Do not use a Markdown table to imitate a worksheet. Use a Markdown table only when the content is genuinely tabular prose, such as a comparison of file formats or types of reference.

When procedural steps must remain in prose, use them sparingly and test them in the stated Excel version. Explain the consequence of important choices, such as why a left merge is used or why two key columns must be selected in the same order.

## 8. R

Code is teaching text. It should be readable, runnable and connected to visible output.

- Start from a real object and task, not isolated syntax.
- Use meaningful object names that remain stable through the example.
- Comment the purpose of nearly every teaching line, following the comment style in `CLAUDE.md`.
- Show console output close to the code, with the project `console()` helper, except for deliberately non-runnable code.
- Do not hide package messages, parsing notes, warnings or errors when they are part of what a student will encounter.
- Interpret the output in prose. Do not make the student guess why it was shown.
- Keep student-facing paths and downloadable data consistent with the rendered example.
- Use current documented syntax and verify unfamiliar functions against official package documentation.

Prefer a complete script students can keep over disconnected fragments that cannot be run in order. Small fragments are appropriate while introducing a function, but assemble them into a coherent script before the workflow ends.

## 9. Figures, tables and callouts

Every figure and table needs a reason to exist.

- Introduce it before it appears.
- State what comparison or feature the reader should notice.
- Include units, population or groups, time period and exclusions where relevant.
- Use alt text that communicates the important visual information rather than repeating the caption.
- Keep one chart focused on one main point.
- Use a table for exact values and a chart for patterns or comparisons.

Use callouts for material that truly has a different function: a worked model, warning, optional resource or embedded workbook. Do not use them merely to decorate a page or rescue material that does not belong in the main sequence.

External resources should be collapsed and placed after the relevant section. Prefer official documentation and sources that add another explanation or useful detail. A long resource list is not a substitute for teaching the subject in the chapter.

## 10. Headings, objectives and pacing

Headings should describe a meaningful stage in the student's understanding or work. Avoid a heading for every two paragraphs. A short section may have no subheadings.

Learning objectives should state observable abilities. Use verbs such as calculate, distinguish, interpret, construct, check and explain. Avoid "understand," "learn about" and objectives that merely list topics.

The body must deliver what the objectives promise. Before finalizing a chapter, map each objective to the section, example and practice task that teaches it. Remove objectives that the chapter only mentions.

Chapter length follows the intellectual work. Do not pad a short chapter to resemble a long one, and do not compress a difficult concept because neighbouring chapters are shorter. Break a chapter when the student completes one coherent task and begins another.

Transitions should explain a logical dependency, not announce motion. "The yield and precipitation tables use different geographic identifiers, so they need the RM lookup before they can be joined" is useful. "Now that we have covered keys, we will move on to joins" is usually not.

## 11. Mechanical house style

- In `.qmd` files, keep each prose paragraph on one source line.
- Use spaced double hyphens (` -- `), not em dashes (`—`). If a sentence needs two asides, split it.
- Use Canadian spelling where it is natural: colour, centre, analyse.
- Use sentence case in headings.
- Put function names, formulas, object names, file names and literal column names in code formatting.
- Give numbers units wherever the unit is needed for interpretation.
- Distinguish observed, synthetic and illustrative data explicitly.
- Use bold sparingly for terms that the student needs to find again.
- Use links and Quarto cross-references without telling students that they have "met" or "seen" the subject before.
- Keep terminology stable across chapters. Do not alternate casually among dataset, data set, table, worksheet and data frame when the distinction matters.

Project-wide conventions in `CLAUDE.md` take precedence where they are more specific.

## 12. Habits to remove

Delete or rewrite:

- "It's not X -- it's Y."
- rhetorical questions used only as transitions;
- "Here's the thing," "The key insight is" and similar stage directions;
- "Recall that," "You met this before" and "As we learned earlier";
- "This trips up beginners" and its variants;
- instructions about how the student should feel: "Pay attention," "Don't panic," "Learn this now";
- claims that a tool is indispensable, powerful, exciting or widely used unless the claim itself matters and is supported;
- repeated groups of three adjectives or outcomes;
- "worth noting," "worth knowing" and similar filler, except on rare occasions;
- drama words such as "quietly" or "silently" unless literal silence is the technical problem;
- signature phrases such as "earns its keep" or "earns its place";
- a final slogan, maxim or aphorism added after the substantive ending;
- a summary that repeats rather than integrates;
- invented first-person opinions attributed to Peter.

The problem is not that any one phrase is forbidden English. These are reliable signs that the prose is performing confidence or polish instead of explaining the material.

## 13. Drafting and review workflow

Use one writer or managing editor for final prose. Other reviewers should normally return editorial memos rather than replacement chapters.

### Before drafting

1. Approve the chapter brief and outline.
2. Build or obtain the dataset, workbook and code.
3. Run the analysis and record the real output.
4. Identify the central decision, likely misconception and necessary check.

### Drafting

1. Draft around the tested example.
2. Keep each section responsible for one part of the chapter promise.
3. Add objectives after the instructional sequence is stable.
4. Link earlier material only when the connection does work in the current explanation.

### Review passes

Keep the passes separate:

- **Developmental:** Does the sequence make sense, and does every section belong?
- **Novice:** Where does the chapter assume knowledge or skip a reasoning step?
- **Technical:** Do the data, formulas, code, outputs, links and claims work?
- **Pedagogical:** Do explanation, example, practice and assessment ask for the same ability?
- **Continuity:** Are terms, data, units and assumptions consistent across chapters?
- **Line edit:** Can anything be clearer, plainer or shorter without losing meaning?
- **Deletion:** What can be removed without changing what students understand or can do?

A review memo should cite a location, describe the problem and its consequence for the student, recommend **cut**, **move**, **combine**, **clarify** or **expand**, and assign a priority. The managing editor decides which recommendations to accept. Do not mechanically incorporate every comment.

Revise surgically. Do not request a full rewrite when the outline and most prose already work.

## 14. Final chapter check

Before handoff, answer yes or no:

### Purpose and structure

- Can the chapter's promise be stated in one sentence?
- Does the opening establish a real question, comparison, task or problem?
- Does every section contribute to that promise?
- Is the order based on the student's reasoning rather than a catalogue of software features?
- Are repeated concepts taught in one home and only connected elsewhere?

### Teaching

- Does the chapter use a tested anchor example?
- Are important results interpreted rather than merely displayed?
- Does at least one check address a plausible error?
- Are the agricultural context, units and data status clear?
- Do the objectives align with the examples and practice work?

### Artifacts

- Do all code and formulas run or calculate as described?
- Is R console output shown where required?
- Does the workbook teach its own mechanics and expose its formulas?
- Do downloads, links, paths, figures and cross-references work?
- Can reported values be traced to the source data and calculation?

### Prose

- Can any preview, recap or closing sentence be deleted?
- Does each paragraph add a distinct piece of explanation?
- Are headings, bold text and callouts used sparingly?
- Are there invented opinions, promotional claims or instructions about how to feel?
- Does the last sentence of each section end on substance rather than a slogan?
- Does the prose sound like a person helping a student rather than a textbook advertising its own clarity?

## 15. Instructions to give an AI writer

Include the chapter brief, this guide, the relevant preceding and following chapter briefs, the tested artifacts and the sections of `CLAUDE.md` governing implementation. Then use a bounded instruction such as:

> Draft this chapter from the approved brief and tested artifacts. Organize it around the student's analytical task. Use Chapters 1--6 as the house model and follow `EDITORIAL_GUIDE.md`. Explain the decisions and checks; let the workbook or code carry mechanics it can show better. Do not invent facts, outputs, first-person opinions or links. Do not add material outside the brief. Mark unresolved technical or pedagogical questions instead of writing around them.

For revision, identify the exact passages and permitted changes. Prefer:

> Apply the accepted items in this editorial memo. Preserve all other prose and structure. Return a short disposition list and a diff.

Avoid:

> Improve this chapter and incorporate all feedback.

That instruction gives the model no stable definition of improvement and no reason to preserve what already works.
