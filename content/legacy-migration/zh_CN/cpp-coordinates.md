## 当前 CCB 坐标类型

CCB 用类型同时编码维度、原点与水平尺度，避免把“现实气泡内 tile”误传为“世界绝对 OMT”。
类型别名以 `(tri)point_<origin>_<scale>[_ib]` 命名，并由 `coords_fwd.h` 和
`coordinates.h` 定义。

### 原点、尺度与轴

- `rel` 是相对偏移；`abs` 是全世界绝对原点。
- `sm`、`omt`、`om` 分别相对 submap、overmap terrain、overmap 左上角。
- `bub` 相对当前 reality bubble；它会随地图载入/角色位置变化。
- `ms`、`sm`、`omt`、`seg`、`om` 分别表示 map square 到 overmap 的单位。
- `point` 是 2D，`tripoint` 包含 z；`_ib` 表示对相应局部原点保证 in-bounds。

x 向屏幕右、y 向屏幕下、z 正值向上。水平尺度变化不会缩放 z。当前常量由
`SEEX/SEEY`、`OMAPX/OMAPY` 等源码定义，不把旧文档数字复制为永久契约。

### 选择和转换

新代码尽量使用 `tripoint_abs_ms`、`tripoint_bub_ms`、`point_abs_omt` 等 typed point；
只有真正没有游戏尺度的数学数据才用 raw `point`/`tripoint`。函数签名应公开需要的原点和
尺度，让错误在编译期出现。

```cpp
tripoint_abs_ms absolute = get_map().getglobal( local );
tripoint_bub_ms local_again = get_map().bub_from_abs( absolute );
point_abs_omt omt = project_to<coords::omt>( absolute.xy() );
```

同一原点改尺度用 `project_to`。向粗尺度投影且需要余数时用 `project_remain`，重组用
`project_combine`。绝对与 bubble 坐标转换必须经过具体 `map`；vehicle mount/rotated
坐标使用 `vehicle::coord_translate`/`mount_to_tripoint` 系列，不做手工旋转和偏移。

### 运算与 sentinel

只有语义成立的类型组合才支持加减：绝对位置加相对 offset 有意义，两个绝对位置相加没有。
distance 需要明确选 `square_dist`、`trig_dist`、`rl_dist` 或 `manhattan_dist`。
`zero` 是原点，`invalid`/`is_invalid()` 是失败 sentinel；不要把 `zero` 当“未设置”。

存档字段必须序列化能跨 reality-bubble 移动的坐标。NPC 或可中断 activity 的目标通常保存
absolute coordinate，而不是 avatar-relative bubble coordinate。

### 验证

编译受影响 translation unit，运行 `point_test`/`coordinate_test` 相关 filter，并覆盖负
坐标、submap/OMT 边界、z-level、map shift、vehicle rotation 与 serialize/deserialize
round trip。clang-tidy 的 point checks 是迁移帮助，不替代边界测试。
