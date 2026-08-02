#!/usr/bin/env python3
"""Apply documentation updates for the verified English example set.

Temporary migration helper; remove before merge.
"""

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
        "| End-to-end demonstration | [`docs/QUICKSTART_DEMO.md`](docs/QUICKSTART_DEMO.md) |\n| Public launch kit |",
        "| End-to-end demonstration | [`docs/QUICKSTART_DEMO.md`](docs/QUICKSTART_DEMO.md) |\n| Verified English examples | [`reports/examples/`](reports/examples/) |\n| Public launch kit |",
        "README status row",
    )
    marker = "## Public launch resources\n"
    section = '''## Verified English examples

The curated [`reports/examples/`](reports/examples/) collection demonstrates the repository's research and audit controls with point-in-time public evidence:

- [`microsoft-fy2026-company-research-20260802.md`](reports/examples/microsoft-fy2026-company-research-20260802.md): full company research, cash conversion, valuation, and scenario analysis;
- [`microsoft-fy2026-q4-earnings-review-20260802.md`](reports/examples/microsoft-fy2026-q4-earnings-review-20260802.md): earnings quality, segment changes, capital intensity, and monitoring signals;
- [`cloud-infrastructure-comparison-20260802.md`](reports/examples/cloud-infrastructure-comparison-20260802.md): definition-aware comparison of Microsoft, AWS, Google Cloud, and Oracle;
- [`VERIFICATION.md`](reports/examples/VERIFICATION.md): source and calculation register.

The examples are newly prepared research artifacts, not mechanical translations of the historical archive. CI requires their metadata and selected audit fixtures to remain valid.

'''
    text = replace_once(text, marker, section + marker, "README example section")
    text = replace_once(
        text,
        "reports/                    Historical and community research output",
        "reports/                    Verified examples plus historical and community research output",
        "README architecture",
    )
    old_validation = '''```bash
python3 scripts/sync-codex-skills.py --check
python3 scripts/sync-codex-prompts.py --check
python3 -m compileall -q scripts tools
```
'''
    new_validation = '''```bash
python3 scripts/repository_quality.py
python3 scripts/sync-codex-skills.py --check
python3 scripts/sync-codex-prompts.py --check
python3 -m compileall -q scripts tools tests
python3 -m unittest discover -s tests -v
```
'''
    text = replace_once(text, old_validation, new_validation, "README validation commands")
    text = replace_once(
        text,
        "The permanent GitHub Actions workflow additionally checks:\n\n- 20 canonical shared workflows;",
        "The permanent GitHub Actions workflow additionally checks:\n\n- repository links, maintained identity, private paths, high-confidence secrets, and operational-language drift;\n- deterministic financial, audit, Taiwan-data, and verified-example tests;\n- 20 canonical shared workflows;",
        "README validation bullets",
    )
    path.write_text(text, encoding="utf-8")


def patch_status() -> None:
    path = ROOT / "docs" / "ENGLISH_EDITION.md"
    text = path.read_text(encoding="utf-8")
    text = replace_once(
        text,
        "| GitHub social-preview metadata | Manual image upload still required in repository settings |",
        "| GitHub social-preview metadata | Uploaded by the maintainer |",
        "status social preview",
    )
    text = replace_once(
        text,
        "| Curated newly verified English reports | Planned after v1.0.0 |",
        "| Curated newly verified English reports | Three published under `reports/examples/` with executable audit fixtures |",
        "status examples",
    )
    text = replace_once(
        text,
        "- generator `--check` modes;\n- Python compilation;",
        "- generator `--check` modes;\n- repository quality gates for links, identity, privacy, secrets, and operational language;\n- deterministic unit and example-report tests;\n- Python compilation;",
        "status validation",
    )
    text = replace_once(
        text,
        "- [x] Prepare an editable 1280 × 640 social-preview source.\n",
        "- [x] Prepare an editable 1280 × 640 social-preview source.\n- [x] Upload the GitHub social preview.\n- [x] Add repository-wide quality gates.\n- [x] Add deterministic financial and audit-tool tests.\n- [x] Publish a curated set of three verified English example reports.\n",
        "completed milestones",
    )
    old_roadmap = '''- [ ] Upload the prepared PNG in GitHub **Settings → Social preview**.
- [ ] Publish the launch article and selected social posts.
- [ ] Record and publish a video demonstration.
- [ ] Add a small curated set of newly verified English research reports.
- [ ] Add link checking and stale-repository-reference validation.
- [ ] Expand tool-level tests for financial and report-audit utilities.
- [ ] Collect installation feedback from Claude Code and Codex users.
'''
    new_roadmap = '''- [ ] Add a unified installer, updater, uninstaller, and diagnostics command.
- [ ] Publish the launch article and selected social posts.
- [ ] Record and publish a video demonstration using a verified example.
- [ ] Collect installation feedback from Claude Code and Codex users.
- [ ] Expand verified examples to additional markets and accounting regimes.
- [ ] Add deeper property-based and CLI error-path tests where useful.
'''
    text = replace_once(text, old_roadmap, new_roadmap, "post-release roadmap")
    path.write_text(text, encoding="utf-8")


def patch_changelog() -> None:
    path = ROOT / "CHANGELOG.md"
    text = path.read_text(encoding="utf-8")
    marker = "## [1.0.0] — 2026-08-02\n"
    section = '''## Unreleased

### Added

- Repository-wide quality gates for links, project identity, private paths, high-confidence secrets, operational language, and workflow inventory.
- Deterministic cross-platform tests for financial calculations, report auditing, Taiwan-stock transformations, and verified example reports.
- Three point-in-time verified English research examples under `reports/examples/` with source registers and executable audit fixtures.

### Fixed

- Replaced float-based expression evaluation with restricted Decimal arithmetic.
- Corrected cross-source comparison behavior for negative values and empty source sets.
- Prevented report audits from passing unverified data or a mismatching single source.

'''
    text = replace_once(text, marker, section + marker, "changelog unreleased section")
    path.write_text(text, encoding="utf-8")


def main() -> None:
    patch_readme()
    patch_status()
    patch_changelog()
    print("Updated documentation for verified English examples.")


if __name__ == "__main__":
    main()
