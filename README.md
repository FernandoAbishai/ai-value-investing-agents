# AI Value Investing Agents

[English](README.md) · [中文](README_ZH.md) · [日本語](README_JA.md)

**An English-first, multi-agent value-investing research framework for Claude Code and OpenAI Codex.**

AI Value Investing Agents turns the principles associated with Warren Buffett, Charlie Munger, Li Lu, and Duan Yongping into reusable AI research workflows for company analysis, earnings reviews, industry screening, portfolio management, and investment-thesis monitoring.

> This repository is an independently maintained English-first fork of [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire). The original methodology, Chinese source material, historical reports, and performance records were created or published by the original maintainer. Fernando Abishai maintains this edition and its English adaptation.

## Why this repository exists

Generic AI investment prompts often produce inconsistent, noncommittal answers. This framework provides structured workflows with explicit decision gates, source validation, valuation checks, risk analysis, and reproducible output formats.

It is designed to help users:

- Analyze public and private companies with repeatable research processes.
- Run multiple investment perspectives in parallel.
- Cross-check financial data and calculations.
- Screen industries and compare companies consistently.
- Track whether an investment thesis is strengthening, weakening, or being falsified.

## Current translation status

The repository now uses English as its default entry point. Translation of the operational files is being completed in stages.

| Area | Status |
|---|---|
| Main README | English |
| Installation instructions | English and updated for this fork |
| Community and maintenance documentation | English-first |
| Core canonical workflows | `investment-research`, `investment-team`, `investment-checklist`, `financial-data`, and `news-pulse` translated |
| Remaining canonical `skills/*.md` workflows | Translation in progress |
| Generated Codex skills and prompts | Synchronized from the current canonical workflow sources |
| Historical research reports | Preserved primarily in their original language |

The translated core workflows are available for both Claude Code and Codex. Workflows not yet translated may still contain legacy-language content in both canonical and generated files.

## Skills

### Deep research

- [`investment-research`](skills/investment-research.md): comprehensive company research.
- [`investment-team`](skills/investment-team.md): parallel multi-agent company analysis.
- [`management-deep-dive`](skills/management-deep-dive.md): management quality and capital-allocation review.
- [`private-company-research`](skills/private-company-research.md): research for information-scarce private companies.
- [`deep-company-series`](skills/deep-company-series.md): long-form company research series.

### Earnings and financial analysis

- [`earnings-review`](skills/earnings-review.md): primary-source earnings analysis.
- [`earnings-team`](skills/earnings-team.md): parallel earnings interpretation and editorial synthesis.
- [`financial-data`](skills/financial-data.md): financial data retrieval and cross-validation.

### Industry screening

- [`industry-research`](skills/industry-research.md): industry value-chain mapping.
- [`industry-funnel`](skills/industry-funnel.md): progressive market-to-shortlist screening.
- [`quality-screen`](skills/quality-screen.md): quantitative quality filtering.
- [`bottleneck-hunter`](skills/bottleneck-hunter.md): supply-chain bottleneck discovery.
- [`investment-checklist`](skills/investment-checklist.md): rapid pre-research decision gates.

### Portfolio and thesis management

- [`income-investment`](skills/income-investment.md): income-oriented equity analysis.
- [`portfolio-review`](skills/portfolio-review.md): portfolio concentration, sizing, and rebalancing.
- [`thesis-tracker`](skills/thesis-tracker.md): post-purchase thesis monitoring.
- [`thesis-drift`](skills/thesis-drift.md): comparison of thesis changes across reports.
- [`news-pulse`](skills/news-pulse.md): rapid attribution of major price moves.

### Thinking and publishing

- [`dyp-ask`](skills/dyp-ask.md): Duan Yongping-inspired reasoning workflow.
- [`wechat-article`](skills/wechat-article.md): multi-agent investment article workflow.

## Installation

### Claude Code

```bash
npm install -g @anthropic-ai/claude-code

git clone https://github.com/FernandoAbishai/ai-value-investing-agents.git
cd ai-value-investing-agents
./scripts/install-claude-commands.sh
```

Windows:

```bat
git clone https://github.com/FernandoAbishai/ai-value-investing-agents.git
cd ai-value-investing-agents
.\scripts\install-claude-commands.bat
```

### OpenAI Codex

Install Codex using an official installation method, then clone this repository:

```bash
git clone https://github.com/FernandoAbishai/ai-value-investing-agents.git
cd ai-value-investing-agents
./scripts/install-codex-skills.sh
```

Optional slash prompts:

```bash
./scripts/install-codex-prompts.sh
```

Windows:

```bat
git clone https://github.com/FernandoAbishai/ai-value-investing-agents.git
cd ai-value-investing-agents
.\scripts\install-codex-skills.bat
.\scripts\install-codex-prompts.bat
```

## Usage examples

Claude Code commands:

```text
/investment-research Tencent
/investment-team NVIDIA
/earnings-review Apple 2026Q2
/industry-funnel AI infrastructure
/investment-checklist Microsoft, Alphabet, Amazon
/portfolio-review Apple 30%, Microsoft 25%, Cash 20%
/news-pulse Tesla
```

Codex skill requests:

```text
Use investment-research to research Tencent.
Use earnings-review to analyze Apple's latest quarterly results.
Use industry-funnel to screen AI infrastructure companies.
Use thesis-drift to compare two investment thesis reports.
```

## Repository architecture

```text
skills/*.md                 Canonical workflow sources
codex-skills/*/SKILL.md     Generated Codex skill packages
codex-prompts/*.md          Optional Codex slash prompts
scripts/                    Installation and synchronization scripts
tools/                      Financial validation utilities
reports/                    Historical and community research output
docs/                       Maintainer and edition documentation
```

Canonical workflows should be edited in `skills/*.md` first. Generated Codex files should then be synchronized using the repository scripts rather than translated independently.

## Financial rigor

The repository includes `tools/financial_rigor.py` for exact-decimal calculations and validation tasks such as:

- Market-cap verification.
- Valuation-ratio verification.
- Multi-source value comparison.
- Bull, base, and bear scenario calculations.
- Benford's Law checks.

AI output can contain factual, mathematical, or sourcing errors. Always verify primary documents, currencies, share counts, units, dates, and calculations before making a financial decision.

## Historical reports and performance material

Historical reports and portfolio-performance screenshots are retained as source material from the original project. They are not presented as results produced, owned, or independently audited by the maintainer of this English edition.

Past performance does not guarantee future results. Nothing in this repository constitutes investment advice.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request. Translation contributions should preserve command names, file paths, variables, output contracts, and financial terminology.

The current translation roadmap is documented in [docs/ENGLISH_EDITION.md](docs/ENGLISH_EDITION.md).

## License

This project is distributed under the repository's [MIT License](LICENSE).

## Disclaimer

This repository is for educational and research purposes only. It does not provide investment, legal, accounting, or tax advice. Perform independent due diligence and consult qualified professionals when appropriate.

---

Maintained by [Fernando Abishai](https://github.com/FernandoAbishai). Original project and methodology: [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire).
