## NPC-faction contract

A `FACTION` template is loaded by `faction_template` and later instantiated as a world faction.
The current constructor requires `id`, `name`, `description`, `likes_u`, `respects_u`,
`known_by_u`, `size`, `power`, and `wealth`. Trust, food, currency, price rules, claims, monster
faction, relations, and epilogues are additional contracts.

### Identity, relations, and economy

Faction IDs enter NPCs, dialogue, missions, camps, EOCs, and saves. Display names translate, but IDs
must not be casually renamed. `relations` is a directional bitset keyed by target faction ID; A's
kill, watch, or share relation to B does not guarantee the reverse relation. Validate every target
and relation flag against current registrations.

A `currency` also creates a price rule. Rules can match current item-group criteria and set markup,
premium, fixed adjustment, or price. Trading still depends on NPC, supply, skills, and other systems;
one item is insufficient evidence.

### World state and compatibility

A template initializes a new faction. A save may contain changed likes, respect, trust, wealth, food,
and membership. Editing the template does not migrate an existing world. Before removing or renaming
an ID, design save migration and update every cross-object reference.

Epilogue snippets, monster factions, currency or item groups, and mission IDs need consistency
checks. `known_by_u`, limited-area claims, and lone-wolf behavior need scenario tests.

### Validation

Run formatting, `make -j2 json-check`, `--check-mods`, and faction price, mission, camp, and NPC
dialogue tests. Cover directional relations, theft or attacks, pricing, food and wealth, epilogues,
new and old worlds, Mod combinations, and missing target IDs.
