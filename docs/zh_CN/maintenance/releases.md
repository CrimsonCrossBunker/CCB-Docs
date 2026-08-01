---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: maintenance.releases
title: 发布维护
language: zh_CN
status: draft
doc_type: how-to
audiences:
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- doc/RELEASE_PROCESS.md
- .github/workflows/release.yml
- .github/workflows/release-android-bundle.yaml
source_symbols: []
source_queries: []
source_fingerprint: e20c16c43878b2fd175b9287b26b0340655df5724554fe0985cf74441118045d
authority: build-config
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: b257834293240b817b77b6d8244f0484ff475e9215a6a56f402f0c7f90db9d29
prerequisites:
- platforms.matrix
- validation.testing
depends_on:
- governance.security-license
redirect_from: []
supersedes:
- legacy.doc-release-diff
- legacy.doc-release-process
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: release
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
search:
  exclude: true
---

# 发布维护

发布行为由当前 workflow 与仓库设置定义，不能照抄旧上游 checklist。历史发布正文在
每条命令确认前只能作为审计输入。

## 发布前

- 选择并记录精确源码 commit 与版本身份；
- 确认目标平台和功能组合的默认分支检查稳定成功；
- 审查存档、数据、Lua API、Mod、翻译、打包与安全影响；
- 核对第三方许可证、署名和 release note 来源；
- 从同一源码 commit 生成文档与 API snapshot；
- 通过受保护 environment 核验签名/发布凭据，绝不放入仓库文件或日志。

## 产物与验证

每个产物记录平台、架构/ABI、构建类型、功能选项、源码 commit、workflow run、
checksum 与签名状态。测试安装/解压和一次启动加载。Android APK/AAB、Windows 包和
Linux 产物是不同证据。

大型 Doxygen、compile database、索引、profile 和符号数据库只作为 CI/Release
artifact，不提交源码。备份与保留机制必须包含 restore test，不能只验证上传成功。

## 发布后

发布 release notes、API changelog、已知兼容问题、文档 snapshot 和回滚/热修路线，
并确认下载链接与玩家入口。失败或部分发布必须明确记录；不得在同一身份下静默替换产物。
