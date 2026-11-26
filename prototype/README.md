# 文件共变更可行性原型

本原型仅验证项目设计方案中的算法 A：文件共变更频次和方向性条件关联强度。**不能**用于证明软件缺陷风险或自动批准 PR。

## 运行

在仓库根目录运行（Python 3.10+）：

```bash
python -m unittest discover -s tests -v
python -m prototype.cochange --input examples/sample_git_history.json --file src/auth.py
python -m prototype.cochange --repo /path/to/local/repository --file README.md --limit 300 --min-support 2
```

算法定义：`CoChange(A,B)=N(A,B)/N(A)`。例如文件 A 被改4次，B和A共同出现2次，A→B强度为0.5；若B一共被改2次，则B→A为1.0。

## 目前处理规则

- 忽略 merge 提交。
- 过滤单次改动文件数超过 `--max-files-per-commit` 的大型提交（默认为30）。
- 设置最小共同出现次数 `--min-support`（默认为2）。
- 同一提交的重复文件名只计一次；每条建议保存对应提交 ID。
- 只在本地读取 Git 历史；不会发送代码、认证信息或请求 GitHub API。

## 尚未解决的技术风险

- 重命名文件路径合并、子模块、文件删除及复杂 merge 历史的处理。
- 提交窗口大小和最小支持度对排序的影响。
- 一次大型功能开发包含大量共同变更不代表长期依赖。
- 历史共变更不等于静态依赖，更不代表必须同时修改。
- 尚未完成真实开源项目的评价、标注与对比实验。

后续需要增加数据采集模块、可靠的历史缓存、算法基线对比、人工审查反馈和前后端服务。
