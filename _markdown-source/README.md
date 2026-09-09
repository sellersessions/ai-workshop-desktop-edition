# Markdown source, not part of the course

Learners never open this folder. It holds the markdown behind the reference PDFs
that sit out in the course folders, so those folders show one file per document
instead of two.

## How it works

- Edit the markdown in here.
- Run `scripts/build-pdfs.sh` from the edition root.
- The PDF is rewritten in its course folder, at the matching path.

The paths in here mirror the course exactly, so
`_markdown-source/Module-5-Agents/AGENT-VERSATILITY-DEMONSTRATION.md` builds
`Module-5-Agents/AGENT-VERSATILITY-DEMONSTRATION.pdf`.

## What is not in here

Three kinds of file stay out in the course, because something other than a
reader depends on the exact path:

| Stays in the course folder | Why |
|---|---|
| Each module `README.md` | It is the module's own source, built to `MODULE-N-READ.pdf` beside it |
| `MODULE-N-GIVE-TO-CLAUDE.md` | Handed to Claude by the learner. It has to be there to drag in |
| `amazon-product-research-pipeline/reports/*.md` | The pipeline writes the learner's own run into these exact paths |

Agent files, skill files, `CLAUDE.md` and `WORKSHOP-FEEDBACK.md` also stay put.
Claude reads those, so they are machinery rather than reading material, and they
get no PDF at all.
