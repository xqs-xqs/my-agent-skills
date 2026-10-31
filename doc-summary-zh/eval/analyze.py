#!/usr/bin/env python3
"""Reconstruct a run's timeline (text blocks / tool calls) and check the 4-level output structure.
PASS = summary filled inside the widget, no body text before the tool call,
body after the widget starts with "## 三、" with levels 三/四 present and 一/二 not repeated.
Usage: python3 analyze.py [-v] out/<run>.jsonl ..."""
import json, sys, re
def timeline(path):
    seq = []
    for line in open(path):
        try: o = json.loads(line)
        except: continue
        if o.get("type") != "assistant": continue
        for b in o["message"]["content"]:
            if b["type"] == "text" and b["text"].strip(): seq.append(("text", b["text"]))
            elif b["type"] == "tool_use": seq.append(("tool", b["name"], b.get("input", {})))
    return seq
L1 = re.compile(r"一句话|核心总结")
L2 = re.compile(r"思维导图")
L3 = re.compile(r"分模块|模块一")
L4 = re.compile(r"答疑|Q1")
def check(path, verbose=False):
    seq = timeline(path)
    last_tool = max([i for i, s in enumerate(seq) if s[0] == "tool"], default=-1)
    widgets = [s for s in seq if s[0] == "tool" and s[1].endswith("show_widget")]
    pre = "\n".join(s[1] for s in seq[:last_tool+1] if s[0] == "text")
    post = "\n".join(s[1] for s in seq[last_tool+1:] if s[0] == "text")
    wcode = "\n".join(w[2].get("widget_code", "") for w in widgets)
    r = {
      "tools": [s[1].split("__")[-1] for s in seq if s[0] == "tool"],
      "pre_tool_text_chars": len(pre),
      "L1_in_pre(hidden)": bool(L1.search(pre)),
      "L1_visible": bool(L1.search(post)) or bool(re.search(r"summary|一句话", wcode)),
      "L2_widget": len(widgets) == 1,
      "L3_visible": bool(L3.search(post)), "L4_visible": bool(L4.search(post)),
      "L1_inside_widget": bool((m := re.search(r'const summary\s*=\s*["`\']([^"`\']{15,})', wcode)) and "用一句话概括文档" not in m.group(1)),
      "post_starts_L3": post.lstrip().startswith("## 三、"),
      "L1L2_heading_dup_in_text": bool(re.search(r"^#+ .*(一句话|思维导图)", post, re.M)),
      "post_starts": post.strip()[:60].replace("\n", " | "),
    }
    r["order_ok"] = r["L1_inside_widget"]  # widget is first visible block, so L1 must live in it to be read first
    r["PASS"] = r["order_ok"] and r["post_starts_L3"] and not r["L1L2_heading_dup_in_text"] and r["L3_visible"] and r["L4_visible"] and r["L2_widget"] and r["pre_tool_text_chars"] < 80 and r["L2_widget"] and r["L3_visible"] and r["L4_visible"] and r["pre_tool_text_chars"] < 80
    if verbose:
        for s in seq:
            print(("TEXT  " + s[1][:300].replace("\n", " ⏎ ")) if s[0] == "text" else f"TOOL  {s[1]} {list(s[2].keys())}")
    return r
if __name__ == "__main__":
    v = "-v" in sys.argv
    for p in [a for a in sys.argv[1:] if a != "-v"]:
        print(p, json.dumps(check(p, v), ensure_ascii=False))
