---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: build.overview
title: 构建 CCB
language: zh_CN
status: active
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- Makefile
- CMakePresets.json
- android/gradlew
- android/build.gradle
- .github/workflows/matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: d1a51672bd4739e5b0051c192091e672288cdc557e3919d08b04fb44b05c952f
authority: build-config
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 2a5adc64a79b2cb017b29f11abb46a6685a76fc1949b56ccc9616d1b25e9eda8
prerequisites:
- architecture.project-map
depends_on:
- platforms.matrix
- validation.quickstart
redirect_from: []
supersedes:
- build-overview
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- cpp-format
- cpp-tests
- json-load
- android-unit
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: build
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/build/overview/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/build/overview/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/build/overview/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/build/overview/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/CMakePresets.json
- path: android/gradlew
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/android/gradlew
- path: android/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/android/build.gradle
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/.github/workflows/matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28build.overview%29%3A+&body=Document+ID%3A+build.overview%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 构建 CCB

构建行为由当前仓库的 Makefile、CMake、Gradle 与 CI 定义。本页解释入口和选择
方式；复制命令前仍应检查对应文件，因为依赖版本和 feature flag 会变化。

## 选择构建系统

| 场景 | 首选入口 | 说明 |
| --- | --- | --- |
| Linux 快速开发 | `make` | 与大量格式、JSON、测试目标共用同一入口 |
| 跨平台/IDE/clangd | CMake preset | `cmake --list-presets` 查看仓库当前 preset |
| Windows MSYS2 | Windows CMake preset 或维护中的 MSYS2 流程 | 在目标 shell 验证，不把 Linux 结果当成 Windows 结果 |
| MSVC | vcpkg/MSVC 文档与 CI | 编译器、依赖和警告差异必须由 MSVC 检查覆盖 |
| Android | `android/gradlew` | 需要 Android SDK/NDK；签名与发布凭据不进仓库 |

本次文档核验在 Linux、源码 commit
`2c899a3db790e11a6ff44d91f319064b1ee65d2a` 上实际运行了：

```sh
# validation: cmake-configure
cmake --list-presets
```

输出包含 `linux-x64`、tiles/sounds Linux preset，以及 Windows MSYS2 preset。
这只验证 preset 可发现性，不代表已完成编译。

## 常用入口

```sh
# validation: cpp-format
make astyle-check

# validation: cpp-tests
make -j2 tests
./tests/cata_test "<focused filter>"

# validation: json-load
make -j2 json-check

# validation: cmake-configure
cmake --preset linux-x64
```

Android 在 `android/` 目录运行：

```sh
# validation: android-unit
./gradlew test
./gradlew assembleDebug
```

这些是权威构建入口中的命令示例。执行者必须记录实际平台、依赖、结果及跳过项；
本站构建并没有替代 Windows、MSVC 或 Android 的真实平台验证。

## 关键配置边界

- `CATA_ENABLE_LUA_UI` 在 CCB 的 Make、CMake 和 Android 配置中默认启用。
- Android 使用 SDL3；desktop 一般使用 SDL2，SDL3 CI 受
  `CCB_DESKTOP_SDL3_ENABLED` 门控。不要从一个平台推断另一平台。
- Tiles、sound、localization 与 Lua 会改变依赖或制品；PR 应说明使用的组合。
- CMake 必须 out-of-tree；大型索引、Doxygen HTML、ctags 与编译数据库只作为
  本地/CI artifact，不提交仓库。

## 构建失败的定位顺序

1. 保存完整命令、首个失败目标和编译器/Gradle 版本。
2. 判断是配置、下载/依赖、编译、链接、资源复制还是测试失败。
3. 与 CI 中相同平台和 feature 组合比较，而不是只比较最后一行错误。
4. 清理仅限明确的构建目录；不要删除工作树或未跟踪用户文件。
5. 修复后重跑失败目标，再运行受影响子系统的验证。

更细的选择见[平台矩阵](../platforms/matrix.md)与
[验证快速入门](../validation/quickstart.md)。
