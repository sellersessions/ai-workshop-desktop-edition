---
name: web-researcher
description: Research any topic or URL from the web. Returns a structured brief you can use for writing, presentations, or decisions.
allowed-tools: WebFetch,WebSearch,Read,Write
---

# Web Researcher Skill

Research any topic or URL and produce a structured brief. Zero external dependencies -- uses Claude Code's built-in web tools.

## When to Use

- User pastes a URL and wants the content summarised
- User asks to research a topic, competitor, or trend
- User wants background material before writing an article
- User says "research this" or "what does this page say?"

## How It Works

### Step 1: Understand What They Want

If they gave a URL, fetch it. If they gave a topic, search for it. If they gave both, do both.

- **URL provided:** Use WebFetch to pull the page content
- **Topic provided:** Use WebSearch to find the top sources, then WebFetch the best 2-3 results
- **Both:** Fetch the URL first, then search for additional context

### Step 2: Extract Key Information

From the fetched content, pull out:

1. **Main topic** -- what is this about, in one sentence?
2. **Key points** -- 5-8 bullet points covering the most important information
3. **Quotes or data** -- any specific numbers, statistics, or notable quotes
4. **Sources** -- where the information came from (with URLs)

### Step 3: Create the Research Brief

Write a structured brief and save it as a `.md` file in the current folder:

```markdown
# Research Brief: [Topic]

**Researched:** [date]
**Sources:** [number] pages reviewed

## Summary

[2-3 sentence overview]

## Key Points

- [bullet points]

## Notable Data & Quotes

- [any specific numbers, statistics, or quotes worth citing]

## Sources

1. [Title](URL) -- [one-line description]
2. [Title](URL) -- [one-line description]

## Suggested Next Steps

- [What the user might want to do with this research]
```

### Step 4: Show the Result

- Tell the user where the file was saved
- Show a preview of the summary and key points
- Ask: "Want me to dig deeper into any of these points, or shall we write something from this?"

## Rules

- **UK English** spelling throughout
- **Short paragraphs** -- scannable, not walls of text
- **Cite sources** -- always include where information came from
- **Be honest** -- if a source seems unreliable or information is uncertain, say so
- **Save the output** -- always write the brief to a file, don't just display it

## The Content Chain

This skill works perfectly with the Content Research Writer skill:

1. User runs `/web-researcher` to gather material on a topic
2. User says "write an article from that research" or "turn this into a blog post"
3. The Content Research Writer reads the research brief and helps draft content

This is the power of skills working together.
