---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.region-settings
title: 'Legacy migration draft: region settings'
language: en
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/REGION_SETTINGS.md
- src/regional_settings.cpp
- src/regional_settings.h
- data/json/region_settings/region_settings/regional_map_settings.json
- data/json/region_settings/region_settings/test_regional_map_settings.json
source_symbols:
- region_settings::load
- region_settings_forest::load
- region_settings_city::load
- region_settings_map_extras::load
source_queries: []
source_fingerprint: 1237c74189c1228b60889a1e83582ceea4a8a7b854ce41ed71146ae8ddb924df
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6d30eb9123f8bb92ad338298e7e986fedb541f4ff0930792e2e1d8da03f3ec40
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/region-settings/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-settings/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/region-settings/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-settings/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/REGION_SETTINGS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/REGION_SETTINGS.md
- path: src/regional_settings.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/regional_settings.cpp
- path: src/regional_settings.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/regional_settings.h
- path: data/json/region_settings/region_settings/regional_map_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/region_settings/region_settings/regional_map_settings.json
- path: data/json/region_settings/region_settings/test_regional_map_settings.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/region_settings/region_settings/test_regional_map_settings.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.region-settings%29%3A+&body=Document+ID%3A+json.region-settings%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: region settings

This is the migration draft page for `json.region-settings`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.region-settings`
- Target: `reference/json/region-settings.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/region-settings/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.region-settings | doc/JSON/REGION_SETTINGS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB region-settings structure

Region settings determine default terrain, ground cover, forests, rivers, lakes and oceans,
cities, road connections, highways, map extras, weather, and feature-flag filters for new
overmaps. They are not one open-ended object: multiple `region_settings_*` object types load
through separate factories and the main `region_settings` composes them by ID.

### Main region

The main object reads default OMT and ground cover, mandatory cities, weather, forest, river,
lake, ocean, highway, ravine, connections, map extras, terrain or furniture replacements, and
switches for roads, railways, specials, and neighbour connections. A valid region with
`id: "default"` must exist or finalization reports it.

Do not infer component fields from a legacy table. For example, the current
`region_settings_city` requires `city_size`, while forest, highway, lake, and map-extra
collections each have their own readers, defaults, and stable IDs.

### Extension and replacement

```jsonc
{
  "type": "region_settings",
  "id": "default",
  "copy-from": "default",
  "feature_flag_settings": {
    "extend": { "blacklist": [ "CCB_EXCLUDED" ] }
  }
}
```

Concrete `copy-from` and extension support depends on that field's reader. Same-ID Mod patches
depend on load order and can replace each other when several Mods alter the default region. A
new region is often easier to review than an implicit change to every world, but still needs
a world-selection entry and correct dimension or layout references.

### Cities, extras, and feature flags

City weighted lists reference OMTs or specials. Radius, size, and spacing affect distribution
but do not guarantee that every candidate can be placed. A map-extra collection combines a
chance with registered extra IDs and weights. Feature blacklists and whitelists combine with
overmap location flags; over-restricting them can leave empty candidates or broken networks.

A region change affects only overmaps that have not been generated. Explored regions are not
rebuilt. Document visual, resource, or road changes separately for new worlds or areas and for
already generated parts of old saves.

### Validation

Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set. Generate
complete overmaps from several seeds, recording the selected region, and inspect cities and
roads, forests and water, specials, extras, weather, and feature filters. Load an old world and
cross into a new overmap to check boundaries and connections.

See [overmap](overmap.md) for OMT and special relationships and [mapgen](mapgen.md) for local generation.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `1237c74189c1228b60889a1e83582ceea4a8a7b854ce41ed71146ae8ddb924df`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/REGION_SETTINGS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/REGION_SETTINGS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/REGION_SETTINGS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
