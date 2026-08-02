#!/usr/bin/env python3
"""Repository-wide quality gates for active source and documentation files.

The checks are deliberately deterministic and avoid network requests so they can
run reliably on Linux, macOS, and Windows CI runners.
"""

from __future__ import annotations

import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
MAX_TEXT_SIZE = 2_000_000
TEXT_SUFFIXES = {
    ".bat",
    ".cfg",
    ".css",
    ".html",
    ".ini",
    ".js",
    ".json",
    ".md",
    ".py",
    ".sh",
    ".svg",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}

ACTIVE_LEGACY_SCAN = (
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".github/",
    "scripts/",
    "skills/",
    "codex-skills/",
    "codex-prompts/",
)

PUBLIC_PATH_SCAN = (
    "AGENTS.md",
    "CLAUDE.md",
    "CONTRIBUTING.md",
    "README.md",
    "README_ZH.md",
    "README_JA.md",
    "SECURITY.md",
    ".github/",
    "docs/",
    "scripts/",
    "skills/",
    "codex-skills/",
    "codex-prompts/",
)

OPERATIONAL_ENGLISH_PREFIXES = ("skills/", "codex-skills/", "codex-prompts/")

MARKDOWN_LINK_RE = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
HTML_LINK_RE = re.compile(r"(?:href|src)\s*=\s*[\"']([^\"']+)[\"']", re.IGNORECASE)
CJK_RE = re.compile(
    "["
    "\u3040-\u30ff"  # Japanese kana
    "\u3400-\u4dbf"  # CJK extension A
    "\u4e00-\u9fff"  # CJK unified ideographs
    "\uac00-\ud7af"  # Hangul syllables
    "]"
)

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\b(?:github_pat_[A-Za-z0-9_]{20,}|gh[pousr]_[A-Za-z0-9]{30,})\b"),
    "OpenAI-style secret": re.compile(r"\bsk-[A-Za-z0-9_-]{30,}\b"),
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
        ["git", "ls-files", "-z"],
        cwd=ROOT,
        check=True,
        stdout=subprocess.PIPE,
    )
    return [ROOT / item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


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


def clean_markdown_target(raw: str) -> str:
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        return target[1 : target.index(">")]
    # Strip an optional Markdown title after an unquoted URL.
    title_match = re.match(r"^(\S+?)(?:\s+[\"'].*[\"'])?$", target)
    return title_match.group(1) if title_match else target


def is_template_target(target: str) -> bool:
    return any(token in target for token in ("{{", "}}", "${", "}", "<report-path>", "<verified"))


def validate_link(path: Path, target: str) -> str | None:
    target = unquote(target.strip())
    if not target or target.startswith("#") or is_template_target(target):
        return None

    split = urlsplit(target)
    if split.scheme in {"http", "https"}:
        if not split.netloc or "." not in split.netloc:
            return f"malformed external URL: {target}"
        return None
    if split.scheme in {"mailto", "tel", "data"}:
        return None
    if split.scheme:
        return None

    link_path = split.path
    if not link_path:
        return None
    resolved = (ROOT / link_path.lstrip("/")) if link_path.startswith("/") else (path.parent / link_path)
    try:
        resolved = resolved.resolve(strict=False)
        resolved.relative_to(ROOT.resolve())
    except ValueError:
        return f"relative link escapes the repository: {target}"

    if not resolved.exists():
        return f"missing local link target: {target}"
    return None


def check_markdown_links(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        if path.suffix.lower() != ".md" or relative(path).startswith("reports/"):
            continue
        text = read_text(path)
        if text is None:
            continue
        matches = list(MARKDOWN_LINK_RE.finditer(text)) + list(HTML_LINK_RE.finditer(text))
        for match in matches:
            target = clean_markdown_target(match.group(1))
            error = validate_link(path, target)
            if error:
                findings.append(
                    Finding("links", relative(path), line_number(text, match.start()), error)
                )
    return findings


def check_legacy_identity(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    patterns = {
        "legacy checkout path": re.compile(r"~/ai-berkshire(?:/|\b)", re.IGNORECASE),
        "legacy maintained repository": re.compile(
            r"(?:github\.com/)?FernandoAbishai/ai-berkshire(?:\.git)?(?:/|\b)", re.IGNORECASE
        ),
        "legacy active project name": re.compile(r"\bAI Berkshire\b", re.IGNORECASE),
        "legacy generic repository name": re.compile(r"(?<!xbtlin/)\bai-berkshire\b", re.IGNORECASE),
    }
    for path in files:
        rel = relative(path)
        if not is_selected(rel, ACTIVE_LEGACY_SCAN):
            continue
        text = read_text(path)
        if text is None:
            continue
        for label, pattern in patterns.items():
            for match in pattern.finditer(text):
                findings.append(
                    Finding("legacy", rel, line_number(text, match.start()), label)
                )
    return findings


def check_private_paths(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        rel = relative(path)
        if not is_selected(rel, PUBLIC_PATH_SCAN):
            continue
        text = read_text(path)
        if text is None:
            continue
        for label, pattern in PRIVATE_PATH_PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append(
                    Finding("privacy", rel, line_number(text, match.start()), label)
                )
    return findings


def check_secrets(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    for path in files:
        if path.suffix.lower() not in TEXT_SUFFIXES and path.name not in {"Dockerfile", "Makefile"}:
            continue
        text = read_text(path)
        if text is None:
            continue
        for label, pattern in SECRET_PATTERNS.items():
            for match in pattern.finditer(text):
                findings.append(
                    Finding("secrets", relative(path), line_number(text, match.start()), label)
                )
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
                Finding(
                    "language",
                    rel,
                    line_number(text, match.start()),
                    f"non-English operational character near {excerpt!r}",
                )
            )
    return findings


def check_required_identity(files: list[Path]) -> list[Finding]:
    findings: list[Finding] = []
    readme = ROOT / "README.md"
    text = read_text(readme) or ""
    required = "https://github.com/FernandoAbishai/ai-value-investing-agents.git"
    if required not in text:
        findings.append(Finding("identity", "README.md", 0, "missing maintained clone URL"))

    canonical = {path.stem for path in (ROOT / "skills").glob("*.md")}
    prompts = {path.stem for path in (ROOT / "codex-prompts").glob("*.md")}
    generated = {path.parent.name for path in (ROOT / "codex-skills").glob("*/SKILL.md")}
    if len(canonical) != 20:
        findings.append(Finding("inventory", "skills/", 0, f"expected 20 workflows, found {len(canonical)}"))
    if prompts != canonical:
        findings.append(Finding("inventory", "codex-prompts/", 0, f"prompt mismatch: {sorted(prompts ^ canonical)}"))
    codex_only = generated - canonical
    if not canonical <= generated or codex_only != {"investment-memo-craft"}:
        findings.append(
            Finding(
                "inventory",
                "codex-skills/",
                0,
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
    findings: list[Finding] = []
    for check in checks:
        findings.extend(check(files))

    if findings:
        for finding in sorted(findings, key=lambda item: (item.check, item.path, item.line)):
            print(finding.render(), file=sys.stderr)
        print(f"Repository quality checks failed with {len(findings)} finding(s).", file=sys.stderr)
        return 1

    print(
        "Repository quality checks passed: local links, URL structure, identity, privacy, "
        "high-confidence secrets, operational language, and workflow inventory."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
