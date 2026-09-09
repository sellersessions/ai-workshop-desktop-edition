# Master Log Self-Drive File

**Follow the instructions in this file, one step at a time.**

**Claude: ask each question below with your multiple-choice tool whenever there are options, so the learner can click an answer rather than type one.**

---

**Before starting:** Ask the user:

> "Quick check: shall we work in plan mode? Just say 'switch to plan mode' and I will describe what I am about to do before I do it, so you can catch anything before it happens. Keep it on for this whole module."

Wait for them to confirm before continuing.

---

**For Claude Code:** When a user gives you this file, help them set up their Master Session Log by following these instructions.

---

## What You're Creating

A single file that keeps track of everything you and the user work on together - across multiple conversations. Think of it as a shared diary that Claude can read at the start of each session to remember what happened before.

---

## Questions to Ask (Keep It Simple)

Ask these five questions one at a time. Wait for their answer before moving on.

### Question 1: Tell me about your project

> "Tell me about your project in 2-3 sentences. What is it, and what's the goal?"

**Why this matters:** This gives you enough context to write a real first log entry -- not just placeholders. Listen for the project name, what they're building or tracking, and who it's for.

---

### Question 2: What have you been working on recently?

> "What have you been working on recently, or what do you want to start with? Give me a few specifics -- files you've created, research you've done, decisions you've made."

**Why this matters:** The first log entry should capture real work, not empty templates. Even if they're just starting, they'll have something ("I set up Claude Code yesterday" or "I've been researching suppliers").

---

### Question 3: What should we call your log?

> "What name would you like for your session log? Most people use something like `MASTER-SESSION-LOG.md` or `SESSION-DIARY.md` - whatever makes sense to you."

**If they're unsure:** Suggest `MASTER-SESSION-LOG.md` - it's clear and professional.

---

### Question 4: Where should it live?

> "Where would you like me to save your session log? I'd recommend the root of your project folder so it's easy to find."

**If they're unsure:** Put it in the project root (same folder as their CLAUDE.md if they have one).

---

### Question 5: What's important to track?

> "What kind of things do you want me to record in your session log? For example:
> - Research findings and summaries
> - Decisions you've made
> - Files we've created or changed
> - Next steps and to-dos
> - Anything else?"

**Listen for what matters to them** - some people care about decisions, others about files, others about next steps.

---

## Create the Log File

Once you have their answers, create the file. **Use their answers from Questions 1 and 2 to populate a real first entry** -- not placeholders. The first entry should feel like a genuine record of their project state, not a blank template.

```markdown
# Master Session Log

This file tracks our work together across sessions. Claude reads this at the start of each conversation to remember what we've done.

**Project:** [From Question 1 -- what the project is and its goal]
**Created:** [today's date and time - UK format]
**Last Updated:** [today's date and time - UK format]

---

## How This Works

- New entries go at the TOP (newest first)
- Each entry has a date, what we did, and any important notes
- I'll update this at the end of each session

---

## Session Log

### [Today's Date] - Project Setup

**What we did:**
- Set up this Master Session Log
- [Use their answers from Question 2 -- mention specific work they described, files they mentioned, research they've done. This should be 3-5 real bullet points, not placeholders.]

**Key decisions:**
- [Pull any decisions from their answers. If they mentioned choosing a niche, a tool, a direction -- capture it here.]

**Files created/changed:**
- MASTER-SESSION-LOG.md (this file)
- [List any other files they mentioned in Question 2]

**Next steps:**
- [Based on what they told you, what's the logical next step? Be specific.]

---

[Previous sessions will appear above this line]
```

**Important:** If their answers to Questions 1 and 2 were brief, ask one follow-up: "Can you tell me a bit more about [specific thing]? I want the first log entry to be useful, not just empty bullet points."

---

## Explain the Benefits

After creating the file, explain:

> "Your Master Session Log is ready. Here's how it helps:
>
> 1. **I'll remember** - When you start a new conversation, I can read this and pick up where we left off
> 2. **You'll find things** - All your research, decisions, and progress in one place
> 3. **Nothing gets lost** - Even if a conversation ends, the important stuff is saved
>
> At the end of each session, just ask me to 'update the log' and I'll add what we did."

---

## Important Behaviours

**Always use UK date format:** DD Month YYYY (e.g., 26 November 2025)

**Always add time for same-day entries:** 14:30 format

**Keep entries scannable:**
- Bullet points, not paragraphs
- Clear headings
- Short summaries

**Newest entries at the top** - so the most recent work is always visible first

---

## If They Already Have a Log

If they mention they have an existing log:

> "I can see you already have a session log. Would you like me to:
> 1. Continue using your existing format
> 2. Help you improve the structure
> 3. Start fresh with a new one"

Respect their existing system - don't force changes.

---

## Quick Reference for Users

Tell them:

> "To use your log effectively:
> - **Start of session:** Ask me to 'read the session log' or 'what did we do last time?'
> - **End of session:** Ask me to 'update the log' or 'add this to the session log'
> - **Finding things:** Just ask 'what research did we do on [topic]?' and I'll search the log"

---

## Verify It Works

Before finishing, run this quick test:

1. Tell the user: "Start a new conversation in this same project folder"
2. Ask them to type: "What was I working on?" or "What did we do last time?"
3. Claude should answer based on the log entry you just created
4. If Claude doesn't know, check the log file is in the project root (same folder as CLAUDE.md)

This test proves the log is working. If it fails, the file is in the wrong place.

---

*This setup takes about 5 minutes. The log grows with each session.*
