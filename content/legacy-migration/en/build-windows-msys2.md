## Current MSYS2 route

The legacy guide still points at a CleverRaven clone, old Windows releases, and a frozen
pacman package line. CCB contributors work from a CCB fork and treat current MSYS2,
Make/CMake configuration, and Windows CI as authoritative.

### Select a shell and toolchain

On a modern Windows installation, use the 64-bit MinGW or UCRT shell matching the installed
package prefix. Do not mix the plain MSYS shell, MINGW64, and UCRT64 toolchains. Fully update
MSYS2 first, then install dependencies based on the current Makefile/CMake configuration,
the first missing-header error, and CI. Do not preserve version numbers copied from this page.

### CMake preset

The pinned source provides:

```sh
cmake --list-presets
cmake --preset windows-x64
cmake --build --preset windows-x64
```

Use `windows-tiles-sounds-x64` for the Tiles and sound combination. These presets use
Ninja Multi-Config and write to `out/build/<preset>/`; current preset data defines the
configuration and install paths.

### Make entry point

The Makefile still supports `MSYS2=1` and `DYNAMIC_LINKING=1`, with dependencies selected
by Tiles, sound, localization, SDL2/SDL3, and other switches. Do not reuse the old guide's
large command that disables lint and tests as the default validation. Build the target,
then select formatting, JSON, or focused tests from `ai/test-matrix.yml`.

### Runtime and review evidence

- Run the artifact from the same MSYS2 environment and confirm that runtime DLLs resolve.
- Record shell type, compiler, CMake or Make, package prefix, and the complete command.
- Windows CI is merge evidence; Linux or WSL does not replace a native Windows result.
- Release and packaging workflows create distributable artifacts. A local developer build
  is not an official package.

MSYS2 package names and tool versions change, so this page intentionally does not freeze a
complete installation command. Resolve differences through current CI and the official
MSYS2 package database.
