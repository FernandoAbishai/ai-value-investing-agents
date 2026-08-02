from __future__ import annotations

import io
import json
import sys
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLES = ROOT / "reports" / "examples"
sys.path.insert(0, str(ROOT / "tools"))

import report_audit  # noqa: E402


REPORTS = {
    "microsoft-fy2026-company-research-20260802.md",
    "microsoft-fy2026-q4-earnings-review-20260802.md",
    "cloud-infrastructure-comparison-20260802.md",
}

REQUIRED_MARKERS = (
    "**Status:** Verified example",
    "**Research cutoff:**",
    "**Workflow demonstrated:**",
    "## Audit statement",
    "## Limitations",
    "## Disclaimer",
)


class VerifiedExampleReportTests(unittest.TestCase):
    def test_expected_report_set_exists(self):
        for name in REPORTS:
            with self.subTest(report=name):
                self.assertTrue((EXAMPLES / name).is_file())

    def test_reports_contain_required_metadata_and_controls(self):
        for name in REPORTS:
            with self.subTest(report=name):
                text = (EXAMPLES / name).read_text(encoding="utf-8")
                for marker in REQUIRED_MARKERS:
                    self.assertIn(marker, text)
                self.assertIn("2026-08-02", text)
                self.assertIn("not", text.lower())
                self.assertIn("advice", text.lower())
                self.assertNotIn("Status:** Draft", text)

    def test_verification_register_references_every_report(self):
        register = (EXAMPLES / "VERIFICATION.md").read_text(encoding="utf-8")
        for name in REPORTS:
            self.assertIn(name, (EXAMPLES / "README.md").read_text(encoding="utf-8"))
        for source_id in ("MSFT-IR", "AMZN-IR", "GOOGL-IR", "ORCL-IR"):
            self.assertIn(source_id, register)

    def test_all_audit_fixtures_pass(self):
        fixtures = sorted((EXAMPLES / "audit").glob("*.json"))
        self.assertEqual(len(fixtures), 3)
        for fixture in fixtures:
            with self.subTest(fixture=fixture.name):
                results = json.loads(fixture.read_text(encoding="utf-8"))
                self.assertGreaterEqual(len(results), 8)
                stream = io.StringIO()
                with redirect_stdout(stream):
                    outcome = report_audit.render_verdict(results, report_name=fixture.name)
                self.assertEqual(outcome["verdict"], "PASS", stream.getvalue())
                self.assertEqual(outcome["unverified_count"], 0)
                self.assertEqual(outcome["fail_count"], 0)

    def test_cloud_report_preserves_definition_warning(self):
        text = (EXAMPLES / "cloud-infrastructure-comparison-20260802.md").read_text(
            encoding="utf-8"
        )
        self.assertIn("No honest single revenue ranking", text)
        self.assertIn("periods are not synchronized", text)
        self.assertIn("Microsoft Cloud", text)
        self.assertIn("Azure and other cloud services", text)
        self.assertIn("Intelligent Cloud", text)


if __name__ == "__main__":
    unittest.main(verbosity=2)
