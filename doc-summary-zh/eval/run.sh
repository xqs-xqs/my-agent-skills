#!/bin/bash
# 用 headless Claude Code 跑一次 doc-summary-zh，输出 stream-json 时间线供 analyze.py 检查。
# 用法: run.sh <SKILL.md> <run_id> [model] [doc.md] [额外要求]
# 例:   ./run.sh ../SKILL.md opus-1 claude-opus-5-5 docs/tcp_congestion.md "用 Markdown 输出"
set -u
HERE=$(cd "$(dirname "$0")" && pwd)
SKILL=$(realpath "$1"); ID=$2; MODEL=${3:-claude-opus-5-5}; DOC=$(realpath "${4:-$HERE/docs/rag_agent_memory.md}"); EXTRA=${5:-}
OUT=$HERE/out; W=$OUT/work/$ID; mkdir -p "$OUT"; rm -rf "$W"; mkdir -p "$W/.claude/skills/doc-summary-zh"
cp "$SKILL" "$W/.claude/skills/doc-summary-zh/SKILL.md"
sed "s#__SERVER__#$HERE/fake_visualize_mcp.py#" > "$OUT/mcp.json" <<'J'
{"mcpServers": {"visualize": {"command": "python3", "args": ["__SERVER__"]}}}
J
PROMPT="【技能：doc-summary-zh】详细总结这个文档${EXTRA:+，$EXTRA}

<document name=\"$(basename "$DOC" .md).pdf\">
$(cat "$DOC")
</document>

（提示：请通过 Skill 工具加载 doc-summary-zh 技能后再作答。）"
cd "$W" && RUN_ID=$ID WIDGET_LOG=$OUT/widgets.jsonl timeout 900 claude -p "$PROMPT" --model "$MODEL" \
  --system-prompt "$(cat "$HERE/sysprompt.txt")" \
  --tools Skill --allowedTools Skill mcp__visualize__read_me mcp__visualize__show_widget \
  --mcp-config "$OUT/mcp.json" --strict-mcp-config --setting-sources project \
  --output-format stream-json --verbose > "$OUT/$ID.jsonl" 2> "$OUT/$ID.err"
