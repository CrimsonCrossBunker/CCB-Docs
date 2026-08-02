## Item aesthetic variants

item 的 `variants` 是同一 itype 的表现变体，不是另一个 gameplay item。每项必须有稳定 `id`，
并可覆盖 name、description、symbol、color、ascii picture；`weight` 默认 1，`append` 控制说明追加，
`expand_snippets` 控制生成时展开。缺少 name/description 时 finalize 从 base item 继承。

这套 `itype_variant_data` 不等于 C++ 的 `cata_variant` typed value container，二者名称相近但契约
无关。写文档、测试和 source symbol 时必须明确是哪一种。

### 适用边界

variant 只能表达视觉、命名或文字差异，不能改变重量、伤害、营养、armor、pocket、recipe 或
其他玩法统计。需要玩法差异时创建独立 itype、inheritance、snippet/conditional name 或合适的
数据结构。大量细小 variant 会增加翻译和 tileset 成本；每项应有可辨识、可出现的用途。

variant ID 会进入 item instance、spawn、migration 和 serialization 路径。删除或重命名已有 ID
前检查保存兼容与 migration；copy-from 清空或替换 variants 时也要审阅展开结果。

### 验证

运行 formatter、`make -j2 json-check`、Mod `--check-mods`，并实际生成每个 weighted variant。
检查默认继承、translation plural、symbol/color/ascii art、snippet expansion、tileset fallback、
存档 round trip 和旧 ID migration。不要用 `tests/cata_variant_test.cpp` 证明 item variant；应使用
item name/spawn/serialization 的 focused test。
