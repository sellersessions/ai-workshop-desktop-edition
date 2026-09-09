# Amazon Product Research Pipeline

**A systematic approach to product research that reduces launch risk**

---

## The Problem This Solves

Most Amazon sellers make a critical mistake:

```
Study competitor REVIEWS (post-purchase feedback)
    → Build "Frankenstein" product based on what customers said AFTER buying
    → Launch with expensive PPC
    → Wonder why they're failing or why it costs too much to move the needle
```

**Reviews are post-purchase.** By the time someone leaves a review, they've already bought. The real question sellers should ask:

> "What are the OBJECTIONS that stop people from buying in the first place?"

This pipeline focuses on **pre-purchase research** - understanding why people DON'T buy, not what they think after they've already committed.

---

## Who This Is For

- Amazon sellers doing product research before committing capital
- Students learning systematic product validation
- Anyone who wants to reduce launch risk before spending on inventory and PPC

---

## What You'll Get

After running this pipeline, you'll have:

1. **Market viability assessment** - Is there enough demand with manageable competition?
2. **Brand ecosystem analysis** - Are there complementary products to build a real brand?
3. **Competitive landscape** - Who are you up against and how can you differentiate?
4. **Financial model** - Landed costs, price points, and cash flow requirements
5. **Customer objections** - The real reasons people hesitate to buy (not post-purchase complaints)
6. **Go/No-Go decision** - Clear recommendation with supporting evidence

---

## Before You Start

### Requirements

- Claude Code CLI installed
- Access to this folder in VS Code
- Web search capability (for market research)

### Time Investment

- **Quick research:** 15-20 minutes (high-level assessment)
- **Deep research:** 45-60 minutes (full pipeline with supplier research)

### Token Usage

This pipeline is designed for classroom use. It asks qualifying questions BEFORE running expensive searches, so you don't waste tokens on the wrong category or product type.

---

## How to Use

### Step 1: Answer the Pre-Deployment Questions

Before running the pipeline, you'll be asked:

| Question | Example Answer |
|----------|----------------|
| What category? | Home & Kitchen |
| What sub-niche? | Kitchen organization / spice racks |
| Budget for first order? | $3,000-5,000 |
| US domestic or overseas suppliers? | Open to both |
| Single product or brand ecosystem? | Want to build a brand |

### Step 2: Run the Pipeline

In Claude Code, say:

```
Use the amazon-product-research-pipeline agent to research [your category/product idea]
```

Or for more control:

```
Read the PIPELINE-CONDUCTOR.md file and run the Amazon product research pipeline for [category].
Start by asking me the pre-deployment questions.
```

### Step 3: Review Your Reports

The pipeline generates reports in the `/reports/` folder:

| Report | What It Contains |
|--------|------------------|
| [01-NICHE-RESEARCH.md](reports/01-NICHE-RESEARCH.md) | Category analysis, sub-niche opportunities |
| [02-DEMAND-COMPETITION.md](reports/02-DEMAND-COMPETITION.md) | Search volume vs competition assessment |
| [03-BRAND-ECOSYSTEM.md](reports/03-BRAND-ECOSYSTEM.md) | Related products for brand building |
| [04-SERP-ANALYSIS.md](reports/04-SERP-ANALYSIS.md) | Search results page breakdown |
| [05-COMPETITOR-DEEP-DIVE.md](reports/05-COMPETITOR-DEEP-DIVE.md) | Top competitor analysis |
| [06-DIFFERENTIATION.md](reports/06-DIFFERENTIATION.md) | How to stand out |
| [07-PRICE-POINT.md](reports/07-PRICE-POINT.md) | Optimal pricing strategy |
| [08-LANDED-COSTS.md](reports/08-LANDED-COSTS.md) | Supplier quotes, shipping, fees |
| [09-CASH-FLOW.md](reports/09-CASH-FLOW.md) | Capital requirements |
| [10-CUSTOMER-OBJECTIONS.md](reports/10-CUSTOMER-OBJECTIONS.md) | Pre-purchase hesitations |
| [HIGHLIGHT-SUMMARY.md](reports/HIGHLIGHT-SUMMARY.md) | Executive summary with links |

### Step 4: Make Your Decision

The `HIGHLIGHT-SUMMARY.md` file gives you a clear Go/No-Go recommendation based on all the research.

---

## Pipeline Phases

### Phase 1: Market Discovery

**Goal:** Find a niche with high demand and manageable competition

- Niche research within your category
- Demand vs competition analysis
- Brand ecosystem opportunities (don't launch single products)

### Phase 2: Competition Analysis

**Goal:** Understand who you're up against and how to differentiate

- SERP analysis for main keywords
- Deep dive on top 3-5 competitors
- Differentiation strategy

### Phase 3: Financial Viability

**Goal:** Know your numbers before committing capital

- Price point analysis (what the market will bear)
- Landed cost calculation (Alibaba + US domestic options)
- Cash flow check (can you afford the inventory?)

### Phase 4: Customer Objections (The Missing Piece)

**Goal:** Understand why people DON'T buy

This is where most sellers fail. They study reviews (post-purchase) instead of objections (pre-purchase).

**Sources for objections:**
- Reddit/forums - People considering but hesitant
- Amazon Q&A sections - Pre-purchase questions reveal concerns
- Return reasons - Post-purchase regret (different from reviews)
- Social media - Complaints about the category

**NOT sources for objections:**
- Competitor reviews - These are post-purchase, biased toward people who already bought

---

## The Customer Objections Framework

### Why Reviews Are Misleading

| Reviews Tell You | Objections Tell You |
|------------------|---------------------|
| What buyers think AFTER purchase | Why people DON'T buy |
| Complaints from committed customers | Hesitations from potential customers |
| Features that disappoint after use | Concerns that prevent the sale |
| Problems with competitors' products | Problems with the entire category |

### Example: Kitchen Knife Set

**What reviews say:**
- "Handle came loose after 6 months"
- "Not as sharp as advertised"
- "Great value for the price"

**What objections reveal:**
- "I don't know if I need a full set or just a chef's knife"
- "How do I know if it's actually sharp before buying?"
- "Will this work with my knife block?"
- "I'm worried about safety - how do I store these?"

**The difference:** Reviews help you build a slightly better knife. Objections help you understand why people hesitate to buy ANY knife set - and that's where the opportunity is.

---

## File Structure

```
/amazon-product-research-pipeline/
├── README.md                          # You are here
├── PIPELINE-CONDUCTOR.md              # The orchestrator agent
├── PRE-DEPLOYMENT-QUESTIONNAIRE.md    # Questions before running
└── /reports/                          # Output folder
    ├── 01-NICHE-RESEARCH.md
    ├── 02-DEMAND-COMPETITION.md
    ├── 03-BRAND-ECOSYSTEM.md
    ├── 04-SERP-ANALYSIS.md
    ├── 05-COMPETITOR-DEEP-DIVE.md
    ├── 06-DIFFERENTIATION.md
    ├── 07-PRICE-POINT.md
    ├── 08-LANDED-COSTS.md
    ├── 09-CASH-FLOW.md
    ├── 10-CUSTOMER-OBJECTIONS.md
    └── HIGHLIGHT-SUMMARY.md
```

---

## Key Principles

### 1. Don't Launch Single Products

If you find a product with no complementary items in the same category, reconsider. Building a brand requires multiple products that serve the same customer.

### 2. Margins Are Getting Tighter

Amazon fees increase regularly. Your landed cost calculations need buffer for:
- FBA fee increases
- Storage fee changes
- PPC cost inflation
- Return rate variations

### 3. The Holy Grail Is Rare

High demand + low competition is extremely difficult to find. The real skill is finding the middle ground and knowing how to differentiate.

### 4. Cash Flow Is King

A great product opportunity means nothing if you can't afford the inventory. The pipeline includes cash flow analysis to ensure viability.

---

## Next Steps After Research

If the pipeline gives you a **GO** recommendation:

1. Order samples from 3-5 suppliers
2. Validate product quality in person
3. Get final quotes with MOQ and lead times
4. Create listing content (use the amazon-content-creator agent)
5. Plan your launch strategy (use the amazon-growth-hacker agent)

If the pipeline gives you a **NO-GO** recommendation:

1. Review the specific concerns flagged
2. Consider adjacent niches in the same category
3. Adjust your budget or timeline
4. Research a different category entirely

---

## Credits

Part of the **AI Workshop Curriculum - Module 5: Agents**

Uses the Amazon Seller Agents pack:
- [01-amazon-trend-researcher.md](../amazon-seller-agents/01-amazon-trend-researcher.md)
- [02-amazon-reddit-scout.md](../amazon-seller-agents/02-amazon-reddit-scout.md)
- [06-amazon-analytics-reporter.md](../amazon-seller-agents/06-amazon-analytics-reporter.md)
- [07-amazon-feedback-analyst.md](../amazon-seller-agents/07-amazon-feedback-analyst.md)

---

*Amazon Product Research Pipeline | Module 5 | AI Workshop Curriculum*
