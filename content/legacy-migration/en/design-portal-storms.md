## The role of a portal storm

A portal storm is anomalous weather and an interdimensional collision that changes a player's
plans, not a scheduled boss fight. It should create unease, disruption, and compound pressure, but
must not depend on unwarned damage to kill a character or force every player to sleep through it.
Sound shelter should matter, while a prepared character may choose to travel at genuine risk rather
than with guaranteed safety.

### Passive and active pressure

- **Passive effects** express worlds colliding: anomalous entities, obstacles, sensory interference,
  or temporary environmental changes. They should not actively hunt the player or spend the
  attention resource known as `ire`.
- **Active effects** express malicious entities noticing an exposed character. They may track,
  sabotage, or force route changes, but need the appropriate trigger and an `ire` cost so pressure
  does not stack without bound.
- A themed storm need not reuse identical resource names, but must still explain what is ambient,
  what can target a character, and how a player observes and reduces risk.

Current first-party data still registers `EOC_PORTAL_EFFECTS_PASSIVE` and
`EOC_PORTAL_EFFECTS_ACTIVE` in
`data/json/effects_on_condition/nether_eocs/portal_storm_effect_on_condition.json`. The EOC chain,
related mapgen, and calling code define actual weights, conditions, variables, and effects; this
page does not freeze their numeric values.

## Content review checklist

Limit repeated messages and effect frequency so sound, visuals, and behavior convey the anomaly.
Cover indoor and outdoor boundaries, underground areas and vehicles, sight, sleep and activity
interruptions, NPCs, different senses, save/reload, and repeated storms over time. A new EOC needs
condition, `ire` accounting, failure-path, and repeat-execution validation plus JSON/EOC loading and
focused tests. Long-term ideas such as localized trackable storms or additional themes remain
possible directions, not claims about current implementation.
