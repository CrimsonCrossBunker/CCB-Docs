## Executable evidence defines support

Compiler support is not a permanent version table. At the pinned CCB commit, `CMakeLists.txt`
requires C++17. Actual support comes from default-branch CI, build scripts, and release toolchains
maintainers can reproduce. Distribution, Xcode market-share, and external links in the legacy page
age quickly and cannot override current workflows.

At the source commit verified by this page, the General build matrix covers:

- a basic clang 13 curses build and test on Ubuntu;
- clang 18 with tiles and ASan on Ubuntu;
- GCC 9 curses/LTO and tiles, sound, CMake, and UBSan combinations on Ubuntu;
- GCC 14 curses and Lua API on Ubuntu;
- macOS 15 and Apple Clang 17 with tiles, sound, and SDL2;
- an Android arm64 build-only job; and
- a separate Windows workflow on windows-2022 using MSVC, pinned CMake and vcpkg, and full tests.

These describe CI at that commit. They do not promise arbitrary older or newer toolchains, and a
build-only target has not thereby run tests.

## Change and validation

Choose the nearest platform CMake preset, Make or Gradle route, or MSVC entry point and record OS,
architecture, compiler, standard library, generator, SDL, tiles, sound, localization, Lua,
sanitizer, and build type. Linux success does not replace Windows, macOS, or Android evidence. A
cross-build does not prove launch, dependency packaging, or input on the target.

Before raising a minimum or using a new library feature, update the matrix so the oldest and newest
supported toolchains compile it, then update prose. Inspect release packaging, third-party
dependencies, and cache keys, and make a check required only after stable default-branch success.
External links help locate tools but are not support promises; repository jobs and configuration
are the evidence.
