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
