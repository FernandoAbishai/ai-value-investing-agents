#!/usr/bin/env python3
"""Apply narrowly scoped financial-tool fixes before running regression tests.

This file is temporary and must be removed before the pull request is merged.
"""

from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


def patch_financial_rigor() -> None:
    path = ROOT / "tools" / "financial_rigor.py"
    text = path.read_text(encoding="utf-8")

    if "import ast\n" not in text:
        text = replace_once(text, "import argparse\n", "import argparse\nimport ast\n", "add ast import")

    old_sources = '''    values = {k: exact(v) for k, v in source_values.items()}
    sources = list(values.keys())
    nums = list(values.values())

    # Find median as reference
    sorted_vals = sorted(float(v) for v in nums)
    n = len(sorted_vals)
    median = sorted_vals[n // 2] if n % 2 == 1 else (sorted_vals[n//2-1] + sorted_vals[n//2]) / 2
'''
    new_sources = '''    if not source_values:
        raise ValueError("source_values must contain at least one source")

    values = {k: exact(v) for k, v in source_values.items()}
    sources = list(values.keys())
    nums = list(values.values())

    # Use an exact Decimal median so negative and fractional values remain auditable.
    sorted_vals = sorted(nums)
    n = len(sorted_vals)
    median_decimal = (
        sorted_vals[n // 2]
        if n % 2 == 1
        else _CTX.divide(
            _CTX.add(sorted_vals[n // 2 - 1], sorted_vals[n // 2]),
            Decimal("2"),
        )
    )
    median = float(median_decimal)
'''
    if old_sources in text:
        text = replace_once(text, old_sources, new_sources, "cross-validation median")

    old_deviation = "        dev = abs(float(val) - median) / median * 100 if median != 0 else 0\n"
    new_deviation = '''        dev = (
            abs(float(val) - median) / abs(median) * 100
            if median != 0
            else (0 if val == 0 else float("inf"))
        )
'''
    if old_deviation in text:
        text = replace_once(text, old_deviation, new_deviation, "cross-validation deviation")

    start_marker = "def exact_calc(expr: str):\n"
    end_marker = "\n\n# ---------------------------------------------------------------------------\n# 6. Three-Scenario Valuation"
    if "def _eval_decimal_node" not in text:
        start = text.index(start_marker)
        end = text.index(end_marker, start)
        replacement = '''_BINARY_DECIMAL_OPERATIONS = {
    ast.Add: _CTX.add,
    ast.Sub: _CTX.subtract,
    ast.Mult: _CTX.multiply,
    ast.Div: _CTX.divide,
}


def _eval_decimal_node(node) -> Decimal:
    """Evaluate a restricted arithmetic AST using Decimal operations only."""
    if isinstance(node, ast.Expression):
        return _eval_decimal_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return Decimal(str(node.value))
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, (ast.UAdd, ast.USub)):
        value = _eval_decimal_node(node.operand)
        return value if isinstance(node.op, ast.UAdd) else -value
    if isinstance(node, ast.BinOp) and type(node.op) in _BINARY_DECIMAL_OPERATIONS:
        operation = _BINARY_DECIMAL_OPERATIONS[type(node.op)]
        return operation(_eval_decimal_node(node.left), _eval_decimal_node(node.right))
    raise ValueError("expression contains unsupported syntax")


def exact_calc(expr: str):
    """Evaluate +, -, *, /, unary signs, and parentheses with Decimal arithmetic."""
    print("=" * 60)
    print("精确计算 (Exact Calculator)")
    print("=" * 60)

    try:
        tree = ast.parse(expr, mode="eval")
        d_result = _eval_decimal_node(tree)
        print(f"  表达式: {expr}")
        print(f"  结果:   {fmt_number(d_result)}")
        print(f"  精确值: {d_result}")
        return float(d_result)
    except (SyntaxError, ValueError, InvalidOperation, ZeroDivisionError) as error:
        print(f"  ❌ Unsupported or invalid expression: {error}")
        return None
'''
        text = text[:start] + replacement + text[end:]

    path.write_text(text, encoding="utf-8")


def patch_report_audit() -> None:
    path = ROOT / "tools" / "report_audit.py"
    text = path.read_text(encoding="utf-8")

    if "unverified_items = []" not in text:
        text = replace_once(
            text,
            "    fail_items = []\n    warn_items = []\n",
            "    fail_items = []\n    warn_items = []\n    unverified_items = []\n",
            "initialize unverified results",
        )

    old_missing = '''        if fetched is None:
            # 没有提供核验值 → 跳过（不计入通过/失败）
            print(f'  ⬜ [{item["id"]:>2}] {label[:35]:35s} {reported:>12.2f} {unit}  →  [未提供核验值，跳过]')
            continue
'''
    new_missing = '''        if fetched is None:
            unverified_items.append({
                'id': item.get('id'),
                'label': label,
                'reported': reported,
                'unit': unit,
                'line_number': item.get('line_number', 0),
            })
            print(f'  ⬜ [{item["id"]:>2}] {label[:35]:35s} {reported:>12.2f} {unit}  →  [unverified: no fetched value]')
            continue
'''
    if old_missing in text:
        text = replace_once(text, old_missing, new_missing, "track unverified results")

    text = text.replace(
        "        pass2 = (diff2 is None) or (diff2 <= _TOLERANCE)\n",
        "        pass2 = None if diff2 is None else (diff2 <= _TOLERANCE)\n",
        1,
    )
    text = text.replace(
        "        if pass1 and pass2:\n",
        "        if pass1 and (pass2 is None or pass2):\n",
        1,
    )
    text = text.replace(
        "        elif not pass1 and not pass2:\n",
        "        elif (not pass1) and (pass2 is None or not pass2):\n",
        1,
    )

    old_counts = '''    total = len([r for r in results if r.get('fetched_value') is not None])
    fail_count = len(fail_items)
    warn_count = len(warn_items)
    pass_count = total - fail_count - warn_count

    print(f'  抽检总数: {total}  |  通过: {GREEN}{pass_count}{RESET}  |  警告: {YELLOW}{warn_count}{RESET}  |  不通过: {RED}{fail_count}{RESET}')
'''
    new_counts = '''    total = len([r for r in results if r.get('fetched_value') is not None])
    fail_count = len(fail_items)
    warn_count = len(warn_items)
    unverified_count = len(unverified_items)
    pass_count = total - fail_count - warn_count

    print(f'  已核验: {total}  |  通过: {GREEN}{pass_count}{RESET}  |  警告: {YELLOW}{warn_count}{RESET}  |  不通过: {RED}{fail_count}{RESET}  |  Unverified: {unverified_count}')
'''
    if old_counts in text:
        text = replace_once(text, old_counts, new_counts, "verdict counts")

    start = text.index("    if fail_count == 0:\n")
    end = text.index("\n    if warn_count > 0:", start)
    new_verdict = '''    if fail_count == 0 and unverified_count == 0:
        print(f'{BOLD}{GREEN}【准出】所有抽检数据通过，报告可发布。{RESET}')
        verdict = 'PASS'
    else:
        issue_count = fail_count + unverified_count
        print(f'{BOLD}{RED}【打回】{issue_count} 个数据点失败或未核验，报告需修正后重审。{RESET}')
        if fail_items:
            print()
            print(f'{BOLD}打回原因：{RESET}')
            for fi in fail_items:
                print(f'  ❌ 第 {fi["line_number"]} 行 | {fi["label"]}')
                print(f'     报告值：{fi["reported"]} {fi["unit"]}')
                print(f'     {fi["source"]}：{fi["fetched"]}  （偏差 {fi["diff1_pct"]}%）')
                if fi.get('fetched2') is not None:
                    print(f'     {fi["source2"]}：{fi["fetched2"]}  （偏差 {fi["diff2_pct"]}%）')
                print(f'     原文：{fi["raw_text"][:80]}')
                print()
        if unverified_items:
            print(f'{BOLD}Unverified items：{RESET}')
            for item in unverified_items:
                print(f'  ⬜ 第 {item["line_number"]} 行 | {item["label"]} — no fetched value')
        verdict = 'FAIL'
'''
    text = text[:start] + new_verdict + text[end:]

    old_return = '''        'warn_count': warn_count,
        'fail_count': fail_count,
        'total': total,
        'fail_items': fail_items,
        'warn_items': warn_items,
'''
    new_return = '''        'warn_count': warn_count,
        'fail_count': fail_count,
        'unverified_count': unverified_count,
        'total': total,
        'fail_items': fail_items,
        'warn_items': warn_items,
        'unverified_items': unverified_items,
'''
    if old_return in text:
        text = replace_once(text, old_return, new_return, "return unverified details")

    path.write_text(text, encoding="utf-8")


def main() -> None:
    patch_financial_rigor()
    patch_report_audit()
    print("Applied financial-tool correctness fixes.")


if __name__ == "__main__":
    main()
