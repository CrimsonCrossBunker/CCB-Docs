---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.cookbook.monsters
title: 纯 Lua 怪物与技能 AI 实战
language: zh_CN
status: active
doc_type: tutorial
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
include_in_search: true
include_in_ai_index: true
translation_status: current
translation_stale_since: null
translation_source_fingerprint: 8468deb56a88c844b6b5dd023fde5a7181e14c5b6d601365334d9201c4e68771
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
stale_reason: null
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/monsters/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/monsters/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/cookbook/monsters/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/monsters/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.cookbook.monsters%29%3A+&body=Document+ID%3A+api.lua.cookbook.monsters%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 纯 Lua 怪物与技能 AI 实战 (Monsters & AI Cookbook)

在 **CCB Lua 0.1** 体系中，Mod 作者可以不编写任何 JSON，直接用纯 Lua 代码定义全新的怪物物种、AI 行为策略与动态特殊攻击。

---

## 1. 怪物系统核心概念

在 CCB 引擎中，怪物（`monster`）继承自 `Creature` 基类：
1. **纯 Lua 实体注册**：通过 `game.monsters.register()` 注册原型。
2. **动态 AI 钩子与技能**：特殊攻击（`special_attacks`）以 Lua 闭包形式直接挂载在怪物实例上，支持精准的范围判定、投射物生成与视线检测。
3. **伤害与抗性系统**：每个怪物都可以具备独立的钝击、斩击、子弹、强酸、电击抗性与环境适应性。

---

## 2. 实战一：定义变异掠食者怪物

以下代码定义了一只具备敏捷移动、隐匿潜行和飞扑撕咬能力的变异潜伏者：

```lua
-- mods/mutant_threats/monsters/stalker.lua
local monsters = {}

function monsters.register_stalker()
    game.monsters.register({
        id = "ccb_mutant_stalker",
        name = "变异暗影潜伏者",
        description = "一种高度特化的掠食生物，身体覆盖着吸收光线的黑色几丁质甲壳，擅长从阴影中发动致命飞扑。",
        symbol = "s",
        color = "dark_gray",
        size = "MEDIUM",
        species = { "MUTANT", "NETHER" },
        
        -- 生存与战斗基础数值
        hp = 160,
        speed = 135,          -- 基础移动速度 135 (比普通人类快 35%)
        aggression = 80,      -- 高侵略性 (主动猎杀)
        morale = 95,          -- 极高士气 (受重伤前不会轻易逃跑)
        diff = 24,            -- 危险等级评分
        
        -- 护甲与抗性防御
        armor = {
            bash = 8,
            cut = 18,         -- 几丁质坚硬外壳，高度抗斩击
            bullet = 12,
            acid = 4,
            electric = 0,     -- 弱电
        },
        
        -- 基础近战攻击
        melee = {
            skill = 6,
            dice = 3,
            sides = 8,
            damage = {
                cut = 12,
                pierce = 8,
                bash = 4,
            },
            effects = {
                { id = "bleed", duration = 30 } -- 攻击附带流血
            }
        },
        
        -- 怪物生物特性 Flags
        flags = {
            "SEES",           -- 具备视力
            "HEARS",          -- 具备听力
            "SMELLS",         -- 具备嗅觉追踪
            "WARM",           -- 温血生物 (可被红外夜视发现)
            "CLIMBS",         -- 可以翻越障碍物
            "NIGHT_VISION",   -- 完美夜视
        },
        
        -- 特殊攻击与技能机制 (Special Attacks)
        special_attacks = {
            -- 技能 1: 飞扑撕咬 (Pounce & Rend)
            {
                name = "shadow_pounce",
                cooldown = 8, -- 8 回合冷却
                condition = function(monster, target)
                    local dist = monster:pos():distance_to(target:pos())
                    -- 目标在 2 到 4 格距离内，且视线无阻挡时触发飞扑
                    return dist >= 2 and dist <= 4 and monster:sees(target)
                end,
                execute = function(monster, target)
                    game.add_msg("danger", "%s 压低身体，化作一道残影飞扑向 %s！", monster:get_name(), target:get_name())
                    -- 瞬间位移到目标邻近格
                    monster:set_pos(target:pos():nearest_empty_neighbor())
                    -- 造成额外穿刺撕裂伤害
                    target:apply_damage(monster, "pierce", 26)
                    target:add_effect("stunned", 1) -- 击晕 1 回合
                end
            }
        },
        
        -- 死亡掉落与解剖收获
        death_drops = {
            items = {
                { id = "meat", count = { 4, 8 }, prob = 1.0 },
                { id = "bone", count = { 6, 12 }, prob = 1.0 },
                { id = "chitin_piece", count = { 3, 6 }, prob = 0.8 },
            }
        }
    })
end

return monsters
```

---

## 3. 实战二：编写带召唤与光环的 Boss 级怪物

```lua
function monsters.register_broodmother()
    game.monsters.register({
        id = "ccb_broodmother",
        name = "寄生母体巢穴",
        symbol = "B",
        color = "magenta",
        size = "LARGE",
        hp = 650,
        speed = 70,
        
        -- 每回合 Tick 时的光环逻辑 (Turn Update Hook)
        on_turn = function(monster)
            -- 周期性散发神经毒雾
            if game.time.turn() % 10 == 0 then
                local center = monster:pos()
                map.create_cloud("gas_neurotoxin", center, 3, 50)
            end
        end,
        
        special_attacks = {
            {
                name = "spawn_larvae",
                cooldown = 15,
                execute = function(monster, target)
                    game.add_msg("warning", "%s 的腹部剧烈蠕动，释放出数只幼虫！", monster:get_name())
                    for i = 1, 3 do
                        local spawn_pt = monster:pos():random_empty_neighbor()
                        if spawn_pt then
                            map.spawn_monster("ccb_mutant_larva", spawn_pt)
                        end
                    end
                end
            }
        }
    })
end
```

---

## 4. 验证与生成测试

在 Mod 的 `main.lua` 中加载该模块：
```lua
local monsters = require("monsters/stalker")

events.on("game_load", function()
    monsters.register_stalker()
end)
```
进入游戏后，在调试菜单中选择 `Debug Menu -> Spawn Monster`，输入 `ccb_mutant_stalker` 即可直接召唤该生物进行战斗测试！
