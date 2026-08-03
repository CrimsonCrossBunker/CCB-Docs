---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.climbing-aids
title: 'Legacy migration draft: climbing aids'
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
- doc/JSON/CLIMBING.md
- src/climbing.cpp
- src/climbing.h
- data/json/climbing.json
source_symbols:
- climbing_aid::load
source_queries: []
source_fingerprint: 997faf1bea95578f5e2960f8dc83e65303b4e20c8d8c8d4c01ebe1e383e235b4
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 65767d284bcbd0680cdbbe6f657e4e26338b74bb1c4dc7f40e10082eb0b1c1b6
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Killa-bite, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/climbing-aids/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/climbing-aids/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/climbing-aids/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/climbing-aids/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/CLIMBING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/CLIMBING.md
- path: src/climbing.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/climbing.cpp
- path: src/climbing.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/climbing.h
- path: data/json/climbing.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/climbing.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.climbing-aids%29%3A+&body=Document+ID%3A+json.climbing-aids%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: climbing aids

This is the migration draft page for `json.climbing-aids`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.climbing-aids`
- Target: `reference/json/climbing-aids.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/climbing-aids/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.climbing-aids | doc/JSON/CLIMBING.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Climbing-aid contract

The `climbing_aid` generic factory builds a lookup by condition category and flag. Top-level `down`
and `condition` are mandatory and `slip_chance_mod` is optional. The project also requires a valid
`default` entry. Runtime constructs a fallback if missing, but consistency checking reports it.

### Condition

Type must be special, ter_furn, veh, item, character, or trait, and flag is mandatory. An item
condition also requires uses. A ter_furn condition may set range, default one. Other categories do
not read those specialized members. Uses is the item quantity consumed; condition detection and
route scanning decide availability.

### Down rules

max_height defaults to one and zero disables downward use. allow_remaining_height defaults true and
easy_climb_back_up defaults zero. When enabled, menu_text and confirm_text are mandatory. Setting
deploy_furn also makes menu_cant and a one-byte menu_hotkey mandatory; otherwise both are optional and
the hotkey is at most one byte. Cost kcal, thirst, damage, and pain apply per descended level.

Furniture deployment needs open-air, existing furniture, vehicle or creature, maximum-height, and
partial-descent review. The menu normally includes all deployable aids plus the safest non-deploying
aid, so slip modifier affects selection rather than being an isolated display number.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. In a multi-Z fixture cover descent
height, partial descent, item consumption, deployment collisions, vehicle-part length, terrain flags,
trait and character conditions, slipping, costs, and return difficulty. New boundaries need focused
climbing tests and save reload coverage.

## History and attribution

Accepted inventory contributors: Killa-bite, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `997faf1bea95578f5e2960f8dc83e65303b4e20c8d8c8d4c01ebe1e383e235b4`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/CLIMBING.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/CLIMBING.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/CLIMBING.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
