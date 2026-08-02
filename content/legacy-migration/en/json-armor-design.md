## Armor JSON design and review

Armor combines the item contract with `islot_armor`. Every `armor` portion requires `covers` and can
set coverage, melee, ranged, or vitals coverage, sublocations, encumbrance, materials, layers,
breathability, and environmental protection independently. Top-level fields and inheritance are then
applied to portions, so review the expanded result.

### Geometry, materials, and wearing

`specifically_covers` restricts coverage to sub-bodyparts. Without sublocation data, covering a
parent bodypart covers its subparts. `sided` lets an instance move between left and right. Layers
control clothing conflicts on shared locations; do not replace the current layer enum and runtime
checks with an arbitrary flag or historical table.

A portion material requires type, allows `covered_by_mat` only from 1 through 100, and uses thickness
for that material layer. The loader still accepts the old string-material form but marks it as legacy;
prefer auditable per-portion materials for new content. Real mass, thickness, material, coverage, and
joint mobility drive balance. Do not falsify physical properties to reach a desired defense value.

### Encumbrance, pockets, and ablative armor

Encumbrance may be one value, an empty/full pair, or use a volume modifier. Pocket modifiers,
rigidity, and contents affect the result. An insert in an ablative pocket remains an armor item; audit
its flag restriction, coverage, direct-wearing boundary, and damage or transformation together.

### Minimum-complexity principle

Ordinary clothing should express only the portions it needs. Add advanced materials, per-subpart
layers, special coverage, relic effects, or transforms only for a player-visible distinction. The old
prose's “complete flag list” is not authoritative; the flag registry and consumers are.

### Validation

Start from a current comparable first-party armor and inspect item info, layering conflicts, full and
empty pockets, sides, melee and ranged attacks, and ablative damage. Run formatting,
`make -j2 json-check`, Mod `--check-mods`, and focused item or armor tests for new boundaries. Balance
numbers also need Responsible-human review of their research sources.
