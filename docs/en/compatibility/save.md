---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: compatibility.save
title: Save compatibility
language: en
status: active
doc_type: explanation
audiences:
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/JSON/OBSOLETION_AND_MIGRATION.md
- src/savegame.cpp
- src/savegame_json.cpp
- src/savegame_legacy.cpp
- src/worldfactory.cpp
source_symbols: []
source_queries: []
source_fingerprint: df55bb55195f94c2514d2e905e94eea1cd9cec31d69201450173ea2da1c41010
authority: source-and-tests
verified_commit: 71f403ecea0dcf16be8fe93c661acbe2a4906cc6
verified_at: '2026-08-09'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 3596e034c75ddee6ed3c287ade547d64bb8aa37481ee6141b98f1e6df3ee8106
prerequisites:
- architecture.overview
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
risk_group: compatibility
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/compatibility/save/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/save/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/compatibility/save/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/save/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/71f403ecea0dcf16be8fe93c661acbe2a4906cc6
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/CONTRIBUTING.md
- path: doc/JSON/OBSOLETION_AND_MIGRATION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/doc/JSON/OBSOLETION_AND_MIGRATION.md
- path: src/savegame.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/savegame.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/savegame_json.cpp
- path: src/savegame_legacy.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/savegame_legacy.cpp
- path: src/worldfactory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/71f403ecea0dcf16be8fe93c661acbe2a4906cc6/src/worldfactory.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28compatibility.save%29%3A+&body=Document+ID%3A+compatibility.save%0ALanguage%3A+en%0AVerified+commit%3A+71f403ecea0dcf16be8fe93c661acbe2a4906cc6%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Save compatibility

Save data is a public compatibility boundary. A change is not complete merely
because a newly created world works: existing worlds, stable IDs, serialized
object ownership, and failure recovery must be considered.

## Review checklist

1. Identify every serialized field, owning type, and load path touched.
2. Determine the oldest supported representation and whether missing fields
   already have safe defaults.
3. Preserve stable JSON IDs. For a rename or removal, use the repository's
   supported migration or obsoletion mechanism instead of silently reusing an
   ID.
4. Test on copies of representative saves. Never use the only copy of a user's
   world as a migration fixture.
5. Test save, reload, a second save/reload cycle, and the affected gameplay
   operation. One successful parse may still leave invalid state.
6. Record incompatibility explicitly in the pull request and release notes.

## Failure handling

Do not catch and discard loader errors to make an old save appear accepted.
Preserve the first diagnostic and enough context to identify the owning object
without leaking personal paths or data. A migration should be deterministic,
idempotent where practical, and covered by a focused regression test.

The `savegame*` and `worldfactory` implementations at the page's verified
commit are the runtime authority. Legacy prose explains concepts but cannot
override current serialization code and tests.

## Finite-water save state

The remaining amount in finite ponds, pools, and channels is stored in the
submap's `finite_liquids` member rather than as ground items. Each record holds
the in-submap coordinates and remaining charges; a tile with no remaining
liquid has no record.

When an older finite-water save is loaded, the loader absorbs matching ground
liquid from finite-water terrain into this hidden state and clamps it to the
terrain's capacity. This removes the item sprite that covered the water and
preserves the amount through later save/load cycles. Changes to this migration
need coverage for legacy ground liquid, the new hidden state, and two
consecutive save/load cycles.
