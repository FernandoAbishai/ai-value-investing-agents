# End-to-End Quickstart Demonstration

This walkthrough verifies installation and runs one complete research workflow without relying on a prewritten report.

## Demonstration Goal

Use `investment-checklist` to compare Microsoft, Alphabet, and Amazon as possible candidates for deeper research.

The demonstration is intentionally a process example rather than a stored investment conclusion. Prices, filings, management roles, and valuation inputs change over time, so the workflow must retrieve current evidence when it runs.

## 1. Clone the Repository

```bash
git clone https://github.com/FernandoAbishai/ai-value-investing-agents.git
cd ai-value-investing-agents
```

## 2. Install for Claude Code

Unix-like systems:

```bash
./scripts/install-claude-commands.sh
```

Windows:

```bat
.\scripts\install-claude-commands.bat
```

Restart Claude Code after installation.

## 3. Install for OpenAI Codex

Unix-like systems:

```bash
./scripts/install-codex-skills.sh
./scripts/install-codex-prompts.sh
```

Windows:

```bat
.\scripts\install-codex-skills.bat
.\scripts\install-codex-prompts.bat
```

Restart Codex after installation.

Codex installs the 20 shared research workflows plus the hand-written Codex-only `investment-memo-craft` writing overlay. The optional prompt installer creates prompts only for the 20 canonical shared workflows.

## 4. Run the Same Workflow in Either Environment

Claude Code:

```text
/investment-checklist Microsoft, Alphabet, Amazon
```

Codex:

```text
Use investment-checklist to compare Microsoft, Alphabet, and Amazon as of today's confirmed date. Apply every source, valuation, and audit gate in the skill.
```

## 5. Expected Execution Sequence

A correct run should:

1. confirm the current date and state the research cutoff;
2. resolve company identities, tickers, exchanges, currencies, and reporting periods;
3. retrieve current primary financial material before using secondary summaries;
4. evaluate business quality, moat, management, financial quality, valuation, and principal risks;
5. distinguish verified facts from estimates, assumptions, and analytical judgments;
6. use `tools/financial_rigor.py` for decision-sensitive calculations;
7. preserve the strongest argument against each candidate;
8. apply the checklist's blocking gates instead of averaging away a serious failure;
9. save the report to the path defined by the canonical workflow;
10. run the report-audit process before describing the result as publication-ready.

## 6. Verify the Generated Report

Check that the report includes:

- a visible cutoff date;
- source titles and reporting periods;
- currencies and units for every material figure;
- explicit uncertainty where data could not be reconciled;
- a clear pass, fail, or deeper-research decision for each company;
- no invented quotation or implied endorsement from a real investor;
- no private paths, tokens, or local identity details.

## 7. Run the Release Audit

Replace `<report-path>` with the generated report:

```bash
python3 tools/report_audit.py extract --report <report-path>
```

Verify each extracted item against reliable sources, then run:

```bash
python3 tools/report_audit.py verdict \
  --results '<verified JSON>' \
  --report <report-path>
```

A failed verdict means the report remains a draft. Correct the failed items and repeat the audit.

## 8. Confirm Source and Generated Workflow Consistency

```bash
python3 scripts/sync-codex-skills.py --check
python3 scripts/sync-codex-prompts.py --check
```

Both commands must complete successfully. Claude Code and Codex should then be following the same canonical workflow for the shared skill.

## Demonstration Success Criteria

The demonstration succeeds when:

- installation completes without writing into the repository itself;
- 20 Claude Code commands are installed;
- 21 Codex skills are installed: 20 generated shared skills plus `investment-memo-craft`;
- 20 optional Codex prompts are installed;
- the workflow confirms the current date;
- current evidence is sourced rather than recalled from training data;
- financial calculations use repository tools;
- the report passes its audit or remains explicitly labeled as a draft;
- Claude Code and Codex produce the same decision structure for the shared workflow even when their wording differs.

The repository's GitHub Actions validation workflow automatically tests installation counts and generated-file consistency on Ubuntu, macOS, and Windows.
