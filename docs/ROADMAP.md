# AI Value Investing Agents Roadmap

## P0 — Near term (1–2 months)

### A-share data-source integration
- Integrate free data sources such as AkShare and Eastmoney.
- Cover A-share financial statements, market data, and trading-activity datasets.
- Keep the existing skill interfaces stable while extending the data layer.

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
