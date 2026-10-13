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
- `reports_index.py`
- `market_data.py`
- `terminal_value.py`
- `stock_screener.py`
- `morningstar_fair_value.py`
- `momentum_backtest.py`
- `momentum_backtest_v2.py`
- `star_history_chart.py`
- `log-command.sh`

### Unified market-data entry point

`tools/market_data.py` is the maintained command surface for installed local-market adapters. It currently registers Mainland China A-shares and Taiwan stocks without changing the behavior of their existing direct tools.

Use:

```bash
python3 tools/market_data.py capabilities
python3 tools/market_data.py quote 600519 --market cn
python3 tools/market_data.py financials 2330 --market tw
python3 tools/market_data.py valuation 2330 --market taiwan --format json
```

The registry records each market's canonical key, aliases, currency, adapter module, supported commands, and source family. Text mode delegates directly to the legacy adapter so existing behavior is preserved. JSON mode adds a versioned metadata envelope around the adapter output for agent and automation use.

The wrapper is a routing and provenance boundary, not a substitute for independent source validation. If one adapter internally uses multiple endpoints from one retrieval path, workflows must still follow `skills/financial-data.md` and obtain an independent confirmation before treating material figures as verified.

### Local-market adapters

These may retain local-language identifiers or parsing strings where required by their data sources:

- `ashare_data.py`
- `twstock_data.py`
- `xueqiu_scraper.py`

The standard for these adapters is not "zero CJK characters." The standard is that an English-speaking maintainer can understand how to invoke, validate, and safely modify the adapter without translating the historical research corpus.

Direct adapter CLIs remain supported for backward compatibility. New maintained workflows should prefer `tools/market_data.py` when the requested market is registered there.

## Upstream synchronization rule

When upstream adds new content:

1. Import historical reports and source data without mechanically translating them.
2. Translate or adapt any new canonical workflow before exposing it as maintained functionality.
3. Keep generated Codex artifacts synchronized with canonical `skills/` sources.
4. Do not import upstream user-memory, personal preference, or private-context files into this maintained fork.
5. Prefer a single canonical English document over duplicated English copies that can drift.

This policy keeps the fork operationally English-first while preserving the research value and provenance of the upstream archive.
