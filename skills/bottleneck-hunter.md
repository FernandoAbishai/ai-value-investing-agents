# Supply-Chain Bottleneck Hunter: Global Physical-Constraint Opportunity Scan

Scan the megatrend in $ARGUMENTS for supply-chain bottlenecks and investable opportunities.

## Core Idea

Do not ask, “Which stock benefits from this trend?” Ask:

> If the trend continues to scale, which physical input, component, machine, certification, or infrastructure layer becomes insufficient first?

Traditional research focuses on obvious leaders and already popular themes. This workflow starts from physical choke points: overlooked suppliers whose shortage could delay an entire value chain.

First-order constraints such as leading accelerators, HBM, or electricity may already be heavily priced. Potential informational advantage is more likely in second- and third-order layers such as optical components, lasers, compound-semiconductor substrates, specialty wafers, epitaxy equipment, wafer-level testing, IC substrates, specialty glass fiber, cooling, and power distribution.

A real bottleneck is not automatically an investment opportunity. Business quality, financial resilience, and valuation are mandatory gates.

---

## Step 0: Confirm the Current Date

Run `date` before beginning. Use the confirmed year in search queries, report headers, market data, and event timelines. Do not rely on a hard-coded year or training-data assumptions.

---

## Step 1: Confirm the Megatrend

### 1.1 Qualification Criteria

Track only trends that satisfy all four conditions:

| Criterion | Requirement | Validation Method |
|---|---|---|
| Durability | Evidence of at least three to five years of growth | Industry forecasts, committed capacity, and capital-expenditure plans |
| Physical intensity | Requires real hardware, materials, equipment, construction, or infrastructure | Distinguish software upgrades from physical expansion |
| Scale | Global annual capital expenditure above approximately USD 50 billion | Aggregate current guidance from major participants |
| Acceleration | Demand growth exceeds realistic supply-expansion speed | Compare demand growth with announced and qualified capacity |

### 1.2 Initial Trend Watchlist

Refresh this list each time the workflow runs:
1. **AI infrastructure** — compute clusters, networking, data centers, cooling, and power.
2. **Energy transition and grid expansion** — nuclear restarts, transmission, storage, and generation.
3. **Defense modernization** — sustained spending cycles and supply-chain localization.
4. **Semiconductor reindustrialization** — fabrication plants, equipment, materials, and regional duplication.
5. **Space economy** — launch cadence, satellite networks, ground systems, and specialized components.

When the user names a specific trend, focus on that trend rather than automatically scanning the entire watchlist.

### 1.3 Trend-Validation Output

```text
Trend:
Primary driver:
Realized validation events, at least three:
  1. [date] [event] [source]
  2.
  3.
Estimated annual capital expenditure: approximately USD X, growing Y%
Demand growth faster than qualified supply growth? Yes / No / Uncertain
Trend status: Trackable / Insufficient evidence
Information grade: A / B / C
```

Use implemented, funded, contracted, delivered, or reported events. Label forecasts and non-binding announcements separately.

---

## Step 2: Decompose the Physical Supply Chain

### 2.1 Layer Framework

Decompose the trend into physical entities rather than concepts:

```text
Layer 0 — End product or service
    │
Layer 1 — Obvious core systems and components
    │          ↑ often widely covered and heavily priced
    ├────────────────────────────────────────────
    │          ↓ lower-visibility search area
Layer 2 — Subcomponents and specialized materials
    │
Layer 3 — Manufacturing equipment and upstream inputs
    │
Layer 4 — Power, cooling, land, labor, permits, and certification
```

### 2.2 AI-Infrastructure Example

```text
Layer 0: model training and inference services
Layer 1: accelerators, HBM, servers, and data centers
Layer 2:
  ├─ Interconnect: optical modules, fiber, switching silicon, and copper cabling
  ├─ Photonics: EML, VCSEL, and CW lasers; modulators; photodetectors
  ├─ Semiconductor materials: InP, GaAs, SOI, and SiC substrates
  ├─ Advanced packaging: CoWoS-related substrates, HBM TSV, ABF films
  ├─ PCB and substrates: high-speed PCB, IC substrates, specialty glass cloth
  ├─ Testing: probe cards, burn-in, and automated test equipment
  ├─ Thermal management: liquid cooling, CDUs, immersion fluids
  └─ Power distribution: busways, UPS systems, switchgear, and transformers
Layer 3:
  ├─ Epitaxy equipment: MOCVD and MBE
  ├─ Specialized lithography and etching
  ├─ High-purity indium, gallium, germanium, gases, and targets
  └─ Qualification and standards such as MSA and Telcordia
Layer 4:
  ├─ Generation and grid infrastructure
  ├─ Cooling water and heat-rejection infrastructure
  └─ Data-center land, interconnection, and permits
```

### 2.3 Search Strategy

For each confirmed trend, search current English and relevant local-language sources using combinations such as:
- `{trend} supply chain bottleneck {current year}`
- `{trend} shortage critical component`
- `{trend} capacity constraint lead time`
- `{trend} sole source supplier qualification`
- Local-language equivalents for shortage, allocation, expansion, delivery time, and price increases.

---

## Step 3: Identify Bottlenecks

### 3.1 Six Bottleneck Tests

Evaluate every material Layer 2 and Layer 3 segment:

| # | Test | Question | Red / Yellow / Green |
|---|---|---|---|
| 1 | Supply concentration | Are there three or fewer qualified global suppliers? | 🔴 ≤2 / 🟡 3–5 / 🟢 >5 |
| 2 | Expansion lead time | How long does qualified new capacity require? | 🔴 >2 years / 🟡 1–2 years / 🟢 <1 year |
| 3 | Substitution difficulty | Can another material or architecture replace it? | 🔴 No practical substitute / 🟡 Partial / 🟢 Easy |
| 4 | Capacity utilization | How fully utilized is current capacity? | 🔴 >90% / 🟡 70–90% / 🟢 <70% |
| 5 | Demand growth | How fast is downstream demand growing? | 🔴 >50% / 🟡 20–50% / 🟢 <20% |
| 6 | Customer qualification | How long does a new supplier need for approval? | 🔴 >1 year / 🟡 6–12 months / 🟢 <6 months |

Bottleneck rating:
- **S**: four or more red tests; potential single-point failure.
- **A**: three red tests; severe constraint.
- **B**: one or two red tests; pressure exists but may be manageable.
- **Not a bottleneck**: no red tests; remove from the priority list.

Do not assign a red test without a source or a clearly labeled estimate.

### 3.2 Bottleneck Map

```text
Supply-Chain Bottleneck Map — {trend}
Updated: YYYY-MM-DD

S-rated:
  1. [segment] — [one-sentence cause] — suppliers: [list]

A-rated:
  1.

B-rated:
  1.

Changes since the prior scan:
  - Added / Upgraded / Downgraded / Resolved — [segment] — [reason]
```

---

## Step 4: Convert Bottlenecks into a Company Universe

### 4.1 Find All Relevant Public Suppliers

For every S- and A-rated segment, search globally:
- `{component} supplier listed company`
- `{component} manufacturer stock`
- `{component} market share company`
- Local-language supplier and market-share queries.

Cover mainland China, Hong Kong, the United States, Japan, South Korea, Taiwan, Europe, and other relevant exchanges.

### 4.2 Initial Filters

| Criterion | Requirement | Reason |
|---|---|---|
| Tradability | Publicly listed on an accessible market | The security can be evaluated and traded |
| Bottleneck exposure | Prefer more than 30% of revenue from the constrained segment | Economic purity |
| Market capitalization | Prioritize companies below USD 10 billion without excluding larger critical suppliers | Lower coverage may create opportunity |
| Liquidity | Prefer average daily trading value above USD 1 million | Entry and exit feasibility |

Label private companies separately as strategic participants or future IPO candidates.

### 4.3 Mandatory Valuation Gate

**A real bottleneck does not override valuation.** Calculate and disclose market capitalization, annual revenue, P/S, and P/E for every ranked public company.

#### Red Valuation Flags

Any red flag caps signal strength at ★★ and requires the label **Valuation Overextended**:
1. Market capitalization exceeds 20% of the company's realistically addressable market.
2. P/S exceeds 30x while revenue growth is below 100%. Revenue growth above 100% may avoid the automatic cap, but must still be labeled high valuation requiring continued hypergrowth.
3. Market capitalization exceeds ten times an evidence-based optimistic five-year revenue estimate.
4. The share price doubles within 60 days after a financing or large issuance, indicating possible sentiment-driven repricing.

#### Yellow Valuation Flags

Require a specific explanation or rating downgrade:
1. Loss-making company with P/S above 15x.
2. P/S more than five times that of profitable peers without a defensible growth, share, or moat explanation.
3. P/E above 80x without a credible PEG and durable growth case.

#### Green Valuation Signals

Potential positive factors, not automatic buy signals:
- P/S below 10x with growing revenue.
- P/E below 30x with an evidence-based moat.

#### Ten-Year Return Test

For every candidate, answer:

> At the current enterprise or equity value, if the optimistic operating case is achieved and the company exits in ten years at 25x earnings, what annualized return results?

If expected annualized return is below 10%, state that the current price lacks an adequate margin of safety.

Show all assumptions, including dilution, terminal margin, share count, currency, and tax treatment where relevant.

The valuation rules prevent recommendations such as a loss-making company at 100x revenue merely because it occupies a genuine bottleneck. They do not automatically exclude every early-stage high-growth company.

### 4.4 Taiwanese Securities

Supply-chain scans frequently identify four-digit Taiwanese tickers. Use:

```bash
python3 tools/twstock_data.py
```

Follow the Taiwan section of `skills/financial-data.md` for price, market capitalization, P/E, and monthly revenue. Monthly year-over-year revenue is a particularly timely public signal for testing whether a bottleneck is producing volume or pricing gains.

### 4.5 Company Deep-Screen Template

```markdown
## {Company} ({Ticker})

**Bottleneck position**
- Exact value-chain role
- Global market share and rank
- Known customers and qualification status

**Capacity and expansion**
- Current capacity and utilization
- Expansion plan and production timeline
- Required capital versus available cash and financing capacity

**Financial snapshot**
- Market cap, revenue, earnings, and growth
- Bottleneck-business revenue exposure
- Gross-margin trend
- P/S and P/E with data date

**Risk checklist**
- [ ] Substitute technology
- [ ] Dilution, convertibles, or repeated issuance
- [ ] Geopolitical and export-control exposure
- [ ] Governance and management history
- [ ] Customer concentration
- [ ] Valuation already discounts several years of success

**Bottleneck durability**
- When could the constraint be resolved?
- What remains valuable after it resolves?
- Is the opportunity cyclical, structural, or one-time?
```

---

## Step 5: Cross-Validate the Thesis

### 5.1 Positive Validation

| Validation | Question | Preferred Evidence |
|---|---|---|
| Customer | Has a major customer qualified, ordered, or disclosed the supplier? | Customer filings, contracts, and company announcements |
| Revenue | Is the bottleneck visible in reported revenue? | Latest two or three financial periods |
| Pricing | Are product prices increasing? | Industry quotations and reported pricing |
| Capacity | Are lead times, allocation, or utilization genuinely tight? | Delivery data, customer disclosures, and capacity statements |
| Capital | Is the supplier investing to expand? | Capital-expenditure guidance and construction evidence |

### 5.2 Inversion and Bear-Case Validation

| Question | Purpose |
|---|---|
| Why would an informed investor avoid the stock? | Surface the strongest bear case |
| Can the bottleneck be bypassed? | Test technology-route risk |
| Can new regional suppliers replicate capacity quickly? | Test future supply shock |
| What happens if end demand falls 50%? | Test operating leverage and downside |
| Has management issued equity near prior peaks? | Test shareholder alignment |
| What growth assumptions are embedded in the current price? | Test valuation realism |

### 5.3 Signal Consistency

Check whether:
- Multiple suppliers in the same segment report similar demand and pricing.
- Downstream customers disclose the same shortage.
- Industry associations or independent research support the constraint.
- Revenue, hiring, capital expenditure, and lead-time signals point in the same direction.

Conflicting evidence must be displayed rather than averaged away.

---

## Step 6: Produce the Bottleneck Opportunity Dashboard

### 6.1 Ranked Table

| Rank | Company | Ticker | Market Cap | Annual Revenue | P/S | P/E | Bottleneck | Rating | Market Share | Revenue Growth | Signal Strength | Valuation |
|---:|---|---|---:|---:|---:|---:|---|:---:|---:|---:|:---:|---|

Market capitalization, annual revenue, P/S, and P/E are mandatory fields. When reliable financial data cannot be obtained, signal strength cannot exceed ★★.

Signal-strength definitions:
- **★★★★★**: multiple independent validations, qualified customers, reported revenue impact, and a green valuation profile.
- **★★★★**: most validations pass; valuation is green or explainable yellow.
- **★★★**: logic is supported but some evidence remains pending; yellow valuation may be acceptable.
- **★★**: early evidence, missing financial data, or a red valuation flag.
- **★**: concept-only exposure without validation.

### 6.2 One-Page Opportunity Summary

```markdown
## {Company} ({Ticker}) — {one-sentence bottleneck position}

**Why this is a bottleneck**
Two or three evidence-based sentences.

**Why this company**
Why it is better positioned than alternative suppliers.

**Catalyst timeline**
- Near term, one to three months:
- Medium term, three to twelve months:

**Principal risks**
1.
2.

**Key data**
Market cap / annual revenue / P/S / P/E / revenue growth / bottleneck exposure

**Margin-of-safety test**
At the current valuation, required year-ten net income and revenue, assumed 25x exit P/E, resulting annualized return, and conclusion.

**Validation status**
Customer / Revenue / Pricing / Capacity / Valuation / Unresolved items

**Conclusion**
Deep research / Watchlist / Wait for a better price / Stop tracking
```

### 6.3 Actions

| Candidate | Action | Reason |
|---|---|---|
| A | Run `/investment-team` | S-rated bottleneck with multiple validations |
| B | Watch until next financial report | Logic supported but revenue evidence incomplete |
| C | Stop tracking | Substitution or valuation risk dominates |

---

## Step 7: Maintain the Bottleneck Map

### 7.1 Incremental Update

On every run:
1. Recheck whether existing bottlenecks still exist.
2. Identify new suppliers, expanded capacity, and substitution breakthroughs.
3. Search recent supply-chain news and financial disclosures.
4. Upgrade, downgrade, add, or resolve each bottleneck with reasons.

### 7.2 State Files

Maintain:
- `reports/bottleneck-map/master-map.md` — current global map.
- `reports/bottleneck-map/watchlist.md` — current company watchlist.
- `reports/bottleneck-map/YYYY-MM-DD/` — timestamped scan reports.
- `reports/bottleneck-map/deep-dive/` — company-specific research.

---

## Hourly Scan Mode

When this workflow is used by an hourly scheduled task, produce a report only when new information is decision-relevant.

### Hourly Process

1. Search news from the last one or two hours for supply-chain constraints, shortages, allocation, lead times, sole-source dependencies, capacity, and price changes in English and relevant local languages.
2. Check tracked companies for abnormal price moves above approximately 5%; investigate the cause rather than treating the move itself as a signal.
3. Check for financial reports, regulatory filings, production updates, and material announcements.
4. Check whether watchlist valuations entered predefined research or purchase ranges.
5. Produce a report only when there is:
   - A new bottleneck signal.
   - A newly investable candidate.
   - A material status change.

When nothing material changes, record the scan in the task log but do not create a report file.

### File Naming

Directory: `reports/bottleneck-map/YYYY-MM-DD/`

| Situation | File Name | Example |
|---|---|---|
| Investable candidates identified | `HH-MM-TICKER1-TICKER2.md` | `09-00-FORM-IBDN.md` |
| New constraint signal but no qualified security | `HH-MM-signal-scan.md` | `14-00-signal-scan.md` |
| No material change | No file | — |

Only include tickers that passed the valuation gate in the filename.

### Candidate Report Template

```markdown
# Bottleneck Hunter — YYYY-MM-DD HH:MM

## Qualified Candidates

### {Company} ({Ticker}) — {bottleneck position}

**Why it matters now**
The specific event or data change.

**Bottleneck**: Layer X, segment, S/A/B
**Financial snapshot**: market cap / revenue / P/S / P/E / growth
**Valuation flag**: Red / Yellow / Green, with explanation
**Ten-year return test**: assumptions and annualized result

**Bull case**
1.
2.

**Bear case**
1.
2.

**Action**: Deep research / Watch / Wait for price

## Other Signals

| Segment | Signal | Source | Initial Assessment |
|---|---|---|---|

## Watchlist Changes

Added / Upgraded / Downgraded / Removed / No change
```

### Signal-Only Template

```markdown
# Bottleneck Signal Scan — YYYY-MM-DD HH:MM

| Segment | Signal | Source | Investable Candidate? | Next Step |
|---|---|---|:---:|---|

Watchlist status: No change / List changes
```

---

## AI Bias Controls

| Bias | Failure Mode | Countermeasure |
|---|---|---|
| Large-cap preference | Search results are dominated by famous companies | Search explicitly for specialized and small-cap suppliers |
| English-language preference | Japanese, Korean, Taiwanese, and Chinese suppliers are omitted | Search local markets and local-language terms |
| Narrative preference | An “AI” label substitutes for actual exposure | Verify the physical supply-chain position and revenue share |
| Confirmation bias | Only evidence supporting the bottleneck is collected | Complete the inversion checklist in Step 5 |
| Recency failure | Old shortage reports are treated as current | Prioritize the latest 30 days and record source dates |

---

## Highest-Priority Principles

1. **Use AI to decompose supply chains, not to produce unsupported stock tips.**
2. **Physical constraints first.** Focus on products, materials, equipment, facilities, qualification, and infrastructure.
3. **Search beyond the obvious first layer.**
4. **Cross-validate every material conclusion with at least two independent sources.**
5. **State uncertainty honestly.** Missing data must remain missing rather than being filled with invented precision.
6. **Every bottleneck expires eventually.** Estimate the duration and resolution path.
7. **Small market capitalization is not business quality.** Financial resilience and governance still matter.
8. **A real bottleneck is not an investment opportunity at any price.** Valuation is a hard gate that cannot be overridden by purity of exposure, signal strength, or narrative appeal.
9. **Begin with evidence, then reason, then conclude.** Do not start from a bullish position.

## Output Requirements

- Full scan: `reports/bottleneck-map/{trend-name}-bottleneck-{YYYYMMDD}.md`
- Daily scan: `reports/bottleneck-map/daily/{YYYY-MM-DD}-{am-or-pm}.md`
- Master map: `reports/bottleneck-map/master-map.md`
- Watchlist: `reports/bottleneck-map/watchlist.md`
- Write in English unless the user explicitly requests another language.
- Source all data and label estimates.
- Present both supporting and opposing evidence for every core conclusion.
