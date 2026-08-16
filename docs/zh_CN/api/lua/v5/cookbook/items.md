---
# GENERATED FROM docs-catalog.yml. DO NOT EDIT THIS BLOCK.
id: api.lua.cookbook.items
title: 纯 Lua 装备与容器口袋实战
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
translation_source_fingerprint: a72760fa18c5e8777dd154d3157780468424dec30614b3b5569e143bbf693b25
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
canonical_url: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/items/
alternate_urls:
  zh: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/items/
  en: https://crimsoncrossbunker.github.io/CCB-Docs/en/api/lua/v5/cookbook/items/
  x-default: https://crimsoncrossbunker.github.io/CCB-Docs/api/lua/v5/cookbook/items/
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
documentation_issue_url: https://github.com/CrimsonCrossBunker/CCB-Docs/issues/new?title=docs%28api.lua.cookbook.items%29%3A+&body=Document+ID%3A+api.lua.cookbook.items%0ALanguage%3A+zh_CN%0AVerified+commit%3A+d32b9cc880a85480840d82cfa05d256c78a16615%0A%0ADescribe+the+documentation+problem%3A%0A
---

# 纯 Lua 装备与容器口袋实战 (Items & Pockets Cookbook)

在 **CCB Lua 0.1** 体系中，Mod 作者可以完全告别静态 JSON 描述，直接在 Lua 中以面向对象和数据流的方式定义游戏中的所有装备、武器、防具与容器。

---

## 1. 核心概念与生命周期

在 CCB 中，物品（Item）的定义具有以下核心特性：
1. **纯代码注册**：在 Mod 的 `main.lua` 或子模块中，通过 `game.items.register()` 注册物品原型。
2. **Pocket 容器模型**：CCB 彻底淘汰了单层背包逻辑，所有物品都具备口袋（Pocket）树状嵌套能力。
3. **动态属性计算**：物品的重量、容积与耐久度在运行时动态递归计算，支持运行时修改与状态挂载。

---

## 2. 实战一：纯 Lua 定义一把战术近战武器

以下示例展示如何定义一把带有自定义攻击判定和特殊材质属性的高频振动短剑：

```lua
-- mods/tactical_weapons/items/vibro_blade.lua
local items = {}

function items.register_weapons()
    game.items.register({
        id = "ccb_vibro_blade",
        name = "高频振动战术短剑",
        description = "一把内置微型超声波发生器的轻量化钛合金短剑，能够轻松切开重型装甲。",
        weight = 850, -- 单位: 克 (g)
        volume = 750, -- 单位: 毫升 (ml)
        price = 4500, -- 交易价值 (美分)
        category = "weapons",
        material = { "titanium", "plastic" },
        symbol = "/",
        color = "light_cyan",
        
        -- 近战属性
        melee = {
            damage = {
                cut = 28,      -- 斩击伤害
                pierce = 14,   -- 穿刺伤害
                bash = 4,      -- 钝击伤害
            },
            attack_cost = 75, -- 攻击消耗的基础动作点数 (AP)
            to_hit = 2,       -- 命中加成修正
        },
        
        -- 武器特性与标签
        flags = {
            "SHEATH_KNIFE",   -- 可插入战术刀鞘
            "UNBREAKABLE_MELEE", -- 近战攻击极不易损坏
            "CONDUCTIVE",     -- 导电材质
        },
        
        -- 自定义使用动作 (IUSE Callback)
        on_use = function(character, item)
            game.add_msg("info", "你按下了短剑握把上的开关，刀刃发出微弱的高频蜂鸣。")
            -- 消耗能量电池或激活附带状态
            return true
        end
    })
end

return items
```

---

## 3. 实战二：定义多功能战术背包（Pocket 容器嵌套模型）

CCB 的每个容器都由一个或多个 `pocket` 组成。每个口袋可以独立限制**最大容积、最大承重、开口尺寸与材质防漏**：

```lua
function items.register_backpack()
    game.items.register({
        id = "ccb_tactical_rig",
        name = "模块化战术胸挂背包",
        description = "专为快速交火设计的模块化胸挂，配备主仓、杂物副仓与防水密封水袋仓。",
        weight = 1200,
        volume = 2000,
        category = "armor",
        symbol = "[",
        color = "dark_gray",
        
        -- 防具属性 (穿戴在躯干)
        armor = {
            covers = { "torso" },
            coverage = 65,      -- 躯干覆盖率 65%
            encumbrance = 12,   -- 穿戴累赘度 12
            warmth = 5,         -- 保暖度
            protection = {
                cut = 8,
                bash = 6,
                ballistic = 12, -- 防弹性能
            }
        },
        
        -- 多口袋容器架构 (Pocket Definitions)
        pockets = {
            -- 1. 主储物仓
            {
                pocket_type = "CONTAINER",
                max_contains_volume = 12000, -- 最大可容纳 12 升
                max_contains_weight = 15000, -- 最大可承重 15 公斤
                max_item_length = 450,       -- 限制物品最长尺寸 (mm)
                rigid = false,               -- 非刚性（装满后体积膨胀）
            },
            -- 2. 快速拔取弹匣副仓
            {
                pocket_type = "CONTAINER",
                max_contains_volume = 1500,
                max_contains_weight = 2000,
                moves = 30,                  -- 快速拔取动作点 (比主仓快 50%)
                item_restriction = { "magazine", "ammo" }, -- 仅限弹匣与弹药
            },
            -- 3. 密封防水水袋仓
            {
                pocket_type = "CONTAINER",
                max_contains_volume = 3000,  -- 3 升液体
                watertight = true,           -- 100% 气密与防水
                open_container = false,      -- 带封口防泼溅
            }
        }
    })
end
```

---

## 4. 实战三：自定义药物与食用效果（带有事件联动）

```lua
function items.register_stims()
    game.items.register({
        id = "ccb_adrenaline_shot",
        name = "军用肾上腺素注射器",
        description = "一次性自动注射器，瞬间大幅提升移动速度和疼痛耐受度，但随后会带来脱水与虚脱副作用。",
        weight = 80,
        volume = 100,
        category = "drugs",
        
        -- 食用/使用逻辑
        on_use = function(character, item)
            -- 1. 降低疼痛
            character:mod_pain(-30)
            -- 2. 增加临时兴奋剂点数
            character:mod_stim(40)
            -- 3. 挂载自定义持续效果
            character:add_effect("adrenaline", 120) -- 持续 120 回合
            
            game.add_msg("warning", "剧烈的刺痛从手臂蔓延，你的心脏开始狂跳，感官瞬间变得无比清晰！")
            
            -- 4. 消耗该物品
            return true
        end
    })
end
```

---

## 5. 调试与加载验证

在你的 Mod 根目录下：
```lua
-- main.lua
local items = require("items/vibro_blade")

events.on("game_load", function()
    items.register_weapons()
    items.register_backpack()
    items.register_stims()
end)
```

启动游戏后，在调试菜单（Debug Menu -> Spawn Item）中搜索 `ccb_vibro_blade` 即可直接生成并测试该物品！
