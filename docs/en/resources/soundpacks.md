---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: soundpacks
title: 'Legacy migration draft: soundpacks'
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
- doc/SOUNDPACKS.md
- src/sdlsound.cpp
- src/sdlsound.h
source_symbols:
- load_soundset
- sfx::load_sound_effects
- sfx::load_playlist
source_queries: []
source_fingerprint: 0246b49b05f9e86197e17d62765a99f0194dc121017d1108d02e49e787ffa0ab
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e15b56a2ff54a305a03790977519ddf3aa98e4f093e51d6212c174461fa6cbb0
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/soundpacks/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/resources/soundpacks/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/resources/soundpacks/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/resources/soundpacks/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/SOUNDPACKS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/SOUNDPACKS.md
- path: src/sdlsound.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/sdlsound.cpp
- path: src/sdlsound.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/sdlsound.h
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28soundpacks%29%3A+&body=Document+ID%3A+soundpacks%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: soundpacks

This is the migration draft page for `soundpacks`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `soundpacks`
- Target: `resources/soundpacks.md`
- Replacement: soundpacks
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| soundpacks | doc/SOUNDPACKS.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Soundpack contracts

A soundpack is a directory under `data/sound/` with `soundpack.txt`. `NAME` is the unique ID used by
the option and `VIEW` is its display name. `load_soundset` resolves the current choice, falls back to
`basic` when needed, and loads JSON from the directory through `DynamicDataLoader`. Sound JSON
loaders return early when audio initialization has not succeeded.

### SFX and playlists

A `sound_effect` requires `id` and `files`; `volume` defaults to 100. `variant` may be a string or an
array and defaults to `default`. `season`, `is_indoors`, and `is_night` become part of the lookup key.
Multiple files are random alternatives for the same key, and paths are relative to the soundpack.
Actual fallback is implemented by the `sfx_resources` lookup. Some call sites require an exact
variant, so not every ID is guaranteed to fall back to `default`.

`sound_effect_preload` warms the listed keys without changing playback semantics. A `playlist`
contains a `playlists` array; each entry has an ID, optional shuffle, and `{file, volume}` entries.
A later definition of the same ID replaces its map entry. Current `music` call sites define
activation and priority; the historical four-ID list is not guaranteed to be a complete registry.

### Inventory and validation

There is no permanently complete hand-maintained SFX ID/variant list. Generate an inventory from all
`play_variant_sound`, ambient, vehicle, UI, and music call sites, then compare it with soundpack JSON.
Check missing or undecodable files, empty lists, duplicate keys, exact/default fallback, seasonal,
indoor, and night combinations, preload, shuffle, compounded volume, loops/channels, distance, pan,
pitch, pack switching, and disabled sound. Distribution also requires author, source, and compatible
license records. A test-mode or no-audio-backend load is not proof of real playback.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `0246b49b05f9e86197e17d62765a99f0194dc121017d1108d02e49e787ffa0ab`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/SOUNDPACKS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/SOUNDPACKS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/SOUNDPACKS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
