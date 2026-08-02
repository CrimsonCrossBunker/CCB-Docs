## 第一个 JSON mapgen

一个可生成的地点通常横跨三类契约：`mapgen` 画出 reality-bubble tiles，`overmap_terrain`
提供 OMT ID/显示/flags，`city_building`、region settings 或 `overmap_special` 决定如何在世界中
摆放。先选一个当前相近地点并沿 loader 与数据引用追踪，不要复制旧上游路径或把文件名当注册。

### 最小流程

1. 为每个地面/楼层/屋顶定义 overmap terrain ID。
2. 添加 `"type": "mapgen"`，用 `om_terrain` 绑定目标 ID；同 ID 的多个实现通过 `weight`
   参与选择。
3. 在 `object` 中给出 `fill_ter`、定长 `rows`，再用 terrain/furniture/palette 和 placement
   entries 解释符号。行宽和行数必须与该 mapgen grid 匹配；标准单 OMT 尺寸来自当前
   `SEEX/SEEY` 常量。
4. 城市建筑用当前 `city_building`/region registration；野外或多连接地点用
   `overmap_special`。多 z-level 的 point 要保证楼梯、梯子、排水管和屋顶开口对齐。
5. 使用 region groundcover 和现有 palette 时检查其全部继承效果，避免修改共享 palette
   意外改变其他地点。

### 内容与概率

Terrain/furniture symbol 可以共享同一格；未显式 terrain 的格子使用 `fill_ter`。Item、monster、
vehicle、NPC、field、trap、liquid 等 placement 各有独立 required fields、chance/repeat 与坐标
语义，不能从另一个 placement 类型类推。Vehicle mount origin 和 rotation 需要真实生成检查；
monster density 与固定 mapgen spawn 解决不同需求。

### 验证

先运行项目 JSON formatter 与 `make -j2 json-check`，再运行目标 Mod `--check-mods` 和 focused
mapgen tests。在全新未生成的 OMT 上通过 debug 反复生成，覆盖所有 weighted variants、四向旋转、
z-level、城市/特殊位置、季节/region、loot density 与边界连接。检查家具下方 terrain、门窗可达、
屋顶/地下层、车辆不跨 OMT、光照/视线和保存重载。已经生成进存档的 submap 不会因 JSON 修改
自动重建，不能作为新定义的验证样本。
