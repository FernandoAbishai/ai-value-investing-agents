---
name: investment-memo-craft
description: Codex-only writing and layout overlay for AI Value Investing Agents research reports. Use when Codex creates, rewrites, revises, or critiques company, industry, portfolio, or fund research—especially long-form Markdown that needs financial rigor, readable business mechanics, inversion, valuation-to-action guidance, restrained typography, and explicit monitoring signals. Do not use this skill to modify Claude Code canonical workflow sources.
---

# Investment Memo Craft

## Purpose

Turn investment research into a decision-ready Codex report. Preserve the data discipline of the underlying research workflow while making the output easier to use: concrete business mechanics, serious inverse thinking, explicit opportunity cost, action thresholds, and calm Markdown structure.

This is a writing and judgment overlay. It does not replace primary-source checks, `financial-data`, valuation tools, report-audit tooling, or the gates defined by the underlying workflow.

For long-form AI Value Investing Agents output, call the artifact a `research report` by default. Use `investment memo` only when the user explicitly requests that format.

This is a hand-written Codex-only skill kept under `codex-skills/` for simple installation. Do not create `skills/investment-memo-craft.md` unless the workflow is intentionally adopted for Claude Code as well.

## Core Workflow

1. **Open with context; reserve the final action for after the evidence.**
   - State the research date, data cutoff, price, market capitalization, valuation, and short thesis early.
   - Do not front-load a complete buy, hold, or sell table unless the user asks for an executive memo.
   - Put detailed recommendations, user-specific implications, and price bands after business quality, risk, and valuation have been argued.
   - Separate `good business` from `good investment at this price`.

2. **Build the operating map before applying philosophy.**
   - Show revenue structure, segment economics, unit drivers, and three-to-five-year trends.
   - For asset-heavy businesses, identify the assets that explain economics or moat.
   - Explain pricing, customer lock-in, cost structure, reinvestment needs, and cash conversion.

3. **Compress the business essence into one memorable sentence.**
   - Explain who pays, why they pay, what is scarce, and what repeats.
   - Avoid generic labels such as `industry leader` unless the mechanism behind durable leadership is stated.

4. **Make the moat falsifiable.**
   - Assess brand and pricing power, switching costs, network effects, scale, cost advantage, regulation, resource scarcity, technology, and culture as applicable.
   - Explain whether the moat widened or narrowed over the last five years.
   - State what could destroy or bypass it.

5. **Use genuine inversion.**
   - Include failure paths with likelihood, impact, and observable indicators.
   - Write the strongest bear case in language a serious non-buyer would accept.
   - Identify the most likely analytical mistake.
   - Do not assign precise probabilities without a defensible empirical basis.

6. **Evaluate management through capital allocation and conduct.**
   - Replace vague praise with decisions: acquisitions, divestitures, buybacks, dividends, leverage, reinvestment, and strategic pivots.
   - Assess incentives, ownership, controlling-shareholder behavior, compensation, related-party transactions, and shareholder treatment.
   - Determine whether the business depends on one person or on a durable system.

7. **Connect industry trend to value capture.**
   - Separate a broad structural trend from company-level economics.
   - Show where the company sits in the value chain and who captures the profit pool.
   - Identify whether TAM growth, pricing, utilization, market share, or capital intensity is the real driver.

8. **Convert valuation into conditional action.**
   - Show current multiples, reverse-DCF intuition, scenario valuation, historical comparison, and comparable companies when useful.
   - Include dividends and other capital returns where material.
   - Define price bands, reinforcement conditions, reduction conditions, and thesis-breaking evidence.
   - Use exact-arithmetic repository tools for decision-sensitive calculations.

9. **Close with a decision section.**
   - Summarize business quality, moat, management, risk, trend, valuation, and confidence.
   - Separate implications for an investor without a position from those for an existing holder.
   - End by distinguishing evidence confidence from actual investment certainty.

## Style Standards

- Prefer numbers, mechanisms, and sourced examples over adjectives.
- Use tables when they reduce cognitive load: segments, assets, failure paths, management decisions, scenarios, and action bands.
- Write clear investor prose that remains useful after the immediate news cycle.
- Keep memorable formulations, but never let rhetoric outrun evidence.
- Avoid vague recommendations such as `wait and see` without naming the price, event, or evidence that changes the decision.
- Follow the user's requested language. English is the default for this maintained edition.
- Do not imitate real investors or present framework commentary as an authentic quotation or endorsement.

## Layout Standards

For long-form reports, prefer a calm stepped layout:

- Use a simple title such as `{Company} ({ticker}) Research Report`.
- Use dated filenames such as `{company}-research-report-{YYYYMMDD}.md`.
- Start with one compact metadata block: research date, cutoff date, price, market cap, key multiples, and one-sentence thesis.
- Use horizontal separators only between major sections.
- Keep section titles short and concrete; avoid dense numbering such as `2.3.1` unless the document is technical.
- Use quote blocks for framework questions, not to fabricate quotations.
- Treat GitHub Markdown as the typography system. Avoid HTML or CSS styling unless the user requests another artifact format.
- Use bold sparingly for labels, decisive phrases, scenario outputs, action rows, and audit verdicts.
- Keep ordinary facts in normal weight. Excess emphasis makes long research harder to scan.
- Use explicit `+` and `-` signs for growth and return ranges.
- Keep audit and tool detail concise at the end unless reproducibility commands are requested.
- Preserve a prior report's useful reading rhythm only when its facts pass current validation.

## Default Report Shape

Use this order unless the underlying workflow or the user requires another structure:

1. **Research scope and bias controls**
   - Data cutoff, evidence quality, consensus risks, missing information, and likely AI biases.

2. **Core data overview**
   - Segments, operating units or assets, three-to-five-year trends, and source reconciliation.

3. **Business essence**
   - Who pays, why revenue repeats, cost structure, customer behavior, asset life, and principal profit drivers.

4. **Moat assessment**
   - Moat sources, evidence, direction, durability, and invalidation conditions.

5. **Inversion and risk**
   - Serious bear case, failure paths, impact, observable warnings, and the analyst's most likely mistake.

6. **Management and capital allocation**
   - Governance, incentives, reinvestment, M&A, buybacks, dividends, leverage, and succession.

7. **Industry and structural trend**
   - Value-chain position, profit-pool capture, cycle or structural trend, and disruption risk.

8. **Valuation and margin of safety**
   - Current valuation, reverse-DCF intuition, bull/base/bear scenarios, peers where useful, and conditional price bands.

9. **Decision and monitoring plan**
   - Summary table, implications for new and existing investors, action triggers, thesis-breaking evidence, and monitoring cadence.

10. **Evidence confidence versus investment certainty**
    - Separate data quality from the certainty of the investment outcome.

11. **Sources and audit record**
    - Key sources, reporting periods, accessed dates, discrepancies, and concise audit result.

## Quality Bar

A strong report answers these questions directly:

- What does the company sell, to whom, and why does revenue repeat?
- Which two or three variables actually move profit and owner earnings?
- Why might an informed investor refuse to buy?
- What expectations are already reflected in the price?
- What outcomes are plausible under bull, base, and bear scenarios?
- What should a prospective investor study or wait for?
- What should an existing holder monitor?
- What evidence would make the thesis wrong?

## Pairing With Other Skills

When a task requires fresh research, use the relevant canonical workflow and its validation requirements first. Apply this skill afterward to structure or rewrite the result.

Pair especially with:

- `financial-data` for source hierarchy and reconciliation;
- `investment-research` or `investment-team` for full company analysis;
- `management-deep-dive` when stewardship is the central uncertainty;
- `portfolio-review` when position sizing and opportunity cost matter;
- `tools/report_audit.py` before treating financially material output as publishable.
