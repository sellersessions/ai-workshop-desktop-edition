#!/usr/bin/env python3
"""Turn one module README.md into a designed deck page, ready for print to PDF.

Source of truth is the README (D4). This script never edits content: it splits
the markdown at each `##` heading, gives each section its own A4 slide, and
wraps the result in the shared deck shell.

Called by build-pdfs.sh. Expects these environment variables:
  DECK_SHELL     path to deck-shell.html
  DOC_TITLE      cover title, e.g. "Module 3"
  DOC_SUBTITLE   cover subtitle, e.g. "Slash Commands"
  DOC_KICKER     small uppercase label above each slide title
  DOC_META       three "label|value" pairs for the cover, separated by ";;"
"""

import os
import re
import html
import subprocess
import datetime
import zoneinfo

SHELL = os.environ["DECK_SHELL"]
TITLE = os.environ["DOC_TITLE"]
SUBTITLE = os.environ["DOC_SUBTITLE"]
KICKER = os.environ["DOC_KICKER"]
META = os.environ.get("DOC_META", "")
SOURCE = os.environ["DOC_SOURCE"]

now = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/London"))
gen_date = now.strftime("%-d %B %Y")


def md_to_html(markdown):
    """Convert a markdown fragment with pandoc, then apply the deck's classes."""
    out = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5"],
        input=markdown, capture_output=True, text=True, check=True).stdout
    out = out.replace("<table>", '<table class="grid">')
    # Pandoc emits GitHub task boxes as disabled checkboxes. A printed page
    # cannot be ticked, so the box becomes a plain bullet.
    out = re.sub(r'<input[^>]*type="checkbox"[^>]*>\s*', "", out)
    return out


def split_sections(markdown):
    """[(title, body)] from the `##` headings. Text before the first `##`
    belongs to the opening section."""
    lines = markdown.splitlines()
    sections, title, buf = [], None, []
    for line in lines:
        if line.startswith("## "):
            if title is not None or "".join(buf).strip():
                sections.append((title, "\n".join(buf)))
            title, buf = line[3:].strip(), []
        elif line.startswith("# ") or line.strip() == "---":
            continue  # the H1 lives on the cover, rules are slide edges here
        else:
            buf.append(line)
    if title is not None or "".join(buf).strip():
        sections.append((title, "\n".join(buf)))
    return [(t, b) for t, b in sections if b.strip() or t]


def footer(number, total):
    return (
        '  <div class="slide-footer">\n'
        '    <div class="doc">%s</div>\n'
        '    <div class="date">%s</div>\n'
        '    <div class="num">Slide %d of %d</div>\n'
        '  </div>\n' % (html.escape(TITLE), gen_date, number, total)
    )


def cover():
    rows = ""
    for pair in [p for p in META.split(";;") if p.strip()]:
        label, _, value = pair.partition("|")
        rows += ('    <div><span class="lbl">%s</span><span class="val">%s</span></div>\n'
                 % (html.escape(label.strip()), html.escape(value.strip())))
    return (
        '<section class="slide cover">\n'
        '  <div class="cover-eyebrow">%s</div>\n'
        '  <h1 class="cover-title">%s</h1>\n'
        '  <div class="cover-subtitle">%s</div>\n'
        '  <div class="cover-meta">\n%s  </div>\n'
        '</section>\n' % (html.escape(KICKER), html.escape(TITLE),
                          html.escape(SUBTITLE), rows)
    )


markdown = open(SOURCE, encoding="utf-8").read()
sections = split_sections(markdown)
total = len(sections) + 1

slides = [cover()]
for index, (heading, body) in enumerate(sections, start=2):
    # The opening section sits above the first `##`, so it borrows the subtitle
    # as its heading rather than arriving on the page with no header at all.
    heading = heading or SUBTITLE
    title_html = ('  <div class="slide-kicker">%s</div>\n  <h2 class="slide-title">%s</h2>\n'
                  % (html.escape(KICKER), html.escape(heading)))
    slides.append('<section class="slide">\n%s%s\n%s</section>\n'
                  % (title_html, md_to_html(body), footer(index, total)))

page = open(SHELL, encoding="utf-8").read()
page = page.replace("<<SLIDES>>", "".join(slides))
for key, value in {
    "DOC_TITLE": TITLE + ": " + SUBTITLE,
    "AUTHOR": "Danny McMillan",
    "DESCRIPTION": SUBTITLE,
    "TAGS": "AI Workshop, Claude Desktop, Seller Sessions",
    "GEN_DATE_ISO": now.strftime("%Y-%m-%d"),
}.items():
    page = page.replace("<<%s>>" % key, html.escape(value))

print(page)
