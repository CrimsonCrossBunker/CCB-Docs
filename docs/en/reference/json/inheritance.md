---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.inheritance
title: 'Legacy migration draft: inheritance'
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
- doc/JSON/JSON_INHERITANCE.md
- src/generic_factory.h
- src/generic_factory.cpp
- src/init.cpp
- tests/generic_factory_test.cpp
source_symbols:
- generic_factory::load
source_queries: []
source_fingerprint: 76ca6fc5abc73f10dffb3ed498ff09916d84b6c9ce62382a15ab58d823cb365c
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5cb76eb48b1689093f8759adcc2a3dd884260a19f83cb3b828c6d7d0a742db38
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: zihanZheng, ehughsbaird, thaelina; accepted inventory identities only.
  Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/inheritance/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/inheritance/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/inheritance/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/inheritance/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/JSON_INHERITANCE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_INHERITANCE.md
- path: src/generic_factory.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/generic_factory.h
- path: src/generic_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/generic_factory.cpp
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/init.cpp
- path: tests/generic_factory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/generic_factory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.inheritance%29%3A+&body=Document+ID%3A+json.inheritance%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: inheritance

This is the migration draft page for `json.inheritance`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.inheritance`
- Target: `reference/json/inheritance.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/inheritance/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.inheritance | doc/JSON/JSON_INHERITANCE.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB JSON inheritance rules

`copy-from` is not an automatic language feature of every JSON object type. Many types use
`generic_factory`, some have specialized implementations, and others do not support it.
For each use, follow the current registration into its loader and confirm the operations
that object actually implements.

### Generic-factory load order

For an object using `generic_factory`, the usual sequence is:

1. With `copy-from`, look for a loaded concrete object or `abstract`.
2. If the base is not loaded, place the child in the deferred queue and retry later.
3. Copy the base, then let the child's loader replace or adjust fields.
4. An `abstract` exists only for inheritance; specifying both `abstract` and a real `id` is an error.
5. Finalization and checks resolve cross-IDs and can find problems not proven during initial loading.

Deferred loading often handles ordering, but does not make an inheritance cycle valid or make
cross-Mod replacement order irrelevant.

### Four modification forms

```jsonc
{
  "type": "ITEM",
  "id": "ccb_example_child",
  "copy-from": "ccb_example_parent",
  "name": { "str": "example child" },
  "relative": { "weight": "50 g" },
  "proportional": { "price": 1.2 },
  "extend": { "flags": [ "WATER_FRIENDLY" ] },
  "delete": { "flags": [ "FRAGILE" ] }
}
```

- A directly specified top-level field normally replaces the inherited value.
- `relative` adds to a base value when its reader supports the operation.
- `proportional` multiplies a base value when its reader supports the operation.
- `extend` and `delete` add or remove members through a supported container reader.

These express intent; they are not guarantees. Using the blocks without `copy-from` is warned
or rejected. An unsupported type, field, or reader may report an error, be ignored, or use
special behavior. Support for `extend` on `ITEM.flags` does not imply support for every array
on every object.

### Abstracts, real objects, and chain depth

Use `abstract` for a stable base that a family of definitions always shares; it is not a real
in-game ID. Prefer one or two narrow inheritance levels. A deep chain makes one base edit
silently affect many objects or Mods and makes save compatibility and balance review harder.
Where a variant mechanism already represents display-only differences, it usually needs no
new inheritance chain.

### Specialized implementations

- `recipe_dictionary::load` performs its own recipe deferral and copy; inline requirements
  add replacement rules.
- An item group can copy only a previously loaded group with the same ID, and its loader reads
  `extend` specially.
- Some objects extend selected containers by default; others support only `copy-from` and not
  all four modification blocks.

Do not maintain a supposedly permanent complete list of supported types. Use the current
object registry to find the registration, then inspect the loader, reader, and tests.

### Review and validation

1. Identify which core or Mod supplies the base, its load order, and stable ID.
2. Confirm whether a direct field replaces, merges, or has specialized semantics.
3. Check the reader for units and ranges used by `relative` or `proportional`.
4. Cover the chain, missing bases, duplicate IDs, and finalization with an existing test or minimal Mod.
5. Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set.

If implementation evidence cannot prove that a field supports an inheritance operation,
write the complete definition explicitly or add a test first. A quiet load is not proof.

## History and attribution

Accepted inventory contributors: zihanZheng, ehughsbaird, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `76ca6fc5abc73f10dffb3ed498ff09916d84b6c9ce62382a15ab58d823cb365c`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/JSON_INHERITANCE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_INHERITANCE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/JSON_INHERITANCE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
