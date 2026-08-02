---
name: thesis-tracker
description: "AI Value Investing Agents skill: Investment Thesis Tracker: A Post-Purchase Discipline System. Source: skills/thesis-tracker.md."
---

## Codex adapter note

This skill is generated from `skills/thesis-tracker.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Investment Thesis Tracker: A Post-Purchase Discipline System

Run an investment-thesis tracking review for $ARGUMENTS.

**Supported input formats**:
- `Company Name` — create a thesis on first use; review it on later uses.
- `Company Name rebuild thesis` — force creation of a new thesis.
- `Company Name quarterly review` — review the thesis using the latest reporting period.

> Buying is the beginning, not the end. The thesis must be monitored throughout the holding period.
>
> When the facts change, the conclusion must be reconsidered.

## Purpose

Many investors follow this process: research → buy → hope. Without a post-purchase system, they may:
- Refuse to sell after the thesis has broken.
- Panic-sell because the price fell even though the thesis remains intact.
- Forget the original reason for owning the company.

Write the exit conditions before or at the time of purchase, then evaluate the thesis against observable evidence each quarter or after a material event.

## Workflow

### Step 1: Select the Operating Mode

Check whether `reports/{company-name}-thesis.md` exists:
- If it does not exist, enter **Mode A: Build the Thesis**.
- If it exists, enter **Mode B: Review the Thesis**.
- If the user says a thesis exists but the file cannot be found, locate the referenced file or request its path only when the available workspace cannot resolve it.

---

## Mode A: Build the Thesis

### A0: Collect Baseline Data

Use WebSearch or the closest available research tools to obtain:
- Current share price.
- Current valuation metrics, including P/E, P/B, and dividend yield when applicable.
- Core figures from the latest financial statements.

If an `/investment-research` or `/investment-team` report already exists, use it as the primary research base and refresh time-sensitive data.

Validate valuation inputs with `tools/financial_rigor.py verify-valuation`.

Record the data date and source quality.

### A1: Write the Core Thesis in No More Than 200 Words

The thesis must answer these five questions, ideally in one sentence each:

```text
I am buying or holding {company} at {price} because:
1. The business earns money by ______, and I understand the economic engine.
2. Its moat is ______ and is widening / stable.
3. Management is ______, supported by ______.
4. The current price represents approximately ______ of estimated intrinsic value, and the margin of safety comes from ______.
5. Even if the thesis is wrong, downside may be limited because ______.
```

If the five statements cannot be completed clearly, the decision is not yet sufficiently defined.

### A2: Define Testable Assumptions

Break the thesis into three to seven specific assumptions:

| # | Core Assumption | Validation Method | Review Frequency | Current Status |
|---|---|---|---|---|
| 1 | Revenue growth remains above 15% | Quarterly revenue growth | Quarterly | 🟢 Supported |
| 2 | Gross margin remains above 60% | Reported gross margin | Quarterly | 🟢 Supported |
| 3 | Management continues disciplined repurchases | Filings and cash-flow statement | Quarterly | 🟢 Supported |
| 4 | Competitors do not achieve a material breakthrough | Industry data and competitor filings | Semiannual | 🟢 Supported |

Avoid vague assumptions such as “the company is good.” Every assumption must be measurable or falsifiable.

### A3: Define Red Lines

A red line triggers mandatory reassessment. Define company-specific conditions before they occur:

| # | Red-Line Condition | Severity | Required Response |
|---|---|---|---|
| 1 | Management-integrity failure, fraud, or abusive related-party transactions | Fatal | Exit unless evidence clearly disproves the event |
| 2 | Core-business revenue declines for two consecutive quarters | Severe | Reduce exposure and rebuild the thesis |
| 3 | A competitor demonstrably neutralizes the core moat | Severe | Start deep research and evaluate exit |
| 4 | Regulation fundamentally impairs the business model | Severe | Re-estimate intrinsic value |
| 5 | Unplanned large-scale insider selling | Warning | Investigate the cause |

The principal reasons to sell are:
1. The original analysis was wrong.
2. The business or thesis changed materially.
3. A clearly superior opportunity exists after considering taxes, risk, and switching costs.

### A4: Record Valuation Anchors

| Metric | Entry | Bull Case | Base Case | Bear Case |
|---|---:|---:|---:|---:|
| Share price | | | | |
| P/E | | | | |
| Market capitalization | | | | |
| Estimated intrinsic value | | | | |
| Margin of safety | | | | |

State the assumptions, date, currency, share count, and calculation method behind every intrinsic-value estimate.

### A5: Save the Thesis

Write the thesis to `reports/{company-name}-thesis.md`, including:
- Creation date.
- Entry price and position size when available.
- Core five-sentence thesis.
- Testable assumptions.
- Red-line conditions.
- Valuation anchors.
- An initially empty review-history table.

---

## Mode B: Review the Thesis

### B1: Read the Existing Thesis

Load from `reports/{company-name}-thesis.md`:
- Core thesis.
- Assumption list.
- Red-line list.
- Valuation anchors.
- Most recent review record.

Do not silently rewrite the original thesis. Preserve it as a historical record and document changes explicitly.

### B2: Collect Current Evidence

Collect:
1. New financial statements or operating data.
2. Material events, including management changes, regulation, litigation, and competitive developments.
3. Current price and valuation metrics.
4. Insider transactions and major shareholder activity.

Prioritize primary sources. Record the data cutoff date and label source gaps.

### B3: Test Every Core Assumption

| # | Core Assumption | Prior Status | New Evidence | Current Status | Change |
|---|---|---|---|---|---|
| 1 | Revenue growth above 15% | 🟢 Supported | Q4 growth was 12% | 🟡 Weakening | ⚠️ |
| 2 | Gross margin above 60% | 🟢 Supported | Gross margin was 61.2% | 🟢 Supported | — |

Status definitions:
- 🟢 **Supported** — current evidence supports the assumption.
- 🟡 **Weakening** — still within an acceptable range, but the trend is unfavorable.
- 🔴 **Impaired** — current evidence materially contradicts the assumption.
- ⚫ **Broken** — the assumption has been falsified.

Distinguish temporary volatility from structural change. Explain the evidence required to upgrade or downgrade each status.

### B4: Check Every Red Line

| # | Red-Line Condition | Triggered? | Evidence |
|---|---|:---:|---|
| 1 | Management-integrity failure | No | — |
| 2 | Two consecutive quarters of core-business decline | No | — |

Any triggered red line must be prominently disclosed with a specific action recommendation. Do not bury it in a general summary.

### B5: Update Valuation

| Metric | Entry | Previous Review | Current | Change |
|---|---:|---:|---:|---:|
| Share price | | | | |
| P/E (TTM) | | | | |
| Estimated intrinsic value | | | | |
| Margin of safety | | | | |

Recalculate rather than merely copying a market-data provider. State whether the change in intrinsic value comes from business performance, revised assumptions, dilution, discount rates, or valuation methodology.

### B6: Produce the Review Report

#### Report Structure

```text
1. Thesis health score out of 10
2. Core-assumption review table
3. Red-line review table
4. Key changes since the previous review, no more than 500 words
5. Updated valuation
6. Conclusion and action recommendation
7. Evidence and events to monitor before the next review
```

#### Thesis Health Formula

```text
Health score = 10
             - 3 × number of broken assumptions
             - 2 × number of impaired assumptions
             - 1 × number of weakening assumptions
             - 5 × number of triggered red lines
```

Floor the score at 1 and cap it at 10. The formula is a discipline aid, not a substitute for judgment. A fatal integrity event may justify exit regardless of the numeric score.

| Score | Meaning | Default Action |
|:---:|---|---|
| 9–10 | All material assumptions remain supported; thesis may be stronger | Consider adding only if valuation and portfolio constraints permit |
| 7–8 | Core assumptions hold with limited weakening | Hold |
| 5–6 | One or two assumptions are impaired, but the core thesis survives | Hold with heightened monitoring or reduce modestly |
| 3–4 | Multiple assumptions are impaired; the foundation is unstable | Consider reducing materially |
| 1–2 | A red line is triggered or a core assumption is broken | Strongly consider exiting |

#### Required Conclusions

Answer clearly:
1. **Is the thesis intact?** Intact / Weakening / Impaired / Broken.
2. **What action is appropriate?** Add / Hold / Reduce / Exit.
3. **When should the next review occur?** After the next report, after a specified event, or on a concrete date.

### B7: Update the Thesis File

Append the review to the history table in `reports/{company-name}-thesis.md`:

| Review Date | Health Score | Core Change | Recommended Action |
|---|:---:|---|---|
| 2026-04-09 | 7/10 | Revenue growth slowed to 12%, while margins improved | Hold |

Also update each assumption's current status without deleting prior evidence.

## Core Principles

- **Define exit conditions before emotions take over.** Decisions made calmly are more reliable than decisions made during a drawdown.
- **Make the thesis falsifiable.** “This is a good company” is not testable; a measurable economic claim is.
- **Act when a genuine red line is triggered.** Repeatedly postponing reassessment can turn a correctable error into a permanent loss.
- **A falling price is not the same as a broken thesis.** Separate market volatility from business deterioration.
- **Admit analytical mistakes.** Do not defend an invalid thesis merely to protect ego or avoid realizing a loss.
