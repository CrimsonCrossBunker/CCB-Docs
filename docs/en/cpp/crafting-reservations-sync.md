---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.crafting-reservations-sync
title: 'Draft: crafting reservations and temporary inventory'
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
- src/crafting.cpp
- src/craft_reservation_search.cpp
- src/temp_crafting_inventory.cpp
- src/lua_platform_crafting.cpp
- src/lua_platform_items.cpp
- src/veh_interact.cpp
- src/version.cmake
source_symbols:
- Character::crafting_inventory
- veh_interact::installation_requirement_availability
source_queries:
- independent_contents
- zero_move_dispatches
- CMAKE_MATCH_1
source_fingerprint: 2b68b6f557a1b5934dd6ce9719a7776f979f0e96ac481021c9f39d680105f052
authority: api-contract
verified_commit: 0a9822532c83189bc431631fd5e2b05a632460c6
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 16b662752793ebd42f81224f79c63633f078f476be19cf928de5097e8189e9ba
prerequisites:
- cpp.lua-bridge
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/crafting-reservations-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting-reservations-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/crafting-reservations-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/crafting-reservations-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/0a9822532c83189bc431631fd5e2b05a632460c6
source_urls:
- path: src/crafting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/crafting.cpp
- path: src/craft_reservation_search.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/craft_reservation_search.cpp
- path: src/temp_crafting_inventory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/temp_crafting_inventory.cpp
- path: src/lua_platform_crafting.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/lua_platform_crafting.cpp
- path: src/lua_platform_items.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/lua_platform_items.cpp
- path: src/veh_interact.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/veh_interact.cpp
- path: src/version.cmake
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/0a9822532c83189bc431631fd5e2b05a632460c6/src/version.cmake
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.crafting-reservations-sync%29%3A+&body=Document+ID%3A+cpp.crafting-reservations-sync%0ALanguage%3A+en%0AVerified+commit%3A+0a9822532c83189bc431631fd5e2b05a632460c6%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: crafting reservations and temporary inventory synchronization

This page describes an unmerged crafting branch and remains a draft. Source and tests define behavior. Compilation of the combined version, Mod loading and platform CI are still pending.

## Reservation units

Unattended steps reserve actual item identities and relevant power resources. Other automation skips reserved objects. Pauses retain their reason, so repeated checks do not repeat the same warning.

CCB worn storage differs from upstream legacy inventory. Independent items in storage pockets form separate provider units, while magazine and modification pockets remain part of their tool. Reserving one tool does not hide every independent tool in its backpack. Moving a container holding reserved objects remains protected as a whole.

## Temporary inventory and Lua

Temporary crafting inventory holds references plus necessary pseudo-items or copies. It is not persistent character inventory. References must remain valid during queries; snapshots cannot change ownership or bypass reservations.

Lua continues through existing Platform v1 crafting, item and task services. Camp and Lua queries use the new inventory type while retaining escrow, refunds, identity checks and duplicate-settlement prevention. No second Lua interface is added.

## Vehicle installation and zone sorting

Installation checks take one snapshot of available component types, reject impossible groups, then perform full quantity, quality and actor checks. Temporary inventory must not cause every part to rescan thousands of items.

Zone sorting retains CCB direct delivery and batch handling costs. A refused cart load can fall back to character carrying. Zero-move dispatches are bounded per turn and their count is cleared before routing hands off activity state.

## Acceptance limits

All 288 cases have passing evidence: one domain run passed 287; the corrected final fixture separately passed 26 assertions. Another focused run passed eight cases and 89 assertions. Coverage includes reservations, temporary inventory, finite water, installation queries, zone sorting and Lua escrow recovery. This does not establish acceptance of the combined version, every platform or all old saves.

CMake owns the version header. An unchanged version preserves its timestamp instead of repeatedly triggering compilation. A real-generator regression failed before the fix and passed afterward.

Sources and attribution: [CDDA #88559](https://github.com/CleverRaven/Cataclysm-DDA/pull/88559): dobbry-vechur; [CDDA #88647](https://github.com/CleverRaven/Cataclysm-DDA/pull/88647): dobbry-vechur; [CDDA #88606](https://github.com/CleverRaven/Cataclysm-DDA/pull/88606): Curtis Merrill; [CDDA #88656](https://github.com/CleverRaven/Cataclysm-DDA/pull/88656): dobbry-vechur; [CDDA #88767](https://github.com/CleverRaven/Cataclysm-DDA/pull/88767): dobbry-vechur. Responsible human: LYHGLYTX.
