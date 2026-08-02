## 当前 CCB effect_type 数据

`effect_type` 定义附着在角色/生物上的持续状态，例如名称、描述、强度、持续时间、免疫、
数值修饰和周期行为。它与 Effect on Condition 的“effect command”不是同一对象：EOC 可以
添加/移除某个 effect_type，但 `effect_type` 本身不是可执行脚本。

### 基础定义

```jsonc
{
  "type": "effect_type",
  "id": "ccb_example_status",
  "name": [ "Example status" ],
  "desc": [ "You are affected by the documentation example." ],
  "max_intensity": 3,
  "max_duration": "1 hour",
  "show_in_info": true
}
```

`load_effect_type` 要求稳定 `id`，并读取多强度 name/desc、显示字段、resist/immune/block/
remove 关系、duration/intensity 演化、消息、flags、enchantment 和 modifier data。数组索引
与 intensity 的对应、缺省回退和 hardcoded 行为要以 `effect.cpp` 与测试为准。

### 实例生命周期

运行时 `effect` 实例保存 effect type、duration、body part、permanent、intensity、开始时间
与来源，并进入存档。因此删除或重命名已发布 effect ID 是存档兼容变化；需要使用
`effect_migration`：

```jsonc
{
  "type": "effect_migration",
  "from": "old_effect_id",
  "to": "ccb_example_status"
}
```

省略 `to` 是否代表移除、以及迁移触发时机，应由当前 loader/反序列化测试确认。目标 ID
不存在会在一致性检查中报告。

### 强度、持续时间与 modifier

`max_intensity`、`int_add_val`、decay 字段与 `int_dur_factor` 共同决定叠加和衰减。`base_mods`
和 `scaling_mods` 下的 STR/DEX/PER/INT、速度、疼痛、伤害、睡眠等条目由
`effect_type::load_mod_data` 的固定映射解释，并不是自由命名属性。错误的 chance/tick/min/
max 组合可能制造每回合高成本或极端数值。

身体部位限制、resist trait/effect、immune flag、blocks/removes 关系会改变能否施加和共存。
循环关系和强度边界需要 focused test，不应只看状态栏文本。

### 验证

1. 从 `load_effect_type` 和相邻第一方 effect 确认字段形状与强度数组。
2. 运行 formatter、`make -j2 json-check` 和实际 Mod 集 `--check-mods`。
3. 运行 `effect_test`/`creature_effect_test` 相关用例，覆盖施加、叠加、衰减、免疫与移除。
4. 对已发布 ID 测试旧存档/`effect_migration`，不要静默改名。
5. 对周期 modifier 测试强度 1、上限、超时和不同 body part。

若目标是执行条件逻辑，请使用[EOC](../eoc/index.md)；不要把脚本副作用塞进状态数据。
