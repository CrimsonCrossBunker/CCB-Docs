## Current CCB EOC model

An Effect on Condition (EOC) combines dialogue conditions and effects so they can be invoked
outside dialogue. It is not an `effect_type` status applied to a creature; the similar names
hide different loaders, lifecycles, and purposes. The complete current key lists are generated
from source registrations in the [condition index](../eoc-conditions.md) and
[effect index](../eoc-effects.md). Do not copy a legacy list and call it complete.

### Minimal activation EOC

```jsonc
{
  "type": "effect_on_condition",
  "id": "EOC_CCB_EXAMPLE",
  "eoc_type": "ACTIVATION",
  "condition": { "u_has_trait": "DEBUG_PREVENT_DEATH" },
  "effect": { "u_message": "The example EOC ran." },
  "false_effect": { "u_message": "The condition did not pass." }
}
```

The `id` is a stable reference used by other JSON, events, and EOCs. A field can reference a
named ID or, where its loader accepts one, contain an inline EOC. The loader records named
references and consistency checking reports missing IDs.

### Types, triggers, and scheduling

The current `effect_on_condition::load` reads `eoc_type`. With no recurrence, an unspecified
type defaults to `ACTIVATION`. Supplying `recurrence` forces `RECURRING` and conflicts with
another explicit type. An `EVENT` must provide `required_event`. Death and death-prevention
types get talkers and stopping behavior from their call sites, not from the EOC alone.

A recurring EOC can use `condition`, `false_effect`, and `deactivate_condition`. `global`
selects global or per-character queues. `run_for_npcs` is valid only with `global: true`.
Frequent recurrences and effects that traverse NPCs or map data have real performance cost;
measure them.

### Conditions, effects, and Boolean composition

A condition can be a simple string or an object. `and` and `or` take condition arrays; `not`
contains one string or condition object. An unrecognized complex condition is a load error.
An effect can be one entry or an ordered array and can compose flow with `if`, `then`, `else`,
other EOCs, and context variables.

The generated indexes record each condition or effect's parameters, defaults, talker types,
and source. An entry's existence does not prove that the current call site supplies a compatible
alpha or beta talker, so examples still need contextual tests.

### Alpha, beta, and context

EOCs reuse dialogue naming: `u_` normally addresses the alpha talker and `npc_` the beta, but
an actual talker may be a character, monster, item, furniture, or absent. Event, death, and
ammunition-effect call sites can omit one side. Guard access with `has_alpha` or `has_beta`.

Variable scopes include the character side, beta side, world-global storage, and this invocation's
context. A `context_val` exists only when the caller supplies that key; event values must match
the current event payload. Do not treat context as persistent save state or assume that a
requeued EOC retains the same context.

### Validation

1. Use the generated condition and effect indexes for keys, parameters, and source locations.
2. Inspect the calling field for actual alpha, beta, context, and lifecycle behavior.
3. Run the JSON loader, EOC registry or parser checks, and `--check-mods` for the real Mod set.
4. Cover true and false conditions, missing talkers, missing variables, and repeated execution.
5. For recurring or event EOCs, test frequency, queues, save reload, and performance.

See the [EOC overview](../../eoc/overview.md) and
[complete JSON/EOC example Mod](../../mods/complete-json-eoc-mod.md) for integrated structure.
