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
