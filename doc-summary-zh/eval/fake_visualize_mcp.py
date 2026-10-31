#!/usr/bin/env python3
"""Minimal stdio MCP server mimicking claude.ai's visualize:read_me / visualize:show_widget."""
import json, sys, os, time
LOG = os.environ.get("WIDGET_LOG", os.path.join(os.path.dirname(os.path.abspath(__file__)), "out", "widgets.jsonl"))
TOOLS = [
  {"name": "read_me",
   "description": "Load design guidelines for show_widget. Must be called once before the first show_widget call in a conversation.",
   "inputSchema": {"type": "object", "properties": {"modules": {"type": "array", "items": {"type": "string"}}}}},
  {"name": "show_widget",
   "description": "Render an HTML/SVG widget inline in the chat for the user. Call read_me first.",
   "inputSchema": {"type": "object", "properties": {
      "title": {"type": "string"},
      "i_have_seen_read_me": {"type": "boolean"},
      "widget_code": {"type": "string", "description": "HTML fragment (style/div/svg/script) rendered in a sandboxed iframe"}},
      "required": ["widget_code"]}},
]
GUIDE = ("Widgets render in an iframe. Use CSS variables: --font-sans, --color-text-primary, "
         "--color-text-secondary, --color-background-primary, --color-background-secondary, "
         "--color-border-tertiary. No external network. Keep widgets self-contained.")
def send(o): sys.stdout.write(json.dumps(o, ensure_ascii=False) + "\n"); sys.stdout.flush()
for line in sys.stdin:
    line = line.strip()
    if not line: continue
    m = json.loads(line); mid = m.get("id"); meth = m.get("method")
    if meth == "initialize":
        send({"jsonrpc": "2.0", "id": mid, "result": {"protocolVersion": m["params"].get("protocolVersion", "2024-11-05"),
              "capabilities": {"tools": {}}, "serverInfo": {"name": "visualize", "version": "0.1"}}})
    elif meth == "tools/list":
        send({"jsonrpc": "2.0", "id": mid, "result": {"tools": TOOLS}})
    elif meth == "tools/call":
        p = m["params"]; name = p["name"]; args = p.get("arguments", {})
        if name == "read_me": txt = GUIDE
        else:
            with open(LOG, "a") as f: f.write(json.dumps({"t": time.time(), "run": os.environ.get("RUN_ID",""), **args}, ensure_ascii=False) + "\n")
            txt = "Widget rendered successfully and is now visible to the user."
        send({"jsonrpc": "2.0", "id": mid, "result": {"content": [{"type": "text", "text": txt}]}})
    elif mid is not None:
        send({"jsonrpc": "2.0", "id": mid, "result": {}})
