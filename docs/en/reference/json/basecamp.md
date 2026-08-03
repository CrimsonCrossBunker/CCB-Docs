---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.basecamp
title: 'Legacy migration draft: basecamp'
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
- doc/JSON/BASECAMP.md
- src/basecamp.cpp
- src/faction_camp.cpp
- src/recipe.cpp
- data/json/recipes/basecamps/components.json
- tests/faction_camp_test.cpp
source_symbols:
- basecamp::available_upgrades
- recipe::load
- basecamp::define_camp
source_queries: []
source_fingerprint: c0cfebafece179418df8534979262e7194922117093218d38658a260291a55f2
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7c5d86708e85d581fc90919db51be582cac06f7e3ceba31d9e3103c25ed40da5
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/basecamp/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/basecamp/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/basecamp/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/basecamp/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/BASECAMP.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/BASECAMP.md
- path: src/basecamp.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/basecamp.cpp
- path: src/faction_camp.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/faction_camp.cpp
- path: src/recipe.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/recipe.cpp
- path: data/json/recipes/basecamps/components.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/recipes/basecamps/components.json
- path: tests/faction_camp_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/faction_camp_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.basecamp%29%3A+&body=Document+ID%3A+json.basecamp%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: basecamp

This is the migration draft page for `json.basecamp`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.basecamp`
- Target: `reference/json/basecamp.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/basecamp/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.basecamp | doc/JSON/BASECAMP.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Basecamp data spans several contracts

A basecamp upgrade is not one object type. It combines blueprint recipes, `update_mapgen`,
`recipe_group`, overmap terrain, and runtime camp state. Before changing one file, trace the complete
ID chain through `basecamp::available_upgrades`, `recipe::load`, and current first-party camp data.

### Blueprint recipes

An ordinary recipe with `construction_blueprint` enters the blueprint path. Its loader reads
`blueprint_name`, `blueprint_parameter_names`, resources, provides, requires, excludes, and needs.
Every blueprint automatically provides and excludes its own result, making it non-repeatable by
default.

`blueprint_provides`, `blueprint_requires`, and `blueprint_excludes` are camp-feature counters whose
amount defaults to one; they are not a global feature registry. Code assigns mission or camp meaning
to selected conventional IDs. A new string has meaning only when a consumer reads it, so the keyword
table in historical prose is not an authoritative complete list.

### Requirements and mapgen

When `blueprint_needs` is absent and `check_blueprint_needs` is true, finalization calculates needs
from mapgen. A parameterized blueprint cannot also rely on explicit needs. `construction_blueprint`
must name an executable update mapgen, and parameter names must cover and translate every choice
shown to the player.

Initial camps and expansions also depend on recipe-group terrain matching, a corresponding OMT, and
mapgen. A Mod must declare dependencies before safely referring to another Mod's recipe, terrain, or
mapgen IDs.

### Validation checklist

Exercise every requires, provides, and excludes branch, repeat prevention, resource items, mapgen
parameters, and the resulting upgraded map. Run formatting, `make -j2 json-check`, complete
`--check-mods`, and a focused `tests/faction_camp_test.cpp` case. Use the repository's
`tools/update_blueprint_needs.py` for calculated requirements and review every result instead of
copying historical examples.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `c0cfebafece179418df8534979262e7194922117093218d38658a260291a55f2`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/BASECAMP.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/BASECAMP.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/BASECAMP.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
