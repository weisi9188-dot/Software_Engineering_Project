# ChangeScope 用户故事追踪索引（候选草稿）

> 目前 **20条功能 + 3条非功能 = 23条**；均为待真实调研确认的候选故事。
> `TODO` 表示尚未有证据/真实 Issue，不能视为已完成课程检查。

| 故事 ID | 草稿 | 来源 UC / 场景 | 建议负责成员 | 优先级 | 调研证据链接 | GitHub Issue |
| --- | --- | --- | --- | --- | --- | --- |
| US-01 | [通过 GitHub 授权登录系统](issue-drafts/US-01.md) | UC01 | A | P0 | TODO | TODO |
| US-02 | [选择允许分析的仓库](issue-drafts/US-02.md) | UC02 | A | P0 | TODO | TODO |
| US-03 | [初始化仓库提交历史](issue-drafts/US-03.md) | UC03 | B | P0 | TODO | TODO |
| US-04 | [增量更新仓库分析数据](issue-drafts/US-04.md) | UC04 | B | P0 | TODO | TODO |
| US-05 | [查找可分析的 Pull Request](issue-drafts/US-05.md) | UC05 | C | P0 | TODO | TODO |
| US-06 | [对指定 PR 发起风险分析](issue-drafts/US-06.md) | UC06 | B | P0 | TODO | TODO |
| US-07 | [理解 PR 风险分数的依据](issue-drafts/US-07.md) | UC07, UC08 | C | P0 | TODO | TODO |
| US-08 | [发现历史关联文件](issue-drafts/US-08.md) | UC09 | B | P0 | TODO | TODO |
| US-09 | [核对关联文件的历史提交证据](issue-drafts/US-09.md) | UC10 | B | P0 | TODO | TODO |
| US-10 | [比较 PR 更新前后的风险变化](issue-drafts/US-10.md) | UC11 | C | P1 | TODO | TODO |
| US-11 | [追踪个人 PR 风险历史](issue-drafts/US-11.md) | UC12 | C | P1 | TODO | TODO |
| US-12 | [按风险优先级安排审查](issue-drafts/US-12.md) | UC13 | C | P0 | TODO | TODO |
| US-13 | [找到合适的审查员并了解原因](issue-drafts/US-13.md) | UC14, UC15 | B | P1 | TODO | TODO |
| US-14 | [反馈风险提示是否有帮助](issue-drafts/US-14.md) | UC16 | D | P0 | TODO | TODO |
| US-15 | [记录关联文件的实际核查结论](issue-drafts/US-15.md) | UC17 | D | P1 | TODO | TODO |
| US-16 | [查看项目风险趋势](issue-drafts/US-16.md) | UC18 | C | P1 | TODO | TODO |
| US-17 | [调整风险评分指标权重](issue-drafts/US-17.md) | UC19 | B | P1 | TODO | TODO |
| US-18 | [比较评分规则版本](issue-drafts/US-18.md) | UC20 | B | P1 | TODO | TODO |
| US-19 | [统计风险提示的有效性反馈](issue-drafts/US-19.md) | UC21 | D | P1 | TODO | TODO |
| US-20 | [导出可追溯的风险分析报告](issue-drafts/US-20.md) | UC22 | D | P1 | TODO | TODO |
| NFR-01 | [风险分析响应性能](issue-drafts/NFR-01.md) | NFR01 | D | P0 | TODO | TODO |
| NFR-02 | [权限与仓库数据隔离](issue-drafts/NFR-02.md) | NFR02 | D | P0 | TODO | TODO |
| NFR-03 | [外部 API 故障时的可用性与恢复](issue-drafts/NFR-03.md) | 新增非功能故事：可用性 | D | P0 | TODO | TODO |

## 使用说明

- 此索引是故事目录，不代替老师要求的“一条故事一个 GitHub Issue”。
- `US-07` 归并原 UC07/UC08；`US-13` 归并原 UC14/UC15，避免仅为页面细节拆分故事。
- 新增 `NFR-03` 用于覆盖课程课堂检查的可用性要求。
- 非功能性能目标、恢复能力和角色权限均为待评审初稿，需要以调研与测试条件确认。
- 后续建立“证据 ID → Story ID → GitHub Issue # → 用例 → 测试编号”的追踪链。
