# Report Correction Guide

**Purpose:** Fine-tune pipeline reports with YOUR real data from Helium 10, Data Dive, Brand Analytics, or your own launch strategy.

---

## How to Use This Document

1. **Copy the relevant correction template** below
2. **Fill in your real data** in the bracketed fields
3. **Give it to Claude** along with the report you want to update
4. **Q&A with Claude** to refine further

**Example prompt to Claude:**
```
I want to correct and update this report with my real data. Here's my correction input:

[Paste your filled-in correction template]

Please update the report to reflect my actual numbers and situation.
```

---

## Quick Selection

| Report | When to Correct |
|--------|-----------------|
| [01 - Niche Research](#01-niche-research-correction) | You have category insights, seasonal data |
| [02 - Demand vs Competition](#02-demand-competition-correction) | You have Helium 10/Data Dive search volumes |
| [03 - Brand Ecosystem](#03-brand-ecosystem-correction) | You've identified your complementary products |
| [04 - SERP Analysis](#04-serp-analysis-correction) | You have live SERP data from your research |
| [05 - Competitor Deep Dive](#05-competitor-deep-dive-correction) | You've analyzed specific competitors |
| [06 - Differentiation](#06-differentiation-correction) | You have your own differentiation angle |
| [07 - Price Point](#07-price-point-correction) | You have pricing research or strategy |
| [08 - Landed Costs](#08-landed-costs-correction) | You have supplier quotes |
| [09 - Cash Flow](#09-cash-flow-correction) | You have your actual budget and timeline |
| [10 - Customer Objections](#10-customer-objections-correction) | You've done your own objection research |
| [Highlight Summary](#highlight-summary-correction) | Update final recommendation with all corrections |
| [Launch Strategy](#launch-strategy-overlay) | Add your launch playbook to the reports |

---

## 01 Niche Research Correction

**Use when:** You have your own category insights, trend data, or seasonal patterns.

```markdown
## CORRECTION INPUT: Niche Research

### My Product/Category
- **Category:** [Your category]
- **Sub-niche:** [Your specific product type]
- **Product concept:** [Brief description of what you're selling]

### My Trend Data
**Source:** [Helium 10 / Jungle Scout / Google Trends / Other]

| Sub-Niche | Trend Direction | Data Point |
|-----------|-----------------|------------|
| [Sub-niche 1] | [Up/Down/Stable] | [% change or specific data] |
| [Sub-niche 2] | [Up/Down/Stable] | [% change or specific data] |
| [Sub-niche 3] | [Up/Down/Stable] | [% change or specific data] |

### My Seasonal Insights
**Source:** [Brand Analytics / Helium 10 / Historical data]

| Period | My Data Shows |
|--------|---------------|
| Q1 (Jan-Mar) | [Your observation] |
| Q2 (Apr-Jun) | [Your observation] |
| Q3 (Jul-Sep) | [Your observation] |
| Q4 (Oct-Dec) | [Your observation] |

**Peak period:** [Month/Season]
**Low period:** [Month/Season]

### Market Gaps I've Identified
1. [Gap 1 - what you've observed]
2. [Gap 2 - what you've observed]
3. [Gap 3 - what you've observed]

### Additional Context
[Any other insights you want incorporated]
```

---

## 02 Demand Competition Correction

**Use when:** You have real search volume data from Helium 10, Data Dive, Brand Analytics, or similar tools.

```markdown
## CORRECTION INPUT: Demand vs Competition

### My Search Volume Data
**Source:** [Helium 10 / Data Dive / Brand Analytics / Jungle Scout]
**Date pulled:** [Date]

| Keyword | Search Volume | Trend | CPR/Giveaways | Notes |
|---------|---------------|-------|---------------|-------|
| [Main keyword] | [Exact number] | [Up/Down/Stable] | [If available] | |
| [Keyword 2] | [Exact number] | [Up/Down/Stable] | | |
| [Keyword 3] | [Exact number] | [Up/Down/Stable] | | |
| [Keyword 4] | [Exact number] | [Up/Down/Stable] | | |
| [Keyword 5] | [Exact number] | [Up/Down/Stable] | | |

**Total search volume:** [Sum or estimate]

### Brand Analytics Data (if available)
**Top 3 clicked ASINs for main keyword:**
1. ASIN: [ASIN] - Click share: [%] - Conversion share: [%]
2. ASIN: [ASIN] - Click share: [%] - Conversion share: [%]
3. ASIN: [ASIN] - Click share: [%] - Conversion share: [%]

### Competition Metrics I've Found
- **Products on page 1:** [Number]
- **Average reviews (page 1):** [Number]
- **Lowest reviews in top 10:** [Number]
- **Amazon Basics/Essentials present:** [Yes/No]
- **Major brands present:** [List any]

### My Assessment
- **Demand level:** [High/Medium/Low]
- **Competition level:** [High/Medium/Low]
- **Entry difficulty:** [Easy/Medium/Hard]

### Additional Context
[Any other data points or observations]
```

---

## 03 Brand Ecosystem Correction

**Use when:** You've identified your own complementary products or have a brand strategy.

```markdown
## CORRECTION INPUT: Brand Ecosystem

### My Complementary Products Research
**Source:** [Your research method]

| Product | Search Volume | Competition | I Want to Sell This |
|---------|---------------|-------------|---------------------|
| [Product 1] | [Volume] | [H/M/L] | [Yes/No/Maybe] |
| [Product 2] | [Volume] | [H/M/L] | [Yes/No/Maybe] |
| [Product 3] | [Volume] | [H/M/L] | [Yes/No/Maybe] |
| [Product 4] | [Volume] | [H/M/L] | [Yes/No/Maybe] |
| [Product 5] | [Volume] | [H/M/L] | [Yes/No/Maybe] |

### My Brand Vision
- **Brand name (if decided):** [Name or "TBD"]
- **Brand positioning:** [Premium/Value/Eco/Other]
- **Target customer:** [Description]
- **Number of products at launch:** [Number]
- **12-month product roadmap:** [Brief plan]

### Existing Brand Research
**Brands I've analyzed in this space:**

| Brand | # of Products | Est. Revenue | What They Do Well | Gap I See |
|-------|---------------|--------------|-------------------|-----------|
| [Brand 1] | [Number] | [Estimate] | [Strength] | [Gap] |
| [Brand 2] | [Number] | [Estimate] | [Strength] | [Gap] |
| [Brand 3] | [Number] | [Estimate] | [Strength] | [Gap] |

### Additional Context
[Your brand strategy notes]
```

---

## 04 SERP Analysis Correction

**Use when:** You have live SERP data from your own Amazon research.

```markdown
## CORRECTION INPUT: SERP Analysis

### My SERP Data
**Keyword:** [Main keyword]
**Date captured:** [Date]
**Device:** [Desktop/Mobile]

| Position | Type | Product/Brand | Price | Reviews | Rating | Badge |
|----------|------|---------------|-------|---------|--------|-------|
| 1 | [Org/Spons] | [Name] | $[XX] | [Count] | [X.X] | [AC/BS/None] |
| 2 | [Org/Spons] | [Name] | $[XX] | [Count] | [X.X] | [AC/BS/None] |
| 3 | [Org/Spons] | [Name] | $[XX] | [Count] | [X.X] | [AC/BS/None] |
| 4 | [Org/Spons] | [Name] | $[XX] | [Count] | [X.X] | [AC/BS/None] |
| 5 | [Org/Spons] | [Name] | $[XX] | [Count] | [X.X] | [AC/BS/None] |
| 6 | [Org/Spons] | [Name] | $[XX] | [Count] | [X.X] | [AC/BS/None] |
| 7 | [Org/Spons] | [Name] | $[XX] | [Count] | [X.X] | [AC/BS/None] |
| 8 | [Org/Spons] | [Name] | $[XX] | [Count] | [X.X] | [AC/BS/None] |

### Sponsored Placement Count
- **Sponsored at top:** [Number]
- **Organic positions:** [Number]
- **Sponsored mid-page:** [Number]

### PPC Estimates (if available)
**Source:** [Helium 10 / Jungle Scout / Other]
- **Suggested bid:** $[X.XX]
- **Estimated CPC:** $[X.XX]
- **PPC difficulty:** [Easy/Medium/Hard]

### Listing Quality Observations
| Position | Title | Images | Bullets | A+ | Video | Overall |
|----------|-------|--------|---------|-----|-------|---------|
| 1 | [1-5] | [1-5] | [1-5] | [Y/N] | [Y/N] | [1-5] |
| 2 | [1-5] | [1-5] | [1-5] | [Y/N] | [Y/N] | [1-5] |
| 3 | [1-5] | [1-5] | [1-5] | [Y/N] | [Y/N] | [1-5] |

### Additional Context
[Your SERP observations]
```

---

## 05 Competitor Deep Dive Correction

**Use when:** You've analyzed specific competitors in detail.

```markdown
## CORRECTION INPUT: Competitor Deep Dive

### Competitor 1: [Name/Brand]
**ASIN:** [ASIN]
**URL:** [Amazon link]

| Metric | Value |
|--------|-------|
| Price | $[XX.XX] |
| Reviews | [Count] |
| Rating | [X.X] |
| BSR | [Number] in [Category] |
| Est. Monthly Sales | [From tool] |
| Est. Monthly Revenue | $[Amount] |

**Listing Quality (1-5):**
- Title: [Score] - Notes: [Notes]
- Images: [Score] - Notes: [Notes]
- Bullets: [Score] - Notes: [Notes]
- A+ Content: [Score] - Notes: [Notes]

**Strengths I've identified:**
1. [Strength]
2. [Strength]
3. [Strength]

**Weaknesses I've identified:**
1. [Weakness]
2. [Weakness]
3. [Weakness]

---

### Competitor 2: [Name/Brand]
**ASIN:** [ASIN]

[Repeat same structure]

---

### Competitor 3: [Name/Brand]
**ASIN:** [ASIN]

[Repeat same structure]

---

### My Competitive Assessment
- **Hardest competitor to beat:** [Name] because [reason]
- **Most vulnerable competitor:** [Name] because [reason]
- **Review velocity I need:** [X reviews/month]
- **Time to compete:** [My estimate]

### Additional Context
[Your competitive insights]
```

---

## 06 Differentiation Correction

**Use when:** You have your own differentiation strategy.

```markdown
## CORRECTION INPUT: Differentiation

### My Differentiation Angle
**Primary differentiation:** [Your main angle]
**Type:** [Feature / Price / Bundle / Brand / Niche / Quality]

**Description:**
[Detailed description of how you'll differentiate]

### Why This Will Work
1. [Reason 1]
2. [Reason 2]
3. [Reason 3]

### Implementation Details
- **Product changes required:** [List]
- **Supplier capable:** [Yes/No/Checking]
- **Cost impact:** [+/- $X per unit]
- **Time to implement:** [Weeks/months]

### Alternative Angles Considered
| Angle | Why Not Chosen |
|-------|----------------|
| [Alternative 1] | [Reason] |
| [Alternative 2] | [Reason] |

### My Differentiation in Listing
**How I'll communicate this:**
- **Main image:** [How it will show]
- **Title:** [Key words to include]
- **Bullets:** [Key messages]
- **A+ content:** [How I'll feature it]

### Additional Context
[Your differentiation strategy notes]
```

---

## 07 Price Point Correction

**Use when:** You have pricing research or a specific pricing strategy.

```markdown
## CORRECTION INPUT: Price Point

### My Pricing Research
**Source:** [Your research method]

| Competitor | Price | Quality Level | Sales Est. |
|------------|-------|---------------|------------|
| [Comp 1] | $[XX.XX] | [Budget/Mid/Premium] | [Est.] |
| [Comp 2] | $[XX.XX] | [Budget/Mid/Premium] | [Est.] |
| [Comp 3] | $[XX.XX] | [Budget/Mid/Premium] | [Est.] |
| [Comp 4] | $[XX.XX] | [Budget/Mid/Premium] | [Est.] |
| [Comp 5] | $[XX.XX] | [Budget/Mid/Premium] | [Est.] |

### Price Gaps I've Found
- **Gap 1:** $[X] - $[Y] - [Opportunity]
- **Gap 2:** $[X] - $[Y] - [Opportunity]

### My Target Price
- **Launch price:** $[XX.XX]
- **Regular price:** $[XX.XX]
- **Positioning:** [Budget/Value/Mid/Premium]

### My Pricing Strategy
**Rationale:** [Why this price]

**Promotional plan:**
- Week 1-2: $[Price] ([X]% off)
- Week 3-4: $[Price]
- Month 2+: $[Price]

**Coupon strategy:** [Describe]
**Lightning Deal price:** $[Price]

### Additional Context
[Your pricing strategy notes]
```

---

## 08 Landed Costs Correction

**Use when:** You have actual supplier quotes.

```markdown
## CORRECTION INPUT: Landed Costs

### My Supplier Quotes
**Source:** [Alibaba / 1688 / Domestic / Trade show]
**Date:** [Date quoted]

| Supplier | MOQ | Unit Price | Location | Sample Cost |
|----------|-----|------------|----------|-------------|
| [Supplier 1] | [Units] | $[X.XX] | [Location] | $[X] |
| [Supplier 2] | [Units] | $[X.XX] | [Location] | $[X] |
| [Supplier 3] | [Units] | $[X.XX] | [Location] | $[X] |

**Selected supplier:** [Name]
**Negotiated price:** $[X.XX] at [MOQ] units

### My Shipping Quotes
**Freight forwarder:** [Name or "researching"]

| Method | Cost | Transit Time |
|--------|------|--------------|
| Sea (LCL) | $[X]/unit or $[X] total | [X] days |
| Sea (FCL) | $[X]/unit or $[X] total | [X] days |
| Air | $[X]/unit or $[X] total | [X] days |

### My Cost Breakdown
| Component | My Actual Cost |
|-----------|----------------|
| Product (FOB) | $[X.XX] |
| Shipping | $[X.XX] |
| Duties ([X]%) | $[X.XX] |
| Customs/brokerage | $[X.XX] |
| Prep/labeling | $[X.XX] |
| FBA fee (estimated) | $[X.XX] |
| **TOTAL LANDED** | **$[X.XX]** |

### My Margin Calculation
- **Sale price:** $[XX.XX]
- **Landed cost:** $[X.XX]
- **Referral fee (15%):** $[X.XX]
- **Gross profit:** $[X.XX]
- **Margin:** [X]%

### Additional Context
[Notes on supplier negotiations, quality specs, etc.]
```

---

## 09 Cash Flow Correction

**Use when:** You have your actual budget and timeline.

```markdown
## CORRECTION INPUT: Cash Flow

### My Actual Budget
- **Total available capital:** $[Amount]
- **Amount allocated for this product:** $[Amount]
- **Additional capital available if needed:** $[Amount or "None"]
- **Source of funds:** [Savings / Loan / Partner / Other]

### My Pre-Launch Costs (Actual/Planned)
| Expense | My Cost | Status |
|---------|---------|--------|
| Samples | $[X] | [Paid/Planned] |
| Photography | $[X] | [Paid/Planned] |
| Listing/copywriting | $[X] | [Paid/Planned] |
| Brand registry | $[X] | [Paid/Planned] |
| UPC codes | $[X] | [Paid/Planned] |
| Other: [Specify] | $[X] | [Paid/Planned] |
| **Total Pre-Launch** | **$[X]** | |

### My Inventory Plan
- **First order quantity:** [Units]
- **Unit cost:** $[X.XX]
- **Total inventory investment:** $[X]
- **Months of inventory:** [X] months (at [X] units/month projected)

### My Marketing Budget
- **PPC Month 1:** $[X]
- **PPC Month 2:** $[X]
- **Vine/reviews:** $[X]
- **Promotions/giveaways:** $[X]
- **Total marketing:** $[X]

### My Timeline
| Milestone | Target Date |
|-----------|-------------|
| Order samples | [Date] |
| Select supplier | [Date] |
| Place inventory order | [Date] |
| Inventory arrives at Amazon | [Date] |
| Launch date | [Date] |

### My Risk Buffer
- **Buffer amount:** $[X]
- **Buffer as % of total:** [X]%
- **What buffer covers:** [Your plan]

### Additional Context
[Your financial situation, constraints, flexibility]
```

---

## 10 Customer Objections Correction

**Use when:** You've done your own objection research.

```markdown
## CORRECTION INPUT: Customer Objections

### My Research Sources
- [ ] Reddit (subreddits: [list])
- [ ] Amazon Q&A sections
- [ ] Facebook groups
- [ ] Forums: [list]
- [ ] Customer interviews
- [ ] Return data (if existing seller)
- [ ] Other: [specify]

### Objections I've Found

#### Price Objections
| Objection | Frequency | Source | My Response |
|-----------|-----------|--------|-------------|
| [Objection 1] | [Common/Occasional/Rare] | [Where found] | [How I'll address] |
| [Objection 2] | [Common/Occasional/Rare] | [Where found] | [How I'll address] |

**Actual quotes:**
> "[Quote 1]" - [Source]
> "[Quote 2]" - [Source]

#### Quality Concerns
| Objection | Frequency | Source | My Response |
|-----------|-----------|--------|-------------|
| [Objection 1] | [Common/Occasional/Rare] | [Where found] | [How I'll address] |
| [Objection 2] | [Common/Occasional/Rare] | [Where found] | [How I'll address] |

**Actual quotes:**
> "[Quote 1]" - [Source]
> "[Quote 2]" - [Source]

#### Fit/Sizing Concerns
| Objection | Frequency | Source | My Response |
|-----------|-----------|--------|-------------|
| [Objection 1] | [Common/Occasional/Rare] | [Where found] | [How I'll address] |
| [Objection 2] | [Common/Occasional/Rare] | [Where found] | [How I'll address] |

#### Trust Issues
| Objection | Frequency | Source | My Response |
|-----------|-----------|--------|-------------|
| [Objection 1] | [Common/Occasional/Rare] | [Where found] | [How I'll address] |

#### Alternative Considerations
| Alternative They Consider | Why | My Counter |
|---------------------------|-----|------------|
| [Alternative 1] | [Why they consider it] | [My response] |
| [Alternative 2] | [Why they consider it] | [My response] |

### Category-Level Concerns
[Any objections to the entire category, not just products]

### My Top 3 Objections to Address
1. **[Objection]:** [How I'll address in listing]
2. **[Objection]:** [How I'll address in listing]
3. **[Objection]:** [How I'll address in listing]

### Additional Context
[Your objection research notes]
```

---

## Highlight Summary Correction

**Use when:** You want to update the final recommendation after correcting other reports.

```markdown
## CORRECTION INPUT: Highlight Summary

### Reports I've Corrected
- [ ] 01 - Niche Research
- [ ] 02 - Demand vs Competition
- [ ] 03 - Brand Ecosystem
- [ ] 04 - SERP Analysis
- [ ] 05 - Competitor Deep Dive
- [ ] 06 - Differentiation
- [ ] 07 - Price Point
- [ ] 08 - Landed Costs
- [ ] 09 - Cash Flow
- [ ] 10 - Customer Objections

### Key Changes from Corrections
1. [Major change 1 - e.g., "Search volume is actually 75,000 not 52,000"]
2. [Major change 2 - e.g., "My budget is $15,000 not $8,000"]
3. [Major change 3 - e.g., "Found a unique differentiation angle"]

### My Updated Assessment

| Factor | Original | My Correction | Impact |
|--------|----------|---------------|--------|
| Demand | [Original] | [My data] | [Better/Worse/Same] |
| Competition | [Original] | [My data] | [Better/Worse/Same] |
| Margins | [Original] | [My data] | [Better/Worse/Same] |
| Capital fit | [Original] | [My data] | [Better/Worse/Same] |
| Objections | [Original] | [My data] | [Better/Worse/Same] |

### My Go/No-Go Assessment
Based on my corrections, I believe this is a: [GO / NO-GO / PROCEED WITH CAUTION]

**Because:** [Your rationale]

### Additional Context
[Any other factors to consider in the summary]
```

---

## Launch Strategy Overlay

**Use when:** You have your own launch playbook to incorporate.

```markdown
## LAUNCH STRATEGY OVERLAY

### My Launch Method
**Primary approach:** [Organic / PPC Heavy / Influencer / Giveaway / Hybrid]

### Pre-Launch Checklist
- [ ] [Your step 1]
- [ ] [Your step 2]
- [ ] [Your step 3]
- [ ] [Your step 4]
- [ ] [Your step 5]

### Launch Week Plan
| Day | Activity | Budget |
|-----|----------|--------|
| Day 1 | [Activity] | $[X] |
| Day 2 | [Activity] | $[X] |
| Day 3 | [Activity] | $[X] |
| Day 4-7 | [Activity] | $[X] |

### PPC Strategy
**Campaign structure:**
- Auto campaign: $[X]/day
- Exact match: $[X]/day
- Phrase match: $[X]/day
- Product targeting: $[X]/day

**Target ACoS:** [X]%
**Launch ACoS tolerance:** [X]%

### Review Strategy
**Target reviews in 30 days:** [Number]
**Methods:**
1. [Method 1 - e.g., Vine]
2. [Method 2 - e.g., Follow-up emails]
3. [Method 3 - e.g., Insert cards]

### Success Metrics
| Metric | Week 1 Target | Month 1 Target | Month 3 Target |
|--------|---------------|----------------|----------------|
| Units/day | [X] | [X] | [X] |
| Reviews | [X] | [X] | [X] |
| BSR | [X] | [X] | [X] |
| ACoS | [X]% | [X]% | [X]% |

### Contingency Plans
**If sales are slow:** [Your plan]
**If reviews are negative:** [Your plan]
**If competitor responds:** [Your plan]
**If stockout risk:** [Your plan]

### Incorporate Into Reports
Please add this launch strategy context to:
- [ ] Cash Flow (update timeline and PPC budget)
- [ ] Highlight Summary (add launch plan section)
- [ ] Create new "Launch Plan" appendix
```

---

## Multi-Report Batch Correction

**Use when:** You have data that affects multiple reports at once.

```markdown
## BATCH CORRECTION

### Data That Affects Multiple Reports

**My real search volume data:**
[Paste your Helium 10 / Data Dive export or key numbers]

**My supplier quotes:**
[Paste your supplier communication or key numbers]

**My budget reality:**
- Total available: $[X]
- Timeline: [X] months to launch

**My differentiation:**
[Your angle in 2-3 sentences]

### Reports to Update
Please update ALL of these reports with my data:
- [ ] 02 - Demand (use my search volumes)
- [ ] 08 - Landed Costs (use my supplier quotes)
- [ ] 09 - Cash Flow (use my budget)
- [ ] 06 - Differentiation (use my angle)
- [ ] Highlight Summary (recalculate recommendation)

### Specific Instructions
[Any other guidance for Claude]
```

---

## Tips for Best Results

### Before Correcting
1. **Have your data ready** - Export from tools, don't guess
2. **Be specific** - Real numbers beat estimates
3. **Note your sources** - Helps Claude understand confidence level

### During Q&A with Claude
- Ask Claude to **explain changes** it makes
- Request **sensitivity analysis** ("What if search volume is 20% lower?")
- Ask for **risk flags** based on your data

### After Correction
- **Compare** original vs corrected reports
- **Validate** that changes make sense
- **Update Highlight Summary** last (after all other corrections)

---

*Report Correction Guide | Amazon Product Research Pipeline | Module 5*
