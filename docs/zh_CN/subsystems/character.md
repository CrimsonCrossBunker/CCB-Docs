---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: subsystems.character
title: 角色与生物系统技术手册
language: zh_CN
status: stale
doc_type: explanation
audiences:
- mod-author
- api-user
- experienced-contributor
- maintainer
owners:
- CCB Lua API maintainers
reviewers:
- Documentation reviewers
- Lua API reviewers
review_interval_days: 60
last_human_reviewer: LYHGLYTX
source_paths:
- data/lua/README.md
- data/lua/manifest.schema.json
- data/lua/types/ccb_api_v5.d.lua
- data/lua/reference/ccb_public_api_v5.json
- data/lua/reference/ccb_public_api_v5_coverage.json
- tools/lua_api/README.md
source_symbols:
- Lua Mod API v5
source_queries: []
source_fingerprint: 30a19e6cbd8c6709ac5ccda80fe349e9459ddaccd8d3dc96507ee282c17f48cb
authority: api-contract
verified_commit: d32b9cc880a85480840d82cfa05d256c78a16615
verified_at: '2026-08-02'
generated: false
generated_by: null
include_in_search: false
include_in_ai_index: false
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 6fa1e8c43132ab67de0355e7270befec94b77e44c258ca5d3372b08f14f52202
prerequisites:
- architecture.overview
depends_on: []
redirect_from: []
supersedes:
- lua.v5.overview
license: CC-BY-SA-3.0
attribution: CCB contributors; generated contract and source paths at the verified commit.
example_validation_ids: []
api_version: '5'
deprecated: false
deprecation_replacement: null
risk_group: lua-api
risk_level: high
pending_source_pr: null
stale_reason: Contains retired Lua API examples; Lua sections need Platform v1 source verification.
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/character/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/character/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/subsystems/character/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/subsystems/character/
source_repository: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb
source_commit_url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/commit/d32b9cc880a85480840d82cfa05d256c78a16615
source_urls:
- path: data/lua/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/README.md
- path: data/lua/manifest.schema.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/manifest.schema.json
- path: data/lua/types/ccb_api_v5.d.lua
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/types/ccb_api_v5.d.lua
- path: data/lua/reference/ccb_public_api_v5.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5.json
- path: data/lua/reference/ccb_public_api_v5_coverage.json
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/data/lua/reference/ccb_public_api_v5_coverage.json
- path: tools/lua_api/README.md
  url: https://github.com/CrimsonCrossBunker/Cataclysm-Cleanwater-Bomb/blob/d32b9cc880a85480840d82cfa05d256c78a16615/tools/lua_api/README.md
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28subsystems.character%29%3A+&body=Document+ID%3A+subsystems.character%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
search:
  exclude: true
---

> **Lua 内容待修订：** 本页仍含已移除的 v5 接口或旧运行时示例，不可作为当前 Lua 开发依据。请使用 [Platform v1 入门](../api/lua/v1/overview.md)。

# 角色与生物系统技术手册 (Characters & Creatures Manual)

本手册系统性讲解 **Cataclysm: Cleanwater Bomb (CCB)** 中的角色（Character）、玩家（avatar）、非玩家角色（NPC）与怪物（Monster）实体系统、底层运作机制以及供 Mod 调用的核心 API。

---

## 1. 实体体系与生命周期

CCB 的所有生物实体均继承自 `Creature` 核心基类：

* **`Creature`（生物基类）**：提供三维网格坐标（`tripoint`）、基础移动速度（`moves`）、每回合生命恢复、视野感知（`sees`）与伤害结算接口。
* **`Character`（人形角色）**：管理分部位肢体解剖结构（`body_part`）、痛觉、耐力、背包库存与武术技能。
* **`avatar`（玩家实体）**：绑定全局输入管理器与任务日志。
* **`monster`（怪物实体）**：挂载攻击 AI、仇恨度（Aggression）、士气（Morale）与特殊攻击行为树。

---

## 2. 身体部位与生命健康模型 (Body Anatomy)

人形角色（`Character`）的生命值并非单一数值，而是划分为 **12 个独立的身体部位**：

| 部位标识符 (`body_part`) | 部位名称 | 关键影响 |
| :--- | :--- | :--- |
| `"head"` | 头部 | 致命部位，HP 归零直接死亡；受创可能引发脑震荡 |
| `"torso"` | 躯干 | 致命部位，HP 归零直接死亡；影响绝大多数装备的穿戴与负重 |
| `"eyes"` / `"mouth"` | 眼部 / 嘴部 | 影响视野清晰度、感知范围与防毒面具过滤效率 |
| `"arm_l"` / `"arm_r"` | 左臂 / 右臂 | 影响近战武器挥舞速度、持枪瞄准稳定性与格挡效果 |
| `"hand_l"` / `"hand_r"` | 左手 / 右手 | 影响精细手工制作、握持物品能力与敏捷判定 |
| `"leg_l"` / `"leg_r"` | 左腿 / 右腿 | 影响基础移动速度；腿部骨折将大幅增加移动 AP 消耗 |
| `"foot_l"` / `"foot_r"` | 左脚 / 右脚 | 影响复杂地形翻越与奔跑体力消耗 |

---

## 3. 核心 API 参考 (Core APIs)

### `character:get_hp(part) -> integer`

查询指定身体部位的当前生命值。

**参数 (Parameters):**
* `part` (*string*, 必填): 目标身体部位标识符（如 `"head"`, `"torso"`, `"arm_l"`）。

**返回值 (Returns):**
* *integer*: 该部位当前的生命值（HP）。

**实战示例 (Example):**
```lua
-- 检查玩家躯干是否处于重伤状态
local torso_hp = player:get_hp("torso")
if torso_hp < 20 then
    game.add_msg("danger", "你的躯干受到致命重创，急需包扎！")
end
```

---

### `character:mod_pain(amount)`

增减角色的疼痛指数。疼痛会直接削减角色的属性与移动速度。

**参数 (Parameters):**
* `amount` (*integer*, 必填): 疼痛变动值。正数为增加疼痛，负数为减轻疼痛（镇痛）。

> [!TIP]
> **疼痛阈值提示**：当疼痛值超过 `40` 时，角色将出现间歇性失神；超过 `80` 时可能因剧痛休克昏迷。

---

### `character:add_effect(effect_id, duration)`

为角色附加一个状态效果（Buff / Debuff）。

**参数 (Parameters):**
* `effect_id` (*string*, 必填): 效果标识符（例如 `"adrenaline"`, `"bleed"`, `"poison"`）。
* `duration` (*integer*, 必填): 持续时间，**单位：回合数 (turns)**。

**实战示例 (Example):**
```lua
-- 注入兴奋剂，获得 60 回合的肾上腺素激增效果
player:add_effect("adrenaline", 60)
game.add_msg("info", "肾上腺素在血管中奔涌！")
```

---

## 4. 关键事件监听 (Event Hooks)

通过订阅以下原生事件，Mod 可以精确感知角色的生存动态：

```lua
-- 监听角色受到伤害事件
events.on("character_takes_damage", function(event)
    local victim = event.character
    local damage = event.damage
    -- 自定义防具充能或护盾吸收逻辑
end)

-- 监听角色从睡眠中苏醒
events.on("character_wakes_up", function(event)
    game.add_msg("info", "天亮了，你揉了揉惺忪的睡眼。")
end)
```
