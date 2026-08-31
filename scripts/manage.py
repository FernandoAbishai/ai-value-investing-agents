#!/usr/bin/env python3
"""Install, update, diagnose, and uninstall AI Value Investing Agents.

The manager is intentionally dependency-free and works on Python 3.10+ across
Windows, macOS, and Linux. It tracks only files installed by this project,
backs up collisions before replacement, and refuses to delete locally modified
managed files unless the user passes ``--force``.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
import uuid
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

PROJECT = "ai-value-investing-agents"
SCHEMA_VERSION = 1
MIN_PYTHON = (3, 10)
ROOT = Path(__file__).resolve().parents[1]


class ManagerError(RuntimeError):
    """Raised for a user-actionable management error."""


@dataclass(frozen=True)
class Component:
    name: str
    source: Path
    destination: Path
    kind: str  # "files" or "directories"
    expected_count: int


@dataclass
class OperationResult:
    changed: int = 0
    unchanged: int = 0
    removed: int = 0
    skipped: int = 0
    backups: int = 0
    issues: list[str] | None = None

    def __post_init__(self) -> None:
        if self.issues is None:
            self.issues = []


class Reporter:
    def __init__(self, *, quiet: bool = False) -> None:
        self.quiet = quiet

    def emit(self, message: str) -> None:
        if not self.quiet:
            print(message)

    def action(self, label: str, path: Path | str) -> None:
        self.emit(f"  {label:<12} {path}")


class InstallationManager:
    def __init__(
        self,
        *,
        root: Path = ROOT,
        state_home: Path | None = None,
        claude_commands_dir: Path | None = None,
        codex_home: Path | None = None,
        reporter: Reporter | None = None,
    ) -> None:
        self.root = root.resolve()
        self.state_home = (
            state_home
            or Path(os.environ.get("AIVA_STATE_HOME", "~/.ai-value-investing-agents"))
        ).expanduser().resolve()
        self.claude_commands_dir = (
            claude_commands_dir
            or Path(os.environ.get("CLAUDE_COMMANDS_DIR", "~/.claude/commands"))
        ).expanduser().resolve()
        self.codex_home = (
            codex_home or Path(os.environ.get("CODEX_HOME", "~/.codex"))
        ).expanduser().resolve()
        self.manifest_path = self.state_home / "manifest.json"
        self.reporter = reporter or Reporter()
        self._backup_root: Path | None = None

    def components(self) -> dict[str, Component]:
        return {
            "claude": Component(
                name="claude",
                source=self.root / "skills",
                destination=self.claude_commands_dir,
                kind="files",
                expected_count=21,
            ),
            "codex-skills": Component(
                name="codex-skills",
                source=self.root / "codex-skills",
                destination=self.codex_home / "skills",
                kind="directories",
                expected_count=22,
            ),
            "codex-prompts": Component(
                name="codex-prompts",
                source=self.root / "codex-prompts",
                destination=self.codex_home / "prompts",
                kind="files",
                expected_count=21,
            ),
        }

    def load_manifest(self) -> dict:
        if not self.manifest_path.exists():
            return {
                "schema_version": SCHEMA_VERSION,
                "project": PROJECT,
                "components": {},
            }
        try:
            manifest = json.loads(self.manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as error:
            raise ManagerError(f"Cannot read manifest {self.manifest_path}: {error}") from error
        if manifest.get("project") != PROJECT:
            raise ManagerError(
                f"Manifest at {self.manifest_path} belongs to another project."
            )
        if manifest.get("schema_version") != SCHEMA_VERSION:
            raise ManagerError(
                f"Unsupported manifest schema: {manifest.get('schema_version')!r}."
            )
        manifest.setdefault("components", {})
        return manifest

    def save_manifest(self, manifest: dict, *, dry_run: bool) -> None:
        if dry_run:
            return
        manifest["schema_version"] = SCHEMA_VERSION
        manifest["project"] = PROJECT
        manifest["source_commit"] = self.source_revision()
        manifest["updated_at"] = datetime.now(timezone.utc).isoformat()
        self.state_home.mkdir(parents=True, exist_ok=True)
        temporary = self.manifest_path.with_name(
            f".{self.manifest_path.name}.tmp-{uuid.uuid4().hex}"
        )
        temporary.write_text(
            json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8"
        )
        os.replace(temporary, self.manifest_path)

    def source_revision(self) -> str:
        try:
            result = subprocess.run(
                ["git", "rev-parse", "--short=12", "HEAD"],
                cwd=self.root,
                check=True,
                capture_output=True,
                text=True,
            )
            return result.stdout.strip()
        except (OSError, subprocess.CalledProcessError):
            return "unknown"

    def source_entries(self, component: Component) -> dict[str, Path]:
        if not component.source.is_dir():
            raise ManagerError(f"Missing source directory: {component.source}")
        if component.kind == "files":
            entries = {
                path.name: path
                for path in sorted(component.source.glob("*.md"))
                if path.is_file()
            }
        elif component.kind == "directories":
            entries = {
                path.name: path
                for path in sorted(component.source.iterdir())
                if path.is_dir() and (path / "SKILL.md").is_file()
            }
        else:
            raise ManagerError(f"Unsupported component kind: {component.kind}")
        if len(entries) != component.expected_count:
            raise ManagerError(
                f"{component.name}: expected {component.expected_count} source entries, "
                f"found {len(entries)}."
            )
        return entries

    def verify_generated_sources(self, selected: Iterable[str]) -> None:
        selected_set = set(selected)
        commands: list[list[str]] = []
        if "codex-skills" in selected_set:
            commands.append(
                [sys.executable, str(self.root / "scripts/sync-codex-skills.py"), "--check"]
            )
        if "codex-prompts" in selected_set:
            commands.append(
                [sys.executable, str(self.root / "scripts/sync-codex-prompts.py"), "--check"]
            )
        for command in commands:
            result = subprocess.run(command, cwd=self.root, capture_output=True, text=True)
            if result.returncode != 0:
                detail = (result.stderr or result.stdout).strip()
                raise ManagerError(
                    "Generated Codex artifacts are stale. Regenerate them before installation."
                    + (f"\n{detail}" if detail else "")
                )

    def install_or_update(
        self,
        selected: Iterable[str],
        *,
        dry_run: bool,
        backup: bool,
        operation: str,
    ) -> OperationResult:
        selected_list = list(selected)
        self.verify_generated_sources(selected_list)
        manifest = self.load_manifest()
        result = OperationResult()
        self.reporter.emit(f"{operation.title()} components: {', '.join(selected_list)}")
        if dry_run:
            self.reporter.emit("Dry run: no files or manifests will be changed.")

        for name in selected_list:
            component = self.components()[name]
            entries = self.source_entries(component)
            previous = manifest["components"].get(name, {})
            previous_entries = previous.get("entries", {})
            destination = component.destination
            self.reporter.emit(f"\n{name} -> {destination}")
            if not dry_run:
                destination.mkdir(parents=True, exist_ok=True)

            new_entries: dict[str, dict[str, str]] = {}
            for entry_name, source in entries.items():
                target = destination / entry_name
                source_hash = hash_path(source)
                target_hash = hash_path(target) if target.exists() else None
                if target_hash == source_hash:
                    result.unchanged += 1
                    self.reporter.action("unchanged", target)
                else:
                    if target.exists() and backup:
                        backup_path = self.backup_entry(name, entry_name, target, dry_run=dry_run)
                        result.backups += 1
                        self.reporter.action("backup", backup_path)
                    elif target.exists() and not backup:
                        self.reporter.action("replace", target)
                    else:
                        self.reporter.action("install", target)
                    if not dry_run:
                        replace_entry(source, target)
                    result.changed += 1
                new_entries[entry_name] = {
                    "sha256": source_hash,
                    "source": source.relative_to(self.root).as_posix(),
                }

            stale_names = sorted(set(previous_entries) - set(entries))
            for entry_name in stale_names:
                target = Path(previous.get("destination", str(destination))) / entry_name
                recorded_hash = previous_entries[entry_name].get("sha256")
                if not target.exists():
                    self.reporter.action("stale absent", target)
                    continue
                current_hash = hash_path(target)
                if current_hash != recorded_hash:
                    result.skipped += 1
                    result.issues.append(
                        f"Preserved modified stale entry: {target}. Remove it manually if obsolete."
                    )
                    self.reporter.action("preserved", target)
                    new_entries[entry_name] = previous_entries[entry_name]
                    continue
                if backup:
                    backup_path = self.backup_entry(name, entry_name, target, dry_run=dry_run)
                    result.backups += 1
                    self.reporter.action("backup", backup_path)
                self.reporter.action("remove stale", target)
                if not dry_run:
                    remove_entry(target)
                result.removed += 1

            if not dry_run:
                manifest["components"][name] = {
                    "destination": str(destination),
                    "kind": component.kind,
                    "entries": new_entries,
                }

        self.save_manifest(manifest, dry_run=dry_run)
        self.print_summary(result)
        return result

    def uninstall(
        self,
        selected: Iterable[str],
        *,
        dry_run: bool,
        force: bool,
        backup: bool,
    ) -> OperationResult:
        selected_list = list(selected)
        manifest = self.load_manifest()
        result = OperationResult()
        self.reporter.emit(f"Uninstall components: {', '.join(selected_list)}")
        if dry_run:
            self.reporter.emit("Dry run: no files or manifests will be changed.")

        for name in selected_list:
            installed = manifest["components"].get(name)
            if not installed:
                self.reporter.emit(f"\n{name}: not recorded as installed")
                continue
            destination = Path(installed["destination"])
            remaining: dict[str, dict[str, str]] = {}
            self.reporter.emit(f"\n{name} <- {destination}")
            for entry_name, metadata in sorted(installed.get("entries", {}).items()):
                target = destination / entry_name
                if not target.exists():
                    result.unchanged += 1
                    self.reporter.action("already absent", target)
                    continue
                current_hash = hash_path(target)
                recorded_hash = metadata.get("sha256")
                modified = current_hash != recorded_hash
                if modified and not force:
                    result.skipped += 1
                    remaining[entry_name] = metadata
                    message = (
                        f"Refusing to delete modified managed entry: {target}. "
                        "Use --force to remove it."
                    )
                    result.issues.append(message)
                    self.reporter.action("preserved", target)
                    continue
                if backup and modified:
                    backup_path = self.backup_entry(name, entry_name, target, dry_run=dry_run)
                    result.backups += 1
                    self.reporter.action("backup", backup_path)
                self.reporter.action("remove", target)
                if not dry_run:
                    remove_entry(target)
                result.removed += 1

            if not dry_run:
                if remaining:
                    installed["entries"] = remaining
                    manifest["components"][name] = installed
                else:
                    manifest["components"].pop(name, None)
                remove_empty_directory(destination)

        self.save_manifest(manifest, dry_run=dry_run)
        self.print_summary(result)
        return result

    def doctor(self, selected: Iterable[str]) -> dict:
        selected_list = list(selected)
        manifest = self.load_manifest()
        report: dict = {
            "project": PROJECT,
            "python": {
                "version": platform.python_version(),
                "minimum": ".".join(str(value) for value in MIN_PYTHON),
                "ok": sys.version_info >= MIN_PYTHON,
            },
            "source_revision": self.source_revision(),
            "manifest": {
                "path": str(self.manifest_path),
                "exists": self.manifest_path.exists(),
            },
            "components": {},
            "generated_checks": {},
            "healthy": True,
        }

        for name in selected_list:
            component = self.components()[name]
            component_report = {
                "source": str(component.source),
                "source_count": 0,
                "expected_count": component.expected_count,
                "destination": str(component.destination),
                "installed": False,
                "entries_ok": 0,
                "entries_missing": [],
                "entries_modified": [],
                "unexpected_managed_entries": [],
                "healthy": True,
            }
            try:
                source_entries = self.source_entries(component)
                component_report["source_count"] = len(source_entries)
            except ManagerError as error:
                source_entries = {}
                component_report["error"] = str(error)
                component_report["healthy"] = False

            installed = manifest["components"].get(name)
            if installed:
                component_report["installed"] = True
                destination = Path(installed["destination"])
                component_report["destination"] = str(destination)
                for entry_name, metadata in sorted(installed.get("entries", {}).items()):
                    target = destination / entry_name
                    if not target.exists():
                        component_report["entries_missing"].append(entry_name)
                    elif hash_path(target) != metadata.get("sha256"):
                        component_report["entries_modified"].append(entry_name)
                    else:
                        component_report["entries_ok"] += 1
                component_report["unexpected_managed_entries"] = sorted(
                    set(installed.get("entries", {})) - set(source_entries)
                )
            else:
                component_report["healthy"] = False
                component_report["error"] = "component is not recorded as installed"

            if (
                component_report["entries_missing"]
                or component_report["entries_modified"]
                or component_report["unexpected_managed_entries"]
            ):
                component_report["healthy"] = False
            report["components"][name] = component_report

        for name, script in (
            ("codex-skills", "sync-codex-skills.py"),
            ("codex-prompts", "sync-codex-prompts.py"),
        ):
            if name not in selected_list:
                continue
            command = [sys.executable, str(self.root / "scripts" / script), "--check"]
            completed = subprocess.run(command, cwd=self.root, capture_output=True, text=True)
            report["generated_checks"][name] = {
                "ok": completed.returncode == 0,
                "message": (completed.stdout or completed.stderr).strip(),
            }

        report["healthy"] = bool(report["python"]["ok"]) and all(
            component["healthy"] for component in report["components"].values()
        ) and all(
            result["ok"] for result in report["generated_checks"].values()
        )
        return report

    def print_doctor(self, report: dict) -> None:
        status = "healthy" if report["healthy"] else "issues found"
        self.reporter.emit(f"AI Value Investing Agents doctor: {status}")
        self.reporter.emit(
            f"Python {report['python']['version']} "
            f"(minimum {report['python']['minimum']}): "
            f"{'ok' if report['python']['ok'] else 'unsupported'}"
        )
        self.reporter.emit(f"Source revision: {report['source_revision']}")
        self.reporter.emit(
            f"Manifest: {report['manifest']['path']} "
            f"({'present' if report['manifest']['exists'] else 'missing'})"
        )
        for name, component in report["components"].items():
            self.reporter.emit(f"\n{name}: {'ok' if component['healthy'] else 'issue'}")
            self.reporter.emit(
                f"  source entries: {component['source_count']} / {component['expected_count']}"
            )
            self.reporter.emit(f"  destination: {component['destination']}")
            self.reporter.emit(f"  installed entries verified: {component['entries_ok']}")
            if component.get("error"):
                self.reporter.emit(f"  error: {component['error']}")
            if component["entries_missing"]:
                self.reporter.emit(
                    "  missing: " + ", ".join(component["entries_missing"])
                )
            if component["entries_modified"]:
                self.reporter.emit(
                    "  modified: " + ", ".join(component["entries_modified"])
                )
            if component["unexpected_managed_entries"]:
                self.reporter.emit(
                    "  stale managed entries: "
                    + ", ".join(component["unexpected_managed_entries"])
                )
        for name, check in report["generated_checks"].items():
            self.reporter.emit(
                f"\n{name} generated-source check: {'ok' if check['ok'] else 'failed'}"
            )
            if check["message"]:
                self.reporter.emit(f"  {check['message']}")

    def backup_entry(
        self,
        component_name: str,
        entry_name: str,
        target: Path,
        *,
        dry_run: bool,
    ) -> Path:
        if self._backup_root is None:
            timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
            self._backup_root = self.state_home / "backups" / timestamp
        backup_target = self._backup_root / component_name / entry_name
        if dry_run:
            return backup_target
        backup_target.parent.mkdir(parents=True, exist_ok=True)
        candidate = backup_target
        suffix = 1
        while candidate.exists():
            candidate = backup_target.with_name(f"{backup_target.name}.{suffix}")
            suffix += 1
        copy_entry(target, candidate)
        return candidate

    def print_summary(self, result: OperationResult) -> None:
        self.reporter.emit(
            "\nSummary: "
            f"changed={result.changed}, unchanged={result.unchanged}, "
            f"removed={result.removed}, skipped={result.skipped}, backups={result.backups}"
        )
        for issue in result.issues or []:
            self.reporter.emit(f"Warning: {issue}")


def hash_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def hash_path(path: Path) -> str:
    if path.is_file():
        return hash_file(path)
    if path.is_dir():
        digest = hashlib.sha256()
        for child in sorted(item for item in path.rglob("*") if item.is_file()):
            relative_name = child.relative_to(path).as_posix().encode("utf-8")
            digest.update(len(relative_name).to_bytes(8, "big"))
            digest.update(relative_name)
            digest.update(bytes.fromhex(hash_file(child)))
        return digest.hexdigest()
    raise ManagerError(f"Cannot hash missing or unsupported path: {path}")


def copy_entry(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.is_dir():
        shutil.copytree(source, destination, copy_function=shutil.copy2)
    else:
        shutil.copy2(source, destination)


def replace_entry(source: Path, destination: Path) -> None:
    temporary = destination.parent / f".{destination.name}.tmp-{uuid.uuid4().hex}"
    try:
        copy_entry(source, temporary)
        if destination.exists():
            remove_entry(destination)
        os.replace(temporary, destination)
    finally:
        if temporary.exists():
            remove_entry(temporary)


def remove_entry(path: Path) -> None:
    if path.is_dir() and not path.is_symlink():
        shutil.rmtree(path)
    else:
        path.unlink(missing_ok=True)


def remove_empty_directory(path: Path) -> None:
    try:
        path.rmdir()
    except OSError:
        return


def selected_components(args: argparse.Namespace) -> list[str]:
    if getattr(args, "all", False):
        return ["claude", "codex-skills", "codex-prompts"]
    if getattr(args, "codex", False):
        return ["codex-skills", "codex-prompts"]
    if getattr(args, "claude", False):
        return ["claude"]
    if getattr(args, "codex_skills", False):
        return ["codex-skills"]
    if getattr(args, "codex_prompts", False):
        return ["codex-prompts"]
    return ["claude", "codex-skills", "codex-prompts"]


def add_component_flags(parser: argparse.ArgumentParser, *, required: bool) -> None:
    group = parser.add_mutually_exclusive_group(required=required)
    group.add_argument("--all", action="store_true", help="manage Claude and all Codex components")
    group.add_argument("--claude", action="store_true", help="manage Claude Code commands")
    group.add_argument("--codex", action="store_true", help="manage Codex skills and prompts")
    group.add_argument("--codex-skills", action="store_true", help="manage Codex skills only")
    group.add_argument("--codex-prompts", action="store_true", help="manage Codex prompts only")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Manage AI Value Investing Agents installations safely."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command in ("install", "update"):
        subparser = subparsers.add_parser(command, help=f"{command} managed components")
        add_component_flags(subparser, required=True)
        subparser.add_argument("--dry-run", action="store_true", help="show changes without writing")
        subparser.add_argument(
            "--no-backup", action="store_true", help="replace collisions without making backups"
        )

    uninstall = subparsers.add_parser("uninstall", help="remove managed components")
    add_component_flags(uninstall, required=True)
    uninstall.add_argument("--dry-run", action="store_true", help="show removals without writing")
    uninstall.add_argument(
        "--force", action="store_true", help="remove locally modified managed entries"
    )
    uninstall.add_argument(
        "--backup-modified",
        action="store_true",
        help="back up modified entries before forced removal",
    )

    doctor = subparsers.add_parser("doctor", help="diagnose source and installation state")
    add_component_flags(doctor, required=False)
    doctor.add_argument("--json", action="store_true", help="write machine-readable JSON")

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    reporter = Reporter(quiet=getattr(args, "json", False))
    manager = InstallationManager(reporter=reporter)
    selected = selected_components(args)

    try:
        if args.command in {"install", "update"}:
            result = manager.install_or_update(
                selected,
                dry_run=args.dry_run,
                backup=not args.no_backup,
                operation=args.command,
            )
            return 1 if result.issues else 0
        if args.command == "uninstall":
            result = manager.uninstall(
                selected,
                dry_run=args.dry_run,
                force=args.force,
                backup=args.backup_modified,
            )
            return 1 if result.issues else 0
        if args.command == "doctor":
            report = manager.doctor(selected)
            if args.json:
                print(json.dumps(report, indent=2, sort_keys=True))
            else:
                manager.print_doctor(report)
            return 0 if report["healthy"] else 1
    except ManagerError as error:
        print(f"Error: {error}", file=sys.stderr)
        return 2

    parser.error(f"Unsupported command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
