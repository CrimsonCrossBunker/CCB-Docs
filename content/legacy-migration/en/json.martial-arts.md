## Current CCB Martial Arts object graph

Martial arts are not one JSON object. The runtime separately registers `attack_vector`,
`weapon_category`, `technique`, `martial_art`, and buffs. A style references techniques and
weapons or categories, then applies buffs or EOCs at combat events.

### Styles and techniques

A `martial_art` needs a stable `id`, `name`, `description`, and `initiate`. `autolearn` contains
skill and level pairs; `primary_skill`, `learn_difficulty`, `teachable`, `weapons`, and
`weapon_category` govern learning and eligible weapons. Validate `strictly_melee` and related
limits through both UI and actual selection logic.

A `technique` currently requires at least `name` and normally provides player/NPC messages and
`attack_vectors`. Critical, counter, disarm, knockback, AoE, repeat, condition, requirement, and
bonus data jointly determine candidacy and execution. Consistency checking reports an ordinary
attack technique without an attack vector; defensive, dummy, grab-break, and miss-recovery types
are exceptions.

### Attack vectors, requirements, and buffs

An `attack_vector` describes weapon or limb use, contact area, limb HP, encumbrance, armor bonus,
and required or forbidden limb flags. It is not just an animation label: selected limbs and contact
affect eligibility, damage, and tests.

A style can attach buffs and inline EOCs at static, move, pause, hit, attack, dodge, block, get-hit,
miss, critical, and kill events. Buffs define duration, stacks, persistence, dodge or block, bonuses,
and requirements. Each event has different actors, weapons, targets, and frequency; an EOC must not
assume a beta talker always exists.

Requirements combine skills, weapon damage, weapon categories, buffs, and character flags. Holding
an allowed weapon does not prove a technique passes limb, condition, ammo, range, or cooldown gates.

### Design and validation

1. Start from the closest first-party style graph and preserve ID prefixes and translated messages.
2. Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set.
3. Run `martial_art_test` for weapon categories, limb substitution, HP, encumbrance, conditions,
   sweep, stun, and knockback.
4. In game, cover unarmed use, every weapon class, injury and high encumbrance, NPCs, criticals,
   counters, and every buff or EOC event.
5. Record DPS, hit and defense changes, stacks, and trigger frequency. Loading does not disprove
   infinite stacking or forced loops.

Legacy bonus strings and flag lists can drift. Use current loaders and consistency checks for exact
enums and bounds.
