## JSON loading phases and order

CCB calls loaders for active Mods in dependency order already resolved for the world. Within one
path, `get_files_from_path(..., recursive=true)` discovers JSON breadth-first and uses current
filesystem sorting within a directory. Ordinary Mod loading excludes `mod_interactions`; matching
interaction content is a later pass after all ordinary content.

### Safe dependencies

Rely on explicit Mod dependencies, documented generic-factory deferred loading, and finalization
owned by a loader. Do not treat file names or directory depth as a universal forward-reference API.
Some handlers require targets during parsing while others retain string IDs until consistency
checking. Inspect the specific handler.

Historical `data/json` layout used depth for relationships such as skills, professions, and
scenarios. New code should prefer explicit factory or loader handling. Moving a file into a
subdirectory can change parse order and break content relying on accidental ordering; treat it as a
high-risk JSON change.

### Mods and interactions

`dependencies` determines active-Mod order. Ordinary content must parse after declared dependencies.
`mod_interactions/<target-id>/` loads in the later pass with source `base#target`. It cannot repair
an earlier ordinary-file exception and does not support nested multi-target directories.

### Validation

Run formatting, `make -j2 json-check`, and `--check-mods` for the complete dependency combination.
For order-sensitive changes, add a minimal fixture covering parent and child order, missing
dependencies, two-Mod overrides, interactions, and finalization. Also exercise packaged path and
case behavior through target-platform CI rather than only a development checkout.
