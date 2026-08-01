from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_source_drift import detect_source_drift  # noqa: E402
from manage_tracking_issues import apply_catalog_updates, drift_updates  # noqa: E402


def git(repository: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repository), *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


def commit(repository: Path, message: str) -> str:
    git(repository, "add", ".")
    git(
        repository,
        "-c",
        "user.name=CCB Docs Test",
        "-c",
        "user.email=test@example.invalid",
        "commit",
        "-m",
        message,
    )
    return git(repository, "rev-parse", "HEAD")


class SourceDriftTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.repository = Path(self.temporary.name)
        git(self.repository, "init", "-b", "master")
        (self.repository / "src").mkdir()
        (self.repository / "notes").mkdir()
        (self.repository / "src/contract.txt").write_text("v1\n", encoding="utf-8")
        (self.repository / "notes/unrelated.txt").write_text("v1\n", encoding="utf-8")
        self.verified = commit(self.repository, "initial")
        self.page = {
            "id": "api.contract",
            "language": "zh_CN",
            "status": "active",
            "verified_commit": self.verified,
            "source_paths": ["src/contract.txt"],
            "risk_group": "api",
            "risk_level": "high",
        }

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_unrelated_commit_does_not_mark_page_stale(self) -> None:
        (self.repository / "notes/unrelated.txt").write_text("v2\n", encoding="utf-8")
        commit(self.repository, "unrelated")
        stale, skipped = detect_source_drift([self.page], self.repository, "HEAD")
        self.assertEqual(stale, [])
        self.assertEqual(skipped, [])

    def test_declared_source_path_change_marks_only_that_page(self) -> None:
        (self.repository / "src/contract.txt").write_text("v2\n", encoding="utf-8")
        commit(self.repository, "contract")
        other = dict(self.page, id="other", source_paths=["notes/unrelated.txt"])
        stale, _ = detect_source_drift(
            [self.page, other],
            self.repository,
            "HEAD",
        )
        keys = [(item["id"], item["language"]) for item in stale]
        self.assertEqual(keys, [("api.contract", "zh_CN")])
        self.assertEqual(stale[0]["changed_paths"], ["src/contract.txt"])

    def test_drift_update_does_not_bump_verified_commit(self) -> None:
        report = {
            "stale_pages": [
                {
                    "id": "api.contract",
                    "language": "zh_CN",
                    "changed_paths": ["src/contract.txt"],
                }
            ]
        }
        catalog = {"pages": [dict(self.page, include_in_ai_index=True)]}
        updates = drift_updates(report, catalog)
        serialized = json.dumps(updates[("api.contract", "zh_CN")])
        self.assertNotIn("verified_commit", serialized)
        self.assertEqual(updates[("api.contract", "zh_CN")]["status"], "stale")

    def test_catalog_update_changes_only_reported_page(self) -> None:
        catalog_path = self.repository / "catalog.yml"
        catalog_path.write_text(
            "pages:\n"
            "  - id: api.contract\n"
            "    language: zh_CN\n"
            "    status: active\n"
            "    verified_commit: 1111111111111111111111111111111111111111\n"
            "    include_in_ai_index: true\n"
            "    stale_reason: null\n"
            "  - id: other\n"
            "    language: en\n"
            "    status: active\n"
            "    verified_commit: 2222222222222222222222222222222222222222\n"
            "    include_in_ai_index: true\n"
            "    stale_reason: null\n",
            encoding="utf-8",
        )
        apply_catalog_updates(
            catalog_path,
            {
                ("api.contract", "zh_CN"): {
                    "status": "stale",
                    "include_in_ai_index": "false",
                    "stale_reason": '"source changed"',
                }
            },
        )
        catalog = yaml.safe_load(catalog_path.read_text(encoding="utf-8"))
        self.assertEqual(catalog["pages"][0]["status"], "stale")
        self.assertFalse(catalog["pages"][0]["include_in_ai_index"])
        self.assertEqual(catalog["pages"][1]["status"], "active")
        self.assertEqual(
            str(catalog["pages"][0]["verified_commit"]),
            "1111111111111111111111111111111111111111",
        )


if __name__ == "__main__":
    unittest.main()
