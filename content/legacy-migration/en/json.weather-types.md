## Weather types and generators

A `weather_type` describes presentation and runtime effects for one weather, while a
`weather_generator` selects candidates and base climate. They are separate object types. Global
consistency requires valid `null` and `clear` weather IDs.

### Weather-type loader

Name, id, sym, ranged_penalty, sight_penalty, light_modifier, priority, sound_attn, dangerous,
precip, and rains are mandatory. Optional members include UI colors and sun symbol, temperature,
light, and sun modifiers, sound and tiles animation, duration, passive field effects, debug EOCs,
required_weathers, and condition. Duration bounds default to five minutes and minimum cannot exceed
maximum.

Condition runs with dialogue context such as `weather_location`. Candidates are sorted by priority
and required weathers must reference valid IDs. File order is not a stable priority, and historical
sound or precipitation tables are not complete; inspect current enums.

### Weather generator

A generator requires base temperature, humidity, pressure, and wind. It may configure seasonal
adjustments, wind distribution, and a weather whitelist or blacklist. The lists are mutually
exclusive. Finalization filters and sorts by priority, while a whitelist path retains clear.

### Validation

Run formatting, `make -j2 json-check`, Mod `--check-mods`, and focused weather tests. With a fixed
seed cover seasons, locations, condition and priority ties, required chains, duration bounds,
indoor/vehicle passive effects, debug EOCs, light, sight, sound, and whitelists. Weather changes may
affect current saved weather and long-term world generation, so state compatibility and balance
impact.
