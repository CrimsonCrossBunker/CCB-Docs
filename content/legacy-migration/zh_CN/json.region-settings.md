## 当前 CCB region settings 结构

Region settings 决定新 overmap 的默认 terrain、地表、森林/河流/湖海、城市、道路连接、
highway、map extras、天气和 feature flag 筛选。它不是一个可以任意添加字段的大对象：
多个 `region_settings_*` object type 由各自 factory 加载，再由主 `region_settings` 通过 ID
引用组合。

### 主 region

主对象读取 default OMT/groundcover、cities（必填）、weather、forest、river、lake、ocean、
highway、ravine、connections、map extras 与 terrain/furniture 替换等组件，并控制是否放置
road、railroad、special 和邻接连接。默认 region 的 `id: "default"` 必须有效，否则 finalize
会报告。

不要从旧表猜组件字段：例如 `region_settings_city` 当前强制 `city_size`，forest、highway、
lake、map-extra collection 都有自己的 reader、默认值和稳定 ID。

### 扩展与覆盖

```jsonc
{
  "type": "region_settings",
  "id": "default",
  "copy-from": "default",
  "feature_flag_settings": {
    "extend": { "blacklist": [ "CCB_EXCLUDED" ] }
  }
}
```

`copy-from`/extend 的具体支持取决于该字段的 reader。相同 ID 的 Mod patch 依赖加载顺序；
多个 Mod 修改 default region 时可能互相覆盖。为独立世界规则建立新 region 通常比隐式修改
所有世界更易审阅，但仍需确认世界选择入口与 dimension/layout 引用。

### 城市、extras 与 feature flags

城市 weighted lists 引用 OMT 或 special；半径/size/spacing 控制宏观分布，不保证每个候选
都能放置。Map extra collection 用 chance 和权重引用已注册 extra。feature blacklist/
whitelist 与 overmap location flags 共同过滤内容；过严组合可能产生空候选或断路。

Region 修改只影响尚未生成的 overmap。玩家走过的区域不会自动重建，因此任何视觉、资源
或道路变化都要分别描述“新世界/新区域”和“旧存档已生成区域”的行为。

### 验证

运行 formatter、`make -j2 json-check` 和实际 Mod 集 `--check-mods`。用多个 seed 生成完整
overmap，记录所选 region，检查城市/道路、森林水体、special、extras、天气和黑白名单；
同时加载旧世界并跨越到新 overmap，确认边界和连接可接受。

具体 OMT/special 关系见[overmap](overmap.md)，局部生成见[mapgen](mapgen.md)。
