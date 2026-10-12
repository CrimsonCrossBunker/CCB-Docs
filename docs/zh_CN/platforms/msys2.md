---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.msys2
title: MSYS2 与 MinGW
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
- CMakePresets.json
- Makefile
- msvc-full-features/vcpkg.json
- tools/build_shaders.py
source_symbols: []
source_queries:
- windows-x64
source_fingerprint: e0d575911300ee3881e0b77aa62a39685e5cf7524a82f55ae2a5088bb4ea7cd9
authority: build-config
verified_commit: 75f90e0741588679986b2867923e8a500678cd86
verified_at: '2026-10-12'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 438403074a5c48398e9616f9de1eb24d61926e32f53d1b27425896490302d2dd
prerequisites:
- platforms.windows
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; MSYS notes adapted from CDDA PR 88588 (Matthew Richmond) and PR 88664 (mqrause).
example_validation_ids:
- cmake-configure
- cpp-tests
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: platforms-windows
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/987
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msys2/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msys2/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msys2/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msys2/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/75f90e0741588679986b2867923e8a500678cd86
source_urls:
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/75f90e0741588679986b2867923e8a500678cd86/CMakePresets.json
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/75f90e0741588679986b2867923e8a500678cd86/Makefile
- path: msvc-full-features/vcpkg.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/75f90e0741588679986b2867923e8a500678cd86/msvc-full-features/vcpkg.json
- path: tools/build_shaders.py
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/75f90e0741588679986b2867923e8a500678cd86/tools/build_shaders.py
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.msys2%29%3A+&body=Document+ID%3A+platforms.msys2%0ALanguage%3A+zh_CN%0AVerified+commit%3A+75f90e0741588679986b2867923e8a500678cd86%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# MSYS2 与 MinGW

MSYS2 提供 `windows-x64` preset 背后的 MinGW Windows lane。所选 MSYS2 subsystem、
compiler architecture、package set 与 shell 必须一致；混用 MSYS/MinGW library 会制造
误导性的 configure 或 runtime failure。

## 契约路径

打开 **MSYS2 UCRT64** 环境并检查仓库 preset。依赖包使用 `mingw-w64-ucrt-x86_64-` 前缀，
不要把其他 subsystem 的头文件、库或 DLL 混入此配置：

```sh
cmake --list-presets
cmake --preset windows-x64
cmake --build --preset windows-x64
```

tiles+sound 使用 `windows-tiles-sounds-x64`。两者都是带 `RelWithDebInfo` build preset
的 multi-configuration Ninja 配置；不要另造会静默偏离 preset 的 build directory 或
configuration。

## 依赖与 shell 边界

`doc/c++/COMPILING-MSYS.md` 解释生态，实际契约由 `CMakePresets.json`、CMake configure
error 和当前 CI 决定。为选定 MinGW architecture 安装依赖，在匹配 shell 运行 MinGW
binary，并在不依赖开发 `PATH` 的环境检查打包 DLL 集合。

启用 SDL3 图形构建时，shader 编译还需要 `glslangValidator`。安装
`mingw-w64-ucrt-x86_64-glslang`，并确认 UCRT64 shell 的 `PATH` 能找到该工具。
SDL3 图片、字体和声音依赖同样来自 UCRT64 包；curses 配置不需要 shader 工具。

```sh
command -v gcc g++ glslangValidator
cmake --preset windows-tiles-sounds-x64 -DUSE_SDL3=ON
```

## 验证

- configure/build 准确 preset；
- 对相同 configuration 运行生成测试；
- tiles/sound 从干净 shell 启动，验证 renderer、font、sound、translation，以及启用
  SDL3 时的 shader artifact；
- PR 记录 shell（`UCRT64`）、compiler/version、preset 与 configuration。

## 常见失败

错误 architecture package、`PATH` 中 MSYS compiler 位于 MinGW 前、旧 CMake cache、
缺失 runtime DLL、混用 slash/drive path 是不同故障。保留首个 configure/link error，
不要靠向源码树复制任意 DLL“修复”。
