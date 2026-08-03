---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.terrain-furniture-transforms
title: 'Legacy migration draft: terrain furniture transforms'
language: en
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/TER_FURN_TRANSFORM.md
- src/magic_ter_fur_transform.cpp
- src/magic_ter_furn_transform.h
- src/mapgen.cpp
- data/json/mapgen/haunting.json
source_symbols:
- ter_furn_transform::load
- ter_furn_data<T>::load
source_queries: []
source_fingerprint: 7a7d7f8f3faec648766f1b2b622d9ba14c2f24702c6e4a2954b9b65e8ee93188
authority: docs-explanation
verified_commit: 80828049edb3adf2a13bb2912a19373dc4e69f32
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0571a43fafca38966d551927fdb7bbd8d47e5e8dc45face4558c7e228b976b79
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/terrain-furniture-transforms/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-furniture-transforms/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/terrain-furniture-transforms/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-furniture-transforms/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/80828049edb3adf2a13bb2912a19373dc4e69f32
source_urls:
- path: doc/JSON/TER_FURN_TRANSFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/TER_FURN_TRANSFORM.md
- path: src/magic_ter_fur_transform.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/magic_ter_fur_transform.cpp
- path: src/magic_ter_furn_transform.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/magic_ter_furn_transform.h
- path: src/mapgen.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/src/mapgen.cpp
- path: data/json/mapgen/haunting.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/data/json/mapgen/haunting.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.terrain-furniture-transforms%29%3A+&body=Document+ID%3A+json.terrain-furniture-transforms%0ALanguage%3A+en%0AVerified+commit%3A+80828049edb3adf2a13bb2912a19373dc4e69f32%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: terrain furniture transforms

This is the migration draft page for `json.terrain-furniture-transforms`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.terrain-furniture-transforms`
- Target: `reference/json/terrain-furniture-transforms.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/terrain-furniture-transforms/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.terrain-furniture-transforms | doc/JSON/TER_FURN_TRANSFORM.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB terrain and furniture transforms

A `ter_furn_transform` is a named reusable tile-conversion table. It matches terrain,
furniture, fields, and traps independently, then selects a replacement from a weighted
`result`. Matching terrain does not automatically create related furniture.

### Basic definition

```jsonc
{
  "type": "ter_furn_transform",
  "id": "ccb_example_transform",
  "terrain": [
    {
      "valid_terrain": [ "t_sand" ],
      "result": [ [ "t_dirt", 4 ], "t_grass" ],
      "message": "The sand shifts.",
      "message_good": true
    }
  ]
}
```

A plain result has weight one; a two-element array supplies a weight. `message_good` defaults
to true. Terrain and furniture can also match `valid_flags`; fields and traps use their own
valid-ID members. Use `ter_furn_transform::load` for the current member names and flag support.

### Matching and conflicts

The loader maps each valid ID or flag to transformation data. When several rules cover one
input, do not use container insertion order as a content-priority mechanism. Keep match sets
disjoint or add a test proving the intended result. Clearing values such as `f_null` and
`fd_null` are real IDs in their systems; JSON null is not a replacement.

Mapgen placings, radius EOC effects, spells, and other callers can invoke a transform. The caller
defines position, range, talkers, repetition, and message display. A transform does not remember
that it already ran. Repetition must be deliberate, especially with random results or possible
A-to-B-to-A cycles.

### Validation

1. Check every valid and result terrain, furniture, field, trap ID, and flag.
2. Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set.
3. Test every input category, no match, several flags, weight boundaries, and null or clear results.
4. Test range, z-level, repeated execution, and messages from each real call site.
5. Run `mapgen_function_test` for mapgen callers and the relevant focused test for EOC or spell callers.

Use a transform for declarative same-tile type replacement. Put cross-tile behavior, condition
chains, and side effects in the EOC or mapgen caller instead of relying on rule-overlap accidents.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `7a7d7f8f3faec648766f1b2b622d9ba14c2f24702c6e4a2954b9b65e8ee93188`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/TER_FURN_TRANSFORM.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/TER_FURN_TRANSFORM.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/TER_FURN_TRANSFORM.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
