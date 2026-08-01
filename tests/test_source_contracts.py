from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_catalog import (  # noqa: E402
    calculate_source_fingerprint,
    validate_source_contracts,
)


def git(repository: Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repository), *args],
        check=True,
        text=True,
        capture_output=True,
    )
    return result.stdout.strip()


class SourceContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.repository = Path(self.temporary.name)
        git(self.repository, "init", "-b", "master")
        (self.repository / "contract.txt").write_text(
            "public_symbol\nsource query\n",
            encoding="utf-8",
        )
        git(self.repository, "add", "contract.txt")
        git(
            self.repository,
            "-c",
            "user.name=CCB Docs Test",
            "-c",
            "user.email=test@example.invalid",
            "commit",
            "-m",
            "contract",
        )
        self.commit = git(self.repository, "rev-parse", "HEAD")
        fingerprint = calculate_source_fingerprint(
            self.repository,
            self.commit,
            ["contract.txt"],
        )
        self.page = {
            "id": "api.contract",
            "language": "zh_CN",
            "verified_commit": self.commit,
            "source_paths": ["contract.txt"],
            "source_symbols": ["public_symbol"],
            "source_queries": ["source query"],
            "source_fingerprint": fingerprint,
        }

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def test_valid_source_metadata_passes(self) -> None:
        self.assertEqual(
            validate_source_contracts({"pages": [self.page]}, self.repository),
            [],
        )

    def test_fingerprint_and_symbol_drift_are_reported(self) -> None:
        page = dict(
            self.page,
            source_fingerprint="0" * 64,
            source_symbols=["missing_symbol"],
        )
        errors = validate_source_contracts({"pages": [page]}, self.repository)
        self.assertTrue(any("source_fingerprint" in error for error in errors))
        self.assertTrue(any("source symbol" in error for error in errors))

    def test_missing_source_path_is_reported(self) -> None:
        page = dict(self.page, source_paths=["missing.txt"])
        errors = validate_source_contracts({"pages": [page]}, self.repository)
        self.assertEqual(len(errors), 1)
        self.assertIn("source path is missing", errors[0])


if __name__ == "__main__":
    unittest.main()
