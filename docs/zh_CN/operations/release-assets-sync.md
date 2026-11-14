---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: operations.release-assets-sync
title: Android 音效与翻译包发布草稿
language: zh_CN
status: draft
doc_type: how-to
audiences:
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 60
last_human_reviewer: Pending human review
source_paths:
- .github/workflows/release.yml
- .github/workflows/matrix.yml
source_symbols: []
source_queries:
- publish-translations
- Android x64 New UI
- clang++-22
- g++-16
source_fingerprint: 654aa06af56cd828a6c7cbe22d369d4d481f5c289b43000be487cb4abd98de06
authority: build-config
verified_commit: 34200a2ffcdaaf925cf2381bf900d2c753cd1a6c
verified_at: '2026-11-14'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8e73ee7a18624c5587638586e4f16ac31f8765fced8cfb51293ca51ea1ceb6ef
prerequisites:
- operations.releases
- platforms.android
depends_on:
- maintenance.releases
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: release
risk_level: high
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/operations/release-assets-sync/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/operations/release-assets-sync/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/operations/release-assets-sync/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/operations/release-assets-sync/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c
source_urls:
- path: .github/workflows/release.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/.github/workflows/release.yml
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/34200a2ffcdaaf925cf2381bf900d2c753cd1a6c/.github/workflows/matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28operations.release-assets-sync%29%3A+&body=Document+ID%3A+operations.release-assets-sync%0ALanguage%3A+zh_CN%0AVerified+commit%3A+34200a2ffcdaaf925cf2381bf900d2c753cd1a6c%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# Android 音效与翻译包发布草稿

CCB #993 引入翻译归档及 Android 音效包配置。本地工具验证覆盖矩阵和归档命令；Android 构建、设备播放及实际 Release 上传仍需发布验收。

后续 Android 打包变更移除了 Experimental Release 中 Android x64、Android x64 New UI 和 Android x32 的内置音效包配置。设备播放和签名需单独验收。

翻译构建完成后，独立步骤把 `translations` artifact 打包为 `ccb-translations-<timestamp>.tar.gz`，上传到创建发布步骤输出的实际 `tag_name`。Experimental 使用时间戳标签；Candidate 和 Stable 保留版本标签。翻译归档是额外文件，不能替代平台安装包。

重跑不覆盖同名归档。已有归档或上传失败时，检查准确来源、日志及文件状态，不静默替换翻译。

五项回归测试覆盖新增翻译字符串、macOS 别名占比累加、真实 tar 归档与三种渠道的模拟上传。模拟上传只记录命令；最终验收仍需核对源码 SHA、workflow run、全部安装包和实际 Release 文件。

改动适配自 CDDA #88516、#88789、#88791、#88836，各来源提交保留原作者与出处。Responsible human: LYHGLYTX。

CI 矩阵使用 Clang 14 作为基本编译器，在 Ubuntu 26.04 上检查 Clang 22 和 GCC 16。保留 Lua、铁路、高级物品管理专项检查和 GCC 单编译任务的内存限制，并显式安装所需包。已记录的矩阵检查覆盖配置解析。
