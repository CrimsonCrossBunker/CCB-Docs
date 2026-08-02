## Current CMake route

The repository's `CMakePresets.json` is authoritative for preset names, generators,
output directories, and default feature combinations. The old statements that CMake is
unofficial, that SDL DLLs should be downloaded manually, and that an in-tree `build/`
directory is acceptable are obsolete. CCB CI uses CMake, while builds remain out of tree.

### Discover and configure

Start at the repository root:

```sh
cmake --list-presets
cmake --preset linux-x64
```

The pinned source defines `linux-x64`, `linux-tiles-sounds-x64`, and Windows MSYS2 and
MSVC presets. Output defaults to `out/build/<preset>/`. If the local list is empty or a
target preset is absent, inspect platform conditions, the generator, and the toolchain
instead of combining commands from the legacy guide.

### Build and override options

```sh
cmake --build --preset linux-x64
```

Use `-DNAME=VALUE` for a temporary override only after confirming that `CMakeLists.txt`
still defines the option. Tiles, sound, localization, Lua, SDL2/SDL3, and sanitizers alter
dependencies and artifacts, so record the preset and every override. Do not commit local
`CMakeUserPresets.json`, absolute paths, vcpkg roots, or generated build trees.

### Validate and diagnose

1. Preserve the first configure error, not only the final build failure.
2. Record CMake, compiler, Ninja or MSBuild, and dependency versions.
3. Remove only the explicit `out/build/<preset>/` directory when a clean configure is
   necessary; never clean the source tree or untracked user files.
4. Configure again and build the affected target. Run the focused test from the preset's
   output when tests are affected.

`cmake --list-presets` was actually checked on Linux for this documentation stack.
Windows preset availability and compilation are evidenced by the Windows CI jobs; a Linux
result does not replace them. See [building CCB](overview.md) and the
[platform matrix](../platforms/matrix.md).
