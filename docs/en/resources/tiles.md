---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: resources.tiles
title: Tilesets
language: en
status: active
doc_type: reference
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- doc/TILESET.md
- gfx/tile_config_template.json
- src/sdltiles.h
- .github/workflows/compose-tilesets.yml
source_symbols:
- void load_tileset()
source_queries:
- TILESETS
source_fingerprint: 548f727df0a5e71280243013c4da40bb2aa4e81cbcd4b78459286334a318b5c9
authority: source-and-tests
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 61061f9df4b9952d28240b82ab556c77960a44966a74848a439c9063fb89270b
prerequisites:
- platforms.ui
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: resources-tiles
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/tiles/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tiles/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/tiles/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tiles/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/TILESET.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/TILESET.md
- path: gfx/tile_config_template.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/gfx/tile_config_template.json
- path: src/sdltiles.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/sdltiles.h
- path: .github/workflows/compose-tilesets.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/compose-tilesets.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28resources.tiles%29%3A+&body=Document+ID%3A+resources.tiles%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Tilesets

Tilesets map game IDs and variants to sprites and tilesheets. Runtime loading, composition,
package metadata, ID fallback, rotations, multitile/connect rules, overlays, and licensing are
all part of the contract.

## Authoritative paths

- `doc/TILESET.md` describes the supported tile JSON concepts and composition model.
- `gfx/` contains bundled tileset metadata and assets; `gfx/tile_config_template.json` is a
  starting shape, not a substitute for a real load.
- `src/sdltiles.*` and the tile loader define runtime behavior.
- `.github/workflows/compose-tilesets.yml` defines checked composition and distributable assets.

## Ownership and IDs

Game JSON owns entity IDs. A tile entry references those IDs and may add variants, rotations,
multitile pieces, seasonal/gender forms, overlays, or fallback. Renaming a game ID without
coordinating tiles can silently degrade to fallback art even when JSON still loads.

## Contributor workflow

Keep source sprites, tile entry JSON, tilesheet metadata, and license/attribution together.
Compose with the workflow/tool used by the repository, review its warnings, then launch the
result in a tiles build. Do not edit a generated tilesheet when the compositing source is the
maintained input.

## Validation

Validate JSON/composition, missing and duplicate IDs, sprite bounds, fallback behavior,
rotations/connections, overlays, zoom/scaling, both map and overmap views, and a clean packaged
load. Sample changed IDs in game; composition success alone cannot prove visual correctness.

## Performance and packaging

Atlas dimensions, texture count, fallback chains, and repeated variant lookup affect startup,
memory, and redraw. Keep generated sheets and source art roles explicit. Large composed output
can be a release/CI artifact when the repository workflow treats it as generated.

## Licensing

Every imported sprite needs compatible licensing and attribution. “From an upstream tileset”
is not sufficient provenance: record source repository/path, author where available, license,
and transformation.
