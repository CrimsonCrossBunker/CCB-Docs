from __future__ import annotations

import re
import unittest
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
WORKFLOW_DIR = ROOT / ".github/workflows"
ACTION_REFERENCE = re.compile(r"^\s*uses:\s*([^\s#]+)")
PINNED_ACTION = re.compile(r"^[^@\s]+@[0-9a-f]{40}$")


def load_workflow(name: str) -> dict:
    return yaml.safe_load((WORKFLOW_DIR / name).read_text(encoding="utf-8"))


class WorkflowQualityTests(unittest.TestCase):
    def test_remote_actions_are_pinned_to_full_commits(self) -> None:
        for workflow in sorted(WORKFLOW_DIR.glob("*.yml")):
            for line_number, line in enumerate(
                workflow.read_text(encoding="utf-8").splitlines(),
                start=1,
            ):
                match = ACTION_REFERENCE.match(line)
                if not match or match.group(1).startswith("./"):
                    continue
                self.assertRegex(
                    match.group(1),
                    PINNED_ACTION,
                    f"{workflow.relative_to(ROOT)}:{line_number}",
                )

    def test_every_workflow_and_job_has_resource_boundaries(self) -> None:
        for workflow_path in sorted(WORKFLOW_DIR.glob("*.yml")):
            workflow = yaml.safe_load(workflow_path.read_text(encoding="utf-8"))
            self.assertIn("permissions", workflow, workflow_path.name)
            self.assertIn("concurrency", workflow, workflow_path.name)
            for job_name, job in workflow["jobs"].items():
                self.assertIn(
                    "timeout-minutes",
                    job,
                    f"{workflow_path.name}:{job_name}",
                )

    def test_node_22_site_qa_runs_the_complete_quality_chain(self) -> None:
        workflow = load_workflow("ci.yml")
        job = workflow["jobs"]["site-qa"]
        self.assertEqual(job["name"], "Site QA (Node 22)")
        run_script = "\n".join(
            step.get("run", "") for step in job["steps"] if isinstance(step, dict)
        )
        for command in (
            "npm ci",
            "npm audit --audit-level=high",
            "npx playwright install --with-deps chromium",
            "scripts/check_site_quality.py",
            "scripts/check_search.py",
            "npm run qa:browser",
            "npm run qa:lighthouse",
            "--offline-archive artifacts/ccb-docs-offline.zip",
        ):
            self.assertIn(command, run_script)

    def test_pages_uses_split_least_privilege_and_publishes_offline_zip(self) -> None:
        workflow = load_workflow("pages.yml")
        self.assertEqual(workflow["permissions"], {})
        self.assertEqual(workflow["jobs"]["build"]["permissions"], {"contents": "read"})
        self.assertEqual(
            workflow["jobs"]["deploy"]["permissions"],
            {"pages": "write", "id-token": "write"},
        )
        build_script = "\n".join(
            step.get("run", "")
            for step in workflow["jobs"]["build"]["steps"]
            if isinstance(step, dict)
        )
        self.assertIn("--offline-archive artifacts/ccb-docs-offline.zip", build_script)


if __name__ == "__main__":
    unittest.main()
