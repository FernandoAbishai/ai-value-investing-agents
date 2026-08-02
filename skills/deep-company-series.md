# Understand a Company: A 3–8 Article Deep-Research Series

Create a long-form public series about $ARGUMENTS. The series should contain three to eight standalone but connected articles, with the count determined by company complexity rather than a fixed template.

Reference structure: `reports/{company}/understand-{company}/`

The defining capability of this workflow is not merely producing long prose. It is rigorous revision: reconciling figures, eliminating false precision, separating fact from scenario, checking attribution, and keeping valuation, management, and business conclusions consistent across the entire series.

## 1. When to Use This Workflow

Use it when the user wants a comprehensive, publication-ready company series rather than a single research memo.

The series should:

- move from misconception correction to business understanding and decision framework;
- allow each article to stand alone while sharing one consistent evidence base;
- serve readers willing to invest substantial time in understanding a company;
- cover both the investment case and the strongest reasons it may fail.

Do not use this workflow for:

- a single company report — use `investment-research`;
- an earnings update — use `earnings-review`;
- an industry map — use `industry-research`;
- a pre-purchase gate — use `investment-checklist`.

## 2. Select the Number of Articles Before Writing

The series is not automatically eight articles. Count the number of company-specific questions that can independently support a substantive article.

| Complexity | Characteristics | Suggested count |
|---|---|---:|
| High | Several distinct businesses, hidden assets or investments, and a long management record | 7–8 |
| Medium | Two or three material businesses plus one major strategic or technological variable | 4–6 |
| Low | One clear core business and a small number of decisive questions | 3 |

### Standard Three-Article Compression

Use all eight analytical axes as a checklist, but combine them when the company does not justify separate pieces.

| Article | Direction | Axes combined |
|---|---|---|
| 01 | What the market misunderstands about X | Misconceptions, business model, moat, profit-engine overview |
| 02 | X’s decisive variable | Hidden assets, technology, regulation, or another company-specific variable |
| 03 | What it is worth and what would break the thesis | Financial quality, management, valuation, red lines, decision framework |

If an article repeats the same evidence with different wording, the series is too long and should be merged. If a draft cannot reasonably contain one decisive question without becoming unwieldy, split it.

## 3. Eight-Axis Template for Complex Companies

| # | Article direction | Decisive question | Typical length |
|---:|---|---|---:|
| 01 | You may not understand X as well as you think | Which three common market assumptions are wrong or incomplete? | 4,000–5,000 words/characters as appropriate |
| 02 | X’s moat: `<one-sentence business essence>` | How strong is the moat, and will it remain in five or ten years? | 6,000–8,000 |
| 03 | X’s largest profit engine: `<business>` | What really generates owner earnings, and why might it persist? | 6,000–8,000 |
| 04 | The other company hidden on X’s balance sheet | What subsidiaries, investments, or hidden assets materially affect value? | 8,000–10,000 |
| 05 | Is X a winner or loser under the current structural change? | How does AI, regulation, energy, geopolitics, or another major variable affect each business? | 8,000–10,000 |
| 06 | Reading X’s financials as a long-term owner | What do margins, FCF, ROE, dilution, and reinvestment reveal? | 8,000–10,000 |
| 07 | Can shareholders trust X’s management? | What do integrity, execution, capital allocation, and succession evidence show? | 8,000–10,000 |
| 08 | What price is attractive, and what evidence requires reassessment? | What do SOTP or scenarios imply, and which red lines matter? | 10,000–12,000 |

Create `00-series-guide.md` as an unpublished directory and methodology page.

Adapt the axes to the company. If it has no meaningful investment portfolio, replace or merge Article 04. If a company-specific issue such as a major product, regulation, or distribution system deserves an article, use it. The test is whether the article can answer one sharp question with independent evidence.

## 4. Shared Structure for Every Article

Each article must include:

- a header block: `> Understand X · Article 0N · <axis>`;
- an estimated reading time;
- an opening based on a verified contradiction, curve, event, or number rather than generic background;
- a clear statement of the question the article will resolve;
- primary evidence, counterevidence, and uncertainty;
- a final `Key takeaways` section with five to eight points whose figures exactly match the body;
- a `Next article` preview framed as a question, without revealing the conclusion;
- a closing disclosure that the series uses public information and value-investing frameworks and is not investment advice.

## 5. Article-Specific Structures

### Article 01: Misconception Reset

- Show how the market has repeatedly reclassified the company.
- Identify three common misconceptions.
- Refute or qualify each with filings and operating evidence.
- Provide a reading map linking the remaining articles.
- End with valuation or business questions, not a premature conclusion.

### Article 02: Moat

- List identifiable challengers and what happened, including dates and sources.
- Explain what users, customers, suppliers, or developers cannot easily move.
- Map the ecosystem or reinforcing loop.
- Test moat durability over five and ten years.
- Run an inversion exercise: with very large capital, which parts remain difficult to replicate?

### Article 03: Profit Engine

- Open with a counterintuitive operating figure.
- Explain the core product or service at the level of pricing power and customer value.
- Quantify plausible growth paths and include the strongest reason they may not occur.
- Examine the organizational capability that sustains the product.
- Explain why the market may misprice the engine.
- Test the effect of the major structural variable.
- Describe a five-year operating picture as a scenario, not a fact.

### Article 04: Hidden Assets

- Build a table of material non-consolidated investments only.
- Explain consolidated versus non-consolidated accounting to prevent double counting.
- Separate strategically permanent holdings from assets that may be reduced or distributed.
- Explain why the market applies a holding-company or uncertainty discount.
- Identify surprising assets or accounting effects.
- Show a simple discount-range method without false precision.

### Article 05: Structural Variable

- Start with the number or event causing the greatest market concern.
- Analyze each business separately; do not force one company-wide conclusion.
- Ask whether the company can still win economically after losing one visible product or technology contest.
- Model paths by which the company may be bypassed over five to ten years.
- Provide several scenarios with explicit triggers.
- End with a one-year monitoring checklist.

### Article 06: Financial Quality

- Open with a meaningful financial curve.
- Explain gross-margin and operating-margin changes.
- State why GAAP, IFRS, non-GAAP, or another measure is used and reconcile differences.
- Analyze EPS, dilution, share-based compensation, and buybacks.
- Review net cash, debt, and liquidity.
- Analyze cash conversion and FCF yield.
- Apply a capital-allocation or retained-earnings test.
- Explain whether ROE changes are positive or mechanically distorted.
- Compare valuation with peers and the company’s own history on a consistent basis.
- Run the repository’s value-investing checklist.
- Compress the financial conclusion into three evidence-based sentences.

### Article 07: Management

- Provide a core-team table.
- Attribute long-term contributions to specific decisions, not adjectives.
- Test alignment through ownership, compensation, and capital-allocation incentives.
- Use one real crisis as an integrity and communication test.
- Audit five years of concrete management promises against outcomes.
- Evaluate acquisitions, divestitures, buybacks, dividends, and reinvestment.
- Address succession risk directly.
- Answer three stewardship questions: integrity, competence, and long-term commitment.
- Provide a supported score or category with limitations.

### Article 08: Decision Framework

- Use a sum-of-the-parts model when appropriate and explain exactly what the investor owns.
- Show historical valuation ranges while warning that hindsight is not a forecast.
- Build bull, base, and bear operating scenarios with explicit assumptions.
- Label all future values as scenarios or estimates.
- Include a red-line list: a trigger requires reassessment, not an automatic action unless explicitly justified.
- Conclude with asymmetric payoff and opportunity cost, not certainty.

## 6. Writing Style

### Voice

- Direct, analytical, and economical.
- Evidence first, reasoning second, conclusion last.
- Present the strongest opposing case for every central claim.
- Use value-investing frameworks without stacking famous names or unverified quotations.
- Make the opening line independently meaningful on a mobile preview.

### Avoid

| Avoid | Reason | Use instead |
|---|---|---|
| obviously, certainly, inevitably | unsupported certainty | the evidence indicates; under these assumptions |
| I think, I feel | weakens evidence discipline | remove or write `under this framework` |
| textbook-perfect, brilliant, flawless | promotional praise | describe the specific operating fact |
| massively undervalued | undefined judgment | state the estimated discount range and assumptions |
| guaranteed, cannot fail | impossible standard | define risk and invalidation conditions |

### Titles

- Use a verified contrast, number, or counter-consensus conclusion.
- Keep subtitles neutral and descriptive.
- Avoid clickbait comparisons such as “the next Berkshire” or “the Chinese version of X.”
- Prefer company and business terminology to personality-driven framing.

## 7. Fact-Checking and False-Precision Controls

### Common False-Precision Traps

1. **Probability-weighted expected return** — do not combine subjective probabilities into a precise expected percentage. Show scenarios, triggers, and direction instead.
2. **Third-party user or share estimates** — methodologies may differ materially. Use the most credible comparisons as anchors, explain definitions, and avoid pretending incompatible estimates are equivalent.
3. **Linear extrapolation** — do not extend one year’s growth mechanically for five or ten years. Use ranges and operating assumptions.
4. **Undisclosed private-company ownership** — label unknown ownership as unknown; do not infer a precise percentage.
5. **Single-cause attribution** — competitor failure, margin change, or market-share movement usually has several causes. Represent the alternatives.
6. **Historical valuation as forecast** — a former multiple is context, not a target.
7. **Management quotation drift** — verify the original wording and date before using quotation marks.

### Mandatory Seven-Part Revision Check

```text
[ ] 1. Cross-article number consistency: market cap, earnings, FCF, ownership, and share count agree.
[ ] 2. Metric definitions: GAAP/IFRS/non-GAAP/SBC/FCF treatments are explicit.
[ ] 3. Double-counting scan: consolidated subsidiaries are not also counted as investments; SOTP parts do not overlap.
[ ] 4. Fair peer comparison: enterprise-value and cash adjustments are applied consistently.
[ ] 5. Subjective probability weighting removed.
[ ] 6. Unsupported absolute language removed.
[ ] 7. Every non-filing data point has a source and date.
```

### Company-Specific Error Register

Before drafting, create an internal list of known high-risk facts requiring direct verification:

- cumulative investment cost versus current value;
- latest ownership percentages;
- treatment and recognition date of in-kind distributions;
- share-count changes caused by buybacks and stock compensation;
- segment definitions and changes;
- currency, units, and reporting-period mismatches.

Do not embed old examples as permanent facts. Verify company-specific values against the latest primary material.

## 8. Execution Workflow

### Phase 1: Research

Before writing the first two articles:

1. Read the last five annual reports when available and the latest interim or quarterly filing.
2. Read at least three independent high-quality analyses to identify consensus and disagreement; do not treat sell-side opinion as primary evidence.
3. Generate an internal research base with `investment-team` or `investment-research`.
4. Define the article count and each decisive question.
5. Build a shared fact table with source, period, currency, unit, confidence, and article references.

### Phase 2: Draft in Order

- Write articles sequentially from 01 to the final article.
- Save each draft under `reports/{company}/understand-{company}/0N-{slug}.md`.
- If that directory already contains an older series, preserve it and use `reports/{company}/understand-{company}-{YYYYMMDD}/`.
- Do not publish or push drafts before the requested review stage.
- Apply user revisions before final publication.

### Phase 3: Cross-Article Consistency Scan

After all articles are drafted, use parallel review or an Explore Agent to check:

1. repeated figures and ownership percentages;
2. first-use definitions of technical and accounting terms;
3. cross-references between articles;
4. key-takeaway figures versus body text;
5. valuation inputs and output consistency;
6. citations and dates;
7. duplicated paragraphs or evidence.

### Phase 4: Release Audit

For each financially material article, run the report audit when applicable:

```bash
python3 tools/report_audit.py extract --report {article_path}
python3 tools/report_audit.py verdict --results '<verified JSON>' --report {article_filename}
```

Before committing public reports, scan for private or local information:

```bash
grep -r "<local-username>\|/Users/\|/home/[^/]*/\|<private-identifier>" reports/ | head
```

Resolve every match before `git pull --rebase`, commit, and push.

## 9. Handling Revision Requests

### Step 1: Verify Before Editing

When a user says a fact is wrong, compare:

- the user-provided figure;
- the primary-source figure;
- the figure currently used in the series.

Do not automatically replace one unverified number with another.

### Step 2: Classify the Revision

| Level | Type | Treatment |
|---|---|---|
| Blocking | Wrong number, attribution, accounting treatment, or company identity | Correct immediately and scan all dependent calculations |
| Material | Unsupported certainty, misleading comparison, or omitted counterevidence | Weaken, qualify, or rewrite |
| Detail | Source format, terminology, or explanatory granularity | Improve while preserving readability |
| Unreliable | Conflicting third-party estimates with no defensible reconciliation | Remove or present as a range with limitations |

### Step 3: Perform Dependency Checks

A single correction may require series-wide changes:

- market capitalization → valuation multiples, discount, FCF yield, and scenario outputs;
- ownership percentage → holdings table, SOTP, history, and disposal analysis;
- metric definition → first-use definition, all later references, and key takeaways;
- share count → EPS, buyback effect, dilution, and per-share value.

### Step 4: Report the Applied Revision

After committing, state:

```text
Commit: {hash}
Revisions applied: {N}
- Direct corrections
- Dependent corrections
- Remaining unresolved items
```

## 10. This Workflow Does Not

- make the investment decision for the reader;
- predict short-term share prices;
- calculate a probability-weighted expected return from subjective probabilities;
- use famous investors’ holdings as proof;
- force eight articles when the company supports fewer;
- publish private user information;
- present framework simulations as authentic quotations from real investors.

## 11. Compliance and Privacy

- Use public, attributable information for public reports.
- Do not include internal company information, private messages, unpublished holdings, or user identity data.
- Verify image and figure reuse rights and provide attribution.
- Keep filesystem paths, usernames, access tokens, and personal identifiers out of committed reports.
- Use one consistent public byline chosen by the user; do not mix identities across files.

## Summary

The standard for an `Understand X` series is not length. It is consistency and auditability: every number reconciles, every assumption is labeled, every counterargument is represented, and every conclusion can be traced to evidence.
