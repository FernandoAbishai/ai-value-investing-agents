# AI Value Investing Agents — Codex Guide

This repository contains English-first investment-research workflows, generated Codex skill packages, compatibility prompts, validation tools, and historical research material. Preserve compatibility between Claude Code and OpenAI Codex.

## Project Identity

- Repository: `FernandoAbishai/ai-value-investing-agents`
- Checkout directory used in examples: `~/ai-value-investing-agents`
- Maintained edition: AI Value Investing Agents
- Framework lineage: [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

Do not reintroduce the old repository name or checkout path into active installation, tooling, or generated-workflow instructions. Historical reports may retain original names when required for accurate attribution.

## Project Layout

- `skills/*.md`: canonical workflow sources used by Claude Code and as the source for generated Codex artifacts.
- `codex-skills/*/SKILL.md`: generated Codex skill packages.
- `codex-prompts/*.md`: generated optional slash-command prompts for Codex.
- `scripts/manage.py`: unified install, update, doctor, and uninstall manager.
- `scripts/`: compatibility wrappers, synchronization, quality, and release scripts.
- `tools/`: exact-arithmetic, financial-data, and report-audit utilities.
- `reports/`: historical and newly generated research output.
- `docs/`: edition, release, and usage documentation.
- `CLAUDE.md`: Claude Code repository guidance.
- `AGENTS.md`: Codex repository guidance.

## Source and Generation Rules

1. Treat `skills/*.md` as the canonical source for shared workflows.
2. After changing a canonical workflow, run:

   ```bash
   python3 scripts/sync-codex-skills.py
   python3 scripts/sync-codex-prompts.py
   ```

3. Verify that generated artifacts are current:

   ```bash
   python3 scripts/sync-codex-skills.py --check
   python3 scripts/sync-codex-prompts.py --check
   ```

4. Do not edit a generated `codex-skills/*/SKILL.md` or `codex-prompts/*.md` file independently of its canonical source.
5. Preserve `$ARGUMENTS`, command names, tool paths, report paths, code blocks, scoring rules, audit gates, and output contracts.
6. Codex-only packages are allowed only when clearly identified and when no same-named canonical workflow exists.

## Research Quality Rules

- Confirm the current date before researching prices, market capitalization, filings, laws, products, management roles, or recent events. State the research cutoff date in the report.
- Prefer primary sources: regulatory filings, annual and interim reports, earnings releases, official exchange data, company announcements, and original papers.
- Cross-check decision-critical financial data with at least two independent sources when the workflow requires it.
- Label facts, estimates, assumptions, analytical judgments, uncertainty, and unavailable data separately.
- Use `python3 tools/financial_rigor.py ...` for market-cap, valuation, percentage, cross-source, and scenario calculations.
- Use `python3 tools/report_audit.py ...` before treating financially material research as publication-ready.
- Do not turn framework-based simulations into authentic quotations or imply endorsement by real investors.
- This repository supports research and learning; it does not provide personalized investment, legal, accounting, or tax advice.

## Language and Output

- English is the canonical workflow language.
- Follow the user's requested report language when specified.
- Do not translate code, paths, variables, ticker symbols, command names, or source titles when doing so would reduce accuracy.
- Public-facing work must include source attribution, date context, and an appropriate limitation or investment-risk disclosure.

## Editing Rules

- Keep changes scoped to the requested workflow, tool, script, documentation, or report.
- Preserve unrelated historical reports.
- Do not include secrets, tokens, private messages, unpublished holdings, local usernames, or machine-specific paths in public files.
- Before committing public research, scan for private paths and identifiers.
- Run Python syntax checks for changed Python files and the relevant generator or installer checks for compatibility changes.
- Prefer permanent validation in `.github/workflows/validate.yml` over one-off manual assumptions.

## Installation Paths

Claude Code commands install to `${CLAUDE_COMMANDS_DIR:-$HOME/.claude/commands}`.

Codex skills and optional prompts install under `${CODEX_HOME:-$HOME/.codex}`.

Use `scripts/manage.py` or its shell and batch wrappers for installation changes. Preserve manifest ownership, collision backups, `--dry-run`, drift diagnostics, and refusal to delete modified entries without explicit force. Keep component-specific installers as compatible aliases.

Use the repository-root-relative commands documented in the README. Do not assume that the checkout is located in a particular user's home directory when running tools; locate the actual repository root first.
