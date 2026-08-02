from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_DIR = ROOT / ".github" / "ISSUE_TEMPLATE"
FORM_NAMES = {
    "workflow-error.yml",
    "financial-data-error.yml",
    "installation-problem.yml",
    "workflow-proposal.yml",
}


class CommunityTemplateTests(unittest.TestCase):
    def test_structured_issue_forms_exist(self):
        for name in FORM_NAMES:
            with self.subTest(form=name):
                self.assertTrue((TEMPLATE_DIR / name).is_file())

    def test_forms_have_required_top_level_fields_and_body(self):
        for name in FORM_NAMES:
            with self.subTest(form=name):
                text = (TEMPLATE_DIR / name).read_text(encoding="utf-8")
                self.assertRegex(text, r"(?m)^name: .+$")
                self.assertRegex(text, r"(?m)^description: .+$")
                self.assertRegex(text, r'(?m)^title: "\[[^]]+\]: "$')
                self.assertRegex(text, r"(?m)^body:$")
                self.assertGreaterEqual(text.count("  - type:"), 5)
                self.assertIn("validations:\n      required: true", text)

    def test_form_ids_are_unique_and_lowercase(self):
        for name in FORM_NAMES:
            with self.subTest(form=name):
                text = (TEMPLATE_DIR / name).read_text(encoding="utf-8")
                ids = re.findall(r"(?m)^    id: ([a-z][a-z0-9_]*)$", text)
                self.assertGreaterEqual(len(ids), 4)
                self.assertEqual(len(ids), len(set(ids)))

    def test_forms_include_privacy_or_security_guard(self):
        for name in FORM_NAMES:
            with self.subTest(form=name):
                text = (TEMPLATE_DIR / name).read_text(encoding="utf-8").lower()
                self.assertTrue(
                    any(term in text for term in ("credential", "private path", "confidential")),
                    f"{name} lacks a privacy or security reminder",
                )

    def test_installation_form_requests_reproducible_environment(self):
        text = (TEMPLATE_DIR / "installation-problem.yml").read_text(encoding="utf-8")
        for identifier in ("operating_system", "os_version", "python", "operation", "command", "output"):
            self.assertIn(f"id: {identifier}", text)
        self.assertIn("doctor --all", text)

    def test_financial_form_requires_period_units_and_sources(self):
        text = (TEMPLATE_DIR / "financial-data-error.yml").read_text(encoding="utf-8")
        self.assertIn("Reporting period and cutoff", text)
        self.assertIn("currency, unit, formula", text)
        self.assertIn("primary-source links", text)
        self.assertIn("not a request for personalized investment advice", text)

    def test_issue_config_disables_blank_issues_and_links_security(self):
        text = (TEMPLATE_DIR / "config.yml").read_text(encoding="utf-8")
        self.assertIn("blank_issues_enabled: false", text)
        self.assertIn("/security/policy", text)
        self.assertIn("docs/INSTALLATION.md", text)
        self.assertIn("reports/examples", text)

    def test_support_and_launch_documents_exist(self):
        required = (
            ROOT / "SUPPORT.md",
            ROOT / "docs" / "launch" / "VIDEO_DEMO_SCRIPT.md",
            ROOT / "docs" / "launch" / "PUBLISHING_CHECKLIST.md",
            ROOT / "docs" / "launch" / "FEEDBACK_PLAN.md",
        )
        for path in required:
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertTrue(path.is_file())

    def test_launch_documents_preserve_research_safety_boundaries(self):
        combined = "\n".join(
            path.read_text(encoding="utf-8")
            for path in (
                ROOT / "docs" / "launch" / "VIDEO_DEMO_SCRIPT.md",
                ROOT / "docs" / "launch" / "PUBLISHING_CHECKLIST.md",
                ROOT / "docs" / "launch" / "FEEDBACK_PLAN.md",
            )
        ).lower()
        for phrase in (
            "research cutoff",
            "personalized investment advice",
            "credentials",
            "primary source",
            "verified example",
        ):
            self.assertIn(phrase, combined)


if __name__ == "__main__":
    unittest.main(verbosity=2)
