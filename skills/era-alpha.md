# Era Alpha: Identifying, Validating, and Holding High-Growth Core Assets

Apply the **Era Alpha framework** to $ARGUMENTS: build an industry map, identify the core growth question, validate the strongest alpha candidates, establish a valuation anchor, and hold until observable fundamentals break.

The goal is to find companies inside major secular growth trends that combine pricing power, durable barriers, superior growth quality, and a defensible path to outperform their peers.

## Method and operating principles

This workflow adapts a professional-investor process into an executable research system:

1. **Narrow the scope.** Do not attempt to master every industry. Select two or three critical links in the target value chain and understand them deeply.
2. **Cross-check financial statements with high-frequency evidence.** Quarterly reports are delayed snapshots. Use weekly or monthly indicators such as shipments, prices, orders, installations, utilization, traffic, or token consumption to test whether reported trends are still intact.
3. **Use a valuation anchor.** Exceptional growth does not make valuation irrelevant. Prefer concentrated entry when valuation is reasonable or discounted, scale carefully when growth can plausibly absorb a premium, and avoid buying into obvious bubbles.

Relationship to other workflows:

- `industry-research` maps a full value chain.
- `industry-funnel` progressively screens a broad universe.
- `era-alpha` focuses on the narrowest, fastest-growing secular themes and asks which company is capturing the highest-quality alpha, whether that advantage is durable, and exactly what would invalidate the thesis.

## Step 1: Build the industry cognition map

For every important link in the target value chain, answer:

1. What stage is the segment in: introduction, growth, maturity, or decline? Use penetration and growth data.
2. How does the segment make money? Examine gross margin, operating expenses, cash conversion, and capital intensity.
3. What is the competitive structure? Estimate concentration, pricing power, and the main barriers: technology, scale, ecosystem, regulation, distribution, or capital.
4. Who are the alpha candidates? Compare revenue growth, ROE/ROIC direction, market-share changes, and free-cash-flow quality.

Prioritize primary sources: filings, annual and quarterly reports, earnings calls, investor presentations, regulatory data, and industry operating statistics. Treat broker or media opinions as leads rather than evidence.

Cover relevant public and private companies across markets when evidence permits. Do not exclude a candidate merely because it is harder to research.

**Output:** an industry map table with `segment | stage | economics | competitive structure | alpha candidates | one-sentence rationale`, followed by the two or three segments worth deeper work.

## Step 2: Answer the core questions independently

Use evidence from Step 1 rather than repeating market consensus.

1. **Which segment is currently the most important and fastest-growing?** Support the answer with growth, penetration, backlog/order visibility, capacity, or comparable operating data.
2. **Who is the core alpha in that segment?** Test three conditions:
   - pricing power: margins are structurally superior or improving;
   - barriers: competitors cannot reproduce the advantage quickly;
   - growth quality: revenue growth is supported by cash flow, not merely receivables, subsidies, or aggressive accounting.
3. **Why this company instead of the runner-up?** State the alpha-versus-beta difference in one sentence. If that distinction cannot be stated clearly, the thesis is not mature enough.

**Output:** one to three alpha candidates and a falsifiable explanation of why each may deserve that label.

## Step 3: Validate growth durability from five directions

For every candidate, test whether the evidence points consistently toward durable growth.

| Dimension | Required validation |
|---|---|
| Financial statements | Last 4–8 quarters of revenue/profit growth, margin direction, cash conversion, backlog, deferred revenue, inventory, capex, and other forward indicators |
| High-frequency data | Weekly/monthly operating indicators appropriate to the industry; compare them with reported trends |
| Industry evolution | Regulation, technical-route risk, substitution, capacity additions, and risk of oversupply |
| Competitive position | Market-share direction, new entrants, customer concentration, supplier dependence, and bargaining power |
| Macro environment | Rates, credit, capex cycle, commodities, geopolitics, or regulation when material |

Any contradiction must be surfaced explicitly. Do not smooth conflicting evidence into a single confident narrative.

## Step 4: Establish a valuation anchor and entry discipline

1. Where do current P/E, EV/EBIT, EV/Sales, FCF yield, or other relevant metrics sit versus the company's own history?
2. Is the premium plausibly supported by the growth rate and duration? Use exact arithmetic and scenario analysis rather than intuition.
3. Classify the opportunity:
   - **Undervalued or reasonable:** eligible for meaningful entry if the thesis is strong.
   - **Expensive but absorbable:** hold or scale gradually only if growth durability is unusually strong.
   - **Obvious bubble:** watch rather than buy; define the valuation or earnings conditions that would reopen the case.
4. State the preferred entry method: immediate, staged, or conditional on a valuation/fundamental threshold.

Use `tools/financial_rigor.py` for calculations and cross-check material figures under `skills/financial-data.md`.

## Step 5: Define holding discipline and inflection signals

A position should not be exited merely because price is volatile. Hold while the fundamental thesis remains intact: growth has not structurally slowed, competitive position has not weakened, penetration still has room to rise, and the relevant industry/macro regime has not reversed.

For every alpha candidate, build a falsifiable inflection checklist.

| Layer | Example signals |
|---|---|
| Macro | Monetary or credit regime reversal; capex-cycle peak |
| Industry | Oversupply and price collapse; technical displacement; penetration saturation; adverse regulatory change |
| Company | Key leadership departure; two consecutive quarters of material margin deterioration; persistent market-share loss; backlog/deferred-revenue reversal; deteriorating cash conversion |

Every signal must specify **what data to watch, the threshold or direction that matters, and how often to review it**.

## Execution rules

1. For large industries, split research by value-chain segment and run parallel research where tooling permits.
2. Return structured facts with sources before synthesizing opinions.
3. State the data cutoff date.
4. Cross-check material financial figures and calculations.
5. Distinguish reported facts, estimates, and inference.
6. If evidence conflicts, show the conflict and lower confidence instead of hiding it.

## Report structure

1. Industry cognition map and selected core segments
2. Core growth question and alpha candidates
3. Five-dimensional growth-durability validation
4. Valuation anchor and entry discipline
5. Holding discipline and observable inflection checklist
6. At least three ways the thesis could be wrong

Prioritize data density and decision usefulness over narrative filler. The final conclusion must identify the strongest candidate, the evidence required to maintain that view, and the concrete conditions that would invalidate it.
