---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.v5.debugging
title: Lua debugging and contract validation
language: en
status: draft
doc_type: how-to
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
- check_public_contract.py
source_queries: []
source_fingerprint: 86ab8c697639288944692daea743e7470450d95825578f8964198c2bd0dbdc83
authority: api-contract
verified_commit: 3ac0bd7f356b30b880dc655f3006ebf1cbda9cfd
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: f5953a3b1725321b7ef41ff313e9a5de3de53a5cd360c7322bbbb1e0cbcc8438
prerequisites:
- api.lua.v5.overview
depends_on:
- api.lua.v5.example-mod
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids:
- lua-contract
- lua-docs
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/565
stale_reason: null
search:
  exclude: true
---

# Lua debugging and contract validation

## Identify the failing phase first

| Phase | Typical evidence | Next step |
| --- | --- | --- |
| Manifest | unknown capability, dependency order, id/version mismatch | validate `lua/manifest.json` against the Schema |
| Candidate load | syntax, module path, illegal top-level call | inspect `debug.log`; the old runtime should remain active |
| Callback | capability, argument, generation, or budget failure | inspect latest runtime error and generated entry |
| UI | expired `ctx`, duplicate control id, unavailable feature | use stable `_id` and the fresh context each draw |
| Generated drift | generated diff or parity failure | update authority then regenerate; never patch outputs |

`game.runtime_status()` reports runtime/world generations, memory, registration counts, the
latest error, and callback timing counters. For handles, inspect `handle:status()` first. For
events, hooks, and callbacks, use the relevant `list`/`describe` call rather than guessing names.

## Authoritative source checks

Run these in the pinned CCB source worktree:

```sh
# validation: lua-contract
python3 tools/lua_api/generate_public_contract.py --check
python3 tools/lua_api/check_public_contract.py
python3 tools/lua_api/check_luals_declarations.py
python3 tools/lua_api/check_examples.py --require-luac
python3 -m unittest discover -s tools/lua_api -p 'test_*.py'
```

They cover reproducible generation, Schema/registration parity, LuaLS signatures, the complete
example Mod, and tool regressions. `check_coverage.py` measures the CBN capability mapping; it is
not the CCB public-doc denominator. Use `ccb_public_api_v5_coverage.json` for that denominator.

## CCB-Docs generation checks

```sh
# validation: lua-docs
python3 scripts/generate_lua_reference.py --source-repo /path/to/CCB --check --require-luac
python3 scripts/generate_catalog.py --check
python3 scripts/check_catalog.py --source-repo /path/to/CCB
python3 scripts/build_site.py --strict --include-drafts
python3 scripts/check_links.py --site-dir site --critical
```

Fix failures in the generator or authoritative input. Do not edit generated page bodies,
catalog-derived front matter, or the publication coverage report by hand.
