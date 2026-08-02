# Portfolio Review: From Researching Companies to Managing a Portfolio

Review and optimize the investment portfolio described in $ARGUMENTS.

**Supported input formats**:
- Allocation list, for example: `Tencent 30%, Meituan 20%, Kweichow Moutai 20%, NVIDIA 15%, Cash 15%`
- Position details, for example: `Tencent 500 shares @ HKD 480, Meituan 1,000 shares @ HKD 130, ...`
- `my portfolio` when a saved portfolio file already exists at `reports/portfolio-latest.md`

> Diversification can protect against ignorance, but concentration requires genuine understanding.
>
> Exceptional investment opportunities are rare, so capital allocation must be deliberate.

## Purpose

Company research is only half of investing. The other half is making portfolio-level decisions:
- How much should be allocated to each position?
- Should a purchase use new cash or replace another holding?
- Are multiple holdings exposed to the same underlying risk?
- What does the best available portfolio look like after considering opportunity cost?

Do not evaluate a stock in isolation. Always ask whether it is the best available use of the next unit of capital.

## Workflow

### Step 1: Parse the Portfolio

Normalize the current holdings into this format:

| Asset | Ticker | Quantity | Cost Basis | Current Price | Market Value | Weight | Gain/Loss |
|---|---|---:|---:|---:|---:|---:|---:|

If only allocation percentages are provided, analyze the portfolio by percentage.

Check whether `reports/portfolio-latest.md` exists. If it does, read it and use it as the current portfolio record unless the user explicitly provides newer data.

### Step 2: Collect Current Information

Use Task or the closest available parallel-agent capability to collect the following for every holding:
1. Current price and valuation metrics, including P/E, P/B, and dividend yield.
2. The most important changes in the latest reporting period.
3. Recent material events.
4. Consensus estimates when available, including forward P/E and target-price ranges.

Validate valuation inputs with `tools/financial_rigor.py verify-valuation`.

Assign each holding an information-availability grade:
- **A**: strong primary-source coverage and current data.
- **B**: sufficient data with limited gaps.
- **C**: material gaps; conclusions must be labeled low confidence.

### Step 3: Review Each Position

Perform a rapid health check for every holding:

| Asset | Current P/E | Has the Original Thesis Changed? | Thesis Health | Position Recommendation |
|---|---:|:---:|:---:|---|
| Tencent | 18x | No | 8/10 | Appropriate |
| Meituan | 25x | Competition intensified | 6/10 | Oversized; consider reducing |

For each holding, answer:
- [ ] If the portfolio did not own it today, would it still be purchased at the current price?
- [ ] Would holding it for five years without the ability to trade be comfortable?
- [ ] Is the original investment thesis still intact?

A position should not be retained merely because it is already owned.

### Step 4: Portfolio-Level Analysis

#### 4.1 Concentration

| Metric | Current Value | Reference Range | Assessment |
|---|---:|---:|---|
| Largest holding | | Below 40% unless exceptionally well understood | |
| Top-three holdings | | 50–80% for a concentrated portfolio | |
| Number of holdings | | 5–15 | |
| Cash allocation | | Commonly 10–30%, depending on opportunity set and liquidity needs | |

A highly concentrated portfolio requires correspondingly deep research. Do not use concentration as a substitute for conviction that has not been earned.

#### 4.2 Correlation and Shared Risk

Identify hidden relationships among holdings:

| Holding A | Holding B | Shared Exposure | Risk |
|---|---|---|---|
| Tencent | Kuaishou | Chinese internet | Regulatory-risk correlation |
| NVIDIA | TSMC | AI supply chain | Shared AI-capex cycle |
| Meituan | PDD | Chinese consumption | Macroeconomic-demand correlation |

Check:
- [ ] Is more than 50% of the portfolio exposed to one industry or theme?
- [ ] Is more than 50% exposed to one country, legal regime, or currency?
- [ ] What happens under a material deterioration in U.S.–China relations?
- [ ] What happens in a global recession?

#### 4.3 Opportunity Cost

Rank every holding by risk-adjusted expected annual return:

| Rank | Asset | Current Weight | Expected Annual Return | Confidence | Expected Return × Confidence |
|:---:|---|---:|---:|:---:|---:|
| 1 | | | | | |
| 2 | | | | | |

Use `tools/financial_rigor.py three-scenario` for scenario calculations.

Expected-return methods:
- **Primary approximation**: expected annual return ≈ free-cash-flow yield + sustainable growth.
- **Value validation**: margin-of-safety normalization + earnings growth + dividend yield.
- **Growth validation**: earnings growth adjusted for plausible valuation-multiple changes.

Compare low-ranked positions with the current risk-free alternative. Use a current, sourced rate rather than a hard-coded assumption. If a holding does not justify its incremental risk over cash or short-duration government securities, consider replacing it.

#### 4.4 Stress Tests

| Scenario | Assumption | Estimated Portfolio Effect | Estimated Maximum Drawdown |
|---|---|---|---|
| Global recession | Corporate earnings fall 20–30% | | |
| U.S.–China conflict intensifies | China-related equities reprice sharply | | |
| Interest-rate shock | Long-term yields rise materially | | |
| Technology bubble unwinds | Technology valuation multiples compress 40% | | |

For each scenario:
- Identify the holdings most exposed.
- Estimate the direction and plausible range of impact.
- Assess whether the portfolio can tolerate the drawdown.
- State whether hedging, position reduction, or no action is appropriate.

### Step 5: Optimization Recommendations

#### 5.1 Rebalancing Plan

| Action | Asset | Current Weight | Suggested Weight | Rationale |
|---|---|---:|---:|---|
| Add | | | | |
| Reduce | | | | |
| Exit | | | | |
| Initiate | | | | |
| Hold | | | | |

Recommendations must account for taxes, liquidity, transaction costs, and the user's stated constraints when those details are available.

#### 5.2 Replacement Candidates

When the portfolio contains positions that do not justify their opportunity cost, or when excess cash needs deployment, recommend using `/industry-research` or `/investment-checklist` to identify candidates. Do not introduce unsupported stock recommendations inside this workflow.

#### 5.3 Cash Management

| Current Cash Weight | Suggested Cash Weight | Rationale |
|:---:|:---:|---|

Cash is a legitimate position when attractive opportunities are unavailable. Do not force capital into a weak idea merely to remain fully invested.

### Step 6: Produce the Portfolio Report

#### Report Structure

```text
1. Portfolio overview: holdings table and allocation description
2. Position-by-position health check
3. Portfolio analysis
   - Concentration
   - Shared exposures and correlated risks
   - Opportunity-cost ranking
   - Stress-test estimates
4. Rebalancing recommendations with specific actions and reasons
5. Next review date and monitoring priorities
```

#### Required Conclusions

Answer clearly:
1. **Overall portfolio health**: Excellent / Good / Needs Adjustment / Serious Problems.
2. **The single most important action**: add, reduce, exit, or make no change.
3. **The largest current portfolio risk**.

### Step 7: Save the Portfolio Record

Write the updated portfolio to `reports/portfolio-latest.md`, including:
- Current holdings table.
- Review date and conclusion.
- An appended rebalancing log.
- The next review trigger or target date.

## Core Principles

- **Every unit of capital has an opportunity cost.** Owning a mediocre asset can prevent ownership of a superior one.
- **Concentration is not automatically safe.** It is justified only by deep understanding, durable economics, and an adequate margin of safety.
- **Cash is a position.** Holding cash is preferable to forcing a weak investment.
- **Portfolio construction can dominate stock selection.** A strong company at an inappropriate weight can still damage the portfolio.
- **Review periodically without overtrading.** A quarterly review is usually sufficient unless a thesis-breaking event occurs.
