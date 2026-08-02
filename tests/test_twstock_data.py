from __future__ import annotations

import io
import json
import os
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch
from urllib.parse import parse_qs, urlsplit

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import twstock_data as tw  # noqa: E402


class FakeResponse:
    def __init__(self, payload):
        self.payload = payload

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, tb):
        return False

    def read(self):
        return json.dumps(self.payload).encode("utf-8")


class TaiwanStockHelpersTests(unittest.TestCase):
    def test_fmt_yi_formats_large_small_and_invalid_values(self):
        self.assertEqual(tw._fmt_yi(250_000_000), "2.5亿")
        self.assertEqual(tw._fmt_yi(25_000), "2.5万")
        self.assertEqual(tw._fmt_yi(12.5), "12.50")
        self.assertEqual(tw._fmt_yi(None), "-")
        self.assertEqual(tw._fmt_yi("n/a"), "n/a")

    def test_token_prefers_environment_over_file(self):
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as handle:
            handle.write("file-token")
            token_path = handle.name
        try:
            with patch.object(tw, "_TOKEN_FILE", token_path), patch.dict(
                os.environ, {"FINMIND_TOKEN": "environment-token"}, clear=False
            ):
                self.assertEqual(tw._token(), "environment-token")
        finally:
            os.unlink(token_path)

    def test_token_falls_back_to_local_file(self):
        with tempfile.NamedTemporaryFile("w", delete=False, encoding="utf-8") as handle:
            handle.write("file-token\n")
            token_path = handle.name
        try:
            with patch.object(tw, "_TOKEN_FILE", token_path), patch.dict(
                os.environ, {}, clear=True
            ):
                self.assertEqual(tw._token(), "file-token")
        finally:
            os.unlink(token_path)

    def test_get_builds_expected_query_and_returns_data(self):
        captured = {}

        def fake_urlopen(request, timeout):
            captured["url"] = request.full_url
            captured["timeout"] = timeout
            return FakeResponse({"status": 200, "data": [{"close": 100}]})

        with patch.object(tw, "_token", return_value="token-value"), patch.object(
            tw.urllib.request, "urlopen", side_effect=fake_urlopen
        ):
            rows = tw._get(
                "TaiwanStockPrice",
                data_id="2330",
                start_date="2026-01-01",
                end_date="2026-01-31",
            )

        self.assertEqual(rows, [{"close": 100}])
        query = parse_qs(urlsplit(captured["url"]).query)
        self.assertEqual(query["dataset"], ["TaiwanStockPrice"])
        self.assertEqual(query["data_id"], ["2330"])
        self.assertEqual(query["start_date"], ["2026-01-01"])
        self.assertEqual(query["end_date"], ["2026-01-31"])
        self.assertEqual(query["token"], ["token-value"])
        self.assertEqual(captured["timeout"], tw._TIMEOUT)

    def test_get_rejects_unsuccessful_api_payload(self):
        with patch.object(tw, "_token", return_value=None), patch.object(
            tw.urllib.request,
            "urlopen",
            return_value=FakeResponse({"status": 500, "msg": "temporary failure"}),
        ):
            with self.assertRaisesRegex(ConnectionError, "temporary failure"):
                tw._get("TaiwanStockPrice", data_id="2330")


class TaiwanStockCommandTests(unittest.TestCase):
    def capture(self, func, *args):
        stream = io.StringIO()
        with redirect_stdout(stream):
            func(*args)
        return stream.getvalue()

    def test_financials_aggregates_quarters_and_calculates_margins(self):
        statement_rows = []
        quarter_dates = ["2025-03-31", "2025-06-30", "2025-09-30", "2025-12-31"]
        metrics = {
            "Revenue": 100,
            "GrossProfit": 40,
            "OperatingIncome": 20,
            "EquityAttributableToOwnersOfParent": 10,
            "EPS": 1,
        }
        for report_date in quarter_dates:
            for metric, value in metrics.items():
                statement_rows.append({"date": report_date, "type": metric, "value": value})
        balance_rows = [
            {
                "date": "2025-12-31",
                "type": "EquityAttributableToOwnersOfParent",
                "value": 400,
            }
        ]

        def fake_get(dataset, **kwargs):
            if dataset == "TaiwanStockFinancialStatements":
                return statement_rows
            if dataset == "TaiwanStockBalanceSheet":
                return balance_rows
            raise AssertionError(f"unexpected dataset: {dataset}")

        with patch.object(tw, "_stock_name", return_value=("Example Corp", "Listed")), patch.object(
            tw, "_get", side_effect=fake_get
        ):
            output = self.capture(tw.cmd_financials, "2330")

        self.assertIn("2025", output)
        self.assertIn("400.00", output)
        self.assertIn("40.0%", output)
        self.assertIn("20.0%", output)
        self.assertIn("10.0%", output)
        self.assertIn("4.00", output)

    def test_revenue_calculates_year_over_year_change(self):
        rows = [
            {"revenue_year": 2024, "revenue_month": 1, "revenue": 100},
            {"revenue_year": 2025, "revenue_month": 1, "revenue": 120},
        ]
        with patch.object(tw, "_stock_name", return_value=("Example Corp", "Listed")), patch.object(
            tw, "_get", return_value=rows
        ):
            output = self.capture(tw.cmd_revenue, "2330")
        self.assertIn("+20.0%", output)

    def test_search_deduplicates_stock_and_combines_industries(self):
        rows = [
            {"stock_id": "2330", "stock_name": "TSMC", "type": "twse", "industry_category": "Semiconductors"},
            {"stock_id": "2330", "stock_name": "TSMC", "type": "twse", "industry_category": "Technology"},
            {"stock_id": "2454", "stock_name": "MediaTek", "type": "twse", "industry_category": "Semiconductors"},
        ]
        with patch.object(tw, "_get", return_value=rows):
            output = self.capture(tw.cmd_search, "TSMC")
        self.assertEqual(output.count("2330 TSMC"), 1)
        self.assertIn("Semiconductors/Technology", output)
        self.assertNotIn("2454", output)

    def test_search_reports_no_match(self):
        with patch.object(tw, "_get", return_value=[]):
            output = self.capture(tw.cmd_search, "missing")
        self.assertIn("missing", output)


if __name__ == "__main__":
    unittest.main(verbosity=2)
