#!/usr/bin/env python3
"""Regression tests for the report index's public/private Git boundary."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class ReportsIndexTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.repo = Path(self.temp.name)
        (self.repo / "tools").mkdir()
        (self.repo / "reports/_index").mkdir(parents=True)
        shutil.copy(ROOT / "tools/reports_index.py", self.repo / "tools/reports_index.py")
        shutil.copy(ROOT / "reports/_index/config.json", self.repo / "reports/_index/config.json")
        self.write("README.md", "# Test index\n")
        self.write("reports/茅台/中文 历史报告.md", "# Historical report\n")
        self.git("init", "-q")
        self.git("config", "core.quotePath", "true")
        self.git("add", ".")
        self.git(
            "-c",
            "user.name=Index Test",
            "-c",
            "user.email=index@example.invalid",
            "commit",
            "-qm",
            "baseline",
        )

    def git(self, *args):
        env = dict(
            os.environ,
            GIT_AUTHOR_DATE="2026-09-30T12:00:00+08:00",
            GIT_COMMITTER_DATE="2026-09-30T12:00:00+08:00",
        )
        return subprocess.run(
            ["git", *args],
            cwd=self.repo,
            env=env,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            check=True,
        )

    def write(self, name, content):
        path = self.repo / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")

    def run_index(self, *args, expected=0):
        result = subprocess.run(
            [sys.executable, "tools/reports_index.py", *args],
            cwd=self.repo,
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
        )
        self.assertEqual(result.returncode, expected, result.stdout + result.stderr)
        return result

    def items(self):
        payload = json.loads((self.repo / "reports/index.json").read_text(encoding="utf-8"))
        return payload["reports"]

    def test_local_drafts_ignored_files_and_intent_to_add_are_not_published(self):
        self.write(".gitignore", "reports/私有/\n")
        for path in (
            "reports/七公司投资研究-20261002/茅台/报告-20261002.md",
            "reports/私有/报告.md",
            "reports/仅占位/报告.md",
        ):
            self.write(path, "# Local unpublished title\n")
        self.git("add", "-N", "reports/仅占位/报告.md")

        output = self.run_index().stdout
        self.assertEqual(
            [item["path"] for item in self.items()],
            ["reports/茅台/中文 历史报告.md"],
        )
        generated = (self.repo / "reports/README.md").read_text(encoding="utf-8")
        self.assertNotIn("Local unpublished title", generated)
        self.assertNotIn("七公司投资研究", output)
        self.run_index("--check")

    def test_staged_report_is_included_and_unstaging_invalidates_index(self):
        path = "reports/七公司投资研究-20261002/茅台/报告-20261002.md"
        self.write(path, "# New report\n")
        self.git("add", "--", path)
        self.run_index()
        self.assertIn(path, [item["path"] for item in self.items()])
        self.run_index("--check")

        self.git("reset", "-q", "HEAD", "--", path)
        before = (self.repo / "reports/index.json").read_bytes()
        self.run_index("--check", expected=1)
        self.assertEqual(before, (self.repo / "reports/index.json").read_bytes())
        self.run_index()
        self.assertNotIn(path, [item["path"] for item in self.items()])

    def test_removing_report_from_git_excludes_remaining_working_copy(self):
        self.run_index()
        path = "reports/茅台/中文 历史报告.md"
        self.git("rm", "--cached", "--", path)
        self.assertTrue((self.repo / path).is_file())
        self.run_index("--check", expected=1)
        self.run_index()
        self.assertEqual(self.items(), [])

    def test_git_failure_does_not_overwrite_published_index(self):
        self.run_index()
        before = (self.repo / "reports/index.json").read_bytes()
        git_dir = self.repo / ".git"
        disabled_git_dir = self.repo / ".git-disabled"
        git_dir.rename(disabled_git_dir)
        try:
            result = self.run_index(expected=1)
            self.assertIn("Unable to read the Git index", result.stderr)
            self.assertEqual(before, (self.repo / "reports/index.json").read_bytes())
        finally:
            disabled_git_dir.rename(git_dir)

    def test_unicode_path_git_date_is_independent_of_quote_path_config(self):
        self.run_index()
        self.assertEqual(self.items()[0]["date"], "2026-09-30")
        self.assertEqual(self.items()[0]["date_source"], "git")

    def test_verified_examples_are_a_theme_and_verification_register_is_not_a_report(self):
        report = "reports/examples/verified-example-20260930.md"
        register = "reports/examples/VERIFICATION.md"
        self.write(report, "# Verified English example\n")
        self.write(register, "# Verification register\n")
        self.git("add", "--", report, register)

        self.run_index()
        indexed = {item["path"]: item for item in self.items()}
        self.assertIn(report, indexed)
        self.assertEqual(indexed[report]["bucket"], "theme")
        self.assertEqual(indexed[report]["group"], "Verified English examples")
        self.assertNotIn(register, indexed)


if __name__ == "__main__":
    unittest.main()
