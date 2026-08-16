---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.core-dev-guide
title: Core Development and Contribution Guide
language: en
status: active
doc_type: how-to
audiences:
- mod-author
- api-user
- experienced-contributor
- maintainer
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- Lua Mod API v5
source_queries: []
source_fingerprint: 30a19e6cbd8c6709ac5ccda80fe349e9459ddaccd8d3dc96507ee282c17f48cb
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a6563eb431fef0176e8dad8ce9e00d2f2018f8c070517edc149ed3553fdd44cf
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes:
- lua.v5.overview
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/core-dev-guide/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/core-dev-guide/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/contributing/core-dev-guide/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/core-dev-guide/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.core-dev-guide%29%3A+&body=Document+ID%3A+contributing.core-dev-guide%0ALanguage%3A+en%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# Core Development & Contribution Guide

This guide describes the complete development lifecycle for contributors writing C++ engine code, fixing bugs, or implementing core mechanics for **Cataclysm: Cleanwater Bomb (CCB)**.

---

## 1. Environment Setup

### 🐧 Linux (Ubuntu / Debian / Arch)
```bash
# Ubuntu / Debian
sudo apt-get update
sudo apt-get install -y build-essential cmake pkg-config astyle \
    libsdl2-dev libsdl2-image-dev libsdl2-ttf-dev libsdl2-mixer-dev \
    libncursesw5-dev liblua5.4-dev libgettextpo-dev

# Arch Linux
sudo pacman -S base-devel cmake astyle sdl2 sdl2_image sdl2_ttf sdl2_mixer ncurses lua gettext
```

### 🪟 Windows (MSVC / Visual Studio 2022)
1. Install **Visual Studio 2022** with "Desktop development with C++" and "C++ CMake tools".
2. Install dependencies via `vcpkg`:
   ```cmd
   vcpkg install sdl2 sdl2-image sdl2-ttf sdl2-mixer gettext lua
   ```
3. Open the project root in VS2022 and select the `x64-Release` or `x64-Debug` CMake preset.

### 🤖 Android (Gradle & NDK)
```bash
cd android/
./gradlew assembleDebug
```

---

## 2. CMake Build Workflows

```bash
# 1. Configure build directory (Tiles & Sound enabled)
cmake -B build -DCMAKE_BUILD_TYPE=Release -DTILES=ON -DSOUND=ON

# 2. Parallel compilation
cmake --build build -j$(nproc)

# 3. Launch game
./build/cataclysm-tiles

# 4. Build and run unit tests
cmake --build build --target cata_test -j$(nproc)
./build/tests/cata_test
```

---

## 3. C++20 Standards & Astyle Formatting

1. **Memory Safety**: Prefer `std::unique_ptr`, `std::shared_ptr`, `std::optional`, and `game_handle` over raw pointers.
2. **Modern Syntax**: Leverage structured bindings (`auto [k, v]`), `constexpr`, and `<ranges>`.
3. **Astyle Formatting**:
   ```bash
   make astyle        # Auto-format modified sources
   make astyle-check  # Verify compliance (CI gate)
   ```

---

## 4. Writing Catch2 Unit Tests

```cpp
TEST_CASE( "weather_forecast_storm_intensity", "[weather]" ) {
    tripoint test_pos( 60, 60, 0 );
    weather_forecast forecast = weather_manager::forecast_at( test_pos, 2 );
    
    CHECK( forecast.wind_speed >= 0.0f );
    CHECK( forecast.wind_speed <= 300.0f );
}
```

Run specific test tags:
```bash
./build/tests/cata_test "[weather]"
```

---

## 5. Debugging & AddressSanitizer

### AddressSanitizer Build:
```bash
cmake -B build-asan -DCMAKE_BUILD_TYPE=Debug -DENABLE_ASAN=ON
cmake --build build-asan -j$(nproc)
```

---

## 6. Git Workflow & PR Submission

1. Branch from `master` (`git checkout -b feat/my-feature`).
2. Adhere to **Atomic Commits** with conventional commit messages (`feat(map): ...`, `fix(water): ...`).
3. Run local checks:
   ```bash
   make astyle-check
   ./build/tests/cata_test
   python3 tools/agent/check_project_metadata.py
   ```
4. Open Pull Request on GitHub naming the **Responsible human**.
