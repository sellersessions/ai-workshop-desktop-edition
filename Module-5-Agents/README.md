# Module 5: AI Agents -- Your Amazon Specialist Team

## WHY -- Why This Matters

Everything you've built so far -- CLAUDE.md, Master Log, commands, skills, MCPs -- gives Claude general capabilities. But Claude is still a generalist. It knows a bit about everything, nothing deeply about Amazon.

Agents change that. Each agent is a specialist with deep instructions for one job. Instead of saying "help me write a listing" and hoping Claude gets it right, you invoke the Content Creator agent -- and it already knows Amazon's title limits, bullet point best practices, and benefit-over-feature writing.

**Before:** Claude gives generic advice. You have to explain Amazon context every time.
**After:** 8 specialists who already understand Amazon selling. You describe the product, they do the rest.

---

## WHAT -- What You'll Learn

How to install and use 8 custom AI agents built specifically for Amazon sellers.

```mermaid
%%{init: {'theme': 'dark', 'themeVariables': {'nodeTextColor': '#e8e8e8', 'primaryTextColor': '#e8e8e8', 'secondaryTextColor': '#cccccc', 'tertiaryTextColor': '#cccccc', 'clusterBkg': 'transparent', 'clusterBorder': '#8b949e'}}}%%
flowchart LR
    A["Trend<br/>Researcher"] --> B["Reddit<br/>Scout"]
    B --> C["Content<br/>Creator"]
    C --> D["Growth<br/>Hacker"]
    D --> E["Analytics<br/>Reporter"]

    style A fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style B fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style C fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style D fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
    style E fill:none,stroke:#8b949e,stroke-width:1px,color:#c9d1d9
```

### The 8 Agents

| # | Agent | What It Does | Example |
|---|-------|-------------|---------|
| 1 | **Trend Researcher** | Product opportunities, BSR trends, market gaps | "Research trending kitchen gadgets under GBP 30" |
| 2 | **Reddit Scout** | Customer pain points, community sentiment | "Find what people complain about with camping chairs" |
| 3 | **Content Creator** | Titles, bullet points, descriptions, A+ content | "Write 5 bullets for my silicone baking mat" |
| 4 | **Growth Hacker** | Launch strategy, PPC, ranking, external traffic | "Create a 30-day launch plan for my new product" |
| 5 | **TikTok Strategist** | TikTok Shop, viral content, influencer strategy | "Plan 10 TikTok video ideas for my skincare product" |
| 6 | **Analytics Reporter** | Sales data, PPC metrics, inventory forecasting | "Analyse this month's sales data and spot trends" |
| 7 | **Feedback Analyst** | Review sentiment, quality issues, feature requests | "Summarise the top 5 complaints from these 100 reviews" |
| 8 | **Support Responder** | Buyer messages, returns, negative feedback handling | "Draft a reply to this angry customer about late delivery" |

### How They Work Together

This isn't 8 disconnected tools. They form a pipeline:

1. **Research phase:** Trend Researcher finds opportunities. Reddit Scout validates demand with real customer language
2. **Content phase:** Content Creator writes the listing. Growth Hacker plans the launch
3. **Scale phase:** TikTok Strategist drives external traffic. Analytics Reporter tracks what's working
4. **Maintain phase:** Feedback Analyst spots product issues early. Support Responder keeps your metrics clean

---

## HOW -- The Self-Drive Process

1. **You read** this README (done)
2. **You give Claude the self-drive file** -- open `AGENTS-SELF-DRIVE.md`, copy the contents, paste into Claude Code
3. **Claude copies the 8 agents** into your `.claude/agents/` folder
4. **You invoke agents by name** -- just mention the agent in your request

### Using an Agent

Just mention it by name:

```
Use the content creator agent to write a product description for my bamboo cutting board
```

Or be more specific:

```
Use the growth hacker agent to create a 30-day launch plan for my new product.
Focus on:
- Pre-launch buzz building
- Launch day tactics
- Post-launch momentum
```

You don't need special syntax. Claude reads the agent file and follows its instructions.

### Agent Files

The 8 agent `.md` files live in the `amazon-seller-agents/` folder in this module. Each agent comes in two versions:

- **Standard** -- the full-detail version (e.g., `01-amazon-trend-researcher.md`)
- **Optimised** -- a tighter version for faster responses (e.g., `01-amazon-trend-researcher-OPTIMIZED.md`)

Start with the optimised versions. Switch to standard if you want more depth.

### Tips

- **Start with one agent** -- pick the one you need most right now
- **Be specific** -- tell the agent your actual product and niche
- **Chain agents** -- Trend Researcher finds an opportunity, Content Creator writes the listing
- **Customise them** -- open any agent `.md` file and tweak the instructions for your niche

### Common Questions

| Question | Answer |
|----------|--------|
| Where do agents live? | In `.claude/agents/` in your project or `~/.claude/agents/` globally |
| Can I delete ones I don't need? | Yes, just delete the .md file |
| Can I edit an agent? | Yes -- open the .md file and customise the instructions |
| Can I create my own? | Yes. Copy an existing one and modify it |
| Do they survive Claude Code updates? | Yes, they're just files in your folder |

### Example Outputs

The `AGENT-TESTS-AMAZON-SUB-AGENTS/` folder contains real outputs from these agents -- trend reports, feedback analyses, Reddit scout findings. Browse them to see what the agents produce.

---

## WHAT IF -- What This Unlocks

You now have a complete AI-powered Amazon toolkit:

| Layer | Module | What It Does |
|-------|--------|-------------|
| Identity | CLAUDE.md (Module 1) | Claude knows your preferences |
| Memory | Master Log (Module 2) | Claude remembers your progress |
| Speed | Commands + Skills (Module 3) | Quick shortcuts and multi-step workflows |
| Power | MCPs (Module 4) | Real-world capabilities (web, files, screenshots) |
| Expertise | Agents (this module) | Amazon-specific specialists |

Everything stacks. An agent can use your MCPs, follow your CLAUDE.md rules, log to your Master Log, and be triggered by a slash command.

### What's Next

- **Customise agents** for your specific niche and products
- **Create new agents** from scratch for tasks unique to your business
- **Combine agents into workflows** -- research, create, launch, analyse in sequence

---

*Module 5 | AI Workshop Curriculum | SSL 2026*
