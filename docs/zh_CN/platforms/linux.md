---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.linux
title: Linux 开发
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
last_human_reviewer: Pending human review
source_paths:
- Makefile
- CMakePresets.json
- .github/workflows/matrix.yml
- doc/c++/COMPILING.md
source_symbols: []
source_queries:
- linux-x64
source_fingerprint: 2dba8fbfa2140a345e7ae382dda6be3b45598895eea9130a0a7f7e02c27158bf
authority: build-config
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 4e369a0d5512e76ab86eb50a35d7ef9d9bf57a9c01e655bdaa4c683411f050da
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
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/linux/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/linux/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/linux/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/linux/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CMakePresets.json
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/matrix.yml
- path: doc/c++/COMPILING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/c++/COMPILING.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.linux%29%3A+&body=Document+ID%3A+platforms.linux%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
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
SDL2/SDL3、sound、localization、sanitizer 和准确 test filter。build directory、
`compile_commands.json`、profiler capture 与 symbol database 是本地/CI artifact，不是要
提交的源码。

## 边界与注意事项

Linux 通过不能证明 Windows 或 Android 支持。SDL3 需要编译后的 shader artifact；SDL2
仍是独立 fallback lane。旧文档中的包管理命令容易过时，应按 configure 输出与已验证
构建配置诊断。
