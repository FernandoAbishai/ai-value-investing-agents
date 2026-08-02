---
name: financial-data
description: "AI Value Investing Agents skill: Financial Data Retrieval and Cross-Validation Standard. Source: skills/financial-data.md."
---

## Codex adapter note

This skill is generated from `skills/financial-data.md` so Claude Code and Codex users share one canonical workflow.

- Treat `$ARGUMENTS` as the user's request in the current Codex thread.
- When the source mentions Claude-only surfaces such as Task, Agent, WebSearch, Bash, Read, or Write, use the closest Codex capability available in this session: subagents when available, web search when needed, shell commands for local tools, and normal file edits for workspace files.
- Use shared project tools from `tools/` in this repository. Prefer running commands from the repository root with paths like `python3 tools/financial_rigor.py ...`; if the current thread starts outside the repo, locate the actual checkout path first instead of assuming a fixed home-directory path.
- Before starting research, run the `date` command to confirm today's date; treat it as the baseline for "latest" data and state the data cutoff date in the report header. Never assume the current date from training data.
- Preserve the research quality rules from `AGENTS.md`: cross-check financial data, use exact arithmetic tools for valuation/math, and clearly label uncertainty and source gaps.

# Financial Data Retrieval and Cross-Validation Standard

This standard applies to every research workflow involving company financial data. **Each material figure must come from two independent sources, and discrepancies greater than 1% must be flagged.**

---

## Source Priority

### U.S. Stocks

| Priority | Source | URL pattern | Access method |
|---|---|---|---|
| 1 — Primary | **Macrotrends** | `macrotrends.net/stocks/charts/{ticker}` | Direct access |
| 2 — Secondary | **StockAnalysis** | `stockanalysis.com/stocks/{ticker}/financials` | Direct access |
| Primary filing | SEC EDGAR | `sec.gov/cgi-bin/browse-edgar` | Original 10-K / 10-Q filings |

### Hong Kong Stocks

| Priority | Source | URL / identifier | Access method |
|---|---|---|---|
| 1 — Primary | **AAStocks** | Company fundamentals section | Direct access |
| 2 — Secondary | **Macrotrends ADR** | Example: TCEHY for Tencent, NTES for NetEase | Direct access |
| Primary filing | HKEXnews | `hkexnews.hk` | Original annual-report PDF |

### Mainland China A-Shares

| Priority | Source | URL / identifier | Access method |
|---|---|---|---|
| 1 — Primary | **Eastmoney** | Search by stock code and open financial statements | Direct access |
| 2 — Secondary | **CNInfo** | `cninfo.com.cn` | Original annual and quarterly reports |

### Taiwan Stocks

| Priority | Source | URL / identifier | Access method |
|---|---|---|---|
| 1 — Primary | **FinMind API** | `api.finmindtrade.com` | `tools/twstock_data.py` |
| 2 — Secondary | **Goodinfo** | `goodinfo.tw/tw/StockDetail.asp?STOCK_ID={code}` | Direct access |
| Primary filing | MOPS | `mops.twse.com.tw` | Original filings and monthly revenue disclosures |

**FinMind retrieval commands**:

```bash
python3 tools/twstock_data.py quote 2330
python3 tools/twstock_data.py valuation 2330
python3 tools/twstock_data.py financials 2330
python3 tools/twstock_data.py revenue 2330
python3 tools/twstock_data.py dividend 2330
python3 tools/twstock_data.py search 台積
```

Special rules for Taiwan stocks:

1. Currency is TWD. Explicitly label currency and convert consistently before cross-market comparisons.
2. Monthly revenue is a valuable early signal because listed companies disclose it every month. Use the `revenue` command in earnings and thesis-monitoring workflows.
3. FinMind income-statement values are quarterly. The tool aggregates them into annual values and labels incomplete years.
4. API tokens must remain local. Read them from `FINMIND_TOKEN` or `local/finmind_token.txt`. Never place tokens in reports, skills, or commits.
5. Cross-check FinMind against Goodinfo or an ADR source. For TSMC, remember that one TSM ADR represents five shares of 2330.

---

## Execution Standard

### Step 1: Retrieve Each Figure Twice

For every financial metric — revenue, net income, gross margin, operating cash flow, leverage, and similar figures — retrieve values independently from **source 1** and **source 2**.

### Step 2: Calculate and Classify the Difference

```text
Difference rate = |source 1 value - source 2 value| / |source 1 value| × 100%
```

| Difference | Required treatment |
|---|---|
| ≤ 1% | ✅ Consistent. Use the primary-source value and cite both sources. |
| >1% to 5% | ⚠️ Flag a discrepancy. Show both values and explain likely causes such as FX or accounting scope. |
| >5% | ❌ Material discrepancy. Check the original filing before using the number. |

### Step 3: Present the Evidence

Use this format for every material figure:

```text
Revenue: CNY 123.9 billion ✅
  - Macrotrends: CNY 124.1 billion
  - StockAnalysis: CNY 123.7 billion
  - Difference: 0.3%
```

Discrepancy example:

```text
Net income: CNY 24.5 billion ⚠️ Data discrepancy
  - Macrotrends: CNY 24.5 billion (GAAP)
  - StockAnalysis: CNY 27.8 billion (non-GAAP)
  - Difference: 13.5%
  - Explanation: different accounting definitions
```

---

## Common Causes of Differences

| Cause | Explanation |
|---|---|
| GAAP vs non-GAAP | Common for earnings and adjusted-profit figures |
| Currency conversion | Different exchange rates or conversion dates |
| Fiscal-year definition | Calendar year vs company fiscal year |
| Consolidation scope | Treatment of minority interests or unconsolidated entities |
| Update lag | One platform has not processed the latest filing |

---

## Special Rules

1. **Private companies**: when only one credible source exists, prefix the figure with `[estimate]` and do not claim successful cross-validation.
2. **Quarterly vs annual figures**: prefer annual figures for validation because quarterly datasets may update at different speeds.
3. **Original filings take priority**: when both aggregators disagree with the filing, use the filing and document the source error.

---

## Share Prices and Corporate-Action Adjustments

Historical price series can be presented on three bases. Mixing them can invalidate long-term return, historical price, and valuation-band analysis.

| Basis | Meaning | Appropriate use |
|---|---|---|
| Unadjusted | Actual traded price with gaps on ex-dividend or split dates | Current snapshot only |
| Forward-adjusted | Historical prices restated relative to the latest price | Historical price comparison, multi-year price change, and historical P/E bands |
| Back-adjusted / total-return basis | Series restated from listing and incorporating distributions | Historical total return and annualized return |

Rules:

1. Use **forward-adjusted prices** for historical price analysis, and never mix adjusted and unadjusted series in one comparison.
2. Current market capitalization and current P/E use the current actual price and current shares outstanding; adjustment is irrelevant to the current snapshot.
3. Restate historical per-share metrics across stock splits or large bonus issues before comparison.
4. Total-return calculations must include dividends.
5. After issuance or buybacks, verify market capitalization using the latest shares outstanding.

---

## Quick Reference

| Company / market | Primary source | Secondary source |
|---|---|---|
| PDD | Macrotrends PDD | StockAnalysis PDD |
| Tencent | AAStocks 0700.HK | Macrotrends TCEHY |
| NetEase | AAStocks 9999.HK | Macrotrends NTES |
| Sanqi Interactive Entertainment | Eastmoney 002555 | CNInfo |
| G-Bits | Eastmoney 603444 | CNInfo |
| Nintendo | Macrotrends NTDOY | StockAnalysis NTDOY |
| Capcom | Macrotrends CCOEY | StockAnalysis CCOEY |
| TSMC | `tools/twstock_data.py 2330` | Goodinfo / Macrotrends TSM |
| MediaTek | `tools/twstock_data.py 2454` | Goodinfo |
