---
name: investment-research
description: "AI Value Investing Agents skill: Investment Research: Buffett–Munger–Duan Yongping–Li Lu Comprehensive Framework. Source: skills/investment-research.md."
---

## Codex adapter note

This skill is generated from `skills/investment-research.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Investment Research: Buffett–Munger–Duan Yongping–Li Lu Comprehensive Framework

Perform a systematic investment research analysis of $ARGUMENTS.

## Research Framework

Use the methodologies of Warren Buffett, Charlie Munger, Duan Yongping, and Li Lu. Execute the following eight modules in order.

### Preliminary Step: AI Research Bias Awareness (Mandatory)

Before beginning the research, assess the company's **AI researchability** and identify potential data biases.

**Information richness rating**:

| Rating | Characteristics | AI research trap | Response strategy |
|---|---|---|---|
| A — Information-rich | Public for many years, broad analyst coverage, extensive media reporting | Consensus is too strong; AI output converges toward market pricing and offers limited alpha | Emphasize disconfirming evidence: Why are smart investors not buying? Which risks are overlooked? |
| B — Moderate information | Public for 1–3 years, limited coverage, some data must be estimated | AI may fill gaps with “reasonable assumptions,” creating a complete-looking report with false certainty | Assign confidence levels to every estimate and distinguish evidence-based inference from unsupported filling |
| C — Information-scarce | Newly listed, obscure stock, emerging market, almost no coverage | AI may become excessively conservative and confuse “hard to see” with “bad” | Use first-principles questions to extract the business essence from limited information |

**First-principles method for C-rated companies**:

When public information is insufficient, do not assemble a report that merely looks complete. Focus on these underlying questions:

1. Who is the customer? Why do they pay? What alternatives do they have?
2. What drives repeat purchases: habit, lock-in, or continuous creation of new value?
3. Could a competitor reproduce this business with 10 billion in capital?
4. Which important decisions has management made, and what do they reveal about judgment and values?

**Bias self-checklist** — remain alert throughout the research:

- [ ] Does my sense of certainty come from the business itself or from the quantity of available information?
- [ ] Would my conclusion change if the amount of available material were cut in half?
- [ ] Is the AI analysis nearly identical to market consensus? If so, where is the informational advantage?
- [ ] Am I underestimating the possibility of a great business with very little public information?

Place the information-richness rating at the beginning of the report. In the final conclusion, explicitly distinguish **AI research confidence** from **actual investment certainty**.

### Step 1: Data Collection

> **Data-source standard**: Follow `skills/financial-data.md`. Every material financial figure must come from two independent sources; flag discrepancies greater than 1%.
>
> - U.S. stocks: Macrotrends as primary + StockAnalysis as secondary
> - Hong Kong stocks: AAStocks as primary + Macrotrends ADR as secondary
> - A-shares: Eastmoney as primary + CNInfo as secondary

Use the Task tool to launch a research Agent that gathers the following from the web:

1. Revenue mix: segment revenue, growth, and gross margin for the latest fiscal year and trailing four quarters
2. Financial metrics: five-year revenue, net income, gross margin, operating margin, free cash flow, and cash reserves
3. Competitive landscape: market share and comparison with major competitors
4. Business model and moat: sources of durable competitive advantage
5. Technical capability: core technology stack and R&D investment
6. Management: founder/CEO background, ownership, and record of important decisions
7. Industry outlook: total addressable market and growth forecasts
8. Risk factors: geopolitics, regulation, supply chain, and other material risks
9. Current valuation: market capitalization, P/E, P/S, PEG, and EV/Revenue
10. Core bull and bear arguments

#### Data Cross-Validation (Mandatory — Use the Financial Rigor Tool)

After collecting the data, **call `tools/financial_rigor.py` to verify material figures programmatically**. Do not rely on LLM mental arithmetic.

**Figures that must be verified**:

- Shares outstanding, confirmed by at least two sources such as the exchange, Yahoo Finance, or StockAnalysis
- Current share price and market capitalization — **manually calculate price × shares outstanding and compare it with the reported market cap to catch unit errors**
- Latest fiscal-year revenue and net income, confirmed by the annual report plus at least one third-party source
- Cash reserves and net cash: cash + short-term investments − total debt, with accounting-scope differences noted
- Management ownership, distinguishing economic ownership from voting power and accounting for dual-class structures

**Mandatory verification procedure using Bash**:

Step 1 — Verify market capitalization with exact decimal arithmetic:

```bash
python3 tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {shares_outstanding} --reported {reported_market_cap} --currency {currency}
```

Step 2 — Cross-validate material figures across sources:

```bash
python3 tools/financial_rigor.py cross-validate \
  --field {field_name} --values '{"source_1": value, "source_2": value}' --unit {unit}
```

Run this separately for revenue, net income, and cash reserves.

Step 3 — Verify valuation metrics precisely, including P/E, P/B, ROE, and FCF yield:

```bash
python3 tools/financial_rigor.py verify-valuation \
  --price {price} --eps {eps} --bvps {book_value_per_share} \
  --fcf-per-share {fcf_per_share} --dividend {dividend_per_share}
```

**Verification rules**:

1. Every material figure requires at least two independent sources.
2. When sources differ, prioritize the company filing or exchange data and explain the discrepancy.
3. **Every calculated figure must be verified with the tool. LLM mental arithmetic is prohibited.**
4. Embed the tool output directly in a report appendix titled “Material Data Cross-Validation Record.”
5. If the tool reports an excessive discrepancy, investigate and resolve it before continuing the analysis.

**Common errors to prevent**:

- Market-cap units: HKD hundreds of millions vs CNY hundreds of millions vs USD hundreds of millions; a missing or extra zero is common
- FCF definitions: sources may define capital expenditure differently, including or excluding leases and acquisitions
- Debt definitions: whether operating lease liabilities are included
- Ownership: economic ownership is not the same as voting power in dual-class companies

### Step 2: Business Essence — Duan Yongping's “Right Business”

Analyze:

- Define the essence of the business in one sentence
- Break down the revenue structure with charts
- Show the five-year profitability trend with charts
- Map the business model: one-time sales vs subscription/repeat purchase; hardware vs software vs platform
- Assess ecosystem stickiness and customer lock-in
- Compare gross margin with peers and explain why it is high or low
- Analyze operating leverage
- **Duan Yongping follow-up**: What makes this a good business? If it can be described in only one sentence, what is that sentence?

### Step 3: Moat Assessment — Buffett's “Economic Moat”

Verify each moat category individually:

| Moat type | Verification question |
|---|---|
| Brand / pricing power | Can the company raise prices without losing sales volume? |
| Switching costs | How costly is it for customers to move to a competitor? |
| Network effects | Does the product improve as more people use it? |
| Scale economies | How large is the cost advantage created by scale? |
| Technology / patents | How many years ahead is the technology, and can it be copied? |

Assess the moat trend: Has it widened or narrowed during the past five years? What is likely during the next five years?

**Buffett follow-up**: Will this moat still exist in ten years? What could destroy it?

### Step 4: Inversion and Risk Register — Munger's “Invert, Always Invert”

- List every plausible path by which the company could fail in a table with path, probability, and impact
- Find historical analogues: Which companies occupied a similar position, and what happened to them?
- Cross-check using multidisciplinary models such as network effects, technology adoption curves, and competitive game theory
- Audit narrative bias, anchoring, and survivorship bias
- Collect the strongest bear arguments

**Munger follow-up**: Where am I most likely to be wrong? Why would smart investors avoid or short this company?

### Step 5: Management Assessment — Duan Yongping's “Right People” + Buffett's Integrity Test

- Review important CEO/founder decisions in a table with date, decision, outcome, and score
- Evaluate capital allocation: R&D returns, acquisition success, and timing of buybacks
- Assess alignment with shareholders: management ownership, compensation structure, and share-sale history
- Assess organizational capability: team stability and key-person risk
- Identify defining cultural characteristics

**Duan Yongping follow-up**: If the CEO retired, could the company preserve its competitiveness?

### Step 6: Industry and Civilizational Trends — Li Lu's Civilization Framework

- Determine whether the industry is undergoing a civilization-scale paradigm shift
- Compare it with historical technological revolutions such as steam, electricity, the internet, and AI
- Analyze the TAM growth curve and ultimate ceiling
- Locate the company within the industry value chain
- Assess technology-path risk
- Analyze customer and supplier concentration

**Li Lu follow-up**: Looking back from twenty years in the future, is this company the Standard Oil of its era or a short-lived 3Com?

### Step 7: Valuation and Margin of Safety — Buffett's Intrinsic Value + Duan Yongping's Right Price

- Present current market pricing in a table of material valuation metrics — **all calculations must be tool-verified**
- Perform a reverse DCF: What growth expectations are embedded in the current price?
- Run a three-scenario valuation — **use the tool for exact calculations; no mental arithmetic**:

```bash
python3 tools/financial_rigor.py three-scenario \
  --price {price} --eps {eps} --shares {shares_in_100_millions} \
  --growth {bull_growth} {base_growth} {bear_growth} \
  --pe {bull_pe} {base_pe} {bear_pe} --years 3 --currency {currency}
```

- Compare with the company's historical valuation
- Compare with peer valuations

**Duan Yongping follow-up**: If the stock market closed tomorrow for five years, would you be willing to hold at this price?

### Step 8: Integrated Decision Memo

Create the following summary table:

| Dimension | Conclusion | Confidence |
|---|---|---|
| Business quality — Duan Yongping | | |
| Moat — Buffett | | |
| Management — Duan Yongping + Buffett | | |
| Largest risk — Munger | | |
| Civilizational trend — Li Lu | | |
| Valuation — Buffett + Duan Yongping | | |

Create a final decision table:

| Investor situation | Recommendation |
|---|---|
| No current position | |
| Existing holder | |
| Sell signals | |
| Add signals | |

Add simulated commentary from all four masters using blockquotes. Clearly label it as a framework-based simulation, not an authentic quotation.

## Output Requirements

1. Support every analysis with data and cite the sources.
2. Use Markdown tables for material data.
3. End every module with the corresponding master's follow-up question.
4. Write the complete report to `~/[company-name]-investment-research-report.md`.
5. Give a clear buy / watch / avoid conclusion rather than evading a decision.
6. Provide concrete price ranges in the valuation section.
7. At the **beginning of the report**, include the A/B/C information-richness rating and an “AI Research Limitations” statement.
8. At the **end of the report**, distinguish AI analysis confidence from investment certainty. Identify which conclusions rest on strong data and which rely on inference from limited information.
9. For a C-rated company, include a “Questions Requiring First-Hand Verification” list and suggest product testing, field research, or supply-chain interviews to address AI blind spots.

## Data Spot-Check — Publication Gate

After writing the report, **perform the data spot-check and publish only after it passes**.

Step 1 — Extract a random 15% audit sample:

```bash
python3 tools/report_audit.py extract \
  --report <report_file_path>
```

The command returns a JSON template whose items contain an empty `fetched_value` field.

Step 2 — Independently retrieve each sampled value:

For every item, follow `skills/financial-data.md` and fill in `fetched_value`, `fetched_source`, `fetched_value2`, and `fetched_source2`.

- U.S. stocks: Macrotrends + StockAnalysis
- Hong Kong stocks: AAStocks + Macrotrends
- A-shares: Eastmoney + CNInfo

Step 3 — Produce the audit verdict:

```bash
python3 tools/report_audit.py verdict \
  --results '<completed_JSON>' \
  --report <report_file_name>
```

- **PASS FOR PUBLICATION**: every sampled discrepancy is ≤ 1%; the report may be published
- **RETURN FOR CORRECTION**: any sampled discrepancy is > 1%; correct the affected data and repeat the audit until it passes
