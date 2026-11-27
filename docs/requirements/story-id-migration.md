# ChangeScope 用户故事编号统一与迁移对照

> **修订日期：2026-11-27；状态：文档编号统一已完成，故事是否已通过真实调研及GitHub Issue化尚待核查。**
> 本次使用上传的 `docs/requirements-kickoff` ZIP 为唯一修改基线，未连接或修改线上GitHub。

## 一、统一规则

| 对象 | 统一编号 | 数量 | 备注 |
|---|---|---:|---|
| 功能故事 | `US01`—`US22` | 22 | 一条独立候选故事对应一个主要功能需求 |
| 非功能故事 | `US23`—`US25` | 3 | 对应性能、安全、可用性需求 |
| 功能需求 | `FR-01`—`FR-22` | 22 | 需求ID，不是故事ID |
| 非功能需求 | `NFR-01`—`NFR-03` | 3 | 需求ID，**不再用于命名故事文件** |
| 功能用例 | `UC01`—`UC22` | 22 | 与`FR-xx`一一对应 |
| 质量验证场景 | `VT-NFR01`—`VT-NFR03` | 3 | 与非功能故事US23—US25对应 |

当前工作目录 `docs/requirements/issue-drafts/` **只保留** `US01.md`—`US25.md` 25份故事草稿及本目录README。旧23份 `US-01`—`US-20`、`NFR-01`—`NFR-03` 故事文件**不再留在正式草稿目录**，避免同义重复、同号异义。

旧版文件没有销毁：保存在另附的 `ChangeScope_旧版用户故事备份_23份.zip`，以及原始仓库提交记录中；需要查看历史时使用该独立备份。

## 二、旧编号 → 新编号（按业务语义映射）

| 旧版文件编号 | 旧版故事标题 | 统一后的故事ID | 处理说明 |
|---|---|---|---|
| `US-01` | [US-01] 通过 GitHub 授权登录系统 | [`US01`](issue-drafts/US01.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-02` | [US-02] 选择允许分析的仓库 | [`US02`](issue-drafts/US02.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-03` | [US-03] 初始化仓库提交历史 | [`US03`](issue-drafts/US03.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-04` | [US-04] 增量更新仓库分析数据 | [`US04`](issue-drafts/US04.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-05` | [US-05] 查找可分析的 Pull Request | [`US05`](issue-drafts/US05.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-06` | [US-06] 对指定 PR 发起风险分析 | [`US06`](issue-drafts/US06.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-07` | [US-07] 理解 PR 风险分数的依据 | [`US07`](issue-drafts/US07.md), [`US08`](issue-drafts/US08.md) | 旧故事同时包含总分与指标解释；拆为US07（风险概览）和US08（指标明细） |
| `US-08` | [US-08] 发现历史关联文件 | [`US09`](issue-drafts/US09.md) | 旧US-08是“发现历史关联文件”，新US08却是“查看风险指标明细”，必须映射到US09 |
| `US-09` | [US-09] 核对关联文件的历史提交证据 | [`US10`](issue-drafts/US10.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-10` | [US-10] 比较 PR 更新前后的风险变化 | [`US11`](issue-drafts/US11.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-11` | [US-11] 追踪个人 PR 风险历史 | [`US12`](issue-drafts/US12.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-12` | [US-12] 按风险优先级安排审查 | [`US13`](issue-drafts/US13.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-13` | [US-13] 找到合适的审查员并了解原因 | [`US14`](issue-drafts/US14.md), [`US15`](issue-drafts/US15.md) | 旧故事合并了推荐结果和推荐依据；拆为US14、US15 |
| `US-14` | [US-14] 反馈风险提示是否有帮助 | [`US16`](issue-drafts/US16.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-15` | [US-15] 记录关联文件的实际核查结论 | [`US17`](issue-drafts/US17.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-16` | [US-16] 查看项目风险趋势 | [`US18`](issue-drafts/US18.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-17` | [US-17] 调整风险评分指标权重 | [`US19`](issue-drafts/US19.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-18` | [US-18] 比较评分规则版本 | [`US20`](issue-drafts/US20.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-19` | [US-19] 统计风险提示的有效性反馈 | [`US21`](issue-drafts/US21.md) | 业务含义延续；按新版详细验收标准为准 |
| `US-20` | [US-20] 导出可追溯的风险分析报告 | [`US22`](issue-drafts/US22.md) | 业务含义延续；按新版详细验收标准为准 |
| `NFR-01 (旧故事文件)` | [NFR-01] 风险分析响应性能 | [`US23`](issue-drafts/US23.md) | 旧文件是非功能故事；新版故事US23，NFR-01仍保留为性能需求ID |
| `NFR-02 (旧故事文件)` | [NFR-02] 权限与仓库数据隔离 | [`US24`](issue-drafts/US24.md) | 旧文件是非功能故事；新版故事US24，NFR-02仍保留为安全需求ID |
| `NFR-03 (旧故事文件)` | [NFR-03] 外部 API 故障时的可用性与恢复 | [`US25`](issue-drafts/US25.md) | 旧文件是非功能故事；新版故事US25，NFR-03仍保留为可用性需求ID |

**关键提醒：** `US-07 → US07 + US08` 和 `US-13 → US14 + US15` 是**拆分映射**，不能通过机械去掉`-`实现。旧版`US-08`映射到`US09`，旧版`US-19`映射到`US21`。

## 三、新版标准故事与需求关联

| 新故事ID | 类型 | 对应需求 | 详细用例或验证场景 |
|---|---|---|---|
| [`US01`](issue-drafts/US01.md) | 功能 | `FR-01` | `UC01` |
| [`US02`](issue-drafts/US02.md) | 功能 | `FR-02` | `UC02` |
| [`US03`](issue-drafts/US03.md) | 功能 | `FR-03` | `UC03` |
| [`US04`](issue-drafts/US04.md) | 功能 | `FR-04` | `UC04` |
| [`US05`](issue-drafts/US05.md) | 功能 | `FR-05` | `UC05` |
| [`US06`](issue-drafts/US06.md) | 功能 | `FR-06` | `UC06` |
| [`US07`](issue-drafts/US07.md) | 功能 | `FR-07` | `UC07` |
| [`US08`](issue-drafts/US08.md) | 功能 | `FR-08` | `UC08` |
| [`US09`](issue-drafts/US09.md) | 功能 | `FR-09` | `UC09` |
| [`US10`](issue-drafts/US10.md) | 功能 | `FR-10` | `UC10` |
| [`US11`](issue-drafts/US11.md) | 功能 | `FR-11` | `UC11` |
| [`US12`](issue-drafts/US12.md) | 功能 | `FR-12` | `UC12` |
| [`US13`](issue-drafts/US13.md) | 功能 | `FR-13` | `UC13` |
| [`US14`](issue-drafts/US14.md) | 功能 | `FR-14` | `UC14` |
| [`US15`](issue-drafts/US15.md) | 功能 | `FR-15` | `UC15` |
| [`US16`](issue-drafts/US16.md) | 功能 | `FR-16` | `UC16` |
| [`US17`](issue-drafts/US17.md) | 功能 | `FR-17` | `UC17` |
| [`US18`](issue-drafts/US18.md) | 功能 | `FR-18` | `UC18` |
| [`US19`](issue-drafts/US19.md) | 功能 | `FR-19` | `UC19` |
| [`US20`](issue-drafts/US20.md) | 功能 | `FR-20` | `UC20` |
| [`US21`](issue-drafts/US21.md) | 功能 | `FR-21` | `UC21` |
| [`US22`](issue-drafts/US22.md) | 功能 | `FR-22` | `UC22` |
| [`US23`](issue-drafts/US23.md) | 非功能 | `NFR-01` | `VT-NFR01` |
| [`US24`](issue-drafts/US24.md) | 非功能 | `NFR-02` | `VT-NFR02` |
| [`US25`](issue-drafts/US25.md) | 非功能 | `NFR-03` | `VT-NFR03` |

## 四、在 GitHub Issue 中如何处理已有记录

**本修订包只修改文件，不代表已更改任何 GitHub Issue。** 如果在线已经建了 Issue：

1. 用**故事内容**而不是数字相似性核对每条 Issue。
2. 对应新版故事时，在 Issue 标题或正文明确写唯一ID，例如 `[Story][US09] 查询历史关联文件`。
3. 遇到旧 `US-07` / `US-13` 的复合故事，讨论是否要拆成两个独立 Issue：先建立真实对应，再关联彼此，勿直接重复创建。
4. 如果现有两个 Issue 表达同一需求，保留一个作为当前 Issue，另一个以“Duplicate”或备注说明后由组员决定是否关闭；**不要伪造Issue编号，不直接删除证据**。
5. 在 [`user-stories-index.md`](user-stories-index.md) 中填写真实 Issue URL、Assignee 和证据链接；未创建的仍写“待创建”。

## 五、影响与不变项

- `SRS_v1.0_候选稿.md` 中保留 `FR-01`—`FR-22` 与 `NFR-01`—`NFR-03` 的需求编号。
- `detailed-use-cases.md` 保留 `UC06 / FR-06 / US06`、`UC09 / FR-09 / US09`、`UC19 / FR-19 / US19` 等关键追溯链。
- `requirements-traceability.md` 以 `US01`—`US25` 为故事主键。
- 算法原型、测试代码和 GitHub Actions 工作流没有更改。
- 本次只做编号与交叉引用整理，**不把未确认的候选用户需求冒充已访谈验证的事实**。
