---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.lua-first-roadmap
title: Lua-first Platform roadmap
language: en
status: draft
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
- ai/lua-first-roadmap.yml
- ai/lua-first-roadmap.schema.json
- data/lua/LUA_FIRST_PLATFORM.md
source_symbols: []
source_queries: []
source_fingerprint: e8cd2ca29e3d1c735f3d5e460f5224b9bd96b723e91b9f1d509db504c762c21f
authority: docs-explanation
verified_commit: b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6
verified_at: '2026-08-09'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 18cd86df4ccf4d50b87415b40ed310c10249b716e624934ec3771301466c5c81
prerequisites:
- architecture.lua-first-platform
depends_on:
- architecture.lua-first-platform
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- agent-context
- lua-contract
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: lua-platform
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/615
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-roadmap/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-roadmap/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6
source_urls:
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/ai/lua-first-roadmap.yml
- path: ai/lua-first-roadmap.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/ai/lua-first-roadmap.schema.json
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6/data/lua/LUA_FIRST_PLATFORM.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.lua-first-roadmap%29%3A+&body=Document+ID%3A+architecture.lua-first-roadmap%0ALanguage%3A+en%0AVerified+commit%3A+b2bbec1a2f4f8e41a2fece924c7c43b426ff2dc6%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Lua-first Platform roadmap

> This page translates the checked source-repository roadmap into human-readable
> guidance. `ai/lua-first-roadmap.yml` is the only machine status source. A
> `planned`, `absent`, or `partial` entry must not be presented as a current game
> feature.

## Reading status

Milestone status describes a complete delivery stage:

- `planned`: the direction is recorded but has no acceptable implementation;
- `in_progress`: work has evidence, but not every exit criterion is satisfied;
- `complete`: exit criteria are satisfied and source, test, or documentation
  evidence is listed;
- `blocked`: a concrete blocking condition exists; it does not merely mean that
  the work is difficult.

Capability status describes a specific surface:

- `absent`: the Platform target surface does not exist;
- `legacy_only`: an old runtime has related power but Platform does not;
- `partial`: reusable foundations or incomplete coverage exist, without a full
  target guarantee;
- `available`: developers can use the target surface with validation and docs.

`legacy_dependency` separately says whether implementation still relies on the
old system: `none`, internal-only `private_adapter`, or author-visible
`public_legacy`. A capability with `public_legacy` can never be `available`.

## Current baseline

Generated legacy contract inventories are migration denominators, not a request
to automatically generate 775 Lua functions:

| Inventory | Current entries | Purpose |
| --- | ---: | --- |
| JSON top-level object types | 190 | Classify into native content domains, internal serialization, or not applicable |
| EOC condition keys | 275 | Classify into normal Lua queries, native methods, or shared query services |
| EOC effect keys | 310 | Classify into native methods, shared mutation services, events/hooks, or workflows |

Whenever those inventories are regenerated, the metadata validator compares
their real lengths with the roadmap counts so the plan cannot silently drift.

## Eight milestones

| Order | Milestone | Current status | Main exit condition |
| ---: | --- | --- | --- |
| 1 | Documentation foundation | `complete` | Authoritative architecture, Agent routing, schema-checked roadmap, paired explanations |
| 2 | Zero-config discovery | `planned` | A directory with only root `main.lua` is discoverable; optional `mod.lua` resolves dependencies first |
| 3 | Native content transaction | `planned` | Pre-finalize execution, staging/commit, owner/generation, private-adapter inventory |
| 4 | Item + recipe + use behaviour | `planned` | First zero-JSON/EOC Mod passes save/load and has an observable game result |
| 5 | Behaviour services | `planned` | Events, hooks, handlers, persistent tasks/state, and shared domain services |
| 6 | Static domain coverage | `planned` | Every checked JSON/EOC entry has a disposition; each domain has tests, declarations, and docs |
| 7 | Core and bundled migration | `planned` | Stable IDs retained, tool emits idiomatic Lua skeletons, old authoring freezes only per completed domain |
| 8 | Legacy removal window | `planned` | At least two stable releases and twelve months, plus save migration and bundled-content checks |

The dependencies form a directed chain. A later milestone cannot skip its
prerequisite by deleting JSON/EOC first and forcing migration. Machine checks
reject unknown dependencies and dependency cycles.

## Current capability coverage

| Capability | Status | Legacy dependency | Next substantive work |
| --- | --- | --- | --- |
| Mod discovery | `absent` | `public_legacy` | Add Platform discovery beside old `modinfo.json` scanning and diagnose conflicts |
| Complete standard libraries | `legacy_only` | `none` | Build a separately versioned trusted Platform Lua state and explicit warnings |
| Native static content | `absent` | `public_legacy` | Add pre-finalize execution, staging registry, and commit semantics |
| Native object surface | `partial` | `none` | Export-root inventory, unbindable-member report, owner/generation checks |
| Events/hooks/callbacks | `partial` | `none` | Native arguments instead of snapshots/talker aliases; stable handler IDs |
| Persistent tasks/state | `partial` | `none` | Save handler, due time, owner, payload and version; define exceptional outcomes |
| Shared domain services | `absent` | `public_legacy` | Classify EOC handlers and first extract operations needed by the vertical slice |
| Developer templates | `absent` | `none` | Deliver `minimal`, `complete`, and safe `create_lua_mod.py` scaffolding |
| Replacement audit | `absent` | `private_adapter` | Build a selector ledger covering each inventory entry exactly once |

Most `partial` entries mean that v5 or C++ has reusable foundations. They do not
mean a Platform author can use the target spelling shown in the architecture.

## Extract existing power instead of restarting

Throwing away old implementation would be slow and would repeat years of
validation rules. Publishing old loaders directly would trap Lua inside a
JSON/EOC shell. The correct extraction unit is a game-domain capability:

1. **Inventory:** choose a JSON type or EOC key from a generated inventory and
   locate its registration and parser.
2. **Trace semantics:** find the C++ object, invariants, errors, and save impact
   that it ultimately reads or changes.
3. **Extract a service:** turn the real query or mutation into a syntax-neutral
   C++ domain method or service.
4. **Bind native objects:** give Lua typed arguments, results, units, and owner
   checks.
5. **Retain a legacy adapter:** let JSON/EOC temporarily call the same service
   without making the old parser a public Lua API.
6. **Test vertically:** cover discovery through finalization, game result,
   saving, and reload.
7. **Record the disposition:** identify target domain, status, evidence, and
   migration in the replacement ledger.
8. **Then migrate content:** bulk-migrate core and bundled Mods only after the
   replacement and tools are usable.

This reuses rules, validation, native objects, and game operations—not the old
languages' shapes.

### First extraction scope

The first slice extracts only the closed loop required for “item + recipe + Lua
use behaviour”:

- zero-config Mod discovery and dependency ordering;
- native item/recipe definitions and cross-ID references;
- units, translated text, and common factory/registry rules;
- a named handler referenced by a definition;
- minimal character/item domain services;
- Mod state, save, load, and reload;
- error locations, LuaLS declarations, minimal template, and end-to-end tests.

This scope is small enough to produce a playable slice quickly and complete
enough to reveal the hardest lifecycle, ownership, and persistence problems.
The next slices can extend the pattern to vehicles, creatures, map generation,
dialogue, missions, and UI.

## What the replacement ledger records

The future ledger is not a simple “old key → new function” table. Each record
needs at least:

- legacy inventory and selector;
- actual game meaning and owning domain;
- target native type, method, or shared service;
- a `not_applicable` reason for engine-internal serialization or similar cases;
- Platform status and legacy-dependency level;
- source, test, declaration, documentation, and migration-tool evidence;
- stable-ID, save, and hybrid-Mod compatibility notes.

The checker eventually requires every entry in all three inventories exactly
once, preventing omissions, duplicate ownership, or a vague “other” bucket.

## Definition of done for a capability

A domain moving from `partial` to `available` needs at least:

1. a native API that does not ask authors for JSON/EOC;
2. tests for loader lifecycle, rollback, and actionable errors;
3. owner/generation invalidation tests for borrowed references;
4. saved data containing stable IDs and serializable payloads only;
5. synchronized LuaLS declarations, runnable examples, and paired docs;
6. realistic expression in the `minimal` or `complete` template;
7. legacy dependency reduced to `none` or `private_adapter`;
8. validated or documented differences across supported platforms such as
   Windows, Linux, and Android.

## Near-term implementation order

A practical near-term PR sequence is:

1. implement zero-config scanning and trusted-code warnings, initially loading
   an empty entry only;
2. establish Platform Lua state, error boundaries, dependency order, and
   candidate reload;
3. establish definition staging, transactions, and owner/generation support;
4. extract services needed by item, recipe, and use behaviour;
5. deliver the example Mod, templates, LuaLS, and end-to-end tests;
6. design replacement-ledger generation and checking from that first evidence;
7. expand domain by domain instead of exporting all C++ at once.

Every PR should update status, evidence, and next actions in
`ai/lua-first-roadmap.yml` and name affected CCB-Docs IDs. See
[Platform v1](lua-first-platform.md) for design boundaries and the
[glossary](lua-first-glossary.md) for terminology.
