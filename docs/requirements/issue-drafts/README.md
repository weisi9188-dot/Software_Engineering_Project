# ChangeScope 用户故事草稿（统一编号版）

> **这里是需求草稿，不是GitHub上已创建的Issues，也不意味着已完成真人访谈。**

本目录只保留 **25份候选故事**：`US01.md`—`US22.md` 为22条功能故事，`US23.md`—`US25.md` 为3条非功能故事。`NFR-01`—`NFR-03` 仅代表SRS中的非功能需求编号，**不再是草稿文件名**。

- 全部编号、标题、关联需求与状态：[用户故事总索引](../user-stories-index.md)
- 旧版`US-xx`、`NFR-xx`对应新编号：[迁移对照](../story-id-migration.md)
- 需求→故事→用例→计划测试：[需求追溯矩阵](../requirements-traceability.md)

## 创建真实GitHub Issue的步骤

1. 先与真实使用者核对候选故事，保留合规的原始访谈/反馈证据。
2. 由四人审核每个故事的独立用户价值，合并或调整不真实或重复的需求。
3. 为确认的故事在GitHub分别创建**真实 Issue**，正文包含`USxx`编号、用户故事、Given/When/Then、真实证据链接，指定真实GitHub Assignee。
4. 在 [`user-stories-index.md`](../user-stories-index.md) 的“GitHub Issue”列回填对应 Issue URL。
5. 若GitHub线上已有旧编号Issue，先按业务内容核对并更新/关联，勿因换号新建重复 Issue。
6. 需求评审及SRS发布须由真实组员Review，并在GitHub留下PR、Release记录。

## 编号示例

- `US09` = 查询历史关联文件 ↔ `FR-09` ↔ `UC09` ↔ `TC-UC09-01`。
- `US19` = 配置风险指标权重 ↔ `FR-19` ↔ `UC19`。
- `US23` = 风险分析性能 ↔ `NFR-01` ↔ `VT-NFR01`。
- `US24` = 权限与数据安全 ↔ `NFR-02` ↔ `VT-NFR02`。
- `US25` = 外部服务故障下的可用性 ↔ `NFR-03` ↔ `VT-NFR03`。

**不要再使用旧的 `US-08` 或旧故事文件 `NFR-01.md` 作为新Issue草稿ID。**
