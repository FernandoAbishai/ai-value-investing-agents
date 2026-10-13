from __future__ import annotations

import io
import json
import sys
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "tools"))

import market_data as md  # noqa: E402


class MarketResolutionTests(unittest.TestCase):
    def test_resolve_market_accepts_common_aliases(self):
        self.assertEqual(md.resolve_market("cn").key, "cn-a")
        self.assertEqual(md.resolve_market("A-SHARE").key, "cn-a")
        self.assertEqual(md.resolve_market("taiwan").key, "tw")
        self.assertEqual(md.resolve_market("TWSE").key, "tw")

    def test_unknown_market_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "Unsupported market"):
            md.resolve_market("us")

    def test_capabilities_expose_stable_adapter_metadata(self):
        capabilities = md.capabilities()
        self.assertEqual([item["market"] for item in capabilities], ["cn-a", "tw"])
        self.assertEqual(capabilities[0]["currency"], "CNY")
        self.assertIn("financials", capabilities[0]["commands"])
        self.assertEqual(capabilities[1]["currency"], "TWD")
        self.assertIn("revenue", capabilities[1]["commands"])

    def test_registered_adapters_expose_every_declared_command(self):
        for spec in md.MARKETS:
            with self.subTest(market=spec.key):
                module = md._load_module(spec)
                for command in spec.commands:
                    self.assertTrue(
                        callable(getattr(module, f"cmd_{command}", None)),
                        f"{spec.adapter_module} is missing cmd_{command}()",
                    )


class MarketDispatchTests(unittest.TestCase):
    def test_text_mode_delegates_without_reformatting(self):
        seen = []

        def fake_quote(query):
            seen.append(query)
            print(f"legacy quote: {query}")

        fake_module = SimpleNamespace(cmd_quote=fake_quote)
        stream = io.StringIO()
        with patch.object(md, "_load_module", return_value=fake_module), patch("sys.stdout", stream):
            result = md.run("cn", "quote", "600519")

        self.assertIsNone(result)
        self.assertEqual(seen, ["600519"])
        self.assertEqual(stream.getvalue(), "legacy quote: 600519\n")

    def test_json_mode_wraps_legacy_output_with_normalized_metadata(self):
        def fake_financials(query):
            print(f"financials for {query}")

        fake_module = SimpleNamespace(cmd_financials=fake_financials)
        with patch.object(md, "_load_module", return_value=fake_module):
            result = md.run("taiwan", "financials", "2330", output_format="json")

        self.assertEqual(result["schema_version"], 1)
        self.assertEqual(result["market"], "tw")
        self.assertEqual(result["currency"], "TWD")
        self.assertEqual(result["command"], "financials")
        self.assertEqual(result["query"], "2330")
        self.assertEqual(result["adapter"], "twstock_data")
        self.assertEqual(result["sources"], ["FinMind"])
        self.assertEqual(result["result_text"], "financials for 2330")

    def test_market_specific_command_is_rejected_before_adapter_load(self):
        with patch.object(md, "_load_module") as load_module:
            with self.assertRaisesRegex(ValueError, "not supported"):
                md.run("cn", "revenue", "600519")
        load_module.assert_not_called()

    def test_invalid_output_format_is_rejected(self):
        fake_module = SimpleNamespace(cmd_quote=lambda query: None)
        with patch.object(md, "_load_module", return_value=fake_module):
            with self.assertRaisesRegex(ValueError, "output_format"):
                md.run("cn", "quote", "600519", output_format="xml")


class MarketCliTests(unittest.TestCase):
    def test_capabilities_json_requires_no_network_adapter_import(self):
        stream = io.StringIO()
        with patch.object(md, "_load_module") as load_module, patch("sys.stdout", stream):
            code = md.main(["capabilities", "--format", "json"])

        self.assertEqual(code, 0)
        load_module.assert_not_called()
        payload = json.loads(stream.getvalue())
        self.assertEqual(payload["schema_version"], 1)
        self.assertEqual([item["market"] for item in payload["markets"]], ["cn-a", "tw"])

    def test_cli_json_prints_dispatch_envelope(self):
        fake_module = SimpleNamespace(cmd_quote=lambda query: print(f"quote {query}"))
        stream = io.StringIO()
        with patch.object(md, "_load_module", return_value=fake_module), patch("sys.stdout", stream):
            code = md.main(["quote", "600519", "--market", "cn", "--format", "json"])

        self.assertEqual(code, 0)
        payload = json.loads(stream.getvalue())
        self.assertEqual(payload["market"], "cn-a")
        self.assertEqual(payload["result_text"], "quote 600519")


if __name__ == "__main__":
    unittest.main(verbosity=2)
