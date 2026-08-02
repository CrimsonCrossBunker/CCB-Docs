---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: eoc.reference
title: 'Legacy migration draft: eoc'
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/EFFECT_ON_CONDITION.md
- src/effect_on_condition.cpp
- src/condition.cpp
- src/npctalk.cpp
- data/json/effects_on_condition/example_eocs.json
- tests/npc_talk_test.cpp
source_symbols:
- effect_on_condition::load
- effect_on_conditions::load
- conditional_t::conditional_t
source_queries: []
source_fingerprint: 836e4deb077ab0b5c5a2cfb9efb2ec0b95b8c58a163d733bcd2ede0a9ca2363a
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5535dd152efecfd8e811300b442e7b3eb83eb7116388bbf5403f84742e2b27cf
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: zihanZheng, LunaGlaze, Anton Simakov, Maleclypse, GuardianDll, thaelina;
  accepted inventory identities only. Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/JSON/EFFECT_ON_CONDITION.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/JSON/EFFECT_ON_CONDITION.md
- path: src/effect_on_condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/effect_on_condition.cpp
- path: src/condition.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/condition.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/npctalk.cpp
- path: data/json/effects_on_condition/example_eocs.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/effects_on_condition/example_eocs.json
- path: tests/npc_talk_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/npc_talk_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28eoc.reference%29%3A+&body=Document+ID%3A+eoc.reference%0ALanguage%3A+en%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: eoc

This is the migration draft page for `eoc.reference`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `eoc.reference`
- Target: `reference/eoc/index.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| eoc.reference | doc/JSON/EFFECT_ON_CONDITION.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB EOC model

An Effect on Condition (EOC) combines dialogue conditions and effects so they can be invoked
outside dialogue. It is not an `effect_type` status applied to a creature; the similar names
hide different loaders, lifecycles, and purposes. The complete current key lists are generated
from source registrations in the [condition index](../eoc-conditions.md) and
[effect index](../eoc-effects.md). Do not copy a legacy list and call it complete.

### Minimal activation EOC

```jsonc
{
  "type": "effect_on_condition",
  "id": "EOC_CCB_EXAMPLE",
  "eoc_type": "ACTIVATION",
  "condition": { "u_has_trait": "DEBUG_PREVENT_DEATH" },
  "effect": { "u_message": "The example EOC ran." },
  "false_effect": { "u_message": "The condition did not pass." }
}
```

The `id` is a stable reference used by other JSON, events, and EOCs. A field can reference a
named ID or, where its loader accepts one, contain an inline EOC. The loader records named
references and consistency checking reports missing IDs.

### Types, triggers, and scheduling

The current `effect_on_condition::load` reads `eoc_type`. With no recurrence, an unspecified
type defaults to `ACTIVATION`. Supplying `recurrence` forces `RECURRING` and conflicts with
another explicit type. An `EVENT` must provide `required_event`. Death and death-prevention
types get talkers and stopping behavior from their call sites, not from the EOC alone.

A recurring EOC can use `condition`, `false_effect`, and `deactivate_condition`. `global`
selects global or per-character queues. `run_for_npcs` is valid only with `global: true`.
Frequent recurrences and effects that traverse NPCs or map data have real performance cost;
measure them.

### Conditions, effects, and Boolean composition

A condition can be a simple string or an object. `and` and `or` take condition arrays; `not`
contains one string or condition object. An unrecognized complex condition is a load error.
An effect can be one entry or an ordered array and can compose flow with `if`, `then`, `else`,
other EOCs, and context variables.

The generated indexes record each condition or effect's parameters, defaults, talker types,
and source. An entry's existence does not prove that the current call site supplies a compatible
alpha or beta talker, so examples still need contextual tests.

### Alpha, beta, and context

EOCs reuse dialogue naming: `u_` normally addresses the alpha talker and `npc_` the beta, but
an actual talker may be a character, monster, item, furniture, or absent. Event, death, and
ammunition-effect call sites can omit one side. Guard access with `has_alpha` or `has_beta`.

Variable scopes include the character side, beta side, world-global storage, and this invocation's
context. A `context_val` exists only when the caller supplies that key; event values must match
the current event payload. Do not treat context as persistent save state or assume that a
requeued EOC retains the same context.

### Validation

1. Use the generated condition and effect indexes for keys, parameters, and source locations.
2. Inspect the calling field for actual alpha, beta, context, and lifecycle behavior.
3. Run the JSON loader, EOC registry or parser checks, and `--check-mods` for the real Mod set.
4. Cover true and false conditions, missing talkers, missing variables, and repeated execution.
5. For recurring or event EOCs, test frequency, queues, save reload, and performance.

See the [EOC overview](../../eoc/overview.md) and
[complete JSON/EOC example Mod](../../mods/complete-json-eoc-mod.md) for integrated structure.

## History and attribution

Accepted inventory contributors: zihanZheng, LunaGlaze, Anton Simakov, Maleclypse, GuardianDll, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `80828049edb3adf2a13bb2912a19373dc4e69f32`; the aggregate source fingerprint is `836e4deb077ab0b5c5a2cfb9efb2ec0b95b8c58a163d733bcd2ede0a9ca2363a`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/EFFECT_ON_CONDITION.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECT_ON_CONDITION.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/JSON/EFFECT_ON_CONDITION.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
