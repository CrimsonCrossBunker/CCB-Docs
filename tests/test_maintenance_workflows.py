from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_maintenance_workflows import (  # noqa: E402
    validate_dependabot,
    validate_monthly_contracts,
    validate_quarterly_live_audit,
    validate_repository,
    validate_runtime_example_workflow,
    validate_scheduled_workflow,
    validate_snapshot_workflow,
)


class MaintenanceWorkflowTests(unittest.TestCase):
    def test_repository_workflows_satisfy_scheduled_policy(self) -> None:
        self.assertEqual(validate_repository(), [])

    def test_policy_rejects_merge_commands(self) -> None:
        maintenance = yaml.safe_load(
            (ROOT / "config/maintenance.yml").read_text(encoding="utf-8")
        )
        source = (ROOT / ".github/workflows/nightly.yml").read_text(encoding="utf-8")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "nightly.yml"
            path.write_text(source + "\n# unsafe\n# gh pr merge 1\n", encoding="utf-8")
            errors = validate_scheduled_workflow(path, "weekly", maintenance)

        self.assertTrue(any("must not merge" in error for error in errors), errors)

    def test_dependabot_routes_locked_ecosystems_through_human_review(self) -> None:
        maintenance = yaml.safe_load(
            (ROOT / "config/maintenance.yml").read_text(encoding="utf-8")
        )

        self.assertEqual(validate_dependabot(maintenance), [])
        dependabot = yaml.safe_load(
            (ROOT / ".github/dependabot.yml").read_text(encoding="utf-8")
        )
        self.assertEqual(
            {item["package-ecosystem"] for item in dependabot["updates"]},
            {"github-actions", "npm", "uv"},
        )
        dependency_policy = maintenance["automation_policy"]["dependency_updates"]
        self.assertTrue(dependency_policy["responsible_human_review_required"])
        self.assertTrue(dependency_policy["action_references_remain_full_sha_pinned"])

    def test_monthly_workflow_checks_authoritative_contracts_before_reports(self) -> None:
        self.assertEqual(validate_monthly_contracts(), [])

    def test_weekly_evidence_collection_has_no_write_token(self) -> None:
        workflow = yaml.safe_load(
            (ROOT / ".github/workflows/nightly.yml").read_text(encoding="utf-8")
        )

        self.assertEqual(workflow["permissions"], {})
        self.assertEqual(workflow["jobs"]["report"]["permissions"], {"contents": "read"})
        self.assertEqual(
            workflow["jobs"]["reconcile"]["permissions"],
            {
                "actions": "read",
                "contents": "write",
                "issues": "write",
                "pull-requests": "write",
            },
        )

    def test_real_nightly_evidence_distinguishes_manual_recovery_from_bot_success(
        self,
    ) -> None:
        maintenance = yaml.safe_load(
            (ROOT / "config/maintenance.yml").read_text(encoding="utf-8")
        )
        settings = yaml.safe_load(
            (ROOT / "repository-settings.target.yml").read_text(encoding="utf-8")
        )
        evidence = maintenance["automation_policy"]["nightly_evidence"]
        record = settings["manual_record"]

        self.assertTrue(evidence["real_run_required"])
        self.assertTrue(evidence["distinguish_manual_recovery_pull_request"])
        self.assertEqual(record["nightly_drift_changed_files"], 5)
        self.assertFalse(record["nightly_automation_pull_request_created"])
        self.assertEqual(record["nightly_drift_pull_request_created_by"], "LYHGLYTX")
        self.assertEqual(
            record["actions_pr_creation_repository_update_result"],
            "http_409_organization_policy",
        )
        self.assertEqual(
            record["actions_pr_creation_organization_inspection_result"],
            "http_403_requires_admin_org",
        )

    def test_quarterly_workflow_routes_live_audit_context_without_token_argv(self) -> None:
        self.assertEqual(validate_quarterly_live_audit(), [])
        source = (ROOT / ".github/workflows/quarterly-maintenance.yml").read_text(
            encoding="utf-8"
        )
        self.assertNotIn('--github-token "${{ github.token }}"', source)

    def test_runtime_example_workflow_builds_headless_and_loads_both_examples(self) -> None:
        self.assertEqual(validate_runtime_example_workflow(), [])

    def test_runtime_example_policy_rejects_the_interactive_curses_backend(self) -> None:
        source = (ROOT / ".github/workflows/runtime-example-mods.yml").read_text(
            encoding="utf-8"
        )
        source = source.replace("-DHEADLESS=ON", "-DHEADLESS=OFF")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-example-mods.yml"
            path.write_text(source, encoding="utf-8")
            errors = validate_runtime_example_workflow(path)

        self.assertTrue(any("headless CCB build" in error for error in errors), errors)

    def test_runtime_example_policy_rejects_an_unpinned_ccb_checkout(self) -> None:
        source = (ROOT / ".github/workflows/runtime-example-mods.yml").read_text(
            encoding="utf-8"
        )
        source = source.replace(
            "ref: ${{ steps.runtime-source.outputs.commit }}",
            "ref: master",
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-example-mods.yml"
            path.write_text(source, encoding="utf-8")
            errors = validate_runtime_example_workflow(path)

        self.assertTrue(any("CCB checkout ref" in error for error in errors), errors)

    def test_runtime_example_policy_rejects_an_unbounded_mod_load(self) -> None:
        source = (ROOT / ".github/workflows/runtime-example-mods.yml").read_text(
            encoding="utf-8"
        )
        source = source.replace(
            '"${RUNTIME_COMMAND_TIMEOUT_SECONDS}s" \\',
            "true \\",
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-example-mods.yml"
            path.write_text(source, encoding="utf-8")
            errors = validate_runtime_example_workflow(path)

        self.assertTrue(any("bounded runtime load" in error for error in errors), errors)

    def test_runtime_example_policy_requires_execution_sentinel(self) -> None:
        source = (ROOT / ".github/workflows/runtime-example-mods.yml").read_text(
            encoding="utf-8"
        )
        source = source.replace(
            'error("validation execution sentinel")',
            'return true',
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "runtime-example-mods.yml"
            path.write_text(source, encoding="utf-8")
            errors = validate_runtime_example_workflow(path)

        self.assertTrue(any("bounded runtime load" in error for error in errors), errors)

    def test_snapshot_dispatch_is_serialized_and_cannot_reconcile_release_health(self) -> None:
        maintenance = yaml.safe_load(
            (ROOT / "config/maintenance.yml").read_text(encoding="utf-8")
        )

        self.assertEqual(validate_snapshot_workflow(maintenance), [])

    def test_snapshot_policy_rejects_ref_scoped_concurrency(self) -> None:
        maintenance = yaml.safe_load(
            (ROOT / "config/maintenance.yml").read_text(encoding="utf-8")
        )
        source = (ROOT / ".github/workflows/docs-snapshot.yml").read_text(
            encoding="utf-8"
        )
        source = source.replace(
            "group: documentation-snapshot",
            "group: documentation-snapshot-${{ github.ref }}",
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "docs-snapshot.yml"
            path.write_text(source, encoding="utf-8")
            errors = validate_snapshot_workflow(maintenance, path)

        self.assertTrue(any("fixed across refs" in error for error in errors), errors)

    def test_snapshot_policy_requires_missing_artifact_fallback(self) -> None:
        maintenance = yaml.safe_load(
            (ROOT / "config/maintenance.yml").read_text(encoding="utf-8")
        )
        source = (ROOT / ".github/workflows/docs-snapshot.yml").read_text(
            encoding="utf-8"
        )
        source = source.replace("continue-on-error: true", "continue-on-error: false")
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "docs-snapshot.yml"
            path.write_text(source, encoding="utf-8")
            errors = validate_snapshot_workflow(maintenance, path)

        self.assertTrue(
            any("artifact download must continue" in error for error in errors),
            errors,
        )


if __name__ == "__main__":
    unittest.main()
