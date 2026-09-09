# Slash Commands Self-Drive File

**Before starting:** Ask the user:

> "Quick check — do you have Plan Mode on? Press **Shift+Tab** once. The indicator at the bottom of the screen will change. Keep it on for this whole module — it means I'll describe what I'm about to do before doing it, so you can catch anything before it happens."

Wait for them to confirm before continuing.

---

**For Claude Code:** When a user gives you this file, help them set up slash commands AND install 3 starter skills by following these instructions.

---

## What You're Creating

Two things:
1. **Slash commands** -- shortcuts stored as `.md` files in `.claude/commands/`
2. **Skills** -- multi-step reasoning files stored in `.claude/skills/`

Think of commands as speed dial, and skills as smart assistants.

---

## Part 1: Slash Commands

### Questions to Ask (Keep It Simple)

Ask these three questions one at a time. Wait for their answer before moving on.

### Question 1: What do you do repeatedly?

> "What tasks do you find yourself asking me to do over and over? For example:
> - Summarise research
> - Update your session log
> - Check your project status
> - Start your morning routine"

**Get 2-3 examples** -- these will become their first commands.

---

### Question 2: What's your working folder?

> "Where are your project files? I'll need to create a `.claude` folder there to store your commands and skills."

**If they're unsure:** Use their current project folder.

---

### Question 3: Pick your first command

> "Let's start simple. Which of these would save you the most time?
>
> 1. `/status` - Quick project health check
> 2. `/log` - Update your session log
> 3. `/research [topic]` - Start research on something
> 4. `/summarise` - Summarise what we just did
>
> Or tell me a custom one you'd like."

---

### Create the Folder Structure

Run these in your terminal first. Claude Code cannot create directories automatically.

```bash
mkdir -p .claude/commands
mkdir -p .claude/skills/find
mkdir -p .claude/skills/web-researcher
mkdir -p .claude/skills/content-research-writer
```

```
[their-project-folder]/
└── .claude/
    ├── commands/
    │   └── [command-name].md
    └── skills/
        ├── find/
        │   └── skill.md
        ├── web-researcher/
        │   └── skill.md
        └── content-research-writer/
            └── skill.md
```

**Important:** Folders must be called `.claude/commands/` and `.claude/skills/` exactly.

---

### Create Their First Command

Based on their choice, create the appropriate command file.

#### If they chose `/status`:

Create `.claude/commands/status.md`:

```markdown
---
description: Quick project status check
---

Give me a quick overview of:

1. What we worked on recently (check the session log if it exists)
2. Any files created or changed today
3. What's next on the to-do list

Keep it brief - bullet points only.
```

#### If they chose `/log`:

Create `.claude/commands/log.md`:

```markdown
---
description: Update the session log
---

Update my Master Session Log with what we just did:

1. Add today's date and time (UK format)
2. Summarise what we accomplished in bullet points
3. Note any decisions made
4. List files created or changed
5. Add next steps

Put the new entry at the TOP of the log (newest first).
```

#### If they chose `/research`:

Create `.claude/commands/research.md`:

```markdown
---
description: Start research on a topic
---

# Research Request: $ARGUMENTS

Research the topic above and give me:

1. **Quick summary** - 2-3 sentences on what this is
2. **Key points** - Bullet list of important facts
3. **Sources** - Where you found this info
4. **Next steps** - What else should I look into?

Keep it scannable - no walls of text.
```

#### If they chose `/summarise`:

Create `.claude/commands/summarise.md`:

```markdown
---
description: Summarise what we just did
---

Summarise our last conversation in this format:

**What we did:**
- [bullet points]

**Key decisions:**
- [bullet points]

**Files involved:**
- [list files]

**Next time:**
- [what to do next]

Keep it under 200 words.
```

---

> **STOP — Restart Claude Code before continuing.**
>
> Slash commands created mid-session are invisible until Claude Code restarts.
> 1. Quit Claude Code completely (Cmd+Q on Mac)
> 2. Reopen Claude Code
> 3. Type `/` — your new command should appear in the list
>
> If it appears: continue to Part 2.
> If it does not appear: check the file is in `.claude/commands/` and ends in `.md`.

---

## Part 2: Install the 3 Starter Skills

After creating their commands, install the 3 skill files from the course module.

Create these files in `.claude/skills/`:

### `.claude/skills/find/skill.md`

A file-finding skill that searches using plain English descriptions. Searches by file name, contents, and type. Returns a scannable list of matches.

### `.claude/skills/web-researcher/skill.md`

A web research skill. Give it a URL or a topic and it fetches content from the web, extracts key points, and saves a structured research brief. No external tools to install -- uses Claude Code's built-in web capabilities.

### `.claude/skills/content-research-writer/skill.md`

A writing partner skill. Give it a topic, some research, or a brief and it helps you outline, draft, and refine content. Works brilliantly after using the web researcher -- the two skills chain together.

**Note:** Each skill lives in its own named subfolder. The file inside must always be called `skill.md`. A flat file like `.claude/skills/find.md` will not be recognised.

**Tell the user:** "I've also installed 3 skills -- `/find`, `/web-researcher`, and `/content-research-writer`. Skills are smarter than commands -- they do multi-step reasoning. Try this: ask me to research a topic, then ask me to write an article from it. That's two skills working together."

---

## Part 3: Explain Plan Mode

After setting up commands and skills, briefly explain Plan Mode:

> "One more thing: Plan Mode. Press **Shift+Tab** to toggle it on.
>
> When Plan Mode is on, I'll think before I build -- I'll outline what I'm going to do and wait for your approval before making changes.
>
> Use it for anything bigger than a quick fix. It stops me from rushing ahead."

---

## Verify Skills Are Working

After installing skills, run this quick check:

1. Type `/find` -- it should appear in the command list
2. Type `/web-researcher` -- it should appear in the command list
3. If either doesn't appear, **restart Claude Code** (skills load at startup, not mid-conversation)

**Tell the user:** "If a skill doesn't show up after copying the file, restart Claude Code. Skills are registered when Claude starts up."

---

## Show Them How to Use It

> "Your commands and skills are ready! Here's how to use them:
>
> - Type `/status`, `/log`, or any command name
> - Type `/find supplier spreadsheet` to search for files
> - Type `/web-researcher` to research any topic or URL
> - Say 'write an article from that research' to chain skills together
> - Press **Shift+Tab** to toggle Plan Mode before big tasks
>
> Want to try one now? Ask me to research something in your niche."

---

## Troubleshooting

**"The command isn't working"**
- Check the folder is called `.claude/commands/` (with the dot)
- Check the file ends in `.md`
- Make sure there's a `description:` line at the top

**"A skill doesn't appear when I type its name"**
- Skills are loaded when Claude Code starts up
- If you added a skill mid-conversation, restart Claude Code
- Check the file is in `.claude/skills/` (not `.claude/commands/`)
- Check the file has a `name:` and `description:` in the frontmatter

**"How do I pass information to a command?"**
- Use `$ARGUMENTS` in your prompt
- Whatever they type after the command becomes `$ARGUMENTS`

---

## Important Behaviours

- **Keep commands simple** -- one clear purpose per command
- **Use natural language** -- write prompts like you're talking to Claude
- **Test each command** -- try it once to make sure it works
- **UK date format** -- always use DD Month YYYY in command outputs

---

*Setup time: 10 minutes for commands + skills. Plan Mode is just a toggle.*
