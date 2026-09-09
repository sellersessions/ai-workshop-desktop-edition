# Workshop Feedback -- Self-Drive File

**For the attendee:** Paste everything below the line into Claude Code at the end of the workshop. Claude will analyse your session, score each module, and generate a feedback report.

**For Danny:** Collect these reports from attendees. The fixed table format makes it easy to compare across 20-30 responses.

---

## Instructions for Claude

You are generating a workshop feedback report. Follow these steps exactly:

### Step 1: Find today's transcripts

Look for `.jsonl` transcript files from today's date. Check these locations:

```
~/.claude/projects/*/
~/.claude/
```

Read all `.jsonl` files modified today. These contain the full session history.

### Step 2: Detect which modules were attempted

Scan the transcript for self-drive file pastes. Each module has a unique signature phrase (see detection table below). A module counts as "attempted" if its signature appears anywhere in the transcript.

### Step 3: Score each module

For each attempted module:
1. Check whether the completion marker was reached (see completion table)
2. Count tool failures (`isError: true` in the transcript)
3. Look for struggle signals (repeated questions, error chains, frustration language)
4. Assign a score using the rubric below

### Step 4: Ask one question

Ask the attendee:

> "What would have made this workshop easier for you? Any moment where you felt stuck or confused -- even briefly?"

Wait for their answer before completing the report.

### Step 5: Fill in the template

Complete the feedback template at the bottom of this file. Save it as `WORKSHOP-FEEDBACK-COMPLETED.md` in the current project folder.

### Step 6: Generate student recommendations

Using the scores from Step 3, write a "Your Next Steps" section at the bottom of the report. This is student-facing -- encouraging, not punitive.

For each module:

- **Score 1-2 (Smooth / Minor friction):** Confirm the module is solid. One line: "Module X -- you're set."
- **Score 3+ (Moderate struggle or worse):** Recommend a resit with a plain-English reason tied to what went wrong. E.g. "Module 3 -- worth redoing. The skill installation had friction that may have left gaps. Run through it again with a fresh conversation and it should click."
- **Skipped modules:** Nudge to come back. E.g. "Module 4 -- not attempted yet. When you're ready, this one connects Claude to your calendar, browser, and files."

Use the Resit Recommendation Rubric (in the scoring section) to keep output consistent across all students. End with the closing line about resit timing.

---

## Module Detection

Each self-drive file has a unique opening phrase. Search the transcript for these exact strings:

| Module | Name | Detection signature |
|--------|------|---------------------|
| 000 | Install Claude Desktop | `open the Code tab`, `Change directory`, `pick my Claude-projects folder` |
| 00 | VS Code + Copilot Setup | `I'm setting up VS Code with GitHub Copilot for the first time` |
| 1 | CLAUDE.md | `You are helping a user create their first CLAUDE.md file` |
| 2 | Master Log | `help them set up their Master Session Log` |
| 3 | Slash Commands + Skills | `help them set up slash commands AND install 3 starter skills` |
| 4 | MCP Tools | `set up their MCP automation tools` |
| 5 | Amazon Seller Agents | `help them install 8 Amazon seller agents` |

If a signature is not found in the transcript, mark that module as **Skipped** (not Blocked).

---

## Completion Markers

What proves a module was finished successfully:

| Module | Completion evidence |
|--------|--------------------|
| 000 | A session in the learner's own project folder, with a `hello.md` created in it |
| 00 | 6 extensions confirmed installed (check for install confirmations) |
| 1 | A `CLAUDE.md` file was created (look for file write operations) |
| 2 | A master session log file was created (any `.md` log file written) |
| 3 | Files created in `.claude/commands/` AND `.claude/skills/` |
| 4 | `.mcp.json` created AND at least 1 MCP tool tested successfully |
| 5 | Files copied to `~/.claude/agents/` AND at least 1 agent invoked |

---

## Struggle Scoring Rubric

| Score | Label | Criteria |
|-------|-------|----------|
| 1 | Smooth | 0-1 errors, no repeated questions, moved through quickly |
| 2 | Minor friction | 2-3 errors but self-resolved without revisiting steps |
| 3 | Moderate struggle | 4-6 errors OR similar questions asked 2+ times |
| 4 | Significant struggle | 7+ errors OR 3+ consecutive failures OR frustration expressed |
| 5 | Blocked | Module not completed, session ended mid-module, or context limit hit |

### Signals to look for

- **Tool failures:** `isError: true` in transcript entries
- **Error chains:** 3+ consecutive failures on the same step
- **Repeated questions:** User asking the same thing in different words
- **Frustration language:** "stuck", "not working", "broken", "help me", "why won't"
- **Incomplete module:** Self-drive pasted but completion marker never reached
- **Context limit:** Session ended abruptly or compaction triggered mid-module

### Resit Recommendation Rubric

Use this to generate consistent recommendations in Step 6:

| Score | Recommendation |
|-------|---------------|
| 1 | Solid -- no action needed |
| 2 | Solid -- no action needed |
| 3 | Worth redoing -- explain what caused the friction |
| 4 | Recommend resit -- specific guidance on what to watch for |
| 5 | Recommend resit -- module wasn't completed, start fresh |
| Skipped | Encourage them to attempt when ready |

---

## Handling Pre-existing Setups

Not every attendee starts from zero. Score based on what actually needed doing:

| Scenario | How to handle |
|----------|---------------|
| Claude Code already installed | Module 000 score = 1. Note "pre-installed" in friction column |
| VS Code already set up | Score only the extension install portion of Module 00 |
| Some extensions pre-existing | Score based only on the new installs needed |
| CLAUDE.md already exists | Score normally -- the exercise still runs (updates existing file) |
| Existing `.claude/commands/` or `.claude/skills/` | Score normally -- new files merge with existing |
| Existing `.mcp.json` | Score normally -- watch for config merge conflicts as friction |
| Module skipped entirely | Mark "Skipped", score N/A. Not a failure |
| Modules done out of order | Score each independently. Note the order in feedback |
| Multiple `.jsonl` files (restarted session) | Analyse all today's files together. Stitch by timestamp |
| Very short attempt (<5 messages) | Mark "Partial". Score based on what happened |

**Key rule:** "Pre-installed" or "already set up" is a good outcome, not a failure. Only score struggle on the parts that actually needed doing.

---

## Feedback Template

Fill in this template after analysing the transcript and getting the attendee's answer.

```
## Workshop Feedback

**Attendee:** [name or initials -- ask if not obvious from transcript]
**Date:** [today's date]
**Course completed:** [yes / partial / no]
**Modules attempted:** [list, e.g. "000, 00, 1, 2, 3, 4, 5"]

### Module Scores

| Module | Completed | Score (1-5) | Top friction point | Errors |
|--------|-----------|-------------|-------------------|--------|
| 000    |           |             |                   |        |
| 00     |           |             |                   |        |
| 1      |           |             |                   |        |
| 2      |           |             |                   |        |
| 3      |           |             |                   |        |
| 4      |           |             |                   |        |
| 5      |           |             |                   |        |

### Summary

**Hardest module:** [which one and why]
**Easiest module:** [which one and why]
**What would have made this easier:** [attendee's answer from Step 4]
**Module order taken:** [sequence they did modules in, if non-linear]
**Pre-existing setup:** [list anything that was already installed/configured]
**Notes:** [anything else -- patterns, workarounds used, recurring issues]

### Your Next Steps

[For each module, one line:]
- Module 000 -- [solid / worth redoing because Y / not attempted yet -- here's what it covers]
- Module 00 -- [solid / worth redoing because Y / not attempted yet -- here's what it covers]
- Module 1 -- [solid / worth redoing because Y / not attempted yet -- here's what it covers]
- Module 2 -- [solid / worth redoing because Y / not attempted yet -- here's what it covers]
- Module 3 -- [solid / worth redoing because Y / not attempted yet -- here's what it covers]
- Module 4 -- [solid / worth redoing because Y / not attempted yet -- here's what it covers]
- Module 5 -- [solid / worth redoing because Y / not attempted yet -- here's what it covers]

Resitting a module takes 10-15 minutes. Start a fresh conversation, paste the self-drive file, and run through it again.
```

---

*Workshop Feedback System | AI Workshop 2.0 | SSL 2026*
