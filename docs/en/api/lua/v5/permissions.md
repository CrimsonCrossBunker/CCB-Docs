---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.permissions
title: Permission and trust model
language: en
status: active
doc_type: explanation
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
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- capability-gating
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 501f84d20d4bf432dd7fec9b757f5af6a18dae36
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 97e992a62f3f105811f0d23a9fdbeac395bb0c6d73ff166b944e26578916a06f
prerequisites:
- api.lua.v5.capabilities
depends_on:
- api.lua.v5.reference.permissions
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/permissions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/permissions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/permissions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/permissions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/501f84d20d4bf432dd7fec9b757f5af6a18dae36
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/501f84d20d4bf432dd7fec9b757f5af6a18dae36/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.v5.permissions%29%3A+&body=Document+ID%3A+api.lua.v5.permissions%0ALanguage%3A+en%0AVerified+commit%3A+501f84d20d4bf432dd7fec9b757f5af6a18dae36%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Permission and trust model

Lua v5 uses capability gating. There is no separate `permissions` manifest field:
`capabilities` is the permission declaration. Permissions bind to a source identity, not to
the current function, page id, or call stack.

## Identity propagation

- `require` executes in the current source environment.
- `modules.import` imports provider source, but it executes with consumer capabilities.
- `services.call` runs under the provider's identity and budget, then copies its result.
- Events, scheduled tasks, hooks, callbacks, action-menu entries, and sidebar callbacks
  restore the registering source's identity.
- Replacing a page with the same id does not inherit the old page source's permissions.

Use `modules.import` for source reuse and `services` when an operation needs the provider's
permission boundary.

## Mutation and interaction boundary

`game.write` is not arbitrary memory access. Each operation still validates ids, coordinate
spaces, generations, ranges, call phase, and result bounds. Dangerous current-context actions
also need `game.actions.dangerous` and a one-time native confirmation naming the source and
action. Many interaction, relocation, and mutation calls are legal only from an active callback.

The Lua standard-library environment omits `io`, `os`, `debug`, native C modules, and arbitrary
dynamic-code/file loading. This is application scripting isolation, not a security sandbox for
untrusted downloaded code. Apply the same trust decision as for any installed game Mod.

## Review checklist

1. Does the manifest request only capabilities that code actually uses?
2. Can a write become a detached read or safe action-queue request?
3. Should a cross-source call use a service to preserve provider identity?
4. Does logging/UI expose local paths, save content, or unnecessary state?
5. Does code assume a capability bypasses parameter, lifecycle, or generation checks? It does not.

See the machine-derived [permission-model reference](reference/permissions.md).
