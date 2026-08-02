## Movement-mode contract

`move_mode` is a generic-factory object. The current loader requires display character and name,
panel character, `exertion_level`, prepare and successful-change messages for foot, animal, and
mech contexts, and `move_type`. `move_type` accepts current prone, crouching, walking, and running
semantics; the displayed name is not the behavior type.

### Speed, stamina, and cycling

`move_speed_multiplier`, `stamina_multiplier`, `sound_multiplier`, `swim_speed_mod`,
`mech_power_use`, and `stop_hauling` affect different subsystems. A multiplier is not an isolated
balance control: terrain move cost, encumbrance, mounts, stamina, noise, and effects still contribute.

Finalization sorts modes by move-speed multiplier and builds forward and reverse cycles. Adding a
mode can change everyone's cycle order without editing existing IDs. Do not treat the order of equal
multipliers as a UI contract.

### Text and mounts

Prepare and change messages cover walking, animal, and mech contexts separately. Failure messages
have defaults, but release content should not rely on placeholder “bugs” text. Character and panel
symbols need valid Unicode and colors use the current color reader. Riding exertion may be separate,
so walking evidence does not prove mounted behavior.

### Validation

Run formatting, `make -j2 json-check`, `--check-mods`, and focused movement, stamina, sound, and
vehicle tests. Cover cycling both ways, UI symbols, failed prone/crouch/run switches, hauling,
swimming, animal and mech power, encumbrance and terrain, save reload, and translation. Record
actual movement, stamina, and sound results rather than only successful JSON loading.
