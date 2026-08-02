## 当前 CCB overmap 数据关系

Overmap 数据分为多种相互引用的对象：`overmap_terrain` 定义 OMT 类型和显示/连接属性，
`overmap_special` 把一个或多个 OMT 组合并规定放置限制，`overmap_connection` 连接道路、
地铁等线性系统，mapgen 再为每个 OMT 生成局部地图。任何一层 ID 不一致都可能到 worldgen
阶段才暴露。

### overmap terrain 与 mapgen

一个 terrain 的稳定 ID 可能在 finalize 后展开为旋转/线性变体；mapgen 使用它的 mapgen ID。
一致性检查会报告没有 mapgen 且没有 uniform terrain 的 OMT，也会检查 static spawn group。
新 terrain 必须同时审阅：

- name、symbol、color、vision 和 flags；
- rotate/LINEAR 及连接方向；
- mapgen ID、uniform terrain、roof/地下层关系；
- monster density、extras 和位置 flag；
- 已发布 ID 对任务目标、存档与 Mod 的兼容性。

不要手写带方向后缀的引用并假定所有匹配场景相同；需要精确、type、subtype、prefix 或
contains 匹配时，以调用字段的当前 `ot_match_type` 语义为准。

### overmap special

fixed special 通过 `overmaps`/connections 组合 OMT；mutable special 使用另一套生成数据。
`occurrences` 是真实 `overmap_special` 的必填放置约束，city size/distance、locations、flags、
priority、rotation 和连接共同决定是否能放置。一个 special 在空白测试世界可放置，不代表
在已有城市、道路、其他 special 和 region blacklist 竞争下总能成功。

Special 可以绑定 inline EOC、参数、spawn 和 mapgen；多格结构的坐标、旋转中心、z-level
及连接端点必须成套验证。迁移已发布 special ID 时使用当前 migration 对象和存档测试。

### connection 与区域关系

`overmap_connection` 描述可连接 terrain 及规则；region settings 再选择城内/城间道路、
trail、sewer、subway 与 rail connection。改变 connection 或 region 引用可能重塑新 overmap，
但不会自动重写已生成区域，形成新旧存档差异。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod 集 `--check-mods` 和 `overmap_test` 相关
用例。至少生成多个 seed/region，检查 special occurrence、旋转、道路连接、边界、z-level、
任务目标和无可放置位置；对已发布 ID 做旧存档加载。

局部 tile 布局见[mapgen](mapgen.md)，宏观分布参数见[region settings](region-settings.md)。
