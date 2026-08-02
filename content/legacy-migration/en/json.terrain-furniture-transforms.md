## Current CCB terrain and furniture transforms

A `ter_furn_transform` is a named reusable tile-conversion table. It matches terrain,
furniture, fields, and traps independently, then selects a replacement from a weighted
`result`. Matching terrain does not automatically create related furniture.

### Basic definition

```jsonc
{
  "type": "ter_furn_transform",
  "id": "ccb_example_transform",
  "terrain": [
    {
      "valid_terrain": [ "t_sand" ],
      "result": [ [ "t_dirt", 4 ], "t_grass" ],
      "message": "The sand shifts.",
      "message_good": true
    }
  ]
}
```

A plain result has weight one; a two-element array supplies a weight. `message_good` defaults
to true. Terrain and furniture can also match `valid_flags`; fields and traps use their own
valid-ID members. Use `ter_furn_transform::load` for the current member names and flag support.

### Matching and conflicts

The loader maps each valid ID or flag to transformation data. When several rules cover one
input, do not use container insertion order as a content-priority mechanism. Keep match sets
disjoint or add a test proving the intended result. Clearing values such as `f_null` and
`fd_null` are real IDs in their systems; JSON null is not a replacement.

Mapgen placings, radius EOC effects, spells, and other callers can invoke a transform. The caller
defines position, range, talkers, repetition, and message display. A transform does not remember
that it already ran. Repetition must be deliberate, especially with random results or possible
A-to-B-to-A cycles.

### Validation

1. Check every valid and result terrain, furniture, field, trap ID, and flag.
2. Run the formatter, `make -j2 json-check`, and `--check-mods` for the actual Mod set.
3. Test every input category, no match, several flags, weight boundaries, and null or clear results.
4. Test range, z-level, repeated execution, and messages from each real call site.
5. Run `mapgen_function_test` for mapgen callers and the relevant focused test for EOC or spell callers.

Use a transform for declarative same-tile type replacement. Put cross-tile behavior, condition
chains, and side effects in the EOC or mapgen caller instead of relying on rule-overlap accidents.
