---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.npcs-dialogue
title: 'Legacy migration draft: npcs and dialogue'
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
- doc/JSON/NPCs.md
- src/npc.cpp
- src/npc_class.cpp
- src/npctalk.cpp
- data/json/npcs/missiondef.json
- tests/npc_talk_test.cpp
source_symbols:
- npc_template::load
- npc_class::load
- json_talk_topic::load
source_queries: []
source_fingerprint: 9e6515c57f4bec96e397fe7ce1624895b165ed1c1d32cceae8e1a50a6cadf6cc
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 5d3c92e04a9f29139d9354752836a8e8c017254b66f1650b0d6e204f6845f8c5
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Killa-bite, Standing-Storm, Maleclypse, LunaGlaze, 李诗琪, Anton Simakov,
  Tektolnes, RenechCDDA, thaelina; accepted inventory identities only. Source paths and Git history remain
  authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: eoc
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/npcs-and-dialogue/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/eoc/npcs-and-dialogue/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/NPCs.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/NPCs.md
- path: src/npc.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/npc.cpp
- path: src/npc_class.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/npc_class.cpp
- path: src/npctalk.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/npctalk.cpp
- path: data/json/npcs/missiondef.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/data/json/npcs/missiondef.json
- path: tests/npc_talk_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/tests/npc_talk_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.npcs-dialogue%29%3A+&body=Document+ID%3A+json.npcs-dialogue%0ALanguage%3A+en%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Legacy migration draft: npcs and dialogue

This is the migration draft page for `json.npcs-dialogue`. It records **1** frozen inventory record(s), but it does not promote legacy prose into a runtime contract.

- Stable document IDs: `json.npcs-dialogue`
- Target: `reference/eoc/npcs-and-dialogue.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/eoc/npcs-and-dialogue/
- Archive reason: —

## Inventory records

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.npcs-dialogue | doc/JSON/NPCs.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## Authority boundary

CCB source and tests remain authoritative for runtime behaviour; schemas, declarations, registrations, and generated inventories govern JSON/Lua/API; CI, CMake, Makefile, and Gradle govern builds. This page explains migration state, history, and auditable provenance only. A current contract wins over conflicting legacy prose.

## Current CCB NPC and dialogue structure

NPC content normally spans three independent objects: `npc` defines a concrete template and
initial relationships, `npc_class` defines generated attributes and equipment distributions,
and `talk_topic` defines the dialogue graph. Missions, factions, item groups, skills, traits,
effects, and topics connect through stable IDs. One loadable file does not prove that the
complete conversation is reachable.

### NPC template

```jsonc
{
  "type": "npc",
  "id": "ccb_example_npc",
  "name_unique": "Example Keeper",
  "gender": "female",
  "class": "NC_CCB_EXAMPLE",
  "faction": "your_followers",
  "attitude": 0,
  "mission": "GUARD",
  "chat": "TALK_CCB_EXAMPLE"
}
```

`npc_template::load` reads the template and composes behavior through class, faction, mission,
and chat IDs. Confirm that a spawn or caller can actually create a new template; manually
spawning it from the Debug menu is not a complete flow test. Random NPC attributes belong in
`npc_class`; named-NPC specifics belong in the template or dialogue.

### Talk topics and responses

```jsonc
{
  "type": "talk_topic",
  "id": "TALK_CCB_EXAMPLE",
  "dynamic_line": "Welcome.",
  "responses": [
    { "text": "Goodbye.", "topic": "TALK_DONE" }
  ]
}
```

`json_talk_topic::load` reads dynamic lines, speaker effects, responses, and repeat responses.
An empty final response list is an error. Responses on an existing topic may be appended by
load order; `replace_built_in_responses` and `insert_before_standard_exits` change composition.
A Mod patch needs declared dependencies and a test of the final graph.

A response condition controls visibility, while success or failure effects choose side effects
and the next topic. Every visible branch should exit or reach another valid node. Avoid
unconditional cycles, empty screens, and mission dialogue with no route back.

### Talker and EOC semantics

In traditional dialogue alpha is usually the player and beta the NPC, so conditions and effects
use `u_` and `npc_` prefixes. If another system invokes the same topic or EOC, talker types can
differ. Check the [condition index](../eoc-conditions.md),
[effect index](../eoc-effects.md), and the actual call site.

Dynamic lines, response text, NPC names, and mission dialogue are player-facing. Use translation
objects or the translatable string form required by the current field, preserve placeholders
and context, and test width and plurals.

### Mission wiring

For an NPC-offered mission, the template's `mission_offered`, the mission definition's origins
and dialogue, and topics leading to mission list or inquiry must agree. Custom completion
conditions and start, end, or fail effects still use the talker and EOC system. See
[missions](../json/missions.md).

### Validation

Run the JSON loader, ID checks, `--check-mods` for the actual Mod set, and relevant
`npc_talk_test` cases. Exercise first contact, hidden and visible conditions, success, failure,
repeat responses, mission acceptance and completion, and exit paths. Also test missing NPCs,
missing topics, and different load order.

## History and attribution

Accepted inventory contributors: Killa-bite, Standing-Storm, Maleclypse, LunaGlaze, 李诗琪, Anton Simakov, Tektolnes, RenechCDDA, thaelina. License: CC-BY-SA-3.0. Raw rejected or anomalous contributor values were not imported or published.

The source inventory is frozen at `0378ca2b84303cf614c617c9d9eaa50138cd21ff`; this cross-repository verification uses `c1b0f95c6d1b074fc49ee2a7976819c124b69047`; the aggregate source fingerprint is `9e6515c57f4bec96e397fe7ce1624895b165ed1c1d32cceae8e1a50a6cadf6cc`. The [filtered-history experiment](/CCB-Docs/en/migration/filtered-history-experiment/) explains why the whole game repository history is not imported.

## Bodies retained in CCB

- [`doc/JSON/NPCs.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/NPCs.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/NPCs.md)

## Replacement and next step

This page remains Draft until a Responsible human reviews the prose, sources, and replacement relationship. Drafts stay outside production navigation, search, and the AI allowlist.
