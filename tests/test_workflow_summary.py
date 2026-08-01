from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from write_workflow_summary import render_summary  # noqa: E402


class WorkflowSummaryTests(unittest.TestCase):
    def test_missing_and_valid_reports_both_reach_summary(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            valid = root / "valid.json"
            valid.write_text(
                json.dumps(
                    {
                        "kind": "docs-coverage",
                        "status": "attention",
                        "findings": [
                            {
                                "id": "stale:test",
                                "severity": "warning",
                                "message": "line one\nline two | value",
                            }
                        ],
                    }
                ),
                encoding="utf-8",
            )

            summary = render_summary("Maintenance", [valid, root / "missing.json"])

        self.assertIn("`docs-coverage` | attention | 1", summary)
        self.assertIn("unavailable", summary)
        self.assertIn("line one line two \\| value", summary)

    def test_weekly_legacy_report_shape_has_a_real_count(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            report = Path(directory) / "source-drift.json"
            report.write_text(
                json.dumps({"stale_pages": [{"id": "test"}], "skipped_pages": []}),
                encoding="utf-8",
            )

            summary = render_summary("Weekly", [report])

        self.assertIn("`source-drift` | attention | 1", summary)


if __name__ == "__main__":
    unittest.main()
