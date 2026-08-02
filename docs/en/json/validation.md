---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.validation
title: JSON validation and evidence levels
language: en
status: draft
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
source_symbols: []
source_queries: []
source_fingerprint: 94e31a97e0b63d9f3b6c7305bbed837cd0c5e5a3cf02417323458b7ed0757177
authority: api-contract
verified_commit: a038c765568fc47a58ef8c523b2722d416f5f61c
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 54da0baf1d3372e2c1bcdb6e0daa5c2ba4dd324e840733ba6a4366f9a73283f3
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/566
stale_reason: null
search:
  exclude: true
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

The generator reads only tracked paths returned by `git ls-files` and pins coverage at
190/275/306. Count changes must accompany registry/parser changes and a generated diff. Never edit
the generated inventories or generated reference pages by hand.
