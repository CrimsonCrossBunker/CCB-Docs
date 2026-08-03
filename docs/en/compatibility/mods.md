---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: compatibility.mods
title: Mod compatibility
language: en
status: active
doc_type: explanation
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
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/MOD_COMPATIBILITY.md
- src/mod_manager.cpp
- src/worldfactory.cpp
- tests/worldfactory_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: a3359e19ec5de3957becfbf9495cc25aeaeac01a15c37e3dc816578f476103d1
authority: source-and-tests
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: cdc0443d43962c6fa7df2cf31aed0552423177b56a0132432e40c272a494f66a
prerequisites:
- architecture.overview
depends_on:
- compatibility.save
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: compatibility
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/compatibility/mods/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/mods/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/compatibility/mods/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/compatibility/mods/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/2c899a3db790e11a6ff44d91f319064b1ee65d2a
source_urls:
- path: CONTRIBUTING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/CONTRIBUTING.md
- path: doc/MOD_COMPATIBILITY.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/doc/MOD_COMPATIBILITY.md
- path: src/mod_manager.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/mod_manager.cpp
- path: src/worldfactory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/src/worldfactory.cpp
- path: tests/worldfactory_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/2c899a3db790e11a6ff44d91f319064b1ee65d2a/tests/worldfactory_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28compatibility.mods%29%3A+&body=Document+ID%3A+compatibility.mods%0ALanguage%3A+en%0AVerified+commit%3A+2c899a3db790e11a6ff44d91f319064b1ee65d2a%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Mod compatibility

Mod compatibility covers identifiers, dependencies, load order, optional
interactions, save data, and public scripting contracts. It is broader than
whether a mod's JSON parses once.

## Stable boundaries

- Keep published type and object IDs stable or provide supported migration and
  obsoletion data.
- Declare dependencies in the mod metadata; do not rely on alphabetical file
  order or another mod being present by accident.
- Put conditional content for another loaded mod under
  `mod_interactions/<other-mod-id>/`. Interaction content loads after ordinary
  mod content; directory IDs are case-sensitive and nested multi-mod
  combinations are not supported by the verified implementation.
- Treat EOC talkers, variables, and context as part of behaviour.
- Treat the Lua manifest version, capabilities, permissions, and published v5
  symbols as an API contract.

## Validation

Load the mod alone with its declared dependencies, then with each supported
interaction set. Create a world, exercise the changed content, save, reload,
and inspect the first loader error. A complete example mod should be loaded by
CI rather than being validated only as isolated JSON files.

Compatibility claims must name the CCB commit, mod versions, dependency set,
and platform. Upstream compatibility does not automatically imply CCB
compatibility because registrations, data, and the Lua surface can diverge.
