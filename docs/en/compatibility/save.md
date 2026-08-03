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
source_fingerprint: aee6b119c4372d0f36b7a81ea4d42d32563374feacdb88b080a75a75e0f354a0
authority: source-and-tests
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: e09ef4b70f339892b6a214edaf933da9ada135e574dcd2acdbc2df204acf345d
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
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/compatibility/save/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/save/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/compatibility/save/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/save/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/2c899a3db790e11a6ff44d91f319064b1ee65d2a
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/CONTRIBUTING.md
- path: doc/JSON/OBSOLETION_AND_MIGRATION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/doc/JSON/OBSOLETION_AND_MIGRATION.md
- path: src/savegame.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/savegame.cpp
- path: src/savegame_json.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/savegame_json.cpp
- path: src/savegame_legacy.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/savegame_legacy.cpp
- path: src/worldfactory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/worldfactory.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28compatibility.save%29%3A+&body=Document+ID%3A+compatibility.save%0ALanguage%3A+en%0AVerified+commit%3A+2c899a3db790e11a6ff44d91f319064b1ee65d2a%0A%0ADescribe+the+documentation+problem%3A%0A
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
