# AI Value Investing Agents Roadmap

## Completed baseline — October 2026

### Unified local-market data layer
- Route maintained local-market workflows through `tools/market_data.py`.
- Register Mainland China A-share and Taiwan adapters behind stable market aliases and capability metadata.
- Preserve the existing direct adapter CLIs for backward compatibility.
- Provide a versioned JSON metadata envelope without weakening the independent-source validation standard.

## P0 — Near term (1–2 months)

### Structured market-data payloads
- Add normalized structured fields behind the unified adapter interface instead of relying only on legacy `result_text`.
- Normalize currency, fiscal period, units, source provenance, and missing-value semantics.
- Keep the existing text interface stable while structured consumers migrate incrementally.

## P1 — Medium term (3–6 months)

### HTML report output
- Add an HTML report format alongside Markdown.
- Support dark mode, navigation, and chart visualizations.
- Improve report distribution and reading experience.

### Multiple research-depth modes
- `lite`: approximately five-minute triage with a valuation range and key conclusion.
- `standard`: current default with complete multi-agent research.
- `deep`: additional cross-validation and historical analogues for institutional-level depth.

### Multi-stock comparison
- Compare 2–4 stocks across the same dimensions.
- Benchmark valuations within an industry.
- Produce a comparison matrix and an explicit preferred candidate.

## P2 — Long term (6+ months)

### Test coverage
- Expand unit tests for core tools such as `financial_rigor.py`.
- Add regression tests for skill outputs.
- Keep iteration from silently breaking existing behavior.

### Portfolio-level analysis
- Evaluate portfolio health.
- Analyze industry and geographic concentration.
- Detect correlation and concentration risk.
