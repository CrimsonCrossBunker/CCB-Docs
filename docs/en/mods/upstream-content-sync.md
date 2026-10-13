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
verified_commit: 4ff8d9a6c64fc587a4dcf2f33082ca92c8945458
verified_at: '2026-10-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: c3082b54d8a14af8ed8261f0abd6647619a93727151d8da0761e5ee268590945
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/997
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/upstream-content-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/mods/upstream-content-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/mods/upstream-content-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/mods/upstream-content-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458
source_urls:
- path: data/json/mapgen/netherum/labyrinth_earth.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458/data/json/mapgen/netherum/labyrinth_earth.json
- path: data/json/region_settings/region_settings/regional_map_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458/data/json/region_settings/region_settings/regional_map_settings.json
- path: data/mods/MindOverMatter/dimensions/shoggothed_world/region_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458/data/mods/MindOverMatter/dimensions/shoggothed_world/region_settings.json
- path: data/upstream-changelog-20260921-20260928.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4ff8d9a6c64fc587a4dcf2f33082ca92c8945458/data/upstream-changelog-20260921-20260928.txt
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28mods.upstream-content-sync%29%3A+&body=Document+ID%3A+mods.upstream-content-sync%0ALanguage%3A+en%0AVerified+commit%3A+4ff8d9a6c64fc587a4dcf2f33082ca92c8945458%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Draft: core and bundled Mod content synchronization

This page accompanies CCB #997 and its data portions from 127 upstream PRs. Only explicitly rejected items are excluded from the frozen historical scope. A source PR may span native and data batches, so portion counts are not unique PR totals.

## Content and compatibility

The batch covers items, recipes, monsters, bundled Mods, forest drops, Exodii labyrinth content and a new MoM dimension. Conflicts apply actual object deltas while preserving CCB stable IDs, stacking, skills, materials and existing callbacks. MoM ravine-bottom terrain requires native loading fields from #996; math expressions and conditional Mod loading require #995 and #994. Data cannot merge alone.

Forest changes increase generation iterations. Seed 20261014 with 1000 regions per biome changed straight sticks from 235/235 to 273/886 for outer/dense forests. The generation step took about 40/141 ms. This samples groups, probabilities and iterations, not complete placement, frame rates or long-term saves.

The upstream weekly changelog is separate historical material. Mention there is not proof that an entry has been synchronized, tested or released in CCB.

## Acceptance limits

Earlier 14 Mod identities loaded in a cached engine with necessary prerequisite adapters. Later MoM data failed in that old engine because its native field was absent. A newly compiled matching combined engine must verify it. Contract, ledger and metadata checks do not replace loading acceptance. New gameplay and old saves remain untested.

Responsible human: LYHGLYTX.
