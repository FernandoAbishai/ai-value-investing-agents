from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import manage  # noqa: E402


class UnifiedManagerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        base = Path(self.temporary.name)
        self.state = base / "state"
        self.claude = base / "claude" / "commands"
        self.codex = base / "codex"
        self.manager = manage.InstallationManager(
            root=ROOT,
            state_home=self.state,
            claude_commands_dir=self.claude,
            codex_home=self.codex,
            reporter=manage.Reporter(quiet=True),
        )
        self.all_components = ["claude", "codex-skills", "codex-prompts"]

    def tearDown(self):
        self.temporary.cleanup()

    def install(self, selected=None):
        selected = selected or self.all_components
        with patch.object(self.manager, "verify_generated_sources", return_value=None):
            return self.manager.install_or_update(
                selected,
                dry_run=False,
                backup=True,
                operation="install",
            )

    def test_install_all_writes_expected_files_and_manifest(self):
        result = self.install()
        self.assertEqual(result.changed, 61)
        self.assertEqual(len(list(self.claude.glob("*.md"))), 20)
        self.assertEqual(len(list((self.codex / "skills").glob("*/SKILL.md"))), 21)
        self.assertEqual(len(list((self.codex / "prompts").glob("*.md"))), 20)

        manifest = json.loads((self.state / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["project"], manage.PROJECT)
        self.assertEqual(set(manifest["components"]), set(self.all_components))
        self.assertEqual(len(manifest["components"]["claude"]["entries"]), 20)
        self.assertEqual(len(manifest["components"]["codex-skills"]["entries"]), 21)
        self.assertEqual(len(manifest["components"]["codex-prompts"]["entries"]), 20)

    def test_doctor_is_healthy_after_install(self):
        self.install()
        report = self.manager.doctor(self.all_components)
        self.assertTrue(report["healthy"], report)
        self.assertTrue(all(item["healthy"] for item in report["components"].values()))
        self.assertTrue(all(item["ok"] for item in report["generated_checks"].values()))

    def test_dry_run_does_not_create_destination_or_manifest(self):
        with patch.object(self.manager, "verify_generated_sources", return_value=None):
            result = self.manager.install_or_update(
                ["claude"],
                dry_run=True,
                backup=True,
                operation="install",
            )
        self.assertEqual(result.changed, 20)
        self.assertFalse(self.claude.exists())
        self.assertFalse((self.state / "manifest.json").exists())

    def test_install_backs_up_preexisting_collision(self):
        self.claude.mkdir(parents=True)
        collision = self.claude / "investment-research.md"
        collision.write_text("local custom content\n", encoding="utf-8")

        result = self.install(["claude"])
        self.assertEqual(result.backups, 1)
        self.assertEqual(
            collision.read_bytes(),
            (ROOT / "skills" / "investment-research.md").read_bytes(),
        )
        backups = list((self.state / "backups").glob("*/claude/investment-research.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(encoding="utf-8"), "local custom content\n")

    def test_update_repairs_drift_and_keeps_backup(self):
        self.install(["claude"])
        target = self.claude / "investment-research.md"
        target.write_text("modified after install\n", encoding="utf-8")

        with patch.object(self.manager, "verify_generated_sources", return_value=None):
            result = self.manager.install_or_update(
                ["claude"],
                dry_run=False,
                backup=True,
                operation="update",
            )
        self.assertEqual(result.changed, 1)
        self.assertEqual(result.unchanged, 19)
        backups = list((self.state / "backups").glob("*/claude/investment-research.md"))
        self.assertEqual(len(backups), 1)
        report = self.manager.doctor(["claude"])
        self.assertTrue(report["healthy"], report)

    def test_uninstall_removes_only_managed_entries(self):
        self.install()
        unrelated = self.claude / "my-own-command.md"
        unrelated.write_text("keep me\n", encoding="utf-8")

        result = self.manager.uninstall(
            self.all_components,
            dry_run=False,
            force=False,
            backup=False,
        )
        self.assertEqual(result.removed, 61)
        self.assertTrue(unrelated.is_file())
        self.assertEqual(unrelated.read_text(encoding="utf-8"), "keep me\n")
        self.assertFalse((self.codex / "skills" / "investment-research").exists())
        manifest = json.loads((self.state / "manifest.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest["components"], {})

    def test_uninstall_preserves_modified_entry_without_force(self):
        self.install(["claude"])
        target = self.claude / "investment-research.md"
        target.write_text("modified after install\n", encoding="utf-8")

        result = self.manager.uninstall(
            ["claude"],
            dry_run=False,
            force=False,
            backup=False,
        )
        self.assertEqual(result.skipped, 1)
        self.assertTrue(result.issues)
        self.assertTrue(target.exists())
        manifest = json.loads((self.state / "manifest.json").read_text(encoding="utf-8"))
        self.assertIn("investment-research.md", manifest["components"]["claude"]["entries"])

    def test_forced_uninstall_can_backup_modified_entry(self):
        self.install(["claude"])
        target = self.claude / "investment-research.md"
        target.write_text("modified after install\n", encoding="utf-8")

        result = self.manager.uninstall(
            ["claude"],
            dry_run=False,
            force=True,
            backup=True,
        )
        self.assertEqual(result.removed, 20)
        self.assertEqual(result.backups, 1)
        self.assertFalse(target.exists())
        backups = list((self.state / "backups").glob("*/claude/investment-research.md"))
        self.assertEqual(len(backups), 1)
        self.assertEqual(backups[0].read_text(encoding="utf-8"), "modified after install\n")

    def test_doctor_detects_missing_and_modified_entries(self):
        self.install(["claude"])
        (self.claude / "investment-research.md").write_text("changed\n", encoding="utf-8")
        (self.claude / "earnings-review.md").unlink()

        report = self.manager.doctor(["claude"])
        self.assertFalse(report["healthy"])
        component = report["components"]["claude"]
        self.assertIn("investment-research.md", component["entries_modified"])
        self.assertIn("earnings-review.md", component["entries_missing"])

    def test_hash_tree_is_stable_and_sensitive_to_content(self):
        source = self.codex / "fixture"
        source.mkdir(parents=True)
        (source / "a.txt").write_text("a", encoding="utf-8")
        (source / "b.txt").write_text("b", encoding="utf-8")
        first = manage.hash_path(source)
        second = manage.hash_path(source)
        self.assertEqual(first, second)
        (source / "b.txt").write_text("changed", encoding="utf-8")
        self.assertNotEqual(first, manage.hash_path(source))


if __name__ == "__main__":
    unittest.main(verbosity=2)
