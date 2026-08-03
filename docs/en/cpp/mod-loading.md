---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.mod-loading
title: Mod-loading subsystem
language: en
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
- api-user
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/mod_manager.h
- src/mod_manager.cpp
- src/worldfactory.cpp
- tests/worldfactory_test.cpp
source_symbols:
- class mod_manager
source_queries: []
source_fingerprint: 73f484f3d7f4222d4a0d71cd4fb98672a4cdca2f7ad7068273531c96ba429d32
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6a5379b1d791d0685dd13a81b84bff6f036d60fd00f92f78e1e3b782671038b8
prerequisites:
- compatibility.mods
depends_on:
- cpp.save
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: mod-loading
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/mod-loading/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mod-loading/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/mod-loading/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/mod-loading/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/mod_manager.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/mod_manager.h
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/mod_manager.cpp
- path: src/worldfactory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/worldfactory.cpp
- path: tests/worldfactory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/worldfactory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.mod-loading%29%3A+&body=Document+ID%3A+cpp.mod-loading%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Mod loading

## Responsibility

`mod_manager` discovers `MOD_INFO`, builds the dependency graph, selects usable/default mods,
records each world's ordered active list, applies declared mod migrations/removals, and supplies
the ordered source set to data loading.

## Entry points

Read `src/mod_manager.h` and `src/mod_manager.cpp`. `refresh_mod_list`, `load_modfile`,
`load_mods_list`, `check_mods_list`, and `worldfactory` world creation/loading are the main
entry points.

## Data ownership

The manager owns discovered `MOD_INFORMATION`, dependency state, and migration maps. A `WORLD`
owns its active ordered mod IDs. Individual factories own objects loaded from those mod paths.

## Dependencies

Mod loading depends on filesystem paths, `modinfo.json`, dependency-tree rules, worldfactory,
JSON dispatch, stable IDs, obsoletion/migration data, localization, and optional Lua manifests.

## Lifecycle

Startup discovers core and user mod directories, validates metadata and dependencies, a world
chooses an ordered set, missing/renamed mods are reconciled, then data and scripts load in that
order; the list persists with the world.

## Invariants

Mod IDs are unique and valid; a mod cannot depend on itself; dependencies precede dependents;
the world order has no duplicates; missing mods require an explicit migration or user decision;
and source attribution retains its mod origin.

## Extension points

Express metadata, dependencies, conflicts, obsoletion, and migration in data. New loader phases
must preserve deterministic order, failure diagnostics, source attribution, and world checks.

## Serialization

`mods.json` stores the world's ordered mod IDs; manager registries are rediscovered. Renames or
removals need migration entries so existing worlds are not silently rewritten or corrupted.

## Tests

Use `tests/worldfactory_test.cpp`, JSON loading, dependency errors, duplicate IDs, missing mods,
migrations, conflicts, and a complete example-mod load. Include Lua manifest validation when a
mod contains Lua.

## Performance

Discovery and JSON load are startup costs. Avoid repeated directory traversal, unstable sorting,
and reloading whole registries for one metadata query.

## CCB divergence

CCB's bundled mods, migration tables, Lua v5 manifests, and accepted upstream content form its
own compatibility set. Do not substitute another project's default mod list or load policy.

## Technical debt

Discovery, user decisions, dependency resolution, and data loading are coupled through startup.
Future separation must preserve exact order and diagnostics before changing behavior.
