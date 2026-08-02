#!/usr/bin/env python3
"""Apply launch-feedback documentation updates. Remove before merge."""

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
        "| Public launch kit | [`docs/launch/`](docs/launch/) |\n| Social-preview source |",
        "| Public launch kit | [`docs/launch/`](docs/launch/) |\n| Support and structured feedback | [`SUPPORT.md`](SUPPORT.md) |\n| Social-preview source |",
        "README status",
    )
    text = replace_once(
        text,
        "- [`docs/launch/SOCIAL_PREVIEW.md`](docs/launch/SOCIAL_PREVIEW.md): preview requirements and upload procedure;\n- [`assets/social-preview-source.svg`](assets/social-preview-source.svg): editable 1280 × 640 social-card source.",
        "- [`docs/launch/SOCIAL_PREVIEW.md`](docs/launch/SOCIAL_PREVIEW.md): preview requirements and upload procedure;\n- [`docs/launch/VIDEO_DEMO_SCRIPT.md`](docs/launch/VIDEO_DEMO_SCRIPT.md): 6–8 minute verified-workflow demonstration script;\n- [`docs/launch/PUBLISHING_CHECKLIST.md`](docs/launch/PUBLISHING_CHECKLIST.md): research, privacy, attribution, and platform publication gate;\n- [`docs/launch/FEEDBACK_PLAN.md`](docs/launch/FEEDBACK_PLAN.md): launch feedback triage, severity, and acceptance process;\n- [`assets/social-preview-source.svg`](assets/social-preview-source.svg): editable 1280 × 640 social-card source.",
        "README launch resources",
    )
    marker = "## Usage examples\n"
    section = '''## Support and feedback

Use the structured GitHub issue forms for:

- workflow or generated-surface errors;
- financial-data, period, unit, source, or calculation errors;
- installation, update, doctor, or uninstall failures;
- distinct workflow proposals with testable output contracts.

Read [`SUPPORT.md`](SUPPORT.md) before opening an issue. Do not post credentials, private paths, confidential documents, unpublished holdings, or requests for personalized investment advice. Potential vulnerabilities must follow [`SECURITY.md`](SECURITY.md).

'''
    text = replace_once(text, marker, section + marker, "README support section")
    text = replace_once(
        text,
        "- deterministic financial, audit, Taiwan-data, verified-example, and installer-safety tests;",
        "- deterministic financial, audit, Taiwan-data, verified-example, installer-safety, and community-template tests;",
        "README validation tests",
    )
    text = replace_once(
        text,
        "Read [CONTRIBUTING.md](CONTRIBUTING.md) before opening an issue or pull request.",
        "Read [SUPPORT.md](SUPPORT.md) before opening an issue and [CONTRIBUTING.md](CONTRIBUTING.md) before opening a pull request.",
        "README contributing links",
    )
    path.write_text(text, encoding="utf-8")


def patch_status() -> None:
    path = ROOT / "docs" / "ENGLISH_EDITION.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "| Public launch article and channel copy | Prepared in `docs/launch/` |",
        "| Public launch article and channel copy | Prepared in `docs/launch/` |\n| Video demonstration script and publishing gate | Prepared in `docs/launch/` |\n| Structured support and feedback intake | Four issue forms, `SUPPORT.md`, and launch triage plan |",
        "status launch rows",
    )
    text = replace_once(
        text,
        "- deterministic unit and example-report tests;",
        "- deterministic unit, example-report, installer, and community-template tests;",
        "status tests",
    )
    text = replace_once(
        text,
        "- [x] Add unified installation, update, diagnostics, and safe uninstall management.\n",
        "- [x] Add unified installation, update, diagnostics, and safe uninstall management.\n- [x] Add structured issue forms, support policy, feedback triage, video script, and publishing checklist.\n",
        "status milestone",
    )
    text = replace_once(
        text,
        "- [ ] Record and publish a video demonstration using a verified example.\n- [ ] Collect installation feedback from Claude Code and Codex users.",
        "- [ ] Record and publish the prepared video demonstration using a verified example.\n- [ ] Collect external installation feedback through the structured issue forms.",
        "status roadmap",
    )
    path.write_text(text, encoding="utf-8")


def patch_changelog() -> None:
    path = ROOT / "CHANGELOG.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "- Unified cross-platform installation management with manifests, backups, dry runs, drift diagnostics, updates, and safe uninstall behavior.\n",
        "- Unified cross-platform installation management with manifests, backups, dry runs, drift diagnostics, updates, and safe uninstall behavior.\n- Structured issue forms for workflow, financial-data, installation, and workflow-proposal feedback.\n- Support policy, launch feedback triage plan, verified-workflow video script, and public publishing checklist.\n",
        "changelog feedback",
    )
    path.write_text(text, encoding="utf-8")


def main() -> None:
    patch_readme()
    patch_status()
    patch_changelog()
    print("Updated launch and feedback documentation.")


if __name__ == "__main__":
    main()
