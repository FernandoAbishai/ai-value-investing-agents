# Contributing Guide

Thank you for contributing to **AI Value Investing Agents**. This repository is an English-first, independently maintained edition derived from the original AI Berkshire framework. Contributions should improve research rigor, reproducibility, compatibility, or usability without weakening attribution or financial-safety controls.

## Before opening a pull request

1. Search existing issues and pull requests for related work.
2. Keep the change focused on one problem.
3. For a new workflow or a substantial behavioral change, open an issue first and explain the use case and its boundary relative to the existing workflows.
4. Do not edit generated Codex files independently. Change the canonical file under `skills/`, regenerate both Codex surfaces, and commit the synchronized result.

## Contributions we welcome

- **Workflow bug fixes** for broken instructions, invalid paths, missing variables, unusable output contracts, or contradictory decision gates.
- **Research-quality improvements** that strengthen primary-source use, cross-validation, exact calculation, uncertainty handling, auditability, attribution, or falsification criteria.
- **Tooling improvements** for financial validation, report auditing, installation, synchronization, and deterministic testing.
- **Documentation fixes** for incorrect commands, stale paths, broken links, confusing explanations, or missing migration information.
- **Compatibility updates** for Claude Code, OpenAI Codex, Python, Windows, macOS, or Linux.
- **Verified example reports** produced with this repository. New examples should go under `reports/examples/` or community contributions under `reports/community/`, state the workflow and model used, include a research cutoff date, identify sources, and include the investment-advice disclaimer.

## Out of scope

- Editing historical reports or performance material merely to change their conclusions.
- Return promises, personalized stock recommendations, or promotional claims presented as research evidence.
- Large automated formatting changes without substantive benefit.
- Boilerplate governance files unrelated to an actual repository need.
- New workflows that duplicate an existing capability without a clear boundary.
- Generated files that were manually edited instead of regenerated from canonical sources.

## Canonical and generated files

The 20 shared workflows are maintained under:

```text
skills/*.md
```

After changing a canonical workflow, run:

```bash
python3 scripts/sync-codex-skills.py
python3 scripts/sync-codex-prompts.py
python3 scripts/sync-codex-skills.py --check
python3 scripts/sync-codex-prompts.py --check
```

`codex-skills/investment-memo-craft/SKILL.md` is the only currently declared Codex-only package and may be maintained directly because it has no same-named canonical workflow.

## Required validation

Before submitting a pull request, run:

```bash
python3 scripts/repository_quality.py
python3 scripts/sync-codex-skills.py --check
python3 scripts/sync-codex-prompts.py --check
python3 -m compileall -q scripts tools
```

The repository-quality check validates local Markdown targets, external URL structure, current project identity, private-path leakage, high-confidence secrets, English operational content, and workflow inventory.

Installation and synchronization are also tested automatically on Ubuntu, macOS, and Windows.

## Pull request description

Explain:

- what changed;
- why the change is needed;
- how it was validated;
- which workflows, tools, or platforms are affected;
- whether generated artifacts changed;
- any known limitations.

For workflow changes, include a concrete example or a representative before-and-after excerpt when possible. Do not include confidential company information, private paths, API credentials, or unpublished personal data.

## Issue reports

A useful issue includes enough detail to reproduce the problem.

### Workflow error

Include the workflow name, complete request, client and model, observed behavior, expected behavior, and any relevant error output.

### Financial-data error

Include the company or ticker, reporting period, incorrect value, expected value, source links, currency, units, and any split, dilution, adjustment, or foreign-exchange considerations.

### Installation problem

Include the operating system, shell, Python version, installation command, destination path expressed without a private username, and full error output.

### Feature or workflow proposal

Describe the research decision it improves, why an existing workflow cannot cover it, expected inputs and outputs, and how correctness could be tested.

Research requests for a specific company are not accepted as repository issues. Use the installed workflows to perform the research directly.

## Security

Do not open a public issue for credential exposure, prompt-injection bypasses, unsafe command execution, or another security vulnerability. Follow [SECURITY.md](SECURITY.md) and use GitHub private vulnerability reporting when available.

## Attribution and real-person frameworks

Preserve the repository's lineage and attribution. Commentary inspired by a real investor must be labeled as a framework-based interpretation unless it is a verified quotation with a reliable source. Do not impersonate a person or imply endorsement.

## Disclaimer

This project is for education and research. It does not provide investment, legal, accounting, or tax advice. Contributions must not present AI-generated output as independently verified without evidence.
