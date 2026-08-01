---
name: news-pulse
description: Rapidly explain unusual stock-price moves using four parallel Agents covering company events, regulation, peers, and market sentiment.
---

# Company News Pulse: Rapid Price-Move Attribution Team

Investigate recent news and explain the price movement described in $ARGUMENTS. **This is not deep investment research. It is rapid intelligence response.** The goal is to answer within roughly 10–15 minutes:

- What recently happened to the company?
- What most likely caused the price move?
- Does the investment thesis require review?

## Appropriate Use

- A held or watched stock rises or falls sharply, commonly ±5% in one day or ±10% in one week
- The stock moves after earnings and the market reaction is unclear
- A headline may be noise or a genuine signal

Do not use this workflow for complete research (`/investment-team`), filing analysis (`/earnings-review`), or long-term thesis monitoring (`/thesis-tracker`).

## Workflow

### Step 1: Confirm Parameters

If $ARGUMENTS does not provide them, ask for:

| Parameter | Meaning | Default |
|---|---|---|
| Company | Name or ticker | Required |
| Time window | Number of days to investigate | 14 days; 7 during earnings season when appropriate |
| Price move | Direction, percentage, and period | Optional but useful for attribution |
| Focus | Company / regulation / industry / sentiment | Equal weighting |

When the user gives only a company name, ask for the desired time window and whether a specific price move must be explained. Do not silently invent these details.

### Step 2: Information-Availability Rating

| Rating | Characteristics | Investigation strategy |
|---|---|---|
| A — Information-rich | Large cap, broad media coverage, earnings season | Prioritize noise reduction and attribution; filter duplicated secondary reporting |
| B — Moderate information | Mid- or small-cap with average coverage | Standard mode; give one or two independent sources for each important event |
| C — Information-scarce | Obscure, newly listed, or lightly covered stock | Discovery mode; finding no explanatory event is itself useful evidence of technical or flow-driven movement |

Pass the rating to every Agent.

### Step 3: Create the Team

Use `TeamCreate`:

- `team_name`: `{company}-newspulse`, lowercase English, such as `pdd-newspulse`
- `agent_type`: `team-lead`

### Step 4: Create Four Investigation Tasks

#### Task 1: Company Events — `company-event-scout`

- `subject`: `Investigate {company} company-specific events during the past {N} days`
- Include:
  1. Exchange, SEC, HKEX, CNInfo, or other official disclosures
  2. Results, guidance, earnings-call details, and profit warnings
  3. Executive changes, insider transactions, buybacks, dividends, and equity compensation
  4. Product launches, M&A, divestitures, major customers, and major orders
  5. Financing, convertible debt, ADR changes, relisting, or delisting proposals
  6. Litigation and disclosed compliance events
  7. For each event: date, source, one-sentence summary, and high / medium / low relevance to the move
  8. Reverse-chronological timeline

#### Task 2: Regulation and Policy — `regulatory-watcher`

- `subject`: `Investigate regulatory and policy changes affecting {industry/company} during the past {N} days`
- Include:
  1. Industry rules, penalties, remediation, or license changes
  2. Cross-border policy, tariffs, export controls, data security, and China–U.S. issues when relevant
  3. Tax changes
  4. Antitrust and competition-law actions
  5. Sector-specific policy
  6. Currency, interest-rate, and capital-control changes
  7. Date, source, and direct / indirect / irrelevant impact
  8. Whether a policy shock has just occurred

#### Task 3: Industry and Peers — `industry-peer-analyst`

- `subject`: `Investigate {company} industry and peer developments during the past {N} days`
- Include:
  1. Three to five direct competitors and their recent results, products, pricing, and personnel changes
  2. Upstream suppliers and downstream customers: prices, capacity, and orders
  3. Industry demand, shipments, tenders, or other activity indicators
  4. Substitute technologies and business models
  5. Sector-index and peer-stock performance
  6. Decide whether the move is company-specific or industry beta
  7. Date and source for each event

#### Task 4: Sentiment and Institutional Views — `sentiment-tracker`

- `subject`: `Investigate {company} sentiment and institutional-view changes during the past {N} days`
- Include:
  1. Sell-side rating and target-price changes
  2. Institutional holdings, 13F data, southbound or northbound flows when relevant
  3. Short interest and short reports
  4. Relevant investor commentary. When appropriate, use:

```bash
python3 tools/xueqiu_scraper.py \
  --user-id 1247347556 \
  --keywords {company},{ticker} \
  --output /tmp/dyp-{company}.md
```

Use the scraper only when the company is relevant to the tracked investor.

  5. Unverified rumors and social discussion from X, Reddit, Xueqiu, or similar sources
  6. Technical signals, block trades, margin financing, and unusual flow data
  7. Decide whether fundamentals or sentiment / liquidity better explains the move

### Step 5: Launch Four Agents in Parallel

Call the Task tool four times **in the same message**.

Each Agent uses:

- `subagent_type`: `general-purpose`
- `run_in_background`: `true`
- `team_name`: `{company}-newspulse`
- `name`: the role name

Prompt template:

```text
You are the {role} on the {company} News Pulse team. Investigate events in the {dimension} dimension during the past {N} days.

Time window: {start_date} to {today}
Price-move context: {user context, or "No specific move; routine check"}
Information-availability rating: {A/B/C}

Complete task #{task_number}: {task_subject}

Requirements:
{task_description}

Investigation method:
- Use WebSearch for time-sensitive queries with dates and terms such as latest or recent.
- Use WebFetch to read primary filings, earnings releases, and regulatory documents.
- Independently verify important events. Rumors require at least two independent sources.
- Do not rely on headlines alone. Mark misleading headlines explicitly.
- Distinguish facts from inference.

Output:
1. Three to five core findings
2. Reverse-chronological timeline:
   | Date | Event | Source | Relevance to price move | Persistence |
3. Attribution conclusion for this dimension with confidence
4. Data gaps and unresolved questions

When complete:
1. Mark the task completed with TaskUpdate.
2. Send the full report to team-lead using SendMessage with type `message` and recipient `team-lead`.
```

### Step 6: Track Progress

- Show three core findings as each Agent reports.
- Wait for all four reports.
- Send `shutdown_request` to all four Agents after receipt.

### Step 7: Team-Lead Attribution Report

Produce an attribution report focused on judgment rather than exhaustive company research.

#### 1. One-Sentence Attribution

In 30–60 words, state the primary cause, secondary cause, and whether the move is a value event, sentiment move, mixed event, or unexplained.

#### 2. Combined Timeline

| Date | Dimension | Event | Source | Attribution weight |
|---|---|---|---|---|
| | Company / policy / industry / sentiment | | | High / medium / low |

A high-weight event can independently explain the move; medium contributes; low is background noise.

#### 3. Attribution Table

| Candidate explanation | Evidence | Counter-evidence | Confidence | Expected persistence |
|---|---|---|---|---|

#### 4. Nature of the Move

Select one:

- [ ] **Value event**: fundamentals, moat, management, or long-term outcome changed; review the thesis
- [ ] **Sentiment / technical move**: no material fundamental change; liquidity, sentiment, or beta dominates
- [ ] **True cause unknown**: no event matches the size of the move; the market may be anticipating information or the investigation may have missed a source
- [ ] **Mixed**: a real event amplified by sentiment or flows

#### 5. Dimension Summaries

Give three to five findings from each dimension and its attribution contribution.

#### 6. Action Checklist

| Action | Recommended? | Reason |
|---|---|---|
| Review thesis with `/thesis-tracker` | | |
| Run `/earnings-review` | | |
| Run `/management-deep-dive` | | |
| Consider adding, reducing, or holding | | Guidance only; the user makes the decision |
| Observe only | | |

#### 7. Next 7–30 Days

List pending disclosures, metrics, and signals to monitor.

#### 8. Information Gaps

State unresolved questions and missing evidence. Prefer an explicit unknown to a fabricated causal narrative.

### Step 8: Save the Report

Write to `reports/{company}/{company}-news-{YYYYMMDD}.md`. Create the company directory when necessary.

### Step 9: Delete the Team

Use `TeamDelete`.

## Core Principles

1. **Speed over completeness**: deliver attribution within roughly 10–15 minutes.
2. **Attribution over listing**: identify which event is large enough to explain the move.
3. **Be honest about unknown causes**: unexplained movement is a valuable and potentially important conclusion.
4. **Do not defend an existing position**: follow the evidence.
5. **Separate catalysts from coincidences**.
6. **Respect information availability**: a C-rated company may have no discoverable news.
7. **Cite sources and distinguish facts from opinions**.
8. **Do not make the user’s trading decision**: provide evidence, attribution, and a follow-up checklist.
