## Conditional Mod compatibility data

`mod_interactions/` lets one Mod load a patch only when one named target Mod is active. It fits
cross-Mod references, compatibility EOCs, combined recipes, or targeted overrides. It is not a
normal dependency: the base Mod should still load independently when the interaction is absent.

### Directory contract

Suppose the current Mod ID is `xedra_evolved` and compatibility is needed only when
`mindovermatter` is active:

```text
Xedra_Evolved/
├── modinfo.json
├── ordinary-content.json
└── mod_interactions/
    └── mindovermatter/
        └── mom-compat-data.json
```

The directory name must match the target Mod ID exactly, including case. Ordinary loading
recursively excludes all of `mod_interactions`; after every active Mod's ordinary data loads, the
loader processes interaction directories in active-Mod order. The current implementation checks
one target-ID directory level and does not express “both Mods active” with `a/b/` nesting.

### Source and override boundaries

Interaction definitions receive the source `base_mod#target_mod`, for example
`xedra_evolved#mindovermatter`. `#` is therefore reserved for combined provenance and is forbidden
in an ordinary Mod ID. Preserve this combined source in diagnostics and object provenance.

Late loading permits only overrides or extensions supported by the owning loader. Do not assume
every object type has identical merge semantics. Inspect the factory or loader for `copy-from`,
`extend`, duplicate IDs, deletion, and obsoletion. Loading later also cannot repair a reference that
an earlier phase must resolve before finalization.

### More than one condition

Do not build nested directories when content needs both A and B. One interaction may load a
compatibility EOC that checks another supported registry condition, or a dedicated compatibility
Mod may declare both `dependencies`. Choose based on whether partial combinations should remain
usable and which package owns the published IDs.

### Validation matrix

Test at least the base Mod alone, the target alone, both together after dependency ordering, and an
old save containing related IDs. Run formatting, `make -j2 json-check`, and `--check-mods` for each
combination. Check duplicate IDs, source diagnostics, EOC talkers and context, save/reload, and
removal of either Mod.

Testing only the combined case misses interaction data leaking into ordinary loading or a base file
that accidentally references the target.
