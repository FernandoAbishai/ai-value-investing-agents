# Changelog

All notable changes to **AI Value Investing Agents** are documented in this file.

The project follows [Semantic Versioning](https://semver.org/) for maintained English-edition releases.

## [1.0.0] — 2026-08-02

### Added

- English canonical versions of all 20 investment-research workflows.
- Generated Codex skill packages and optional slash prompts synchronized from canonical sources.
- Cross-platform installers for Claude Code and OpenAI Codex.
- Permanent GitHub Actions validation on Ubuntu, macOS, and Windows.
- Automatic semantic-version release publication for approved `Release vX.Y.Z` commits.
- End-to-end quickstart demonstration in `docs/QUICKSTART_DEMO.md`.
- Exact-arithmetic and report-audit requirements across decision-sensitive workflows.

### Changed

- Renamed the maintained edition and active checkout path to `ai-value-investing-agents`.
- Rebuilt the English README, maintenance documentation, and repository identity.
- Updated `AGENTS.md` and `CLAUDE.md` to remove stale project names, paths, fixed-language requirements, and obsolete operating assumptions.
- Converted real-investor style simulations into explicitly labeled framework-based interpretations where appropriate.
- Strengthened source, attribution, privacy, copyright, current-date, and false-precision controls.

### Compatibility

- Claude Code uses `skills/*.md` as installed slash commands.
- Codex uses generated `codex-skills/*/SKILL.md` packages and optional `codex-prompts/*.md` entries.
- Canonical source and generated artifacts are validated for one-to-one consistency.

### Migration

Existing users of the original checkout path should clone or rename their local directory to:

```text
ai-value-investing-agents
```

Use the maintained repository URL:

```text
https://github.com/FernandoAbishai/ai-value-investing-agents.git
```

Historical reports and original-project attribution remain preserved.

### Limitations

- Historical reports are primarily retained in their original language and may contain data that was current only when they were written.
- Generated research can contain factual or mathematical errors and must be independently verified.
- The repository does not provide personalized investment, legal, accounting, or tax advice.

## Attribution

This repository is an English-first maintained edition derived from the original [AI Berkshire](https://github.com/xbtlin/ai-berkshire) project created by xbtlin.
