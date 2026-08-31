# AI Value Investing Agents

[English](README.md) · [中文](README_ZH.md) · [日本語](README_JA.md)

[![Validate](https://github.com/FernandoAbishai/ai-value-investing-agents/actions/workflows/validate.yml/badge.svg)](https://github.com/FernandoAbishai/ai-value-investing-agents/actions/workflows/validate.yml)
[![GitHub release](https://img.shields.io/github/v/release/FernandoAbishai/ai-value-investing-agents?display_name=tag)](https://github.com/FernandoAbishai/ai-value-investing-agents/releases)

**An English-first, multi-agent value-investing research framework for Claude Code and OpenAI Codex.**

AI Value Investing Agents turns principles associated with Warren Buffett, Charlie Munger, Li Lu, and Duan Yongping into reusable AI research workflows for company analysis, earnings reviews, industry screening, portfolio management, thesis monitoring, and long-form publishing.

> This repository is an independently maintained English-first edition derived from [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire). The original methodology, Chinese source material, historical reports, and performance records were created or published by the original maintainer. Fernando Abishai maintains this edition and its English adaptation.

## Why this repository exists

Generic AI investment prompts often produce inconsistent, noncommittal answers. This framework provides structured workflows with explicit decision gates, source validation, valuation checks, risk analysis, uncertainty labels, and reproducible output formats.

It is designed to help users:

- Analyze public and private companies with repeatable research processes.
- Run multiple investment perspectives in parallel.
- Cross-check financial data and calculations.
- Screen industries and compare companies consistently.
- Identify high-growth secular alpha and define observable exit conditions.
- Track whether an investment thesis is strengthening, weakening, or being falsified.
- Produce long-form research with source, privacy, attribution, and revision controls.

## Release status

The canonical operational translation is complete and the maintained branch now incorporates upstream research changes through August 30, 2026.

| Area | Status |
|---|---|
| Stable English-edition release | `v1.1.0` |
| Canonical shared workflows | 21 English `skills/*.md` sources |
| Generated Codex shared skills | 21 synchronized packages |
| Codex-only skills | 1 declared overlay: `investment-memo-craft` |
| Optional Codex prompts | 21 synchronized prompts for shared workflows |
| Installation validation | Ubuntu, macOS, and Windows |
| Unified local management | [`docs/INSTALLATION.md`](docs/INSTALLATION.md) |
| End-to-end demonstration | [`docs/QUICKSTART_DEMO.md`](docs/QUICKSTART_DEMO.md) |
| Verified English examples | [`reports/examples/`](reports/examples/) |
| Public launch kit | [`docs/launch/`](docs/launch/) |
| Support and structured feedback | [`SUPPORT.md`](SUPPORT.md) |
| Social-preview source | [`assets/social-preview-source.svg`](assets/social-preview-source.svg) |
| Historical research reports | Preserved primarily in their original language and synchronized from upstream where compatible |

Claude Code and Codex use the same English canonical workflows for the 21 shared capabilities. Codex additionally includes the hand-written `investment-memo-craft` report-structure overlay. Generated-file checks prevent the shared environments from silently drifting apart.

## Skills

### Deep research

- [`investment-research`](skills/investment-research.md): comprehensive company research, including audited long-horizon terminal-value and IRR analysis.
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
- [`era-alpha`](skills/era-alpha.md): identify core alpha inside secular high-growth themes, validate growth durability, anchor valuation, and define falsifiable holding/exit signals.
- [`investment-checklist`](skills/investment-checklist.md): rapid pre-research decision gates.

### Portfolio and thesis management

- [`income-investment`](skills/income-investment.md): income-oriented equity analysis.
- [`portfolio-review`](skills/portfolio-review.md): portfolio concentration, sizing, and rebalancing.
- [`thesis-tracker`](skills/thesis-tracker.md): post-purchase thesis monitoring.
- [`thesis-drift`](skills/thesis-drift.md): comparison of thesis changes across reports.
- [`news-pulse`](skills/news-pulse.md): rapid attribution of major price moves.

### Thinking and publishing

- [`dyp-ask`](skills/dyp-ask.md): Duan Yongping-inspired reasoning with explicit attribution boundaries.
- [`wechat-article`](skills/wechat-article.md): Author–Editor–Reader workflow for publication-ready long-form articles.
- [`investment-memo-craft`](codex-skills/investment-memo-craft/SKILL.md): Codex-only report-writing and layout overlay.

## Installation

Clone the repository after installing Claude Code, OpenAI Codex, or both through their official distribution channels:

```bash
git clone https://github.com/FernandoAbishai/ai-value-investing-agents.git
cd ai-value-investing-agents
```

### Install both environments

Unix-like systems:

```bash
./scripts/install.sh --all
```

Windows:

```bat
scripts\install.bat --all
```

### Install one environment

```bash
./scripts/install.sh --claude
./scripts/install.sh --codex
```

Codex installation includes 21 generated shared skills, the Codex-only `investment-memo-craft` overlay, and 21 optional compatibility prompts.

### Update, diagnose, or uninstall

```bash
./scripts/manage.sh update --all
./scripts/manage.sh doctor --all
./scripts/manage.sh uninstall --all
```

Windows uses `scripts\manage.bat` with the same arguments.

The manager supports `--dry-run`, collision backups, SHA-256 drift detection, JSON diagnostics, component-specific targets, and safe forced removal. It never downloads content or runs `git pull`.

See [`docs/INSTALLATION.md`](docs/INSTALLATION.md) for destinations, environment overrides, backup behavior, recovery, and backward-compatible commands.

Restart Claude Code or Codex after installation or update.

## End-to-end demonstration

Follow [`docs/QUICKSTART_DEMO.md`](docs/QUICKSTART_DEMO.md) to:

1. install the workflows in either environment;
2. run the same multi-company checklist request;
3. verify the current-date and sourcing behavior;
4. audit a generated report;
5. confirm Claude Code and Codex use synchronized decision structures.

## Verified English examples

The curated [`reports/examples/`](reports/examples/) collection demonstrates the repository's research and audit controls with point-in-time public evidence:

- [`microsoft-fy2026-company-research-20260802.md`](reports/examples/microsoft-fy2026-company-research-20260802.md): full company research, cash conversion, valuation, and scenario analysis;
- [`microsoft-fy2026-q4-earnings-review-20260802.md`](reports/examples/microsoft-fy2026-q4-earnings-review-20260802.md): earnings quality, segment changes, capital intensity, and monitoring signals;
- [`cloud-infrastructure-comparison-20260802.md`](reports/examples/cloud-infrastructure-comparison-20260802.md): definition-aware comparison of Microsoft, AWS, Google Cloud, and Oracle;
- [`VERIFICATION.md`](reports/examples/VERIFICATION.md): source and calculation register.

The examples are newly prepared research artifacts, not mechanical translations of the historical archive. CI requires their metadata and selected audit fixtures to remain valid.

## Public launch resources

The repository includes a reusable launch package:

- [`docs/launch/LAUNCH_ARTICLE.md`](docs/launch/LAUNCH_ARTICLE.md): long-form public announcement;
- [`docs/launch/SOCIAL_POSTS.md`](docs/launch/SOCIAL_POSTS.md): LinkedIn, X, Reddit, Hacker News, and release copy;
- [`docs/launch/SOCIAL_PREVIEW.md`](docs/launch/SOCIAL_PREVIEW.md): preview requirements and upload procedure;
- [`docs/launch/VIDEO_DEMO_SCRIPT.md`](docs/launch/VIDEO_DEMO_SCRIPT.md): 6–8 minute verified-workflow demonstration script;
- [`docs/launch/PUBLISHING_CHECKLIST.md`](docs/launch/PUBLISHING_CHECKLIST.md): research, privacy, attribution, and platform publication gate;
- [`docs/launch/FEEDBACK_PLAN.md`](docs/launch/FEEDBACK_PLAN.md): launch feedback triage, severity, and acceptance process;
- [`assets/social-preview-source.svg`](assets/social-preview-source.svg): editable 1280 × 640 social-card source.

The editable source remains tracked in Git; the raster social preview was uploaded separately through repository settings.

## Support and feedback

Use the structured GitHub issue forms for:

- workflow or generated-surface errors;
- financial-data, period, unit, source, or calculation errors;
- installation, update, doctor, or uninstall failures;
- distinct workflow proposals with testable output contracts.

Read [`SUPPORT.md`](SUPPORT.md) before opening an issue. Do not post credentials, private paths, confidential documents, unpublished holdings, or requests for personalized investment advice. Potential vulnerabilities must follow [`SECURITY.md`](SECURITY.md).

## Usage examples

Claude Code commands:

```text
/investment-research Tencent
/investment-team NVIDIA
/earnings-review Apple 2026Q2
/industry-funnel AI infrastructure
/era-alpha AI data-center power and cooling
/investment-checklist Microsoft, Alphabet, Amazon
/portfolio-review Apple 30%, Microsoft 25%, Cash 20%
/news-pulse Tesla
```

Codex skill requests:

```text
Use investment-research to research Tencent.
Use earnings-review to analyze Apple's latest quarterly results.
Use industry-funnel to screen AI infrastructure companies.
Use era-alpha to identify and validate the strongest alpha candidates in a secular growth theme.
Use thesis-drift to compare two investment thesis reports.
Use investment-memo-craft to restructure the completed report for decision use.
```

## Repository architecture

```text
skills/*.md                 21 canonical shared workflow sources
codex-skills/*/SKILL.md     21 generated shared packages + 1 Codex-only package
codex-prompts/*.md          21 optional generated Codex prompts
scripts/                    Synchronization, installation management, and quality scripts
tools/                      Financial validation utilities, including terminal-value audit tooling
reports/                    Verified examples plus historical and upstream research output
docs/                       Maintainer, release, launch, and usage documentation
```

Canonical shared workflows should be edited in `skills/*.md` first. Their generated Codex files must then be synchronized using the repository scripts rather than edited independently. A clearly marked Codex-only package may be maintained directly when no same-named canonical source exists.

## Validation

Before submitting a workflow or tooling change, run:

```bash
python3 scripts/repository_quality.py
python3 scripts/sync-codex-skills.py --check
python3 scripts/sync-codex-prompts.py --check
python3 -m compileall -q scripts tools tests
python3 -m unittest discover -s tests -v
```

The permanent GitHub Actions workflow additionally checks:

- repository links, maintained identity, private paths, high-confidence secrets, and operational-language drift;
- deterministic financial, audit, Taiwan-data, verified-example, installer-safety, and community-template tests;
- unified install, update, doctor, uninstall, and backward-compatible alias lifecycles;
- 21 canonical shared workflows;
- 21 matching generated Codex skills and 21 prompts;
- exactly one declared Codex-only skill, `investment-memo-craft`;
- clean installation of 21 Claude commands, 22 Codex skills, and 21 Codex prompts;
- Unix-like installation on Ubuntu and macOS;
- Windows `.bat` installation.

## Financial rigor

The repository includes `tools/financial_rigor.py` for exact-decimal calculations and validation tasks such as:

- Market-cap verification.
- Valuation-ratio verification.
- Multi-source value comparison.
- Bull, base, and bear scenario calculations.
- Benford's Law checks.

For long-horizon analysis, `tools/terminal_value.py` adds terminal-value and IRR calculations plus publication gates for currency consistency, `r - g` denominator width, and separation of discrete risks from the discount rate.

AI output can contain factual, mathematical, sourcing, or interpretation errors. Always verify primary documents, currencies, share counts, units, dates, and calculations before making a financial decision.

## Historical reports and performance material

Historical reports and portfolio-performance screenshots are retained as source material from the original project. They are not presented as results produced, owned, or independently audited by the maintainer of this English edition.

Past performance does not guarantee future results. Nothing in this repository constitutes investment advice.

## Contributing

Read [SUPPORT.md](SUPPORT.md) before opening an issue and [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request. Contributions should preserve command names, paths, variables, output contracts, financial terminology, and source/generated consistency.

See [`CHANGELOG.md`](CHANGELOG.md), [`docs/ENGLISH_EDITION.md`](docs/ENGLISH_EDITION.md), and the [v1.1.0 release notes](docs/releases/v1.1.0.md) for edition history and release details.
