from __future__ import annotations

import hashlib
import json
import sys
import tempfile
import unittest
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from create_docs_snapshot import (  # noqa: E402
    SnapshotError,
    create_snapshot,
    ensure_workflow_failure_report,
    verify_snapshot,
)


class SnapshotTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.temp = Path(self.temporary.name)
        self.site = self.temp / "site"
        (self.site / "en").mkdir(parents=True)
        (self.site / "index.html").write_text("<h1>中文</h1>\n", encoding="utf-8")
        (self.site / "en/index.html").write_text("<h1>English</h1>\n", encoding="utf-8")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_snapshot_is_deterministic_and_restore_verified(self) -> None:
        first = self.temp / "first.zip"
        second = self.temp / "second.zip"

        create_snapshot(self.site, first, "test-snapshot")
        create_snapshot(self.site, second, "test-snapshot")

        self.assertEqual(first.read_bytes(), second.read_bytes())
        result = verify_snapshot(first)
        self.assertEqual(result["restore_test"], "pass")
        self.assertGreater(result["entry_count"], 2)

    def test_restore_rejects_path_traversal(self) -> None:
        archive = self.temp / "traversal.zip"
        with zipfile.ZipFile(archive, "w") as output:
            output.writestr("../escape", b"bad")

        with self.assertRaisesRegex(SnapshotError, "unsafe path"):
            verify_snapshot(archive)

    def test_creation_rejects_site_symlink(self) -> None:
        outside = self.temp / "outside.txt"
        outside.write_text("secret\n", encoding="utf-8")
        (self.site / "external.txt").symlink_to(outside)

        with self.assertRaisesRegex(SnapshotError, "external symlink"):
            create_snapshot(self.site, self.temp / "unsafe.zip", "unsafe")

    def test_restore_rejects_corrupt_payload_hash(self) -> None:
        archive = self.temp / "corrupt.zip"
        payloads = {
            "site/index.html": b"zh",
            "site/en/index.html": b"en",
            "repository/docs-catalog.yml": b"catalog",
            "repository/repository-settings.target.yml": b"settings",
        }
        manifest = {
            "schema_version": 1,
            "label": "corrupt",
            "source_commit": "0" * 40,
            "entries": [
                {
                    "path": name,
                    "bytes": len(content),
                    "sha256": hashlib.sha256(content).hexdigest(),
                }
                for name, content in sorted(payloads.items())
            ],
        }
        payloads["site/index.html"] = b"changed"
        with zipfile.ZipFile(archive, "w") as output:
            for name, content in payloads.items():
                output.writestr(name, content)
            output.writestr("snapshot-manifest.json", json.dumps(manifest))

        with self.assertRaisesRegex(SnapshotError, "hash mismatch"):
            verify_snapshot(archive)

    def test_missing_workflow_report_is_synthesized_as_failure(self) -> None:
        report = self.temp / "restore-health.json"

        created = ensure_workflow_failure_report(report, "failure")
        payload = json.loads(report.read_text(encoding="utf-8"))

        self.assertTrue(created)
        self.assertEqual(payload["status"], "failure")
        self.assertEqual(payload["summary"]["workflow_result"], "failure")
        self.assertEqual(payload["findings"][0]["id"], "snapshot-workflow-failed")

    def test_existing_workflow_report_is_never_overwritten(self) -> None:
        report = self.temp / "restore-health.json"
        original = '{"status": "pass", "findings": []}\n'
        report.write_text(original, encoding="utf-8")

        created = ensure_workflow_failure_report(report, "failure")

        self.assertFalse(created)
        self.assertEqual(report.read_text(encoding="utf-8"), original)

    def test_workflow_report_rejects_unknown_job_result(self) -> None:
        with self.assertRaisesRegex(SnapshotError, "invalid snapshot workflow result"):
            ensure_workflow_failure_report(
                self.temp / "restore-health.json",
                "timed-out",
            )

    def test_cancelled_or_timed_out_job_result_is_reportable(self) -> None:
        report = self.temp / "restore-health.json"

        ensure_workflow_failure_report(report, "cancelled")
        payload = json.loads(report.read_text(encoding="utf-8"))

        self.assertEqual(payload["summary"]["workflow_result"], "cancelled")
        self.assertEqual(payload["findings"][0]["id"], "snapshot-workflow-failed")


if __name__ == "__main__":
    unittest.main()
