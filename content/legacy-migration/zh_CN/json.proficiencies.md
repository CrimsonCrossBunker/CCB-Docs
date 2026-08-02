## Proficiency、category 与 migration

Proficiency 是独立于 skill 的知识图。recipe/activity 决定何时学习或使用它；JSON definition
提供 identity、前置、默认 penalty、学习属性和 consumer-specific bonuses。依赖可以形成任意有向
图，不要假设只是一棵树。

### 三种 object

`proficiency` 必须有 name、description、can_learn、category。可选字段包括 teachable（默认 true）、
time_to_learn、required_proficiencies、ignore_focus、default time/skill/weakpoint modifiers 和
bonuses。旧 `default_fail_multiplier` 仍被转换但会报告，新的数据使用
`default_skill_penalty`。

`proficiency_category` 要求 name/description，ID 由 factory 提供。`proficiency_migration` 要求
from，可选 to；缺少 to 表示移除旧 proficiency，给出 to 则必须引用有效 ID。删除/重命名公开 ID
时 migration 是存档兼容的一部分。

### Bonuses 与 consumers

bonus entry 要求 type/value，但 bonus key 的含义由具体 activity/attack consumer 定义；JSON 中
可解析不表示有代码使用。新增 key/type 必须同时实现 consumer、文档和测试。recipe 可覆盖默认
time/skill/learning/max-experience，最终效果要查 recipe 展开结果。

### 验证

检查 category、所有 prerequisites、循环/不可达节点、learnable/teachable 组合、migration 和引用
它的 recipes/books/activities。运行 formatter、`make -j2 json-check`、Mod `--check-mods`，再用
focused crafting/learning/save migration tests 覆盖无 proficiency、部分学习、已掌握和旧 ID。
生成 proficiency index 用于发现，不替代 loader 与 consumer 审核。
