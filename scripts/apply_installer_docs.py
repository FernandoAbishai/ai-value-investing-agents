#!/usr/bin/env python3
"""Apply unified-installer documentation updates. Remove before merge."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def patch_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "| Installation validation | Ubuntu, macOS, and Windows |\n| End-to-end demonstration |",
        "| Installation validation | Ubuntu, macOS, and Windows |\n| Unified local management | [`docs/INSTALLATION.md`](docs/INSTALLATION.md) |\n| End-to-end demonstration |",
        "README status",
    )
    start = text.index("## Installation\n")
    end = text.index("## End-to-end demonstration\n", start)
    installation = '''## Installation

Clone the repository after installing Claude Code, OpenAI Codex, or both through their official distribution channels:

```bash
git clone https://github.com/FernandoAbishai/ai-value-investing-agents.git
cd ai-value-investing-agents
```

### Install both environments

Unix-like systems:

```bash
./scripts/install.sh --all
```

Windows:

```bat
scripts\\install.bat --all
```

### Install one environment

```bash
./scripts/install.sh --claude
./scripts/install.sh --codex
```

Codex installation includes 20 generated shared skills, the Codex-only `investment-memo-craft` overlay, and 20 optional compatibility prompts.

### Update, diagnose, or uninstall

```bash
./scripts/manage.sh update --all
./scripts/manage.sh doctor --all
./scripts/manage.sh uninstall --all
```

Windows uses `scripts\\manage.bat` with the same arguments.

The manager supports `--dry-run`, collision backups, SHA-256 drift detection, JSON diagnostics, component-specific targets, and safe forced removal. It never downloads content or runs `git pull`.

See [`docs/INSTALLATION.md`](docs/INSTALLATION.md) for destinations, environment overrides, backup behavior, recovery, and backward-compatible commands.

Restart Claude Code or Codex after installation or update.

'''
    text = text[:start] + installation + text[end:]
    text = replace_once(
        text,
        "The GitHub social-preview image must be uploaded through repository settings; tracking the source asset in Git does not activate the repository metadata automatically.",
        "The editable source remains tracked in Git; the raster social preview was uploaded separately through repository settings.",
        "README social preview status",
    )
    text = replace_once(
        text,
        "scripts/                    Installation and synchronization scripts",
        "scripts/                    Synchronization, installation management, and quality scripts",
        "README architecture",
    )
    text = replace_once(
        text,
        "- deterministic financial, audit, Taiwan-data, and verified-example tests;\n- 20 canonical shared workflows;",
        "- deterministic financial, audit, Taiwan-data, verified-example, and installer-safety tests;\n- unified install, update, doctor, uninstall, and backward-compatible alias lifecycles;\n- 20 canonical shared workflows;",
        "README validation bullets",
    )
    path.write_text(text, encoding="utf-8")


def patch_agents() -> None:
    path = ROOT / "AGENTS.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- `scripts/`: synchronization and installation scripts.",
        "- `scripts/manage.py`: unified install, update, doctor, and uninstall manager.\n- `scripts/`: compatibility wrappers, synchronization, quality, and release scripts.",
        "AGENTS layout",
    )
    text = replace_once(
        text,
        "Use the repository-root-relative commands documented in the README. Do not assume that the checkout is located in a particular user's home directory when running tools; locate the actual repository root first.",
        "Use `scripts/manage.py` or its shell and batch wrappers for installation changes. Preserve manifest ownership, collision backups, `--dry-run`, drift diagnostics, and refusal to delete modified entries without explicit force. Keep component-specific installers as compatible aliases.\n\nUse the repository-root-relative commands documented in the README. Do not assume that the checkout is located in a particular user's home directory when running tools; locate the actual repository root first.",
        "AGENTS installer rules",
    )
    path.write_text(text, encoding="utf-8")


def patch_claude() -> None:
    path = ROOT / "CLAUDE.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "scripts/                      Synchronization and installation scripts",
        "scripts/                      Synchronization, quality, and installation-management scripts",
        "CLAUDE layout",
    )
    marker = "## Git and Repository Operations\n"
    section = '''## Local Installation Management

Use the unified manager rather than copying installed files manually:

```bash
./scripts/install.sh --all
./scripts/manage.sh update --all
./scripts/manage.sh doctor --all
./scripts/manage.sh uninstall --all
```

Windows uses `scripts\\install.bat` and `scripts\\manage.bat`. Preserve backups, manifests, `--dry-run`, component targeting, and modified-file deletion safeguards when changing installer behavior. Existing component-specific scripts are compatibility aliases and must remain tested.

'''
    text = replace_once(text, marker, section + marker, "CLAUDE installer section")
    path.write_text(text, encoding="utf-8")


def patch_status() -> None:
    path = ROOT / "docs" / "ENGLISH_EDITION.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "| Cross-platform installation validation | Ubuntu, macOS, and Windows |",
        "| Unified installation management | Install, update, doctor, uninstall, backups, manifests, and dry-run |\n| Cross-platform installation validation | Ubuntu, macOS, and Windows |",
        "status manager row",
    )
    text = replace_once(
        text,
        "- [x] Publish a curated set of three verified English example reports.\n",
        "- [x] Publish a curated set of three verified English example reports.\n- [x] Add unified installation, update, diagnostics, and safe uninstall management.\n",
        "status milestone",
    )
    text = replace_once(
        text,
        "- [ ] Add a unified installer, updater, uninstaller, and diagnostics command.\n",
        "",
        "status roadmap",
    )
    path.write_text(text, encoding="utf-8")


def patch_changelog() -> None:
    path = ROOT / "CHANGELOG.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- Three point-in-time verified English research examples under `reports/examples/` with source registers and executable audit fixtures.\n",
        "- Three point-in-time verified English research examples under `reports/examples/` with source registers and executable audit fixtures.\n- Unified cross-platform installation management with manifests, backups, dry runs, drift diagnostics, updates, and safe uninstall behavior.\n",
        "changelog manager",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    patch_readme()
    patch_agents()
    patch_claude()
    patch_status()
    patch_changelog()
    print("Updated unified installer documentation.")


if __name__ == "__main__":
    main()
