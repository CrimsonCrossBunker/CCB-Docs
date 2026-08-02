from __future__ import annotations

import copy
import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from check_examples import load_validation_ids, validate_examples  # noqa: E402
from generate_catalog import load_catalog  # noqa: E402


class ExampleValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.catalog = load_catalog()
        cls.known_ids = load_validation_ids(
            ROOT / "config" / "example-validations.yml"
        )

    def test_all_marked_examples_are_registered(self) -> None:
        examples, errors = validate_examples(self.catalog, self.known_ids)
        self.assertEqual(errors, [])
        self.assertGreater(len(examples), 0)
        self.assertEqual({item.language for item in examples}, {"zh_CN", "en"})

    def test_unknown_catalog_validation_id_fails(self) -> None:
        catalog = copy.deepcopy(self.catalog)
        catalog["pages"][0]["example_validation_ids"].append("invented-command")
        _, errors = validate_examples(catalog, self.known_ids)
        self.assertTrue(any("unknown example validation ids" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
