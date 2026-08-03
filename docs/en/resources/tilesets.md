---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: tilesets
title: 'Legacy migration draft: tilesets'
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
- doc/TILESET.md
- tools/gfx_tools/compose.py
- tools/gfx_tools/decompose.py
- .github/workflows/compose-tilesets.yml
source_symbols: []
source_queries: []
source_fingerprint: 60752d04ad6e528c8eafada2d0bf4f559f838591a7a555c1f59a07efa2427b9f
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8198b2ad1f1e4facca95c164daa4d85ab39aadb0be58bb677e680a6d497be3d7
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
risk_group: resources
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/tilesets/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tilesets/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/tilesets/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/tilesets/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/TILESET.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/TILESET.md
- path: tools/gfx_tools/compose.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tools/gfx_tools/compose.py
- path: tools/gfx_tools/decompose.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tools/gfx_tools/decompose.py
- path: .github/workflows/compose-tilesets.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/.github/workflows/compose-tilesets.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28tilesets%29%3A+&body=Document+ID%3A+tilesets%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: tilesets

This is the migration draft page for `tilesets`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `tilesets`
- Target: `resources/tilesets.md`
- Replacement: tilesets
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| tilesets | doc/TILESET.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Tileset authoring and composition

CCB distributions use compositing tilesets: individual PNG sprites, tile-entry JSON,
`tile_info.json`, and `tileset.txt` are converted by `tools/gfx_tools/compose.py` into tilesheets and
`tile_config.json`. Runtime-readable fields remain defined by the tiles loader; compose only
validates and transforms the source format it understands.

### Source layout and tile entries

A tile entry maps one or more game-entity `id` values to `fg` and `bg` sprite roots. It may use
rotations, weighted variants, `multitile`/`additional_tiles`, seasonal, gender, and item-variant
names, plus contextual layering. Terrain/furniture connections and rotation also depend on
`connect_groups`, `connects_to`, and `rotates_to` in game JSON. A tileset cannot create those runtime
relationships. Inventory hardcoded overlay and animation IDs from current `cata_tiles.cpp` and call
sites; a historical hand-maintained list can be incomplete.

`tile_info.json` describes default and per-sheet sprite sizes, offsets, pixel scale, sheet width,
and filler/fallback/exclusion behavior. Duplicate sprite roots, filler ordering, and cross-directory
references affect the result, so keep names unambiguous and review compose warnings.
`layering.json` contexts, item/field variants, offsets, and layers form a separate runtime contract.

### Composition, distribution, and validation

Current CI uses a command shaped like:

```sh
python3 tools/gfx_tools/compose.py --use-all --obsolete-fillers \
  --feedback CONCISE --format-json --loglevel INFO SOURCE DEST
```

Take actual flags from `compose.py --help`; options such as `--only-json`, `--fail-fast`, and palette
conversion change output or diagnostics. Compose into a temporary destination, review unused,
missing, and duplicate sprites plus generated JSON and image dimensions, then load it in a tiled
build. Test rotation, multitiles, fallback, zoom, seasons, overlays, and layering. Use
`decompose.py` only to convert an old indexed tileset, then manually organize its generated names
and directories.

Every artwork needs a redistributable license and traceable attribution; successful composition is
not license approval. `.github/workflows/compose-tilesets.yml` defines the current packaging matrix.
External tileset-repository content is not a CCB runtime contract, so pin and review its source and
revision.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `60752d04ad6e528c8eafada2d0bf4f559f838591a7a555c1f59a07efa2427b9f`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/TILESET.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/TILESET.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/TILESET.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
