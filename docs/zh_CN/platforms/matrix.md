---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.matrix
title: 平台矩阵
language: zh_CN
status: draft
doc_type: reference
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
- android/app/build.gradle
- .github/workflows/matrix.yml
- .github/workflows/msvc-full-features.yml
- .github/workflows/sdl3-matrix.yml
- .github/workflows/release.yml
- .github/actions/setup-sdl3-stack-macos/action.yml
source_symbols: []
source_queries: []
source_fingerprint: 3af89901fb085d31b24e3b4ddf1bf2bbc90275acb78acafff4d1cce77922e6e2
authority: build-config
verified_commit: 7d65b4eff3d92393e659699a312b694f0e72d2cb
verified_at: '2026-10-11'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 479d980e5f008a8893ca4c1282505d3488c96fd9c25c4412bb29beb7bb85002f
prerequisites:
- build.overview
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- android-unit
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/987
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/matrix/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/matrix/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/matrix/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/matrix/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/7d65b4eff3d92393e659699a312b694f0e72d2cb
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/CMakePresets.json
- path: android/app/build.gradle
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/android/app/build.gradle
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/matrix.yml
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/msvc-full-features.yml
- path: .github/workflows/sdl3-matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/sdl3-matrix.yml
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/release.yml
- path: .github/actions/setup-sdl3-stack-macos/action.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/actions/setup-sdl3-stack-macos/action.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.matrix%29%3A+&body=Document+ID%3A+platforms.matrix%0ALanguage%3A+zh_CN%0AVerified+commit%3A+7d65b4eff3d92393e659699a312b694f0e72d2cb%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 平台矩阵

CCB 支持多种构建环境，但验证结论只对明确的工具链与功能组合成立。Linux 构建成功
不能替代 Windows、MSVC 或 Android 的证据。

| 平台 | 维护中的入口 | 关键边界 | 最小有效证据 |
| --- | --- | --- | --- |
| Linux | Make 或 `linux-x64` CMake preset | 图形构建要求 SDL3 >= 3.4.0 | 配置/构建与聚焦测试 |
| WSL | WSL 内的 Linux 工具链 | 文件系统与图形集成不同于原生 Linux | 注明 WSL 版本和源码所在文件系统 |
| Windows MSYS2 | Windows MSYS2 CMake presets | 包名、shell 引号和 DLL 打包不同 | 在 MSYS2 中完成 preset 配置/构建 |
| Windows MSVC | vcpkg/MSVC 流程和 MSVC CI | 编译器诊断与依赖模型不同 | MSVC workflow 或等价本地构建 |
| Android | Gradle wrapper 与 native CMake | Android 使用 SDL3，产物按 ABI 区分 | Gradle 测试；APK/AAB 注明 variant 和 ABI |

不要照抄旧的 preset 名称，应先查看当前仓库：

```sh
# validation: cmake-configure
cmake --list-presets
```

## 功能组合

Tiles、sound、本地化、tests、Lua Platform v1、编译器和构建类型都是平台身份的一部分，
PR 中必须记录。所有图形路径统一使用 SDL3，常规 Linux/macOS 矩阵和 MSVC 工作流
直接验证此后端，不需要可选仓库变量。Release 保留十个安装包：Windows 2、Linux 3、
macOS 2、Android 3。手动 matrix/MSVC 的 `package_artifacts=true` 可验证并上传安装包，
不会发布 Release；`run_tests` 单独控制宽范围原生测试。

## 本页没有声称什么

本页记录 verified commit 中 Make、CMake presets、Gradle 与 CI 提供的入口，不声称
文档构建期间真实跑过每个矩阵单元。发布维护者必须以发布 commit 的默认分支检查和
产物为准。

具体命令见[构建 CCB](../build/overview.md)，风险扩展规则见
[测试策略](../validation/testing.md)。
