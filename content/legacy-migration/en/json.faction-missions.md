## Faction mission data boundary

The `faction_mission` generic factory currently supplies names, descriptions, and display metadata
for basecamp missions. Target selection, NPC dispatch, rewards or risk, and map mutation remain
largely implemented by C++ consumers such as `faction_camp.cpp`. Adding a JSON object does not create
an executable mission system.

### Loader fields

Name and desc are mandatory. Skill, difficulty, risk, activity, time, positions, items_label,
items_possibilities, effects, and footer are optional. Difficulty and risk accept only NONE,
VERY_LOW, LOW, MEDIUM, HIGH, and VERY_HIGH. Activity must exist in the activity-level map or the
loader reports it as invalid.

Time, effects, and item fields are translated descriptions rather than a structured duration, loot
table, or effect program. They must accurately describe the matching hardcoded consumer and cannot
replace consumer tests.

### Adding or changing a mission

Find camp code and unlock conditions that consume the mission ID before editing its display object.
Check positions, real duration, skill training, food or gear transfer, failure and risk, and repeat
semantics. A new data-driven behavior first needs a public execution contract, loader, and tests;
natural-language effects are not instructions.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. In the camp menu, check zero, one, and
multiple-NPC displays, translations, unavailable reasons, departure and return, and repeat missions.
A new ID or behavior needs focused faction-camp tests and prose that agrees with the implementation.
