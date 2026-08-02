---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.crash-reports
title: Crash report 与 symbol
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
review_interval_days: 120
last_human_reviewer: Pending human review
source_paths:
- src/crash.h
- src/crash.cpp
- src/debug.cpp
- .github/workflows/msvc-full-features.yml
source_symbols:
- void init_crash_handlers();
source_queries:
- BACKTRACE
source_fingerprint: 84f96e7aba0cf6b109527bb678678b13f9cce878d74ec03480ebb49d390f8fe0
authority: source-and-tests
verified_commit: dbaedf8357408ae6f96309732d6e087e9b878e18
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 14e660250e730d64aebabb110fc3d1a74e23ae94c705bcb34374b794001e8ef1
prerequisites:
- validation.debugging
- platforms.matrix
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: diagnostics
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/operations/crash-reports/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/crash-reports/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/crash-reports/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/crash-reports/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/dbaedf8357408ae6f96309732d6e087e9b878e18
source_urls:
- path: src/crash.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/crash.h
- path: src/crash.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/crash.cpp
- path: src/debug.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/src/debug.cpp
- path: .github/workflows/msvc-full-features.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/dbaedf8357408ae6f96309732d6e087e9b878e18/.github/workflows/msvc-full-features.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.crash-reports%29%3A+&body=Document+ID%3A+operations.crash-reports%0ALanguage%3A+zh_CN%0AVerified+commit%3A+dbaedf8357408ae6f96309732d6e087e9b878e18%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Crash report 与 symbol

有效 crash report 要识别准确 binary，并提供足以复现或 symbolize 的状态。最后画面截图或
单独一行“crashed”只是辅助证据，不是 stack trace。

## 最小报告

- 准确 CCB commit、tag/release URL，以及 binary 是否本地重编；
- OS/version、architecture 或 Android ABI/API/device、compiler/build type、curses/tiles、
  SDL2/SDL3、sound、localization、Lua UI 与 sanitizer/backtrace setting；
- active Mod/相关配置、复现步骤、预期/实际结果；
- 首个 error 及上下文 debug log，可得的 stack trace/tombstone/minidump；
- 新 world 是否复现、是否需要 save，以及 consent/redaction 说明。

## Native 路径

`src/crash.cpp` 安装平台 crash handler/stack trace support，`src/debug.cpp` 拥有 debug log。
stack 只有配合同一 commit/build configuration 的 executable、shared library 与 symbol 才
有用。处理前保留 raw address。

## Android 路径

区分 Java exception、native `crash_dump`/tombstone、renderer/device loss、asset copy、
storage 与 install/signature failure。收集包含 process start 和 fatal block 的聚焦
`logcat`，记录 version code/name、package、ABI 与 install/update state。

## 隐私与安全

log、save、path、username、world name、network address、token 与 device info 可能敏感。
去除 secret 时保留 control flow/ID；私密 save/dump 使用获准受限渠道，默认不能放公开 Issue。

## Triage 流程

在报告 commit/config 复现，用匹配 artifact symbolize，缩减 Mod/data，定位 owner subsystem，
可行时添加确定性 regression test。得到处理后 trace 也不能丢弃原始 log。

## Artifact 政策

PDB、debug symbol、tombstone、core file 与 profiler capture 是 CI/release/diagnostic artifact，
不是仓库源码。记录 checksum、retention、access 与 deletion policy。
