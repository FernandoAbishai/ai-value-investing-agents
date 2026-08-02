# AI Value Investing Agents: English Edition Status

**AI Value Investing Agents** is the maintained English-first edition of the AI Berkshire value-investing research framework.

## Project Identity

- **Repository:** `FernandoAbishai/ai-value-investing-agents`
- **Display name:** AI Value Investing Agents
- **Stable release:** `v1.0.0`
- **Framework lineage:** AI Berkshire
- **Maintainer:** Fernando Abishai
- **Original project:** [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

The original methodology, Chinese workflows, historical reports, and performance materials were created or published by the original project maintainer. This edition focuses on English accessibility, source/generated consistency, clearer attribution, reproducible installation, and maintainable workflows for Claude Code and OpenAI Codex.

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

Generated files must not be translated or edited independently because that creates drift between Claude Code and Codex behavior.

## Current Status

| Area | Status |
|---|---|
| Repository identity and clone paths | Complete |
| English README and installation instructions | Complete |
| `AGENTS.md` and `CLAUDE.md` | English and aligned with the maintained edition |
| All 20 canonical `skills/*.md` workflows | English |
| Codex skill packages | Generated from canonical English sources |
| Codex slash prompts | Generated from canonical English sources |
| Cross-platform installation validation | Ubuntu, macOS, and Windows |
| End-to-end workflow demonstration | Published in `docs/QUICKSTART_DEMO.md` |
| Tagged English-edition release | `v1.0.0` |
| Historical research archive | Preserved primarily in its original language |
| Curated newly verified English reports | Planned after v1.0.0 |
| Social preview and launch material | Planned after v1.0.0 |

## Validation and Release Process

`.github/workflows/validate.yml` verifies:

- generator `--check` modes;
- Python compilation;
- one-to-one correspondence among 20 canonical workflows, 20 Codex skill packages, and 20 prompts;
- clean installation on Ubuntu, macOS, and Windows.

`.github/workflows/release.yml` publishes a semantic-version GitHub release only when a commit merged to `main` begins with `Release vX.Y.Z`, the matching release-notes file exists, and release validation succeeds.

Release notes for the first maintained edition are in `docs/releases/v1.0.0.md`.

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
- [x] Add cross-platform installation and consistency validation.
- [x] Publish an end-to-end workflow demonstration.
- [x] Prepare and publish the `v1.0.0` English-edition release.

## Post-v1.0.0 Roadmap

- [ ] Add a GitHub social preview image.
- [ ] Publish a public launch article and video demonstration.
- [ ] Add a small curated set of newly verified English research reports.
- [ ] Add link checking and stale-repository-reference validation.
- [ ] Expand tool-level tests for financial and report-audit utilities.
- [ ] Collect installation feedback from Claude Code and Codex users.

## v1.0.0 Release Checklist

```text
[x] Both synchronization scripts pass with --check.
[x] Installation scripts are covered on Unix-like environments and Windows.
[x] README commands match actual repository paths.
[x] Generated Codex artifacts match all canonical workflows.
[x] Active guidance contains no stale maintained-project paths.
[x] Public documentation contains no private paths, tokens, or identity data.
[x] An end-to-end workflow demonstration is published.
[x] Release notes explain lineage, attribution, limitations, and migration.
```
