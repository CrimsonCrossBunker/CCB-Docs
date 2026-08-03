---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.missions
title: 'Legacy migration draft: missions'
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
- doc/JSON/MISSIONS_JSON.md
- src/missiondef.cpp
- src/mission.cpp
- src/npctalk.cpp
- data/json/npcs/missiondef.json
- tests/mission_test.cpp
source_symbols:
- mission_type::load
- json_talk_topic::load
source_queries: []
source_fingerprint: 481a644bd91a15b8782ffe06487427489aeefdd0193f6898b30b059790db353b
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b90beff44fd9dc7f9ac4468b8f37145814a83c2acc27311df4a8d78d35aa166f
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Maleclypse, thaelina; accepted inventory identities only. Source paths
  and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/missions/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/missions/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/missions/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/missions/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/JSON/MISSIONS_JSON.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MISSIONS_JSON.md
- path: src/missiondef.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/missiondef.cpp
- path: src/mission.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/mission.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/src/npctalk.cpp
- path: data/json/npcs/missiondef.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/json/npcs/missiondef.json
- path: tests/mission_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/mission_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.missions%29%3A+&body=Document+ID%3A+json.missions%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Legacy migration draft: missions

This is the migration draft page for `json.missions`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.missions`
- Target: `reference/json/missions.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/missions/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.missions | doc/JSON/MISSIONS_JSON.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB mission-definition model

A `mission_definition` is the template for an assignable mission. A runtime mission instance
references its stable ID and saves state, target, deadline, giver, and other data. Renaming a
released ID affects saves, NPC dialogue, and follow-up chains. Goals, dialogue, and start,
end, or fail behavior cross the mission loader, talker and EOC system, and map code, so they
need end-to-end validation.

### Basic definition

```jsonc
{
  "type": "mission_definition",
  "id": "MISSION_CCB_EXAMPLE",
  "name": { "str": "Find an example part" },
  "description": "Bring an example part back to the mission giver.",
  "goal": "MGOAL_FIND_ITEM",
  "item": "ccb_example_part",
  "count": 1,
  "difficulty": 1,
  "value": 1000,
  "origins": [ "ORIGIN_ANY_NPC" ],
  "dialogue": {
    "describe": "I need a part.",
    "offer": "Could you find an example part?",
    "accepted": "Thank you.",
    "rejected": "Maybe later.",
    "advice": "Look nearby.",
    "inquire": "Did you find it?",
    "success": "Exactly what I needed.",
    "success_lie": "You do not have it.",
    "failure": "We will have to manage without it."
  }
}
```

The current `mission_type::load` requires `name`, `difficulty`, `value`, and `goal`. When
origins contains `ORIGIN_ANY_NPC`, `ORIGIN_OPENER_NPC`, or `ORIGIN_SECONDARY`, all nine
dialogue fields above are mandatory. A different origin still needs a real assignment entry;
the definition's existence does not make it reachable.

### Goals and target fields

Different `MGOAL_*` values use item, item group, count, monster type or species, destination,
or `goal_condition`. After choosing a goal, inspect the current enum and loader plus a
first-party mission with that goal for its companion fields. Unrelated fields do not become
completion conditions. `MGOAL_CONDITION` uses a dialogue condition and depends on the talker
and context supplied during mission checking.

`deadline`, urgency, required, removed, or empty containers, generic rewards, and
invisible-on-complete settings affect UI and settlement. A follow-up references another
mission ID; check for cycles, unreachable missions, and giver dialogue.

### Start, end, and fail phases

Each phase can name a registered hardcoded mission function or contain an object read by
`parse_funcs`, including effects, mission-target assignment, and mapgen updates:

```jsonc
"start": {
  "effect": { "u_message": "Mission started." },
  "assign_mission_target": {
    "om_terrain": "field",
    "random": true,
    "reveal_radius": 1
  }
}
```

Alpha and beta often correspond to the player and mission giver, but the phase and assignment
source determine actual talkers. Map-target search, special placement, z-level, and reveal can
fail. Cover the no-target path instead of assuming world generation satisfies every constraint.

### NPC dialogue wiring

The NPC template and dialogue need routes to list, accept, inquire about, and complete a mission.
`mission_offered`, origins, follow-up, and `TALK_MISSION_*` nodes must form a reachable graph.
See [NPCs and dialogue](../eoc/npcs-and-dialogue.md).

### Validation

Run the formatter, `make -j2 json-check`, `--check-mods` for the actual Mod set, and relevant
`mission_test` and `npc_talk_test` cases. Exercise assignment, rejection, acceptance, target
generation, completion, failure, deadlines, save and load, and follow-up. Also test missing
items, terrain, or topics, an unplaceable target, and old saved IDs.

## History and attribution

Accepted inventory contributors: Maleclypse, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `d32b9cc880a85480840d82cfa05d256c78a16615`; the aggregate source fingerprint is `481a644bd91a15b8782ffe06487427489aeefdd0193f6898b30b059790db353b`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/MISSIONS_JSON.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MISSIONS_JSON.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/JSON/MISSIONS_JSON.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
