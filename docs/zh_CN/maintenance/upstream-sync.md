---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: maintenance.upstream-sync
title: 上游同步
language: zh_CN
status: draft
doc_type: how-to
audiences:
- experienced-contributor
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 120
last_human_reviewer: LYHGLYTX
source_paths:
- CONTRIBUTING.md
- GOVERNANCE.md
- doc/development_process.md
source_symbols: []
source_queries: []
source_fingerprint: d5d7414ad8ce1f7b2c96ed84f49a05f3fdce63af9d065c7a906b1d55c165bbd1
authority: governance
verified_commit: 2c899a3db790e11a6ff44d91f319064b1ee65d2a
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 7879927db6623b701d64de6a3aec0cd3ecc14b6c0e248d648b7cd3cfdeffa842
prerequisites:
- getting-started.experienced-index
depends_on:
- compatibility.save
- compatibility.mods
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; see source paths and Git history.
example_validation_ids:
- cpp-tests
- json-load
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: upstream
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/560
stale_reason: null
search:
  exclude: true
---

# 上游同步

CCB 与其他 Cataclysm 系仓库共享历史，但不是镜像。上游 commit 是证据和素材，不能
覆盖 CCB 的运行时权威。

## 修改前记录来源

- 来源仓库、PR/Issue 与精确 commit 范围；
- 原作者和适用许可证；
- 移植理由以及它要解决的 CCB 问题；
- 有意省略或重写的文件与行为；
- 已知 CCB 分歧与可能冲突区域。

在 commit message 和 PR 中保留署名，不要把多个上游变化压成无法追溯的补丁。

## 检查 CCB 边界

比较注册、数据 ID、序列化、Mod 加载、EOC context、Lua v5 公共契约、UI/input、
桌面/Android 配置与测试。查找来源修改之后的上游修复，但逐项评估。上游测试通过
不能证明 CCB 兼容。

## 验证与记录

先运行能证明目标行为的最小 CCB 测试；涉及共享核心、存档、数据、API 或平台风险时
再扩大。只有为防止未来错误重复移植所必需时才写源码注释；完整分歧解释放在
CCB-Docs 并链接精确来源。

只有来源可审计、最终 CCB diff 已理解、兼容影响明确且 Responsible human 负责时，
移植才达到 ready 状态。
