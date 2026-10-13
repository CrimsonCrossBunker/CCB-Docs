---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: mods.upstream-content-sync
title: 'Draft: core and bundled Mod content synchronization'
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
- data/json/mapgen/netherum/labyrinth_earth.json
- data/json/region_settings/region_settings/regional_map_settings.json
- data/mods/MindOverMatter/dimensions/shoggothed_world/region_settings.json
- data/upstream-changelog-20260921-20260928.txt
source_symbols: []
source_queries: []
source_fingerprint: 529cab08c982dc2364c967e7c0b522069ff08879567eea35c94192ec07069d63
authority: api-contract
verified_commit: eb8bfeabd8748176cc33aa2329b634d17bb61885
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 072e461e95c1d2fb3ed904f0b98c2469a8808ee67eab57fa90beeb9ac4b30326
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/upstream-content-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/mods/upstream-content-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/upstream-content-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/mods/upstream-content-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/eb8bfeabd8748176cc33aa2329b634d17bb61885
source_urls:
- path: data/json/mapgen/netherum/labyrinth_earth.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/data/json/mapgen/netherum/labyrinth_earth.json
- path: data/json/region_settings/region_settings/regional_map_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/data/json/region_settings/region_settings/regional_map_settings.json
- path: data/mods/MindOverMatter/dimensions/shoggothed_world/region_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/data/mods/MindOverMatter/dimensions/shoggothed_world/region_settings.json
- path: data/upstream-changelog-20260921-20260928.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/eb8bfeabd8748176cc33aa2329b634d17bb61885/data/upstream-changelog-20260921-20260928.txt
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.upstream-content-sync%29%3A+&body=Document+ID%3A+mods.upstream-content-sync%0ALanguage%3A+en%0AVerified+commit%3A+eb8bfeabd8748176cc33aa2329b634d17bb61885%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: core and bundled Mod content synchronization

This page accompanies CCB #997 and its data portions from 128 upstream PRs. Only explicitly rejected items are excluded from the frozen historical scope. A source PR may span native and data batches, so portion counts are not unique PR totals.

## Content and compatibility

The batch covers items, recipes, monsters, bundled Mods, forest drops, Exodii labyrinth content and a new MoM dimension. Conflicts apply actual object deltas while preserving CCB stable IDs, stacking, skills, materials and existing callbacks. MoM ravine-bottom terrain requires native loading fields from #996; math expressions and conditional Mod loading require #995 and #994. Data cannot merge alone.

Forest changes increase generation iterations. Seed 20261014 with 1000 regions per biome changed straight sticks from 235/235 to 273/886 for outer/dense forests. The generation step took about 40/141 ms. This samples groups, probabilities and iterations, not complete placement, frame rates or long-term saves.

The upstream weekly changelog is separate historical material. Mention there is not proof that an entry has been synchronized, tested or released in CCB.

## Acceptance limits

Matching game and test binaries built successfully on combined branch #1000 with Clang 23, Release, C++17, SDL3, tiles, sound, zh_CN and the sole Lua Platform v1. The valid scope contains 992 cases: the broad run passed 991 and exposed a sight-cache setup assumption in one visible-NPC fixture. After correcting that fixture, 528 combined Lua and vision cases passed 86,021 assertions. Six integration regressions passed 2,567 assertions. These are results from bounded runs, not a claim that one process passed all 992 cases.

The new binary passed independent loading checks for core and all 18 affected non-obsolete Mods (19 identities total), including MoM dimension and Xedra data. Loading does not establish every new gameplay path, old-save compatibility, actual GPUs, all desktop platforms or Android device acceptance.

Responsible human: LYHGLYTX.
