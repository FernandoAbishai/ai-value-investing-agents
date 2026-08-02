from __future__ import annotations

import io
import os
import subprocess
import sys
import unittest
from contextlib import redirect_stdout
from decimal import Decimal
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(TOOLS))

import financial_rigor as rigor  # noqa: E402


def run_cli(args: list[str], encoding: str = "gbk") -> subprocess.CompletedProcess:
    env = dict(os.environ)
    env["PYTHONIOENCODING"] = encoding
    env.pop("PYTHONUTF8", None)
    return subprocess.run(
        [sys.executable, str(TOOLS / "financial_rigor.py"), *args],
        capture_output=True,
        env=env,
        check=False,
    )


class FinancialRigorTests(unittest.TestCase):
    def capture(self, func, *args, **kwargs):
        stream = io.StringIO()
        with redirect_stdout(stream):
            result = func(*args, **kwargs)
        return result, stream.getvalue()

    def test_exact_preserves_decimal_text_for_float(self):
        self.assertEqual(rigor.exact(0.1), Decimal("0.1"))

    def test_market_cap_accepts_match_and_rejects_large_gap(self):
        passed, _ = self.capture(rigor.verify_market_cap, 10, 100, 1000, "USD")
        failed, _ = self.capture(rigor.verify_market_cap, 10, 100, 800, "USD")
        self.assertTrue(passed)
        self.assertFalse(failed)

    def test_verify_valuation_returns_expected_ratios(self):
        result, _ = self.capture(
            rigor.verify_valuation,
            100,
            eps=5,
            bvps=20,
            fcf_per_share=4,
            dividend=2,
            revenue_per_share=25,
        )
        self.assertEqual(
            result,
            {
                "PE": 20.0,
                "PB": 5.0,
                "ROE": 25.0,
                "P_FCF": 25.0,
                "FCF_Yield": 4.0,
                "Dividend_Yield": 2.0,
                "PS": 4.0,
            },
        )

    def test_cross_validate_flags_negative_outlier(self):
        result, _ = self.capture(
            rigor.cross_validate,
            "net income",
            {"filing": -100, "source_b": -100, "source_c": -150},
            tolerance_pct=2,
        )
        self.assertFalse(result["all_consistent"])
        self.assertEqual(result["consensus"], -100.0)

    def test_cross_validate_rejects_empty_sources(self):
        with self.assertRaises(ValueError):
            self.capture(rigor.cross_validate, "revenue", {})

    def test_exact_calc_uses_decimal_arithmetic(self):
        result, _ = self.capture(rigor.exact_calc, "0.1 + 0.2")
        self.assertEqual(result, 0.3)

    def test_exact_calc_supports_parentheses_and_scientific_notation(self):
        result, _ = self.capture(rigor.exact_calc, "(2.5e3 - 500) / 4")
        self.assertEqual(result, 500.0)

    def test_exact_calc_rejects_unsupported_operator(self):
        result, output = self.capture(rigor.exact_calc, "2 ** 8")
        self.assertIsNone(result)
        self.assertIn("unsupported", output.lower())

    def test_exact_calc_rejects_names_and_calls(self):
        result, _ = self.capture(rigor.exact_calc, "__import__('os')")
        self.assertIsNone(result)

    def test_benford_requires_meaningful_sample_size(self):
        result, _ = self.capture(rigor.benford_check, list(range(1, 20)))
        self.assertIsNone(result)


class Utf8ConsoleRegressionTests(unittest.TestCase):
    def test_pass_warning_and_failure_paths_survive_gbk(self):
        cases = [
            ["verify-market-cap", "--price", "8", "--shares", "500000000", "--reported", "4000000000", "--currency", "CNY"],
            ["verify-market-cap", "--price", "8", "--shares", "500000000", "--reported", "4120000000", "--currency", "CNY"],
            ["verify-market-cap", "--price", "8", "--shares", "500000000", "--reported", "40", "--currency", "CNY"],
        ]
        for args in cases:
            with self.subTest(args=args):
                proc = run_cli(args)
                self.assertEqual(proc.returncode, 0, proc.stderr.decode("utf-8", "replace"))
                self.assertNotIn(b"UnicodeEncodeError", proc.stderr)

    def test_cross_validate_and_scenarios_survive_gbk(self):
        cases = [
            ["cross-validate", "--field", "revenue", "--values", '{"filing":1234,"source":1234}', "--unit", "CNY"],
            ["three-scenario", "--price", "8", "--eps", "0.5", "--shares", "5", "--growth", "0.15", "0.03", "-0.10", "--pe", "22", "15", "10", "--years", "3", "--currency", "CNY"],
        ]
        for args in cases:
            with self.subTest(args=args):
                proc = run_cli(args)
                self.assertEqual(proc.returncode, 0, proc.stderr.decode("utf-8", "replace"))
                self.assertNotIn(b"UnicodeEncodeError", proc.stderr)

    def test_force_utf8_is_idempotent_and_tolerates_binary_stream(self):
        rigor._force_utf8_stdio()
        rigor._force_utf8_stdio()
        original = sys.stdout
        try:
            sys.stdout = io.BytesIO()
            rigor._force_utf8_stdio()
        finally:
            sys.stdout = original


if __name__ == "__main__":
    unittest.main(verbosity=2)
