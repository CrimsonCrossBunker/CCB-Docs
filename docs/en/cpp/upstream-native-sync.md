---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.upstream-native-sync
title: 'Draft: native behavior synchronization'
language: en
status: draft
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
- src/activity_actor.cpp
- src/activity_actor_definitions.h
- src/event.h
- src/regional_settings.h
- src/weather.cpp
- src/main.cpp
- src/lua_platform_runtime_services.cpp
- src/veh_type.cpp
- src/character_inventory.cpp
- src/recipe_dictionary.cpp
- tests/lua_platform_environment_predicate_test.cpp
- tests/lua_platform_effects_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: a80d78267dc97036358b0302ad889a4043deaf8d31273adcb26ecbb070591d10
authority: api-contract
verified_commit: eb8bfeabd8748176cc33aa2329b634d17bb61885
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e8b0038844e89009ee18be20605c85e55b3a7694f20777597de133e4318495c8
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- lua-contract
api_version: '1'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/1000
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/upstream-native-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/upstream-native-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/eb8bfeabd8748176cc33aa2329b634d17bb61885
source_urls:
- path: src/activity_actor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/activity_actor.cpp
- path: src/activity_actor_definitions.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/activity_actor_definitions.h
- path: src/event.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/event.h
- path: src/regional_settings.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/regional_settings.h
- path: src/weather.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/weather.cpp
- path: src/main.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/main.cpp
- path: src/lua_platform_runtime_services.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/lua_platform_runtime_services.cpp
- path: src/veh_type.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/veh_type.cpp
- path: src/character_inventory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/character_inventory.cpp
- path: src/recipe_dictionary.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/src/recipe_dictionary.cpp
- path: tests/lua_platform_environment_predicate_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/tests/lua_platform_environment_predicate_test.cpp
- path: tests/lua_platform_effects_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/tests/lua_platform_effects_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.upstream-native-sync%29%3A+&body=Document+ID%3A+cpp.upstream-native-sync%0ALanguage%3A+en%0AVerified+commit%3A+eb8bfeabd8748176cc33aa2329b634d17bb61885%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: native behavior synchronization

This page accompanies unmerged CCB #996. Combined acceptance has completed the bounded checks below.

## CCB adaptation

Door operations use saveable activities, including the contextual menu. Network prediction and server acknowledgement can execute the same checked activity synchronously. Costs belong to the actual actor; this path does not replace their existing activity or debit the local avatar for a remote actor. Opening location and vehicle ownership checks also use that actor.

Marloss/Mycus retains four established item callbacks and stable EOC IDs. Regional NPC multipliers scale CCB's existing frequency setting. New events append to the existing enum rather than renumbering it. Startup decomposition retains multiplayer, replay, Android and conditional Mod loading.

Source and generated inventories define weather, ravine terrain, equipment capacity and effect-condition contracts. Platform v1 remains the only Lua authoring entry point. Native primitive availability is not a claim that its full Lua selector or gameplay migration is complete.

## Acceptance limits

Shared dependency ordering failed before the fix and passed afterward. The math prerequisite passed two cases and 20 assertions; morale coverage is reading, not assignment. Ledger checks distinguish primitive evidence from full selector migration evidence.

Matching game and test binaries built successfully on combined branch #1000 with Clang 23, Release, C++17, SDL3, tiles, sound, zh_CN and the sole Lua Platform v1. The valid scope contains 992 cases: the broad run passed 991 and exposed a sight-cache setup assumption in one visible-NPC fixture. After correcting that fixture, 528 combined Lua and vision cases passed 86,021 assertions. Six integration regressions passed 2,567 assertions. These are results from bounded runs, not a claim that one process passed all 992 cases.

The new binary passed independent loading checks for core and all 18 affected non-obsolete Mods (19 identities total), including MoM dimension and Xedra data. Loading does not establish every new gameplay path, old-save compatibility, actual GPUs, all desktop platforms or Android device acceptance.

Integration aligns negative trap radii in Lua and native iteration: both return an empty result. Vehicle fuel inference excludes liquid-fuel magazine wells while allowing auxiliary battery wells with integral liquid storage; existing pressurized-tank reload rules remain intact.

Only 20 explicitly rejected entries were excluded. Of the remaining 248, 233 were adapted or confirmed equivalent to existing CCB behavior. Fifteen seasoning, ownership, legacy-inventory, portrait-dialogue and help changes remain retained for review, rather than rejected.

Responsible human: LYHGLYTX.
