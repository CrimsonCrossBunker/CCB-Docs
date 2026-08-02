## Dimension region layout

`dimension_region_layout` 决定一个 dimension 的 overmap 使用哪个 `region_settings`。当前
loader 必须读取 `generation_mode`，但 pinned CCB 实现的 switch 只为 `UNIFORM` 创建 generator；
JSON 枚举或头文件中出现其他 mode 不等于它们可用。

### 当前支持的模式

`UNIFORM` 是 dynamic layout，并要求 `uniform_region`。第一次访问某个 overmap 时 generator
把该坐标映射到同一个 region。当前第一方 `dimension_regions.json` 也全部使用这一模式。

头文件保留 MANUAL_VORONOI、RANDOM、EIGHTHS 与 static layout 的类型和部分基类，但 loader
没有对应 case。不要发布使用这些值的 Mod，也不要把未接线的 `generated_bounds_*` 或
`layout_out_of_bounds` 当成公开 JSON 契约。要启用新模式，必须先实现 deserialize、generator、
factory finalize/check 与测试，而不只是放开枚举。

### ID 链与验证

layout 的 `uniform_region` 必须是有效 region settings，`dimension.region_layout` 再引用这个
layout。检查完整链：dimension → layout → region settings → overmap generation 数据。

运行 formatter、`make -j2 json-check` 和完整 `--check-mods`，实际创建新 world/dimension 并生成
多个 overmap。对新 generator 加 deterministic seed、边界、存档 reload 与无效 ID fallback
测试；region layout 变化可能改变新生成世界，必须在 PR 标明兼容性影响。
