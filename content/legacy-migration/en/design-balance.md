## What balance documentation is for

CCB balance goals help contributors make consistent tradeoffs among verisimilitude, readability,
risk, resource cost, and long-term progression. They do not establish permanent numeric limits for
every value. The old stat, skill, monster, weapon, and resource tables captured reference points at
the time they were written. They can explain intent, but they are not current runtime contracts.
Rebuild the baseline from current JSON, C++, tests, and observed game data before making a change.

### Define the problem first

1. Describe the current player-visible behavior, a repeatable scenario, and the affected stage of
   progression.
2. Locate the loaders, formulas, data objects, and tests that implement it instead of copying
   numbers from a superficially similar entry.
3. Distinguish bug fixes, content calibration, difficulty preferences, and new mechanics. They need
   different evidence and may need different options or compatibility treatment.
4. Consider acquisition, time, noise, carrying cost, durability, damage, recovery, and enemy
   counterplay together. Avoid balancing an ecosystem through one number alone.
5. Compare representative early-, middle-, and late-game scenarios before and after the change,
   including random and extreme cases.

## Balance principles

- Real-world evidence constrains plausible ranges, while the game compresses complex systems into
  mechanics players can understand and operate.
- Powerful tools may remain powerful. Scarcity, supply, time, noise, mass, exposure, and maintenance
  can provide tradeoffs without forcing every option to be equivalent.
- Prefer enemies and equipment that create different decisions over an endless race of larger hit
  point, armor, and damage values.
- Lethal outcomes without warning or reasonable counterplay are rarely meaningful difficulty.
  Hazards should normally expose observable cues and learnable responses.
- Save and mod compatibility are design constraints. Changes to IDs, serialized fields,
  inheritance, or widely reused data require a separate migration assessment.

## Evidence and validation

A design statement can propose direction; it cannot prove that behavior is implemented. A balance
change should cite current source paths and tests, provide reproducible comparison steps, and run
the relevant JSON loading, focused unit tests, or live game scenario. When an old table or example
does not match current data, cite it as a historical snapshot instead of silently turning it into a
new authority.
