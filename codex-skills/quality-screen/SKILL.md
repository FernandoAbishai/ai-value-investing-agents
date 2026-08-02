---
name: quality-screen
description: "AI Value Investing Agents skill: Quality Screen: Seven Metrics to Eliminate Clearly Inferior Companies. Source: skills/quality-screen.md."
---

## Codex adapter note

This skill is generated from `skills/quality-screen.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Quality Screen: Seven Metrics to Eliminate Clearly Inferior Companies

Apply a quality screen to $ARGUMENTS and quickly eliminate companies that do not meet first-class business standards.

**Supported inputs**:

| Mode | Example | Behavior |
|---|---|---|
| Individual companies | `Tencent, Meituan, NVIDIA` | Screen each company |
| Industry | `global cloud computing` | Identify 10–20 major listed companies, then screen each |
| Market or index | `NASDAQ 100` | Retrieve the constituent list and screen it |
| Theme | `global AI infrastructure` | Identify 15–30 relevant companies, then screen them |

For industry, market, and theme modes, also report the pass rate, relative ranking, and sector-level conclusions.

## Design Principles

- **Goal**: avoid excluding a genuinely first-class company while removing clearly inferior candidates
- **Logic**: seven hard metrics plus three exemption rules
- **Scope**: listed companies; banks and insurers are exempt from the interest-coverage test

## Seven Elimination Metrics

| # | Metric | Eliminate when | What it measures |
|---|---|---|---|
| 1 | Ten-year average ROE | Below 8% | Capital efficiency |
| 2 | Five-year cumulative free cash flow | Negative | Whether accounting profit converts to cash |
| 3 | Interest coverage, EBIT / interest | Below 2× | Debt-service capacity |
| 4 | Long-term gross margin | Below 15% | Pricing power and differentiation |
| 5 | Operating cash flow / net income, five-year average | Below 0.7 | Earnings quality |
| 6 | Long-term net margin | Below 5% | Resilience to revenue volatility |
| 7 | Five-year share-count growth | Above 20%, excluding acquisition-driven issuance | Shareholder dilution discipline |

## Exemption Rules

### Exemption A: Strategic Investment Phase — Metric 1

Exempt a low ROE result only when all are true:

1. Listed for fewer than ten years
2. Gross margin above 30%
3. Operating cash flow positive during the latest two years

This indicates that low ROE may reflect deliberate reinvestment rather than a structurally weak business.

### Exemption B: Deliberately Low Net Margin — Metric 6

Exempt a low net-margin result only when both are true:

1. Gross margin above 30%
2. Net margin has recovered above 5% during the latest two years or shows a clear upward trend

### Exemption C: High-Turnover, Low-Margin Model — Metrics 4 and 6

Exempt low gross and net margins only when all are true:

1. ROE above 20%
2. Operating cash flow / net income above 1.0
3. The model is genuinely membership-based, commission-based, or high-turnover/low-markup

This protects businesses whose economics are expressed through membership income, platform commissions, or turnover rather than product markup.

## Process

### Step 1: Parse the Input and Determine Scope

- For named companies or tickers, enter individual-company mode.
- For industries, markets, indices, or themes:
  1. Use current web sources to identify the relevant listed companies.
  2. Cover the 15–20 largest companies for an industry.
  3. Retrieve the complete constituent list for an index when practical.
  4. Cover 15–30 companies for a theme.
  5. Present the company universe before screening; process batches in parallel when there are more than 30 companies.

Resolve each company's full name, ticker, and exchange.

### Step 2: Collect Data in Parallel

Launch an independent Agent for each company and retrieve:

1. Annual ROE for up to ten years and its average
2. Operating cash flow and capital expenditure for five years; calculate cumulative FCF
3. Latest annual EBIT and interest expense; calculate interest coverage
4. Five-year gross-margin trend
5. Five-year operating cash flow / net income ratios and their average
6. Up to ten years of net margins and the average
7. Current and five-year-ago shares outstanding; calculate dilution

Prioritize company filings, then reputable research and financial-data platforms. Follow `skills/financial-data.md`, use at least two independent sources for material figures, and flag discrepancies above 1%.

Use exact calculations where applicable. Do not rely on mental arithmetic.

### Step 3: Test Each Metric

For every company and every metric, mark:

- ✅ Pass
- ❌ Fail
- ⚠️ Borderline, with the actual figure
- ⚠️→✅ Exemption applied, with the exact exemption and evidence
- Data unavailable, which must not be treated automatically as either pass or fail

### Step 4: Produce Results

```markdown
# Quality Screen Results

**Screening date**: {current date}
**Companies screened**: {N}

## Summary

| Company | ROE | FCF | Interest coverage | Gross margin | OCF/NI | Net margin | Dilution | Result |
|---|---|---|---|---|---|---|---|---|
| Example A | ✅ 24% | ✅ | ✅ | ✅ 56% | ✅ | ✅ 30% | ✅ | **Pass** |
| Example B | ❌ 3% | ❌ | ❌ | ✅ 20% | ✅ | ❌ 2% | ✅ | **Eliminate** |
| Example C | ⚠️→✅ | ✅ | ✅ | ✅ 35% | ✅ | ⚠️→✅ | ✅ | **Pass by exemption** |

## Companies Passing

## Companies Eliminated

| Company | Failed metric | Evidence | Reason |
|---|---|---|---|

## Companies Passing by Exemption

| Company | Exemption | Evidence | Reason |
|---|---|---|---|

## Borderline Cases

## Sector Summary

**Pass rate**: {passed}/{total} = {percentage}

| Quality tier | Companies | Shared characteristics |
|---|---|---|
| First class | | |
| Acceptable | | |
| Eliminated | | |

**Sector conclusion**: state whether the group deserves deeper work and identify the two or three strongest candidates.
```

## Special Cases

1. **Banks and insurers**: do not apply interest coverage; their economics are based on financial liabilities and spreads.
2. **REITs**: replace standard ROE with a suitable core-operating or adjusted return measure and explain it.
3. **Missing data**: report missing data explicitly.
4. **Cyclical companies**: use a full-cycle average covering at least one peak and one trough.
5. **Short listing history**: use all available years and label the limited window.

## Limitations

This screen can remove clearly weak companies, but passing does not prove that a company is excellent or attractively priced. Passing companies still require analysis of business durability, management quality, valuation, and competitive direction.

Elimination is the first step, not the final investment decision.
