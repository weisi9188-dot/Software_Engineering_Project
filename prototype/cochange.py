"""文件共变更关联分析：标准库实现，供早期技术可行性验证。

定义：CoChange(A, B) = N(A,B) / N(A)，方向性关联。
当前版本仅用于课程实验；不等于静态依赖，也不声称预测缺陷。
"""
from __future__ import annotations

import argparse
from collections import Counter
from itertools import combinations
import json
from pathlib import Path
import subprocess
from typing import Iterable


def collect_git_history(repo: str | Path, *, limit: int = 300) -> list[dict]:
    """从本地 Git 仓库读取最近若干次非 merge 提交及文件列表。

    不上传任何信息、不要求 GitHub token。
    局限：当前不处理文件重命名链，保留 Git 展示的路径。
    """
    command = [
        "git", "-C", str(repo), "log", "--no-merges",
        f"-n{limit}", "--format=__CHANGE_SCOPE_COMMIT__%H",
        "--name-only", "--diff-filter=ACMR",
    ]
    completed = subprocess.run(
        command, check=True, capture_output=True, text=True, encoding="utf-8"
    )
    commits: list[dict] = []
    current: dict | None = None

    for raw_line in completed.stdout.splitlines():
        line = raw_line.strip()
        if line.startswith("__CHANGE_SCOPE_COMMIT__"):
            if current is not None:
                commits.append(current)
            current = {"sha": line.removeprefix("__CHANGE_SCOPE_COMMIT__"), "files": []}
        elif current is not None and line:
            current["files"].append(line)
    if current is not None:
        commits.append(current)
    return commits


def calculate_cochanges(
    commits: Iterable[dict],
    *,
    max_files_per_commit: int = 30,
    min_support: int = 2,
) -> dict:
    """统计每个文件被改次数及共变更次数。

    - 相同提交内文件去重。
    - 太大的提交被过滤（可能是自动格式化/生成造成的噪声）。
    - 返回可追溯的共同提交 SHA 及方向性条件频率。
    """
    if max_files_per_commit < 1 or min_support < 1:
        raise ValueError("max_files_per_commit 与 min_support 必须为正整数")

    file_counts: Counter[str] = Counter()
    pair_counts: Counter[tuple[str, str]] = Counter()
    witnesses: dict[tuple[str, str], list[str]] = {}
    skipped_large = 0
    accepted = 0

    for index, commit in enumerate(commits):
        files = commit.get("files", [])
        if not isinstance(files, list):
            raise ValueError(f"第 {index + 1} 条提交的 files 不是列表")
        distinct = sorted({f for f in files if isinstance(f, str) and f})
        if len(distinct) > max_files_per_commit:
            skipped_large += 1
            continue
        if not distinct:
            continue

        accepted += 1
        file_counts.update(distinct)
        sha = str(commit.get("sha") or f"local-{index + 1}")

        for left, right in combinations(distinct, 2):
            pair_counts[(left, right)] += 1
            witnesses.setdefault((left, right), []).append(sha)

    directed: list[dict] = []
    for (left, right), support in pair_counts.items():
        if support < min_support:
            continue
        for source, target in ((left, right), (right, left)):
            directed.append({
                "source": source,
                "target": target,
                "support": support,
                "source_change_count": file_counts[source],
                "score": round(support / file_counts[source], 6),
                "commits": witnesses[(left, right)],
            })
    directed.sort(key=lambda x: (x["source"], -x["score"], -x["support"], x["target"]))
    return {
        "accepted_commits": accepted,
        "skipped_large_commits": skipped_large,
        "file_counts": dict(file_counts),
        "relations": directed,
    }


def related_to(result: dict, filename: str, *, limit: int = 10) -> list[dict]:
    """查询给定文件指向其他文件的历史关联。"""
    rows = [r for r in result["relations"] if r["source"] == filename]
    return sorted(rows, key=lambda r: (-r["score"], -r["support"], r["target"]))[:limit]


def main() -> None:
    parser = argparse.ArgumentParser(description="ChangeScope 文件共变更分析原型")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--input", help="JSON 提交历史文件（人工构造的示例也可）")
    group.add_argument("--repo", help="本地 Git 仓库路径")
    parser.add_argument("--file", required=True, help="要查询的文件路径")
    parser.add_argument("--limit", type=int, default=300, help="读取的 Git 提交数")
    parser.add_argument("--min-support", type=int, default=2)
    parser.add_argument("--max-files-per-commit", type=int, default=30)
    args = parser.parse_args()

    if args.input:
        payload = json.loads(Path(args.input).read_text(encoding="utf-8"))
        commits = payload["commits"]
    else:
        commits = collect_git_history(args.repo, limit=args.limit)

    result = calculate_cochanges(
        commits,
        max_files_per_commit=args.max_files_per_commit,
        min_support=args.min_support,
    )
    print(f"有效提交：{result['accepted_commits']}；过滤大提交：{result['skipped_large_commits']}")
    print(f"目标文件：{args.file}；历史修改次数：{result['file_counts'].get(args.file, 0)}")
    recommendations = related_to(result, args.file)
    if not recommendations:
        print("当前历史窗口及阈值下无符合条件的关联文件。")
        return
    for item in recommendations:
        print(
            f"{item['target']}: score={item['score']:.3f}, "
            f"共同修改={item['support']}次, "
            f"支持提交={','.join(item['commits'][:5])}"
        )


if __name__ == "__main__":
    main()
