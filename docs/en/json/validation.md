---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.validation
title: JSON validation and evidence levels
language: en
status: active
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- data/reference/json/ccb_json_object_types.json
- tools/json_api/contract-inventory.schema.json
- tools/json_api/generate_contracts.py
- tools/json_api/test_generate_contracts.py
- src/init.cpp
- src/generic_factory.h
- tests/json_load_test.cpp
- doc/JSON/JSON_INHERITANCE.md
- doc/JSON/JSON_STYLE.md
- tools/agent/generate_lua_first_replacement_ledger.py
- tools/agent/check_lua_first_replacement_ledger.py
source_symbols: []
source_queries: []
source_fingerprint: be0cec4549bdc28a9da387ded44644be569fb32aef07b5801e43a2facd88c30e
authority: api-contract
verified_commit: c961002ea44c8d41372ce683fac2505f903e6eb6
verified_at: '2026-10-29'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0f7a263e0a5c1d706a2ef65f9540c275b000dce6a79fafee558b583202012a33
prerequisites:
- json.overview
depends_on:
- reference.json-object-types
- eoc.overview
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; source contracts and Git history remain authoritative.
example_validation_ids:
- json-contract
- json-load
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1067
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/validation/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/validation/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/validation/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c961002ea44c8d41372ce683fac2505f903e6eb6
source_urls:
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/data/reference/json/ccb_json_object_types.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/json_api/test_generate_contracts.py
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/src/init.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/src/generic_factory.h
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tests/json_load_test.cpp
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/doc/JSON/JSON_INHERITANCE.md
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/doc/JSON/JSON_STYLE.md
- path: tools/agent/generate_lua_first_replacement_ledger.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/agent/generate_lua_first_replacement_ledger.py
- path: tools/agent/check_lua_first_replacement_ledger.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c961002ea44c8d41372ce683fac2505f903e6eb6/tools/agent/check_lua_first_replacement_ledger.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.validation%29%3A+&body=Document+ID%3A+json.validation%0ALanguage%3A+en%0AVerified+commit%3A+c961002ea44c8d41372ce683fac2505f903e6eb6%0A%0ADescribe+the+documentation+problem%3A%0A
---

# JSON validation and evidence levels

Different checks prove different facts. Do not report “parses” as “fully loads,” and do not use
lexical occurrence counts as evidence that a field is required.

## Recommended order

1. Run the repository JSON formatter to prove canonical project formatting.
2. Regenerate contract inventories and run their Schema, count, source-location, and example-pointer tests.
3. Run `json-check`. The current `chkjson` checks object/array syntax and a top-level string `type`
   under `data/json`; it is not a full semantic invocation of every loader.
4. Build the test program. Test startup loads core/test data; then run focused Catch2 tests for the type.
5. For an external mod, load it in a real CCB executable and test world; record version,
   dependencies, and logs.

Run these from the CCB source root:

```sh
# validation: json-contract
python3 tools/json_api/generate_contracts.py --check
python3 -m unittest discover -s tools/json_api -p 'test_*.py'
# validation: json-load
make -j2 json-check
```

## Evidence levels

| Marker | What it proves | What it does not prove |
| --- | --- | --- |
| `mandatory` / `optional` | Explicit field-read evidence in a loader | Every conditional and cross-field constraint |
| `partial` | A subset of the contract is classified | That omitted fields are safe or optional |
| `unclassified` | No publishable source classification yet | That the field does not exist |
| `lexical_only` | Matching text exists in data or legacy prose | A minimal valid example, requiredness, or equal semantics |
| `schema: none` | No general validator-backed Schema is recorded | That the loader performs no validation |

The generator reads only version-controlled paths returned by `git ls-files`. Inventories record registrations, source fingerprints, and observed data-instance counts. These changes have different meanings: item values, vehicle parts, and other JSON content can change a fingerprint or instance count without adding an object type or changing a field contract.

After changing data or source read by the inventory, regenerate from the same revision, then run `--check` and the relevant tests. If the baseline inventory was already stale, distinguish the baseline census refresh from the behavior change in the PR. If the replacement ledger references those inventories, update its linked fingerprints through its generator afterward. Never edit generated inventories or reference pages by hand.

```sh
python3 tools/json_api/generate_contracts.py
python3 tools/agent/generate_lua_first_replacement_ledger.py
python3 tools/json_api/generate_contracts.py --check
python3 tools/agent/check_lua_first_replacement_ledger.py
```

PRs that refresh inventories must still complete the documentation fields required by the current impact rules. Keep the companion documentation PR in draft until its source PR merges, then verify the final source commit. Generated checks do not establish gameplay acceptance.
