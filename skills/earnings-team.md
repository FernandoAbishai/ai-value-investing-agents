# Earnings Team: Four-Perspective Review and Publishable Article

Perform a team-based earnings analysis of $ARGUMENTS. Four research Agents interpret the filing in parallel, a Team Lead synthesizes the evidence, an editor rewrites the research for publication, and a reader-review Agent challenges clarity and usefulness.

**Supported input**: `company period`, for example `Tencent 2025Q4`, `PDD 2025 annual report`, or `Meituan latest`.

## Design

A strong earnings analysis must solve two problems:

1. Understand what changed in the business and its future.
2. Communicate the conclusion clearly enough for a serious investor to use.

The workflow has three phases:

- **Research**: four parallel perspectives
- **Synthesis**: Team Lead integrates agreements, contradictions, and missing evidence
- **Publication**: editor rewrite, reader review, and final revision

## Phase 1: Parallel Research

### Step 1: Retrieve Primary Sources

Retrieve in parallel:

| Material | Preferred source | Priority |
|---|---|---|
| Original filing | Company IR, SEC EDGAR, HKEXnews, CNInfo | Highest |
| Earnings-call transcript | Company IR, transcript provider, reliable financial platform | Highest |
| Shareholder letter | Annual report | High for annual periods |
| Prior filing and call | Same sources | High for promise tracking |

Rate source availability:

| Rating | Availability | Effect |
|---|---|---|
| A | Complete originals | Execute every section |
| B | Partial originals or reliable compilation | Label secondary material and reduce footnote confidence |
| C | News and data summaries only | Focus on core changes and disclose insufficient primary-source access |

Tell every Agent the rating before research begins.

### Step 2: Show the Team

| Phase | Role | Perspective | Core question |
|---|---|---|---|
| Research | Team Lead | Coordination | What is the integrated judgment? |
| Research | Business-quality analyst | Duan Yongping | Did the business improve or deteriorate? |
| Research | Financial-quality auditor | Buffett | Are the earnings real cash earnings? |
| Research | Competition analyst | Munger | How is the competitive position changing? |
| Research | Risk-signal analyst | Li Lu | Which signals imply permanent-loss risk? |
| Publication | Editor | Investor publishing | Can the research become a clear article? |
| Publication | Reader reviewer | Informed ordinary investor | Is the article understandable, credible, and actionable? |

### Step 3: Launch Four Research Agents in Parallel

Launch all four Agents in the same message.

#### Agent 1: Business Quality

Determine whether the business improved, remained stable, or deteriorated.

Analyze:

- Revenue by segment and geography; acceleration and deceleration
- Whether growth came from volume, price, or mix
- User and customer metrics such as DAU, MAU, ARPU, retention, and engagement
- Gross-margin and market-share signals affecting pricing power and moat
- Changes in differentiation, pricing power, and durable advantage
- Whether the business is becoming more or less capital intensive
- Whether management speaks concretely about products and customers

Mark each subsection as improving, stable, or deteriorating and provide a concise framework-based Duan Yongping perspective. Do not present simulated commentary as an authentic quotation.

#### Agent 2: Financial Quality

Determine whether the company generated genuine cash earnings and whether the margin of safety changed.

Extract and verify:

- Revenue, gross profit, operating income, and net income
- GAAP and non-GAAP differences
- Operating cash flow relative to net income
- Free cash flow and capital expenditure
- Receivables, inventory, capitalized costs, and non-recurring gains
- Net cash or net debt and potential impairment risks
- Current valuation and three-scenario value range

Use exact tools and include their output:

```bash
python3 tools/financial_rigor.py cross-validate \
  --field revenue --values '{"source_1": value, "source_2": value}' --unit {unit}

python3 tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {shares} --reported {reported_market_cap} --currency {currency}

python3 tools/financial_rigor.py verify-valuation \
  --price {price} --eps {eps} --bvps {book_value_per_share}

python3 tools/financial_rigor.py three-scenario \
  --price {price} --eps {eps} --shares {shares_in_100_millions} \
  --growth {bull} {base} {bear} --pe {bull_pe} {base_pe} {bear_pe}
```

Provide green, yellow, or red signals for earnings quality and a concise Buffett-style framework conclusion.

#### Agent 3: Competition

Determine what the filing reveals about competitive direction.

Analyze:

- Company growth relative to industry growth
- Gross margin and selling-expense changes
- R&D intensity and whether it is proactive or defensive
- Comparable results from major competitors
- Management's language about competition
- Technology, regulatory, and demand shifts
- Inversion: what could destroy the company, and did this filing strengthen any failure path?

Output a competition judgment — strengthening, stable, or deteriorating — plus a peer comparison table and a Munger-style inversion conclusion.

#### Agent 4: Risk and Management Signals

Determine which signals could lead to permanent capital loss.

Analyze:

- Management tone: candid, clear, vague, deflecting, or externalizing
- Prior commitments versus delivery
- Related-party transactions, stock dilution, contingencies, and accounting changes
- Segment economics and customer/supplier concentration
- The three to five hardest earnings-call questions and response quality
- Regulatory, compliance, litigation, and irreversible strategic risks

Output a management-credibility score from one to five, commitment fulfillment rate, risk register, and Li Lu-style framework conclusion.

### Step 4: Track Progress

Show a compact progress table and update it as each report arrives. Surface three to five important findings from every completed perspective.

## Phase 2: Team Lead Synthesis

Do not concatenate four reports. Identify:

1. High-confidence agreements across perspectives
2. Contradictions that matter to the thesis
3. Important issues that every Agent overlooked
4. Differences caused by source availability or accounting definitions

Produce the research draft:

```markdown
# {Company} {Period} Earnings Review
**Four-perspective analysis | {date}**

## One-Sentence Conclusion

## Three Most Important Changes

## Four-Perspective Scorecard
| Perspective | Core question | Conclusion | Score | Change from prior period |

## Core Data

## Perspective Summaries

## Management Tone and Promise Tracking

## Framework Decisions
| Perspective | Existing holder | No current position | Reason |

## Final Judgment
1. Beat / met / missed expectations
2. Thesis strengthened / unchanged / weakened / broken
3. Next catalyst
4. Add / hold / reduce evidence
```

## Phase 3: Edit and Reader Review

Launch the editor and reader reviewer in parallel.

### Editor

Rewrite the research into a publication-ready investor article while preserving every material fact and conclusion.

Requirements:

- Informative headline without clickbait
- State the main conclusion within the opening 100 words
- Use an inverted-pyramid structure
- Keep tables concise and paragraphs short
- Explain technical metrics with clear analogies without sacrificing accuracy
- Include periodic section summaries
- Make every section decision-relevant
- End with separate guidance for existing holders and observers
- Target 1,000–3,000 words unless the evidence requires otherwise

### Reader Reviewer

Review from the perspective of an informed ordinary investor.

Score:

- Readability — 30%
- Information value — 30%
- Credibility — 20%
- Action guidance — 20%

Use this format:

```markdown
## Reader Review

### Overall Score: X/10

### Strengths

### Mandatory Corrections
- Problem → proposed correction

### Optional Improvements

### Questions the Article Did Not Answer

### One-Sentence Verdict
```

### Team Lead Final Revision

- Resolve every mandatory correction
- Adopt useful optional improvements
- Answer missing questions when evidence exists
- Re-read the full article for consistency
- Remove unsupported certainty and accidental simulated quotations

## Output Files

```text
reports/{company}/
├── {company}-earnings-{period}.md
├── {company}-earnings-{period}-research-draft.md
├── {company}-earnings-{period}-business.md
├── {company}-earnings-{period}-financial.md
├── {company}-earnings-{period}-competition.md
├── {company}-earnings-{period}-risk.md
└── {company}-earnings-{period}-reader-review.md
```

## Publication Gate

Run the final article through the report audit:

```bash
python3 tools/report_audit.py extract \
  --report reports/{company}/{company}-earnings-{period}.md

python3 tools/report_audit.py verdict \
  --results '<completed_JSON>' \
  --report {report_file_name}
```

Publish only after the audit passes.

## Relationship to Other Skills

| Skill | Use |
|---|---|
| `/earnings-review` | Faster, focused earnings review |
| `/earnings-team` | Important filing requiring parallel research and publication |
| `/investment-team` | Full first-time company research |

## Principles

- Prioritize original documents.
- Make the four perspectives challenge one another.
- Team Lead synthesis is judgment, not assembly.
- Give a clear conclusion.
- Attach disconfirming evidence to positive findings.
- Editing must improve clarity without lowering rigor.
- Reader review must materially influence the final article.
- Cross-check material data and use exact calculation tools.
