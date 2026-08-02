## 设计稿与当前实现必须分开

旧 faction 文档同时记录已经存在的阵营、未完成章节、未来任务构想和作者推测，不能当作当前游戏状态
清单。第一方 faction ID、基础关系、currency、food、wealth、epilogue 等数据以
`data/json/npcs/factions.json` 和 `faction` loader 为准；NPC、对话、任务、mapgen 和 tests 决定玩家
实际能遇到的成员与行为。文档冲突时标记 stale 并按这些来源修复。

## 阵营写作模板

每个阵营页面或提案至少区分：

- **身份与来源**：成员如何形成、哪些信息是玩家可见、哪些是后台剧透；
- **结构与规模**：领导、成员、从属关系和地理范围，并标明数字是实现值还是叙事估计；
- **目标与限制**：短期需求、长期方向、不能或不愿做的事情；
- **关系**：对玩家、其他人类阵营、mutant/augmentation 和非人势力的态度及其变化条件；
- **基地与经济**：真实 location、货币、商品来源、生产能力和供应瓶颈；
- **任务与发展**：当前 mission ID/对话入口、计划内容以及会改变世界或存档的阶段。

Blob、Mycus、triffid、netherum、Exodii、Yrax、mi-go 等不必符合人类国家模型。保留其不同感知、时间尺度、
沟通和价值体系，不要为了给玩家任务就让不可交流的力量突然采用普通 barter 或道德语言。

## 验证

新增或修改阵营时检查稳定 ID、`copy-from`、relations 对称性、mon faction、currency、price rules、food、
epilogue、NPC class、dialogue talker、mission 与 mapgen 引用。运行 JSON/EOC 加载、重复/失效 ID 检查和
相关 faction/monster-faction tests；在实际游戏覆盖首次发现、敌对转换、贸易、任务阶段和保存重载。
未实现的外交、基地或结局保持 draft，不能在正式页面写成现有功能。
