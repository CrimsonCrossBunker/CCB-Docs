## Boundaries of the electricity model

CCB deliberately does not simulate a complete electrical circuit. Power for handheld devices is
primarily abstracted as capacity, consumption, and a compatible battery class. Voltage, current,
series or parallel cells, and physical connectors are normally not exposed. This tradeoff lets a
player reason about runtime, carried energy, and resupply instead of wiring. When a high-draw device
really needs a restriction, express it through an existing visible contract rather than assuming an
unregistered electrical simulation.

## Current data representation

Battery cells are represented by `MAGAZINE` objects in item data. Battery ammunition categories,
capacity, default contents, and flags describe stored energy. A tool with a replaceable battery
accepts one through a `MAGAZINE_WELL` pocket. Ammo restrictions, adaptors, flags, relevant code, and
tests jointly define actual compatibility. `data/json/items/battery.json` is one entry point for
current first-party battery data, whose range now extends beyond the old table, including special
or atomic cells. The historical table is therefore not a complete inventory.

Large vehicle storage and handheld tool batteries are not one interchangeable interface. Trace the
current item, pocket, ammo, vehicle-part registrations, and tests separately before changing either
side; do not infer compatibility from display names.

## Adding or calibrating a device

1. Estimate an order of magnitude from credible real runtime and power evidence, and record the
   conditions. Manufacturer best-case advertising is not a direct test value.
2. Choose the closest existing battery class and combine its capacity with device consumption to
   obtain a reasonable runtime. Do not add types merely to reproduce multiple physical cells.
3. Inspect the tool pocket, ammo restrictions, default battery, supported adaptors, charging paths,
   and insertion and removal behavior.
4. Cover empty, partial, full, incompatible, adapted, save/reload, and charging boundaries.
5. Run JSON loading and focused battery tests. Record mod and documentation impact when a public
   JSON field or compatibility relationship changes.

Short-lived or high-draw real devices warrant tighter estimates; low-draw devices with ample
capacity tolerate wider approximations. The goal is credible runtime and clear player decisions,
not apparently precise electrical parameters that the runtime does not implement.
