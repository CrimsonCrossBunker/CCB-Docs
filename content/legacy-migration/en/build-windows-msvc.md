## Current MSVC and vcpkg route

CCB's full MSVC route is jointly defined by the `msvc-full-features/` solution, vcpkg
manifest and triplets, CMake presets, and `.github/workflows/msvc-full-features.yml`.
The legacy CleverRaven clone, an arbitrary latest vcpkg, and old Visual Studio versions do
not override those pinned contracts.

### Recommended entry points

Install Visual Studio 2022 with the C++ desktop and game workloads, Git, and project-
compatible CMake and vcpkg versions. At the pinned source, CI uses CMake 3.31.6 and vcpkg
revision `f6672d8e480ccdecddfad3fd1b838ba369ffe6cd`; record any local version difference.

Choose either route:

1. open `msvc-full-features/Cataclysm-vcpkg-static.sln` with `Release` and `x64`; or
2. use the `windows-x64-msvc` or `windows-tiles-sounds-x64-msvc` CMake preset.

The central CI solution command is:

```powershell
msbuild -m -p:Configuration=Release -p:Platform=x64 -p:UseSDL3=false `
  "-target:Cataclysm-vcpkg-static;Cataclysm-test-vcpkg-static;JsonFormatter-vcpkg-static;zzip" `
  msvc-full-features/Cataclysm-vcpkg-static.sln
```

That command is CI evidence; this page does not claim it was rerun on a local Windows host.

### Test and run

- Build the test target with the same configuration and platform as the game.
- Run a focused Catch2 filter from the output directory. Release is generally practical for
  routine validation; reserve Debug for iterator diagnostics or source-level stepping.
- Localization, Tiles, sound, SDL2/SDL3, and static linking alter targets and dependencies;
  state the combination in the PR.
- On a vcpkg failure, preserve the relevant buildtree log and pinned revision before trying
  a different version. Do not silently update to arbitrary HEAD.

Signing and distribution are outside this page; see [release maintenance](../maintenance/releases.md).
