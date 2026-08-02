## Current steel abstraction

CCB uses a small set of material classes to express major differences in impurities, carbon
content, and heat treatment rather than simulating complete metallurgy. Current
`data/json/materials.json` includes `budget_steel`, `lc_steel`, `mc_steel`, `hc_steel`, `ch_steel`,
`qt_steel`, and the legacy-compatible `steel`, among others. That data and its loader define real
IDs, resistances, repair materials, and descriptions. Historical SAE comparisons, skill tables, and
hour counts are design approximations, not recipe contracts.

Low-, medium-, and high-carbon, case-hardened, and quench-tempered categories should create
understandable differences in working, durability, and repair. Harder processes normally require
better heat control, tools, knowledge, time, and risk. The game may compress cooling and batching,
but an advanced steel should not become a cost-free numeric upgrade.

## Writing or migrating recipes

1. Start from current material, item, and recipe IDs and confirm what the target actually uses
   instead of inferring it from a display name.
2. Compare the real process with tool quality, proficiencies, skills, activity time, batches, fuel,
   and components that the game can currently express.
3. Separate stock production, forging, case hardening or quenching and tempering, and repair. Do not
   apply a finished-item treatment to a generic ingot when that process would not fit.
4. Prefer recovery from pre-Cataclysm vehicles, machinery, and goods. A new mining or smelting route
   must show why it is sensible under current setting and technology constraints and not busywork.
5. For upgrades and repairs, inspect `copy-from`, material, `repaired_with`, requirement groups,
   tool energy, batch time, and disassembly results.

Validation includes JSON formatting and loading, recipe reachability, component conservation, batch
scaling, tool energy, failure conditions, repair, and disassembly. Historical tables may explain a
tradeoff, but every concrete skill, time, carbon quantity, or material property must be rechecked in
current data at the pinned commit.
