---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.wounds
title: 'Legacy migration draft: wounds'
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
- doc/JSON/WOUNDS.md
- src/wound.cpp
- src/wound.h
- src/init.cpp
source_symbols:
- wound_type::load
- wound_fix::load
source_queries: []
source_fingerprint: ef0fb6b359a73bb54b104854bcea65edc98edadcc35797a645434a547424ea53
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 9f8bde6a2118c68e195d01abefbac3af74ad206791079b5000598638de670933
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Anton Simakov, GuardianDll, thaelina; accepted inventory identities only.
  Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/wounds/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/wounds/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/wounds/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/wounds/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/WOUNDS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/WOUNDS.md
- path: src/wound.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/wound.cpp
- path: src/wound.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/wound.h
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/init.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.wounds%29%3A+&body=Document+ID%3A+json.wounds%0ALanguage%3A+en%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: wounds

This is the migration draft page for `json.wounds`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.wounds`
- Target: `reference/json/wounds.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/wounds/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.wounds | doc/JSON/WOUNDS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Wounds and wound fixes

A `wound` is persistent state bound to a bodypart and a `wound_fix` is a treatment definition. Each
has its own generic factory. During finalization, fixes resolve requirements and register backward
links on wounds they remove. They are not aliases for ordinary effects.

### Wound fields

Name, description, damage_types, and damage_required are mandatory. Pain defaults to 0–0, healing
time to indefinitely long, weight to one, and limit to zero. Optional members cover limb scores,
progression, and bodypart type or flag allow/deny lists. A progression requires id and bounds chance
from 0 through 100. Range ordering, damage IDs, and progression IDs need consumer tests because
`wound_type::check` is currently empty.

### Wound-fix fields

Name and description are mandatory. Time, skills, removed and added wounds, success message, HP
modifier, proficiencies, and requirements are optional. A proficiency entry requires an ID, defaults
time_save to one, and defaults is_mandatory false. Requirements may reference `[id, count]` or define
one inline requirement and are consolidated at finalization.

Fix consistency validates skill, wound, proficiency, and requirement IDs. Deleting or renaming a
wound affects saves, progression, and fixes and needs an explicit migration or compatibility
strategy. Do not assume safety when no automatic wound-migration contract exists.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. Focused wound tests need damage
thresholds, per-limb limits, allow/deny lists, progression, random pain and healing ranges, mandatory
proficiencies, requirement consumption, add and remove, positive and negative HP changes, and save
reload. Mark destructive or unimplemented combinations experimental rather than publishing them
solely because JSON loads.

## History and attribution

Accepted inventory contributors: Anton Simakov, GuardianDll, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`; the aggregate source fingerprint is `ef0fb6b359a73bb54b104854bcea65edc98edadcc35797a645434a547424ea53`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/WOUNDS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/WOUNDS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/WOUNDS.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
