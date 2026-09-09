# Agent Versatility Demonstration

**Created:** Monday, 08 December 2025 at 16:16 BST
**Module:** 5 - Free AI Agents
**Purpose:** Demonstrate that agents are skill-based, not domain-locked

---

## The Core Insight

Agents are labelled by their original use case, but their **underlying skills transfer to any domain**.

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
    A["Agent Label<br/>(Amazon, Moving)"] --> B["Core Skill<br/>(The Real Value)"]
    B --> C["Any Domain<br/>(Your Use Case)"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px

    class A,B,C default
```

---

## Discussion Flow: Real-World Examples

### Question 1: DVLA Data Entry

**Scenario:** A delegate wants team members to input data into the DVLA website.

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
    Q1["DVLA<br/>Data Entry<br/>Need"] --> S1["What Skill?<br/>Documentation<br/>or Automation"]
    S1 --> A1["Agent-3<br/>Content Creator<br/>SOPs & Guides"]
    S1 --> A2["Playwright MCP<br/>Browser<br/>Automation"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px

    class Q1,S1,A1,A2 default
```

<table width="100%">
<tr>
<td width="50%" valign="top">

**If Training Team (Documentation)**

Use **amazon-agent-3** (Content Creator):
- Create step-by-step SOP
- Build data entry checklist
- Write error-handling procedures
- Draft training materials

Also consider **admin-coordinator** for SOP drafts.

</td>
<td width="50%" valign="top">

**If Automating Process**

Use **Playwright MCP**:
- Navigate to DVLA website
- Fill form fields programmatically
- Handle multi-step forms
- Screenshot verification

Note: Check DVLA terms of service first.

</td>
</tr>
</table>

---

### Question 2: Amazon Seller Central Audit

**Scenario:** Make sure Amazon isn't overcharging fees or missing reimbursements.

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
    Q2["Seller Central<br/>Fee Audit<br/>Need"] --> S2["What Skill?<br/>Financial<br/>Analysis"]
    S2 --> A3["Agent-6<br/>Analytics Reporter<br/>Financial Forensics"]
    A3 --> O1["FBA Fee<br/>Discrepancies"]
    A3 --> O2["Lost Inventory<br/>Claims"]
    A3 --> O3["Reimbursement<br/>Gaps"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px

    class Q2,S2,A3,O1,O2,O3 default
```

**Agent-6 Core Skill:** Financial analysis and budget tracking

| What Amazon Gets Wrong | What Agent-6 Finds |
|------------------------|-------------------|
| FBA fee overcharges | Dimension/weight vs actual product |
| Lost inventory | Shipments sent vs received vs reimbursed |
| Damaged inventory | Units damaged but not credited |
| Customer returns | Returns not restocked or reimbursed |
| Referral fee errors | Wrong category percentages |
| Storage fee spikes | Aged inventory cost analysis |

---

## The Pattern: Skill-Based Thinking

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
    subgraph WRONG["Wrong Question"]
        W1["Which Amazon<br/>agent do I use?"]
    end

    subgraph RIGHT["Right Question"]
        R1["What SKILL<br/>do I need?"]
    end

    W1 -.->|"Reframe"| R1
    R1 --> R2["Match skill<br/>to agent"]
    R2 --> R3["Apply to<br/>ANY domain"]

    classDef default fill:transparent,stroke:#ffffff,stroke-width:2px,color:#ffffff,padding:15px
    classDef subgraphStyle fill:transparent,stroke:#ffffff,stroke-width:1px,color:#ffffff

    class W1,R1,R2,R3 default
```

---

## Agent Skills Quick Reference

| Agent | Label Says | Core Skill | Can Be Used For |
|-------|-----------|------------|-----------------|
| amazon-agent-1 | Trend Researcher | Market analysis | Any industry trends, competitor research |
| amazon-agent-2 | Reddit Scout | Community research | Any forum/community insights |
| amazon-agent-3 | Content Creator | Documentation | SOPs, guides, training materials |
| amazon-agent-4 | Growth Hacker | Phase coordination | Any project timeline management |
| amazon-agent-5 | TikTok Strategist | Social content | Any platform content strategy |
| amazon-agent-6 | Analytics Reporter | Financial analysis | Any budget/fee/cost analysis |
| amazon-agent-7 | Feedback Analyst | Decision framework | Any multi-stakeholder decisions |
| amazon-agent-8 | Support Responder | Communication templates | Any vendor/client correspondence |

---

## Key Takeaway

**Don't ask:** "Which Amazon agent handles this?"

**Ask:** "What skill do I need?" Then find the agent with that skill.

The "Amazon" label is just where the agent started. The skill is universal.

---

## Workshop Exercise

Present delegates with random scenarios and have them identify:

1. What skill is needed?
2. Which agent has that skill?
3. How would they prompt it?

**Example scenarios:**
- "I need to compare three software vendors"
- "My team keeps making the same mistakes"
- "I want to understand what customers say on forums"
- "I need to track where our budget is going"

---

*Module 5 Demonstration Material | AI Workshop Curriculum*
