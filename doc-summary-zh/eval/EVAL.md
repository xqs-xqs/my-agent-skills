# doc-summary-zh 结构稳定性测试

用 headless Claude Code 模拟 claude.ai 的调用环境，检查四层级是否按 一 → 二 → 三 → 四 出现在用户可见的位置。

## 组成

| 文件 | 作用 |
|------|------|
| `fake_visualize_mcp.py` | 假的 `visualize` MCP 服务（`read_me` / `show_widget`），把组件代码记到 `out/widgets.jsonl` |
| `sysprompt.txt` | 近似 claude.ai 的系统提示词 |
| `run.sh` | 跑一次 skill，输出 stream-json 时间线到 `out/<run_id>.jsonl` |
| `analyze.py` | 还原"正文块 / 工具调用"的先后顺序并判定 PASS |
| `render_widgets.js` | 用 Chromium 实际渲染组件，检查总结句、导图节点、JS 报错、引擎是否被改动，并截图 |
| `docs/` | 两份测试文档（RAG 讲义、TCP 拥塞控制） |

## 用法

```bash
cd doc-summary-zh/eval
for i in 1 2 3; do ./run.sh ../SKILL.md opus-$i claude-opus-5-5 & done; wait
python3 analyze.py out/*.jsonl
node render_widgets.js
```

## PASS 判定

1. `show_widget` 的组件代码里 `summary` 填了真实总结句（不是模板占位文字）
2. 工具调用前没有正文
3. 工具返回后正文以 `## 三、` 开头，第三、四层级都在，且没有重复第一、二层级的标题

## 结果记录

| 版本 | 用例 | 通过 | 主要问题 |
|------|------|------|----------|
| v1.1 | RAG 讲义 × Opus 6 次 + Sonnet 3 次 | 0 / 9 | 2/6 次 Opus 完全丢掉第一层级（总结只写在推理里，正文直接从"第三层级"开始）；其余均为"导图 → 一句话总结 → 二、见上图"，顺序错乱 |
| v1.2 | RAG 讲义 + TCP 讲义 × Opus/Sonnet 共 13 次 | 13 / 13 | — |
| v1.2 | 附加"用 Markdown 输出"要求 × 3 次 | 3 / 3 | — |
