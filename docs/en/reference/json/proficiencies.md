---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.proficiencies
title: 'Legacy migration draft: proficiencies'
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
- doc/JSON/PROFICIENCY.md
- src/proficiency.cpp
- src/proficiency.h
- data/json/proficiencies/misc.json
- tests/crafting_test.cpp
source_symbols:
- proficiency::load
- proficiency_category::load
- proficiency_migration::load
source_queries: []
source_fingerprint: f5656b361798c328b6a002d40cc8abf6e325f847c7da9380c240b26c721e0f8f
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f2d9d2740cba8c17d9593401b953d2668198d3bb0d709238ad1b090c450019bf
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/proficiencies/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/proficiencies/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/proficiencies/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/proficiencies/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/PROFICIENCY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/PROFICIENCY.md
- path: src/proficiency.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/proficiency.cpp
- path: src/proficiency.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/proficiency.h
- path: data/json/proficiencies/misc.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/proficiencies/misc.json
- path: tests/crafting_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/crafting_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.proficiencies%29%3A+&body=Document+ID%3A+json.proficiencies%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: proficiencies

This is the migration draft page for `json.proficiencies`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.proficiencies`
- Target: `reference/json/proficiencies.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/proficiencies/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.proficiencies | doc/JSON/PROFICIENCY.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Proficiencies, categories, and migrations

A proficiency is knowledge tracked separately from skills. Recipes and activities decide when it is
learned or consumed; the JSON definition supplies identity, prerequisites, default penalties,
learning properties, and consumer-specific bonuses. Dependencies form a general directed graph, not
necessarily a tree.

### Three object types

A `proficiency` requires name, description, can_learn, and category. Optional fields include
teachable (default true), time_to_learn, required_proficiencies, ignore_focus, default time, skill,
and weakpoint modifiers, and bonuses. Legacy `default_fail_multiplier` is converted with a warning;
new data uses `default_skill_penalty`.

A `proficiency_category` requires name and description; its factory owns the ID. A
`proficiency_migration` requires from and optionally has to. Missing to removes the old proficiency;
present to must reference a valid ID. Migration is part of save compatibility when a public ID is
deleted or renamed.

### Bonuses and consumers

A bonus entry requires type and value, but a bonus key gains meaning only from a particular activity
or attack consumer. Successful JSON parsing does not prove code consumes it. A new key or type needs
consumer implementation, documentation, and tests. Recipes can override default time, skill,
learning, and maximum experience, so inspect expanded recipes.

### Validation

Check categories, every prerequisite, cycles or unreachable nodes, learnable and teachable states,
migrations, and referencing recipes, books, and activities. Run formatting, `make -j2 json-check`,
Mod `--check-mods`, and focused crafting, learning, and save-migration tests for missing, partial,
known, and old-ID states. The generated proficiency index aids discovery but does not replace loader
and consumer review.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `f5656b361798c328b6a002d40cc8abf6e325f847c7da9380c240b26c721e0f8f`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/PROFICIENCY.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/PROFICIENCY.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/PROFICIENCY.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
