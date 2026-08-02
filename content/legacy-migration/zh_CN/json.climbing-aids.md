## Climbing aid 契约

`climbing_aid` generic factory 按 condition category + flag 建立 lookup。顶层 `down` 与
`condition` 必填，`slip_chance_mod` 可选。项目还要求有效 `default` entry；缺失时运行时虽会构造
fallback，但 consistency check 会报告。

### Condition

type 必须是 special、ter_furn、veh、item、character 或 trait，flag 必填。item condition 还要求
uses；ter_furn 可设置 range（默认 1）；其他 category 不读取这些专用字段。uses 表示使用时消耗的
item 数量，condition 检测和 route scan 决定 aid 是否可用。

### Down rules

max_height 默认 1，设为 0 禁止向下；allow_remaining_height 默认 true，easy_climb_back_up 默认 0。
启用时 menu_text 与 confirm_text 必填。设置 deploy_furn 后，menu_cant 和单字节 menu_hotkey 也
必填；否则二者可选且 hotkey 最多一个字节。cost 的 kcal、thirst、damage、pain 按下降层数应用。

部署 furniture 必须验证开放空气、已有 furniture/vehicle/creature、max height 和部分下降行为。
当前 menu 通常列出全部 deployable aids 与最安全的 non-deploy aid；slip modifier 会影响选择，不是
孤立显示数字。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`。在多 Z-level fixture 覆盖向下高度、
部分下降、item 消耗、部署碰撞、veh part length、terrain flag、trait/character condition、滑落、
体力/伤害 cost 与返回难度。新增边界需要 climbing focused tests 和存档 reload 检查。
