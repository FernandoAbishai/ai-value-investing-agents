# AI Value Investing Agents: English Edition Status

**AI Value Investing Agents** is the maintained English-first edition of the AI Berkshire value-investing research framework.

## Project Identity

- **Repository:** `FernandoAbishai/ai-value-investing-agents`
- **Display name:** AI Value Investing Agents
- **Framework lineage:** AI Berkshire
- **Maintainer:** Fernando Abishai
- **Original project:** [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

The original methodology, Chinese workflows, historical reports, and performance materials were created or published by the original project maintainer. This edition focuses on English accessibility, source/generated consistency, clearer attribution, and maintainable workflows for Claude Code and OpenAI Codex.

## Repository Description

> English-first fork of AI Berkshire: a multi-agent value-investing research framework for Claude Code and OpenAI Codex.

## Recommended Topics

`ai-agents`, `value-investing`, `investment-research`, `fundamental-analysis`, `financial-analysis`, `stock-analysis`, `multi-agent-systems`, `agentic-ai`, `claude-code`, `openai-codex`, `llm`, `fintech`, `portfolio-management`, `warren-buffett`, `charlie-munger`, `python`

## Translation Architecture

The repository uses one canonical source per workflow:

1. Edit `skills/*.md` first.
2. Regenerate `codex-skills/*/SKILL.md` with `scripts/sync-codex-skills.py`.
3. Regenerate `codex-prompts/*.md` with `scripts/sync-codex-prompts.py`.
4. Run both scripts with `--check`.
5. Verify that command names, paths, placeholders, code blocks, audit gates, and output contracts remain intact.

Generated files must not be translated or edited independently because that creates drift between Claude Code and Codex behavior.

## Current Status

| Area | Status |
|---|---|
| Repository identity and clone paths | Complete |
| English README and installation instructions | Complete |
| Community and maintenance documentation | English-first |
| All 20 canonical `skills/*.md` workflows | English |
| Codex skill packages | Generated from canonical English sources |
| Codex slash prompts | Generated from canonical English sources |
| Historical research archive | Preserved primarily in its original language |
| Curated English demonstration reports | Pending |
| Tagged English-edition release | Pending |
| Social preview and launch material | Pending |

## Historical Reports

Historical Chinese reports remain available as source material. The English edition should prioritize a curated set of representative, newly verified English reports rather than mechanically translating the entire archive.

Recommended demonstration set:

- one full company deep dive;
- one multi-agent `investment-team` report;
- one multi-company or industry comparison;
- one earnings review showing primary-source and audit discipline.

Every translated or adapted report should:

- retain attribution to the original source when applicable;
- state whether figures and conclusions were merely translated or updated;
- include the research cutoff date;
- distinguish historical output from results independently produced by this edition;
- pass the repository audit process when financially material.

## Performance Claims

Any historical track record shown in this edition must be attributed to the original project maintainer unless independently produced and documented by this edition. Historical returns do not guarantee future results and must not be presented as independently audited without evidence.

## Attribution and Real-Person Frameworks

Workflows inspired by real investors must distinguish among:

- verified quotations;
- paraphrases of publicly discussed ideas;
- framework-based simulations or interpretations.

Generated commentary must not impersonate a real person or imply endorsement. Unverified wording should be paraphrased rather than placed in quotation marks.

## Discovery Roadmap

### Completed

- [x] Rename the repository to `ai-value-investing-agents`.
- [x] Establish the English repository identity.
- [x] Correct clone URLs and language navigation.
- [x] Translate all canonical operational workflows.
- [x] Synchronize Codex skills and prompts from canonical sources.
- [x] Clarify historical-report and performance attribution.

### Next

- [ ] Publish a tagged English-edition release.
- [ ] Add a GitHub social preview image.
- [ ] Publish a launch article and concrete workflow demonstration.
- [ ] Add a small curated set of newly verified English reports.
- [ ] Run a repository-wide documentation and installation smoke test.

## Release Readiness Checklist

Before the first tagged English-edition release:

```text
[ ] Both synchronization scripts pass with --check.
[ ] Installation scripts are tested on at least one Unix-like environment and Windows.
[ ] README commands match actual repository paths.
[ ] No generated Codex artifact contains stale legacy-language workflow text.
[ ] No public document contains private paths, tokens, or user identity data.
[ ] At least one end-to-end workflow demonstration is published.
[ ] Release notes explain lineage, attribution, limitations, and migration from the old repository name.
```
