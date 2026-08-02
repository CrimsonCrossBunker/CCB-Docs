## Proficiencies, categories, and migrations

A proficiency is knowledge tracked separately from skills. Recipes and activities decide when it is
learned or consumed; the JSON definition supplies identity, prerequisites, default penalties,
learning properties, and consumer-specific bonuses. Dependencies form a general directed graph, not
necessarily a tree.

### Three object types

A `proficiency` requires name, description, can_learn, and category. Optional fields include
teachable (default true), time_to_learn, required_proficiencies, ignore_focus, default time, skill,
and weakpoint modifiers, and bonuses. Legacy `default_fail_multiplier` is converted with a warning;
new data uses `default_skill_penalty`.

A `proficiency_category` requires name and description; its factory owns the ID. A
`proficiency_migration` requires from and optionally has to. Missing to removes the old proficiency;
present to must reference a valid ID. Migration is part of save compatibility when a public ID is
deleted or renamed.

### Bonuses and consumers

A bonus entry requires type and value, but a bonus key gains meaning only from a particular activity
or attack consumer. Successful JSON parsing does not prove code consumes it. A new key or type needs
consumer implementation, documentation, and tests. Recipes can override default time, skill,
learning, and maximum experience, so inspect expanded recipes.

### Validation

Check categories, every prerequisite, cycles or unreachable nodes, learnable and teachable states,
migrations, and referencing recipes, books, and activities. Run formatting, `make -j2 json-check`,
Mod `--check-mods`, and focused crafting, learning, and save-migration tests for missing, partial,
known, and old-ID states. The generated proficiency index aids discovery but does not replace loader
and consumer review.
