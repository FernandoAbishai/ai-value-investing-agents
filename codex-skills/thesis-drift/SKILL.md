---
name: thesis-drift
description: "AI Value Investing Agents skill: Investment Thesis Drift Detection: Separate Evidence Changes from Wording Changes. Source: skills/thesis-drift.md."
---

## Codex adapter note

This skill is generated from `skills/thesis-drift.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Investment Thesis Drift Detection: Separate Evidence Changes from Wording Changes

Analyze $ARGUMENTS to determine whether an investment thesis has materially changed.

**Supported input formats**:
- `Company old-report-path new-report-path` — compare two research reports or thesis snapshots.
- `Company reports/{company}-thesis-old-date.md reports/{company}-thesis-new-date.md` — compare dated thesis snapshots.
- `Company` — automatically locate `reports/{company}-thesis.md` and historical snapshots in the same area; if no baseline exists, use the missing-baseline procedure.

The purpose is to distinguish changes in facts from changes in price, tone, structure, or wording.

## Design Principle

Long-term investors must separate three different events:

- **Evidence changed**: revenue, margins, cash generation, competitive position, management behavior, or capital allocation changed in a verifiable way.
- **Price changed**: market sentiment or valuation multiples changed while the business remained substantially the same.
- **Wording changed**: two reports express the same underlying evidence and thresholds differently.

Only evidence-driven changes count as thesis drift. A rewritten paragraph is not drift, and a share-price move is not automatically a fundamental change.

This workflow depends on the structured outputs of `thesis-tracker`: core thesis, testable assumptions, red lines, valuation anchors, and monitoring history. If those structures are missing, reconstruct only what the reports actually support and label every unavailable dimension.

## Step 0: Confirm the Current Date

Run `date` before using current market data, filings, or recent news. Put the comparison date and each source period in the report.

## Step 1: Determine the Operating Mode

Parse `$ARGUMENTS`:

- Two report paths supplied → **specified-report comparison**.
- Company name only → **automatic snapshot comparison**.
- Only one usable report or no historical baseline → **missing-baseline procedure**.
- Reports refer to different companies or securities → stop and require explicit confirmation; do not perform cross-company drift analysis.

---

## Mode A: Specified-Report Comparison

### A1. Read and Validate Both Reports

Extract from each report:

- report date, company name, ticker, and listing;
- five-sentence core thesis, when present;
- core assumptions;
- red-line conditions;
- valuation anchors;
- monitoring history;
- management-quality judgment;
- moat and competitive-position judgment;
- recommended action: buy, hold, watch, reduce, or exit.

If a report lacks a required structure, mark it `Structure missing` and extract only supported evidence from the prose. Use `Unable to determine` where evidence cannot be recovered. Never invent the missing baseline.

### A2. Normalize the Evidence

Organize both reports into the same evidence table:

| Dimension | Old-report evidence | New-report evidence | Source | Verifiable? |
|---|---|---|---|---|
| Valuation anchors | | | | |
| Core assumptions | | | | |
| Red lines | | | | |
| Management quality | | | | |
| Competitive moat | | | | |

Compare evidence, definitions, thresholds, and reporting periods—not writing style. Synonyms, reordered sections, stronger adjectives, or shorter prose with unchanged facts must be classified as `Unchanged`.

### A3. Verify Numbers and Valuation

Use `tools/financial_rigor.py` for every decision-sensitive calculation. Do not use mental arithmetic.

```bash
python3 tools/financial_rigor.py verify-valuation \
  --price {current_price} \
  --eps {eps} \
  --bvps {book_value_per_share} \
  --fcf-per-share {free_cash_flow_per_share}
```

Use the appropriate commands for market capitalization, percentage changes, cross-source reconciliation, and scenarios:

```bash
python3 tools/financial_rigor.py verify-market-cap \
  --price {price} --shares {shares} --reported {reported_market_cap} --currency {currency}

python3 tools/financial_rigor.py cross-validate \
  --field {field} --values '{JSON}' --unit {unit}

python3 tools/financial_rigor.py three-scenario \
  --price {price} --eps {eps} --shares {shares} \
  --growth {bull} {base} {bear} --pe {bull_pe} {base_pe} {bear_pe}

python3 tools/financial_rigor.py calc --expr '{exact_expression}'
```

Cross-check decision-critical financial data with at least two independent sources when available. Mark unsupported, inconsistent, or non-reproducible figures as `Low confidence / verification required`.

### A4. Classify Drift by Fixed Dimension

Use exactly these five dimensions:

| Dimension | Focus | Improved | Unchanged | Weakened |
|---|---|---|---|---|
| Valuation anchors | Intrinsic value, PE/PB/FCF yield, margin of safety, valuation range | Margin of safety expanded or intrinsic value rose on verified assumptions | No material change in range or margin of safety | Margin of safety narrowed, intrinsic value fell, or valuation assumptions failed |
| Core assumptions | Revenue, margins, cash flow, users, orders, capacity, or other testable assumptions | More assumptions gained supporting evidence | Status and evidence remain materially similar | Assumptions weakened, were damaged, or failed |
| Red lines | Integrity, regulation, business decline, competitive breach, abnormal management action | Previously elevated red-line risk materially declined | No trigger and risk level unchanged | A red line triggered or became materially more likely |
| Management quality | Integrity, execution, capital allocation, shareholder alignment | New actions increase justified trust | Conduct supports the prior judgment | Conduct reduces trust or capital allocation deteriorates |
| Competitive moat | Share, pricing power, switching cost, network effect, cost advantage, substitutes | Moat widened or competitive advantage was newly validated | Competitive position materially unchanged | Moat weakened or a competitor achieved a meaningful breakthrough |

Each dimension must receive exactly one result: `Improved`, `Unchanged`, or `Weakened`. If evidence is genuinely insufficient, report `Unable to determine` separately and explain the missing evidence rather than forcing a direction.

### A5. Apply Evidence-Driven Rules

Every `Improved` or `Weakened` conclusion must cite concrete new evidence, such as:

- a filing line item, including revenue growth, gross margin, operating cash flow, buybacks, or net cash;
- a regulatory filing or issuer announcement;
- a management, regulatory, customer, supplier, or competitive event;
- verified price and valuation data, explicitly labeled as valuation change rather than business change.

If no evidence explains the apparent change, classify the dimension as `Unchanged` or `Unable to determine`. Do not infer drift from tone.

### A6. Produce the Drift Report

Use this structure:

```text
1. Comparison objects and period
2. Overall conclusion: did the thesis drift?
3. Dimension drift table
4. Evidence differences
5. Valuation and calculation verification
6. Recommended-action migration
7. Uncertainty and missing sources
8. Next monitoring priorities
```

#### Dimension Drift Table

| Dimension | Old judgment | New judgment | Drift direction | Triggering evidence | Confidence |
|---|---|---|:---:|---|:---:|
| Valuation anchors | | | Improved / Unchanged / Weakened | | High / Medium / Low |
| Core assumptions | | | Improved / Unchanged / Weakened | | High / Medium / Low |
| Red lines | | | Improved / Unchanged / Weakened | | High / Medium / Low |
| Management quality | | | Improved / Unchanged / Weakened | | High / Medium / Low |
| Competitive moat | | | Improved / Unchanged / Weakened | | High / Medium / Low |

For an `Unchanged` row, use `—` in the triggering-evidence column. Do not manufacture a trigger to fill the table.

The overall conclusion must answer:

1. Did the thesis drift? `No drift`, `Positive drift`, `Negative drift`, or `Insufficient evidence`.
2. Where did the drift originate? Valuation, fundamentals, management, competition, or a red-line event.
3. Was it a fact change or only a price change?
4. How should the action migrate? For example: Watch → Buy, Buy → Hold, Hold → Reduce, or Reduce → Exit.
5. What evidence is required next? A filing, management explanation, regulatory disclosure, customer data, or competitor result.

---

## Mode B: Automatic Snapshot Comparison

### B1. Locate Candidate Snapshots

Search within `reports/` for:

- `reports/{company}-thesis.md`;
- `reports/{company}-thesis-*.md`;
- files under `reports/{company}/` containing `thesis`, `tracking`, or an equivalent localized term.

Use the earliest structurally complete file as the old report and the latest structurally complete file as the new report. User-specified dates take precedence.

### B2. Prevent Incorrect Pairing

Before comparison, confirm:

- company name or ticker matches;
- report dates differ;
- both files contain an extractable thesis or research conclusion.

If identity cannot be confirmed, stop and require explicit file paths.

### B3. Execute Mode A

After selecting two valid snapshots, perform the complete Mode A workflow.

---

## Mode C: Missing-Baseline Procedure

When only one report exists or no historical baseline can be found:

1. State clearly that drift cannot be measured without a historical baseline.
2. Do not reconstruct a former thesis from memory, market narratives, or current hindsight.
3. Direct the user to run `thesis-tracker` to create a structured baseline.
4. If the current report is sufficiently complete, recommend saving it as `reports/{company}-thesis.md` for future comparisons.

Use this output:

```text
Investment-thesis drift cannot be evaluated: no historical baseline was found.

Located:
- Current report: {path / not found}
- Historical baseline: not found

Next steps:
1. Run thesis-tracker for {company} to establish the baseline.
2. After the next filing or material event, compare the old and new reports with thesis-drift.
```

## Key Principles

- **Evidence before wording** — paraphrasing is not drift.
- **Fundamentals before price** — price affects valuation anchors, not automatically business quality.
- **Verify every number** — use `tools/financial_rigor.py` for percentages, multiples, market capitalization, and scenario arithmetic.
- **Preserve uncertainty** — missing or inconsistent evidence must remain uncertain.
- **Handle red lines separately** — a low valuation cannot offset an integrity or thesis-breaking event.
- **Make the output auditable** — every non-neutral conclusion must trace to specific evidence.
