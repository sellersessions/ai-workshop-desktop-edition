#!/usr/bin/env bash
#
# Build every learner-facing PDF in the Desktop Edition.
#
# Rule that makes this hold (D4): README.md is the source. The PDF is output
# only. Never hand-edit a PDF. Run this script after every README edit.
#
# Design: the deck system used across Danny's packs. Tokens and slide furniture
# are copied verbatim in scripts/deck-shell.html. One `##` section per A4 page,
# cover page first, footer carries the document title, the date and slide x of y.
#
# One module README.md  ->  MODULE-N-READ.pdf in the same folder.
# The landing README.md ->  AI-WORKSHOP-2.0-DESKTOP-EDITION-READ.pdf at the root.
#
# Usage: ./scripts/build-pdfs.sh

set -euo pipefail

EDITION_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SCRIPT_DIR="$EDITION_DIR/scripts"

export DECK_SHELL="$SCRIPT_DIR/deck-shell.html"
CHROME="${CHROME:-/Applications/Google Chrome.app/Contents/MacOS/Google Chrome}"

for tool in pandoc python3; do
  command -v "$tool" >/dev/null || { echo "Missing: $tool"; exit 1; }
done
[ -f "$DECK_SHELL" ] || { echo "Missing deck shell: $DECK_SHELL"; exit 1; }
[ -x "$CHROME" ] || { echo "Missing Chrome: $CHROME"; exit 1; }

WORK="$(mktemp -d)"
trap 'rm -rf "$WORK"' EXIT

build() {
  local md="$1" out="$2" title="$3" subtitle="$4" kicker="$5" meta="$6"
  local html="$WORK/$(basename "$out" .pdf).html"

  export DOC_SOURCE="$md" DOC_TITLE="$title" DOC_SUBTITLE="$subtitle" \
         DOC_KICKER="$kicker" DOC_META="$meta"
  python3 "$SCRIPT_DIR/render.py" > "$html"

  "$CHROME" --headless --disable-gpu --no-sandbox \
    --no-pdf-header-footer --print-to-pdf="$out" "file://$html" 2>/dev/null

  echo "built: ${out#$EDITION_DIR/}"
}

COVER_META="Course|AI Workshop 2.0, Desktop Edition;;Author|Danny McMillan, Seller Sessions;;You need|A Mac or PC and a paid Claude plan"

# Landing page.
build "$EDITION_DIR/README.md" \
      "$EDITION_DIR/AI-WORKSHOP-2.0-DESKTOP-EDITION-READ.pdf" \
      "AI Workshop 2.0" "Desktop Edition: start here" \
      "Seller Sessions | AI Workshop" "$COVER_META"

# Modules. The number comes from the folder name, so Module-000 and Module-00 keep theirs.
for dir in "$EDITION_DIR"/Module-*/; do
  [ -f "$dir/README.md" ] || { echo "skipped, no README: $(basename "$dir")"; continue; }
  folder="$(basename "$dir")"
  number="$(echo "$folder" | cut -d- -f2)"
  name="$(echo "$folder" | cut -d- -f3- | tr '-' ' ')"
  build "$dir/README.md" \
        "$dir/MODULE-$number-READ.pdf" \
        "Module $number" "$name" \
        "AI Workshop 2.0 | Module $number" "$COVER_META"
done

# ---------------------------------------------------------------------------
# Everything else the learner reads. Same design system, same furniture.
#
# Out of scope on purpose:
#   *-GIVE-TO-CLAUDE.md   handed to Claude, never read by the learner (D3)
#   agent and skill files, CLAUDE.md, PIPELINE-CONDUCTOR, the questionnaire,
#   WORKSHOP-FEEDBACK.md  Claude reads these, a PDF would only cause confusion
#   .Archives             frozen (builder rule 6)
# ---------------------------------------------------------------------------

# Source markdown for these docs lives in _markdown-source/, mirroring the
# course paths. The PDF is written back into the course folder, so learners
# see one file per document and the markdown stays available for editing.
SRC_DIR="$EDITION_DIR/_markdown-source"

doc() {
  local rel="$1" label="$2"
  local md="$SRC_DIR/$rel"
  local dir base title
  [ -f "$md" ] || { echo "skipped, no source: $rel"; return; }
  dir="$EDITION_DIR/$(dirname "$rel")"
  base="$(basename "$md" .md)"
  title="$(grep -m1 '^# ' "$md" | sed 's/^# //')"
  [ -n "$title" ] || title="$base"
  build "$md" "$dir/$base.pdf" "$title" "$label" "AI Workshop 2.0 | $label" "$COVER_META"
}

doc_inplace() {
  local md="$1" label="$2"
  local dir base title
  dir="$(dirname "$md")"
  base="$(basename "$md" .md)"
  title="$(grep -m1 '^# ' "$md" | sed 's/^# //')"
  [ -n "$title" ] || title="$base"
  build "$md" "$dir/$base.pdf" "$title" "$label" "AI Workshop 2.0 | $label" "$COVER_META"
}

doc "QUESTION-HELPER.md"                                   "Course reference"
doc "PROBLEM-SOLVING-FRAMEWORK.md"                         "Course reference"
doc "Module-00-VS-Code-Optional/COPILOT-CHEATSHEET.md"     "Module 00 reference"
doc "Module-5-Agents/AGENT-VERSATILITY-DEMONSTRATION.md"   "Module 5 reference"
doc "Module-5-Agents/YOUR-WORKFLOW-BEHAVIORAL-PATTERNS.md" "Module 5 reference"

for md in "$SRC_DIR/Module-5-Agents/AGENT-TESTS-AMAZON-SUB-AGENTS"/*.md; do
  [ -e "$md" ] && doc "${md#$SRC_DIR/}" "Module 5 worked example"
done

for md in "$SRC_DIR/Module-5-Agents/amazon-product-research-pipeline/example"/*.md; do
  [ -e "$md" ] && doc "${md#$SRC_DIR/}" "Pipeline worked example"
done

# reports/ stays in the course folder: PIPELINE-CONDUCTOR writes the learner's
# own run into these exact paths, so the markdown is machinery, not an archive.
for md in "$EDITION_DIR/Module-5-Agents/amazon-product-research-pipeline/reports"/*.md; do
  [ -e "$md" ] && doc_inplace "$md" "Pipeline sample report"
done

for md in "$SRC_DIR/ADDITIONAL-RESOURCES"/*.md \
          "$SRC_DIR/Module-3-Slash-Commands/ADDITIONAL-RESOURCES"/*.md; do
  [ -e "$md" ] && doc "${md#$SRC_DIR/}" "Additional resources"
done

echo "done"
