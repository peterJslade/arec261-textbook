#!/bin/bash
# Sync the student-facing datasets from the book's practice/data folder into the
# 261_student_view project that Peter opens in Positron. Run from anywhere.
set -e
SRC="$(dirname "$0")/../practice/data"
DST="$(dirname "$0")/../../261_student_view/data"
rsync -av --include="*.csv" --include="*.xlsx" --exclude="*" "$SRC/" "$DST/"
