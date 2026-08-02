---
name: investment-team
description: "AI Value Investing Agents skill: Investment Research Team: Four-Role Parallel Analysis Framework. Source: skills/investment-team.md."
---

## Codex adapter note

This skill is generated from `skills/investment-team.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Investment Research Team: Four-Role Parallel Analysis Framework

Analyze $ARGUMENTS using a real multi-Agent investment research team created with the Team tools.

## Workflow

### Step 1: Show the Team Structure

Present this structure before launch:

| Role | Responsibility | Framework |
|---|---|---|
| **team-lead** — you | Coordination, synthesis, final report | Four-master integrated framework |
| **business-analyst** | Business model and moat | Duan Yongping lens |
| **financial-analyst** | Financial statements and valuation | Buffett lens |
| **industry-researcher** | Industry structure and competition | Munger lens |
| **risk-assessor** | Risk and management assessment | Li Lu lens |

### Step 1.5: AI Research-Bias Assessment

Rate the company’s information richness before creating the team:

| Rating | Characteristics | Research adjustment |
|---|---|---|
| A — Information-rich | Long public history and broad coverage | Emphasize disconfirming evidence and non-consensus views; avoid polished restatements of consensus |
| B — Moderate information | Recent listing or limited coverage | Every Agent must label estimates and confidence; the team lead must disclose data sufficiency |
| C — Information-scarce | Obscure, newly listed, or emerging-market company | Use first-principles mode; do not optimize for a complete-looking report |

**Important**: abundant information is not the same as high certainty. AI confidence is not investment certainty. Certainty must come from the economics of the business.

Pass the rating and its implications to every Agent.

### Step 1.75: WebSearch Permission Preflight

Before launching background Agents, verify that WebSearch is allowed. Background Agents cannot request interactive permissions, so blocked web access can silently degrade the workflow into stale, training-only analysis.

Run:

```bash
grep -l '"WebSearch"' .claude/settings.local.json ~/.claude/settings.local.json 2>/dev/null
```

If neither file allows WebSearch, **stop before creating Agents** and tell the user:

> ⚠️ WebSearch is not allowed. Background research Agents would be unable to browse and could produce stale analysis. Add `"WebSearch"` to `permissions.allow` in `.claude/settings.local.json`, or enable it through `/permissions`, and run the command again.

If permission is present, continue.

### Step 2: Create the Team

Use `TeamCreate`:

- `team_name`: `{company-name}-research`, lowercase English, such as `meituan-research`
- `agent_type`: `team-lead`

### Step 3: Create Four Tasks

Use `TaskCreate`. Every task must include `subject`, `description`, and `activeForm`.

#### Task 1: Business Model Analysis

- `subject`: `Analyze {company} business model, moat, and customer value`
- Include:
  1. Business essence and revenue mix
  2. Product or platform flywheel
  3. Brand, switching costs, network effects, scale, and technology
  4. Value created for each customer group
  5. Business portfolio and synergies
  6. Duan Yongping “good business” test: differentiation, pricing power, durability
  7. Latest filings, industry reports, and public information

#### Task 2: Financial and Valuation Analysis

- `subject`: `Analyze {company} financials, profitability, and valuation`
- Include:
  1. Three- to five-year revenue, net-income, and operating-income trends
  2. ROE, ROA, gross margin, and operating margin
  3. Operating cash flow, free cash flow, and capex
  4. Cash, leverage, and liquidity
  5. P/E, P/S, P/B, EV metrics vs history and peers
  6. Intrinsic value vs market price
  7. Mandatory tool verification:

```bash
python3 tools/financial_rigor.py verify-market-cap --price {price} --shares {shares} --reported {market_cap} --currency {currency}
python3 tools/financial_rigor.py verify-valuation --price {price} --eps {eps} --bvps {book_value_per_share}
python3 tools/financial_rigor.py cross-validate --field {field} --values '{JSON}' --unit {unit}
python3 tools/financial_rigor.py three-scenario --price {price} --eps {eps} --shares {shares_in_100_millions} --growth {bull} {base} {bear} --pe {bull_pe} {base_pe} {bear_pe}
```

Embed the tool output as a verification record. Mental arithmetic is prohibited.

#### Task 3: Industry and Competition

- `subject`: `Analyze {industry} structure and {company} competitive position`
- Include:
  1. Market size, growth, and penetration
  2. Competitor market share and strategy
  3. Threat assessment for major competitors
  4. Segment structure
  5. Technology, regulation, and new entrants
  6. Value distribution across the supply chain
  7. Latest industry and competitive information

#### Task 4: Risk and Management

- `subject`: `Assess {company} investment risks and management quality`
- Include:
  1. CEO capability, integrity, strategy, capital allocation, and decision record
  2. Current and potential regulation
  3. Competitive risk
  4. Business risk, including losses and expansion uncertainty
  5. Macro and industry-cycle exposure
  6. Ownership, related-party transactions, and shareholder returns
  7. Ten-year durability and disruption risks
  8. Latest regulatory developments and management statements

### Step 4: Launch Four Agents in Parallel

Call the Task tool four times **in the same message**.

Each Agent uses:

- `subagent_type`: `general-purpose`
- `run_in_background`: `true`
- `team_name`: the team name
- `name`: `business-analyst`, `financial-analyst`, `industry-researcher`, or `risk-assessor`

Use this prompt pattern:

```text
You are the {role} on the {company} investment research team, analyzing the company through the {master} investment lens.

Complete task #{task_number}: {task_subject}

Requirements:
{task_description}

Research method:
- Use WebSearch for current filings, industry reports, and news.
- Financial data must come from two independent sources under `skills/financial-data.md`.
- For U.S. stocks use Macrotrends + StockAnalysis; Hong Kong use AAStocks + Macrotrends; A-shares use Eastmoney + CNInfo; Taiwan use FinMind `tools/twstock_data.py` + Goodinfo.
- Flag source discrepancies greater than 1%.
- Cite material figures and distinguish facts from inference.
- If WebSearch is blocked, do not pretend the report is current. Put a prominent warning at the top, state the knowledge cutoff, reduce confidence, and notify team-lead.

Output:
- Detailed Markdown report with tables
- Explicit conclusions and scores for each dimension
- Overall conclusion for this role

When complete:
1. Mark the task completed using TaskUpdate.
2. Send the full report to team-lead using SendMessage with type `message` and recipient `team-lead`.
```

### Step 5: Receive Reports and Track Progress

- Show a live progress table to the user.
- When each report arrives, show three to five core findings.
- Wait until all four reports are received.

### Step 6: Shut Down Team Members

After receiving all four reports, send a `shutdown_request` to each Agent using SendMessage.

### Step 7: Produce the Integrated Report

Synthesize the four reports into this structure:

#### 1. One-Sentence Verdict

A 50–100 word paragraph stating whether the company deserves investment consideration and why.

#### 2. Four-Dimension Scorecard

| Dimension | Framework | Score — 1 to 5 stars | Core judgment |
|---|---|---|---|

Show the composite score.

#### 3. Core Data Snapshot

Show major financial and operating metrics for the latest two years.

#### 4. Dimension Summaries

Give three to five important findings per dimension.

#### 5. Bull vs Bear

- Five to seven bull arguments
- Five to seven bear arguments

#### 6. Buffett Pre-Purchase Checklist

| # | Test | Pass? | Explanation |
|---|---|---|---|

Evaluate ten material tests.

#### 7. Final Investment Guidance

- Qualitative table covering business quality, management, valuation, and timing
- Tiered guidance for aggressive, moderate, and conservative investors, including price ranges
- Three to five add signals and three to five reduce signals

#### 8. Final Summary

A 100–200 word conclusion.

### Step 8: Save the Report

Write it to `~/{company}-investment-research-report_{YYYYMMDD}.md`.

### Step 9: Data Spot-Check — Publication Gate

```bash
python3 tools/report_audit.py extract --report <report_file_path>
# Independently retrieve each sampled item under skills/financial-data.md
python3 tools/report_audit.py verdict --results '<completed_JSON>' --report <report_file_name>
```

- **PASS FOR PUBLICATION**: all sampled discrepancies are ≤1%
- **RETURN FOR CORRECTION**: any sampled discrepancy exceeds 1%; correct and repeat

### Step 10: Delete the Team

Use `TeamDelete` to clean up team resources.

## Mandatory Rules

1. Launch all four Agents in parallel in the same message.
2. Agents report through SendMessage, not shared report files.
3. Browse for current data and cross-validate material figures.
4. Give an explicit buy / watch / avoid conclusion and concrete price ranges.
5. Support conclusions with data and sources.
6. Keep the user updated while Agents work.
7. Include the information-richness rating and AI limitations in the final report.
8. When information is scarce, leave explicit unknowns instead of filling the framework with speculation.
