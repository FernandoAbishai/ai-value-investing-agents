# Installation and Local Management

AI Value Investing Agents includes a dependency-free Python manager for Claude Code commands, Codex skills, and optional Codex prompts.

## Requirements

- Python 3.10 or newer.
- A local clone of this repository.
- Write access to the selected installation directories.

Default destinations:

| Component | Default destination | Override |
|---|---|---|
| Claude Code commands | `~/.claude/commands` | `CLAUDE_COMMANDS_DIR` |
| Codex skills | `~/.codex/skills` | `CODEX_HOME` |
| Codex prompts | `~/.codex/prompts` | `CODEX_HOME` |
| Manager manifest and backups | `~/.ai-value-investing-agents` | `AIVA_STATE_HOME` |

The manifest contains local installation paths and hashes. It is stored outside the repository and must not be committed.

## Install

### Unix-like systems

Install everything:

```bash
./scripts/install.sh --all
```

Install one environment:

```bash
./scripts/install.sh --claude
./scripts/install.sh --codex
```

Install one Codex surface:

```bash
./scripts/install.sh --codex-skills
./scripts/install.sh --codex-prompts
```

### Windows

```bat
scripts\install.bat --all
scripts\install.bat --claude
scripts\install.bat --codex
```

The installation manager verifies that generated Codex packages are synchronized before copying them.

## Dry run

Preview every file that would be installed, replaced, backed up, or removed:

```bash
./scripts/install.sh --all --dry-run
```

Windows:

```bat
scripts\install.bat --all --dry-run
```

A dry run does not create destinations, backups, or a manifest.

## Backups

Installation and update operations back up an existing conflicting file or skill before replacing it. Backups are written under:

```text
<AIVA_STATE_HOME>/backups/<UTC timestamp>/<component>/
```

An identical installed entry is left unchanged and is not backed up again.

`--no-backup` disables collision backups. Use it only when the destination is disposable or already protected elsewhere.

## Update an existing installation

After pulling a newer repository version, refresh installed components from the current checkout:

```bash
./scripts/manage.sh update --all
```

Windows:

```bat
scripts\manage.bat update --all
```

Update uses the same safe reconciliation process as installation:

- identical files are unchanged;
- different files are backed up and replaced;
- obsolete managed entries are removed when they were not modified locally;
- modified obsolete entries are preserved and reported.

The update command updates installed files from the current checkout. It does not run `git pull` or change repository branches.

## Diagnose

Check Python compatibility, source inventory, generated-file synchronization, the installation manifest, missing entries, and local modifications:

```bash
./scripts/manage.sh doctor --all
```

Windows:

```bat
scripts\manage.bat doctor --all
```

Machine-readable output:

```bash
./scripts/manage.sh doctor --all --json
```

The command returns a nonzero exit code when it detects an issue.

## Uninstall

Remove only entries recorded in the manager manifest:

```bash
./scripts/manage.sh uninstall --all
```

Windows:

```bat
scripts\manage.bat uninstall --all
```

The manager preserves unrelated files in the destination directories.

If a managed entry was modified after installation, uninstall refuses to delete it. Review the file, then either keep it or explicitly force removal:

```bash
./scripts/manage.sh uninstall --all --force --backup-modified
```

`--backup-modified` saves changed entries before forced removal.

Preview an uninstall:

```bash
./scripts/manage.sh uninstall --all --dry-run
```

## Custom temporary installation

The environment variables can isolate a test installation completely:

```bash
export CLAUDE_COMMANDS_DIR="$(mktemp -d)/claude/commands"
export CODEX_HOME="$(mktemp -d)/codex"
export AIVA_STATE_HOME="$(mktemp -d)/state"
./scripts/install.sh --all
./scripts/manage.sh doctor --all
```

Do not place private usernames or tokens in committed examples or issue reports.

## Backward-compatible scripts

The existing component-specific commands remain available and delegate to the unified manager:

```bash
./scripts/install-claude-commands.sh
./scripts/install-codex-skills.sh
./scripts/install-codex-prompts.sh
```

Windows equivalents remain available as `.bat` files.

## Recovery

If installation is interrupted:

1. Run `doctor --all` to identify missing or modified entries.
2. Run `update --all` to restore files from the current checkout.
3. Inspect the timestamped backup directory before deleting it.
4. Do not delete the manifest manually unless you intentionally want the manager to forget the installation.

If the manifest is lost, installation can safely create a new one. Existing collisions will be backed up before replacement.

## Security model

- Generated Codex artifacts must pass their synchronization checks before installation.
- The manager never downloads or executes remote content.
- The manager does not modify the repository checkout.
- Uninstall acts only on manifest-recorded entries.
- Modified managed entries require explicit force before deletion.
- Backups and manifests can contain local paths; keep the state directory private.
