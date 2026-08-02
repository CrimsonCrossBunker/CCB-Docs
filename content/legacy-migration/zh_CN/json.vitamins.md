## `vitamin` 对象不是只表示营养素

CCB 的 `vitamin` registry 是角色体内随时间变化的通用量系统。`vit_type` 当前接受 `vitamin`、`toxin`、
`drug` 和 `counter`；第一方数据除钙、铁、维生素 C 外，还用它表示药物剂量、mutagen primer、血量相关
计数、过敏原和其他隐藏状态。不要因对象类型名推断其一定会出现在营养 UI。

### Loader 字段

除 generic-factory 所需的 `id`/`type` 外，新定义必须提供 `name`、`vit_type`、`min` 和 `rate`；`max`
可省略且当前默认 `0`。`deficiency` 与 `excess` 引用 effect type；`disease` 与 `disease_excess` 是数量范围
数组，依顺序映射 effect intensity。`weight_per_unit` 允许把质量换算为内部单位。`decays_into` 的每项是
目标 vitamin ID 与增减量，自然代谢一个单位时分别应用。`flags` 是字符串集合，其具体消费者要从当前
代码和数据确认。

```json
{
  "type": "vitamin",
  "id": "example_counter",
  "vit_type": "counter",
  "name": { "str": "Example counter" },
  "min": 0,
  "max": 100,
  "rate": "1 h",
  "excess": "example_effect",
  "disease_excess": [ [ 10, 49 ], [ 50, 100 ] ]
}
```

这是结构示例，不是待添加的第一方 ID。阈值的起止顺序可由 loader 处理，但范围重叠或空洞仍会产生难以
理解的结果；设计时应使用连续、可测试的区间。

## 继承、单位和验证

Vitamin 通过 `generic_factory` 支持 `copy-from`。当前测试覆盖 scalar override，以及对 `flags`、`disease`、
`disease_excess`、`decays_into` 的 `extend`/`delete`。`flags` 作为 set 去重；重复目标的 `decays_into`
条目保持为独立规则，不会自动求和。覆盖已有 `id` 时最后加载定义生效，因此 Mod 必须评估跨加载顺序兼容。

营养型数据在 JSON food 中常以 RDA 百分比表示，其他类型使用内部单位；`rate` 决定每日吸收/衰减换算，
`weight_per_unit` 决定质量换算。新增对象应运行 JSON formatting/loading、vitamin consistency 和
`[vitamin]` 专项测试，并覆盖 effect ID、边界数量、继承、自然衰减、简化营养、显示 flags、摄入延迟及
保存重载。不要把旧 MME 表或第一方数值复制为永久 Schema。
