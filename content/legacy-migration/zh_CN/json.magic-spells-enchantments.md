## 当前 CCB Magic、Spell 与 Enchantment 契约

这组契约包含 `SPELL`、`magic_type`、`enchantment` 和在其他对象中使用的 inline
`fake_spell`。它们共享部分 ID 和条件，但 lifecycle 不同：spell 被施放，magic type
提供系统默认规则，enchantment 按持有者/载体状态持续求值。

### Spell 最小骨架

```jsonc
{
  "type": "SPELL",
  "id": "spell_ccb_example",
  "name": "Example pulse",
  "description": "A documentation-only spell.",
  "effect": "attack",
  "shape": "blast",
  "valid_targets": [ "hostile" ],
  "min_damage": 1,
  "damage_increment": 1,
  "max_damage": 5,
  "min_range": 3,
  "max_range": 3,
  "energy_source": "MANA",
  "base_energy_cost": 10,
  "base_casting_time": 100
}
```

当前 `spell_type::load` 强制读取 `name`、`description`、`effect`、`shape` 与
`valid_targets`。Effect 和 shape 必须在 native registry 中存在。damage、range、AoE、
duration、pierce、accuracy、energy 和 casting time 通常使用 min/increment/max；表达式和
单位由对应 reader 决定，不能假定全是普通整数。

`caster_condition`、`target_condition`、target species/monster、body parts 和 flags 共同
限制合法目标。`extra_effects`/`fake_spell` 可以连锁施法，consistency check 会检查循环；
WONDER、permanent summon、vitamin energy、touch/no-hands 与 formula 参数也有专门约束。

### Magic type、学习与 channel

`magic_type` 可集中声明 energy、level/XP/failure formula、cannot-cast flags、failure cost
和 failure EOC。level 与 XP formula 必须成对且参数数目正确。Spell 可以覆盖 magic type，
并通过 book、profession/NPC、`learn_spells` 或其他当前入口学习。

Channeled spell 需要 max turns、channel spell 与 end spell；interrupt、每回合耗能和重复
effect 必须覆盖取消、移动、受击、资源耗尽和保存边界。多 projectile 与重复/随机
extra spell 需要性能和递归上限审阅。

### Enchantment

Enchantment 可以是具名 ID，也可以在调用者能提供稳定 inline ID 时内联。`has` 与
`condition` 决定 HELD/WIELD/WORN、ACTIVE/INACTIVE/ALWAYS 或 dialogue condition。
`values`、skills、custom、encumbrance、melee/incoming damage 支持 add/multiply；
mutations、effects、bodypart changes、special vision、emitter、hit effects 和 intermittent
spell 各有独立语义。

Character、monster 与 vehicle 只处理其实现认为 relevant 的子集。不要因为字段能加载就
假设对所有载体生效；用 `is_monster_relevant`/`is_vehicle_relevant` 和调用点查证。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod 集 `--check-mods`，以及
`magic_spell_test`、`magic_spell_effect_test`、`enchantments_test` 的相关 filter。
覆盖每个 level 边界、失败率/资源、target/shape、extra-effect cycle、channel 中断、
enchantment 开关与 add/multiply 顺序，并保存重载。玩家/NPC/monster/vehicle 和 inline
载体分别测试；高频 intermittent/area spell 需要 profile。
