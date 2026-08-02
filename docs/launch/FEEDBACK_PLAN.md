# Launch Feedback Plan

This plan converts public feedback into scoped, reproducible repository work without turning comments into unverified requirements.

## Objectives

During the first public launch cycle, collect evidence about:

1. installation success and failure by operating system;
2. workflow clarity and missing decision gates;
3. financial-data, unit, period, and calculation errors;
4. differences between Claude Code and Codex behavior;
5. usability of reports, audits, and verification registers;
6. requests for additional markets, accounting regimes, or workflows.

Do not collect personal portfolio details, brokerage information, confidential company material, credentials, or personalized investment objectives.

## Intake channels

### Structured GitHub issues

Use the repository forms for actionable defects and proposals:

- workflow error;
- financial data error;
- installation problem;
- workflow proposal.

These are the system of record. Feedback received elsewhere should be summarized into a GitHub issue only when it is reproducible, in scope, and safe to publish.

### External comments

LinkedIn, X, Reddit, Hacker News, and YouTube comments are discovery channels, not the authoritative backlog. Do not commit directly to an implementation in a comment thread. Ask the reporter to use the appropriate issue form or create a scoped issue that attributes the public discussion without copying private information.

### Security reports

Potential vulnerabilities move to private vulnerability reporting. Do not request exploit details in a public issue.

## Triage states

Use these conceptual states even when GitHub labels are not configured:

| State | Meaning | Required next action |
|---|---|---|
| New | Not yet evaluated | Confirm scope, safety, and minimum evidence |
| Needs reproduction | Plausible but incomplete | Request exact version, command, input, and redacted output |
| Needs source verification | Financial or factual claim is disputed | Obtain primary-source evidence and reproduce the calculation |
| Confirmed | Reproduced and in scope | Define acceptance criteria and implementation boundary |
| Planned | Approved for a release or milestone | Assign order and dependencies |
| Resolved | Fix merged and validated | Link commit or release and request confirmation |
| Not planned | Duplicate, out of scope, unsafe, or unsupported | Explain the reason without debating personal investment views |

## Severity guidance

### Critical

- credential or private-data exposure;
- unsafe command execution or destructive installer behavior;
- release or workflow permission abuse;
- a financial tool producing materially wrong results across normal inputs while appearing verified.

Handle security-sensitive cases privately.

### High

- report audit incorrectly returns `PASS` for failed or unverified data;
- installer deletes unrelated or locally modified files without explicit force;
- canonical and generated workflows materially diverge;
- a primary-source figure is systematically assigned the wrong sign, unit, currency, or period.

### Medium

- a workflow path, command, placeholder, or output contract is broken;
- one platform fails installation with a reproducible error;
- a verified example contains a material but localized source or calculation error.

### Low

- wording, formatting, discoverability, or non-blocking documentation issues;
- feature requests without current user impact.

Severity describes repository impact, not the expected movement of a security price.

## Reproduction standard

A confirmed report should contain:

- exact repository tag or commit;
- operating system and Python version when relevant;
- canonical workflow or tool name;
- minimal redacted input;
- observed output;
- expected output;
- reliable source evidence for financial claims;
- a deterministic test or a clear reason one cannot be created.

## Weekly launch review

During the active launch period, review feedback in this order:

1. security and destructive behavior;
2. incorrect financial calculations or false audit passes;
3. installation failures;
4. source/generated drift;
5. workflow defects;
6. documentation and discoverability;
7. new workflow proposals.

Create no more than one implementation issue per distinct root cause. Merge duplicates and preserve the clearest reproduction.

## Acceptance criteria for fixes

A fix is complete only when:

- the root cause is explained;
- a regression test exists when feasible;
- repository quality gates pass;
- Ubuntu, macOS, and Windows CI pass when the change is cross-platform;
- canonical and generated artifacts remain synchronized;
- documentation or verified examples are updated when behavior changes;
- no temporary migration workflow or script remains.

## Feedback metrics

Track manually in the launch-feedback issue or a future project board:

- successful installations by operating system;
- reproducible installation failures;
- confirmed workflow defects;
- confirmed financial-data errors;
- average time from confirmation to merge;
- proposals accepted, deferred, or rejected;
- number of issues closed for missing reproduction or unsafe content.

Do not use stars, impressions, or comment volume as a proxy for research correctness.

## Closing the launch cycle

The launch cycle can move to normal maintenance when:

- no unresolved critical or high-severity issue remains;
- installation has been confirmed by external users on at least Windows and one Unix-like system;
- the video and launch article are published or intentionally deferred;
- the main recurring feedback themes have scoped issues or documented reasons for no action;
- the next release boundary is clear.
