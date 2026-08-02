# Security Policy

## Supported versions

Security fixes are provided for the latest stable release and the current `main` branch.

## Reporting a vulnerability

Do not open a public issue for a vulnerability involving:

- API keys, credentials, private paths, or sensitive report data;
- prompt-injection bypasses that cause unintended tool or command execution;
- unsafe installer behavior or writes outside the documented destination;
- command injection, path traversal, or arbitrary file overwrite;
- release, workflow, or repository-permission abuse;
- another issue that could materially affect users of AI Value Investing Agents.

Use GitHub's private vulnerability reporting feature for this repository when available. Include a clear description, affected files or workflows, reproduction steps, impact, and any proposed mitigation. Avoid placing real credentials or confidential data in the report; use redacted examples instead.

## Scope

Security reports should concern the maintained repository's scripts, tools, workflows, installers, or operational instructions. Incorrect investment conclusions, ordinary model hallucinations, and disagreements with research judgments are quality issues rather than security vulnerabilities unless they arise from a reproducible security boundary failure.

## Safe research handling

This repository is designed for public-source research. Do not commit confidential filings, paid-source content without permission, customer information, private portfolio data, access tokens, or personally identifying local paths. Run `python3 scripts/repository_quality.py` before submitting changes.

## Disclosure

Please allow reasonable time for validation and remediation before public disclosure. Confirmed issues may be documented in release notes or a security advisory after a fix is available.
