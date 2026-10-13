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
| 1 — Local retrieval | **Tencent + Eastmoney** | Stock code such as `600519` | `tools/market_data.py --market cn` |
| 2 — Independent check | **CNInfo** | `cninfo.com.cn` | Original annual and quarterly reports |

**A-share retrieval commands**:

```bash
python3 tools/market_data.py quote 600519 --market cn
python3 tools/market_data.py valuation 600519 --market cn
python3 tools/market_data.py financials 600519 --market cn
python3 tools/market_data.py search Kweichow --market cn
```

Special rules for A-shares:

1. Currency is CNY. Explicitly label it in cross-market work.
2. The local adapter routes quote data through Tencent and financial/search data through Eastmoney. Treat that adapter output as one retrieval path, not as two independent confirmations.
3. Cross-check material figures against CNInfo or the original issuer filing before treating them as verified.
4. `tools/ashare_data.py` remains a backward-compatible direct adapter, but maintained workflows should prefer `tools/market_data.py`.

### Taiwan Stocks

| Priority | Source | URL / identifier | Access method |
|---|---|---|---|
| 1 — Local retrieval | **FinMind API** | `api.finmindtrade.com` | `tools/market_data.py --market tw` |
| 2 — Secondary | **Goodinfo** | `goodinfo.tw/tw/StockDetail.asp?STOCK_ID={code}` | Direct access |
| Primary filing | MOPS | `mops.twse.com.tw` | Original filings and monthly revenue disclosures |

**Taiwan retrieval commands**:

```bash
python3 tools/market_data.py quote 2330 --market tw
python3 tools/market_data.py valuation 2330 --market tw
python3 tools/market_data.py financials 2330 --market tw
python3 tools/market_data.py revenue 2330 --market tw
python3 tools/market_data.py dividend 2330 --market tw
python3 tools/market_data.py search TSMC --market tw
```

Special rules for Taiwan stocks:

1. Currency is TWD. Explicitly label currency and convert consistently before cross-market comparisons.
2. Monthly revenue is a valuable early signal because listed companies disclose it every month. Use the `revenue` command in earnings and thesis-monitoring workflows.
3. FinMind income-statement values are quarterly. The adapter aggregates them into annual values and labels incomplete years.
4. API tokens must remain local. Read them from `FINMIND_TOKEN` or `local/finmind_token.txt`. Never place tokens in reports, skills, or commits.
5. Cross-check FinMind against Goodinfo or an ADR source. For TSMC, remember that one TSM ADR represents five shares of 2330.
6. `tools/twstock_data.py` remains a backward-compatible direct adapter, but maintained workflows should prefer `tools/market_data.py`.

### Unified Local-Market Interface

Use `tools/market_data.py` as the maintained entry point for installed local-market adapters:

```bash
python3 tools/market_data.py capabilities
python3 tools/market_data.py capabilities --format json
```

The current registry exposes Mainland China A-shares (`cn-a`) and Taiwan (`tw`) with aliases such as `cn`, `a-share`, `taiwan`, `twse`, and `tpex`. Text mode preserves each existing adapter's human-readable output. `--format json` wraps the same result in a stable envelope containing market, currency, command, adapter, and source metadata.

The JSON envelope standardizes invocation and provenance metadata; it **does not** turn one adapter into multiple independent sources. Continue applying the two-source validation rule below.

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
| Sanqi Interactive Entertainment | `tools/market_data.py financials 002555 --market cn` | CNInfo |
| G-Bits | `tools/market_data.py financials 603444 --market cn` | CNInfo |
| Nintendo | Macrotrends NTDOY | StockAnalysis NTDOY |
| Capcom | Macrotrends CCOEY | StockAnalysis CCOEY |
| TSMC | `tools/market_data.py financials 2330 --market tw` | Goodinfo / Macrotrends TSM |
| MediaTek | `tools/market_data.py financials 2454 --market tw` | Goodinfo |
