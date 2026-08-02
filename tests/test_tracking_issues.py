from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import yaml


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from manage_tracking_issues import (  # noqa: E402
    GitHubClient,
    TrackingError,
    apply_catalog_updates,
    manage_maintenance_issue,
)


ANCHORED_CATALOG = """\
schema_version: 2
pages:
  - &page_defaults
    id: home
    title: CCB 开发文档
    language: zh_CN
    status: active
    include_in_ai_index: true
    stale_reason: null
    nav: { section: 首页, order: 0 }
  - &architecture_overview_zh
    <<: *page_defaults
    status: active
    include_in_ai_index: true
    id: architecture.overview
    title: CCB 项目架构
    language: zh_CN
    path: architecture/overview.md
    nav: { section: 架构, order: 20 }
  - <<: *architecture_overview_zh
    title: CCB project architecture
    language: en
    nav: { section: Architecture, order: 20 }
"""


UPDATED_ANCHORED_CATALOG = """\
schema_version: 2
pages:
  - &page_defaults
    id: home
    title: CCB 开发文档
    language: zh_CN
    status: active
    include_in_ai_index: true
    stale_reason: null
    nav: { section: 首页, order: 0 }
  - &architecture_overview_zh
    <<: *page_defaults
    status: stale
    include_in_ai_index: false
    id: architecture.overview
    title: CCB 项目架构
    language: zh_CN
    path: architecture/overview.md
    stale_reason: "zh source drift"
    nav: { section: 架构, order: 20 }
  - <<: *architecture_overview_zh
    title: CCB project architecture
    language: en
    stale_reason: "en source drift"
    nav: { section: Architecture, order: 20 }
"""


class FakeIssueClient:
    def __init__(self, issues: list[dict]) -> None:
        self.issues = issues
        self.created: list[dict] = []
        self.updated: list[tuple[int, str, str, str]] = []

    def list_issues(self) -> list[dict]:
        return self.issues

    def create_issue(self, title: str, body: str) -> dict:
        issue = {
            "number": 100 + len(self.created),
            "title": title,
            "body": body,
            "state": "open",
        }
        self.created.append(issue)
        self.issues.append(issue)
        return issue

    def update_issue(self, number: int, title: str, body: str, state: str) -> None:
        self.updated.append((number, title, body, state))
        issue = next(item for item in self.issues if item["number"] == number)
        issue.update({"title": title, "body": body, "state": state})


def response(status: int, payload: object, headers: dict[str, str] | None = None) -> Mock:
    result = Mock()
    result.status_code = status
    result.headers = headers or {}
    result.text = "response"
    result.content = b"{}" if payload is not None else b""
    result.json.return_value = payload
    return result


class TrackingIssueTests(unittest.TestCase):
    def test_catalog_updates_preserve_anchored_bilingual_format(self) -> None:
        updates = {
            ("architecture.overview", "zh_CN"): {
                "status": "stale",
                "include_in_ai_index": "false",
                "stale_reason": '"zh source drift"',
            },
            ("architecture.overview", "en"): {
                "status": "stale",
                "include_in_ai_index": "false",
                "stale_reason": '"en source drift"',
            },
        }
        with tempfile.TemporaryDirectory() as directory:
            catalog_path = Path(directory) / "docs-catalog.yml"
            catalog_path.write_text(ANCHORED_CATALOG, encoding="utf-8")

            apply_catalog_updates(catalog_path, updates)

            result = catalog_path.read_text(encoding="utf-8")

        self.assertEqual(result, UPDATED_ANCHORED_CATALOG)
        pages = yaml.safe_load(result)["pages"]
        by_key = {(page["id"], page["language"]): page for page in pages}
        for key, reason in (
            (("architecture.overview", "zh_CN"), "zh source drift"),
            (("architecture.overview", "en"), "en source drift"),
        ):
            self.assertEqual(by_key[key]["status"], "stale")
            self.assertFalse(by_key[key]["include_in_ai_index"])
            self.assertEqual(by_key[key]["stale_reason"], reason)

    def test_catalog_updates_reject_missing_page_without_writing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            catalog_path = Path(directory) / "docs-catalog.yml"
            catalog_path.write_text(ANCHORED_CATALOG, encoding="utf-8")

            with self.assertRaisesRegex(TrackingError, "catalog page not found"):
                apply_catalog_updates(
                    catalog_path,
                    {("missing.page", "en"): {"status": "stale"}},
                )

            self.assertEqual(
                catalog_path.read_text(encoding="utf-8"),
                ANCHORED_CATALOG,
            )

    def test_maintenance_issue_reuses_one_and_closes_duplicates(self) -> None:
        marker = "<!-- ccb-docs:maintenance:monthly-api-diff -->"
        client = FakeIssueClient(
            [
                {"number": 1, "title": "old", "body": marker, "state": "open"},
                {"number": 2, "title": "copy", "body": marker, "state": "open"},
            ]
        )
        report = {
            "schema_version": 1,
            "status": "attention",
            "findings": [
                {"id": "api-drift:test", "severity": "error", "message": "changed"}
            ],
        }

        manage_maintenance_issue(
            client,
            report,
            "monthly-api-diff",
            "[maintenance] API diff",
        )

        self.assertEqual(client.created, [])
        self.assertEqual(client.issues[0]["state"], "open")
        self.assertEqual(client.issues[1]["state"], "closed")
        self.assertIn("duplicate of #1", client.issues[1]["body"])

    def test_zero_findings_closes_every_matching_issue(self) -> None:
        marker = "<!-- ccb-docs:maintenance:archive-review -->"
        client = FakeIssueClient(
            [
                {"number": 3, "title": "one", "body": marker, "state": "open"},
                {"number": 4, "title": "two", "body": marker, "state": "open"},
            ]
        )

        manage_maintenance_issue(
            client,
            {"findings": []},
            "archive-review",
            "[maintenance] Archive review",
        )

        self.assertEqual([issue["state"] for issue in client.issues], ["closed", "closed"])

    @patch("manage_tracking_issues.time.sleep")
    def test_rate_limit_retries_with_bounded_wait(self, sleep: Mock) -> None:
        client = GitHubClient("owner/repository", "token")
        client.session.request = Mock(
            side_effect=[
                response(429, {}, {"Retry-After": "1"}),
                response(200, {"ok": True}),
            ]
        )

        payload = client.request("GET", "/example")

        self.assertEqual(payload, {"ok": True})
        sleep.assert_called_once_with(1)
        self.assertEqual(client.session.request.call_count, 2)

    @patch("manage_tracking_issues.time.sleep")
    def test_rate_limit_refuses_an_unbounded_wait(self, sleep: Mock) -> None:
        client = GitHubClient("owner/repository", "token")
        client.session.request = Mock(
            return_value=response(403, {}, {"Retry-After": "31"})
        )

        with self.assertRaisesRegex(TrackingError, "rate limit exhausted"):
            client.request("GET", "/example")

        sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
