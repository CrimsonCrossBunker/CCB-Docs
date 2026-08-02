## Placing and validating a new comestible

Directories and file names help maintainers find data but do not change `COMESTIBLE` loader
semantics. Identify the content domain, then place the object in the narrowest current file under
`data/json/items/comestibles/` with comparable entries. Do not copy a historical list containing
removed or renamed files.

### Current classification order

Prefer a clear domain file such as medicine, mutagen or serum, MRE, brewing, frozen, spice, protein,
alien, or netherum. Ordinary drinks split among alcohol, soup, drink, and drink_other. Solid food
uses current neighbors for baked goods, bread, casseroles, cereal, dairy, eggs, fruit, junk food,
meat or offal, mushrooms, nuts, raw produce or grain, sandwiches, seeds, vegetables, and wheat. Use
`other.json` only when no natural category exists.

Classification is not a gameplay tag. Declare fields and IDs explicitly for search, recipes, item
groups, or effects rather than relying on the path.

### Loader contract

`comestible_type` is mandatory. Explicit charges are bounded to at least one, while the absent-field
default path can be zero. Other members cover stack size, quench, fun, stimulant, health, spoilage,
calories, vitamins, addiction, cooks or eats like, cooking and smoking results, consumption EOCs, and
contamination. Take requiredness, defaults, and bounds from `islot_comestible::deserialize`.

### Validation

Choose a current comparable item and recipe and inspect nutrition, portions or charges, container,
spoilage, price, item groups, recipe results, and translations. Run formatting,
`make -j2 json-check`, and Mod `--check-mods`. Nutrition or processing changes also need focused
comestible and recipe tests for ingredients, byproducts, `cooks_like`, and `NUTRIENT_OVERRIDE`.
