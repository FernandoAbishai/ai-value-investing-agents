#!/usr/bin/env python3
"""Deterministic repository-wide quality gates for active public surfaces."""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SELF_PATH = "scripts/repository_quality.py"
MAX_TEXT_SIZE = 2_000_000
TEXT_SUFFIXES = {
    ".bat", ".cfg", ".css", ".html", ".ini", ".js", ".json", ".md",
    ".py", ".sh", ".svg", ".toml", ".txt", ".yaml", ".yml",
}

ACTIVE_LEGACY_SCAN = (
    "AGENTS.md", "CLAUDE.md", "CONTRIBUTING.md", "SECURITY.md",
    ".github/", "scripts/", "skills/", "codex-skills/", "codex-prompts/",
)
PUBLIC_PATH_SCAN = (
    "AGENTS.md", "CLAUDE.md", "CHANGELOG.md", "CONTRIBUTING.md", "README.md",
    "README_ZH.md", "README_JA.md", "SECURITY.md", ".github/", "docs/",
    "scripts/", "skills/", "codex-skills/", "codex-prompts/",
)
OPERATIONAL_ENGLISH_PREFIXES = ("skills/", "codex-skills/", "codex-prompts/")
EXPECTED_SHARED_WORKFLOWS = 21

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)
CJK_RE = re.compile("[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]")

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{30,})\b"),
    "OpenAI secret": re.compile(r"\bsk-(?:proj-)?[A-Za-z0-9_-]{40,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b"),
    "Slack token": re.compile(r"\bxox[baprs]-[0-9A-Za-z-]{20,}\b"),
}
PRIVATE_PATH_PATTERNS = {
    "macOS user path": re.compile(r"/Users/(?!<|\$|\{|example(?:/|\b))[^/\s]+/"),
    "Linux user path": re.compile(r"/home/(?!runner(?:/|\b)|<|\$|\{|example(?:/|\b))[^/\s]+/"),
    "Windows user path": re.compile(
        r"[A-Za-z]:\\Users\\(?!%USERNAME%|<|\$|\{|example(?:\\|\b))[^\\\s]+\\",
        re.IGNORECASE,
    ),
}


@dataclass(frozen=True)
class Finding:
    check: str
    path: str
    line: int
    message: str

    def render(self) -> str:
        location = f"{self.path}:{self.line}" if self.line else self.path
        return f"[{self.check}] {location}: {self.message}"


def tracked_files() -> list[Path]:
    result = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, check=True, stdout=subprocess.PIPE
    )
    return [ROOT / value.decode("utf-8") for value in result.stdout.split(b"\0") if value]


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def read_text(path: Path) -> str | None:
    try:
        if path.stat().st_size > MAX_TEXT_SIZE:
            return None
        return path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def is_selected(path: str, selectors: tuple[str, ...]) -> bool:
    return any(path == selector or path.startswith(selector) for selector in selectors)


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def source_line(text: str, offset: int) -> str:
    start = text.rfind("\n", 0, offset) + 1
    end = text.find("\n", offset)
    return text[start:] if end == -1 else text[start:end]


def clean_markdown_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    match = re.match(r"^(\S+?)(?:\s+[\"'].*[\"'])?$", target)
    return match.group(1) if match else target


def is_template_target(target: str) -> bool:
    return any(token in target for token in ("{{", "}}", "${", "}", "<report-path>", "<verified"))


def validate_link(path: Path, target: str) -> str | None:
    target = unquote(target.strip())
    if not target or target.startswith("#") or is_template_target(target):
        return None
    split = urlsplit(target)
    if split.scheme in {"http", "https"}:
        return None if split.netloc and "." in split.netloc else f"malformed external URL: {target}"
    if split.scheme in {"mailto", "tel", "data"} or split.scheme:
        return None
    if not split.path:
        return None
    resolved = (ROOT / split.path.lstrip("/")) if split.path.startswith("/") else (path.parent / split.path)
    try:
        resolved = resolved.resolve(strict=False)
        resolved.relative_to(ROOT.resolve())
    except ValueError:
        return f"relative link escapes the repository: {target}"
    return None if resolved.exists() else f"missing local link target: {target}"


def check_markdown_links(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        rel = relative(path)
        if path.suffix.lower() != ".md" or rel.startswith("reports/"):
            continue
        text = read_text(path)
        if text is None:
            continue
        for match in list(MARKDOWN_LINK_RE.finditer(text)) + list(HTML_LINK_RE.finditer(text)):
            error = validate_link(path, clean_markdown_target(match.group(1)))
            if error:
                findings.append(Finding("links", rel, line_number(text, match.start()), error))
    return findings


def check_legacy_identity(files: list[Path]) -> list[Finding]:
    patterns = {
        "legacy checkout path": re.compile(r"~/ai-berkshire(?:/|\b)", re.IGNORECASE),
        "legacy maintained repository": re.compile(
            r"(?:github\.com/)?FernandoAbishai/ai-berkshire(?:\.git)?(?:/|\b)", re.IGNORECASE
        ),
        "legacy active project name": re.compile(r"\bAI Berkshire\b", re.IGNORECASE),
        "legacy generic repository name": re.compile(r"(?<!xbtlin/)\bai-berkshire\b", re.IGNORECASE),
    }
    findings: list[Finding] = []
    for path in files:
        rel = relative(path)
        if rel == SELF_PATH or not is_selected(rel, ACTIVE_LEGACY_SCAN):
            continue
        text = read_text(path)
        if text is None:
            continue
        for label, pattern in patterns.items():
            for match in pattern.finditer(text):
                findings.append(Finding("legacy", rel, line_number(text, match.start()), label))
    return findings


def check_private_paths(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        rel = relative(path)
        if rel == SELF_PATH or not is_selected(rel, PUBLIC_PATH_SCAN):
            continue
        text = read_text(path)
        if text is None:
            continue
        for label, pattern in PRIVATE_PATH_PATTERNS.items():
            for match in pattern.finditer(text):
                line = source_line(text, match.start())
                # Detection examples are allowed only when explicitly marked with placeholders.
                if "<local-username>" in line and "<private-identifier>" in line:
                    continue
                findings.append(Finding("privacy", rel, line_number(text, match.start()), label))
    return findings


def check_secrets(files: list[Path]) -> list[Finding]:
    """Scan maintained code/docs; historical report archives are intentionally excluded."""
    findings: list[Finding] = []
    for path in files:
        rel = relative(path)
        if rel == SELF_PATH or not is_selected(rel, PUBLIC_PATH_SCAN):
            continue
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"Dockerfile", "Makefile"}:
            continue
        text = read_text(path)
        if text is None:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append(Finding("secrets", rel, line_number(text, match.start()), label))
    return findings


def check_operational_english(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        rel = relative(path)
        if not rel.endswith(".md") or not is_selected(rel, OPERATIONAL_ENGLISH_PREFIXES):
            continue
        text = read_text(path)
        if text is None:
            continue
        match = CJK_RE.search(text)
        if match:
            excerpt = text[max(0, match.start() - 20) : match.start() + 20].replace("\n", " ")
            findings.append(
                Finding("language", rel, line_number(text, match.start()), f"non-English operational character near {excerpt!r}")
            )
    return findings


def check_required_identity(_: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    readme = read_text(ROOT / "README.md") or ""
    clone_url = "https://github.com/FernandoAbishai/ai-value-investing-agents.git"
    if clone_url not in readme:
        findings.append(Finding("identity", "README.md", 0, "missing maintained clone URL"))

    canonical = {path.stem for path in (ROOT / "skills").glob("*.md")}
    prompts = {path.stem for path in (ROOT / "codex-prompts").glob("*.md")}
    generated = {path.parent.name for path in (ROOT / "codex-skills").glob("*/SKILL.md")}
    if len(canonical) != EXPECTED_SHARED_WORKFLOWS:
        findings.append(
            Finding(
                "inventory",
                "skills/",
                0,
                f"expected {EXPECTED_SHARED_WORKFLOWS} workflows, found {len(canonical)}",
            )
        )
    if prompts != canonical:
        findings.append(Finding("inventory", "codex-prompts/", 0, f"prompt mismatch: {sorted(prompts ^ canonical)}"))
    codex_only = generated - canonical
    if not canonical <= generated or codex_only != {"investment-memo-craft"}:
        findings.append(
            Finding(
                "inventory", "codex-skills/", 0,
                f"shared or Codex-only mismatch: missing={sorted(canonical - generated)}, extra={sorted(codex_only)}",
            )
        )
    return findings


def main() -> int:
    files = tracked_files()
    checks = (
        check_markdown_links,
        check_legacy_identity,
        check_private_paths,
        check_secrets,
        check_operational_english,
        check_required_identity,
    )
    findings = [finding for check in checks for finding in check(files)]
    if findings:
        for finding in sorted(findings, key=lambda item: (item.check, item.path, item.line)):
            print(finding.render(), file=sys.stderr)
        print(f"Repository quality checks failed with {len(findings)} finding(s).", file=sys.stderr)
        return 1
    print(
        "Repository quality checks passed: local links, URL structure, identity, privacy, "
        "active-surface secrets, operational language, and workflow inventory."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
