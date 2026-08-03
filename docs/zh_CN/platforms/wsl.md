---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: platforms.wsl
title: WSL 开发
language: zh_CN
status: active
doc_type: how-to
audiences:
- new-contributor
- experienced-contributor
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- Makefile
- CMakePresets.json
- doc/c++/COMPILING.md
source_symbols: []
source_queries:
- linux-x64
source_fingerprint: fbd977708b89bb26456c14aa37df1c21f9ca4170fe06454a11a30d7932dad2b0
authority: build-config
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 0a36c080292216c43bf7099099a3ef9650b42506f28e6cc3ead4c14cbaa6e1d9
prerequisites:
- platforms.linux
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
risk_group: platforms-wsl
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/wsl/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/wsl/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/platforms/wsl/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/platforms/wsl/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/Makefile
- path: CMakePresets.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/CMakePresets.json
- path: doc/c++/COMPILING.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/doc/c++/COMPILING.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28platforms.wsl%29%3A+&body=Document+ID%3A+platforms.wsl%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
---

# WSL 开发

WSL 在 Windows host 上运行 Linux toolchain，适合 Linux 构建与测试，但不能证明原生
MSVC/MinGW packaging、Windows DLL discovery 或原生 Windows console/input 路径。

## 有意选择文件系统

Linux 构建放在 WSL Linux filesystem 通常比 `/mnt/c` 更快，权限也更可预测。记录 checkout
与 build directory 位于 Linux 还是 mounted Windows filesystem；case sensitivity、
executable bit、file watching 与 path translation 都可能改变故障形态。

## 构建路径

使用 `Makefile` 或 `CMakePresets.json` 的 Linux 契约，不使用 Windows preset：

```sh
cmake --list-presets
cmake --preset linux-x64
cmake --build --preset linux-x64
```

tiles、sound 或实际启动游戏还要分别说明 WSL version、graphics integration、display/audio
environment、GPU/driver path 与 SDL 版本。headless curses test 通过不能验证这些层。

## 验证边界

报告 Windows version、WSL version/distribution、filesystem location、compiler、preset/
flag，以及 binary 是否只在 WSL 内测试。用 Git 验证 line ending/executable bit，但不要
把平台生成文件或本地 mount path 加入仓库。

## 常见失败

mounted drive 元数据慢、Windows tool 意外位于 `PATH` 前、CRLF shell script、GUI/audio
socket 不可用和 memory limit 需要不同修复。判断是 CCB 代码还是 WSL 集成前，应在原生
Linux CI lane 复现。
