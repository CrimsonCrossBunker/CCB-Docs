## 游戏选项与 external options

CCB 的 option 不是单一 JSON registry。菜单选项主要在 `options_manager::add_options` 中注册；
隐藏的 external option 来自 `data/core/external_options.json` 及 Mod 数据，最后由
`options_manager::add_external` 建立具有类型和默认值的内部条目。保存的全局值来自
`config/options.json`，世界级值来自世界目录并可覆盖对应 world option。

读取保存值时，只有已注册的 option 才有意义。`options_manager::deserialize` 先通过
`migrateOptionName`/`migrateOptionValue` 处理旧名称和值，忽略明确移除的旧项，再设置当前条目。
external option 默认总是隐藏；支持的基础类型由 `get_value_type` 决定，包括 bool、int、float、
int_map、string_select 与 string_input。不要把旧文档中的加载顺序当作永久 ABI，应从当前启动、
世界加载和 Mod loader 路径验证。

把菜单项迁移为 external option 时需保存旧存档行为。历史上的 `stub` 方案用于避免 external
definition 覆盖已经设置的值，但具体字段与处理顺序必须和当前 loader 及
`external_options.json` 对照。修改时测试默认值、全局/世界覆盖、旧名称和值迁移、未知/移除项、
Mod load order 与保存后重载；用户可见说明应与菜单 tooltip 同步。
