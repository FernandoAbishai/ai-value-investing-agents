---
name: earnings-review
description: "AI Value Investing Agents skill: Earnings Review: Primary-Source Deep Reading. Source: skills/earnings-review.md."
---

## Codex adapter note

This skill is generated from `skills/earnings-review.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Earnings Review: Primary-Source Deep Reading

Perform a detailed earnings review of $ARGUMENTS.

**Supported input**: `company period`, for example `Tencent 2025Q4`, `PDD 2025 annual report`, or `Meituan latest`. When no period is supplied, use the latest available filing.

## Purpose

Most AI investment workflows rely on secondary summaries. This workflow prioritizes original filings, earnings-call transcripts, shareholder letters, and investor-day materials. The objective is not to repeat reported figures, but to determine what changed in the business, financial quality, management credibility, and investment thesis.

## Process

### Preliminary Step: Source Availability Rating

| Rating | Available material | Effect on analysis |
|---|---|---|
| A | Complete filing and transcript | Execute every section normally |
| B | Partial original material or reliable third-party compilation | Label non-primary material and reduce confidence in footnote analysis |
| C | Only news reports and data-site summaries | Focus on core financial changes, skip unsupported footnote conclusions, and state that primary-source coverage is insufficient |

### Step 1: Retrieve Primary Materials

Launch research Agents in parallel to retrieve:

1. The original filing from company IR, SEC EDGAR, HKEXnews, CNInfo, or the relevant regulator
2. The earnings-call transcript or recording
3. The shareholder letter, when applicable
4. Recent investor-day or analyst-day materials
5. The prior-period filing and transcript for promise tracking

When complete originals cannot be obtained, follow `skills/financial-data.md` and use the standard two-source combinations. Label the material as third-party rather than primary, and flag discrepancies greater than 1%.

### Step 2: Extract and Verify Core Financial Data

#### 2.1 Income Statement

| Metric | Current period | Prior period | YoY change | Guidance | Assessment |
|---|---|---|---|---|---|

Cover:

- Total revenue and revenue by segment and geography
- Gross profit and gross margin
- Operating profit and margin, distinguishing GAAP and non-GAAP
- Net income, including material non-recurring items
- Basic and diluted EPS

#### 2.2 Cash Flow — Highest Priority

| Metric | Current period | Prior period | Change | Interpretation |
|---|---|---|---|---|

Cover:

- Operating cash flow relative to net income; above 100% is strong, below 80% requires scrutiny
- Capital expenditure, separating maintenance from expansion where possible
- Free cash flow = operating cash flow − capital expenditure
- Buybacks and dividends
- Ending cash and equivalents

#### 2.3 Balance-Sheet Health

Cover:

- Cash plus short-term investments versus interest-bearing debt
- Net cash or net debt trend
- Receivables days and whether credit terms appear to be loosening
- Inventory days and signs of accumulation
- Goodwill and intangible assets and potential impairment risk

#### 2.4 Programmatic Verification

Use `tools/financial_rigor.py` for material calculations and cross-validation. Do not use mental arithmetic.

```bash
python3 tools/financial_rigor.py cross-validate \
  --field revenue --values '{"company_filing": 108.3e9, "secondary_source": 107.9e9}' --unit USD

python3 tools/financial_rigor.py verify-market-cap \
  --price 101 --shares 1.488e9 --reported 1.44e11 --currency USD

python3 tools/financial_rigor.py verify-valuation \
  --price 101 --eps 9.6 --bvps 26.5 --fcf-per-share 10.2
```

Embed the tool output in the report's validation appendix.

### Step 3: Read Management Discussion and Q&A

#### 3.1 Tone Analysis

| Signal | What to look for |
|---|---|
| Candid | Management acknowledges problems and explains causes precisely |
| Clear | Strategy includes concrete actions and measurable goals |
| Vague | Repeated confidence language without substance |
| Deflecting | Direct questions are answered with unrelated talking points |
| Externalizing | Problems are attributed entirely to macro or competitors |

Quote or accurately paraphrase the relevant passage and cite the source. Do not invent management language.

#### 3.2 Promise Tracking

Extract specific commitments from the prior filing or call and compare them with current outcomes.

| Prior commitment | Current outcome | Assessment |
|---|---|---|
| | | Met / Partially met / Missed |

#### 3.3 Hardest Questions

Identify the most challenging analyst questions and assess the quality of management's response.

| Analyst question | Management response | Quality 1–5 | Avoided? |
|---|---|---:|:---:|

### Step 4: Footnotes and Hidden Information

Check:

- Related-party transactions
- Stock-based compensation and dilution
- Contingent liabilities, litigation, guarantees, and commitments
- Accounting-policy changes
- Segment profitability and cross-subsidization
- Customer and supplier concentration

Flag abnormal patterns:

- Receivables growing faster than revenue
- Inventory growing faster than revenue
- Operating cash flow falling below net income with a widening gap
- Sudden growth in capitalized costs
- Rising dependence on non-recurring gains

### Step 5: Historical Comparison

Place the current period in at least a four-quarter or three-year series.

| Metric | Q-4 | Q-3 | Q-2 | Q-1 | Current | Trend |
|---|---|---|---|---|---|---|

Determine whether revenue growth, margins, cash conversion, and capital intensity are improving or deteriorating.

Compare actual results with prior guidance:

| Metric | Prior guidance | Actual | Variance | Interpretation |
|---|---|---|---|---|

### Step 6: Produce the Earnings Review

Use this structure:

1. One-page core data table
2. Three most important changes, within 500 words total
3. Management tone and promise tracking
4. Hidden information in footnotes
5. Selected earnings-call questions
6. Relationship to the investment thesis
7. Conclusion: what this report changed

The conclusion must answer clearly:

1. Did results beat, meet, or miss expectations?
2. Did the investment thesis strengthen, remain unchanged, weaken, or break?
3. What is the next important catalyst or verification point?
4. For an existing holder, is the evidence more consistent with adding, holding, or reducing?

### Step 7: Save the Report

Write the report to `reports/{company}-earnings-{period}.md`.

### Step 8: Data Spot-Check — Publication Gate

```bash
python3 tools/report_audit.py extract \
  --report reports/{company}-earnings-{period}.md

python3 tools/report_audit.py verdict \
  --results '<completed_JSON>' \
  --report {report_file_name}
```

- **PASS FOR PUBLICATION**: every sampled figure passes
- **RETURN FOR CORRECTION**: correct failed figures and repeat the audit

## Principles

- Read originals rather than summaries whenever possible.
- Focus on changes and trends, not isolated numbers.
- Evaluate how management communicates, not only what it says.
- Read the footnotes.
- Produce a judgment, not a filing summary.
