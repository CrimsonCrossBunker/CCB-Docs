## Movement mode 契约

`move_mode` 是 generic factory 对象。当前 loader 强制读取显示字符/名称、panel character、
`exertion_level`、步行/骑乘/机甲的 prepare 与成功消息，以及 `move_type`。`move_type` 只接受
当前注册的 prone、crouching、walking、running 语义；显示名称不是行为类型。

### 速度、体力和循环

`move_speed_multiplier`、`stamina_multiplier`、`sound_multiplier`、`swim_speed_mod`、
`mech_power_use` 和 `stop_hauling` 影响不同子系统。倍率不是独立平衡旋钮：terrain move cost、
encumbrance、mount、stamina、noise 和 effect 会继续参与最终结果。

Finalize 按 move-speed multiplier 排序并建立正向/反向 cycle。新增模式可能改变所有玩家的
循环顺序，即使没有修改现有 ID；相同 multiplier 的稳定顺序也不应当作 UI 契约。

### 文本和载具

prepare/change message 分别覆盖徒步、animal 和 mech；失败消息有默认值但不应依赖占位的
“bugs”文本发布。字符和 panel symbol 必须是合法 Unicode；颜色由当前 color reader 解析。
骑乘 exertion 可独立设置，不能用步行测试推断。

### 验证

运行 formatter、`make -j2 json-check`、`--check-mods` 和 movement/stamina/sound/vehicle
focused tests。覆盖 cycle 两个方向、UI symbol、prone/crouch/run 切换失败、hauling、swim、
animal/mech power、负重/terrain、保存重载与翻译。记录实际 move、stamina 和 sound，而不只
检查 JSON 能加载。
