---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.martial-arts
title: 旧文档迁移草稿：martial arts
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
- doc/JSON/MARTIALART_JSON.md
- src/martialarts.cpp
- src/martialarts.h
- data/json/martialarts.json
- tests/martial_art_test.cpp
source_symbols:
- martialart::load
- ma_technique::load
- ma_buff::load
- attack_vector::load
source_queries: []
source_fingerprint: 2dae37d80a7a5118d1ba3e4e39e6e061160fc23beaa6e745832bb491a88d3d62
authority: docs-explanation
verified_commit: 02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
verified_at: '2026-08-02'
generated: true
generated_by: scripts/generate_legacy_migration.py
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: d1fae3685a2aac9b2884292d435301ccf5b8e193c742ce2aca5302580fe166e5
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
risk_group: json
risk_level: high
pending_source_pr: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/pull/568
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/martial-arts/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/martial-arts/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/reference/json/martial-arts/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/martial-arts/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b
source_urls:
- path: doc/JSON/MARTIALART_JSON.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MARTIALART_JSON.md
- path: src/martialarts.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/martialarts.cpp
- path: src/martialarts.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/src/martialarts.h
- path: data/json/martialarts.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/data/json/martialarts.json
- path: tests/martial_art_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/tests/martial_art_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.martial-arts%29%3A+&body=Document+ID%3A+json.martial-arts%0ALanguage%3A+zh_CN%0AVerified+commit%3A+02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 旧文档迁移草稿：martial arts

本页是 `json.martial-arts` 的迁移草稿页面。它记录 **1** 条冻结清单记录，但不把旧说明提升为运行时契约。

- Stable document IDs: `json.martial-arts`
- Target: `reference/json/martial-arts.md`
- Replacement: https://crimsoncrossbunker.github.io/CCB-Docs/reference/json/martial-arts/
- Archive reason: —

## 清单记录

| stable ID | original path | action | status | last applicable | merge target |
| --- | --- | --- | --- | --- | --- |
| json.martial-arts | doc/JSON/MARTIALART_JSON.md | migrate_preserve | stubbed | 7a008bf28d7ee7ebef549514228a0d0b45b7bac4 | — |

## 权威边界

运行时行为仍以 CCB 源码和测试为准；JSON/Lua/API 以 Schema、声明、注册信息和生成清单为准；构建以 CI、CMake、Makefile 与 Gradle 为准。本页只解释迁移状态、历史和可审核来源。若旧正文与当前契约冲突，应以契约为准。

## 当前 CCB Martial Arts 对象图

武术不是单个 JSON 对象。当前运行时分别注册 `attack_vector`、`weapon_category`、
`technique`、`martial_art` 与 buff；style 再引用 technique、weapon/category，并在战斗
事件上应用 buff 或 EOC。

### Style 与 technique

`martial_art` 需要稳定 `id`、`name`、`description` 和 `initiate`。`autolearn` 是
skill/level pair；`primary_skill`、`learn_difficulty`、`teachable`、`weapons` 与
`weapon_category` 决定学习和可用武器。`strictly_melee` 等限制必须与 UI 和实际选择逻辑
一起验证。

`technique` 当前至少需要 `name`；通常还提供玩家/NPC messages 和 `attack_vectors`。
crit、counter、disarm、knockback、AoE、repeat、condition、requirements 与 bonuses 共同
决定何时进入候选和执行什么。缺少 attack vector 的普通攻击 technique 会被 consistency
check 报告；defensive、dummy、grab-break 或 miss-recovery 等类型是例外。

### Attack vector、requirements 与 buff

`attack_vector` 描述 weapon/limb、contact area、limb HP、encumbrance、armor bonus 和
required/forbidden limb flags。它不是纯动画名称：选中的 limb 和 contact 会影响可执行性、
伤害与测试。

Style 可在 static、move、pause、hit、attack、dodge、block、get-hit、miss、crit、kill
时机挂 buff 和 inline EOC。Buff 有 duration、stack、persist、dodge/block 与 bonus/requirement
数据。每个触发时机的 actor、武器、目标和重复频率不同；EOC 不应假定始终存在 beta talker。

requirements 包括 skill、weapon damage、weapon category、buff、character flag 等组合。
“装备了允许武器”并不保证 technique 通过 limb、condition、ammo、range 或 cooldown 条件。

### 设计与验证

1. 先用已有第一方 style 找到最接近的对象图，保持 ID 前缀和翻译 message。
2. 运行 formatter、`make -j2 json-check` 和实际 Mod 集 `--check-mods`。
3. 运行 `martial_art_test`，覆盖 weapon category、limb substitution/HP/encumbrance、
   condition、sweep、stun 与 knockback。
4. 在游戏中分别测试空手、每类武器、受伤/高负重、NPC、crit/counter 和每个 buff/EOC 时机。
5. 记录 DPS、命中、防御、stack 与触发频率；加载成功无法证明没有无限叠层或强制循环。

旧文档中的 bonus 字符串与 flag 清单可能落后；具体枚举和范围以当前 loader/consistency
check 为准。

## 历史与归属

清单中的已接受贡献者为：thaelina。许可证：CC-BY-SA-3.0。异常贡献者原始值没有导入或发布。

源清单冻结 commit 为 `0378ca2b84303cf614c617c9d9eaa50138cd21ff`；本次交叉仓验证 commit 为 `02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b`；聚合源指纹为 `2dae37d80a7a5118d1ba3e4e39e6e061160fc23beaa6e745832bb491a88d3d62`。[过滤历史实验报告](/CCB-Docs/migration/filtered-history-experiment/)记录了为何不导入整个游戏仓库历史。

## CCB 中保留的正文

- [`doc/JSON/MARTIALART_JSON.md`](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MARTIALART_JSON.md) — [history](https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commits/02d1b4949f8fdb7c59e5aada0b0ce8bf633f3c5b/doc/JSON/MARTIALART_JSON.md)

## 替代与下一步

该页保持 Draft，直到 Responsible human 对正文、来源与替代关系完成审查；Draft 不进入正式导航、搜索或 AI allowlist。
