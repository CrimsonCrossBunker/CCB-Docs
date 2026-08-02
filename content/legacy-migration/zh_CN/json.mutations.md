## 当前 CCB Mutation 契约

`mutation` 由 `mutation_branch` factory 加载。当前 `mutation_branch::load` 强制读取
`name`、`description` 与 `points`；激活、分类、阈值、装备冲突和 EOC 是叠加在同一个
稳定 trait ID 上的不同子系统。

### 基础定义

```jsonc
{
  "type": "mutation",
  "id": "TRAIT_CCB_EXAMPLE",
  "name": { "str": "Example adaptation" },
  "description": "A documentation-only example.",
  "points": 1,
  "starting_trait": false,
  "purifiable": true,
  "category": [ "MUTCAT_CCB_EXAMPLE" ]
}
```

`points` 是角色创建/评价数据，不等价于突变获取权重。`starting_trait`、
`random_start_allowed`、`valid` 和 `purifiable` 控制不同入口。`variants` 给同一 trait
提供带权名称/描述变化，不创建新的稳定 trait ID。

### 主动、被动与装备关系

主动 mutation 可配置 `cost`、`time` 以及 kcal、thirst、sleepiness、mana、stamina 等资源，
并通过当前 activation/EOC 字段产生效果。`starts_active` 只对可激活 trait 有意义。
reflex activation 的 condition、开关消息和 talker 语义必须按 EOC 条件验证。

`destroys_gear`、`allow_soft_gear`、bodypart/armor 与 enchantment 会改变穿戴、身体结构和
缓存。获得、移除、净化、变体切换与保存重载都可能触发缓存更新；不要只测角色创建界面。

### Category、阈值与关系图

mutation category 是具名注册对象，控制 vitamin、threshold、primer/mutagen 与 category
强度。trait 的 `prereqs`、`prereqs2`、`threshreq`、`cancels`、`replacements` 和 additions
形成有向图。修改任何边都要检查不可达节点、循环、阈值前后替换和 instability 对好坏结果
的影响。

删除或改名公开 trait 时使用当前 `trait_migration` 契约，可替换 trait/variant 或明确移除。
仅在 JSON 中删除旧 ID 会让旧存档和其他 Mod 失去引用。

### 验证

运行 formatter、`make -j2 json-check`、实际 Mod 集 `--check-mods` 和相关
`mutation_test`。覆盖角色创建、mutagen/primer、净化、阈值、坏突变概率、主动 cooldown、
resource 不足、装备冲突、enchantment/cache、NPC 与存档重载。还要检查翻译 variant、
消息参数和 EOC true/false 路径。

旧文档中的化学流程与概率说明会随实现变化；系统解释以当前 mutation 源码和测试为准。
