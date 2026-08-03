---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.examine-actions
title: 'Legacy migration draft: examine actions'
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
last_human_reviewer: LYHGLYTX
source_paths:
- doc/JSON/EXAMINE.md
- src/iexamine.cpp
- src/iexamine_actors.cpp
- src/mapdata.cpp
- tests/iexamine_test.cpp
source_symbols:
- iexamine_functions_from_string
- appliance_convert_examine_actor::load
- cardreader_examine_actor::load
- eoc_examine_actor::load
source_queries: []
source_fingerprint: 1bbd6d207b2fbbd6700e3fd88ce3ec2b5cc23a18f36cf5431e054a0cf62d77ad
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: af886e54c932e01310782aa2b626a15be7a797cc7e68fbfa273ead06fbf8e08e
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: LunaGlaze, Maleclypse, thaelina; accepted inventory identities only. Source
  paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/examine-actions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/examine-actions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/examine-actions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/examine-actions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/EXAMINE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/EXAMINE.md
- path: src/iexamine.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/iexamine.cpp
- path: src/iexamine_actors.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/iexamine_actors.cpp
- path: src/mapdata.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/mapdata.cpp
- path: tests/iexamine_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/iexamine_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.examine-actions%29%3A+&body=Document+ID%3A+json.examine-actions%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: examine actions

This is the migration draft page for `json.examine-actions`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.examine-actions`
- Target: `reference/json/examine-actions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/examine-actions/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.examine-actions | doc/JSON/EXAMINE.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Terrain and furniture examine actions

`examine_action` accepts a registered hardcoded string, a JSON examine actor, or an array mixing
both. The current map in `iexamine_functions_from_string` defines string registrations. An unknown
name reports an error and falls back to `none`; the historical hand-written list is not complete.

### Actor contracts

- `appliance_convert` requires item and optionally sets furniture or terrain. Finalization validates
  the item, terrain, furniture, and appliance vpart.
- `cardreader` requires flags, success_msg, and redundant_msg. The mapgen_id route is exclusive with
  radius plus terrain or furniture changes; query, hacking, card consumption, and monster despawn
  also have combination constraints.
- `effect_on_conditions` loads named or inline EOCs in order. Its dialogue has the examiner as u,
  null npc, and `this` furniture ID plus `pos` context.
- `mortar` requires ammo and range and may use condition, aim or flight variables, and completion
  EOCs. Completion also supplies `this`, `pos`, and `target`.

The top-level actor type selects the concrete loader. Do not copy fields across actors or infer
mandatory members and defaults from occurrence counts.

### Design boundary

Reference an existing hardcoded action when it matches. Prefer an actor or EOC for configurable
composition. A new hardcoded string or actor type changes a public contract and needs registration,
loader and finalization, JSON inventory, bilingual documentation, and tests together. An EOC must
define talkers, context variables, repeat behavior, and map-bubble boundaries.

### Validation

Run formatting, `make -j2 json-check`, Mod `--check-mods`, and examine a focused fixture. Cover
missing items, cards, or ammo; cancelled queries; repeat use; invalid IDs; hacking and mapgen paths;
EOC context; and save reload in `tests/iexamine_test.cpp`. Successful parsing alone is insufficient.

## History and attribution

Accepted inventory contributors: LunaGlaze, Maleclypse, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `1bbd6d207b2fbbd6700e3fd88ce3ec2b5cc23a18f36cf5431e054a0cf62d77ad`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/EXAMINE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/EXAMINE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/EXAMINE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
