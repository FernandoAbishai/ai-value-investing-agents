# Verification Register for English Example Reports

> **Register cutoff:** 2026-08-02  
> **Scope:** Three reports under `reports/examples/`  
> **Method:** Primary-source transcription, formula recomputation, definition review, and deterministic audit fixtures

## Source register

| ID | Source | Type | Period or publication date | Used for |
|---|---|---|---|---|
| MSFT-IR | Microsoft FY2026 Q4 earnings release and financial statements | Primary company source | Quarter and year ended 2026-06-30; published 2026-07-29 | Microsoft income statement, balance sheet, cash flow, segments, cloud growth, RPO, shareholder returns |
| MSFT-METRICS | Microsoft FY2026 Q4 metrics | Primary company source | FY2026 Q4 | Product, cloud, and operating metrics |
| MSFT-SEC | Microsoft SEC filings index / FY2026 Form 10-K access | Primary filing index | FY2026 | Filing availability and document hierarchy |
| MSFT-REUTERS | Reuters post-earnings market report | Secondary market source | 2026-07-30 | Approximate $3.35T market capitalization and market reaction only |
| AMZN-IR | Amazon Q1 2026 earnings release | Primary company source | Quarter ended 2026-03-31 | AWS sales, AWS operating income, TTM operating cash flow, TTM free cash flow |
| GOOGL-IR | Alphabet 2025 Q4 earnings call | Primary company source | 2025 Q4, reported 2026-02 | Google Cloud revenue, operating income, margin, backlog, expected 2026 capex |
| ORCL-IR | Oracle FY2026 Q4 earnings release | Primary company source | Quarter and year ended 2026-05-31 | Oracle cloud and OCI revenue, RPO, operating cash flow, free cash flow |

## Source URLs

- MSFT-IR: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/press-release-webcast
- MSFT-METRICS: https://www.microsoft.com/en-us/investor/earnings/fy-2026-q4/metrics
- MSFT-SEC: https://www.microsoft.com/en-us/investor/sec-filings
- MSFT-REUTERS: https://www.reuters.com/business/microsoft-set-record-one-day-market-cap-gain-after-upbeat-azure-forecast-2026-07-30/
- AMZN-IR: https://ir.aboutamazon.com/news-release/news-release-details/2026/Amazon-com-Announces-First-Quarter-Results/
- GOOGL-IR: https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx
- ORCL-IR: https://investor.oracle.com/investor-news/news-details/2026/Oracle-Announces-Record-Q4-and-FY-2026-Results-Driven-by-Cloud-Infrastructure--Cloud-Applications/

## Recomputed Microsoft FY2026 figures

All values below use USD billions unless stated otherwise.

| Derived metric | Formula | Result used in reports |
|---|---|---:|
| Revenue growth | `331.839 / 281.724 - 1` | 17.79% |
| FY2026 operating margin | `155.237 / 331.839` | 46.78% |
| FY2025 operating margin | `128.528 / 281.724` | 45.62% |
| GAAP net margin | `133.749 / 331.839` | 40.31% |
| Adjusted net margin | `128.786 / 331.839` | 38.81% |
| FY2026 simple FCF | `182.935 - 115.948` | $66.987B |
| FY2025 simple FCF | `136.162 - 64.551` | $71.611B |
| Simple FCF change | `66.987 / 71.611 - 1` | -6.46% |
| Property additions / revenue | `115.948 / 331.839` | 34.94% |
| Productivity and Business Processes margin | `83.879 / 139.996` | 59.92% |
| Intelligent Cloud margin | `56.972 / 137.791` | 41.35% |
| More Personal Computing margin | `14.386 / 54.052` | 26.62% |
| Net cash | `76.843 - 9.227 - 31.067` | $36.549B |

## Recomputed Microsoft Q4 figures

| Derived metric | Formula | Result used in reports |
|---|---|---:|
| Revenue growth | `90.007 / 76.441 - 1` | 17.75% |
| Operating margin | `40.603 / 90.007` | 45.11% |
| Prior-year operating margin | `34.323 / 76.441` | 44.90% |
| Q4 simple FCF | `55.441 - 35.802` | $19.639B |
| Prior-year Q4 simple FCF | `42.647 - 17.079` | $25.568B |
| Simple FCF change | `19.639 / 25.568 - 1` | -23.19% |
| Property-additions growth | `35.802 / 17.079 - 1` | 109.63% |
| Property additions / revenue | `35.802 / 90.007` | 39.78% |
| Q4 Productivity and Business Processes margin | `21.900 / 37.847` | 57.86% |
| Q4 Intelligent Cloud margin | `15.955 / 39.306` | 40.59% |
| Q4 More Personal Computing margin | `2.748 / 12.854` | 21.38% |

## Approximate Microsoft valuation calculations

The $3.35 trillion equity value is a rounded secondary market figure reported after earnings and is time-sensitive.

| Approximate metric | Formula | Result |
|---|---|---:|
| Price / GAAP net income | `3350 / 133.749` | 25.05× |
| Price / adjusted net income | `3350 / 128.786` | 26.01× |
| Price / simple FCF | `3350 / 66.987` | 50.01× |
| Price / revenue | `3350 / 331.839` | 10.10× |
| Implied price per outstanding share | `3350 / 7.427` | $451.06 |
| Simple FCF per outstanding share | `66.987 / 7.427` | $9.02 |

## Scenario recomputation

The company-research scenario table starts with FY2026 adjusted EPS of $17.28 and an approximate inferred price of $451.06.

| Scenario | Formula | Year-three EPS | Indicated price |
|---|---|---:|---:|
| Bull | `17.28 × 1.18³`, then `× 30` | $28.39 | $851.75 |
| Base | `17.28 × 1.12³`, then `× 25` | $24.28 | $606.93 |
| Bear | `17.28 × 1.06³`, then `× 20` | $20.58 | $411.62 |

Scenarios are assumption maps, not sourced forecasts.

## Cloud comparison calculations

| Metric | Formula | Result |
|---|---|---:|
| AWS Q1 2026 segment operating margin | `14.2 / 37.6` | 37.77% |
| Microsoft Intelligent Cloud Q4 margin | `15.955 / 39.306` | 40.59% |
| Google Cloud Q4 margin | Company-reported | 30.1% |

Oracle did not disclose a standalone OCI operating margin in the cited release. No estimate was inserted.

## Definition controls

The following disclosures are deliberately not treated as interchangeable:

- Microsoft Cloud revenue;
- Azure and other cloud services growth;
- Microsoft Intelligent Cloud segment revenue;
- AWS segment revenue;
- Google Cloud segment revenue;
- Oracle total cloud revenue;
- Oracle OCI IaaS revenue;
- Microsoft commercial RPO;
- Oracle total RPO;
- Google Cloud backlog.

## Executable audit fixtures

The directory [`audit/`](audit/) contains selected point checks for each report. `tests/test_example_reports.py` loads those fixtures and calls `tools/report_audit.py`. CI requires every fixture to receive a `PASS` verdict.

The fixture comparison values are transcriptions or formula recomputations, not independent third-party audits. They make the checking process explicit and regression-testable.

## Verification limitations

- Source documents can later be amended or superseded.
- The Microsoft earnings-release financial statements were labeled unaudited at publication.
- Market capitalization changes continuously.
- Company-defined cloud and free-cash-flow measures differ.
- Analytical judgments about moat, risk, or capital returns cannot be “verified” like arithmetic.

## Disclaimer

This register supports educational research examples. It is not an accounting opinion, investment recommendation, or guarantee of completeness.
