---
name: industry-funnel
description: "AI Value Investing Agents skill: Industry Funnel: From the Full Market to Three Value-Investing Finalists. Source: skills/industry-funnel.md."
---

## Codex adapter note

This skill is generated from `skills/industry-funnel.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Industry Funnel: From the Full Market to Three Value-Investing Finalists

Run a funnel-based value-investing screen for the industry or theme in $ARGUMENTS, progressing from a broad global universe to no more than three finalists.

## When to Use This Workflow

Use this workflow when the user names an industry or investment direction such as AI infrastructure, innovative medicines, or robotics and wants to:
1. Avoid missing important public and private participants.
2. Apply consistent filters to remove story-driven or low-quality companies.
3. Focus deep research on the few strongest candidates.
4. Preserve explicit inclusion and elimination reasons at every stage.

Relationship to `industry-research`:
- `industry-research` maps the full value chain and segment economics.
- `industry-funnel` screens companies from a broad universe to a concentrated shortlist.

They are complementary: map the industry first when the structure is unclear, then run the funnel to select companies.

---

## Funnel Overview

```text
Layer 1: Full-market scan      30–60 companies
         Activity + momentum + top market-cap union
                 ↓ five hard value-investing filters
Layer 2: Coarse screen         ≤10 companies
         All five pass, or four pass with one near-pass
                 ↓ structured review
Layer 3: Detailed analysis     ≤10 companies
         300–500 words per company
                 ↓ portfolio-aware selection
Layer 4: Four-framework review 3 finalists
         800–1,200 words per company
                 ↓
Output: investment view, price conditions, monitoring signals, and sizing guidance
```

Every rejected company must retain a documented reason. The funnel must not operate as a black box.

---

## Step 1: Build the Full-Market Universe

### 1.1 Three Inclusion Sets

**Set A — Trading activity**
- Select the industry leaders by average daily trading value over the latest 30 trading days.
- Build separate top-30 lists for mainland China, Hong Kong, and the United States when enough candidates exist.

**Set B — Price movement**
- Top 20 by 30-day return.
- Top 20 by 90-day return.
- Use the union of both lists.

**Set C — Market-cap anchor**
- Top 30 industry companies by current market capitalization regardless of recent price movement.

Final universe = A ∪ B ∪ C, normally 30–60 companies.

Momentum is an inclusion mechanism, not an investment recommendation.

### 1.2 Required Markets

| Market | Suggested Sources |
|---|---|
| Mainland China | Exchange and established financial-data industry classifications |
| Hong Kong | HKEX classifications and established market-data platforms |
| United States | Exchange listings, industry ETFs, filings, and established market data |
| International | Relevant Japanese, South Korean, Taiwanese, European, Australian, and other companies |
| Private companies | Separate potential-IPO section with latest known valuation and possible timing |

For Taiwanese companies, use `python3 tools/twstock_data.py` where applicable and follow `skills/financial-data.md`.

### 1.3 Universe Table

| Company | Ticker | Market | Market Cap | One-Sentence Business | Industry Revenue Exposure | Inclusion Set A/B/C |
|---|---|---|---:|---|---:|---|

Required checks:
- Label companies with less than 30% relevant revenue as **non-pure-play**.
- Do not omit Chinese or Asian companies because English-language coverage is weaker.
- Do not omit small companies merely because large companies are easier to research.
- Record the market-data cutoff date and currency.

---

## Step 2: Apply Five Hard Value-Investing Filters

Apply the following filters to every company in the broad universe.

### 2.1 Filters

| # | Metric | Pass Standard | Allowed Adjustment | Primary Evidence |
|---|---|---|---|---|
| 1 | Valuation | Reasonable versus history and peers | High growth may qualify when PEG < 1.5 and assumptions are defensible | Filings and validated market data |
| 2 | ROE | Above 15% or a clear three-year improvement trend | Adjust for capital-intensive industry economics | Financial statements |
| 3 | Operating cash flow | Positive and above 70% of net income | No automatic waiver | Cash-flow statement |
| 4 | Debt ratio | Below 60% | Utilities and power may allow up to 70% with stable cash flows | Balance sheet |
| 5 | Moat quick score | At least ★★★ | No automatic waiver | Evidence-based qualitative analysis |

Five moat categories:
- Brand and pricing power.
- Switching costs and customer retention.
- Network effects.
- Scale advantages.
- Technology, license, regulation, or resource barriers.

Use sector-appropriate definitions for financial companies, REITs, and other businesses where standard leverage or cash-flow ratios are not comparable. Explain every adjustment.

### 2.2 Screen Table

| Company | P/E or Relevant Valuation | ROE | OCF / Net Income | Debt Ratio | Moat | Overall | Keep/Reject | Reason |
|---|---:|---:|---:|---:|:---:|---|---|---|

Retention rules:
- Five passes: retain.
- Four passes plus one defensible near-pass: retain with a yellow flag.
- Fewer than four passes: reject and record the reason.

Target: retain no more than ten companies. If more than twelve survive, raise the moat requirement to ★★★★ and compare valuation quality more strictly.

Do not manipulate thresholds merely to produce a desired number of finalists.

---

## Step 3: Detailed Analysis of the Survivors

Write 300–500 words per retained company using this structure:

```markdown
## {Company} ({Ticker})

**Business model in one sentence**
What it sells, to whom, and how it earns money.

**Financial quality**
- Revenue and profit growth
- Gross margin
- ROE
- Cash conversion
- Most important financial change in the last one or two years

**Moat depth**
- Primary moat types with evidence
- Whether those advantages are likely to remain in five years

**Top three risks**
1.
2.
3.

**Valuation snapshot**
- Current P/E, P/S, and EV/EBITDA when meaningful
- Position in the historical range
- Peer comparison
- Conclusion: Expensive / Reasonable / Attractive

**Advance to the final three?** Yes / No, with the decisive reason.
```

### Finalist Selection Standard

Do not simply choose the three highest numeric scores. Select a complementary set when suitable:
- At least one high-certainty, lower-upside core candidate.
- At least one medium-certainty growth candidate.
- Optionally one high-risk, high-upside candidate.

When fewer than three companies meet the standard, return two finalists plus one watchlist candidate rather than lowering the threshold.

---

## Step 4: Four-Framework Review of the Finalists

Perform an 800–1,200-word review for each finalist.

### 4.1 Business Essence — Duan Yongping-Inspired

- Define the business in plain language.
- Is it a good business, and why?
- What does staying within its circle of competence and proper conduct mean for management?
- Where does durability come from?

### 4.2 Moat and Margin of Safety — Buffett-Inspired

| Moat | Strength | Specific Evidence |
|---|:---:|---|
| Brand and pricing power | | |
| Switching costs | | |
| Network effects | | |
| Scale advantages | | |
| Technology, licensing, or resource barriers | | |

Answer:
- Is the moat likely to survive ten years?
- What valuation or business condition creates a margin of safety?

### 4.3 Failure Modes — Munger-Inspired

- Identify the three most plausible failure paths.
- Estimate a simplified severe-downside value.
- Present the strongest informed bear case.
- Review integrity, compliance, governance, and incentive risks.

### 4.4 Long-Term Trend — Li Lu-Inspired

- Is the market a civilization-level transition or a temporary cycle?
- What historical transformation is the closest analogy?
- What could the company's role be in ten to twenty years?
- Is the market winner-take-most, oligopolistic, or structurally fragmented?

### 4.5 Final Recommendation Format

```text
Recommendation: ★★★★☆
Portfolio role: Core / Satellite / Option / Watchlist
Purchase condition: Current price / N% pullback / Specific valuation threshold
Suggested share of the theme allocation: X%
Critical monitoring signal: the observable event that would invalidate the thesis
Information grade: A / B / C
```

Generated framework commentary must be labeled as analysis inspired by public investment principles, not as an authentic quotation or endorsement.

---

## Step 5: Consolidated Output

### 5.1 Finalist Portfolio Table

| Company | Role | Rating | Suggested Theme Weight | Core Logic | Principal Risk |
|---|---|:---:|---:|---|---|
| A | Core | ★★★★★ | 50–60% | | |
| B | Satellite | ★★★★☆ | 25–35% | | |
| C | Option | ★★★☆☆ | 5–15% | | |

Do not force full investment when valuations are unattractive. Unallocated cash is acceptable.

### 5.2 ETF Alternatives

List one to three relevant ETFs across appropriate markets for users who prefer diversification. Verify current holdings, expense ratios, liquidity, and index methodology.

### 5.3 Industry Position

Assess:
- Industry P/E and P/B historical percentile when meaningful.
- Fund flows, ETF subscriptions or redemptions, and coverage intensity.
- Industry stage: Early / Expansion / Mature / Declining.

### 5.4 Information Sufficiency

| Dimension | Grade | Explanation |
|---|:---:|---|
| Company financial data | A/B/C | |
| Valuation freshness | A/B/C | |
| Industry-structure evidence | A/B/C | |
| Management evidence | A/B/C | |

- **A**: strong and current evidence.
- **B**: some gaps that do not overturn the central conclusion.
- **C**: material gaps; use the conclusion cautiously.

### 5.5 Data Requiring Updates

List:
- Estimated figures.
- Unverified figures.
- Missing primary documents.
- The next earnings report or event that could materially change the screen.

### 5.6 Source Register

List sources by category:
- Company filings.
- Regulatory documents.
- Industry reports.
- Market data.
- Reputable news and interviews.

Every material fact must be traceable to a source.

---

## AI Bias Controls

| Bias | Failure Mode | Control |
|---|---|---|
| Large-cap preference | More coverage and longer analysis are mistaken for quality | Rank by hard metrics, moat evidence, and valuation—not report length |
| English-language preference | U.S. companies dominate the shortlist | Search English and relevant Asian-language sources |
| Story preference | Momentum and media attention are mistaken for business exposure | Measure actual revenue and profit contribution |
| Present-state preference | Current winners crowd out improving businesses | Allow documented trend improvement as an explicit exception |
| Public-market preference | The best private participant is ignored | Maintain a separate future-IPO candidate list |

---

## Output Requirements

1. Save the report to `reports/{industry-name}-funnel-{YYYYMMDD}.md`.
2. Write in English unless the user explicitly requests another language.
3. Use direct, decision-oriented language.
4. Source every material figure; label estimates as estimates.
5. Follow the order: evidence → reasoning → conclusion.
6. Include the strongest counterargument for every core conclusion.
7. Preserve an elimination log at every funnel stage.

## Publication Audit Gate

After writing the report:

```bash
# Step 1 — Extract a 15% random audit sample
python3 tools/report_audit.py extract \
  --report <report-path>

# Step 2 — Recheck every sampled item against reliable sources
# Follow skills/financial-data.md.

# Step 3 — Produce the release or rejection verdict
python3 tools/report_audit.py verdict \
  --results '<completed-JSON>' \
  --report <report-file-name>
```

- **Release**: every sampled item passes.
- **Reject**: one or more items fail; correct the report and rerun the audit.

## Next Actions

After selecting the finalists, use:
- `/investment-team` for full parallel company research.
- `/investment-checklist` for a disciplined pre-purchase checklist.
- `/management-deep-dive` for management and capital-allocation research.

`industry-funnel` is the selection entry point; the other workflows provide deeper validation.
