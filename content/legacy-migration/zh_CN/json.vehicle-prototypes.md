## Vehicle prototype 契约

`vehicle` prototype 用来生成 stock vehicle；生成后的车辆使用另一套存档表示。prototype 的
`id` 来自 generic factory，`parts` 是核心结构，`name`、`items`、`zones` 和 `color_palette`
可选；`blueprint` 当前只为兼容读取，不驱动生成。

### Parts 与安装顺序

每个 part group 必须有 `x`、`y` 和 `parts`。元素可以是 `vpart_id` 字符串，也可以是带
`part` 的对象；对象还可设置 0–100 的 `ammo`、`ammo_types`、`ammo_qty`、`fuel` 和 `tools`。
`part#variant` 在两种形式中都由最后一个 `#` 分割。

数组顺序就是安装顺序，必须满足游戏中的 frame、mount、wheel、engine、turret 等安装前置和
stacking 规则。同坐标可分多组追加，但不能借此绕过安装约束。有限的 copy-from 会先继承父项，
再追加 parts/items/zones；检查最终展开结果，而不是只看子对象。

### Items、zones 与导出

item spawn 要求 `x`、`y`、0–100 `chance`；可给 `items`、`item_groups`、`magazine` 和
`ammo`。item 可用字符串或 `{ "id", "variant" }`。zone 要求 type/x/y，并可有 name/filter；
只有车辆拥有 faction owner 时才实际放置。

Debug exporter 可生成 parts、部分 turret/fuel/tool、简单 cargo items、zones 与视觉 blueprint，
但会留下 placeholder id/name，且不保证复杂容器和 comestible round-trip。输出必须格式化并
人工审阅。

### 验证

运行 formatter、`make -j2 json-check` 与目标 Mod 的 `--check-mods`。新增复杂 prototype 时在
游戏中生成并检查 refresh、安装顺序、cargo、owner zones 与 palette。若修改 exporter 或字段，
扩展 `tests/vehicle_export_test.cpp` 的序列化后重新 load 等价测试。
