## 新增 comestible 的放置与验证

目录和文件名帮助维护者查找数据，但不改变 `COMESTIBLE` loader 语义。先确认 object 的内容域，
再放入当前 `data/json/items/comestibles/` 中最窄、已有相似项目的文件；不要照抄旧列表中已经删除
或改名的文件。

### 当前分类顺序

优先使用明确领域文件：medicine、mutagen/serum、MRE、brewing、frozen、spice、protein、alien/
netherum 等。普通 drink 区分 alcohol、soup、drink 与 drink_other；solid food 按 baked、bread、
casserole、cereal、dairy、egg、fruit、junkfood、meat/offal、mushroom、nuts、raw produce/grain、
sandwich、seed、veggy、wheat 等现有邻居放置。无法自然归类才用 `other.json`。

分类不是 gameplay tag。需要搜索、recipe、item group 或 effect 行为时，显式声明对应字段和 ID，
不要依赖 path。

### Loader 契约

`comestible_type` 必填。charges 至少为 1（缺省路径可为 0），其余包括 stack size、quench、fun、
stim、health、spoilage、calories、vitamins、addiction、cooks/eats like、cook/smoke result、
consumption EOC 与 contamination。requiredness、默认和 bounds 以
`islot_comestible::deserialize` 为准。

### 验证

找一个当前相似 item 和 recipe，核对 nutrition、portion/charges、container、spoilage、价格、
item group、recipe 结果及翻译。运行 formatter、`make -j2 json-check` 和 Mod `--check-mods`；营养
或加工变化还要运行 focused comestible/recipe tests，确保 ingredients、byproducts、cooks_like 与
`NUTRIENT_OVERRIDE` 的关系合理。
