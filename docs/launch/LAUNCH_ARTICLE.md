# Launching AI Value Investing Agents v1.0.0

Today I am releasing **AI Value Investing Agents v1.0.0**, the first stable version of a maintained English-first, multi-agent value-investing research framework for Claude Code and OpenAI Codex.

The project is designed for one recurring problem: general-purpose AI can produce fluent investment commentary, but fluency is not the same as disciplined research. A useful workflow needs explicit source rules, repeatable decision gates, exact arithmetic, uncertainty labels, valuation checks, and a clear path from evidence to action.

AI Value Investing Agents packages those requirements into reusable workflows.

## What is included

The release provides **20 canonical English workflows** shared by Claude Code and Codex, covering:

- public- and private-company research;
- multi-agent fundamental analysis;
- earnings and financial-data review;
- industry mapping, screening, and supply-chain bottleneck discovery;
- management and capital-allocation analysis;
- income-investment review;
- portfolio concentration and sizing;
- post-purchase thesis monitoring and drift detection;
- long-form research and publication workflows.

Codex also includes one additional hand-written reporting overlay, `investment-memo-craft`, for converting validated research into a decision-ready long-form report.

## Why the canonical-source architecture matters

The project does not maintain separate logic for Claude Code and Codex.

The canonical workflow lives in `skills/*.md`. From that source, the repository generates:

- `codex-skills/*/SKILL.md` packages;
- optional `codex-prompts/*.md` slash prompts.

This prevents the two environments from quietly drifting into different research standards. Continuous integration checks that the shared inventory remains synchronized.

## Research discipline built into the workflows

The workflows are structured to require several habits that generic prompts often omit:

1. **Confirm the current date** before using recent prices, filings, executives, laws, products, or market events.
2. **Prefer primary sources** and identify the reporting period, currency, units, publication date, and access date.
3. **Cross-check decision-critical figures** when independent sources are available.
4. **Use exact calculation tools** instead of mental arithmetic for valuation, market capitalization, payout, scenario, and portfolio calculations.
5. **Separate verified facts, estimates, assumptions, and analytical judgments.**
6. **Apply blocking gates** so that integrity, debt, evidence, or structural-business failures cannot be averaged away by an attractive score.
7. **Audit financially material reports** before treating them as publication-ready.
8. **State uncertainty and missing evidence** rather than filling gaps with confident prose.

## Clear attribution and lineage

AI Value Investing Agents is an independently maintained English-first edition derived from the original `xbtlin/ai-berkshire` project.

The original methodology, Chinese workflow material, historical research archive, and historical performance materials were created or published by the original maintainer. This edition preserves that lineage while rebuilding the operational layer for English use, consistent Claude Code and Codex behavior, and clearer source and attribution requirements.

Workflows inspired by real investors are presented as analytical frameworks. They do not impersonate those people, fabricate quotations, or imply endorsement.

## Tested installation

The v1.0.0 release is validated on:

- Ubuntu;
- macOS;
- Windows.

The automated checks verify:

- 20 canonical shared workflows;
- 20 matching generated Codex shared skills;
- exactly one declared Codex-only skill;
- 20 optional Codex prompts;
- clean installation of 20 Claude Code commands, 21 Codex skills, and 20 prompts;
- Python compilation and generator consistency.

## Installation

Clone the repository:

```bash
git clone https://github.com/FernandoAbishai/ai-value-investing-agents.git
cd ai-value-investing-agents
```

For Claude Code:

```bash
./scripts/install-claude-commands.sh
```

For OpenAI Codex:

```bash
./scripts/install-codex-skills.sh
./scripts/install-codex-prompts.sh
```

Windows `.bat` installers are included in `scripts/`.

## A reproducible first run

The repository includes an end-to-end quickstart using `investment-checklist` to compare Microsoft, Alphabet, and Amazon.

The example intentionally does not store a timeless investment conclusion. Instead, it shows the process a correct run should follow: confirm the date, retrieve current evidence, evaluate each company through the same gates, perform exact calculations, preserve the strongest counterargument, and audit the resulting report.

See [`docs/QUICKSTART_DEMO.md`](../QUICKSTART_DEMO.md).

## What this release is not

This project does not promise that AI-generated research is correct. It does not replace primary documents, independent judgment, or qualified financial, legal, accounting, or tax advice.

Its purpose is narrower and more useful: make the research process more explicit, repeatable, auditable, and difficult to fake with polished language alone.

## Repository

**FernandoAbishai/ai-value-investing-agents**

Release: **v1.0.0 — English Edition**
