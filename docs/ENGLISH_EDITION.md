# AI Value Investing Agents: English Edition Status

**AI Value Investing Agents** is the maintained English-first edition of the AI Berkshire value-investing research framework.

## Project Identity

- **Repository:** `FernandoAbishai/ai-value-investing-agents`
- **Display name:** AI Value Investing Agents
- **Stable release:** `v1.2.0`
- **Framework lineage:** AI Berkshire
- **Maintainer:** Fernando Abishai
- **Original project:** [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

The original methodology, Chinese workflows, historical reports, and performance materials were created or published by the original project maintainer. This edition focuses on English accessibility, source/generated consistency, clearer attribution, reproducible installation, deterministic research tooling, and maintainable workflows for Claude Code and OpenAI Codex.

## Repository Description

> English-first edition derived from AI Berkshire: a multi-agent value-investing research framework for Claude Code and OpenAI Codex.

## Recommended Topics

`ai-agents`, `value-investing`, `investment-research`, `fundamental-analysis`, `financial-analysis`, `stock-analysis`, `multi-agent-systems`, `agentic-ai`, `claude-code`, `openai-codex`, `llm`, `fintech`, `portfolio-management`, `warren-buffett`, `charlie-munger`, `python`

## Canonical Architecture

The repository uses one canonical source per shared workflow:

1. Edit `skills/*.md` first.
2. Regenerate `codex-skills/*/SKILL.md` with `scripts/sync-codex-skills.py`.
3. Regenerate `codex-prompts/*.md` with `scripts/sync-codex-prompts.py`.
4. Run both synchronization scripts with `--check`.
5. Verify command names, paths, placeholders, code blocks, audit gates, and output contracts.

Generated shared files must not be translated or edited independently because that creates drift between Claude Code and Codex behavior.

A Codex-only skill may be maintained directly under `codex-skills/` only when it is clearly declared and has no same-named canonical source. The current declared Codex-only skill is `investment-memo-craft`.

## Current Status

| Area | Status |
|---|---|
| Repository identity and clone paths | Complete |
| English README and installation instructions | Complete |
| `AGENTS.md` and `CLAUDE.md` | English and aligned with the maintained edition |
| Canonical shared `skills/*.md` workflows | 21 English workflows |
| Generated Codex shared packages | 21 packages from canonical English sources |
| Codex-only packages | 1 declared package: `investment-memo-craft` |
| Codex slash prompts | 21 generated prompts for shared workflows |
| Unified installation management | Install, update, doctor, uninstall, backups, manifests, and dry-run |
| Cross-platform installation validation | Ubuntu, macOS, and Windows |
| End-to-end workflow demonstration | Published in `docs/QUICKSTART_DEMO.md` |
| Tagged English-edition release | `v1.2.0` |
| Upstream reusable-framework review | Complete through October 12, 2026 |
| Historical report index | 2,203 tracked reports · 109 company groups · 16 themes |
| Report-index drift gate | Full-history read-only GitHub Actions check |
| Public launch article and channel copy | Prepared in `docs/launch/` |
| Video demonstration script and publishing gate | Prepared in `docs/launch/` |
| Structured support and feedback intake | Four issue forms, `SUPPORT.md`, issue #17, and launch triage plan |
| Social-preview design source | Prepared at `assets/social-preview-source.svg` |
| GitHub social-preview metadata | Uploaded by the maintainer |
| Historical research archive | Preserved primarily in its original language |
| Curated newly verified English reports | Three published under `reports/examples/` with executable audit fixtures |

## Validation and Release Process

`.github/workflows/validate.yml` verifies:

- generator `--check` modes for shared Codex surfaces;
- repository quality gates for links, identity, privacy, secrets, and operational language;
- deterministic unit, example-report, installer, report-index regression, and community-template tests;
- Python compilation;
- one-to-one correspondence among 21 canonical workflows, 21 generated Codex shared packages, and 21 prompts;
- the presence of exactly one declared Codex-only package, `investment-memo-craft`;
- clean installation of 21 Claude Code commands, 22 Codex skills, and 21 prompts on Ubuntu, macOS, and Windows.

`.github/workflows/report-index.yml` checks out full Git history and runs `python3 tools/reports_index.py --check`. This keeps the history-dependent archive index deterministic without requiring every cross-platform validation job to fetch the full repository history.

`.github/workflows/release.yml` publishes a semantic-version GitHub release only when a commit merged to `main` begins with `Release vX.Y.Z`, the matching release-notes file exists, and release validation succeeds. Release validation includes repository quality gates, generated-surface checks, report-index freshness, the complete deterministic test suite, workflow inventory consistency, and the unified installation lifecycle.

Release notes for the current maintained edition are in `docs/releases/v1.2.0.md`; earlier releases remain documented under `docs/releases/`.

## Upstream Synchronization

The English edition does not attempt commit-count parity with the original project. Upstream changes are reviewed selectively and adapted when they improve reusable methodology, tooling, correctness, privacy, or maintenance.

The current review boundary is upstream commit `ab56abcb31ef8e3a92d925f1b18fb339341ac9d3` from October 12, 2026. The review record and synchronization policy are maintained in `docs/UPSTREAM_REVIEW_2026-10.md`.

Bulk historical research, portfolio records, publishing assets, and maintainer-specific material are not automatically imported merely to reduce divergence.

## Historical Report Index

`tools/reports_index.py` generates:

- `reports/README.md` for human navigation;
- `reports/index.json` for machine-readable inventory.

The generator indexes only report contents represented in Git's index. Untracked drafts, ignored files, and intent-to-add placeholders are excluded. Git-read failures stop generation rather than risking publication of local-only material.

The initial committed inventory contains 2,203 reports across 109 company groups and 16 themes. `reports/examples/` is classified as `Verified English examples`, while its `VERIFICATION.md` register is excluded from the report inventory.

## Historical Reports

Historical reports remain available as source material. The English edition prioritizes a curated set of newly verified English reports rather than mechanically translating the entire archive.

Every translated, adapted, or newly produced report should:

- retain attribution to the original source when applicable;
- state whether figures and conclusions were translated, updated, or newly researched;
- include the research cutoff date;
- distinguish historical output from results independently produced by this edition;
- pass the repository audit process when financially material.

## Performance Claims

Any historical track record shown in this edition must be attributed to the original project maintainer unless independently produced and documented by this edition. Historical returns do not guarantee future results and must not be presented as independently audited without evidence.

## Attribution and Real-Person Frameworks

Workflows inspired by real investors distinguish among:

- verified quotations;
- paraphrases of publicly discussed ideas;
- framework-based interpretations.

Generated commentary must not impersonate a real person or imply endorsement. Unverified wording should be paraphrased rather than placed in quotation marks.

## Completed Milestones

- [x] Rename the maintained repository to `ai-value-investing-agents`.
- [x] Establish the English repository identity.
- [x] Correct clone URLs and language navigation.
- [x] Translate all canonical operational workflows.
- [x] Synchronize Codex skills and prompts from canonical sources.
- [x] Clarify historical-report and performance attribution.
- [x] Replace stale Claude Code and Codex repository guidance.
- [x] Update the Codex-only report overlay for the English edition.
- [x] Add cross-platform installation and consistency validation.
- [x] Publish an end-to-end workflow demonstration.
- [x] Prepare and publish the `v1.0.0` English-edition release.
- [x] Prepare a long-form launch article and channel-specific social copy.
- [x] Prepare an editable 1280 × 640 social-preview source.
- [x] Upload the GitHub social preview.
- [x] Add repository-wide quality gates.
- [x] Add deterministic financial and audit-tool tests.
- [x] Publish a curated set of three verified English example reports.
- [x] Add unified installation, update, diagnostics, and safe uninstall management.
- [x] Add structured issue forms, support policy, feedback triage, video script, and publishing checklist.
- [x] Prepare the `v1.1.0` reliability and operations release.
- [x] Add `era-alpha` as the 21st canonical shared workflow.
- [x] Add long-horizon terminal-value and IRR audit tooling.
- [x] Review reusable upstream framework changes through October 12, 2026.
- [x] Add hardened report indexing with cross-platform regression coverage.
- [x] Bootstrap the generated archive index from full Git history.
- [x] Add permanent report-index drift validation.
- [x] Prepare the `v1.2.0` upstream-sync and research-index release.

## Post-v1.2.0 Roadmap

- [ ] Publish the launch article and selected social posts.
- [ ] Record and publish the prepared video demonstration using a verified example.
- [ ] Collect external installation feedback through issue #17 and the structured issue forms.
- [ ] Expand verified examples to additional markets and accounting regimes.
- [ ] Add deeper property-based and CLI error-path tests where useful.
- [ ] Continue selective upstream reviews when reusable framework changes appear.

## v1.2.0 Release Checklist

```text
[x] Both Codex synchronization scripts pass with --check.
[x] Repository quality gates pass.
[x] The complete deterministic test suite passes on Ubuntu, macOS, and Windows.
[x] Unified install, doctor, idempotent update, and uninstall pass.
[x] Backward-compatible installer aliases remain validated.
[x] The report index was generated from a full-history checkout and passes --check.
[x] The permanent report-index workflow passes after merge on main.
[x] The upstream review boundary is documented through October 12, 2026.
[x] README and edition metadata identify v1.2.0 as the stable release candidate.
[x] Release notes explain compatibility, upgrade steps, attribution, and limitations.
[x] Release validation no longer contains the stale hardcoded 20-workflow assertion.
[x] No temporary write-enabled bootstrap workflow remains in the merge candidate.
```
