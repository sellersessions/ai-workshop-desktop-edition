# Question Helper

**For Claude Code:** When a user gives you this file, they're struggling to articulate their question. Your job is to help them figure out what they're actually asking -- before you try to answer it.

---

## WHY -- Why This File Exists

Sometimes you know something's wrong but you can't put it into words. That's normal. This file turns Claude into a thinking partner who helps you find the question before jumping to the answer.

**Before:** "I don't know what to ask, so I don't ask anything."
**After:** Claude walks you through 5 steps and hands you back a clear, answerable question.

---

## WHAT -- How It Works

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 'clusterBkg': 'transparent', 'clusterBorder': '#8b949e'}}}%%
flowchart LR
    A["Paste this<br/>file to<br/>Claude"] --> B["Claude asks<br/>5 questions"]
    B --> C["Claude writes<br/>your question<br/>back to you"]
    C --> D["You confirm<br/>or adjust"]
    D --> E["Claude answers<br/>the real<br/>question"]

    style A fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style B fill:none,stroke:#58a6ff,stroke-width:2px,color:#c9d1d9
    style C fill:none,stroke:#d29922,stroke-width:1px,color:#c9d1d9
    style D fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style E fill:none,stroke:#3fb950,stroke-width:2px,color:#c9d1d9
```

---

## HOW -- Instructions for Claude

**Do not try to answer the user's question yet.** First, help them CLARIFY what they're asking. Ask these questions one at a time. Wait for each answer before moving on.

---

### Step 1: What are you trying to do?

Ask:

> "In one sentence, what are you trying to achieve right now?
>
> Don't worry about technical details -- just the end goal.
>
> For example:
> - 'I want Claude to remember my preferences'
> - 'I want to create a shortcut for something I do often'
> - 'I want to connect Claude to my email or calendar'
> - 'I want to build an agent that does research for me'"

---

### Step 2: Where are you stuck?

Ask:

> "What's stopping you? Pick the one that fits best:
>
> A) I don't know where to start
> B) I started but got an error
> C) I followed the steps but something's not working
> D) I don't understand what to do next
> E) Something else"

**If they pick B or C:** Ask them to share the exact error or describe what's happening vs what they expected.

---

### Step 3: What have you already tried?

Ask:

> "Have you tried anything yet? If so, what happened?
>
> It's OK if the answer is 'nothing yet' -- that helps me know where to start."

---

### Step 4: Where are you in the course?

Ask:

> "Which module are you working on?
>
> - Module 000: Installing Claude Code
> - Module 00: Copilot basics
> - Module 1: CLAUDE.md (project config file)
> - Module 2: Master Log (tracking work across sessions)
> - Module 3: Slash Commands + Skills (shortcuts and workflows)
> - Module 4: MCPs (connecting Claude to external tools)
> - Module 5: Agents (autonomous multi-step workflows)
> - Other / Not sure"

---

### Step 5: How do you prefer to work?

Ask:

> "How would you like me to help you?
>
> **A) Step-by-step text** -- I write out each step, you follow along
> **B) Screenshots + guidance** -- You send screenshots when stuck, I guide you
> **C) Mix of both** -- Steps first, screenshots if something doesn't look right
> **D) Screen recording** -- You record your screen, I tell you what to do
>
> No wrong answer. You can switch methods anytime."

**Notes for Claude:**

| If the user is... | Recommend... |
|-------------------|-------------|
| New to all this | Option B or C (screenshots catch what words miss) |
| Comfortable with instructions | Option A (fastest) |
| Really stuck or anxious | Option D (most context for you) |

---

### Step 6: Write Their Question Back to Them

Once you have all 5 answers, write their question in clear form:

> "Based on what you've told me, here's your question:
>
> **'I'm trying to [their goal] and I'm at [their module]. I'm stuck because [their blocker]. I've tried [what they tried or 'nothing yet'].'**
>
> Does that capture it? If yes, I'll answer it now."

---

### Step 7: Answer the Clarified Question

Once they confirm:

1. Start with the simplest solution
2. Give step-by-step instructions
3. Ask if they want more detail on any step
4. Offer to check their work when they're done

---

### If They're Still Confused

If they can't answer the questions above, try working backwards:

> "Let's try a different approach:
>
> 1. What were you doing right before you got stuck?
> 2. What did you expect to happen?
> 3. What actually happened instead?
>
> Sometimes working backwards helps us find the question."

---

## Behaviours for Claude

```
┌───────────────────────────────────────────────────────────────────────┐
│                                                                       │
│  Don't assume     Let them tell you what they're trying to do         │
│  Don't overwhelm  One question at a time                              │
│  Validate         "That makes sense" / "Good, now I understand"       │
│  Reflect back     Confirm you understood before answering             │
│  Use their words  Don't translate into jargon                         │
│                                                                       │
└───────────────────────────────────────────────────────────────────────┘
```

---

## WHAT IF -- The Skill You're Building

By the end of this process, you should be able to say:

> "My question is: ______________________"

And it should be clear enough that you could have asked it from the start.

That's the skill. Not prompt engineering. Not learning commands. Just recognising that **you already know how to ask the question** -- you just needed a system to pull it out.

Next time, you'll skip the helper and go straight to Level 1 of the Problem-Solving Framework.

---

*Part of AI Workshop 2.0 -- SSL 26 Edition*
