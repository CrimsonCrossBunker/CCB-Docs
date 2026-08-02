## Relics and procedural artifacts

An artifact combines a base item with relic data. Premade relics and `relic_procgen_data` are distinct
paths. A procgen dataset supplies weighted base items, charge templates, active spells, passive
enchantment values, and type weights. Generation rules set power budget, attribute limit, negative
power allowance, and resonance.

### Procgen lists

Every weighted entry requires weight. A passive entry requires an enchantment value type and may set
minimum, maximum, increment, power per increment, and ench_has. An active entry requires spell_id and
may set levels, power, and ench_has. Item entries require item and type-weight entries require a
usable value. Dataset checks validate active spells but do not prove balance, item suitability, or
that every enchantment consumer is meaningful.

### Charges

A charge template contains range and power objects for max_charges, charges, and charges_per_use,
plus recharge_type and time. Generation clamps starting charges to the maximum and selects time from
the range. The current procgen-template loader does not read the historical `recharge_condition`
field. That member exists on generated runtime charge information and must not be presented as this
JSON input contract.

Take recharge-type and ench_has enums from `relic.cpp`. Multiple generated active spells share one
activation charge cost. Verify how their activation requirements combine with the current generator.

### Power, resonance, and validation

Power is a generator selection budget, not automatic balance proof. A resonant generation rule feeds
final power into current resonance runtime; thresholds, effects, and lore are behavior and design
contracts and cannot be copied from stale prose.

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. Generate many samples with a fixed RNG
seed and inspect empty weighted lists, invalid spells or items, charge bounds, positive and negative
budgets, activation positions, save reload, and resonance. Generator changes need deterministic
distribution and consistency tests.
