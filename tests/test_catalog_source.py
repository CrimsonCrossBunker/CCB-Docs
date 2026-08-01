from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_catalog import source_fingerprint, validate_source_contracts  # noqa: E402


class CatalogSourceTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.repository = Path(self.temporary.name)
        subprocess.run(["git", "init", "-q", str(self.repository)], check=True)
        (self.repository / "contract.txt").write_text(
            "public_contract_symbol\n", encoding="utf-8"
        )
        subprocess.run(
            ["git", "-C", str(self.repository), "add", "contract.txt"],
            check=True,
        )
        subprocess.run(
            [
                "git",
                "-C",
                str(self.repository),
                "-c",
                "user.name=Catalog Test",
                "-c",
                "user.email=catalog@example.invalid",
                "commit",
                "-q",
                "-m",
                "fixture",
            ],
            check=True,
        )
        self.commit = subprocess.run(
            ["git", "-C", str(self.repository), "rev-parse", "HEAD"],
            check=True,
            text=True,
            capture_output=True,
        ).stdout.strip()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def page(self) -> dict:
        return {
            "id": "fixture.contract",
            "language": "zh_CN",
            "verified_commit": self.commit,
            "source_paths": ["contract.txt"],
            "source_symbols": ["public_contract_symbol"],
            "source_fingerprint": source_fingerprint(
                self.repository,
                self.commit,
                ["contract.txt"],
            ),
        }

    def test_exact_source_path_symbol_and_fingerprint_are_valid(self) -> None:
        self.assertEqual(
            validate_source_contracts({"pages": [self.page()]}, self.repository),
            [],
        )

    def test_missing_source_path_is_auditable_error(self) -> None:
        page = self.page()
        page["source_paths"] = ["missing.txt"]
        errors = validate_source_contracts({"pages": [page]}, self.repository)
        self.assertIn("invalid source_paths", errors[0])

    def test_missing_source_symbol_is_auditable_error(self) -> None:
        page = self.page()
        page["source_symbols"] = ["not_registered"]
        errors = validate_source_contracts({"pages": [page]}, self.repository)
        self.assertIn("missing source symbol", errors[0])


if __name__ == "__main__":
    unittest.main()
