---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.overview
title: JSON contract overview
language: en
status: stale
doc_type: explanation
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
source_fingerprint: 694345d1f3eb604519f90e93d870396341c99719edf7270e88a651574b995a7e
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d24151da9c3f3be1b0307ecb5a26a8425e9791b3376028d77e457e08745e6012
prerequisites:
- architecture.project-map
depends_on:
- reference.json-object-types
- validation.testing
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; source contracts and Git history remain authoritative.
example_validation_ids: []
api_version: contract-inventory-v1
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: data/reference/json/ccb_json_object_types.json,
  tools/json_api/test_generate_contracts.py'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/reference/json/ccb_json_object_types.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/reference/json/ccb_json_object_types.json
- path: tools/json_api/contract-inventory.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/contract-inventory.schema.json
- path: tools/json_api/generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/generate_contracts.py
- path: tools/json_api/test_generate_contracts.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/json_api/test_generate_contracts.py
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/init.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/generic_factory.h
- path: tests/json_load_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/json_load_test.cpp
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_INHERITANCE.md
- path: doc/JSON/JSON_STYLE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/JSON_STYLE.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.overview%29%3A+&body=Document+ID%3A+json.overview%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# JSON contract overview

CCB's JSON contract is not defined by one universal Schema. Runtime loaders and tests define
behaviour; `DynamicDataLoader` registrations define top-level `type` dispatch; schemas,
validators, and generated inventories record the subset that machines can prove. Legacy prose
and data examples are leads, not overrides for those contracts.

## Current machine coverage

- The [JSON object-type registry](../reference/json-object-types.md) indexes 190 unique
  registered types and 191 registration calls.
- 183 registered types have top-level instance candidates among 6,714 audited tracked JSON files.
- Seven registered types have no instance candidate; the inventory found no observed, unregistered
  top-level string type.
- All 190 general Schema statuses are `none`; the registry must not be presented as a complete
  game JSON Schema.
- Field contracts are `unclassified` for 189 types and currently `partial` for
  `effect_on_condition`.

These figures describe the generated inventories at commit
`a038c765568fc47a58ef8c523b2722d416f5f61c`. They do not claim that every field, default,
inheritance rule, or cross-ID reference has been classified.

## How an object acquires meaning

1. The JSON parser proves that the file syntax and root container are readable.
2. A top-level object's string `type` enters registry dispatch.
3. Its loader or factory decides mandatory and optional fields, defaults, and errors in source.
4. Factory finalization/checks and cross-reference validation may reject it later.
5. Runtime tests prove specific behaviour and compatibility.

An occurrence in data is therefore only lexical instance evidence. A mention in legacy prose is
also only `lexical_only` evidence. Confirm a field in the loader, tests, and validators named by
the registry.

## Where to start

- To determine whether a `type` is registered, use the [generated registry](../reference/json-object-types.md).
- Before changing inherited objects, read [inheritance and copy-from](inheritance-copy-from.md).
- Before submitting, follow [JSON validation and evidence levels](validation.md).
- For EOCs, start with [EOC contracts and lifecycle](../eoc/overview.md).
- For a reproducible fixture, use the [complete JSON/EOC mod tutorial](../mods/complete-json-eoc-mod.md).

If this page conflicts with an inventory, Schema, registration, or test, mark the page stale and
repair it. Do not change runtime contracts merely to match prose.
