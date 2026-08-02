## CCB gameplay direction

CCB is an open-world survival game. Its core experience comes from planning with incomplete
information, limited resources, and a changing environment; taking understandable risks; and
dealing with the consequences of those plans. World simulation should support those decisions,
not add unobservable detail solely for the sake of simulation.

### Properties contributors should preserve

- Time, position, noise, weather, carrying capacity, injury, supply, and enemy behavior should form
  connected choices.
- A strong solution may be clearly better than an improvised one, but should have acquisition,
  operation, maintenance, or exposure costs that make sense in the world.
- Separate character knowledge, player knowledge, and interface hints. Danger may surprise, but
  should not depend on arbitrary rules that cannot be learned.
- Failure should normally be traceable to observable decisions. Necessary randomness needs bounded
  outcomes, feedback, and appropriate recovery space.
- Automation and convenience should remove repetition while retaining meaningful route, resource,
  time, and risk decisions.
- NPCs, factions, missions, and world events should interact through shared systems where possible
  instead of creating exceptions for a single script.

## Verisimilitude and abstraction

Verisimilitude determines what is plausible in the world; abstraction selects which details are
worth operating as a player. A contributor may omit electrical parameters, repeated labor, or
invisible microscopic processes while preserving consequences that change strategy. Conversely,
being “more realistic” is not enough to justify a mechanic: explain how a player understands and
responds to it and how it composes with existing systems.

## Intent is not implementation

The legacy design documents mix long-term vision, implementation at the time, and unfinished
ideas. The migrated text retains reusable principles, but every concrete behavior must still be
confirmed in current C++, JSON, Lua registrations, and tests. Proposals should label current
behavior, desired behavior, and possible future direction explicitly. Do not write aspiration as an
existing contract. Governance and merge decisions follow current `GOVERNANCE.md`, not personal
authority statements preserved in old prose.
