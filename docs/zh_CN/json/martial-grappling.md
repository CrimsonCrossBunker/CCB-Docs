---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: json.martial-grappling
title: 主动武术擒抱战技
language: zh_CN
status: draft
doc_type: reference
audiences:
- mod-author
- player
- maintainer
owners:
- CCB maintainers
reviewers:
- Documentation reviewers
review_interval_days: 90
last_human_reviewer: Pending review
source_paths:
- data/json/martial_grappling.json
- data/json/martialarts.json
- src/martialarts.h
- src/martialarts.cpp
- src/melee.cpp
- src/monster.cpp
- src/avatar_action.cpp
- tests/martial_grappling_test.cpp
source_symbols:
- use_grapple_technique
- grapple_cooldown_effect
source_queries: []
source_fingerprint: 3fea3da996506b145f5a008d65da1c90ff8dbd01a936b76daf87150bfc734f2a
authority: source-and-tests
verified_commit: 603cd50217c18f1ba9b4fab50d25fb0d46216dd1
verified_at: '2026-11-04'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: aa749873f5ff8e39ca1fec84deb1b60c6dfc454886c12480e9d23eff14fc830f
prerequisites:
- json.overview
depends_on:
- reference.json-object-types
redirect_from: []
supersedes: []
license: CC-BY-SA-3.0
attribution: CCB contributors; gameplay design inspired by CTLG monster dragging.
example_validation_ids: []
api_version: null
deprecated: false
deprecation_replacement: null
risk_group: martial-arts
risk_level: normal
pending_source_pr: null
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/json/martial-grappling/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/json/martial-grappling/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/json/martial-grappling/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/json/martial-grappling/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/603cd50217c18f1ba9b4fab50d25fb0d46216dd1
source_urls:
- path: data/json/martial_grappling.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/data/json/martial_grappling.json
- path: data/json/martialarts.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/data/json/martialarts.json
- path: src/martialarts.h
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/martialarts.h
- path: src/martialarts.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/martialarts.cpp
- path: src/melee.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/melee.cpp
- path: src/monster.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/monster.cpp
- path: src/avatar_action.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/src/avatar_action.cpp
- path: tests/martial_grappling_test.cpp
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/603cd50217c18f1ba9b4fab50d25fb0d46216dd1/tests/martial_grappling_test.cpp
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28json.martial-grappling%29%3A+&body=Document+ID%3A+json.martial-grappling%0ALanguage%3A+zh_CN%0AVerified+commit%3A+603cd50217c18f1ba9b4fab50d25fb0d46216dd1%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

# 主动武术擒抱战技

擒抱战技通过武术的 `techniques` 列表绑定，在主动战技菜单中选择。设计灵感来自 CTLG
的 G 键拖拽怪物：空手角色先建立控制，再拖动目标，最后使用流派对应的摔投技。

## 战技字段

| 字段 | 含义 |
| --- | --- |
| `manual_activation` | 设为 `true`，由玩家主动选择执行。 |
| `strictly_unarmed` | 设为 `true`；擒抱要求两条可用、空闲的手臂。 |
| `attack_vectors` | 提供可用的徒手攻击向量，如 `vector_punch`。 |
| `grapple_action` | `hold`、`drag` 或 `throw`。 |
| `grapple_power` | 正数杠杆百分比，影响体重上限和摔投伤害。 |
| `grapple_stamina` | 正数基础耐力消耗，随目标体重增加。 |
| `grapple_cooldown` | 正数冷却时长，相同动作的战技共享冷却。 |

角色需要站立、清醒且未骑乘；原有战技使用条件仍然有效。菜单显示基础耐力消耗、共享冷却
以及剩余恢复时间。

## 控制与移动

`hold` 为相邻怪物施加带有来源信息的 `martial_grapple` 效果。每个角色同时控制一个目标，
建立新控制会释放旧目标。控制者保持相邻、能使用两条空闲手臂且剩余耐力至少为 100 时，
被控制的怪物无法移动。

`drag` 使角色沿远离目标的方向后退一格，将怪物拉到角色原先的位置，并保留控制的剩余
时长。`throw` 释放控制，将怪物摔到角色身后，造成钝击伤害并施加 `downed`。拖拽和摔投
要求使用者本人建立的控制，以及畅通、有支撑的落点；束缚和载具连接也会影响可用性。

## 体重、体型与消耗

承重上限以千克计，公式为 `(力量 * 10 + 徒手技能 * 5) * grapple_power / 100`。
目标体重必须在上限内，体型最多比角色大一级。令 `load = 目标体重千克 / 承重上限千克`，
则耐力消耗为 `grapple_stamina + floor(grapple_stamina * load)`，行动消耗为
`floor(100 + 100 * load + max(0, 体型差) * 25)` 移动点。

负荷增大会缩短控制和倒地时长，并降低摔投伤害；体型差也会独立影响控制和冲击效果。
核心擒抱、拖拽的冷却分别为 3 秒和 1 秒，摔投冷却为 4 至 6 秒。效果序列化保存控制来源
及冷却，切换武术后仍然受相同动作的共享冷却约束。

## 核心流派

| 流派 | 主动终结技 |
| --- | --- |
| 柔道 | 大腰摔：杠杆效率更高。 |
| 合气道 | 呼吸投：低冲击的借力引导。 |
| 潘克拉辛 | 抱摔：更高冲击与耐力消耗。 |
| 太极拳 | 推手失衡：以控制和低冲击倒地为主。 |
| 马伽术 | 控制摔倒：平衡冲击与恢复时间。 |
| 泰拳 | 通过共享的擒抱和拖拽战技实现缠抱控制。 |

战技定义在 `data/json/martial_grappling.json`，流派绑定在 `data/json/martialarts.json`。
运行 `cata_test "[martial_arts]" --rng-seed 20261104` 可覆盖擒抱和现有武术行为，专门的
回归用例位于 `tests/martial_grappling_test.cpp`。
