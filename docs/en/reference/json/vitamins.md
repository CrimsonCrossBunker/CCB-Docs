---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.vitamins
title: 'Legacy migration draft: vitamins'
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
- doc/JSON/VITAMIN.md
- src/vitamin.cpp
- src/vitamin.h
- data/json/vitamin.json
- tests/vitamin_test.cpp
source_symbols:
- vitamin::load
source_queries: []
source_fingerprint: a7c81f55e1988cc468b2d6b426ffe2e675666e6607c63a88131c2bda776767d1
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5f734e6923fa7a31bfb07e3adee5734ce05f8393bcc1dfdd5e089b5d7aa53638
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: zihanZheng, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/vitamins/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vitamins/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/vitamins/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vitamins/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/VITAMIN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/VITAMIN.md
- path: src/vitamin.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/vitamin.cpp
- path: src/vitamin.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/vitamin.h
- path: data/json/vitamin.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/vitamin.json
- path: tests/vitamin_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/vitamin_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.vitamins%29%3A+&body=Document+ID%3A+json.vitamins%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: vitamins

This is the migration draft page for `json.vitamins`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.vitamins`
- Target: `reference/json/vitamins.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/vitamins/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.vitamins | doc/JSON/VITAMIN.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## A `vitamin` object is not only a nutrient

CCB's `vitamin` registry is a general system for quantities in a character that change over time.
`vit_type` currently accepts `vitamin`, `toxin`, `drug`, and `counter`. First-party data uses it not
only for calcium, iron, and vitamin C, but also drug doses, mutagen primers, blood-related counters,
allergens, and hidden state. The object type name does not guarantee appearance in nutrition UI.

### Loader fields

In addition to generic-factory `id` and `type`, a new definition must provide `name`, `vit_type`,
`min`, and `rate`. `max` is optional and currently defaults to `0`. `deficiency` and `excess`
reference effect types. `disease` and `disease_excess` are quantity ranges whose order maps to
effect intensity. `weight_per_unit` converts mass into internal units. Every `decays_into` entry is
a target vitamin ID and signed adjustment applied separately when one unit is naturally metabolized.
`flags` is a string set; confirm each flag's consumer in current code and data.

```json
{
  "type": "vitamin",
  "id": "example_counter",
  "vit_type": "counter",
  "name": { "str": "Example counter" },
  "min": 0,
  "max": 100,
  "rate": "1 h",
  "excess": "example_effect",
  "disease_excess": [ [ 10, 49 ], [ 50, 100 ] ]
}
```

This illustrates structure and is not a proposed first-party ID. The loader accepts either order
for each range endpoint, but overlaps and gaps still create hard-to-understand results. Design
continuous, testable thresholds.

## Inheritance, units, and validation

Vitamins support `copy-from` through `generic_factory`. Current tests cover scalar overrides and
`extend` or `delete` for `flags`, `disease`, `disease_excess`, and `decays_into`. Flags deduplicate as
a set. Duplicate decay targets remain independent rules and do not sum automatically. When a mod
overrides an existing `id`, the last loaded definition wins, so load-order compatibility matters.

Nutritional values in food JSON are commonly expressed as RDA percentages, while other types use
their internal units. `rate` controls daily absorption and decay conversion, and
`weight_per_unit` controls mass conversion. Run JSON formatting and loading, vitamin consistency,
and focused `[vitamin]` tests for a new object. Cover effect IDs, boundary amounts, inheritance,
natural decay, simplified nutrition, display flags, ingestion delay, and save/reload. Do not freeze
the legacy MME table or current first-party values as a permanent schema.

## History and attribution

Accepted inventory contributors: zihanZheng, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `a7c81f55e1988cc468b2d6b426ffe2e675666e6607c63a88131c2bda776767d1`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/VITAMIN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/VITAMIN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/VITAMIN.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
