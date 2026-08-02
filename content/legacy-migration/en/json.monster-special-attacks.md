## Monster special-attack contract

`special_attacks` is an ordered capability set on a `MONSTER`. An entry may use legacy
`[ native_name, cooldown ]` syntax for a registered C++ attack or an actor object with `type` and
`id`. Actor types, fields, and behavior come from `MonsterGenerator::init_attack`,
`mattack_actors.cpp`, and tests.

### Identity, cooldowns, and conditions

Repeated actor subtypes on one monster need distinct `id` values; otherwise loading reports a
duplicate and retains only the last definition. A cooldown can use current fixed or expression forms.
Whether a failed condition, missing target, or missing resource consumes cooldown depends on the
actor call path and needs implementation-specific tests.

Leap, melee or bite, gun, spell, grab, and summon actors have different required members. For
example, leap requires `max_range` while gun reads `gun_type`, ranges or modes, targeting, and ammo.
Do not apply one actor's field table to another. A `condition` normally gets the monster as alpha;
beta availability depends on how that actor constructs its dialogue.

### Inheritance and side effects

The Monster `copy-from` reader supports replacement or deletion, with names and `id` values
determining the result. Self or target effects, fields, spawns, sounds, messages, ammo, item, and
spell IDs must exist. Attacks can mutate maps, cross z-levels, grab body parts, or establish targeting
state; failure paths must clean up state.

### Validation

Run formatting, `make -j2 json-check`, `--check-mods` for the real Mod, and relevant
`monster_attack_test`, `mondefense_test`, and actor tests. Cover no target, invisible targets,
minimum and maximum range, obstacles, cooldowns, empty ammo, false conditions, player/NPC/monster
targets, save reload, and duplicate actor IDs. Profile frequent path searches, AoE, spawn, and field
actors.
