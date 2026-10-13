#!/usr/bin/env python3
"""Unified market-data entry point for local market adapters.

This module gives maintained workflows one stable command surface while preserving
existing market-specific tools for backward compatibility.

Examples:
    python3 tools/market_data.py capabilities
    python3 tools/market_data.py --market cn quote 600519
    python3 tools/market_data.py --market tw financials 2330
    python3 tools/market_data.py --market taiwan revenue 2330 --format json

The first version intentionally delegates to the proven market-specific adapters
instead of rewriting their retrieval logic. The JSON format is a stable envelope
around the adapter's legacy text output; future versions can add structured fields
without breaking the text interface or the existing tools.
"""

from __future__ import annotations

import argparse
import importlib
import io
import json
import sys
from contextlib import redirect_stdout
from dataclasses import asdict, dataclass
from typing import Iterable


SCHEMA_VERSION = 1


@dataclass(frozen=True)
class MarketSpec:
    key: str
    name: str
    aliases: tuple[str, ...]
    currency: str
    adapter_module: str
    commands: tuple[str, ...]
    sources: tuple[str, ...]


MARKETS: tuple[MarketSpec, ...] = (
    MarketSpec(
        key="cn-a",
        name="Mainland China A-Shares",
        aliases=("cn", "china", "a-share", "ashare", "cn-a"),
        currency="CNY",
        adapter_module="ashare_data",
        commands=("quote", "valuation", "financials", "search"),
        sources=("Tencent Market Data", "Eastmoney"),
    ),
    MarketSpec(
        key="tw",
        name="Taiwan Stocks",
        aliases=("tw", "taiwan", "twse", "tpex"),
        currency="TWD",
        adapter_module="twstock_data",
        commands=("quote", "valuation", "financials", "revenue", "dividend", "search"),
        sources=("FinMind",),
    ),
)

_ALIAS_MAP = {
    alias.casefold(): spec
    for spec in MARKETS
    for alias in (spec.key, *spec.aliases)
}


def resolve_market(value: str) -> MarketSpec:
    """Resolve a market key or alias to its canonical adapter specification."""
    try:
        return _ALIAS_MAP[value.strip().casefold()]
    except KeyError as exc:
        supported = ", ".join(spec.key for spec in MARKETS)
        raise ValueError(f"Unsupported market {value!r}. Supported markets: {supported}") from exc


def capabilities() -> list[dict[str, object]]:
    """Return deterministic metadata for all installed local market adapters."""
    return [
        {
            "market": spec.key,
            "name": spec.name,
            "aliases": list(spec.aliases),
            "currency": spec.currency,
            "adapter": spec.adapter_module,
            "commands": list(spec.commands),
            "sources": list(spec.sources),
        }
        for spec in MARKETS
    ]


def _load_module(spec: MarketSpec):
    """Lazily import a trusted adapter from the local tools directory."""
    return importlib.import_module(spec.adapter_module)


def _command_function(spec: MarketSpec, command: str):
    if command not in spec.commands:
        available = ", ".join(spec.commands)
        raise ValueError(
            f"Command {command!r} is not supported for {spec.key}. "
            f"Available commands: {available}"
        )

    module = _load_module(spec)
    func = getattr(module, f"cmd_{command}", None)
    if func is None or not callable(func):
        raise RuntimeError(
            f"Adapter {spec.adapter_module!r} does not expose cmd_{command}()"
        )
    return func


def run(market: str, command: str, query: str, *, output_format: str = "text"):
    """Run one market-data command through the selected local adapter.

    ``text`` delegates directly to the existing adapter and therefore preserves
    backward-compatible output. ``json`` captures that output inside a stable
    metadata envelope that agents and automation can consume consistently.
    """
    spec = resolve_market(market)
    func = _command_function(spec, command)

    if output_format == "text":
        return func(query)
    if output_format != "json":
        raise ValueError("output_format must be 'text' or 'json'")

    buffer = io.StringIO()
    with redirect_stdout(buffer):
        func(query)

    envelope = {
        "schema_version": SCHEMA_VERSION,
        "market": spec.key,
        "market_name": spec.name,
        "currency": spec.currency,
        "command": command,
        "query": query,
        "adapter": spec.adapter_module,
        "sources": list(spec.sources),
        "result_text": buffer.getvalue().rstrip("\n"),
    }
    return envelope


def _print_capabilities(output_format: str) -> None:
    data = capabilities()
    if output_format == "json":
        print(json.dumps({"schema_version": SCHEMA_VERSION, "markets": data}, ensure_ascii=False, indent=2))
        return

    for item in data:
        aliases = ", ".join(item["aliases"])
        commands = ", ".join(item["commands"])
        sources = ", ".join(item["sources"])
        print(f"{item['market']}: {item['name']} ({item['currency']})")
        print(f"  aliases: {aliases}")
        print(f"  commands: {commands}")
        print(f"  adapter: {item['adapter']}")
        print(f"  sources: {sources}")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Unified entry point for installed market-data adapters",
    )
    parser.add_argument(
        "command",
        choices=("capabilities", "quote", "valuation", "financials", "revenue", "dividend", "search"),
        help="Operation to run",
    )
    parser.add_argument("query", nargs="?", help="Ticker, stock code, or search keyword")
    parser.add_argument(
        "--market",
        help="Market key or alias, such as cn, cn-a, tw, or taiwan",
    )
    parser.add_argument(
        "--format",
        dest="output_format",
        choices=("text", "json"),
        default="text",
        help="Output format (default: text)",
    )
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    if args.command == "capabilities":
        if args.market or args.query:
            parser.error("capabilities does not accept --market or a query")
        _print_capabilities(args.output_format)
        return 0

    if not args.market:
        parser.error(f"{args.command} requires --market")
    if not args.query:
        parser.error(f"{args.command} requires a ticker, stock code, or search keyword")

    try:
        result = run(
            args.market,
            args.command,
            args.query,
            output_format=args.output_format,
        )
    except (ConnectionError, RuntimeError, ValueError) as exc:
        print(f"market-data error: {exc}", file=sys.stderr)
        return 2

    if args.output_format == "json":
        print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
