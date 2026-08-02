---
name: private-company-research
description: "AI Value Investing Agents skill: Private Company Research: Multi-Agent Deep Research Framework. Source: skills/private-company-research.md."
---

## Codex adapter note

This skill is generated from `skills/private-company-research.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Private Company Research: Multi-Agent Deep Research Framework

Perform a team-based deep research analysis of $ARGUMENTS. This workflow is designed for private companies such as Ant Group, Xiaohongshu, SpaceX, and Stripe.

**Final objective**: under conditions of naturally scarce and uneven information, estimate the company's **real business value** rather than merely repeating its latest funding-round valuation.

## Why Private-Company Research Is Different

- There are no standardized public financial statements.
- Valuation anchors are limited and often distorted by preferred-share terms.
- Information asymmetry is much larger.
- Exit paths may include IPO, acquisition, secondary transfer, or no liquidity event.

## AI Bias Awareness — Core Requirement

Private companies create severe AI-research risks:

1. **False conservatism**: limited information is mistaken for a weak company.
2. **False precision**: plausible estimates are presented as verified facts.
3. **Comparable-company trap**: public-market valuation logic is forced onto a structurally different business.
4. **Survivorship and publicity bias**: available online information is disproportionately positive and company-controlled.

Rules:

- Prefer an explicit “unknown” over a fabricated complete table.
- Tag every material figure with confidence: 🟢 high, 🟡 medium, or 🔴 low.
- Distinguish verified fact from inference and estimation.
- When information is extremely scarce, switch to first-principles mode and answer only:
  1. Which real problem does the company solve?
  2. Why is this team unusually capable of solving it?
  3. What is the upside ceiling and the most likely failure path?
  4. Which milestone would validate or invalidate the thesis?

Information asymmetry cannot be eliminated. The goal is to identify the few facts and signals that matter most.

## Team Structure

| Role | Responsibility | Core question |
|---|---|---|
| **team-lead** | Coordination, evidence reconciliation, final decision | What is the integrated investment judgment? |
| **business-decoder** | Business model, products, users, and moat | What is the essence of the business? |
| **financial-detective** | Financial reconstruction and valuation | What do the economics probably look like? |
| **competitive-mapper** | Industry, competitors, and substitutes | Who competes with or could disrupt it? |
| **risk-governance-analyst** | Management, governance, investors, risks, and exits | What could go wrong, and who controls the company? |
| **tech-ip-analyst** | Technology stack, patents, R&D, and technical moat | Is the technology defensible and durable? |
| **signal-miner** | Hiring, app data, litigation, digital footprint, and supply-chain signals | What do unconventional data sources reveal? |

## Process

### Step 1: Create the Team

Use TeamCreate:

- `team_name`: `{company}-private-research`, lowercase English
- `agent_type`: `team-lead`

### Step 2: Create Six Tasks

Every task must include `subject`, `description`, and `activeForm`.

#### Task 1: Business Model, Product, and Users

Analyze:

- One-sentence definition of the business
- Customer problem, value proposition, and alternatives
- Demand resilience during economic stress
- Revenue model by advertising, commission, subscription, SaaS, hardware, licensing, or financial services
- Recurring versus one-time revenue and customer/channel concentration
- Unit economics: CAC, LTV, payback, marginal cost, and break-even scale
- Product portfolio, product life cycle, and flywheel effects
- Business Model Canvas across all nine standard elements
- MAU, DAU, retention, engagement, user demographics, and acquisition channels
- App-store ratings, review themes, and product-update cadence
- Pricing power and historical price changes
- Moat score from one to five across network effects, switching costs, brand, data, regulatory licenses, and scale
- International expansion when applicable

Output a clear business-quality score, moat classification, source list, and confidence assessment.

#### Task 2: Financial Reconstruction and Valuation

Build a source matrix in descending order of reliability:

1. Prospectuses and regulatory filings
2. Parent-company or related listed-company reports
3. Regulatory enforcement and compliance disclosures
4. Bond, ABS, or trust documents
5. Corporate registry records
6. Funding announcements
7. Reputable research reports
8. Deep reporting from established media
9. Industry-data inference
10. Former-employee or insider claims, used only as weak supporting evidence

Estimate, with source, date, confidence, and method:

- Revenue by year and business line
- Volume and price drivers
- Gross margin and operating expenses
- EBITDA, operating profit, and net income
- Operating cash flow, capital expenditure, free cash flow, cash burn, and runway
- Employee count, revenue per employee, and capital efficiency

Cross-validate every material figure. List all conflicting sources and explain which one is used.

Build the complete funding and valuation timeline:

| Round | Date | Amount | Pre-money | Post-money | Lead investors | Follow-on investors | Change in valuation | Notes |
|---|---|---:|---:|---:|---|---|---:|---|

Assess down rounds, insider participation, funding frequency, liquidation preferences, anti-dilution, and listing-performance clauses when evidence exists. Do not invent preferred terms.

Use five valuation methods:

1. Latest funding valuation adjusted for preference and illiquidity
2. Public comparable companies with explicit discounts and premiums
3. Bear, base, and bull DCF scenarios
4. Terminal-market-value backsolve at five and ten years
5. Recent transaction comparables

| Method | Value range | Confidence | Weight | Weighted value |
|---|---:|---|---:|---:|

Distinguish reasonable value from conservative margin-of-safety value. If evidence is inadequate, state that reliable valuation is not possible.

#### Task 3: Industry and Competition

Analyze:

- Independent definition of the company's true market
- TAM, SAM, and SOM with multiple source estimates
- Industry stage and growth drivers
- Full value-chain map, profit pools, and bargaining power
- Quantified Porter's Five Forces scorecard
- Direct competitors, cross-industry entrants, substitutes, and large-platform threats
- Two or three detailed competitor comparisons
- The latest twelve months of financing, product, hiring, and strategic changes
- Whether the market tends toward winner-take-all, oligopoly, or fragmentation
- Three scenarios: company wins, stable coexistence, or disruption
- Global public-company analogues and the limits of those comparisons

#### Task 4: Risk, Management, Governance, Investors, and Exit

Analyze:

- Founder and CEO background, strategic predictions, execution, values, controversy, and crisis behavior
- Core team quality, executive turnover, and key-person dependency
- Ownership, voting control, dual-class shares, VIE structure, board composition, and employee equity plans
- Investor roster, strategic value, fund-life pressure, secondary sales, and follow-on behavior
- Full risk register across regulation, competition, technology, talent, financing, IPO, geopolitics, monetization, governance, compliance, macro, and ESG
- Exit paths: domestic IPO, Hong Kong IPO, U.S. IPO, acquisition, secondary transfer, SPAC, or no exit
- Three concrete failure paths, liquidation value, and thesis-breaking signals
- At least five reasons a smart investor would decline the opportunity

#### Task 5: Technology and Intellectual Property

Analyze:

- Technical architecture inferred from engineering blogs, open-source projects, hiring, and conference talks
- Technology-debt and migration signals
- Patent quantity, quality, citations, jurisdictions, lawsuits, and competitor comparison
- R&D headcount, estimated spend, academic publications, conference presence, open-source output, and productization speed
- CTO and technical-leadership quality
- Talent density, hiring direction, and retention signals
- Technical moat across algorithms, data, engineering complexity, talent, and ecosystem
- How AI and other emerging technologies strengthen or threaten the business
- Risks from failed technical direction, open-source substitution, platform dependence, security incidents, and key-person loss

#### Task 6: Alternative Data and Hidden Signals

Analyze:

- Hiring scale and mix across engineering, product, sales, AI, international expansion, compliance, finance, and IR
- App-store ranking, downloads, ratings, updates, complaints, and web-traffic trends
- Social-media attention and sentiment
- Corporate-registry changes, subsidiaries, business-scope changes, litigation, enforcement, and labor disputes
- Suppliers, partners, procurement, and listed counterpart disclosures
- Domains, subdomains, SSL certificates, and trademark registrations
- Conference participation, standards involvement, and government relationships
- Secondary-market transactions and employee share sales when observable

Summarize:

| Signal category | Direction | Strength | Confidence | Key finding |
|---|---|---|---|---|
| Hiring | | | | |
| Product data | | | | |
| Sentiment | | | | |
| Legal | | | | |
| Supply chain | | | | |
| Digital footprint | | | | |
| Industry visibility | | | | |
| Secondary trading | | | | |

List every anomalous signal, especially evidence that contradicts the company's public narrative.

### Step 3: Launch Six Agents in Parallel

Launch all six Agents in the same message with:

- `subagent_type`: `general-purpose`
- `run_in_background`: `true`
- `team_name`: the created team
- `name`: the corresponding role

Use this prompt pattern:

```text
You are the {role} on the {company} private-company research team.

This is a private company. There are no standardized public financial statements, available information may conflict, and missing information must never be filled with invented certainty.

Complete task #{task number}: {subject}

Research requirements:
- Use current web research with several different query formulations in all relevant languages.
- Prefer primary regulatory and corporate documents.
- Read critical original documents rather than relying on search snippets.
- Cross-check material figures with at least two sources.
- Label each important figure with source, date, and confidence.
- Show every estimation method and assumption.
- Distinguish fact from inference.
- Mark unavailable information as missing.

At the end provide:
1. Overall score from one to five
2. Information completeness: sufficient / moderate / insufficient / severely insufficient
3. Three most important findings
4. The largest information blind spot

Mark the task completed and send the full report to team-lead.
```

### Step 4: Track Progress

Show which Agents are complete, which remain active, and three to five findings from each completed report.

### Step 5: Reconcile Evidence Before Synthesis

The Team Lead must:

1. **Resolve data conflicts**: list every source, choose one only with an explicit reason, or retain a range.
2. **Test signal consistency**:
   - Growth narrative versus hiring trend
   - Technical-leadership claims versus patent and talent evidence
   - Valuation versus competitive position
   - Management narrative versus observed actions
3. **Map information coverage**:
   - White zone: verified
   - Gray zone: partial evidence
   - Black zone: unknown
4. **Audit bias**: ensure negative evidence is not materially less developed than positive evidence.

### Step 6: Produce the Final Report

Use this structure:

1. One-sentence real-value judgment
2. Company profile with confidence tags
3. Six-dimension scorecard
4. Cross-validated data mosaic
5. Signal-consistency matrix
6. Three to five findings from each dimension
7. Business essence and moat scorecard
8. Five-method valuation table and conservative/base/bull value range
9. Bull and bear cases, each with evidence
10. Risk matrix and top three risks
11. Exit-path assessment
12. One-page decision memo
13. Information-blind-spot map
14. Ongoing monitoring checklist
15. Final 150–250 word conclusion

The decision memo must include:

- Company stage and latest observable valuation
- Three-sentence thesis
- Conservative and reasonable value ranges
- Current valuation comparison and margin of safety
- Three key assumptions with metrics and validation dates
- Thesis-breaking risks and stop conditions
- Invest / watch / avoid conclusion
- Expected exit route, time frame, return multiple, and annualized return range when supportable

Provide separate guidance for lead investors, follow-on investors, secondary buyers, post-IPO buyers, and investors who should not participate.

### Step 7: Save and Clean Up

Write the final report to:

`reports/{company}/{company}-private-{YYYYMMDD}.md`

Then use TeamDelete to remove team resources.

## Mandatory Rules

1. Launch all six Agents in parallel.
2. Attach source, date, and confidence to every material figure.
3. Show all estimation logic.
4. Use at least two sources for material data when possible.
5. Perform cross-dimension signal-consistency tests.
6. Give a clear invest / watch / avoid conclusion with an explicit confidence level.
7. Search in all languages relevant to the company.
8. Treat alternative data as potentially valuable, not automatically as noise.
9. Never equate limited information with a weak business.
10. Leave gaps rather than manufacturing completeness.
11. If reliable valuation is impossible, state that directly.
