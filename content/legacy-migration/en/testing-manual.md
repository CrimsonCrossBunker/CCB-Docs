## Evidence-based manual playtesting

Automated checks prove formatting, loading, and encoded invariants. A non-trivial gameplay, UI, or
content change also needs manual validation in a CCB binary matching the source commit. State the
observable risks first and build the smallest scenarios; a few minutes of unguided play is not
evidence that a change was tested.

### Preparation and records

- Use a dedicated test world and character. Record commit, build flags, platform, mod set, seed,
  options, and save origin.
- Format and load JSON first. Compile the affected C++ target and run the focused test before play.
- Ensure binary and data come from the same commit. Restart or reload according to the actual loader
  lifecycle; returning to the main menu does not refresh every registry.
- Preserve reproduction steps, expected and actual results, logs, screenshots or short video, and
  cover normal, failure, and important boundary paths.

The debug menu can spawn items or monsters, edit map/overmap data, advance time, teleport, or call
subsystem entry points, but debug spawning can skip part of natural-generation context. Test a
monster-definition change on newly spawned instances. Growth, evolution, and offscreen processing
need unload/reload and time advancement. Test mapgen on fresh OMTs with direction, z-level, and region
coverage. EOC, Lua, save migration, and multiplayer need their real entry paths.

Remove debug-only state afterward and do not commit test saves, logs, or generated artifacts. A PR
must separate locally executed checks, CI coverage, and work not run. One successful manual run does
not replace a deterministic regression test; a bug fix still needs the narrowest automated case
that failed on the old implementation.
