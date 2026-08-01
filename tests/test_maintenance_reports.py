from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from datetime import date
from pathlib import Path
from unittest.mock import patch

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from generate_maintenance_reports import (  # noqa: E402
    agent_benchmark_readiness,
    api_diff,
    archive_review,
    contract_fingerprint,
    docs_coverage,
    permissions_audit,
    ruleset_policy_findings,
)


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


class MaintenanceReportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.temp = Path(self.temporary.name)
        self.source = self.temp / "source"
        self.source.mkdir()
        git(self.source, "init", "-b", "master")
        (self.source / "contracts").mkdir()
        (self.source / "contracts/api.json").write_text("{\"version\": 1}\n", encoding="utf-8")
        (self.source / "AGENTS.md").write_text("agent map\n", encoding="utf-8")
        commit(self.source, "initial")

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def write_contract_config(self, baseline: str | None) -> tuple[Path, Path]:
        watch = self.temp / "watch.yml"
        baseline_path = self.temp / "baseline.yml"
        watch.write_text(
            yaml.safe_dump(
                {
                    "schema_version": 1,
                    "contracts": {
                        "test-api": {
                            "paths": ["contracts/api.json"],
                            "pending_source_pr": None,
                        }
                    },
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        baseline_path.write_text(
            yaml.safe_dump(
                {
                    "schema_version": 1,
                    "source_commit": None,
                    "contracts": {"test-api": baseline},
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        return watch, baseline_path

    def write_permissions_config(self, active: bool = False) -> tuple[Path, Path]:
        settings = self.temp / "repository-settings.yml"
        maintenance = self.temp / "maintenance.yml"
        settings.write_text(
            yaml.safe_dump(
                {
                    "schema_version": 1,
                    "enforcement": "active" if active else "deferred",
                    "prerequisites": {"minimum_confirmed_human_reviewers": 2},
                    "target": {
                        "pages_source": "github_actions",
                        "allow_github_actions_create_pull_requests": True,
                        "actions_bot_may_approve": False,
                        "ruleset": {
                            "name": "protected-default-branch",
                            "enforcement": "active" if active else "deferred",
                            "require_pull_request": True,
                            "required_non_author_human_approvals": 1,
                            "dismiss_stale_reviews": True,
                            "require_conversation_resolution": True,
                            "required_status_checks": ["Documentation CI / validate"],
                            "prohibit_force_push": True,
                            "prohibit_branch_deletion": True,
                            "bypass": {
                                "policy": "emergency_only",
                                "actors": ["team:maintainers"] if active else [],
                                "reason_required": True,
                            },
                        },
                        "security": {
                            "secret_scanning": "enabled_target",
                            "push_protection": "enabled_target",
                            "dependency_updates": "enabled_target",
                            "organization_2fa": (
                                "enabled" if active else "deferred_pending_audit"
                            ),
                        },
                    },
                    "manual_record": {
                        "confirmed_reviewers": ["reviewer-a", "reviewer-b"] if active else [],
                        "protection_enabled_at": "2026-08-01T00:00:00Z" if active else None,
                        "actions_pr_creation_result": "enabled" if active else "blocked",
                        "required_checks": ["Documentation CI / validate"] if active else [],
                        "required_checks_verified_at": (
                            "2026-08-01T00:00:00Z" if active else None
                        ),
                    },
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        maintenance.write_text(
            yaml.safe_dump(
                {
                    "schema_version": 1,
                    "repository": "CrimsonCrossBunker/CCB-Docs",
                    "governance_blockers": {
                        "required_human_reviewers": {
                            "state": "resolved" if active else "blocked",
                            "issue": "https://example.invalid/reviewers",
                        },
                        "ruleset_enforcement": {
                            "state": "resolved" if active else "blocked",
                            "issue": "https://example.invalid/ruleset",
                        },
                        "actions_pull_request_creation": {
                            "state": "resolved" if active else "blocked",
                            "issue": "https://example.invalid/actions",
                        },
                        "organization_2fa": {
                            "state": "enabled_after_audit" if active else "blocked",
                            "issue": "https://example.invalid/2fa",
                        },
                    },
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        return settings, maintenance

    def build_complete_docs_contract(self) -> dict:
        source_commit = "0" * 40
        zh_url = "https://docs.example.test/guides/target/"
        en_url = "https://docs.example.test/en/guides/target/"
        registry_entries = [
            {
                "id": "repo.agents",
                "path": "AGENTS.md",
                "status": "active",
                "ccb_docs_ids": [],
            }
        ]
        documents = []
        legacy = self.source / "legacy"
        legacy.mkdir()
        for index in range(175):
            path = f"legacy/doc-{index:03}.md"
            stable_id = f"legacy.doc-{index:03}"
            stubbed = index == 0
            if stubbed:
                body = (
                    "<!-- CCB-DOC-MOVED-START -->\n"
                    f"Stable document ID: `{stable_id}`\n"
                    f"Last in-repository commit: `{source_commit}`\n"
                    f"Chinese: {zh_url}\nEnglish: {en_url}\n"
                    "Moved date: `2026-08-02`\n"
                    "This body is no longer maintained; the entry remains permanently.\n"
                    "<!-- CCB-DOC-MOVED-END -->\n"
                )
            else:
                body = f"# Document {index}\n"
            (self.source / path).write_text(body, encoding="utf-8")
            registry_entries.append(
                {
                    "id": f"repo.legacy-{index:03}",
                    "path": path,
                    "status": "moved_stub" if stubbed else "active",
                    "ccb_docs_ids": [stable_id] if stubbed else [],
                }
            )
            documents.append(
                {
                    "original_path": path,
                    "source_commit": source_commit,
                    "action": "migrate_rewrite" if stubbed else "keep_in_repo",
                    "migration_status": "stubbed" if stubbed else "verified",
                    "stable_document_id": stable_id,
                    "merge_target": "guide.target" if stubbed else None,
                    "replacement": "guide.target" if stubbed else None,
                    "zh_url": zh_url if stubbed else None,
                    "en_url": en_url if stubbed else None,
                    "moved_at": "2026-08-02" if stubbed else None,
                }
            )
        (self.source / "ai").mkdir()
        (self.source / "doc/migration").mkdir(parents=True)
        (self.source / "ai/documentation-registry.yml").write_text(
            yaml.safe_dump(
                {
                    "schema_version": 1,
                    "entry_count": len(registry_entries),
                    "entries": registry_entries,
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        (self.source / "doc/migration/markdown-inventory.yml").write_text(
            yaml.safe_dump(
                {
                    "schema_version": 2,
                    "document_count": 175,
                    "documents": documents,
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )
        commit(self.source, "add complete documentation contracts")
        pages = []
        for language in ("zh_CN", "en"):
            pages.append(
                {
                    "id": "guide.target",
                    "language": language,
                    "path": "guides/target.md",
                    "status": "active",
                    "risk_group": "test",
                    "risk_level": "normal",
                    "translation_status": "current",
                    "translation_stale_since": None,
                    "verified_at": "2026-08-01",
                    "review_interval_days": 365,
                    "last_human_reviewer": "Responsible human",
                    "doc_type": "reference",
                    "include_in_search": True,
                    "include_in_ai_index": True,
                }
            )
        return {
            "site": {
                "base_url": "https://docs.example.test/",
                "default_language": "zh_CN",
            },
            "pages": pages,
        }

    def test_api_report_distinguishes_missing_baseline_match_and_drift(self) -> None:
        watch, baseline = self.write_contract_config(None)
        missing = api_diff(self.source, "HEAD", watch, baseline)
        self.assertEqual(
            missing["summary"]["contracts"]["test-api"]["status"],
            "baseline-missing",
        )

        fingerprint = contract_fingerprint(self.source, "HEAD", ["contracts/api.json"])
        watch, baseline = self.write_contract_config(fingerprint)
        matching = api_diff(self.source, "HEAD", watch, baseline)
        self.assertEqual(matching["status"], "pass")
        self.assertEqual(matching["findings"], [])

        (self.source / "contracts/api.json").write_text("{\"version\": 2}\n", encoding="utf-8")
        commit(self.source, "change contract")
        changed = api_diff(self.source, "HEAD", watch, baseline)
        self.assertEqual(changed["summary"]["contracts"]["test-api"]["status"], "changed")
        self.assertEqual(changed["findings"][0]["id"], "api-drift:test-api")

    def test_agent_benchmark_never_fabricates_missing_observations(self) -> None:
        config = self.temp / "benchmark.yml"
        config.write_text(
            yaml.safe_dump(
                {
                    "schema_version": 1,
                    "token_limit": 1000,
                    "tasks": [
                        {
                            "id": "navigation",
                            "expected_paths": ["AGENTS.md"],
                            "expected_document_ids": ["home"],
                        }
                    ],
                    "observation_schema": {
                        "required_metrics": ["correct_path_hit_rate", "unrelated_changes"]
                    },
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )

        result = agent_benchmark_readiness(self.source, "HEAD", config, None)

        self.assertEqual(result["status"], "blocked")
        self.assertFalse(result["summary"]["observations_supplied"])
        self.assertEqual(
            result["summary"]["behavioral_metrics"],
            {"correct_path_hit_rate": None, "unrelated_changes": None},
        )

    def test_missing_authoritative_benchmark_is_an_explicit_blocker(self) -> None:
        config = self.temp / "benchmark.yml"
        config.write_text(
            yaml.safe_dump(
                {
                    "schema_version": 1,
                    "token_limit": 1000,
                    "tasks": [],
                    "observation_schema": {"required_metrics": []},
                },
                sort_keys=False,
            ),
            encoding="utf-8",
        )

        result = agent_benchmark_readiness(
            self.source,
            "HEAD",
            config,
            None,
            run_source_benchmark=True,
        )

        identities = {item["id"] for item in result["findings"]}
        self.assertEqual(result["status"], "blocked")
        self.assertIn("authoritative-agent-benchmark-missing", identities)
        self.assertFalse(result["summary"]["observations_supplied"])

    def test_docs_coverage_reports_overdue_translation_and_review(self) -> None:
        pages = [
            {
                "id": "test.doc",
                "language": language,
                "status": "active",
                "risk_group": "test",
                "risk_level": "normal",
                "translation_status": (
                    "translation-stale" if language == "en" else "current"
                ),
                "translation_stale_since": "2026-01-01" if language == "en" else None,
                "verified_at": "2026-01-01",
                "review_interval_days": 30,
                "last_human_reviewer": "Responsible human",
                "doc_type": "reference",
                "include_in_search": True,
                "include_in_ai_index": True,
            }
            for language in ("zh_CN", "en")
        ]
        with patch("generate_maintenance_reports.load_catalog", return_value={"pages": pages}):
            result = docs_coverage(date(2026, 3, 1))

        identities = {item["id"] for item in result["findings"]}
        self.assertIn("translation-overdue:test.doc", identities)
        self.assertIn("review-overdue:test.doc", identities)
        self.assertEqual(result["summary"]["stable_document_ids"], 1)

    def test_docs_coverage_reconciles_registry_inventory_stubs_and_catalog(self) -> None:
        catalog = self.build_complete_docs_contract()
        with patch("generate_maintenance_reports.load_catalog", return_value=catalog):
            result = docs_coverage(date(2026, 8, 2), self.source)

        regressions = {
            item["id"]
            for item in result["findings"]
            if item["id"].startswith("docs-coverage-regression:")
        }
        self.assertEqual(regressions, set())
        self.assertEqual(result["summary"]["frozen_inventory_documents"], 175)
        self.assertEqual(result["summary"]["permanent_stub_verified"], 1)
        self.assertEqual(result["summary"]["migration_catalog_mappings_verified"], 1)
        self.assertEqual(result["summary"]["new_unregistered_markdown"], 0)

        (self.source / "NEW_UNREGISTERED.md").write_text("# New\n", encoding="utf-8")
        commit(self.source, "add unregistered Markdown")
        with patch("generate_maintenance_reports.load_catalog", return_value=catalog):
            regressed = docs_coverage(date(2026, 8, 2), self.source)
        identities = {item["id"] for item in regressed["findings"]}
        self.assertIn("unregistered-markdown", identities)
        self.assertIn("docs-coverage-regression:documentation-registry", identities)
        self.assertEqual(regressed["summary"]["new_unregistered_markdown"], 1)

    def test_archive_review_detects_index_leaks(self) -> None:
        pages = [
            {
                "id": "old.doc",
                "language": language,
                "status": "archived",
                "include_in_search": language == "en",
                "include_in_ai_index": False,
                "verified_at": "2026-01-01",
                "review_interval_days": 365,
            }
            for language in ("zh_CN", "en")
        ]
        with patch("generate_maintenance_reports.load_catalog", return_value={"pages": pages}):
            result = archive_review(date(2026, 2, 1))

        self.assertEqual(result["findings"][0]["id"], "archive-index-leak:old.doc:en")
        self.assertEqual(result["summary"]["excluded_from_ai"], 2)

    def test_permissions_report_keeps_admin_only_changes_blocked(self) -> None:
        settings, maintenance = self.write_permissions_config()
        result = permissions_audit(
            settings,
            maintenance,
            github_token="",
        )

        identities = {item["id"] for item in result["findings"]}
        self.assertEqual(result["status"], "blocked")
        self.assertFalse(result["summary"]["safe_to_enable_required_approval"])
        self.assertIn("confirmed-reviewers", identities)
        self.assertIn("ruleset-not-enforced", identities)
        self.assertIn("actions-pr-creation", identities)
        self.assertIn("organization-2fa", identities)
        self.assertIn("github-observation-token-missing", identities)
        self.assertEqual(result["summary"]["github_observations"]["state"], "unobserved")

    def test_permissions_report_exposes_404_and_permission_denials(self) -> None:
        settings, maintenance = self.write_permissions_config()

        def deny(endpoint: str, _token: str, _api_base: str) -> dict:
            return {
                "state": "unobserved",
                "http_status": 403 if "actions/permissions" in endpoint else 404,
                "error": "Not Found or insufficient permission",
            }

        with patch("generate_maintenance_reports.github_api_get", side_effect=deny):
            result = permissions_audit(
                settings,
                maintenance,
                github_token="read-only-token",
            )

        identities = {item["id"] for item in result["findings"]}
        self.assertIn("github-observation-unavailable:rulesets", identities)
        self.assertIn("github-observation-unavailable:workflow_permissions", identities)
        self.assertIn("github-observation-unavailable:pages_environment", identities)
        self.assertIn("github-observation-unavailable:repository_security", identities)
        self.assertIn("github-observation-unavailable:organization_2fa", identities)
        self.assertEqual(result["summary"]["github_observations"]["state"], "partial")
        self.assertFalse(result["summary"]["safe_to_enable_required_approval"])

    def test_permissions_report_uses_live_read_only_observations(self) -> None:
        settings, maintenance = self.write_permissions_config(active=True)

        def observe(endpoint: str, _token: str, _api_base: str) -> dict:
            if endpoint.endswith("rulesets?includes_parents=true"):
                data = [
                    {
                        "id": 1,
                        "name": "protected-default-branch",
                        "target": "branch",
                        "enforcement": "active",
                        "source_type": "Repository",
                    }
                ]
                status = 200
            elif endpoint.endswith("/rulesets/1"):
                data = {
                    "bypass_actors": [
                        {
                            "actor_id": 42,
                            "actor_type": "Team",
                            "bypass_mode": "always",
                        }
                    ],
                    "conditions": {
                        "ref_name": {
                            "include": ["refs/heads/main"],
                            "exclude": [],
                        }
                    },
                    "rules": [
                        {"type": "deletion"},
                        {"type": "non_fast_forward"},
                        {
                            "type": "pull_request",
                            "parameters": {
                                "required_approving_review_count": 1,
                                "dismiss_stale_reviews_on_push": True,
                                "required_review_thread_resolution": True,
                            },
                        },
                        {
                            "type": "required_status_checks",
                            "parameters": {
                                "required_status_checks": [
                                    {"context": "Documentation CI / validate"}
                                ]
                            },
                        },
                    ],
                }
                status = 200
            elif endpoint.endswith("actions/permissions/workflow"):
                data = {
                    "default_workflow_permissions": "read",
                    "can_approve_pull_request_reviews": True,
                }
                status = 200
            elif endpoint.endswith("environments/github-pages"):
                data = {
                    "name": "github-pages",
                    "protection_rules": [],
                    "deployment_branch_policy": None,
                }
                status = 200
            elif endpoint.endswith("/pages"):
                data = {
                    "build_type": "workflow",
                    "status": "built",
                    "html_url": "https://docs.example.test/",
                }
                status = 200
            elif endpoint.endswith("/vulnerability-alerts"):
                data = None
                status = 204
            elif endpoint.endswith("/automated-security-fixes"):
                data = None
                status = 204
            elif endpoint.startswith("orgs/"):
                data = {"two_factor_requirement_enabled": True}
                status = 200
            else:
                data = {
                    "security_and_analysis": {
                        "secret_scanning": {"status": "enabled"},
                        "secret_scanning_push_protection": {"status": "enabled"},
                        "dependabot_security_updates": {"status": "enabled"},
                    }
                }
                status = 200
            return {"state": "observed", "http_status": status, "data": data}

        with patch("generate_maintenance_reports.github_api_get", side_effect=observe):
            result = permissions_audit(
                settings,
                maintenance,
                github_token="read-only-token",
            )

        self.assertEqual(result["status"], "pass")
        observations = result["summary"]["github_observations"]
        self.assertEqual(observations["state"], "observed")
        self.assertEqual(observations["organization"], "CrimsonCrossBunker")
        self.assertEqual(
            observations["controls"]["rulesets"]["rulesets"][0]["detail_state"],
            "observed",
        )
        self.assertEqual(
            observations["controls"]["workflow_permissions"][
                "default_workflow_permissions"
            ],
            "read",
        )
        self.assertTrue(
            observations["controls"]["repository_security"]["push_protection"]
            == "enabled"
        )
        self.assertTrue(result["summary"]["safe_to_enable_required_approval"])

    def test_ruleset_policy_requires_complete_effective_rules(self) -> None:
        desired = {
            "require_pull_request": True,
            "required_non_author_human_approvals": 1,
            "dismiss_stale_reviews": True,
            "require_conversation_resolution": True,
            "required_status_checks": ["Documentation CI / validate"],
            "prohibit_force_push": True,
            "prohibit_branch_deletion": True,
            "bypass": {"policy": "emergency_only"},
        }
        observed = {
            "id": 1,
            "detail_state": "observed",
            "rules": [
                {
                    "type": "pull_request",
                    "parameters": {
                        "required_approving_review_count": 0,
                        "dismiss_stale_reviews_on_push": False,
                        "required_review_thread_resolution": False,
                    },
                }
            ],
            "bypass_actors": [],
        }

        identities = {
            item["id"] for item in ruleset_policy_findings(observed, desired)
        }

        self.assertIn("github-observed-ruleset-policy:approval-count", identities)
        self.assertIn(
            "github-observed-ruleset-policy:required-status-checks",
            identities,
        )
        self.assertIn(
            "github-observed-ruleset-policy:force-push-prohibited",
            identities,
        )
        self.assertIn(
            "github-observed-ruleset-policy:branch-deletion-prohibited",
            identities,
        )
        self.assertIn(
            "github-observed-ruleset-policy:emergency-bypass-missing",
            identities,
        )


if __name__ == "__main__":
    unittest.main()
