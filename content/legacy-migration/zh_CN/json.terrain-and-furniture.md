## 地形、家具与砸击契约

地形和家具的 `bash` 对象由 `map_common_bash_info` 读取共同字段，再分别由
`map_ter_bash_info` 与 `map_furn_bash_info` 读取替换目标。CCB 会把未完成的砸击伤害存到
地图格；达到当前 `str_max`（或 blocked/supported 变体）后替换对象并清除累计伤害。

### 强度与伤害 profile

`str_min` 是每种伤害开始生效时使用的 armor threshold，`str_max` 是对象的有效 HP。
`damage_to()` 对武器的每种 damage type 应用 `bash_damage_profile` multiplier，分别减去
threshold 后只累计正值。profile 未显式列出的合法 damage type 会在 finalize 时使用该类型的
`bash_conversion_factor`；默认 profile 只覆盖 bash，其余类型由 finalize 补齐。

因此旧文档中的“`str_max - str_min` 就是 HP”不再准确。不要只看角色力量或单一 bash
数值推断结果；武器 damage composition、profile、blocked/supported 状态与已有 map damage 都会
影响实际破坏过程。

### 共同字段与替换

- `profile` 引用 `bash_damage_profile`，默认 `default`。
- `str_min_blocked`/`str_max_blocked` 和 `str_min_supported`/`str_max_supported` 是条件替代值。
- `items`、`sound*`、`hit_field`、`destroyed_field`、`explosive` 和 tent/collapse 字段控制副作用。
- terrain 必须提供 `ter_set`；`ter_set_bashed_from_above` 默认跟随它。
- furniture 的 `furn_set` 可省略并默认为 `f_null`。

字段 requiredness 与默认值以三个 loader 为准，不要从现有 JSON 的出现频率反推契约。

### 修改与验证

新增 profile 时必须使用有效 damage type 和非负 multiplier，并让 factory finalize/check 通过。
修改 terrain/furniture `bash` 时同时核对替换 ID、掉落组、字段生成、从上方砸击、支撑/阻挡和
累计伤害重置。运行 JSON formatter、`make -j2 json-check`，并为行为变化扩展
`tests/map_bash_test.cpp` 的 focused case；Mod 组合还要运行真实 `--check-mods`。
