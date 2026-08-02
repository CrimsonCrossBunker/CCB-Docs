## Wounds and wound fixes

A `wound` is persistent state bound to a bodypart and a `wound_fix` is a treatment definition. Each
has its own generic factory. During finalization, fixes resolve requirements and register backward
links on wounds they remove. They are not aliases for ordinary effects.

### Wound fields

Name, description, damage_types, and damage_required are mandatory. Pain defaults to 0–0, healing
time to indefinitely long, weight to one, and limit to zero. Optional members cover limb scores,
progression, and bodypart type or flag allow/deny lists. A progression requires id and bounds chance
from 0 through 100. Range ordering, damage IDs, and progression IDs need consumer tests because
`wound_type::check` is currently empty.

### Wound-fix fields

Name and description are mandatory. Time, skills, removed and added wounds, success message, HP
modifier, proficiencies, and requirements are optional. A proficiency entry requires an ID, defaults
time_save to one, and defaults is_mandatory false. Requirements may reference `[id, count]` or define
one inline requirement and are consolidated at finalization.

Fix consistency validates skill, wound, proficiency, and requirement IDs. Deleting or renaming a
wound affects saves, progression, and fixes and needs an explicit migration or compatibility
strategy. Do not assume safety when no automatic wound-migration contract exists.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. Focused wound tests need damage
thresholds, per-limb limits, allow/deny lists, progression, random pain and healing ranges, mandatory
proficiencies, requirement consumption, add and remove, positive and negative HP changes, and save
reload. Mark destructive or unimplemented combinations experimental rather than publishing them
solely because JSON loads.
