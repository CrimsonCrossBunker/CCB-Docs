## Separate design from current implementation

The legacy faction page mixes implemented groups, empty sections, future mission concepts, and
author speculation. It is not a current game-status inventory. First-party faction IDs and base
relations, currency, food, wealth, and epilogue data come from `data/json/npcs/factions.json` and the
`faction` loader. NPCs, dialogue, missions, mapgen, and tests determine whom a player can actually
meet and how they behave. Mark conflicting prose stale and repair it from those sources.

## Faction writing template

A faction page or proposal should distinguish at least:

- **Identity and origin:** how members formed and which facts are player-visible or backstage
  spoilers.
- **Structure and scale:** leadership, membership, dependencies, and geographic reach, labeling a
  number as implemented data or narrative estimate.
- **Goals and limits:** immediate needs, long-term direction, and what the group cannot or will not
  do.
- **Relations:** attitudes toward the player, human groups, mutation or augmentation, and non-human
  powers, including conditions that change them.
- **Bases and economy:** real locations, currency, sources of goods, production capacity, and supply
  bottlenecks.
- **Missions and development:** current mission IDs and dialogue entry points, planned content, and
  stages that alter world or save state.

The Blob, Mycus, triffids, netherum, Exodii, Yrax, and mi-go need not follow a human-state model.
Preserve their different perception, timescale, communication, and values instead of making an
incommunicable power suddenly use ordinary barter or moral language merely to supply a quest.

## Validation

For a faction change, inspect stable IDs, `copy-from`, relation symmetry, monster faction, currency,
price rules, food, epilogues, NPC classes, dialogue talkers, missions, and mapgen references. Run
JSON/EOC loading, duplicate and invalid-ID checks, and relevant faction or monster-faction tests;
exercise first discovery, hostility changes, trade, mission stages, and save/reload in game. Keep
unimplemented diplomacy, bases, and endings draft instead of presenting them as current features.
