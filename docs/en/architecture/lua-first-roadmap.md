---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: architecture.lua-first-roadmap
title: Lua-first Platform roadmap
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
- ai/lua-first-roadmap.yml
- ai/lua-first-roadmap.schema.json
- data/lua/LUA_FIRST_PLATFORM.md
source_symbols: []
source_queries: []
source_fingerprint: 05c4efbbb59bd9cb6550d35141c21123e5a34da7ecce125a07efc74a57ab26b9
authority: docs-explanation
verified_commit: c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
verified_at: '2026-08-12'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2682c28d441a435396381d5c65ad2ea8b8319135d90f924078edd1dab829ca9a
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-roadmap/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/architecture/lua-first-roadmap/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/architecture/lua-first-roadmap/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd
source_urls:
- path: ai/lua-first-roadmap.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-roadmap.yml
- path: ai/lua-first-roadmap.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/ai/lua-first-roadmap.schema.json
- path: data/lua/LUA_FIRST_PLATFORM.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd/data/lua/LUA_FIRST_PLATFORM.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28architecture.lua-first-roadmap%29%3A+&body=Document+ID%3A+architecture.lua-first-roadmap%0ALanguage%3A+en%0AVerified+commit%3A+c663ceb2c1bd1f5b23ffc533c2e7944fd859b4bd%0A%0ADescribe+the+documentation+problem%3A%0A
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

## Nine milestones

| Order | Milestone | Current status | Main exit condition |
| ---: | --- | --- | --- |
| 1 | Documentation foundation | `complete` | Authoritative architecture, Agent routing, schema-checked roadmap, paired explanations |
| 2 | Zero-config discovery | `complete` | A directory with only root `main.lua` is discoverable; optional `mod.lua` resolves dependencies first |
| 3 | Native content transaction | `in_progress` | Pre-finalize execution, staging/commit, owner/generation, private-adapter inventory |
| 4 | Item + recipe + use behaviour | `complete` | First zero-JSON/EOC Mod passes save/load and has an observable game result |
| 5 | Behaviour services | `in_progress` | Events, hooks, handlers, persistent tasks/state, and shared domain services |
| 6 | Playable MVP v0.1 | `complete` | A bundled pure-Lua Mod passes discovery, dependency selection, real save, full reload, and continued play |
| 7 | Static domain coverage | `in_progress` | Every checked JSON/EOC entry has a disposition; each domain has tests, declarations, and docs |
| 8 | Core and bundled migration | `in_progress` | Stable IDs retained, tool emits idiomatic Lua skeletons, old authoring freezes only per completed domain |
| 9 | Legacy removal window | `planned` | At least two stable releases and twelve months, plus save migration and bundled-content checks |

The dependencies form a directed chain. A later milestone cannot skip its
prerequisite by deleting JSON/EOC first and forcing migration. Machine checks
reject unknown dependencies and dependency cycles.

## Current capability coverage

| Capability | Status | Legacy dependency | Next substantive work |
| --- | --- | --- | --- |
| Mod discovery | `partial` | `none` | Complete manual desktop/Android Mod-selector interaction checks |
| Complete standard libraries | `partial` | `none` | Complete desktop/Android first-enable trusted-code interaction checks |
| Native static content | `partial` | `none` | Continue field-complete typed registrar and extractor coverage without exposing old loaders |
| Native object surface | `partial` | `none` | Complete the export-root and unbindable-member inventories and extend explicit owners |
| Events/hooks/callbacks | `partial` | `none` | Extend actor-kind coverage beyond the audited semantic events |
| Presentation primitives | `partial` | `none` | Complete manual desktop/Android checks, then add domain-shaped composable forms |
| Persistent tasks/state | `partial` | `none` | Extend copied-world and stable-ID compatibility coverage |
| Shared domain services | `partial` | `none` | Review primitive and bounded selectors against exact native semantics |
| Developer templates | `partial` | `none` | Add end-to-end examples only when they prove another native domain |
| Migration extractor | `partial` | `none` | Add conversions only after a typed registrar and semantic evidence exist |
| Replacement audit | `partial` | `none` | Review primitive and planned entries domain by domain while keeping counts distinct |

All eleven capabilities now have runnable implementation or checked foundations,
and no public Platform surface depends on an old parser. `partial` still means
incomplete coverage; it is not a claim of complete JSON/EOC replacement parity.

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

### Delivered first extraction scope

The first “item + recipe + Lua use behaviour” closed loop is now delivered:

- zero-config Mod discovery and dependency ordering;
- native item/recipe definitions and cross-ID references;
- units, translated text, and common factory/registry rules;
- a named handler referenced by a definition;
- minimal character/item domain services;
- Mod state, save, load, and reload;
- error locations, LuaLS declarations, minimal template, and end-to-end tests.

The slice now passes a playable-MVP gate covering a real game save, Lua runtime
shutdown, full data reload, continued item-handler play, and exactly-once
execution of an overdue task. Further content catalogs and character/world
operations are being extended with the same native pattern across vehicles,
creatures, maps, dialogue, missions, and UI—without copying the old loaders.

## What the replacement ledger records

The checked ledger is not a simple “old key → new function” table. Each record
contains:

- legacy inventory and selector;
- actual game meaning and owning domain;
- target native type, method, or shared service;
- a `not_applicable` reason for engine-internal serialization or similar cases;
- Platform status and legacy-dependency level;
- source, test, declaration, documentation, and migration-tool evidence;
- stable-ID, save, and hybrid-Mod compatibility notes.

The checker now requires every entry in all three inventories exactly once.
The current 775 dispositions are:

| Disposition | Count | Complete-replacement claim |
| --- | ---: | --- |
| Full selector parity (`implemented_unverified`) | 0 | No selector can yet make this claim |
| Bounded shape implemented (`bounded_implemented_unverified`) | 119 | Only the ledger's named finite shapes |
| Native primitive available (`primitive_available_unverified`) | 440 | Composition exists; this is not old-selector parity |
| Planned | 198 | Migration work, not a shipped API |
| Reviewed not applicable | 18 | An explicit native-Lua or engine-internal reason exists |

This is why “Lua-first is playable” and “JSON/EOC are not fully replaced” are
both true. Zero full-selector entries does not deny the native API; it prevents
finite shapes and composition primitives from being overstated as parity with
every use of an old-language selector.

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

## Next implementation order

Zero-config scanning, the Platform Lua state, first transaction foundations,
the item/recipe/behaviour slice, templates, migration tooling, LuaLS, and the
775-entry ledger are already present. The next sequence is:

1. finish desktop and Android manual interaction gates for Mod selection,
   trusted-code confirmation, and presentation primitives;
2. extend explicit owner/generation handling to the remaining borrowed native
   references;
3. complete static registrars and extractors field by field without publishing
   the old loaders;
4. add native services for environment, dialogue, activities, combat,
   navigation, and relocation;
5. promote bounded and primitive entries only with source semantics and
   conversion fixtures that prove full parity;
6. extend copied-world, stable-ID, save, and supported-platform coverage;
7. migrate core content and freeze old authoring only after a domain reaches
   `available` completely.

Every PR should update status, evidence, and next actions in
`ai/lua-first-roadmap.yml` and name affected CCB-Docs IDs. See
[Platform v1](lua-first-platform.md) for design boundaries, the
[Platform v1 API overview](../api/lua/platform-v1/overview.md) for runnable
interfaces, and the [glossary](lua-first-glossary.md) for terminology.
