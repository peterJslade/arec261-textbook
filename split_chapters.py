#!/usr/bin/env python3
"""Split textbook.qmd into per-chapter .qmd files for Quarto book format."""

import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(BASE_DIR, "textbook.qmd")

# Read source
with open(SOURCE, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Skip frontmatter (between first two --- lines)
start = 0
if lines[0].strip() == "---":
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            start = i + 1
            break

# Find chapter starts: lines beginning with "# " (but not "# " inside a code block)
# We need to detect code fences
chapter_starts = []
in_code_block = False
for i in range(start, len(lines)):
    line = lines[i]
    stripped = line.strip()
    if stripped.startswith("```"):
        in_code_block = not in_code_block
        continue
    if in_code_block:
        continue
    # Real chapter heading
    if re.match(r"^# [^#]", line):
        chapter_starts.append(i)

print(f"Found {len(chapter_starts)} chapter headings at lines: "
      f"{[s + 1 for s in chapter_starts]}")

# Map chapter index to output filename
# Order: Preface, Introduction, Module 1..12, References
filenames = [
    "index.qmd",       # Preface
    "intro.qmd",       # Introduction
    "module01.qmd",
    "module02.qmd",
    "module03.qmd",
    "module04.qmd",
    "module05.qmd",
    "module06.qmd",
    "module07.qmd",
    "module08.qmd",
    "module09.qmd",
    "module10.qmd",
    "module11.qmd",
    "module12.qmd",
    "references.qmd",
]

if len(chapter_starts) != len(filenames):
    print(f"WARNING: expected {len(filenames)} chapters, got {len(chapter_starts)}")

# Add end sentinel
chapter_starts.append(len(lines))

# Write each chapter
for idx, fname in enumerate(filenames):
    if idx >= len(chapter_starts) - 1:
        break
    chapter_lines = lines[chapter_starts[idx]:chapter_starts[idx + 1]]

    # Strip any \newpage lines (irrelevant for HTML book)
    chapter_lines = [ln for ln in chapter_lines if ln.strip() != "\\newpage"]

    # Trim trailing blank lines
    while chapter_lines and chapter_lines[-1].strip() == "":
        chapter_lines.pop()

    out_path = os.path.join(BASE_DIR, fname)
    with open(out_path, "w", encoding="utf-8") as f:
        f.writelines(chapter_lines)
        f.write("\n")
    print(f"Wrote {fname} ({len(chapter_lines)} lines)")

print("Done.")
