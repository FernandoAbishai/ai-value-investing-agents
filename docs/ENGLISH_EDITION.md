# AI Value Investing Agents

**AI Value Investing Agents** is the maintained English-first edition of the AI Berkshire value-investing research framework.

## Project identity

- **Repository name:** `ai-value-investing-agents`
- **Display name:** AI Value Investing Agents
- **Framework lineage:** AI Berkshire
- **Maintainer:** Fernando Abishai
- **Original project:** [xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

The original methodology, Chinese workflows, and historical research archive were created by xbtlin. This edition focuses on making the framework accessible and maintainable for an English-speaking audience while preserving clear attribution.

## Recommended repository description

> English-first fork of AI Berkshire: a multi-agent value investing research framework for Claude Code and Codex.

## Recommended topics

`ai-agents`, `value-investing`, `investment-research`, `fundamental-analysis`, `financial-analysis`, `stock-analysis`, `multi-agent-systems`, `agentic-ai`, `claude-code`, `openai-codex`, `llm`, `fintech`, `portfolio-management`, `warren-buffett`, `charlie-munger`, `python`

## Translation architecture

The repository should use a single canonical source for each workflow:

1. Translate `skills/*.md` first.
2. Regenerate `codex-skills/*/SKILL.md` with the existing synchronization script.
3. Regenerate `codex-prompts/*.md` from canonical sources.
4. Verify that command names, paths, placeholders, and code blocks remain unchanged.

Generated files should not be translated independently because that creates drift between Claude Code and Codex behavior.

## Historical reports

Historical Chinese reports should remain available as source material. The English edition should prioritize a curated set of representative translated reports rather than attempting to translate the entire archive immediately.

Recommended initial English report set:

- One full company deep-dive
- One multi-agent investment-team report
- One multi-company comparison

Every translated report should retain source attribution and clearly state whether data or conclusions were updated during translation.

## Performance claims

Any track record shown in this edition must be attributed to the original project maintainer unless independently produced and documented by this edition. Historical returns do not guarantee future results and should never be presented as independently audited without evidence.

## Discovery roadmap

1. Rename the repository to `ai-value-investing-agents`.
2. Set the English repository description and topics.
3. Correct clone URLs and language navigation in the README.
4. Translate canonical operational skills.
5. Publish a tagged English-edition release.
6. Add a GitHub social preview image.
7. Publish a launch article and concrete workflow demonstration.
