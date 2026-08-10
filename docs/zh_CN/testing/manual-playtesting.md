---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: testing-manual
title: 旧文档迁移草稿：manual playtesting
language: zh_CN
status: stale
doc_type: explanation
audiences:
- new-contributor
- experienced-contributor
- maintainer
- mod-author
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 365
last_human_reviewer: LYHGLYTX
source_paths:
- doc/TESTING_YOUR_CHANGES.md
- tests/AGENTS.md
- Makefile
- CMakeLists.txt
- .github/workflows/matrix.yml
source_symbols: []
source_queries: []
source_fingerprint: 7badd83cf8a19d410f0d2183cacd6b564d381a8f96a17b6bc332b2cc5b003988
authority: docs-explanation
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: bdfeaec135c5ecb8dabb94ab1753b940d90279ba1f560c5ce43e365d4a9ab9a1
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: thaelina; accepted inventory identities only. Source paths and Git history
  remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: testing
risk_level: high
pending_source_pr: null
stale_reason: 'Source paths changed after d32b9cc880a8: .github/workflows/matrix.yml, Makefile'
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/testing/manual-playtesting/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/testing/manual-playtesting/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/testing/manual-playtesting/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/testing/manual-playtesting/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: doc/TESTING_YOUR_CHANGES.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/TESTING_YOUR_CHANGES.md
- path: tests/AGENTS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tests/AGENTS.md
- path: Makefile
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/Makefile
- path: CMakeLists.txt
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/CMakeLists.txt
- path: .github/workflows/matrix.yml
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/.github/workflows/matrix.yml
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28testing-manual%29%3A+&body=Document+ID%3A+testing-manual%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：manual playtesting

本页是 `testing-manual` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `testing-manual`
- Target: `testing/manual-playtesting.md`
- Replacement: testing-manual
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| testing-manual | doc/TESTING_YOUR_CHANGES.md | merge_into | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | testing-manual |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 有证据的手动 playtesting

自动化检查证明格式、加载和已编码不变量；非平凡的 gameplay/UI/content 变化还需要在与 source
commit 匹配的 CCB binary 中手动验证。先写出变更的可观察风险，再构造最小场景，不要无目的地
玩几分钟后声称“测试过”。

### 准备与记录

- 使用独立测试世界/角色，记录 commit、build flags、平台、Mod set、seed、option 与存档来源。
- JSON 必须先 format/load；C++ 先编译受影响 target 并运行 focused test。
- 确认 binary 与 data 来自同一 commit。重新启动或按实际 loader 生命周期 reload；不要假设回到
  主菜单能刷新所有 registry。
- 保留复现步骤、期望/实际结果、日志、截图或短视频，并同时测正常路径、失败路径和关键边界。

Debug menu 可生成 item/monster、编辑 map/overmap、跳时、传送或调用子系统入口，但 debug 生成
会跳过自然生成的一部分上下文。Monster definition 变化应用新生成实例测试；成长、进化与离屏
处理还需 unload/reload 和时间推进。Mapgen 使用未生成 OMT 并覆盖方向/z-level/region；EOC、Lua、
save migration 和 multiplayer 要走自己的真实入口。

测试完撤销 debug-only 状态，不把测试存档、日志或 generated artifacts 提交。PR 中区分实际执行、
CI 覆盖与未运行项目；一次手动成功不能替代 deterministic regression test，修 bug 时仍应添加能
在旧实现失败的最窄自动化用例。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `d32b9cc880a85480840d82cfa05d256c78a16615`；聚合源指纹为 `7badd83cf8a19d410f0d2183cacd6b564d381a8f96a17b6bc332b2cc5b003988`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/TESTING_YOUR_CHANGES.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/doc/TESTING_YOUR_CHANGES.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/d32b9cc880a85480840d82cfa05d256c78a16615/doc/TESTING_YOUR_CHANGES.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
