# Slash Commands for Non-Technical Users

Quick reference for the built-in commands and chat UI controls you'll use most.

---

## Essential Slash Commands

| Command | What it does | When to use it |
|---------|-------------|----------------|
| `/compact` | Shrinks long conversation history while keeping key points | When your chat is getting long and Claude starts forgetting earlier context |
| `/cost` | Shows your current usage/spend for this session | When you want to check how much you've used |
| `/review` | Runs a focused review on your current draft or content | After writing something -- get specific issues and improvements, not just "looks good" |
| `/todos` | Turns the current discussion into a simple to-do list | When a chat becomes a plan and you want clear, trackable tasks |

---

## Chat Box UI

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 'clusterBkg': 'transparent', 'clusterBorder': '#8b949e'}}}%%
flowchart LR
    A["Text box<br/>Type prompts"] --> G[Send]
    B["Plan Mode<br/>toggle"] --> A
    C["Edit Mode<br/>toggle"] --> A
    D["Context<br/>pie chart"] --> A
    F["Slash icon<br/>command list"] --> A

    style A fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style B fill:none,stroke:#58a6ff,stroke-width:2px,color:#c9d1d9
    style C fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style D fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style F fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style G fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
```

---

## What the UI Controls Do

| Control | What it does | Plain English |
|---------|-------------|---------------|
| **Plan Mode toggle** | "Think first, then act" mode | Claude proposes a plan before making changes. You approve before it starts |
| **Edit Mode toggle** | Ask before editing / Auto | Controls whether Claude needs your permission before changing files |
| **Context pie chart** | Shows how full Claude's memory is | When the pie is nearly full, use `/compact` or start a new chat |
| **Slash icon** | Opens the command list | Click to browse all available commands instead of typing from memory |

---

*Reference sheet for Module 3 | AI Workshop Curriculum*
