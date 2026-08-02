## 当前 CCB Monster 契约

`MONSTER` 由 `MonsterGenerator::load_monster` 交给 generic factory，再由 `mtype::load`
解释字段、继承和范围。旧字段表只能作为历史线索；当前 loader、first-party JSON 和
`tests/monster_test.cpp` 才是契约。

### 最小定义与身份

```jsonc
{
  "type": "MONSTER",
  "id": "mon_ccb_example",
  "name": { "str": "example creature" },
  "description": "A creature used by documentation.",
  "default_faction": "wildlife",
  "symbol": "e",
  "color": "light_green",
  "material": [ "flesh" ],
  "species": [ "MAMMAL" ],
  "volume": "62500 ml",
  "weight": "80 kg",
  "hp": 40,
  "speed": 90
}
```

`id` 是 spawn group、mapgen、任务、EOC 和存档引用的稳定标识。`name`、
`default_faction` 与 `symbol` 由当前 loader 强制读取；数值边界、单位和默认值应直接查
`mtype::load`，不要把示例值当成推荐平衡值。

定义 monster 并不会让它出现。自然生成通常还需要 monster group、mapgen/static spawn、
事件或 EOC。`species`、faction、material、harvest、death drops 和 item group 都必须指向
真实注册 ID。

### 行为组合

- `flags`、anger/fear/placate trigger、vision、path settings 和 move skills 控制通用 AI。
- `special_attacks` 可以引用已注册 native attack，也可使用当前 actor 对象；同 subtype
  多次出现需要不同 `id`，否则 loader 会报告覆盖。
- `weakpoint_sets` 先合并具名集合，inline `weakpoints` 最后覆盖同名项；删除也有专门语义。
- `armor`、`melee_damage`、`attack_effs`、`emit_fields` 和 death function 使用各自子契约。
- upgrades、reproduction、revive/zombify/fungalize 与 corpse/egg/baby ID 会影响长生命周期。

`copy-from` 只继承 factory 支持的内容。`extend`、`delete`、`relative` 与 `proportional`
并非对每个字段等价；特别是 armor、weakpoints 和 special attacks 有专门 reader。

### 验证

运行 formatter、`make -j2 json-check` 和真实 Mod 集的 `--check-mods`。再运行
`monster_test` 的相关 filter，并在多 seed 世界检查 spawn、faction、路径、攻击 cooldown、
掉落、死亡、升级/繁殖和保存重载。性能审阅应覆盖高频 special attack、pathfinding、
field emission 和大量群体生成。

字段存在不代表组合可玩；HP、speed、armor、damage、spawn weight 和 loot 必须作为一个
整体做平衡与回归测试。
