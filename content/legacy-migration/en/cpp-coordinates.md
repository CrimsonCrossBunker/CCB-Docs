## Current CCB coordinate types

CCB types encode dimension, origin, and horizontal scale together so a reality-bubble tile cannot
silently become an absolute world OMT. Aliases use
`(tri)point_<origin>_<scale>[_ib]` and are defined by `coords_fwd.h` and `coordinates.h`.

### Origins, scales, and axes

- `rel` is an offset and `abs` uses the fixed world origin.
- `sm`, `omt`, and `om` are relative to a submap, overmap terrain, or overmap corner.
- `bub` is relative to the current reality bubble and changes as map coverage moves.
- `ms`, `sm`, `omt`, `seg`, and `om` are horizontal units from map square to overmap.
- `point` is 2D, `tripoint` includes z, and `_ib` guarantees bounds for the relevant local origin.

x points right, y points down, and positive z points up. Horizontal scale conversion does not scale
z. Current `SEEX/SEEY`, `OMAPX/OMAPY`, and related source constants are authoritative; do not freeze
legacy numeric values as a permanent contract.

### Selection and conversion

Prefer typed points such as `tripoint_abs_ms`, `tripoint_bub_ms`, and `point_abs_omt` in new code.
Use raw `point` or `tripoint` only for mathematics with no game coordinate system. Function
signatures should expose required origin and scale so misuse fails at compile time.

```cpp
tripoint_abs_ms absolute = get_map().getglobal( local );
tripoint_bub_ms local_again = get_map().bub_from_abs( absolute );
point_abs_omt omt = project_to<coords::omt>( absolute.xy() );
```

Use `project_to` to change scale while retaining origin, `project_remain` when a coarse projection
also needs its remainder, and `project_combine` to reconstruct it. Absolute/bubble conversion needs
a specific `map`. Vehicle mount and rotated coordinates use
`vehicle::coord_translate` or `mount_to_tripoint` families, not hand-written rotation offsets.

### Operations and sentinels

Only meaningful type combinations support arithmetic: an absolute position plus a relative offset
is meaningful; two absolute positions added together are not. Select `square_dist`, `trig_dist`,
`rl_dist`, or `manhattan_dist` deliberately. `zero` is an origin; `invalid` and `is_invalid()` are
failure sentinels. Do not use zero to mean unset.

A saved field must serialize coordinates that remain meaningful after reality-bubble movement. NPC
or interruptible-activity targets normally store absolute coordinates rather than avatar-relative
bubble coordinates.

### Validation

Compile affected translation units and run relevant `point_test` and `coordinate_test` filters.
Cover negative coordinates, submap and OMT boundaries, z-levels, map shifts, vehicle rotation, and
serialization round trips. Clang-tidy point checks assist migration but do not replace boundary
tests.
