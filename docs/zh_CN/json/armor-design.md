---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json-armor-design
title: 旧文档迁移草稿：armor design
language: zh_CN
status: active
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
- doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md
- src/item_armor.cpp
- src/item_factory.cpp
- data/json/items/armor/torso_armor.json
- tests/item_test.cpp
source_symbols: []
source_queries: []
source_fingerprint: a9714429c46f2041888b761dac2dd50fb337ba9405ccd4439c40b6ceacb56f27
authority: docs-explanation
verified_commit: 4e3b9aa99ae59630abf60f717bdaf563b2d63245
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 035e9840690568b77b4e754f7a7b992af931afaa10097aa5ad63715894012514
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
risk_group: design
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/armor-design/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/armor-design/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/armor-design/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/armor-design/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/4e3b9aa99ae59630abf60f717bdaf563b2d63245
source_urls:
- path: doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md
- path: src/item_armor.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/item_armor.cpp
- path: src/item_factory.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/src/item_factory.cpp
- path: data/json/items/armor/torso_armor.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/data/json/items/armor/torso_armor.json
- path: tests/item_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/4e3b9aa99ae59630abf60f717bdaf563b2d63245/tests/item_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json-armor-design%29%3A+&body=Document+ID%3A+json-armor-design%0ALanguage%3A+zh_CN%0AVerified+commit%3A+4e3b9aa99ae59630abf60f717bdaf563b2d63245%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 旧文档迁移草稿：armor design

本页是 `json-armor-design` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json-armor-design`
- Target: `json/armor-design.md`
- Replacement: json-armor-design
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json-armor-design | doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md | migrate_rewrite | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## Armor JSON 设计与审核

Armor 是 item 契约加上 `islot_armor`。每个 `armor` portion 必须声明 `covers`，并可独立设置
coverage、melee/ranged/vitals coverage、sublocations、encumbrance、materials、layers、
breathability 与 environmental protection。顶层字段和 inheritance 会再应用到各 portion；审核时
必须看最终展开值。

### 几何、材料与穿戴

`specifically_covers` 把 coverage 限定到 sub-bodypart；缺少 sublocation 数据时，覆盖 parent
bodypart 就视为覆盖其 subparts。`sided` 让实例在左右侧之间切换。layers 决定同部位衣物冲突，
不要用任意 flag 或旧表替代当前 layer enum 与运行时检查。

portion material 要有 type，`covered_by_mat` 必须为 1–100，thickness 为该材料层厚度。旧字符串
material 形式仍能读取但代码已标为旧路径；新内容优先使用可审核的 per-portion material。真实
重量、厚度、材料、coverage 和活动关节决定平衡，不能为了目标数值伪造物理属性。

### Encumbrance、pockets 与 ablative

encumbrance 可为单值或 empty/full pair，也可用 volume modifier。pocket 自身 modifier、rigidity
与内容共同影响结果。ablative pocket 的 insert 仍是 armor item；其 flag restriction、coverage、
不可直接穿戴边界和破损/transform 都要一起核对。

### 最小复杂度原则

普通衣物只表达真实需要的 portions；高级材料、per-subpart layers、特殊 coverage、relic effect 或
transform 只在能说明玩家可见差异时加入。不要复制旧文档的“完整 flag 列表”，flag 注册表和
consumer 才是契约。

### 验证

从当前相似第一方 armor 取基线，检查 item info、穿戴冲突、满/空 pocket、左右侧、近战/远程和
ablative damage。运行 formatter、`make -j2 json-check`、Mod `--check-mods`，并为新边界扩展
focused item/armor tests。平衡数字还需要 Responsible human 审阅其研究来源。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `80828049edb3adf2a13bb2912a19373dc4e69f32`；聚合源指纹为 `a9714429c46f2041888b761dac2dd50fb337ba9405ccd4439c40b6ceacb56f27`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/80828049edb3adf2a13bb2912a19373dc4e69f32/doc/design-balance-lore/ARMOR_BALANCE_AND_DESIGN.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
