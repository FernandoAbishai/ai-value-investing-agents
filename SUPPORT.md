# Support and Feedback

AI Value Investing Agents is maintained as an open-source research framework. Support is provided through reproducible GitHub issues rather than private investment consultation.

## Start here

- Installation, update, diagnostics, uninstall, and recovery: [`docs/INSTALLATION.md`](docs/INSTALLATION.md)
- End-to-end workflow walkthrough: [`docs/QUICKSTART_DEMO.md`](docs/QUICKSTART_DEMO.md)
- Verified English examples: [`reports/examples/`](reports/examples/)
- Contribution requirements: [`CONTRIBUTING.md`](CONTRIBUTING.md)
- Security reporting: [`SECURITY.md`](SECURITY.md)

## Choose the correct issue form

### Workflow error

Use the workflow-error form for broken instructions, invalid paths, missing variables, contradictory decision gates, generated-source drift, or unusable output contracts.

Include the exact workflow, environment, repository version, redacted request, observed behavior, and expected behavior.

### Financial data error

Use the financial-data form for a wrong value, period, unit, currency, accounting definition, calculation, or source interpretation.

Include primary-source evidence and identify GAAP versus adjusted metrics, fiscal periods, share counts, currency, and corporate actions when relevant.

### Installation problem

Use the installation form for failures in install, update, doctor, uninstall, dry-run, or compatibility aliases.

Run the doctor command when possible:

```bash
./scripts/manage.sh doctor --all
```

Windows:

```bat
scripts\manage.bat doctor --all
```

Redact local usernames, private directories, credentials, and unrelated file names before posting output.

### Workflow proposal

Use the workflow-proposal form for a distinct, testable research process. Explain the decision it improves, the gap in current workflows, source hierarchy, output contract, blocking gates, validation strategy, and safety boundaries.

## Not supported

The issue tracker is not for:

- personalized buy, sell, allocation, tax, or legal advice;
- requests to research a specific company without a repository defect;
- guaranteed returns or performance claims;
- confidential company documents, private messages, unpublished holdings, or paid-source redistribution;
- general questions already answered in the README or installation guide;
- public vulnerability disclosure before a fix is available.

## Security issues

Do not open a public issue for credential exposure, unsafe command execution, path traversal, prompt-injection bypasses, release abuse, or another security vulnerability. Follow [`SECURITY.md`](SECURITY.md) and use GitHub private vulnerability reporting when available.

## Response expectations

Maintainer response time is not guaranteed. High-quality reports are easier to evaluate when they include:

1. a minimal reproduction;
2. exact file and version information;
3. complete but redacted error output;
4. reliable evidence;
5. a clear expected result;
6. confirmation that privacy and credential checks were performed.

Issues may be closed when they are duplicates, not reproducible, outside scope, unsafe to discuss publicly, or missing essential evidence after a reasonable request for clarification.

## Research disclaimer

Repository support does not convert generated output into professional investment advice. Users remain responsible for verifying filings, prices, currencies, calculations, legal obligations, and suitability for their circumstances.
