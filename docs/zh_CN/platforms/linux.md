---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.linux
title: Linux 开发
language: zh_CN
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- Makefile
- CMakePresets.json
- .github/workflows/matrix.yml
- doc/c++/COMPILING.md
- CMakeLists.txt
- .github/actions/setup-sdl3-stack/action.yml
source_symbols: []
source_queries:
- linux-x64
source_fingerprint: abe5b45a8d3024027e643dd8b0797a20967055098488185be3475fbcb377962e
authority: build-config
verified_commit: 7d65b4eff3d92393e659699a312b694f0e72d2cb
verified_at: '2026-10-11'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b35fb53e6d6883e1d78329e7096e78927b197bb182ae3e67c465c9066ce61458
prerequisites:
- platforms.matrix
- build.overview
depends_on:
- validation.testing
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cmake-configure
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms-linux
risk_level: normal
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/987
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/linux/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/linux/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/linux/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/linux/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/7d65b4eff3d92393e659699a312b694f0e72d2cb
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/CMakePresets.json
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/workflows/matrix.yml
- path: doc/c++/COMPILING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/doc/c++/COMPILING.md
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/CMakeLists.txt
- path: .github/actions/setup-sdl3-stack/action.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/7d65b4eff3d92393e659699a312b694f0e72d2cb/.github/actions/setup-sdl3-stack/action.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.linux%29%3A+&body=Document+ID%3A+platforms.linux%0ALanguage%3A+zh_CN%0AVerified+commit%3A+7d65b4eff3d92393e659699a312b694f0e72d2cb%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Linux 开发

Linux 是本地和 CI 覆盖最广的平台，但构建结果只有连同 compiler、frontend、SDL 版本、
localization、sound、test、sanitizer 与 build type 才有意义。

## 权威入口

- `Makefile` 定义原生 Make feature switch 与验证 target。
- `CMakePresets.json` 定义 `linux-x64`、`linux-tiles-sounds-x64` 和 vcpkg 变体。
- `.github/workflows/matrix.yml` 记录当前 CI 实际覆盖的组合。
- `doc/c++/COMPILING.md` 可提供背景；与以上构建文件冲突时以构建文件为准。

## 受支持路径

最小 CMake 路径是 curses、启用本地化与测试的 `linux-x64` preset；
`linux-tiles-sounds-x64` 增加图形与音频依赖面。原生 Make 通过 `TILES`、`SOUND`、
`SDL3`、`LOCALIZE`、`TESTS`、compiler、sanitizer 与 release flag 表达相同维度。

```sh
cmake --list-presets
cmake --preset linux-x64
cmake --build --preset linux-x64
```

聚焦原生测试遵循根 AGENTS 和 test matrix，不要复制大型 release 命令：

```sh
make -j2 tests
./tests/cata_test "<focused filter>"
```

## 验证与产物

报告 distribution、architecture、compiler/version、Make/CMake、preset/flag、curses/tiles、
SDL3 SDK 版本、sound、localization、sanitizer 和准确 test filter。build directory、
`compile_commands.json`、profiler capture 与 symbol database 是本地/CI artifact，不是要
提交的源码。

## 边界与注意事项

Linux 通过不能证明 Windows 或 Android 已验收。图形构建统一使用 SDL3，并需要
编译后的 shader artifact。`TILES=1 SDL3=0` 和 `TILES=ON USE_SDL3=OFF` 会报错；
终端构建和仅本地化目标不查询 SDL 依赖。旧包管理命令容易过时，应按 configure 输出
与已验证构建配置诊断。
