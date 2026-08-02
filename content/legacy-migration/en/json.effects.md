## Current CCB effect-type data

An `effect_type` defines a persistent status attached to a character or creature: names,
descriptions, intensity, duration, immunity, numerical modifiers, and periodic behavior. It is
not the same object as an Effect on Condition effect command. An EOC can add or remove an
effect type, but an `effect_type` is not an executable script.

### Basic definition

```jsonc
{
  "type": "effect_type",
  "id": "ccb_example_status",
  "name": [ "Example status" ],
  "desc": [ "You are affected by the documentation example." ],
  "max_intensity": 3,
  "max_duration": "1 hour",
  "show_in_info": true
}
```

`load_effect_type` requires a stable `id` and reads per-intensity names and descriptions,
display fields, resist, immune, block, and remove relationships, duration and intensity
evolution, messages, flags, enchantments, and modifier data. Array indexing, fallbacks, and
hardcoded behavior come from `effect.cpp` and its tests.

### Instance lifecycle

A runtime `effect` instance serializes its effect type, duration, body part, permanence,
intensity, start time, and source. Deleting or renaming a released effect ID is therefore a
save-compatibility change and needs an `effect_migration`:

```jsonc
{
  "type": "effect_migration",
  "from": "old_effect_id",
  "to": "ccb_example_status"
}
```

Confirm with current loader and deserialization tests whether omitting `to` represents removal
and when migration occurs. Consistency checking reports a missing target ID.

### Intensity, duration, and modifiers

`max_intensity`, `int_add_val`, decay fields, and `int_dur_factor` combine to control stacking
and decay. Entries below `base_mods` and `scaling_mods` for STR, DEX, PER, INT, speed, pain,
hurt, sleep, and other values use the fixed mapping in `effect_type::load_mod_data`; they are
not arbitrary property names. Bad chance, tick, min, or max combinations can create every-turn
cost or extreme values.

Body-part restrictions, resist traits or effects, immune flags, and block or remove relationships
change whether statuses can be applied or coexist. Cycles and intensity limits need focused
tests, not only a visual check of the status panel.

### Validation

1. Check `load_effect_type` and neighbouring first-party effects for shapes and intensity arrays.
2. Run the formatter, `make -j2 json-check`, and `--check-mods` for the real Mod set.
3. Run relevant `effect_test` or `creature_effect_test` cases for application, stacking, decay,
   immunity, and removal.
4. Test an old save or `effect_migration` for a released ID; never rename it silently.
5. Test periodic modifiers at intensity one, the cap, expiration, and different body parts.

For conditional execution use an [EOC](../eoc/index.md); do not hide scripted side effects in
status data.
