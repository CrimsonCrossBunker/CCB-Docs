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
- doc/c++/COMPILING-MSYS.md
- .github/workflows/msvc-full-features.yml
source_symbols: []
source_queries:
- windows-x64
source_fingerprint: 8cd18fa5d699734e435a4a5e4adc4c4e5d73f59fd585323ec6ce56b474c752e9
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: bc3e58ed87ce480f2925aecac89f9313b9869c581272cfae45131748b7f4ae03
prerequisites:
- platforms.windows
depends_on: []
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
risk_group: platforms-windows
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msys2/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msys2/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/msys2/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/msys2/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/CMakePresets.json
- path: doc/c++/COMPILING-MSYS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/c++/COMPILING-MSYS.md
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/.github/workflows/msvc-full-features.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.msys2%29%3A+&body=Document+ID%3A+platforms.msys2%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# MSYS2 与 MinGW

MSYS2 提供 `windows-x64` preset 背后的 MinGW Windows lane。所选 MSYS2 subsystem、
compiler architecture、package set 与 shell 必须一致；混用 MSYS/MinGW library 会制造
误导性的 configure 或 runtime failure。

## 契约路径

打开匹配的 MinGW64 环境并检查仓库 preset：

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

## 验证

- configure/build 准确 preset；
- 对相同 configuration 运行生成测试；
- tiles/sound 从干净 shell 启动，验证 renderer、font、sound、translation，以及启用
  SDL3 时的 shader artifact；
- PR 记录 shell（`MINGW64`）、compiler/version、preset 与 configuration。

## 常见失败

错误 architecture package、`PATH` 中 MSYS compiler 位于 MinGW 前、旧 CMake cache、
缺失 runtime DLL、混用 slash/drive path 是不同故障。保留首个 configure/link error，
不要靠向源码树复制任意 DLL“修复”。
