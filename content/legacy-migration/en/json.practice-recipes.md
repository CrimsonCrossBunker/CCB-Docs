## Practice recipes

`type: practice` uses the main recipe dictionary and crafting UI but has no ordinary result. The
loader rejects `result` and `difficulty`, and requires id, name, category, subcategory, and
`practice_data`; description is optional. Components, tools, using, skill and proficiency,
autolearn, and book learning share recipe contracts, while byproducts remain available.

### practice_data

`min_difficulty` has no separate mandatory check and retains its structure default when absent.
`max_difficulty` defaults to `MAX_SKILL - 1` and `skill_limit` to `MAX_SKILL`. Runtime recipe
difficulty follows practical skill within the range, and the UI marks practice above the skill limit
as no longer increasing it.

The historical recommendations that `skill_limit <= max_difficulty + 1` and every practice takes one
hour are balance conventions, not current loader bounds. Explain exceptions and compare against
current entries for the same skill or proficiency.

### Design and validation

Use `CC_PRACTICE` and the correct subcategory for consistent navigation. Requirements should model
practice consumption; byproducts must not bypass a productive recipe. Proficiency practice also
needs prerequisites, learning time, focus, and failure or time multipliers reviewed.

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. In the crafting UI, cover locked,
below-range, in-range, above-limit, missing requirement, helper, and book cases. Add focused
`tests/crafting_gui_test.cpp` coverage and prove no result item is generated.
