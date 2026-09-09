# Your Workflow: Behavioral Patterns with Claude Code

**Created:** Monday, 08 December 2025 at 16:20 BST
**Purpose:** Show workshop students how simple the human-AI collaboration actually is
**Evidence:** 88 conversation sessions, session logs, live demonstration

---

## The Core Truth: It's Just Questions and Answers

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 
  'primaryColor': 'transparent',
  'primaryTextColor': '#ffffff',
  'primaryBorderColor': '#ffffff',
  'lineColor': '#ffffff',
  'secondaryColor': 'transparent',
  'tertiaryColor': 'transparent',
  'background': '#000000',
  'mainBkg': 'transparent',
  'secondBkg': 'transparent',
  'tertiaryBkg': 'transparent',
  'fontSize': '14px'
}}}%%

flowchart LR
    A["You<br/>Ask Question"] --> B["Claude<br/>Responds"]
    B --> C["You<br/>Refine or<br/>Move On"]
    C --> A

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px

    class A,B,C default
```

**That's it.** No coding. No complex commands. Just conversation.

---

## Pattern 1: Question and Response

From today's session:

| You Said | Claude Did |
|----------|-----------|
| "Let's walk through Module 5" | Read the directory, showed what's there |
| "What agent for DVLA data entry?" | Identified the skill needed, matched to agent |
| "What about Seller Central auditing?" | Mapped financial analysis to Agent-6 |
| "Put this in a markdown file" | Created the file with diagrams |
| "Show me in Explorer" | Opened the file in VS Code |

**No commands memorized. No syntax learned. Just plain English.**

---

## Pattern 2: Troubleshooting Together

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 
  'primaryColor': 'transparent',
  'primaryTextColor': '#ffffff',
  'primaryBorderColor': '#ffffff',
  'lineColor': '#ffffff',
  'secondaryColor': 'transparent',
  'tertiaryColor': 'transparent',
  'background': '#000000',
  'mainBkg': 'transparent',
  'secondBkg': 'transparent',
  'tertiaryBkg': 'transparent',
  'fontSize': '14px'
}}}%%

flowchart LR
    A["Problem<br/>Occurs"] --> B["Describe<br/>What Happened"]
    B --> C["Claude<br/>Investigates"]
    C --> D["Try<br/>Solution"]
    D --> E{"Works?"}
    E -->|No| B
    E -->|Yes| F["Document<br/>the Fix"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px

    class A,B,C,D,E,F default
```

**Real examples from session logs:**

| Problem | How It Was Solved |
|---------|-------------------|
| MCP server corrupted | Claude checked file size, restored from backup |
| Wrong product data in report | Claude re-extracted from source, replaced files |
| Agent not responding | Claude verified installation path, reinstalled |
| File not found | Claude searched with Glob, located actual path |

**Key insight:** You describe the problem. Claude investigates. You iterate together until it's fixed.

---

## Pattern 3: Always Log, Always Document

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 
  'primaryColor': 'transparent',
  'primaryTextColor': '#ffffff',
  'primaryBorderColor': '#ffffff',
  'lineColor': '#ffffff',
  'secondaryColor': 'transparent',
  'tertiaryColor': 'transparent',
  'background': '#000000',
  'mainBkg': 'transparent',
  'secondBkg': 'transparent',
  'tertiaryBkg': 'transparent',
  'fontSize': '14px'
}}}%%

flowchart LR
    A["Work<br/>Session"] --> B["Claude<br/>Logs It"]
    B --> C["Master<br/>Session Log"]
    C --> D["Future<br/>Reference"]
    D --> E["Resume<br/>Anytime"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px

    class A,B,C,D,E default
```

**From your 88 conversation sessions:**

| What Gets Logged | Why It Matters |
|------------------|----------------|
| What was done | Never lose progress |
| Files created/modified | Find things later |
| Decisions made | Remember the "why" |
| Next steps identified | Pick up where you left off |

**Your Master Session Log:** 154KB of documented work, searchable, referenceable.

---

## Pattern 4: MCPs Enable Everything

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 
  'primaryColor': 'transparent',
  'primaryTextColor': '#ffffff',
  'primaryBorderColor': '#ffffff',
  'lineColor': '#ffffff',
  'secondaryColor': 'transparent',
  'tertiaryColor': 'transparent',
  'background': '#000000',
  'mainBkg': 'transparent',
  'secondBkg': 'transparent',
  'tertiaryBkg': 'transparent',
  'fontSize': '14px'
}}}%%

flowchart LR
    subgraph MCPs["11 MCP Servers"]
        M1["Filesystem<br/>Read/Write"]
        M2["Notion<br/>Pages/DBs"]
        M3["Playwright<br/>Browser"]
        M4["GitHub<br/>Repos"]
    end

    A["Your<br/>Question"] --> MCPs
    MCPs --> B["Claude<br/>Takes Action"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px
    classDef subgraphStyle fill:transparent,stroke:#ffffff,stroke-width:1px,color:#ffffff

    class A,B,M1,M2,M3,M4 default
```

**What MCPs let Claude do:**

| MCP | Capability | Example |
|-----|------------|---------|
| **Filesystem** | Read, write, organize files | "Move all PDFs to archive folder" |
| **Notion** | Create pages, update databases | "Add this to my Notion workspace" |
| **Playwright** | Automate browsers | "Fill out this form for me" |
| **GitHub** | Manage repos, PRs, issues | "Create a branch for this feature" |
| **Firecrawl** | Scrape websites | "Get all product data from this page" |

**Without MCPs:** Claude can only talk.
**With MCPs:** Claude can act.

---

## Pattern 5: Agents as Team Members

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 
  'primaryColor': 'transparent',
  'primaryTextColor': '#ffffff',
  'primaryBorderColor': '#ffffff',
  'lineColor': '#ffffff',
  'secondaryColor': 'transparent',
  'tertiaryColor': 'transparent',
  'background': '#000000',
  'mainBkg': 'transparent',
  'secondBkg': 'transparent',
  'tertiaryBkg': 'transparent',
  'fontSize': '14px'
}}}%%

flowchart LR
    A["You<br/>Delegate"] --> B["Agent<br/>Specializes"]
    B --> C["Autonomous<br/>Execution"]
    C --> D["Results<br/>Delivered"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px

    class A,B,C,D default
```

**How you use agents (from session logs):**

| Task | Agent Used | What It Did Autonomously |
|------|-----------|-------------------------|
| Property analysis | Agent-1 (Trend Researcher) | Analyzed 29 properties, ranked them |
| Budget calculations | Agent-6 (Analytics Reporter) | Created affordability spreadsheet |
| Documentation | Agent-3 (Content Creator) | Generated checklists and guides |
| Decision support | Agent-7 (Feedback Analyst) | Built family decision framework |

**Like real team members:** You assign the task, they execute it, you review the results.

---

## The Complete Workflow

```mermaid
%%{init: {'theme':'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 
  'primaryColor': 'transparent',
  'primaryTextColor': '#ffffff',
  'primaryBorderColor': '#ffffff',
  'lineColor': '#ffffff',
  'secondaryColor': 'transparent',
  'tertiaryColor': 'transparent',
  'background': '#000000',
  'mainBkg': 'transparent',
  'secondBkg': 'transparent',
  'tertiaryBkg': 'transparent',
  'fontSize': '14px'
}}}%%

flowchart LR
    A["Ask<br/>Question"] --> B["Claude<br/>Responds"]
    B --> C{"Need<br/>Action?"}
    C -->|Yes| D["MCPs<br/>Execute"]
    C -->|No| E["Discuss<br/>Further"]
    D --> F["Agent<br/>Specializes"]
    F --> G["Log<br/>Everything"]
    E --> A
    G --> H["Resume<br/>Anytime"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px

    class A,B,C,D,E,F,G,H default
```

---

## What Students Should Take Away

### The Simple Version

<table width="100%">
<tr>
<td width="50%" valign="top">

**What You Do:**

1. Ask questions in plain English
2. Describe problems when stuck
3. Say "log this" or "document that"
4. Assign tasks to agents
5. Review and refine results

</td>
<td width="50%" valign="top">

**What Claude Does:**

1. Answers and takes action
2. Investigates and proposes fixes
3. Creates structured documentation
4. Delegates to specialized agents
5. Iterates until you're satisfied

</td>
</tr>
</table>

### The Technical Foundation (Already Set Up)

| Layer | What It Is | Your Interaction |
|-------|-----------|------------------|
| **MCPs** | Tools Claude can use | None - just works |
| **Agents** | Specialized team members | "Use agent X to..." |
| **Session Logs** | Memory across sessions | Automatic |
| **File System** | Your organized workspace | Claude manages it |

---

## Live Example: This Conversation

**What happened in the last 20 minutes:**

1. You asked to return to Module 5
2. I read the directory and explained it
3. You threw curveballs (DVLA, Seller Central)
4. I matched skills to agents
5. You asked for a markdown file
6. I created it with diagrams
7. You asked to analyze your patterns
8. I created THIS file

**Total commands you typed:** Zero
**Technical knowledge required:** Zero
**Results:** Two documented teaching materials

---

## The Proof: 88 Sessions, Same Pattern

From your conversation history:

| Metric | Value |
|--------|-------|
| Total conversations | 88 |
| Session log size | 154KB |
| Agents installed | 27 |
| MCPs configured | 11 |
| Your coding required | None |

**Every session follows the same pattern:** Question → Response → Iterate → Document → Resume

---

*Module 5 Teaching Material | AI Workshop Curriculum*
