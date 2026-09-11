"""Split an over-long markdown section so every deck slide fits one A4 page.

Used by render.py. A section that runs past one page used to spill onto a
second sheet, and because the footer is pinned to the bottom of the slide box
it landed on the spill page, leaving the first page footerless. Rather than
clip the content, the section is split into parts, each part becoming its own
numbered slide.

Splitting happens at block boundaries. A markdown table is split by row, with
the header and separator repeated on each part, so a long table stays readable
across slides instead of being cut in half.
"""

import re

TABLE_LINE = re.compile(r"^\s*\|")
TABLE_SEP = re.compile(r"^\s*\|[\s:|-]+\|?\s*$")
# A top-level list item: a marker at the left margin. Indented lines below it
# are that item's own continuation and travel with it.
LIST_ITEM = re.compile(r"^ {0,1}(?:[-*+]|\d+[.)])\s+\S")


class ListBlock:
    """A run of list items. Long lists are the other block that has to be
    divisible: one nested list can easily outrun a page on its own."""

    def __init__(self, items):
        self.items = items

    def render(self, items):
        return "\n".join(items)


def _as_list(block):
    """Split a list block into top-level items, or return None if the block is
    not a list."""
    lines = block.splitlines()
    if not lines or not LIST_ITEM.match(lines[0]):
        return None
    items, current = [], []
    for line in lines:
        if LIST_ITEM.match(line) and current:
            items.append("\n".join(current))
            current = [line]
        else:
            current.append(line)
    if current:
        items.append("\n".join(current))
    return ListBlock(items) if len(items) > 1 else None


class Table:
    """A markdown table held as header, separator and rows, so it can be
    divided by row and rebuilt with its header intact on every part."""

    def __init__(self, lines):
        self.header = lines[0]
        self.sep = lines[1]
        self.rows = lines[2:]

    def render(self, rows):
        return "\n".join([self.header, self.sep] + rows)


def _is_table(block):
    lines = [l for l in block.splitlines() if l.strip()]
    return len(lines) >= 2 and TABLE_LINE.match(lines[0]) and TABLE_SEP.match(lines[1])


def raw_blocks(body):
    """Blank-line separated blocks, except that a fenced code block is always
    one block. A blank line inside a ``` fence is part of the code, and cutting
    there would split the fence across two slides and print it as raw text."""
    blocks, current, fence = [], [], None
    for line in body.splitlines():
        stripped = line.strip()
        if fence is None and stripped.startswith("```"):
            fence = stripped[:3]
            current.append(line)
            continue
        if fence is not None:
            current.append(line)
            if stripped.startswith(fence):
                fence = None
            continue
        if not stripped:
            if current:
                blocks.append("\n".join(current))
                current = []
            continue
        current.append(line)
    if current:
        blocks.append("\n".join(current))
    return blocks


def parse_segments(body):
    """Break a section body into blocks, promoting a markdown table into a
    Table and a list into a ListBlock so each can be split by row or item."""
    segments = []
    for block in raw_blocks(body):
        if not block.strip():
            continue
        if _is_table(block):
            segments.append(Table([l for l in block.splitlines() if l.strip()]))
            continue
        as_list = _as_list(block)
        segments.append(as_list if as_list else block)
    return segments


def _atoms(body):
    """Flatten a body into the smallest pieces that may be moved between
    slides: whole blocks, and individual table rows bound to their table."""
    out = []
    for segment in parse_segments(body):
        if isinstance(segment, Table):
            for row in segment.rows:
                out.append((len(row) + 1, ("row", segment, row)))
        elif isinstance(segment, ListBlock):
            for item in segment.items:
                out.append((len(item) + 1, ("row", segment, item)))
        else:
            out.append((len(segment) + 2, ("block", segment, None)))
    return out


def _rebuild(atoms):
    """Turn a run of atoms back into markdown, regrouping consecutive rows of
    the same table under a repeated header."""
    chunks, table, rows = [], None, []

    def flush():
        if table is not None and rows:
            chunks.append(table.render(rows))

    for kind, owner, value in atoms:
        if kind == "row":
            if owner is not table:
                flush()
                table, rows = owner, []
            rows.append(value)
        else:
            flush()
            table, rows = None, []
            chunks.append(owner)
    flush()
    return "\n\n".join(chunks)


def split_body(body, parts):
    """Divide a section body into `parts` slides of roughly equal weight.
    Returns a list of markdown strings, empties dropped."""
    if parts <= 1:
        return [body]
    atoms = _atoms(body)
    if not atoms:
        return [body]

    total = sum(weight for weight, _ in atoms)
    target = total / parts
    buckets = [[] for _ in range(parts)]
    index, seen = 0, 0
    for weight, atom in atoms:
        if index < parts - 1 and seen >= target * (index + 1):
            index += 1
        buckets[index].append(atom)
        seen += weight

    built = [_rebuild(bucket) for bucket in buckets]
    return [b for b in built if b.strip()] or [body]
