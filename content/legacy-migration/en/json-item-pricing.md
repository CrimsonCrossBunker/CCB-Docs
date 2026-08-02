## Item prices and trade rules

`price` is the old-world or baseline price and `price_postapoc` is the post-Cataclysm trade baseline;
both use non-negative money units. An NPC quote is not a direct display of either value. Item count,
charges or stack size, contents, trade direction, NPC adjustments, faction or personal price rules,
and currency can all change it.

### Faction rules

A faction `price_rules` entry uses item, group, and related matchers and may set `markup`, `premium`,
`fixed_adj`, or a fixed `price`. The consumer searches from the end and uses the first matching rule.
An NPC personal rule can override the faction rule. Declaring `currency` also adds an equivalent rule
for that currency.

Historical currency anchors, fixed price bands, and a “no item above this limit” statement are balance
advice, not loader or trade-code constraints. Price against current CCB faction data, comparable
items, and the real trade UI, and explain availability, utility, consumption rate, replaceability,
and the target faction.

### Charges and contents

For count-by-charges items, fixed rule prices and base item prices account for stack size or charges.
Loaded magazines, ammo, and container contents may also contribute. Do not treat a whole-stack JSON
price as one charge or compensate for the same factor in item, group, and faction rules.

### Validation

Run formatting, `make -j2 json-check`, and Mod `--check-mods`. A new rule needs NPC-buying and
NPC-selling cases, currency, conditional matching, personal override, charged stacks, and contents in
`tests/faction_price_rules_test.cpp`. A Responsible human reviews balance; tests prove only that the
calculation follows the contract.
