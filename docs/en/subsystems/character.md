---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.character
title: Characters and Creatures Manual
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
- Lua Mod API v5
source_queries: []
source_fingerprint: 30a19e6cbd8c6709ac5ccda80fe349e9459ddaccd8d3dc96507ee282c17f48cb
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 288754596440a1d571ef830cb63b3541390668930744733d8dd833cf0158830a
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes:
- lua.v5.overview
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/character/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/character/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/character/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/character/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.character%29%3A+&body=Document+ID%3A+subsystems.character%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Characters & Creatures Manual

This manual provides a detailed technical reference for the character, avatar, NPC, and monster entity subsystems in **Cataclysm: Cleanwater Bomb (CCB)**.

---

## 1. Entity Hierarchy & Lifecycle

All living entities in CCB inherit from the `Creature` base class:

* **`Creature`**: Base class providing 3D coordinates (`tripoint`), speed counter (`moves`), HP regeneration, line-of-sight checks (`sees`), and damage dispatch.
* **`Character`**: Humanoid actor managing distinct anatomical body parts (`body_part`), pain, stamina, inventory trees, and martial arts.
* **`avatar`**: The player entity bound to the input manager and mission logs.
* **`monster`**: Non-humanoid creatures with AI trees, aggression, morale, and special attacks.

---

## 2. Anatomical Health Model (`body_part`)

A `Character`'s health is tracked across **12 anatomical body parts**:

| Body Part ID | Name | Impact |
| :--- | :--- | :--- |
| `"head"` | Head | Vital part. Zero HP results in instant death. Concussions degrade stats. |
| `"torso"` | Torso | Vital part. Zero HP causes death. Governs armor encumbrance and carry mass. |
| `"eyes"` / `"mouth"` | Eyes / Mouth | Determines visual acuity, hearing, and gas mask filtration efficiency. |
| `"arm_l"` / `"arm_r"` | Left / Right Arm | Governs melee swing speed, ranged weapon aim stability, and blocking. |
| `"hand_l"` / `"hand_r"` | Left / Right Hand | Determines fine crafting agility and grip strength. |
| `"leg_l"` / `"leg_r"` | Left / Right Leg | Dictates base movement speed. Fractures drastically increase AP movement costs. |
| `"foot_l"` / `"foot_r"` | Left / Right Foot | Influences rough terrain traversing and stamina drain. |

---

## 3. Core APIs

### `character:get_hp(part) -> integer`

Queries the current hit points of the designated body part.

**Parameters:**
* `part` (*string*, required): Target body part identifier (e.g., `"head"`, `"torso"`, `"arm_l"`).

**Returns:**
* *integer*: Current HP value.

**Example:**
```lua
local torso_hp = player:get_hp("torso")
if torso_hp < 20 then
    game.add_msg("danger", "Your torso is critically wounded, bandage immediately!")
end
```

---

### `character:mod_pain(amount)`

Modifies the pain index of the character. Pain decreases stats and movement speed.

**Parameters:**
* `amount` (*integer*, required): Value delta. Positive increases pain, negative alleviates pain (analgesic).

---

### `character:add_effect(effect_id, duration)`

Attaches a status buff or debuff to the character.

**Parameters:**
* `effect_id` (*string*, required): Status identifier (e.g., `"adrenaline"`, `"bleed"`, `"poison"`).
* `duration` (*integer*, required): Duration in **turns**.

**Example:**
```lua
player:add_effect("adrenaline", 60)
game.add_msg("info", "Adrenaline rushes through your bloodstream!")
```

---

## 4. Key Event Subscriptions

```lua
events.on("character_takes_damage", function(event)
    local victim = event.character
    local damage = event.damage
    -- Custom energy shield absorption logic
end)

events.on("character_wakes_up", function(event)
    game.add_msg("info", "You awaken as morning light filters through the shelter.")
end)
```
