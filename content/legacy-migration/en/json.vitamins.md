## A `vitamin` object is not only a nutrient

CCB's `vitamin` registry is a general system for quantities in a character that change over time.
`vit_type` currently accepts `vitamin`, `toxin`, `drug`, and `counter`. First-party data uses it not
only for calcium, iron, and vitamin C, but also drug doses, mutagen primers, blood-related counters,
allergens, and hidden state. The object type name does not guarantee appearance in nutrition UI.

### Loader fields

In addition to generic-factory `id` and `type`, a new definition must provide `name`, `vit_type`,
`min`, and `rate`. `max` is optional and currently defaults to `0`. `deficiency` and `excess`
reference effect types. `disease` and `disease_excess` are quantity ranges whose order maps to
effect intensity. `weight_per_unit` converts mass into internal units. Every `decays_into` entry is
a target vitamin ID and signed adjustment applied separately when one unit is naturally metabolized.
`flags` is a string set; confirm each flag's consumer in current code and data.

```json
{
  "type": "vitamin",
  "id": "example_counter",
  "vit_type": "counter",
  "name": { "str": "Example counter" },
  "min": 0,
  "max": 100,
  "rate": "1 h",
  "excess": "example_effect",
  "disease_excess": [ [ 10, 49 ], [ 50, 100 ] ]
}
```

This illustrates structure and is not a proposed first-party ID. The loader accepts either order
for each range endpoint, but overlaps and gaps still create hard-to-understand results. Design
continuous, testable thresholds.

## Inheritance, units, and validation

Vitamins support `copy-from` through `generic_factory`. Current tests cover scalar overrides and
`extend` or `delete` for `flags`, `disease`, `disease_excess`, and `decays_into`. Flags deduplicate as
a set. Duplicate decay targets remain independent rules and do not sum automatically. When a mod
overrides an existing `id`, the last loaded definition wins, so load-order compatibility matters.

Nutritional values in food JSON are commonly expressed as RDA percentages, while other types use
their internal units. `rate` controls daily absorption and decay conversion, and
`weight_per_unit` controls mass conversion. Run JSON formatting and loading, vitamin consistency,
and focused `[vitamin]` tests for a new object. Cover effect IDs, boundary amounts, inheritance,
natural decay, simplified nutrition, display flags, ingestion delay, and save/reload. Do not freeze
the legacy MME table or current first-party values as a permanent schema.
