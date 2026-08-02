## Climbing-aid contract

The `climbing_aid` generic factory builds a lookup by condition category and flag. Top-level `down`
and `condition` are mandatory and `slip_chance_mod` is optional. The project also requires a valid
`default` entry. Runtime constructs a fallback if missing, but consistency checking reports it.

### Condition

Type must be special, ter_furn, veh, item, character, or trait, and flag is mandatory. An item
condition also requires uses. A ter_furn condition may set range, default one. Other categories do
not read those specialized members. Uses is the item quantity consumed; condition detection and
route scanning decide availability.

### Down rules

max_height defaults to one and zero disables downward use. allow_remaining_height defaults true and
easy_climb_back_up defaults zero. When enabled, menu_text and confirm_text are mandatory. Setting
deploy_furn also makes menu_cant and a one-byte menu_hotkey mandatory; otherwise both are optional and
the hotkey is at most one byte. Cost kcal, thirst, damage, and pain apply per descended level.

Furniture deployment needs open-air, existing furniture, vehicle or creature, maximum-height, and
partial-descent review. The menu normally includes all deployable aids plus the safest non-deploying
aid, so slip modifier affects selection rather than being an isolated display number.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. In a multi-Z fixture cover descent
height, partial descent, item consumption, deployment collisions, vehicle-part length, terrain flags,
trait and character conditions, slipping, costs, and return difficulty. New boundaries need focused
climbing tests and save reload coverage.
