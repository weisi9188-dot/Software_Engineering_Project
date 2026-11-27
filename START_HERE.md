# ChangeScope 项目启动包｜四人小组

> **状态：项目初始材料 / 待访谈与团队评审。**
> 适配仓库：https://github.com/weisi9188-dot/Software_Engineering_Project
> 不替换已有的 `README.md` 和 `ChangeScope_Design.md`。
> 重要：所有需求内容均为**候选草稿**，不是已经完成的真人调研结论。

## 先做什么（按顺序）

1. 四位成员把 GitHub 用户名填入 `docs/project/team-roles.md`。
2. 由 A 创建分支 `docs/requirements-kickoff`，通过 PR 合入本启动包；D 检查 `main` 分支保护是否启用。
3. 创建 GitHub `story` 标签；确认 GitHub 的 Issue Forms 模板能正常显示。
4. B、C 与 A/D 分别联系真实受访者，完成访谈、记录编号和证据存档。不要把姓名、联系方式、仓库令牌、商业机密放入公开仓库。
5. 基于访谈补写 `docs/requirements/research-report.md`，在真实证据支持下修改故事草稿。
6. 每条**确认过的**用户故事单独建 GitHub Issue（至少20条、其中至少3条非功能），设置 `story` 标签、GitHub Assignee，并补真实证据链接。
7. 由 B 可并行试跑 `prototype/` 下的文件共变更分析，结果仅用于技术可行性判断。

## 现在就能上传的文件

- `docs/project/`：四人职责、项目章程草案、技术风险登记
- `docs/requirements/`：调研计划、访谈提纲、访谈记录与调研报告模板、25条统一编号的故事草稿（22条功能 + 3条非功能）与追踪索引
- `.github/ISSUE_TEMPLATE/user_story.yml`：用户故事 Issue 表单
- `.github/pull_request_template.md`：PR 人工评审模板
- `.github/workflows/prototype-tests.yml`：算法原型自动测试
- `prototype/`、`tests/`、`examples/`：最小可运行技术实验（仅标准库）

## 本地验证

```bash
python -m unittest discover -s tests -v
python -m prototype.cochange --input examples/sample_git_history.json --file src/auth.py --min-support 2
# 有本地 Git 仓库时：
python -m prototype.cochange --repo /path/to/local/repository --file src/auth.py --limit 300 --min-support 2
```

**注意：** 示例 JSON 是虚构的测试数据，不得作为用户访谈证据或风险模型实际效果。

## 将文件合入现有仓库（仓库维护者自行操作）

```bash
git clone https://github.com/weisi9188-dot/Software_Engineering_Project.git
cd Software_Engineering_Project
git checkout -b docs/requirements-kickoff

# 把本压缩包解压到当前仓库根目录，不覆盖已有 README.md / ChangeScope_Design.md

git add .
git commit -m "docs: initialize requirements research and cochange prototype"
git push -u origin docs/requirements-kickoff
# 然后在 GitHub 发起 PR，由另一位组员评审，再合并。
```

本包**没有**上传到 GitHub，也不会自动创建 Issues 或代替真人访谈。

## 下次课前核对

- [ ] 仓库、分支保护、PR 评审流程可检查
- [ ] 真实受访者与原始记录已保留（公开版本须脱敏）
- [ ] 调研报告已通过 PR 合并
- [ ] ≥20 条独立的用户故事 Issue
- [ ] 其中 ≥3 条非功能故事：性能 / 安全 / 可用性
- [ ] 每条包含“作为—我想—以便”和 Given/When/Then
- [ ] 每条具有 `story` 标签、真实负责人和调研证据链接
- [ ] 能演示一条“调研证据 → Issue → 验收标准”的追溯链
- [ ] 组内准备8分钟讲解材料
