#!/usr/bin/env python3
"""Apply v1.1.0 release metadata and validation updates. Remove before merge."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


def patch_changelog() -> None:
    path = ROOT / "CHANGELOG.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "## Unreleased\n\n### Added\n",
        "## Unreleased\n\nNo unreleased changes.\n\n## [1.1.0] — 2026-08-02\n\n### Added\n",
        "changelog version heading",
    )
    text = replace_once(
        text,
        "- Support policy, launch feedback triage plan, verified-workflow video script, and public publishing checklist.\n\n### Fixed\n",
        "- Support policy, launch feedback triage plan, verified-workflow video script, and public publishing checklist.\n\n### Changed\n\n- Strengthened release publication so quality gates, deterministic tests, and the unified installation lifecycle must pass before a tag is created.\n- Updated the maintained stable-version references and release documentation for `v1.1.0`.\n\n### Fixed\n",
        "changelog changed section",
    )
    path.write_text(text, encoding="utf-8")


def patch_readme() -> None:
    path = ROOT / "README.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "| Stable English-edition release | `v1.0.0` |",
        "| Stable English-edition release | `v1.1.0` |",
        "README stable version",
    )
    text = replace_once(
        text,
        "and the [v1.0.0 release notes](docs/releases/v1.0.0.md)",
        "and the [v1.1.0 release notes](docs/releases/v1.1.0.md)",
        "README release notes link",
    )
    path.write_text(text, encoding="utf-8")


def patch_edition_status() -> None:
    path = ROOT / "docs" / "ENGLISH_EDITION.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- **Stable release:** `v1.0.0`",
        "- **Stable release:** `v1.1.0`",
        "edition identity version",
    )
    text = replace_once(
        text,
        "| Tagged English-edition release | `v1.0.0` |",
        "| Tagged English-edition release | `v1.1.0` |",
        "edition status version",
    )
    text = replace_once(
        text,
        "Release notes for the first maintained edition are in `docs/releases/v1.0.0.md`.",
        "Release notes for the current maintained edition are in `docs/releases/v1.1.0.md`; the initial edition remains documented in `docs/releases/v1.0.0.md`.",
        "edition release notes",
    )
    text = replace_once(
        text,
        "- [x] Prepare and publish the `v1.0.0` English-edition release.\n",
        "- [x] Prepare and publish the `v1.0.0` English-edition release.\n- [x] Prepare the `v1.1.0` reliability and operations release.\n",
        "edition milestone",
    )
    path.write_text(text, encoding="utf-8")


def patch_release_workflow() -> None:
    path = ROOT / ".github" / "workflows" / "release.yml"
    text = path.read_text(encoding="utf-8")
    old_validation = '''      - name: Validate release commit
        run: |
          python3 scripts/sync-codex-skills.py --check
          python3 scripts/sync-codex-prompts.py --check
          python3 -m compileall -q scripts tools
          python3 - <<'PY'
'''
    new_validation = '''      - name: Validate release commit
        run: |
          python3 scripts/repository_quality.py
          python3 scripts/sync-codex-skills.py --check
          python3 scripts/sync-codex-prompts.py --check
          python3 -m compileall -q scripts tools tests
          python3 -m unittest discover -s tests -v
          python3 - <<'PY'
'''
    text = replace_once(text, old_validation, new_validation, "release validation commands")
    marker = "      - name: Publish GitHub release\n"
    lifecycle = '''      - name: Validate unified installation lifecycle
        env:
          CLAUDE_COMMANDS_DIR: ${{ runner.temp }}/release-claude/commands
          CODEX_HOME: ${{ runner.temp }}/release-codex
          AIVA_STATE_HOME: ${{ runner.temp }}/release-state
        run: |
          ./scripts/install.sh --all --dry-run
          test ! -e "$AIVA_STATE_HOME/manifest.json"
          ./scripts/install.sh --all
          ./scripts/manage.sh doctor --all
          ./scripts/manage.sh update --all
          ./scripts/manage.sh uninstall --all

'''
    text = replace_once(text, marker, lifecycle + marker, "release installation lifecycle")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    patch_changelog()
    patch_readme()
    patch_edition_status()
    patch_release_workflow()
    print("Applied v1.1.0 release metadata and validation updates.")


if __name__ == "__main__":
    main()
