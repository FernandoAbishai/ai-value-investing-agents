#!/usr/bin/env python3
"""Generate human- and machine-readable indexes for tracked research reports.

This is an English-first adaptation of the report-index layer added upstream in
xbtlin/ai-berkshire. It intentionally indexes only report files that are
actually present in Git's index. Untracked drafts, ignored files, and
intent-to-add placeholders are excluded so local work cannot leak into public
navigation.

Outputs:
  reports/index.json  machine-readable report inventory
  reports/README.md   human-readable GitHub report index

Metadata priority:
  YAML front matter > filename > report body > latest Git commit date

Usage:
  python3 tools/reports_index.py
  python3 tools/reports_index.py --check
"""

from __future__ import annotations

import json
import os
import re
import subprocess
import sys
from collections import OrderedDict, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = os.path.join(ROOT, "reports")
CONFIG = os.path.join(REPORTS, "_index", "config.json")

DATE_IN_NAME = re.compile(r"(20[2-3]\d)(0[1-9]|1[0-2])(0[1-9]|[12]\d|3[01])")
DATE_IN_BODY = re.compile(r"(20[2-3]\d)[-/年](\d{1,2})[-/月](\d{1,2})")
H1 = re.compile(r"^#\s+(.+?)\s*$")

# Rules are ordered: the first matching category wins. Chinese keywords remain
# because the historical archive is intentionally preserved in its source
# language even though maintained operational surfaces are English-first.
TYPE_RULES = [
    ("working paper", ["研究底稿", "审计", "核验", "复核", "评审", "check", "verify", "底稿", "对账"]),
    ("earnings", ["earnings", "财报", "中报", "年报", "季报", "业绩", "电话会", "q1", "q2", "q3", "q4"]),
    ("publication", ["公众号", "wechat", "推文"]),
    ("deep series", ["看懂", "深度研究", "deep-dive", "深度投研"]),
    ("comparison", ["横评", "对比", "vs", "对决", "pk", "换仓", "轮动"]),
    ("management", ["7s", "管理层", "组织", "management"]),
    ("valuation", ["估值", "赔率", "凯利", "仓位", "valuation", "fair_value", "终值"]),
    ("screen", ["funnel", "筛选", "召回", "screen", "候选池"]),
]


def _force_utf8_stdio() -> None:
    """Keep Unicode archive paths safe on Windows consoles and captured pipes."""
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, OSError, ValueError):
            pass


def load_config() -> dict:
    with open(CONFIG, encoding="utf-8") as handle:
        return json.load(handle)


def git_report_paths() -> set[str]:
    """Return report paths whose contents are actually represented in Git's index."""
    try:
        raw = subprocess.check_output(
            ["git", "ls-files", "--cached", "-z", "--", "reports/"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        )
        # `git add -N` creates an index entry without staging the file contents.
        intent_to_add = subprocess.check_output(
            ["git", "diff", "--name-only", "--diff-filter=A", "-z", "--", "reports/"],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        raise RuntimeError(
            "Unable to read the Git index; report-index generation stopped to avoid publishing local-only files."
        ) from exc

    paths = {os.fsdecode(path) for path in raw.split(b"\0") if path}
    intent_paths = {os.fsdecode(path) for path in intent_to_add.split(b"\0") if path}
    return paths - intent_paths


def git_dates() -> dict[str, str]:
    """Return the latest commit date for each path in one Git-history pass."""
    dates: dict[str, str] = {}
    try:
        raw = subprocess.check_output(
            [
                "git",
                "-c",
                "core.quotePath=false",
                "log",
                "--pretty=format:__D__%ad",
                "--date=short",
                "--name-only",
            ],
            cwd=ROOT,
            stderr=subprocess.DEVNULL,
        ).decode("utf-8", "replace")
    except (OSError, subprocess.CalledProcessError):
        return dates

    current_date: str | None = None
    for line in raw.splitlines():
        if line.startswith("__D__"):
            current_date = line[5:].strip()
        elif line.strip() and current_date and line not in dates:
            dates[line] = current_date
    return dates


def parse_front_matter(lines: list[str]) -> tuple[dict[str, str], int]:
    """Parse the small key:value subset of YAML needed by the report index."""
    if not lines or lines[0].strip() != "---":
        return {}, 0
    metadata: dict[str, str] = {}
    for index, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            return metadata, index + 1
        if ":" in line:
            key, value = line.split(":", 1)
            metadata[key.strip().lower()] = value.strip().strip("\"'")
    return {}, 0


def read_head(path: str, count: int = 40) -> list[str]:
    try:
        with open(path, encoding="utf-8", errors="replace") as handle:
            lines = []
            for _ in range(count):
                line = handle.readline()
                if not line:
                    break
                lines.append(line.rstrip("\n"))
            return lines
    except OSError:
        return []


def guess_type(name: str, relpath: str) -> str:
    haystack = (name + " " + relpath).lower()
    for label, keywords in TYPE_RULES:
        if any(keyword in haystack for keyword in keywords):
            return label
    return "research"


def guess_date(
    metadata: dict[str, str],
    filename: str,
    parent: str,
    head: list[str],
    gitmap: dict[str, str],
    relpath: str,
) -> tuple[str, str]:
    if metadata.get("date"):
        date = metadata["date"].replace("/", "-")
        if re.match(r"^20\d\d-\d\d-\d\d$", date):
            return date, "front-matter"

    for source in (filename, parent):
        match = DATE_IN_NAME.search(source)
        if match:
            return "%s-%s-%s" % match.groups(), "filename"

    for line in head[:15]:
        match = DATE_IN_BODY.search(line)
        if match:
            year, month, day = match.groups()
            return "%s-%02d-%02d" % (year, int(month), int(day)), "body"

    if relpath in gitmap:
        return gitmap[relpath], "git"
    return "", "missing"


def bucket_of(top: str, config: dict) -> tuple[str, str]:
    top = config["aliases"].get(top, top)
    if top in config["screens"]:
        return "screen", top
    if top in config["themes"]:
        return "theme", top
    if top in config["masters"]:
        return "master", top
    if top in config["other"]:
        return "other", top
    return "company", top


def collect(config: dict, gitmap: dict[str, str]):
    items = []
    unknown_dirs: set[str] = set()
    tracked = git_report_paths()
    excluded: list[str] = []
    known = (
        set(config["themes"])
        | set(config["masters"])
        | set(config["screens"])
        | set(config["other"])
        | set(config.get("companies", []))
    )

    for dirpath, dirnames, filenames in os.walk(REPORTS):
        dirnames[:] = [name for name in dirnames if name not in config["skip_dirs"]]
        for filename in filenames:
            if not filename.endswith(".md") or filename in config["skip_files"]:
                continue

            full = os.path.join(dirpath, filename)
            rel = os.path.relpath(full, ROOT).replace(os.sep, "/")
            if rel not in tracked:
                excluded.append(rel)
                continue

            report_rel = os.path.relpath(full, REPORTS).replace(os.sep, "/")
            parts = report_rel.split("/")
            top = parts[0] if len(parts) > 1 else ""
            head = read_head(full)
            metadata, _ = parse_front_matter(head)

            title = metadata.get("title", "")
            if not title:
                for line in head:
                    match = H1.match(line)
                    if match:
                        title = match.group(1)
                        break
            if not title:
                title = re.sub(r"-?\d{8}$", "", filename[:-3])
            title = re.sub(r"[*`]", "", title).strip()

            if top:
                bucket, group = bucket_of(top, config)
                if bucket == "company" and top not in known and top not in config["aliases"]:
                    unknown_dirs.add(top)
            else:
                bucket, group = "theme", "Cross-company"

            date, date_source = guess_date(
                metadata,
                filename,
                parts[-2] if len(parts) > 1 else "",
                head,
                gitmap,
                rel,
            )
            series = parts[1] if len(parts) > 2 else ""
            report_type = metadata.get("type") or guess_type(filename, report_rel)
            items.append(
                OrderedDict(
                    [
                        ("title", title),
                        ("path", rel),
                        ("bucket", bucket),
                        ("group", group),
                        ("series", series),
                        ("type", report_type),
                        ("date", date),
                        ("date_source", date_source),
                        ("ticker", config["tickers"].get(group, "")),
                    ]
                )
            )

    items.sort(key=lambda item: (item["date"], item["path"]), reverse=True)
    return items, sorted(unknown_dirs), sorted(excluded)


def display_name(name: str) -> str:
    return re.sub(r"-20[2-3]\d[01]\d[0-3]\d$", "", name) or name


UNSAFE = {
    "%": "%25",
    " ": "%20",
    "(": "%28",
    ")": "%29",
    "#": "%23",
    "?": "%3F",
    "[": "%5B",
    "]": "%5D",
    "<": "%3C",
    ">": "%3E",
    '"': "%22",
}


def url_path(path: str) -> str:
    """Escape characters that can break Markdown links while preserving Unicode names."""
    return "".join(UNSAFE.get(character, character) for character in path)


def md_link(text: str, path: str) -> str:
    safe_text = text.replace("[", "〔").replace("]", "〕").replace("|", "丨")
    return "[%s](%s)" % (safe_text, url_path(path.replace("reports/", "", 1)))


def render(items: list[dict], config: dict) -> str:
    del config  # Classification is already represented in items.
    by_bucket = defaultdict(lambda: defaultdict(list))
    for item in items:
        by_bucket[item["bucket"]][item["group"]].append(item)

    latest = max((item["date"] for item in items if item["date"]), default="")
    lines = [
        "# Research Report Index",
        "",
        "> Generated by `tools/reports_index.py`; do not edit this file manually.",
        "> Stage a new report with `git add` before regenerating the index, then commit the report and generated index together.",
        "",
        "**%d reports** · **%d companies** · **%d themes** · latest %s"
        % (len(items), len(by_bucket["company"]), len(by_bucket["theme"]), latest or "—"),
        "",
        "[Recent](#recent) · [Companies](#companies) · [Themes](#themes) · [Investors and thinkers](#investors-and-thinkers) · [Screening pools](#screening-pools)",
        "",
        "---",
        "",
        "## Recent",
        "",
        "| Date | Report | Group | Type |",
        "|---|---|---|---|",
    ]

    seen = defaultdict(int)
    shown = []
    for item in items:
        if item["bucket"] == "screen" or item["type"] == "working paper":
            continue
        key = item["group"] + "/" + (item["series"] or "")
        if seen[key] >= 3:
            continue
        seen[key] += 1
        shown.append(item)
        if len(shown) >= 40:
            break

    for item in shown:
        lines.append(
            "| %s | %s | %s | %s |"
            % (
                item["date"] or "—",
                md_link(item["title"], item["path"]),
                display_name(item["group"]),
                item["type"],
            )
        )
    lines.extend(["", "---", ""])

    def section(title: str, bucket: str, note: str = "") -> None:
        groups = by_bucket.get(bucket, {})
        if not groups:
            return
        lines.extend([f"## {title}", ""])
        if note:
            lines.extend([note, ""])
        order = sorted(groups.items(), key=lambda pair: (-len(pair[1]), pair[0]))
        for name, group_items in order:
            group_items = sorted(
                group_items,
                key=lambda item: (item["date"], item["title"]),
                reverse=True,
            )
            last = group_items[0]["date"] or "—"
            lines.append("<details>")
            lines.append(
                "<summary><b>%s</b> · %d reports · latest %s</summary>"
                % (display_name(name), len(group_items), last)
            )
            lines.append("")
            current_series = None
            for item in group_items:
                if item["series"] and item["series"] != current_series:
                    current_series = item["series"]
                    lines.extend(["", "*%s*" % display_name(current_series), ""])
                elif not item["series"] and current_series is not None:
                    current_series = None
                    lines.append("")
                lines.append(
                    "- `%s` %s — %s"
                    % (item["date"] or "  —  ", md_link(item["title"], item["path"]), item["type"])
                )
            lines.extend(["", "</details>", ""])
        lines.extend(["---", ""])

    section("Companies", "company")
    section("Themes", "theme")
    section("Investors and thinkers", "master")

    screens = by_bucket.get("screen", {})
    if screens:
        lines.extend(
            [
                "## Screening pools",
                "",
                "> These are intermediate screening or scenario artifacts, not finished research reports.",
                "",
                "| Pool | Files | Latest |",
                "|---|---:|---|",
            ]
        )
        for name, group_items in sorted(screens.items(), key=lambda pair: -len(pair[1])):
            last = max((item["date"] for item in group_items if item["date"]), default="—")
            lines.append(
                "| [%s](%s) | %d | %s |"
                % (display_name(name), url_path(name), len(group_items), last)
            )
        lines.append("")

    return "\n".join(lines) + "\n"


ROOT_README = os.path.join(ROOT, "README.md")
MARK_START = "<!-- REPORTS-INDEX:START generated by tools/reports_index.py -->"
MARK_END = "<!-- REPORTS-INDEX:END -->"
BANNER_START = "<!-- REPORTS-BANNER:START generated by tools/reports_index.py -->"
BANNER_END = "<!-- REPORTS-BANNER:END -->"


def index_stats(items: list[dict]) -> tuple[int, int, int, str]:
    groups = defaultdict(set)
    for item in items:
        if item["bucket"] != "screen":
            groups[item["bucket"]].add(item["group"])
    latest = max((item["date"] for item in items if item["date"]), default="—")
    return len(items), len(groups["company"]), len(groups["theme"]), latest


def root_banner_block(items: list[dict]) -> str:
    total, companies, themes, latest = index_stats(items)
    return "\n".join(
        [
            BANNER_START,
            "",
            "> **Research archive:** [browse the generated report index](reports/README.md). "
            "%d reports · %d companies · %d themes · latest %s."
            % (total, companies, themes, latest),
            "",
            BANNER_END,
        ]
    )


def root_readme_block(items: list[dict]) -> str:
    total, companies, themes, latest = index_stats(items)
    fresh = [
        item
        for item in items
        if item["bucket"] != "screen" and item["type"] != "working paper"
    ][:8]

    lines = [MARK_START, ""]
    lines.append(
        "**[Browse all research →](reports/README.md)** · %d reports · %d companies · %d themes · latest %s"
        % (total, companies, themes, latest)
    )
    lines.extend(["", "Recent:", "", "| Date | Report | Group |", "|---|---|---|"])
    seen = defaultdict(int)
    rows = 0
    for item in fresh:
        if seen[item["group"]] >= 2:
            continue
        seen[item["group"]] += 1
        rows += 1
        title = item["title"].replace("[", "〔").replace("]", "〕").replace("|", "丨")
        lines.append(
            "| %s | [%s](%s) | %s |"
            % (item["date"] or "—", title, url_path(item["path"]), display_name(item["group"]))
        )
        if rows >= 6:
            break
    lines.extend(["", MARK_END])
    return "\n".join(lines)


def update_root_readme(items: list[dict]) -> tuple[str | None, str | None]:
    if not os.path.exists(ROOT_README):
        return None, None
    with open(ROOT_README, encoding="utf-8") as handle:
        old = handle.read()
    new = old
    for start, end, builder in (
        (BANNER_START, BANNER_END, root_banner_block),
        (MARK_START, MARK_END, root_readme_block),
    ):
        if start in new and end in new:
            head = new.split(start, 1)[0]
            tail = new.split(end, 1)[1]
            new = head + builder(items) + tail
    return old, new


def main() -> int:
    _force_utf8_stdio()
    check = "--check" in sys.argv
    config = load_config()
    try:
        items, unknown, excluded = collect(config, git_dates())
    except RuntimeError as exc:
        print(str(exc), file=sys.stderr)
        return 1

    index_path = os.path.join(REPORTS, "index.json")
    readme_path = os.path.join(REPORTS, "README.md")
    payload = json.dumps({"count": len(items), "reports": items}, ensure_ascii=False, indent=2) + "\n"
    readme = render(items, config)
    root_old, root_new = update_root_readme(items)

    if check:
        stale = []
        pairs = [(index_path, payload), (readme_path, readme)]
        if root_old is not None:
            pairs.append((ROOT_README, root_new))
        for path, expected in pairs:
            current = ""
            if os.path.exists(path):
                with open(path, encoding="utf-8") as handle:
                    current = handle.read()
            if current != expected:
                stale.append(os.path.relpath(path, ROOT).replace(os.sep, "/"))
        if stale:
            print(
                "Report index is stale; run `python3 tools/reports_index.py`: " + ", ".join(stale)
            )
            return 1
        print("Report index is current.")
        return 0

    with open(index_path, "w", encoding="utf-8") as handle:
        handle.write(payload)
    with open(readme_path, "w", encoding="utf-8") as handle:
        handle.write(readme)
    if root_new is not None and root_new != root_old:
        with open(ROOT_README, "w", encoding="utf-8") as handle:
            handle.write(root_new)
        print("Updated the root README report-index block.")

    missing = [item for item in items if not item["date"]]
    print("Indexed %d reports -> reports/README.md and reports/index.json" % len(items))
    if missing:
        print("  Missing a usable date: %d reports" % len(missing))
    if excluded:
        print(
            "  Excluded %d local-only report files; stage intended public reports before regenerating."
            % len(excluded)
        )
    if unknown:
        print(
            "  New directories not listed in config.json companies (treated as companies): %s"
            % ", ".join(unknown)
        )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
