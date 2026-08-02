## Nested, merged, and update mapgen

A full variant shares an `om_terrain` ID and replaces the whole map according to weight. Nested
mapgen overlays a local chunk inside a caller. Update mapgen changes an already existing map during
play. Their lifecycles differ, so similar JSON shapes do not make them interchangeable.

### Nested mapgen

The top level uses `nested_mapgen_id` and may provide weighted variants under one ID.
`object.mapgensize` must contain two identical positive numbers; the current implementation still
supports square nests only. Rows, palettes, placements, and nested calls operate in this local
coordinate system. Blank symbols normally preserve the underlying map. Use current null/clear
values or clearing flags when terrain, furniture, items, traps, and fields must be removed rather
than leaving half of the old state.

A caller selects weighted `chunks` through a `nested` symbol or `place_nested` coordinates; `null`
is the valid no-placement candidate. Current nested placement can also test neighbors, joins,
flags, predecessors, and z-level. `jmapgen_nested` and `nest_conditional_placement_test.cpp` define
that behavior. Keep the chunk inside the caller grid and make doors, walls, and traversable edges
consistent across every variant.

### Merged and update mapgen

A two-dimensional `om_terrain` array registers one merged definition at an offset for each OMT; rows
use continuous total coordinates. `common_check_bounds` rejects a coordinate range that crosses its
current grid boundary, so large rows do not mean every placement may span OMTs. Keep vehicles,
range-based spawns, and nests inside one OMT and cover boundaries with focused tests.

`update_mapgen_id` registers a runtime update. Its call site chooses target OMT, parameters,
mirroring/rotation, collision policy, and mission context. An update can collide with player
construction, vehicles, items, and saved state, so document idempotence, conflicts, and repeat
triggering. Do not infer all current trigger paths from an old trap example.

Validate nest weights and conditions, rotation, local clearing, NPCs and vehicles, merged
boundaries, update collision, repeat execution, and save reload. Run JSON and target-mod loading,
focused mapgen/nest/update tests, and debug generation while recording seed, position, direction,
and call parameters.
