## Basecamp data spans several contracts

A basecamp upgrade is not one object type. It combines blueprint recipes, `update_mapgen`,
`recipe_group`, overmap terrain, and runtime camp state. Before changing one file, trace the complete
ID chain through `basecamp::available_upgrades`, `recipe::load`, and current first-party camp data.

### Blueprint recipes

An ordinary recipe with `construction_blueprint` enters the blueprint path. Its loader reads
`blueprint_name`, `blueprint_parameter_names`, resources, provides, requires, excludes, and needs.
Every blueprint automatically provides and excludes its own result, making it non-repeatable by
default.

`blueprint_provides`, `blueprint_requires`, and `blueprint_excludes` are camp-feature counters whose
amount defaults to one; they are not a global feature registry. Code assigns mission or camp meaning
to selected conventional IDs. A new string has meaning only when a consumer reads it, so the keyword
table in historical prose is not an authoritative complete list.

### Requirements and mapgen

When `blueprint_needs` is absent and `check_blueprint_needs` is true, finalization calculates needs
from mapgen. A parameterized blueprint cannot also rely on explicit needs. `construction_blueprint`
must name an executable update mapgen, and parameter names must cover and translate every choice
shown to the player.

Initial camps and expansions also depend on recipe-group terrain matching, a corresponding OMT, and
mapgen. A Mod must declare dependencies before safely referring to another Mod's recipe, terrain, or
mapgen IDs.

### Validation checklist

Exercise every requires, provides, and excludes branch, repeat prevention, resource items, mapgen
parameters, and the resulting upgraded map. Run formatting, `make -j2 json-check`, complete
`--check-mods`, and a focused `tests/faction_camp_test.cpp` case. Use the repository's
`tools/update_blueprint_needs.py` for calculated requirements and review every result instead of
copying historical examples.
