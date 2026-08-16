---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: contributing.core-dev-guide
title: 游戏本体核心开发与贡献指南
language: zh_CN
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/contributing/core-dev-guide/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28contributing.core-dev-guide%29%3A+&body=Document+ID%3A+contributing.core-dev-guide%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 游戏本体核心开发与贡献指南 (Core Development & Contribution Guide)

本指南面向所有希望为 **Cataclysm: Cleanwater Bomb (CCB)** 贡献 C++ 引擎代码、修复 Bug 或新增核心机制的开发者，提供从环境配置、编译构建、代码规范、测试调试到 PR 提交的全流程标准实践。

---

## 1. 全平台开发环境搭建 (Environment Setup)

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
1. 安装 **Visual Studio 2022**（勾选“使用 C++ 的桌面开发”与“C++ CMake 工具”）。
2. 使用 `vcpkg` 安装依赖库：
   ```cmd
   vcpkg install sdl2 sdl2-image sdl2-ttf sdl2-mixer gettext lua
   ```
3. 在 VS2022 中直接“打开文件夹”选择项目根目录，选择 `x64-Release` 或 `x64-Debug` 预设即可一键编译。

### 🤖 Android (Gradle & NDK)
1. 安装 **Android Studio** 与 **NDK 25+**。
2. 进入 `android/` 目录：
   ```bash
   ./gradlew assembleDebug
   ```

---

## 2. 现代 CMake 与 Make 构建指令 (Build Workflows)

推荐使用 **CMake 现代构建系统**：

```bash
# 1. 配置构建目录 (启用 SDL2 图形界面与音效)
cmake -B build -DCMAKE_BUILD_TYPE=Release -DTILES=ON -DSOUND=ON

# 2. 多核并发极速编译
cmake --build build -j$(nproc)

# 3. 运行游戏
./build/cataclysm-tiles

# 4. 编译并运行自动化单元测试
cmake --build build --target cata_test -j$(nproc)
./build/tests/cata_test
```

---

## 3. C++20 代码规范与 Astyle 自动格式化

CCB 项目全面采用 **现代 C++20 标准**，要求保持极高的代码整洁度与健壮性：

### 核心编码规范
1. **内存与指针安全**：
   - 杜绝野指针和裸 `new`/`delete`，优先使用 `std::unique_ptr`、`std::shared_ptr`、`std::optional` 或引擎句柄 `game_handle`。
   - 引用传递优于指针传递；只读数据强制使用 `const&`。
2. **现代语法特性**：
   - 合理使用 `auto`、结构化绑定（`auto [k, v] = ...`）、`constexpr` 与 `<ranges>` 算法库。
3. **Astyle 代码自动格式化**：
   在提交代码前，必须执行项目自带的格式化检查：
   ```bash
   # 自动格式化所有被修改的 C++ 源码
   make astyle
   # 验证格式合规性 (CI 门禁要求)
   make astyle-check
   ```

---

## 4. 编写与运行 Catch2 单元测试

为确保改动不引入潜在回归，任何核心子系统的逻辑修改必须附带 Catch2 单元测试：

```cpp
// tests/weather_test.cpp
#include "catch/catch.hpp"
#include "weather.h"

TEST_CASE( "weather_forecast_storm_intensity", "[weather]" ) {
    GIVEN( "a stormy weather pattern" ) {
        tripoint test_pos( 60, 60, 0 );
        
        WHEN( "querying 2 hours ahead forecast" ) {
            weather_forecast forecast = weather_manager::forecast_at( test_pos, 2 );
            
            THEN( "wind speed must remain within safe physical boundaries" ) {
                CHECK( forecast.wind_speed >= 0.0f );
                CHECK( forecast.wind_speed <= 300.0f );
            }
        }
    }
}
```

运行单个测试用例：
```bash
./build/tests/cata_test "[weather]"
```

---

## 5. 本地调试与内存检测 (Debugging & ASan)

### 1. VSCode Launch 调试配置
在 `.vscode/launch.json` 中配置 GDB 调试：
```json
{
    "name": "(gdb) Launch Game",
    "type": "cppdbg",
    "request": "launch",
    "program": "${workspaceFolder}/build/cataclysm-tiles",
    "args": ["--debug"],
    "cwd": "${workspaceFolder}",
    "MIMode": "gdb",
    "setupCommands": [{ "text": "-enable-pretty-printing" }]
}
```

### 2. 启用 AddressSanitizer 内存泄露排查
```bash
cmake -B build-asan -DCMAKE_BUILD_TYPE=Debug -DENABLE_ASAN=ON
cmake --build build-asan -j$(nproc)
```

---

## 6. Git 工作流与 Pull Request 提交流程

1. **从 `master` 创建特性分支**：
   ```bash
   git checkout -b fix/finite-water-gradient
   ```
2. **遵循原子提交（Atomic Commits）**：
   - 每次提交聚焦于单一明确的改进，Commit 信息遵循约定式提交（如 `fix(water): correct gradient calculation`、`feat(lua): expose weather radar API`）。
3. **本地完整运行验证**：
   ```bash
   make astyle-check
   ./build/tests/cata_test
   python3 tools/agent/check_project_metadata.py
   ```
4. **提交 Pull Request**：
   - 明确标注 **Responsible human**（指明你的 GitHub 账号作为代码责任人）。
   - 如改动影响 Lua 契约或文档，需在 PR 中勾选并说明 Documentation Impact。
