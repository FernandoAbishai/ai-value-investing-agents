from __future__ import annotations

import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CJK_RE = re.compile("[\u3040-\u30ff\u3400-\u4dbf\u4e00-\u9fff\uac00-\ud7af]")

CANONICAL_ROOT_FILES = (
    "README.md",
    "AGENTS.md",
    "CLAUDE.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "SUPPORT.md",
    "README_EN.md",
)

CANONICAL_DIRECTORIES = (
    ".github",
    "docs",
    "scripts",
    "skills",
    "codex-skills",
    "codex-prompts",
)

TEXT_SUFFIXES = {".md", ".py", ".sh", ".bat", ".yml", ".yaml", ".json", ".txt"}

# The canonical README intentionally exposes localized navigation labels.
ALLOWED_CJK_LINES = {
    "README.md": {
        "[English](README.md) · [中文](README_ZH.md) · [日本語](README_JA.md)",
    },
}


class EnglishFirstLanguagePolicyTests(unittest.TestCase):
    def iter_canonical_files(self):
        for name in CANONICAL_ROOT_FILES:
            path = ROOT / name
            if path.exists():
                yield path
        for directory in CANONICAL_DIRECTORIES:
            base = ROOT / directory
            if not base.exists():
                continue
            for path in base.rglob("*"):
                if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
                    yield path

    def filtered_text(self, path: Path) -> str:
        rel = path.relative_to(ROOT).as_posix()
        allowed = ALLOWED_CJK_LINES.get(rel, set())
        lines = path.read_text(encoding="utf-8").splitlines()
        return "\n".join(line for line in lines if line not in allowed)

    def test_canonical_maintained_surfaces_are_english_first(self):
        findings = []
        for path in self.iter_canonical_files():
            text = self.filtered_text(path)
            match = CJK_RE.search(text)
            if not match:
                continue
            line = text.count("\n", 0, match.start()) + 1
            rel = path.relative_to(ROOT).as_posix()
            excerpt = text[max(0, match.start() - 24):match.start() + 24].replace("\n", " ")
            findings.append(f"{rel}:{line} near {excerpt!r}")
        self.assertEqual([], findings, "Non-English text found in canonical maintained surfaces")

    def test_upstream_personal_memory_file_is_not_present(self):
        self.assertFalse((ROOT / "ai_CLAUDE.md").exists())


if __name__ == "__main__":
    unittest.main()
