---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.wounds
title: 旧文档迁移草稿：wounds
language: zh_CN
status: draft
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
last_human_reviewer: Pending human review
source_paths:
- doc/JSON/WOUNDS.md
- src/wound.cpp
- src/wound.h
- src/init.cpp
source_symbols:
- wound_type::load
- wound_fix::load
source_queries: []
source_fingerprint: db92a6ba158f1a65862d0f34952e0e68526ab44413c80dd28176bf3ba13f8266
authority: docs-explanation
verified_commit: c1b0f95c6d1b074fc49ee2a7976819c124b69047
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: a878a33c095c47f549c67a51947a409f868684e24919cddf40a8b4eada3a2a64
prerequisites: []
depends_on: []
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: 'CCB contributors: Anton Simakov, GuardianDll, thaelina; accepted inventory identities only.
  Source paths and Git history remain authoritative.'
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/wounds/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/wounds/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/wounds/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/wounds/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/c1b0f95c6d1b074fc49ee2a7976819c124b69047
source_urls:
- path: doc/JSON/WOUNDS.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/WOUNDS.md
- path: src/wound.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/wound.cpp
- path: src/wound.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/wound.h
- path: src/init.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/src/init.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.wounds%29%3A+&body=Document+ID%3A+json.wounds%0ALanguage%3A+zh_CN%0AVerified+commit%3A+c1b0f95c6d1b074fc49ee2a7976819c124b69047%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：wounds

本页是 `json.wounds` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.wounds`
- Target: `reference/json/wounds.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/wounds/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.wounds | doc/JSON/WOUNDS.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Wound 与 wound fix

`wound` 是绑定 bodypart 的持久状态，`wound_fix` 是治疗定义。两者各有 generic factory；fix 在
finalize 时解析 requirements 并反向登记到被移除的 wound。它们不是普通 effect 的别名。

### Wound fields

name、description、damage_types、damage_required 必填。pain 默认 0–0，healing_time 默认无限，
weight 默认 1，limit 默认 0；还可设置 limb scores、progression 及 bodypart type/flag 白黑名单。
progression 要求 id，chance 限制为 0–100。range pair 的顺序、damage type ID 和 progression ID
需要 consumer/test 验证，当前 `wound_type::check` 本身为空，不能只依赖 factory check。

### Wound fix fields

name/description 必填；time、skills、removed/added wounds、success_msg、HP modifier、proficiencies
和 requirements 可选。proficiency entry 要求 ID，time_save 默认 1，is_mandatory 默认 false。
requirements 可引用 `[id, count]` 或定义 inline requirement，finalize 后合并。

fix consistency 检查 skill、wound、proficiency 与 requirement IDs。删除/重命名 wound 会影响存档、
progression 和 fixes，必须提供明确 migration/compatibility 策略；没有自动 wound migration 契约时
不能假装安全。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`。用 focused wound tests 覆盖 damage
threshold、每 limb limit、白黑名单、progression、随机 pain/heal range、mandatory proficiency、
requirements 消耗、add/remove、HP 正负修改和存档 reload。破坏性或未实现的组合应明确标为
experimental，而不是仅凭 JSON 成功加载发布。

## 历史与归属

清单中的已接受贡献者为：Anton Simakov, GuardianDll, thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `c1b0f95c6d1b074fc49ee2a7976819c124b69047`；聚合源指纹为 `db92a6ba158f1a65862d0f34952e0e68526ab44413c80dd28176bf3ba13f8266`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/WOUNDS.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/WOUNDS.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/c1b0f95c6d1b074fc49ee2a7976819c124b69047/doc/JSON/WOUNDS.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
