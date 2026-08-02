---
name: investment-checklist
description: "AI Value Investing Agents skill: Buffett Value-Investing Pre-Purchase Checklist. Source: skills/investment-checklist.md."
---

## Codex adapter note

This skill is generated from `skills/investment-checklist.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Buffett Value-Investing Pre-Purchase Checklist

Run the Buffett-style pre-purchase checklist on $ARGUMENTS.

**Supported input**: one or more companies separated by commas or spaces, for example `Tencent, Moutai, NVIDIA` or `NVDA AAPL MSFT`.

## Workflow

### Step 1: Parse the Input

Identify every company or ticker in $ARGUMENTS. For each one, determine:

- Full company name, ticker, and exchange
- Whether it is publicly traded
- For a private company, mark it as **private**, explain any indirect exposure, and skip the full checklist

### Step 1.5: AI Research-Bias Warning

Assign each company an information-richness rating and show it in the report:

| Rating | Standard | Effect on the checklist |
|---|---|---|
| A | Long public history and abundant data | Run normally, but guard against the consensus trap: clear metrics do not automatically mean genuine certainty |
| B | Limited data requiring estimates | Label confidence for every estimate and weight business-quality judgments by data reliability |
| C | Extremely scarce information | Do not force every box to be filled. Mark unknowns honestly and focus on verifiable core questions |

**Core principle**: this checklist exists to eliminate bad choices. For a C-rated company, insufficient data is neither a pass nor a fail. Mark it as a gray area requiring first-hand information.

Do not confuse “little information” with “an incomprehensible business.”

### Step 2: Parallel Data Collection

Launch one independent research Agent for each company, with all companies researched in parallel. Each Agent should collect:

1. Profitability: five- to ten-year ROE trend, gross margin, net margin, and free cash flow
2. Valuation: current price, market cap, trailing and forward P/E, P/B, and dividend yield
3. Growth: three-year revenue and profit growth
4. Financial health: debt, capital intensity, cash reserves, and net cash or net debt
5. Competitive position: market share, major competitors, and share trends
6. Moat evidence: brand, switching costs, network effects, scale, and technology
7. Management record: background, ownership, important decisions, and capital allocation
8. Recent developments: material results, M&A, regulation, and management changes during the past six months

### Step 3: Apply the Six Gates

Apply all six gates to every publicly traded company.

---

#### Gate 1: Can I Understand the Business? — Circle of Competence

Answer:

- [ ] Can the company’s money-making mechanism be explained in one sentence?
- [ ] What business is it likely to be in ten years from now?
- [ ] Which variables determine success or failure?
- [ ] Is the industry understanding based on real research or hearsay?

**Score from one to five stars**:

- ★★★★★: exceptionally simple and clear business with high ten-year certainty
- ★★★★☆: clear model with some technical complexity
- ★★★☆☆: understandable, but the industry changes quickly
- ★★☆☆☆: complex operations or an industry undergoing major disruption
- ★☆☆☆☆: outside the circle of competence

**Hard rejection**: if the revenue model cannot be explained, mark it “outside the circle of competence” and stop the analysis.

---

#### Gate 2: Is It a Good Business? — Economic Characteristics

Use data. **Verify material metrics precisely with the tool**:

```bash
python3 tools/financial_rigor.py verify-valuation \
  --price {price} --eps {eps} --bvps {book_value_per_share} \
  --fcf-per-share {fcf_per_share} --dividend {dividend_per_share}
```

| Metric | Company value | Reference standard | Judgment |
|---|---|---|---|
| Five-year average ROE | | >15% strong; >20% excellent | |
| Gross margin | | >40% may indicate pricing power | |
| Free cash flow | | Consistently positive and broadly tracks earnings | |
| Capital intensity | | Asset-light is generally preferable | |
| Debt | | Interest-bearing debt / net income <3 years | |

**Scoring**:

- ★★★★★: ROE above 25%, high margins, strong FCF, asset-light, low debt
- ★★★★☆: four criteria pass
- ★★★☆☆: three criteria pass
- ★★☆☆☆: two criteria pass or trends deteriorate
- ★☆☆☆☆: most criteria fail or FCF remains negative

---

#### Gate 3: Is the Moat Deep Enough?

| Moat type | Present? | Evidence | Widening or narrowing? |
|---|---|---|---|
| Brand / pricing power | | | |
| Switching costs | | | |
| Network effects | | | |
| Cost / scale advantage | | | |
| Technology / patents | | | |

Additional test: Could a competitor reproduce the business with 10 billion in capital?

**Scoring**:

- ★★★★★: multiple reinforcing moats that are widening
- ★★★★☆: at least one strong and stable moat
- ★★★☆☆: some moat, but limited depth or unclear direction
- ★★☆☆☆: moat is being eroded
- ★☆☆☆☆: no meaningful moat

---

#### Gate 4: Can Management Be Trusted?

| Test | Assessment |
|---|---|
| Honesty: promises vs delivery | |
| Capital allocation: buybacks, dividends, acquisitions | |
| Shareholder alignment: ownership and compensation | |
| Owner mindset: founder vs hired manager | |
| Governance: related-party transactions, goodwill, audit quality | |
| Can the company function after the CEO leaves? | |

**Scoring**:

- ★★★★★: founder-led, excellent capital allocation, strongly aligned interests
- ★★★★☆: strong management with minor weaknesses
- ★★★☆☆: adequate management with governance concerns
- ★★☆☆☆: integrity or governance problems
- ★☆☆☆☆: serious integrity problem — hard rejection

---

#### Gate 5: Is the Price Cheap Enough? — Margin of Safety

| Metric | Value | Historical percentile | Judgment |
|---|---|---|---|
| Trailing P/E | | | |
| Forward P/E | | | |
| P/B | | | |
| Dividend yield | | | |
| FCF yield | | | |

Run the three-scenario valuation with the tool. **No mental arithmetic**:

```bash
python3 tools/financial_rigor.py three-scenario \
  --price {price} --eps {eps} --shares {shares_in_100_millions} \
  --growth {bull} {base} {bear} --pe {bull_pe} {base_pe} {bear_pe} \
  --currency {currency}
```

Also answer:

- What valuation range does the tool produce?
- How much could be lost at the current price if the thesis is wrong?
- Would the investor confidently add after a 50% decline?

**Scoring**:

- ★★★★★: priced below roughly half of intrinsic value
- ★★★★☆: meaningful margin of safety, approximately 30% discount
- ★★★☆☆: fair value with limited margin of safety
- ★★☆☆☆: expensive
- ★☆☆☆☆: severely overvalued

---

#### Gate 6: Position Sizing and Decision Discipline

Check for emotional errors:

- Is the purchase driven by FOMO?
- Is it based primarily on someone else’s recommendation?
- Could the investor tolerate the stock being untradeable for five years?
- Can the purchase thesis be written clearly in fewer than 200 words?

---

### Step 4: Mirror Test

Write this statement for every company:

> “I am buying ___ at ___ because:
> 1. The essence of the business is ___, and I understand it;
> 2. Its moat is ___ and is widening / narrowing;
> 3. Management is ___ and is / is not trustworthy;
> 4. The current price is approximately ___% of intrinsic value and does / does not provide enough margin of safety;
> 5. If I am wrong, the downside is manageable / unmanageable because ___.”

**If the thesis cannot be expressed in five sentences, do not buy.** Mark the mirror test as passed or failed.

### Step 5: Quick-Rejection Checklist

Any triggered item produces a rejection:

- [ ] Cannot explain how the company makes money
- [ ] Free cash flow has been negative for three consecutive years with no visible improvement
- [ ] Management has a serious integrity issue
- [ ] Competitive advantage is being irreversibly eroded
- [ ] Returns depend on finding a greater fool willing to pay more
- [ ] The investor cannot tolerate a complete loss
- [ ] The main reason to buy is “everyone else is buying” or “the price has been rising”
- [ ] The purchase thesis cannot be written in fewer than 200 words

### Step 6: Comparison Table for Multiple Companies

| Company | Checklist passed? | Circle of competence | Good business | Moat | Management | Margin of safety | Core conclusion |
|---|---|---|---|---|---|---|---|
| | | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | ★☆☆☆☆ | |

### Step 7: Final Verdict and File Output

Give one explicit verdict per company:

- ✅ **Pass** — X of 6 gates passed; eligible for deeper research
- ❌ **Fail** — identify the triggered red line
- ❓ **Gray area** — identify the unresolved issue and first-hand information required
- N/A — private or not directly investable

Write the complete report to `~/buffett-checklist-[company-or-multi-company-comparison].md`.

## Output Requirements

1. Give each company its own section with six-gate scorecard, core data, three to five risks, mirror test, and explicit verdict.
2. Include a final comparison table when multiple companies are analyzed.
3. Use full-star symbols only; no half stars.
4. Label data dates and mark estimates as estimates.
5. End with Buffett’s principle that the first rule of investing is not to lose money.
6. Use direct language. Avoid filler and clearly distinguish authentic quotations from framework-based paraphrases.

## Core Principles

- **It is better to miss an opportunity than to make a bad investment.**
- **Be honest about the circle of competence.**
- **Margin of safety is the lifeline.**
- **Never skip the mirror test.**
