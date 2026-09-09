# Agents Self-Drive File

**Follow the instructions in this file, one step at a time.**

**Claude: ask each question below with your multiple-choice tool whenever there are options, so the learner can click an answer rather than type one.**

---

**Before starting:** Ask the user:

> "Quick check: shall we work in plan mode? Just say 'switch to plan mode' and I will describe what I am about to do before I do it, so you can catch anything before it happens. Keep it on for this whole module."

Wait for them to confirm before continuing.

---

**For Claude Code:** When a user gives you this file, help them install 8 Amazon seller agents by following these instructions.

---

## Pre-Flight Checks

Complete both steps before installing anything.

### Step 1: Module dependency check

Ask the user:

> "Have you completed Modules 1 to 4? Agents work best when your CLAUDE.md and Master Log are already set up, they use both to follow your preferences and log sessions.
>
> If you haven't done Module 4 (MCPs): the Trend Researcher and Reddit Scout agents need web browsing to work properly. You can still install everything now, but those two agents will be limited until MCPs are set up."

---

### Step 2, Course materials check

Find the `amazon-seller-agents` folder yourself, inside the course folder the learner downloaded. Tell them where it is. Do not ask them to search for it.

- If you find it: tell the learner where it is and carry on.
- If you cannot find it: the course files are not on their machine yet. Ask them to download the course folder, then come back to you.

---

## What You're Creating

8 specialist AI agents built for Amazon sellers. Each agent is a `.md` file with deep instructions for one specific job -- trend research, content creation, analytics, support, etc.

---

## Installation Steps

### Step 1: Create the Agents Directory

Create the folder `~/.claude/agents` if it does not exist yet.

**Note:** `~/.claude/agents/` is your global agents folder, these agents will be available in every project you open in Claude Code, not just this one. That's intentional: your Amazon specialists travel with you.

### Step 2: Copy the 8 Amazon Agents

Copy every file ending in `-OPTIMIZED.md` from that folder into `~/.claude/agents/`. Do the copying yourself, then tell the learner what you moved and where it went.

**Example** (your path will differ):
```bash
cp /Users/yourname/Documents/AI-Workshop/Module-5-Agents/amazon-seller-agents/*-OPTIMIZED.md ~/.claude/agents/
```

Install the OPTIMIZED versions only. These are faster and better suited for workshop use. The full-detail standard versions are in the same folder if you want them later, copy them individually when needed.

### Step 3: Verify Installation

List what is now in `~/.claude/agents/` and show the learner.

You should see exactly 8 agent files (all ending in `-OPTIMIZED.md`).

---

> **STOP: start a new session before continuing.**
>
> A new session picks these up. Testing on 9 September 2026 showed agents appearing straight away, so if they are already listed you can carry on.
> 1. Start a new session in the Code tab
> 2. Check the folder name beside the session title is still your project folder
> 3. Ask: "Which agents do you have available?"
>    Claude should list the 8 Amazon agents by name.
>
> If it lists them: continue.
> If it doesn't: check the files are in `~/.claude/agents/` and end in `.md`.

---

## The 8 Agents

| # | Agent File | What It Does |
|---|-----------|-------------|
| 1 | `01-amazon-trend-researcher` | Product opportunities, BSR trends, market gaps |
| 2 | `02-amazon-reddit-scout` | Customer pain points, community sentiment |
| 3 | `03-amazon-content-creator` | Titles, bullets, descriptions, A+ content |
| 4 | `04-amazon-growth-hacker` | Launch strategy, PPC, ranking, traffic |
| 5 | `05-amazon-tiktok-strategist` | TikTok Shop, viral content, influencers |
| 6 | `06-amazon-analytics-reporter` | Sales data, PPC metrics, inventory |
| 7 | `07-amazon-feedback-analyst` | Review analysis, product improvements |
| 8 | `08-amazon-support-responder` | Buyer messages, returns, seller metrics |

---

## Show Them How to Use It

After installing, demonstrate:

> "Your 8 Amazon agents are installed. To use one, just mention it by name:
>
> - 'Use the trend researcher agent to find trending kitchen gadgets under GBP 30'
> - 'Use the content creator agent to write 5 bullet points for my product'
> - 'Use the feedback analyst agent to summarise these customer reviews'
>
> You don't need special syntax. Just describe what you want and name the agent.
>
> Want to try one now? Tell me about a product you're working on."

If the user isn't sure whether the agent is active, tell them to ask:

> "Are you using the [agent name] agent right now?"

Claude will confirm which agent is active. If it isn't using one, ask again with the agent name more explicitly at the start of the message.

---

## Tips to Share

- **Start with one agent** -- whichever matches their current need
- **Chain agents** -- Trend Researcher finds an opportunity, Content Creator writes the listing
- **Agents are just .md files** -- they can open and customise any agent
- **Agents use MCPs** -- if Module 4 is set up, agents can browse websites and take screenshots
- **They stack with everything** -- agents follow CLAUDE.md rules, log to Master Log, and use MCP powers

---

*Module 5 | AI Workshop Curriculum | SSL 2026*
