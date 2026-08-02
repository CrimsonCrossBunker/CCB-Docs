---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.changelog
title: Lua API changelog
language: en
status: active
doc_type: reference
audiences:
- mod-author
- api-user
- experienced-contributor
- maintainer
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: Not yet reviewed (draft)
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- native_luals_callable_parity
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 39c073b18b6732436210edee27a6ab51c66015ee4864fd7f0c7173416ec41363
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.migration
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/changelog/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/changelog/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/changelog/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/changelog/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.changelog%29%3A+&body=Document+ID%3A+api.lua.v5.changelog%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Lua API changelog

This page records only API changes supported by repository commits and generated contracts.
The current contract marks callables whose exact introduction history cannot be recovered as
`since: untracked-before-or-at-v5`. That is not a release date and must not be guessed.

## API v5 contract baseline (pending)

| Field | Value |
| --- | --- |
| Pinned commit | `3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd` |
| Source PR | [CCB #565](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/565) |
| API version | 5 |
| Unique public symbols | 2,806 |
| Undocumented | 0 |
| Native/LuaLS callable parity | 100% |
| Manifest Schema/runtime/LuaLS parity | true |

This baseline first joins modules, namespaces, classes/fields, functions, methods, properties,
operators, enums, events/fields, hooks, callbacks, capabilities, the permission model, and
manifest fields into one public inventory, with documentation ids and sources on each record.

## Updating this changelog

A public API change must update the authoritative registration/declaration/Schema, tests,
generated contract and coverage, examples when applicable, and this changelog. New entries get
a real `since`; deprecations set `deprecated: true` and a `deprecation_replacement`. Never patch
only generated JSON or generated pages.

After the source lands, every Lua page must refresh to the final master commit, regenerate, and
pass the [debugging and validation](debugging.md) checks before draft can become active.
