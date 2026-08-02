## Dimension 定义与切换

`dimension` object 只读取 `region_layout`；finalize 时无效引用会报告并退回 `default`。运行时把
非主 dimension 的 world 数据放在 save 的 dimension 区域，并在 travel 时切换当前加载的数据。
这不是可从未加载 dimension 任意读写地图的远程 API。

### 数据与 EOC 边界

定义新 dimension 时同时提供有效 `dimension_region_layout` 及其 region settings。当前 layout
实现只支持 UNIFORM；先验证 layout 页面中的实现边界。

`u_travel_to_dimension` 负责切换。`npc_travel_radius` 默认 0，filter 默认 `all`；当前 consumer
解析 filter 和半径后选择同行 NPC。`item_travel_radius` 默认 -1（不搬运），可用
`target_location` 改变收集与放置中心；还存在 vehicle 选项。字段、默认值与允许 filter 必须以
EOC registry 和 `talk_effect_fun::f_travel_to_dimension` 为准，旧片段只作示例。

`clear_dimension` 会清除对应 dimension 的持久化世界数据，之后再次进入会重新生成。这会丢失
其中的地图、物品、车辆、怪物、NPC 等状态，属于破坏性作者功能；不要把它当成普通传送清理。

### 安全工作流

先在 travel 前保存所需 location variable，再切换，再对已加载 dimension 做 mapgen update 或
teleport。不要在旧 dimension 卸载后继续使用其 bubble coordinate，也不要假设两个 dimension
的同坐标代表同一地点。

运行 formatter、`make -j2 json-check` 和 Mod `--check-mods`。用临时世界覆盖首次创建、往返、
存档 reload、NPC/item/vehicle 边界、无效 layout fallback 与 clear 后再生；不要在珍贵存档测试
`clear_dimension`。
