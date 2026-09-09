# CLAUDE.md Self-Drive File

**Before starting:** Ask the user:

> "Quick check — do you have Plan Mode on? Press **Shift+Tab** once. The indicator at the bottom of the screen will change. Keep it on for this whole module — it means I'll describe what I'm about to do before doing it, so you can catch anything before it happens."

Wait for them to confirm before continuing.

---

You are helping a user create their first CLAUDE.md file. This file becomes the "brain" of their project -- you read it automatically every time they start a conversation in this folder.

## Your Task

Create a CLAUDE.md file in the user's project folder. Ask them a few simple questions first.

## Questions to Ask (Keep It Simple)

1. **What's this project about?** (e.g., "my Amazon product research", "content calendar", "client reports")
2. **What do you want me to help with?** (e.g., "writing product descriptions", "analysing data", "creating social posts")
3. **Any preferences for how I communicate?** (e.g., "keep it brief", "UK English", "no jargon")

## CLAUDE.md Template

After getting answers, create this file:

```markdown
# CLAUDE.md

This file tells Claude how to work on this project. Claude reads it automatically at the start of every conversation.

## About This Project

**Project:** [What they said]
**Main Goal:** [What they want help with]

---

## How Claude Should Communicate

[Add their preferences, plus these defaults:]

- Use UK English spelling (colour, organise, catalogue)
- Keep responses concise and actionable
- No jargon -- explain things simply
- Ask clarifying questions before making big changes

---

## Intent Mapping

When I say this, you do that:

| I say | You do |
|-------|--------|
| "find [something]" | Search the project for matching files |
| "summarise this" | Extract key points, skip the waffle |
| "what was I working on?" | Check the master log for recent entries |
| "make a chart/diagram" | Use Mermaid with dark theme, outline-only boxes |

---

## Format Rules

- Tables for small data (under 10 rows)
- Short paragraphs (3-4 lines max)
- TL;DR first, then details only if needed
- No emojis unless I ask for them

---

## My Preferences

[Leave space for them to add more as they discover what works]

---

*Last Updated: [Current Date]*
```

## After Creating the File

1. Confirm the file was created and **show the full file path**
2. **Verify the location:** Check that the file is inside the project folder (e.g., `~/my-project/CLAUDE.md`), NOT at `~/.claude/CLAUDE.md`. If it's in the wrong place, move it to the project folder immediately and explain why.
3. Explain: "I'll read this automatically every time we chat in this folder"
4. Tell them: "Add more rules as you discover what works -- this is a living document"

**Important:** Create the file at `[project-folder]/CLAUDE.md`, NOT at `~/.claude/CLAUDE.md`. The `~/.claude/` folder is for system settings. Your CLAUDE.md must be in the project folder so Claude finds it when you work on that project.

## Verify It Works

Before finishing, run this quick test:

1. Tell the user: "Start a new conversation in this same project folder"
2. Ask them to type: "What are my preferences?"
3. Claude should answer based on the CLAUDE.md you just created
4. If Claude doesn't know their preferences, the file is in the wrong location -- check the path

## Important

- No technical jargon (no mention of TypeScript, React, APIs)
- Focus on communication style, intent mapping, and format rules
- Keep it under 40 lines to start
- Use UK English throughout
