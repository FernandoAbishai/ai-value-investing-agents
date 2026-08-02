# Management Deep Dive: Buying a Stock Means Buying People

Perform a deep management analysis of $ARGUMENTS.

**Supported inputs**: `company` or `person company`, for example `Meituan`, `Wang Xing Meituan`, or `Jensen Huang NVIDIA`.

## Purpose

Most management analysis stops at biographies, ownership, and compensation. This workflow goes deeper by examining whether words match actions, how capital was allocated, how leaders behaved under pressure, and whether employees, customers, suppliers, and industry participants corroborate the public narrative.

Use this workflow when management is central to the thesis or when the standard `/investment-research` management score is uncertain or below four stars.

## Process

### Step 1: Identify the Real Decision-Makers

Use current sources to identify:

| Role | Name | Tenure | Background | Ownership / options |
|---|---|---|---|---|
| CEO / chair | | | | |
| CFO | | | | |
| Founder, if no longer in office | | | | |
| Controlling person, if different from CEO | | | | |
| Other critical executives | | | | |

Distinguish formal titles from actual influence. A founder may remain the strategic center after stepping down.

Launch four research Agents in parallel:

1. Public statements, forecasts, shareholder letters, calls, interviews, and social media
2. Capital-allocation decisions: acquisitions, buybacks, dividends, and new ventures
3. Governance, ownership, related-party transactions, and compensation
4. External validation from employees, customers, merchants, suppliers, and industry reputation

### Step 2: CEO Circle of Competence

#### 2.1 Strategic Judgment

Review at least five years of public statements.

| Date | Management judgment or forecast | Actual outcome | Accuracy |
|---|---|---|:---:|

Ask:

- Did the CEO make correct judgments before the market recognized them?
- Did the CEO remain disciplined during periods of excessive optimism?
- Is the industry view independent or merely consensus-following?

#### 2.2 Execution

| Dimension | Assessment | Evidence |
|---|---|---|
| Strategy to execution | Were stated plans delivered? | |
| Organizational capability | Can the company attract and retain strong people? | |
| Crisis response | How did management act under stress? | |
| Learning speed | How quickly were mistakes corrected? | |

### Step 3: Integrity — Highest Priority

#### 3.1 Promise Versus Delivery

Extract specific commitments from the latest three years of earnings calls, letters, and interviews.

| # | Date | Commitment | Venue | Outcome | Assessment |
|---|---|---|---|---|---|

Calculate a commitment fulfillment rate:

| Fulfillment rate | Interpretation |
|---:|---|
| Above 80% | Excellent reliability |
| 60–80% | Generally reliable, with execution variance |
| 40–60% | Concerning overpromising |
| Below 40% | Serious credibility problem |

#### 3.2 Behavior During Difficult Periods

Identify major crises such as sharp drawdowns, earnings misses, regulatory shocks, or competitive attacks.

| Crisis | Date | Management response | Retrospective assessment |
|---|---|---|---|

Determine whether management communicated directly, accepted internal responsibility, and chose difficult long-term actions over short-term market appeasement.

#### 3.3 Treatment of Stakeholders

| Stakeholder | Observed attitude | Evidence | Assessment |
|---|---|---|---|
| Shareholders | | | |
| Employees | | | |
| Customers / users | | | |
| Merchants / suppliers | | | |
| Regulators / society | | | |

### Step 4: Capital Allocation

Review every material decision during the past five years.

#### Acquisitions

| Date | Target | Amount | Strategic logic | Subsequent return | Score 1–5 |
|---|---|---:|---|---|---:|

#### Buybacks

Use `tools/financial_rigor.py verify-valuation` to compare valuation at the time of repurchase with current and historical valuation.

| Date | Amount | Average price | Valuation at purchase | Retrospective result | Score 1–5 |
|---|---:|---:|---:|---|---:|

#### Dividends

| Year | Dividend amount | Payout ratio | FCF | Sustainable? |
|---|---:|---:|---:|:---:|

#### New Ventures

| Date | Area | Cumulative investment | Current status | Return assessment | Score 1–5 |
|---|---|---:|---|---|---:|

Score:

| Dimension | Score 1–5 | Explanation |
|---|---:|---|
| Acquisition discipline | | |
| Buyback timing | | |
| Dividend policy | | |
| New-business investment | | |
| Cash management | | |
| **Overall** | | |

### Step 5: Governance

#### 5.1 Ownership and Control

| Item | Details | Risk assessment |
|---|---|---|
| Dual-class or super-voting shares | | |
| Founder / controller ownership | | |
| VIE structure | | |
| Independent-board quality | | |
| Recent insider buying or selling | | |

#### 5.2 Compensation

| Executive | Total annual compensation | Share of company net income | Peer comparison | Reasonable? |
|---|---:|---:|---|:---:|

Assess whether incentives reward long-term per-share value or short-term metrics.

#### 5.3 Related-Party Transactions

| Related party | Transaction | Amount | Arm's length? | Risk |
|---|---|---:|:---:|---|

### Step 6: External Validation

Use only publicly accessible material and label its limitations.

#### Employee View

| Dimension | Trend | Key feedback |
|---|---|---|
| Culture | | |
| Management approval | | |
| Work intensity | | |
| Compensation satisfaction | | |
| Career outlook | | |

#### Customer and Merchant View

| Dimension | Rating / trend | Key feedback |
|---|---|---|
| Product satisfaction | | |
| Customer service | | |
| Merchant / supplier relationships | | |

#### Industry Reputation

Summarize recurring views from credible industry sources and distinguish representative evidence from isolated anecdotes.

### Step 7: CEO Departure Scenario

| Question | Answer |
|---|---|
| Could the company operate normally if the CEO left tomorrow? | |
| Is there management depth and a credible successor? | |
| Does the moat depend on one person or on systems and culture? | |
| Has the company handled leadership transitions well before? | |

### Step 8: Produce the Management Report

Use this structure:

1. Key people overview
2. Integrity assessment
   - Promise fulfillment
   - Behavior under pressure
   - Stakeholder treatment
3. Capability assessment
   - Strategic judgment
   - Execution
   - Capital allocation
4. Governance
5. External validation
6. Succession risk
7. Overall score and investment conclusion

Weighted score:

| Dimension | Weight | Score 1–5 | Weighted result |
|---|---:|---:|---:|
| Integrity | 35% | | |
| Strategy and execution | 25% | | |
| Capital allocation | 25% | | |
| Governance | 15% | | |
| **Overall** | 100% | | |

Apply the “buying people” test:

1. Is this person honest and aligned with shareholders?
2. Is this person capable in strategy, execution, and capital allocation?
3. Would you willingly entrust capital to this person for ten years?

Integrity is a veto. Strong ability cannot compensate for untrustworthy behavior.

### Step 9: Save the Report

Write the report to `reports/{company}-management-{YYYYMMDD}.md`.

## Principles

- Judge actions rather than rhetoric.
- Evaluate leaders most carefully during difficult periods.
- Treat capital allocation as the final management exam.
- Do not become emotionally attached to admired executives.
- Clearly separate verified facts, reasonable inference, and anecdotal evidence.
