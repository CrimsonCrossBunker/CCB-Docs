---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.movement-modes
title: 'Legacy migration draft: movement modes'
language: en
status: draft
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
- doc/JSON/MOVE_MODE.md
- src/move_mode.cpp
- src/move_mode.h
- data/json/move_modes.json
source_symbols:
- move_mode::load
source_queries: []
source_fingerprint: 3a00588b939b053ee86e7754623a56ab4ca546f9304e4230da35cde8e69a7a3d
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 04d86c0f8ad02af3ea342a7a4b6505a374939da0346266d4c1ecce2ad2684075
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/movement-modes/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/movement-modes/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/movement-modes/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/movement-modes/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/MOVE_MODE.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MOVE_MODE.md
- path: src/move_mode.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/move_mode.cpp
- path: src/move_mode.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/move_mode.h
- path: data/json/move_modes.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/move_modes.json
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.movement-modes%29%3A+&body=Document+ID%3A+json.movement-modes%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: movement modes

This is the migration draft page for `json.movement-modes`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.movement-modes`
- Target: `reference/json/movement-modes.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/movement-modes/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.movement-modes | doc/JSON/MOVE_MODE.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Movement-mode contract

`move_mode` is a generic-factory object. The current loader requires display character and name,
panel character, `exertion_level`, prepare and successful-change messages for foot, animal, and
mech contexts, and `move_type`. `move_type` accepts current prone, crouching, walking, and running
semantics; the displayed name is not the behavior type.

### Speed, stamina, and cycling

`move_speed_multiplier`, `stamina_multiplier`, `sound_multiplier`, `swim_speed_mod`,
`mech_power_use`, and `stop_hauling` affect different subsystems. A multiplier is not an isolated
balance control: terrain move cost, encumbrance, mounts, stamina, noise, and effects still contribute.

Finalization sorts modes by move-speed multiplier and builds forward and reverse cycles. Adding a
mode can change everyone's cycle order without editing existing IDs. Do not treat the order of equal
multipliers as a UI contract.

### Text and mounts

Prepare and change messages cover walking, animal, and mech contexts separately. Failure messages
have defaults, but release content should not rely on placeholder “bugs” text. Character and panel
symbols need valid Unicode and colors use the current color reader. Riding exertion may be separate,
so walking evidence does not prove mounted behavior.

### Validation

Run formatting, `make -j2 json-check`, `--check-mods`, and focused movement, stamina, sound, and
vehicle tests. Cover cycling both ways, UI symbols, failed prone/crouch/run switches, hauling,
swimming, animal and mech power, encumbrance and terrain, save reload, and translation. Record
actual movement, stamina, and sound results rather than only successful JSON loading.

## History and attribution

Accepted inventory contributors: thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `3a00588b939b053ee86e7754623a56ab4ca546f9304e4230da35cde8e69a7a3d`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MOVE_MODE.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MOVE_MODE.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MOVE_MODE.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
