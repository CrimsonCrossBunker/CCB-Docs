---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: cpp.save
title: Save subsystem
language: en
status: active
doc_type: reference
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending human review
source_paths:
- src/savegame.cpp
- src/savegame_json.cpp
- src/savegame_legacy.cpp
- tests/worldfactory_test.cpp
source_symbols:
- const int savegame_version = 39;
source_queries: []
source_fingerprint: 50026553eb625ef2ef0861270fc41c0a232cfaa1e00e471a34e5b59055aa0cb5
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 1539fd64a9a2b9434540c1e4f16a32720c008c1fdefe17c80a5cee834eae7a3a
prerequisites:
- compatibility.save
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: save-compatibility
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/save/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/save/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/cpp/save/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/cpp/save/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/savegame.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame_json.cpp
- path: src/savegame_legacy.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/savegame_legacy.cpp
- path: tests/worldfactory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/tests/worldfactory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28cpp.save%29%3A+&body=Document+ID%3A+cpp.save%0ALanguage%3A+en%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Save system

## Responsibility

The save system persists a world as versioned JSON and supporting files: game/global state,
avatar and NPCs, monsters, overmaps, submaps, vehicles, items, activities, factions, missions,
map memory, and mod order, while loading older supported representations.

## Entry points

Start in `src/savegame.cpp`, `src/savegame_json.cpp`, and `src/savegame_legacy.cpp`. The constant
`savegame_version`, parsed `savegame_loading_version`, top-level game load/store, and each type's
`serialize` / `deserialize` pair are the compatibility boundary.

## Data ownership

Each runtime owner serializes its durable state; the world directory owns the file set. The
save layer coordinates records but must not become a second runtime owner. Caches, pointers,
windows, and local coordinate views are reconstructed.

## Dependencies

Saving depends on filesystem/path APIs, JSON archives, worldfactory, map/overmap storage, every
durable subsystem's serializer, IDs, mod order, and migration/default logic.

## Lifecycle

A new world starts at the current version; saves write a version marker and records; loading
detects the stored version, applies field defaults and legacy conversions, reconnects IDs and
ownership, rebuilds caches, then returns a live world.

## Invariants

Loading old supported fields is non-destructive; one object is serialized by its owner; IDs and
absolute coordinates remain stable; failed writes do not masquerade as complete saves; and the
version only advances with intentional migration support.

## Extension points

Add serialization beside the owning type, use named fields and safe defaults, and add explicit
version-gated migration only when necessary. Never serialize raw pointers or derived caches.

## Serialization

This subsystem is the serialization contract. A field change must document writer, reader,
default, old versions affected, removal horizon, and round-trip evidence; deletion or rename
requires a compatibility strategy.

## Tests

Use focused serializer/world tests and curated old-save fixtures where available. Verify current
round trip, absent field, malformed input handling, and the oldest version touched.

## Performance

Save/load walks much of the world and can allocate heavily. Keep streaming boundaries, avoid
quadratic ID reconnection, and measure large worlds without hiding failures behind timing.

## CCB divergence

CCB's current version and legacy readers are authoritative only for CCB. An upstream serializer
cannot be copied without comparing field history, mod migrations, and world layout.

## Technical debt

Compatibility logic is distributed across type serializers and version checks. Keep each new
exception localized and documented; do not perform a broad format rewrite with unrelated work.
