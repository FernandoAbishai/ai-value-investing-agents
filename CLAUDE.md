# AI Value Investing Agents — Claude Code Guide

## Project Overview

AI Value Investing Agents is an English-first, multi-agent value-investing research framework for Claude Code and OpenAI Codex.

- Repository: `FernandoAbishai/ai-value-investing-agents`
- Maintained edition: AI Value Investing Agents
- Framework lineage: [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)
- Example checkout path: `~/ai-value-investing-agents`

The repository preserves historical reports and methodology from the original project while maintaining one English canonical workflow source for both supported agent environments.

## Repository Structure

```text
skills/                       Canonical workflow definitions
codex-skills/*/SKILL.md       Generated Codex skill packages
codex-prompts/*.md            Generated optional Codex prompts
scripts/                      Synchronization, quality, and installation-management scripts
tools/                        Financial, report-validation, and report-index utilities
reports/                      Historical and newly generated research plus generated indexes
assets/                       Images and other report assets
docs/                         Edition, release, upstream-review, and usage documentation
```

## Canonical Workflow Rule

`skills/*.md` is the source of truth. After editing a workflow, run:

```bash
python3 scripts/sync-codex-skills.py
python3 scripts/sync-codex-prompts.py
python3 scripts/sync-codex-skills.py --check
python3 scripts/sync-codex-prompts.py --check
```

Do not edit generated Codex files independently. Preserve command names, `$ARGUMENTS`, paths, calculations, audit gates, scoring systems, and output contracts.

## Research Principles

These rules have priority across every workflow:

1. **Evidence before conclusion.** Start with data and source quality, then reason, then conclude.
2. **No predetermined bullish or bearish stance.** Include the strongest counterargument for every material thesis.
3. **Separate fact from interpretation.** Mark verified facts, estimates, assumptions, scenarios, and analytical judgments.
4. **Confirm the current date.** Run `date` before using current prices, filings, company roles, laws, product information, or recent news. State the cutoff date.
5. **Use primary sources first.** Prefer filings, annual and interim reports, official announcements, exchange data, earnings material, and original papers.
6. **Cross-check critical numbers.** Use at least two independent sources when the workflow requires verification.
7. **Use exact arithmetic.** Run `python3 tools/financial_rigor.py ...` for valuation, market capitalization, percentages, and scenarios.
8. **Audit publishable research.** Run `python3 tools/report_audit.py ...` for financially material public reports.
9. **Be explicit about missing data.** Never fill gaps with invented precision.
10. **Do not impersonate real investors.** Clearly distinguish verified quotations, paraphrases, and framework-based interpretations.

## Report Language and Style

English is the canonical workflow language, but reports should follow the user's requested language.

Use a direct, analytical style. Avoid promotional certainty, unsupported superlatives, generic AI filler, and famous-investor name-dropping as evidence. Keep technical terms, source titles, code, paths, variables, and ticker symbols in their accurate original form where necessary.

## Report Paths

Use filesystem-safe names and the path defined by each workflow. Common patterns include:

| Workflow | Typical output |
|---|---|
| `investment-research` | `reports/{company}/{company}-research-{YYYYMMDD}.md` |
| `investment-team` | `reports/{company}/` with role reports and a synthesis |
| `investment-checklist` | `reports/{company}/{company}-checklist-{YYYYMMDD}.md` |
| `earnings-review` | `reports/{company}/{company}-earnings-{period}.md` |
| `private-company-research` | `reports/{company}/{company}-private-{YYYYMMDD}.md` |
| `management-deep-dive` | `reports/{company}/{company}-management-{YYYYMMDD}.md` |
| `industry-research` | `reports/{industry}-industry-{YYYYMMDD}.md` |
| `industry-funnel` | `reports/{industry}-funnel-{YYYYMMDD}.md` |
| `thesis-tracker` | `reports/{company}-thesis.md` or the workflow-defined company directory |
| `portfolio-review` | `reports/portfolio-latest.md` |

When an existing report structure differs, preserve it unless the task specifically requests migration.

## Report Index Publication

`reports/README.md` and `reports/index.json` are generated surfaces. Do not edit them manually.

When publishing a new tracked report or changing report classification metadata:

```bash
git add <report files>
python3 tools/reports_index.py
python3 tools/reports_index.py --check
git add reports/README.md reports/index.json
```

Important publication boundaries:

- The generator only indexes report contents represented in Git's index.
- Untracked files, ignored files, and `git add -N` intent-to-add placeholders must remain excluded.
- If Git index state cannot be read, generation must fail closed rather than publish local-only paths.
- Run index generation from a full-history checkout so Git-derived dates are deterministic.
- Keep fork-specific taxonomy changes in `reports/_index/config.json`; do not copy upstream classifications blindly.
- `reports/examples/VERIFICATION.md` is a verification register, not a research report, and must stay excluded from the inventory.

The permanent `Report Index` GitHub Actions workflow runs the read-only `--check` gate on pull requests and `main` pushes. A stale generated index is a release blocker.

## Local Installation Management

Use the unified manager rather than copying installed files manually:

```bash
./scripts/install.sh --all
./scripts/manage.sh update --all
./scripts/manage.sh doctor --all
./scripts/manage.sh uninstall --all
```

Windows uses `scripts\install.bat` and `scripts\manage.bat`. Preserve backups, manifests, `--dry-run`, component targeting, and modified-file deletion safeguards when changing installer behavior. Existing component-specific scripts are compatibility aliases and must remain tested.

## Git and Repository Operations

Use the actual checkout path rather than assuming a specific home directory.

```bash
git status
git pull --rebase origin main
# edit and validate
git add <scoped files>
git commit -m "describe the scoped change"
git push
```

Do not push intermediate research scratch files unless requested. Do not overwrite historical reports or mix a new series into an existing series directory; use a dated directory when the workflow specifies conflict handling.

## Privacy and Publication Safety

Public files must not include:

- API keys, tokens, credentials, or private URLs;
- local usernames or machine-specific paths;
- private messages, internal company information, or unpublished holdings;
- personal identity details unrelated to attribution;
- copyrighted images without a valid use basis and attribution.

Before publishing, scan changed report and documentation files for private paths or identifiers and review all image rights, quotations, and source links.

## Validation Before Completion

Run the checks relevant to the change:

```bash
python3 -m compileall scripts tools tests
python3 scripts/repository_quality.py
python3 scripts/sync-codex-skills.py --check
python3 scripts/sync-codex-prompts.py --check
python3 -m unittest discover -s tests -v
```

For changes that add, remove, rename, or reclassify tracked reports, also run from a full-history checkout:

```bash
python3 tools/reports_index.py --check
```

Installation behavior is validated by `.github/workflows/validate.yml` on Unix-like runners and Windows. Report-index freshness is validated by the dedicated full-history workflow. A failing validation means the change is not release-ready.
