# Tooling and Language Policy

AI Value Investing Agents is maintained as an **English-first** repository. The canonical user-facing workflows, installation documentation, contribution surfaces, and maintained English documentation are written in English.

The repository also preserves research artifacts and market-specific adapters inherited from the upstream project. Those files may legitimately contain Chinese or other local-language text when the language is part of the underlying market data, company names, source labels, or historical research record.

## Canonical maintained surfaces

The following areas are expected to remain English-first:

- `README.md`
- `AGENTS.md`, `CLAUDE.md`, `CONTRIBUTING.md`, `SECURITY.md`, `SUPPORT.md`
- `.github/`
- `docs/` except explicitly localized compatibility documents
- `scripts/`
- `skills/`
- `codex-skills/`
- `codex-prompts/`
- public CLI documentation and newly added generic tooling

## Historical and localized surfaces

The following areas may preserve original-language material when changing it would reduce fidelity or make upstream synchronization unnecessarily expensive:

- `reports/` historical research archive
- `README_ZH.md` and `README_JA.md`
- market-specific datasets
- company and security names in local scripts or fixtures
- source labels whose exact language is required for parsing or source matching
- localized market adapters such as A-share, Taiwan-stock, or Xueqiu integrations

Preserving these materials does **not** make them canonical product documentation.

## Tool categories

### Core generic tools

These support the maintained framework directly and should expose English-facing interfaces over time:

- `financial_rigor.py`
- `report_audit.py`
- `terminal_value.py`
- `stock_screener.py`
- `morningstar_fair_value.py`
- `momentum_backtest.py`
- `momentum_backtest_v2.py`
- `star_history_chart.py`
- `log-command.sh`

### Local-market adapters

These may retain local-language identifiers or parsing strings where required by their data sources:

- `ashare_data.py`
- `twstock_data.py`
- `xueqiu_scraper.py`

The standard for these adapters is not "zero CJK characters." The standard is that an English-speaking maintainer can understand how to invoke, validate, and safely modify the adapter without translating the historical research corpus.

## Upstream synchronization rule

When upstream adds new content:

1. Import historical reports and source data without mechanically translating them.
2. Translate or adapt any new canonical workflow before exposing it as maintained functionality.
3. Keep generated Codex artifacts synchronized with canonical `skills/` sources.
4. Do not import upstream user-memory, personal preference, or private-context files into this maintained fork.
5. Prefer a single canonical English document over duplicated English copies that can drift.

This policy keeps the fork operationally English-first while preserving the research value and provenance of the upstream archive.
