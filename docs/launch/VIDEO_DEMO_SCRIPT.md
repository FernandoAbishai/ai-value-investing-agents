# Video Demonstration Script

## Production target

- **Length:** 6–8 minutes
- **Format:** screen recording with voice-over
- **Primary audience:** developers, investors, researchers, and AI-agent users
- **Demonstration artifact:** [`reports/examples/microsoft-fy2026-q4-earnings-review-20260802.md`](../../reports/examples/microsoft-fy2026-q4-earnings-review-20260802.md)
- **Research cutoff shown on screen:** 2026-08-02
- **Core message:** AI investment research becomes more useful when evidence, calculations, decision gates, and audits are explicit.

Do not present the example as a current recommendation. The report is a point-in-time demonstration built from a closed reporting period.

## Recording checklist

Before recording:

1. Pull the current `main` branch.
2. Run `python3 scripts/repository_quality.py`.
3. Run `python3 -m unittest discover -s tests -v`.
4. Use a clean temporary installation directory or a dedicated demo profile.
5. Hide browser bookmarks, notifications, local usernames, tokens, private repositories, and unrelated files.
6. Confirm that every displayed URL is public.
7. Set the terminal font large enough for a 1080p recording.
8. Disable autocomplete or shell history suggestions that could expose private commands.

## Suggested title

**I Built Auditable AI Value-Investing Workflows for Claude Code and Codex**

Alternative technical title:

**AI Value Investing Agents: From Prompt to Verified Research Workflow**

## Thumbnail text

Use no more than four words:

```text
AUDITABLE AI RESEARCH
```

## Chapter 1 — The problem (0:00–0:45)

### Screen

Open the repository README and show the release-status table.

### Voice-over

> General AI prompts can produce fluent investment commentary without a dependable research process. They may mix reporting periods, use stale prices, hide uncertainty, or present a calculation without showing the inputs. AI Value Investing Agents turns that open-ended prompt into explicit workflows for Claude Code and OpenAI Codex.

> This demonstration is not about asking an AI which stock to buy. It is about building a repeatable process that can be inspected, tested, and audited.

### On-screen emphasis

Highlight:

- 20 shared workflows;
- verified English examples;
- cross-platform validation;
- research and audit tools.

## Chapter 2 — Install and diagnose (0:45–1:45)

### Screen

Open a terminal in the repository and use temporary destinations:

```bash
export CLAUDE_COMMANDS_DIR="$(mktemp -d)/claude/commands"
export CODEX_HOME="$(mktemp -d)/codex"
export AIVA_STATE_HOME="$(mktemp -d)/state"
./scripts/install.sh --all --dry-run
./scripts/install.sh --all
./scripts/manage.sh doctor --all
```

On Windows, use equivalent temporary folders and `scripts\install.bat` / `scripts\manage.bat`.

### Voice-over

> The unified manager supports dry runs, backups, an external manifest, drift detection, updates, diagnostics, and safe uninstall. It verifies generated Codex artifacts before installation and does not download remote code or run Git operations.

> The doctor command checks the source inventory, installed hashes, manifest, Python version, and synchronization state.

### Privacy note

Do not show your real home-directory path. Keep the demo inside temporary directories.

## Chapter 3 — The workflow contract (1:45–2:45)

### Screen

Open [`skills/earnings-review.md`](../../skills/earnings-review.md). Scroll through:

- current-date confirmation;
- primary-source requirements;
- period comparison;
- adjustment handling;
- cash-flow and capital-intensity review;
- red, yellow, and green signals;
- output and audit requirements.

Then open the generated Codex package and show that it derives from the same canonical workflow.

### Voice-over

> The Markdown workflow is the contract. It defines the inputs, evidence hierarchy, calculations, decision gates, report path, and release conditions. Claude Code uses the canonical workflow directly. Codex packages and optional prompts are generated from that same source so the environments do not silently drift.

## Chapter 4 — Verified earnings example (2:45–4:45)

### Screen

Open the Microsoft FY2026 Q4 earnings-review example. Show its metadata first:

- verified-example status;
- research cutoff;
- primary reporting period;
- workflow demonstrated;
- audit status.

Then show:

1. the headline-results table;
2. GAAP versus adjusted results;
3. the segment table;
4. the cash-conversion bridge;
5. the signal dashboard;
6. the next-period checklist.

### Voice-over

> This report separates the operational result from cash conversion. Revenue and operating income grew strongly, Azure accelerated, and backlog expanded. At the same time, property-and-equipment additions more than doubled and simple free cash flow declined.

> The workflow does not average those facts into a vague score. It states that demand and execution were green, cash conversion was yellow, and future red triggers depend on the relationship between cloud growth, utilization, margins, and infrastructure spending.

> The report also keeps GAAP results separate from investment-related adjustments instead of treating every adjusted number as automatically superior.

## Chapter 5 — Reproduce a calculation (4:45–5:35)

### Screen

Run an exact calculation using values from the report:

```bash
python3 tools/financial_rigor.py exact-calc --expr "55.441 - 35.802"
```

Then show the corresponding line in [`reports/examples/VERIFICATION.md`](../../reports/examples/VERIFICATION.md).

### Voice-over

> Decision-sensitive arithmetic is reproduced with repository tools. Here, quarterly operating cash flow minus property-and-equipment additions equals 19.639 billion dollars of simple free cash flow. The verification register preserves the formula and source inputs.

> Simple free cash flow is explicitly labeled as a mechanical measure. It does not pretend to know how much investment is maintenance versus growth capital.

## Chapter 6 — Audit before publication (5:35–6:35)

### Screen

Show the audit fixture:

[`reports/examples/audit/microsoft-fy2026-q4-earnings-review.json`](../../reports/examples/audit/microsoft-fy2026-q4-earnings-review.json)

Then run the example-report test:

```bash
python3 -m unittest tests.test_example_reports -v
```

Optionally run the complete suite:

```bash
python3 -m unittest discover -s tests -v
```

### Voice-over

> A report is not publication-ready merely because it looks polished. Selected material figures are registered with their source or exact recomputation, and CI requires every fixture to receive a passing audit verdict.

> The test also requires a visible cutoff, workflow name, limitations, disclaimer, and definition controls. If a value is missing or unverified, the auditor cannot silently approve it.

## Chapter 7 — Definition-aware comparison (6:35–7:15)

### Screen

Open [`reports/examples/cloud-infrastructure-comparison-20260802.md`](../../reports/examples/cloud-infrastructure-comparison-20260802.md) and show the paragraph beginning “No honest single revenue ranking”.

### Voice-over

> The comparison example refuses to rank incompatible cloud disclosures as if they were the same metric. Microsoft Cloud, Azure growth, AWS segment revenue, Google Cloud, and Oracle OCI use different definitions and periods. Preserving those differences is part of research quality, not a limitation to hide.

## Chapter 8 — Close and call to action (7:15–7:50)

### Screen

Return to the README and then show the structured issue forms.

### Voice-over

> AI Value Investing Agents is open source and supports Claude Code and OpenAI Codex. The repository includes 20 shared workflows, deterministic financial and audit tests, verified examples, and safe cross-platform installation management.

> Feedback is most useful when it is reproducible. The issue forms separate workflow errors, financial-data problems, installation failures, and workflow proposals. The project is for research and education, not personalized investment advice.

### Final card

```text
AI Value Investing Agents
20 shared workflows · verified examples · cross-platform CI
github.com/FernandoAbishai/ai-value-investing-agents
```

## Description template

```text
AI Value Investing Agents is an English-first, multi-agent value-investing research framework for Claude Code and OpenAI Codex.

This video demonstrates:
- safe cross-platform installation and diagnostics;
- a canonical earnings-review workflow;
- a point-in-time verified Microsoft FY2026 Q4 example;
- exact financial calculations;
- executable report-audit fixtures;
- definition-aware cloud comparison.

Repository:
https://github.com/FernandoAbishai/ai-value-investing-agents

Release:
https://github.com/FernandoAbishai/ai-value-investing-agents/releases/tag/v1.0.0

Verified examples:
https://github.com/FernandoAbishai/ai-value-investing-agents/tree/main/reports/examples

Educational and research use only. Nothing in the video or repository is personalized investment, legal, accounting, or tax advice. The example evidence is limited to its stated research cutoff.
```

## Pinned-comment template

```text
Which part should be improved first: workflow coverage, financial validation, installation, or report auditing?

Please use the repository's structured issue forms for reproducible bugs and data errors. Do not post credentials, private paths, confidential material, or personal portfolio information.
```

## Editing rules

- Keep the pace measured; do not speed through tables that viewers need to inspect.
- Zoom into the exact row being discussed.
- Use callouts for “primary source”, “derived calculation”, “analytical judgment”, and “limitation”.
- Do not add animated stock-price arrows, return claims, or sensational buy/sell language.
- Do not imply endorsement from Microsoft, Anthropic, OpenAI, Warren Buffett, Charlie Munger, Li Lu, Duan Yongping, or the original project maintainer.
- Preserve source titles and the stated cutoff in screenshots.
