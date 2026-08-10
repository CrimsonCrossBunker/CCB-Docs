---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.inheritance-copy-from
title: JSON inheritance and copy-from
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
translation_source_fingerprint: 011b017522ac8f0fe674d25c2f3f6729ee36910b59b50abb94d54402ccefd8b1
prerequisites:
- json.overview
depends_on:
- reference.json-object-types
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/inheritance-copy-from/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/inheritance-copy-from/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/inheritance-copy-from/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/inheritance-copy-from/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.inheritance-copy-from%29%3A+&body=Document+ID%3A+json.inheritance-copy-from%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# JSON inheritance and `copy-from`

`copy-from` is not an implicit language feature shared by every JSON type. It works only when the
corresponding loader or factory implements inheritance, and types may have different merge and
validation rules.

## The source-backed common skeleton

`generic_factory` looks for `copy-from`, resolves a parent object, and lets a type use a dedicated
`handle_inheritance` implementation or assignment copying. An `abstract` can act as an inheritance
template. Support for `relative`, `proportional`, `extend`, and `delete` depends on the type, the
field's C++ representation, and dedicated loader code.

That establishes three boundaries:

- Registration of a `type` does not prove `copy-from` support.
- `copy-from` support does not prove support for all four incremental operations.
- A loadable example for one type does not prove the same merge semantics for another.

The [object-type registry](../reference/json-object-types.md) locates loaders, but its current field
classification does not automatically prove complete inheritance behaviour. For an unclassified
entry, inspect whether its loader uses `generic_factory`, whether it implements
`handle_inheritance`, and which regression tests cover it.

## Safe change procedure

1. Locate the target `type` and loader in the registry.
2. Resolve the parent ID or abstract and the same-type constraint.
3. Read that type's implementation of `copy-from`, `extend`, `delete`, `relative`, and
   `proportional`.
4. Keep inheritance chains shallow and avoid undeclared cross-mod load-order dependencies.
5. Test resolved values after real loading; do not compare input JSON text alone.

The item-name inheritance and monster attack-cooldown tests in `tests/json_load_test.cpp` show the
right testing layer: load data, then inspect the resolved object.

## Compatibility

Changing a parent may change every descendant. Renaming or deleting a parent ID, changing a
default, or changing replacement into extension can affect mods and saves. List descendants, run
data loading and focused tests, and record JSON/mod documentation impact in the pull request.
