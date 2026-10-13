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
source_symbols: []
source_queries: []
source_fingerprint: 45bdb293e00ff84398ec125d6248085114b5a679525856dd868880016f4fd031
authority: api-contract
verified_commit: b071fca094b716cf409dd1ba74c90581b5fe63de
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a4a5f3472a5a864373bb97cbc37b8bd6a59553236f7e75364077415f0774f222
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/996
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/upstream-native-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/upstream-native-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/upstream-native-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/b071fca094b716cf409dd1ba74c90581b5fe63de
source_urls:
- path: src/activity_actor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/activity_actor.cpp
- path: src/activity_actor_definitions.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/activity_actor_definitions.h
- path: src/event.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/event.h
- path: src/regional_settings.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/regional_settings.h
- path: src/weather.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/weather.cpp
- path: src/main.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b071fca094b716cf409dd1ba74c90581b5fe63de/src/main.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.upstream-native-sync%29%3A+&body=Document+ID%3A+cpp.upstream-native-sync%0ALanguage%3A+en%0AVerified+commit%3A+b071fca094b716cf409dd1ba74c90581b5fe63de%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: native behavior synchronization

This page accompanies unmerged CCB #996. Combined acceptance is in progress.

## CCB adaptation

Door operations use saveable activities, including the contextual menu. Network prediction and server acknowledgement can execute the same checked activity synchronously. Costs belong to the actual actor; this path does not replace their existing activity or debit the local avatar for a remote actor. Opening location and vehicle ownership checks also use that actor.

Marloss/Mycus retains four established item callbacks and stable EOC IDs. Regional NPC multipliers scale CCB's existing frequency setting. New events append to the existing enum rather than renumbering it. Startup decomposition retains multiplayer, replay, Android and conditional Mod loading.

Source and generated inventories define weather, ravine terrain, equipment capacity and effect-condition contracts. Platform v1 remains the only Lua authoring entry point. Native primitive availability is not a claim that its full Lua selector or gameplay migration is complete.

## Acceptance limits

Shared dependency ordering failed before the fix and passed afterward. The math prerequisite passed two cases and 20 assertions; morale coverage is reading, not assignment. Ledger checks distinguish primitive evidence from full selector migration evidence.

Whole-batch compilation with crafting, rendering and data, followed by runtime checks, remains pending. Generated inventories and draft CI checks do not establish every-platform or old-save acceptance.

Responsible human: LYHGLYTX.
