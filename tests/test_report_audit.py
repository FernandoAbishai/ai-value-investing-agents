from __future__ import annotations

import io
import os
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import report_audit as audit  # noqa: E402


class NumberParsingTests(unittest.TestCase):
    def test_clean_num_normalizes_signs_and_separators(self):
        cases = {
            "-1.72": -1.72,
            "+3.5": 3.5,
            "−4.2": -4.2,
            "–5.1": -5.1,
            "－6.3": -6.3,
            "-1,234.5": -1234.5,
            "-1，234.5": -1234.5,
        }
        for raw, expected in cases.items():
            with self.subTest(raw=raw):
                self.assertEqual(audit._clean_num(raw), expected)
        self.assertIsNone(audit._clean_num("n/a"))

    def test_extracts_negative_values_without_flipping_sign(self):
        md = (
            "| Company | Price | Daily change | PB |\n"
            "|---|---:|---:|---:|\n"
            "| Example A | 27.40 | -1.72% | 1.03x |\n"
            "| Example B | 17.56 | -1.90% | 2.18x |\n"
            "| Example C | 12.78 | +1.11% | 1.79x |\n"
        )
        values = {point["reported_value"] for point in audit.extract_data_points(md)}
        self.assertIn(-1.72, values)
        self.assertIn(-1.90, values)
        self.assertIn(1.11, values)
        self.assertNotIn(1.72, values)

    def test_filters_huge_negative_value(self):
        md = (
            "| Metric | Value |\n"
            "|---|---:|\n"
            "| Invalid | -9999999999999999 |\n"
            "| Valid | -12.5 |\n"
        )
        values = {point["reported_value"] for point in audit.extract_data_points(md)}
        self.assertIn(-12.5, values)
        self.assertTrue(all(abs(value) < 1e15 for value in values))

    def test_code_blocks_are_not_parsed_as_kv_lines(self):
        md = "Revenue: 100 B\n\n```text\nFake metric: 999 B\n```\n"
        points = audit.extract_data_points(md)
        labels = {point["label"] for point in points}
        self.assertTrue(any("Revenue" in label for label in labels))
        self.assertFalse(any("Fake metric" in label for label in labels))

    def test_sampling_is_reproducible_and_bounded(self):
        points = [
            {"id": index, "line_number": index, "label": str(index), "reported_value": index, "unit": ""}
            for index in range(1, 101)
        ]
        first = audit.sample_points(points, ratio=0.15, seed=42)
        second = audit.sample_points(points, ratio=0.15, seed=42)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 15)
        self.assertEqual(first, sorted(first, key=lambda item: item["line_number"]))


class VerdictTests(unittest.TestCase):
    def render(self, results):
        stream = io.StringIO()
        with redirect_stdout(stream):
            outcome = audit.render_verdict(results, "fixture.md")
        return outcome, stream.getvalue()

    def item(self, **overrides):
        base = {
            "id": 1,
            "label": "Revenue",
            "reported_value": 100,
            "unit": "B",
            "line_number": 10,
            "raw_text": "Revenue: 100 B",
            "fetched_source": "filing",
        }
        base.update(overrides)
        return base

    def test_matching_single_source_passes(self):
        outcome, _ = self.render([self.item(fetched_value=100.5)])
        self.assertEqual(outcome["verdict"], "PASS")
        self.assertEqual(outcome["pass_count"], 1)

    def test_mismatching_single_source_fails(self):
        outcome, _ = self.render([self.item(fetched_value=120)])
        self.assertEqual(outcome["verdict"], "FAIL")
        self.assertEqual(outcome["fail_count"], 1)

    def test_no_verified_values_cannot_pass(self):
        outcome, output = self.render([self.item(fetched_value=None)])
        self.assertEqual(outcome["verdict"], "FAIL")
        self.assertEqual(outcome["unverified_count"], 1)
        self.assertIn("unverified", output.lower())

    def test_two_matching_sources_pass(self):
        outcome, _ = self.render(
            [
                self.item(
                    fetched_value=100,
                    fetched_value2=100.5,
                    fetched_source2="secondary",
                )
            ]
        )
        self.assertEqual(outcome["verdict"], "PASS")
        self.assertEqual(outcome["warn_count"], 0)

    def test_one_matching_and_one_mismatching_source_warns_but_passes(self):
        outcome, _ = self.render(
            [
                self.item(
                    fetched_value=100,
                    fetched_value2=120,
                    fetched_source2="secondary",
                )
            ]
        )
        self.assertEqual(outcome["verdict"], "PASS")
        self.assertEqual(outcome["warn_count"], 1)

    def test_both_mismatching_sources_fail(self):
        outcome, _ = self.render(
            [
                self.item(
                    fetched_value=120,
                    fetched_value2=125,
                    fetched_source2="secondary",
                )
            ]
        )
        self.assertEqual(outcome["verdict"], "FAIL")
        self.assertEqual(outcome["fail_count"], 1)

    def test_pct_diff_uses_absolute_reported_value(self):
        self.assertAlmostEqual(audit._pct_diff(-100, -110), 0.1)
        self.assertEqual(audit._pct_diff(0, 0), 0)
        self.assertEqual(audit._pct_diff(0, 1), float("inf"))


class ConsoleRegressionTests(unittest.TestCase):
    def test_extract_survives_gbk_console(self):
        md = (
            "# Test report\n\n"
            "| Company | Revenue | Margin |\n"
            "|---|---:|---:|\n"
            "| Example Corp | €11,297M | 26.1% |\n"
            "Rating: ★★☆☆☆ → Monitor\n"
        )
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as handle:
            handle.write(md)
            path = handle.name
        try:
            env = dict(os.environ)
            env["PYTHONIOENCODING"] = "gbk"
            env.pop("PYTHONUTF8", None)
            proc = subprocess.run(
                [sys.executable, str(TOOLS / "report_audit.py"), "extract", "--report", path, "--seed", "1"],
                capture_output=True,
                env=env,
                check=False,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr.decode("utf-8", "replace"))
            self.assertNotIn(b"UnicodeEncodeError", proc.stderr)
        finally:
            os.unlink(path)

    def test_force_utf8_is_idempotent_and_tolerates_binary_stream(self):
        audit._force_utf8_stdio()
        audit._force_utf8_stdio()
        original = sys.stdout
        try:
            sys.stdout = io.BytesIO()
            audit._force_utf8_stdio()
        finally:
            sys.stdout = original


if __name__ == "__main__":
    unittest.main(verbosity=2)
