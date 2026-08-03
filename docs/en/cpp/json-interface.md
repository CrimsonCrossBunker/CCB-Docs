---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp-json-interface
title: 'Legacy migration draft: json interface'
language: en
status: active
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
review_interval_days: 365
last_human_reviewer: LYHGLYTX
source_paths:
- doc/c++/JSON_INTERFACE.md
- src/flexbuffer_json.h
- src/flexbuffer_json.cpp
- src/generic_factory.h
- tests/generic_factory_test.cpp
source_symbols:
- JsonObject
- JsonArray
- generic_factory
source_queries: []
source_fingerprint: c63af9e125cbee7cbed69fcdde222171233e52ab5c6bdc2661d41903fa1b0bd7
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0692ae6ad72ffd129b9c96456c280f91b44d176e70e19e4468880145edc0bb47
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: ehughsbaird; accepted inventory identities only. Source paths and Git
  history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: cpp
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/json-interface/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/json-interface/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/json-interface/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/json-interface/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/c++/JSON_INTERFACE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c++/JSON_INTERFACE.md
- path: src/flexbuffer_json.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/flexbuffer_json.h
- path: src/flexbuffer_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/flexbuffer_json.cpp
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/generic_factory.h
- path: tests/generic_factory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/generic_factory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp-json-interface%29%3A+&body=Document+ID%3A+cpp-json-interface%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: json interface

This is the migration draft page for `cpp-json-interface`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `cpp-json-interface`
- Target: `cpp/json-interface.md`
- Replacement: cpp-json-interface
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| cpp-json-interface | doc/c++/JSON_INTERFACE.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## CCB C++ JSON interface

First distinguish three jobs: loading human-authored game data, reading program-written old saves,
and writing new saves. They share `JsonValue`, `JsonArray`, `JsonObject`, `JsonMember`, and
`JsonOut`, but have different compatibility policies. Game data has factory inheritance; save data
must recognize old formats and must not treat `copy-from` as a save mechanism.

### Read and write basics

`JsonValue` tests and reads scalars or becomes an object or array. `JsonObject` accesses named
members, `JsonArray` iterates or consumes positions, and `JsonMember` preserves both key and value.
Prefer `read` and existing deserializers or readers instead of reimplementing type dispatch.

After a type implements `T::serialize( JsonOut & ) const` or a free `serialize`,
`JsonOut::write` and `member` can compose it. Implement the corresponding `deserialize` for reads.
The emitted form is a compatibility contract: before renaming, removing, or changing a field type,
retain an old-format reader and round-trip plus frozen-fixture tests.

### Game-data loaders

A generic factory manages IDs, `copy-from`, deferred loading, finalization, and consistency checks.
An object's `load` normally uses:

- `mandatory( jo, was_loaded, name, member[, reader] )` for values required on first definition;
- `optional( jo, was_loaded, name, member[, reader], default )` for an explicit first-load default;
- typed readers for shorthand, units, IDs, containers, and supported inheritance operations.

Put the default in the `optional` call rather than relying only on header initialization.
`was_loaded` preserves a parent's value when the child omits a member. Passing false incorrectly
erases inherited state; passing true incorrectly can skip first-definition requirements.

`extend` and `delete`, `relative`, and `proportional` are all opt-in. Container readers often support
the first pair; numeric operations depend on the type and reader. A field resembling a vector or
integer is not proof that every patch form is supported.

### Errors and strictness

Let `JsonObject` or the reader throw at a specific member so file, line, column, and member context
survive. Do not call `allow_omitted_members` broadly for “compatibility”; reserve it for deliberate
forwarding or ignored-object boundaries. Run finalization and consistency checking after parsing
because cross-ID failures and cycles often appear only there.

### Validation

For game data, run formatting, `make -j2 json-check`, `--check-mods` for the actual Mod set, and
object-focused tests. For save data, test current write-to-read round trips, frozen old fixtures,
missing and added fields, and malformed input. Compile every target using a changed public header
and confirm diagnostics retain source context.

## History and attribution

Accepted inventory contributors: ehughsbaird. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `c63af9e125cbee7cbed69fcdde222171233e52ab5c6bdc2661d41903fa1b0bd7`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/c++/JSON_INTERFACE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/JSON_INTERFACE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c%2B%2B/JSON_INTERFACE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
