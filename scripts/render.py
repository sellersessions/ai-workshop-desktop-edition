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
import sys
import html
import shutil
import tempfile
import subprocess
import datetime
import zoneinfo

from deckfit import split_body

SHELL = os.environ["DECK_SHELL"]
TITLE = os.environ["DOC_TITLE"]
SUBTITLE = os.environ["DOC_SUBTITLE"]
KICKER = os.environ["DOC_KICKER"]
META = os.environ.get("DOC_META", "")
SOURCE = os.environ["DOC_SOURCE"]
# When DOC_OUT is set the script prints the PDF itself, refitting any section
# that runs past one page. Without it the HTML still goes to stdout as before.
OUT = os.environ.get("DOC_OUT")
CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
MAX_PASSES = 6

now = datetime.datetime.now(zoneinfo.ZoneInfo("Europe/London"))
gen_date = now.strftime("%-d %B %Y")


MERMAID_FENCE = re.compile(r"```mermaid\n(.*?)```", re.S)
MERMAID_INIT = re.compile(r"^%%\{init:.*?\}%%\s*$", re.M)


def extract_mermaid(markdown):
    """Pull mermaid fences out before pandoc runs, so they survive as diagrams
    rather than arriving in the PDF as a wall of source. Returns the markdown
    with placeholders, plus the diagram sources in order."""
    diagrams = []

    def take(match):
        source = MERMAID_INIT.sub("", match.group(1)).strip()
        diagrams.append(source)
        return "\n\nMERMAIDSLOT%d\n\n" % (len(diagrams) - 1)

    return MERMAID_FENCE.sub(take, markdown), diagrams


def md_to_html(markdown):
    """Convert a markdown fragment with pandoc, then apply the deck's classes."""
    markdown, diagrams = extract_mermaid(markdown)
    out = subprocess.run(
        ["pandoc", "-f", "gfm", "-t", "html5"],
        input=markdown, capture_output=True, text=True, check=True).stdout
    out = out.replace("<table>", '<table class="grid">')
    # Pandoc emits GitHub task boxes as disabled checkboxes. A printed page
    # cannot be ticked, so the box becomes a plain bullet.
    out = re.sub(r'<input[^>]*type="checkbox"[^>]*>\s*', "", out)
    for index, source in enumerate(diagrams):
        out = out.replace(
            "<p>MERMAIDSLOT%d</p>" % index,
            '<pre class="mermaid">%s</pre>' % html.escape(source))
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


def build_page(parts_per_section):
    """Render the whole deck. Returns the HTML and, for each slide after the
    cover, the index of the section it came from, so an overflowing slide can
    be traced back to the section that needs dividing."""
    pending, owners = [], []
    for index, (heading, body) in enumerate(sections):
        # The opening section sits above the first `##`, so it borrows the
        # subtitle rather than arriving on the page with no header at all.
        base = heading or SUBTITLE
        for part_number, part in enumerate(split_body(body, parts_per_section[index])):
            title = base if part_number == 0 else base + " (continued)"
            pending.append((title, part))
            owners.append(index)

    total = len(pending) + 1
    slides = [cover()]
    for number, (title, body) in enumerate(pending, start=2):
        title_html = ('  <div class="slide-kicker">%s</div>\n  <h2 class="slide-title">%s</h2>\n'
                      % (html.escape(KICKER), html.escape(title)))
        slides.append('<section class="slide">\n%s%s\n%s</section>\n'
                      % (title_html, md_to_html(body), footer(number, total)))

    page = open(SHELL, encoding="utf-8").read()
    page = page.replace("<<SLIDES>>", "".join(slides))
    for key, value in {
        "DOC_TITLE": TITLE + ": " + SUBTITLE,
        "AUTHOR": "Danny McMillan",
        "DESCRIPTION": SUBTITLE,
        "TAGS": "AI Workshop, Claude Desktop, Seller Sessions",
        "GEN_DATE_ISO": now.strftime("%Y-%m-%d"),
        "MERMAID_JS": "file://" + os.path.join(os.path.dirname(os.path.abspath(SHELL)),
                                               "vendor", "mermaid.min.js"),
    }.items():
        page = page.replace("<<%s>>" % key, html.escape(value))
    return page, owners


def print_pdf(page, destination):
    handle, path = tempfile.mkstemp(suffix=".html")
    with os.fdopen(handle, "w", encoding="utf-8") as f:
        f.write(page)
    try:
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--no-sandbox",
             "--allow-file-access-from-files", "--virtual-time-budget=20000",
             "--no-pdf-header-footer", "--print-to-pdf=" + destination,
             "file://" + path],
            check=True, capture_output=True)
    finally:
        os.unlink(path)


# A4 at 96dpi. A slide taller than this runs onto a second sheet.
PAGE_PX = 1123

PROBE = ("<script>setTimeout(function(){var o=[];"
         "document.querySelectorAll('.slide').forEach(function(s,i){"
         "o.push(i+':'+Math.round(s.getBoundingClientRect().height))});"
         "document.title='MEASURE '+o.join(',')},2500)</script>")

MEASURED = re.compile(r"MEASURE ([^<]*)")


def unwrap_print_css(page):
    """Promote the @media print rules to ordinary CSS, so an on-screen
    measurement renders exactly what the printer will lay out."""
    key = "@media print{"
    start = page.find(key)
    if start < 0:
        return page
    index, depth = start + len(key), 1
    while index < len(page) and depth:
        if page[index] == "{":
            depth += 1
        elif page[index] == "}":
            depth -= 1
        index += 1
    return page[:start] + page[start + len(key):index - 1] + page[index:]


def measure(page):
    """Slide heights in pixels, diagrams drawn, under the print stylesheet."""
    probe = unwrap_print_css(page).replace("</body>", PROBE + "</body>")
    handle, path = tempfile.mkstemp(suffix=".html")
    with os.fdopen(handle, "w", encoding="utf-8") as f:
        f.write(probe)
    try:
        dom = subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--no-sandbox",
             "--allow-file-access-from-files", "--virtual-time-budget=20000",
             "--window-size=794,1123", "--dump-dom", "file://" + path],
            capture_output=True, text=True).stdout
    finally:
        os.unlink(path)
    found = MEASURED.search(dom)
    if not found:
        return []
    heights = {}
    for item in found.group(1).split(","):
        position, _, value = item.partition(":")
        heights[int(position)] = int(value)
    return [heights[k] for k in sorted(heights)]


if not OUT:
    print(build_page([1] * len(sections))[0])
    sys.exit(0)

parts_per_section = [1] * len(sections)
page, owners = build_page(parts_per_section)
for attempt in range(MAX_PASSES):
    heights = measure(page)
    if not heights:
        break
    wanted = list(parts_per_section)
    for slide, height in enumerate(heights):
        if slide == 0 or height <= PAGE_PX + 2:
            continue  # the cover is fixed, and this slide already fits
        sheets = -(-height // PAGE_PX)
        section = owners[slide - 1]
        wanted[section] = max(wanted[section], parts_per_section[section] + sheets - 1)
    if wanted == parts_per_section:
        if any(h > PAGE_PX + 2 for h in heights[1:]):
            sys.stderr.write(
                "fit: %s has a slide that cannot be divided further\n" % OUT)
        break
    parts_per_section = wanted
    page, owners = build_page(parts_per_section)
else:
    sys.stderr.write("fit: %s still spills after %d passes\n" % (OUT, MAX_PASSES))

print_pdf(page, OUT)
