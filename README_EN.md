

<div align="center">


# 🧰 my-agent-skills

> A personal collection of Claude Skills
>
> Sharing skills that genuinely improve daily learning, work, and reading workflows.

**🌐 Language**: [简体中文](./README.md) | **English**

</div>


---

## 📖 Table of Contents

- [🧰 my-agent-skills](#-my-agent-skills)
  - [📖 Table of Contents](#-table-of-contents)
  - [🤔 What is a Skill](#-what-is-a-skill)
  - [📁 Repository Structure](#-repository-structure)
  - [📚 Skill List](#-skill-list)
  - [🆚 Prompt or Skill?](#-prompt-or-skill)
  - [📋 Prompt Templates](#-prompt-templates)
  - [🚀 Installation](#-installation)
    - [Option 1: Download a Single Skill](#option-1-download-a-single-skill)
    - [Option 2: Clone the Entire Repo](#option-2-clone-the-entire-repo)
  - [💡 Usage Tips](#-usage-tips)
  - [🤝 Contributing](#-contributing)
  - [🛠️ Build Your Own Skill](#️-build-your-own-skill)
  - [📌 FAQ](#-faq)
  - [📜 License](#-license)
  - [🌟 Star History](#-star-history)

---

## 🤔 What is a Skill

A Skill is a **pluggable capability package** for Claude. At its core, it's a structured Markdown instruction file (SKILL.md) that tells Claude how to think, what steps to follow, and what format to output when encountering specific types of tasks.

Think of it as:

- 📝 A domain-specific SOP (Standard Operating Procedure)
- 🧠 A specialist's "working manual"
- 🔌 An "app plugin" for Claude — once installed, it auto-triggers in relevant scenarios

**Key advantages:**

- **Auto-triggering**: No need to copy prompts each time; Claude decides when to invoke based on the description
- **Write once, reuse forever**: Define your workflow once, execute consistently every time
- **Shareable & iterable**: Package as `.skill` files for easy distribution

---

## 📁 Repository Structure

```
my-agent-skills/
├── README.md                     # Chinese homepage
├── README.EN.md                  # English version (this file)
├── LICENSE                       # Open source license
│
├── doc-summary-zh/               # Skill 1: Structured Chinese doc summarizer
│   ├── SKILL.md                  # Core instruction file
│   ├── doc-summary-zh.skill      # Packaged installer
│   └── README.md                 # Skill-specific documentation
│
├── [skill-2]/                    # Future skills
│   └── ...
│
├── prompts/                      # Prompt templates (paste manually, no install)
│   ├── extract.md                # Single-conversation knowledge capture
│   ├── weekly-review.md          # Cross-doc thinking-pattern insights
│   ├── question-review.md        # Question-asking training
│   ├── handoff-export.md         # Cross-conversation handoff · stage 1 (transcribe)
│   └── handoff-resume.md         # Cross-conversation handoff · stage 2 (resume)
│
└── docs/                         # General documentation
    ├── how-to-install.md         # Installation guide
    └── how-to-create.md          # Skill authoring guide
```

**Design Principles**

- Each skill lives in its own folder; folder name matches the skill's `name` field
- Each skill ships with both `SKILL.md` (readable/editable) and `.skill` (one-click install)
- Each skill has its own README describing specific usage
- Each prompt is a standalone `.md` file with its usage included inside

---

## 📚 Skill List

| Skill                                                   | Function                                                     | Use Case                                                     | Status |
| ------------------------------------------------------- | ------------------------------------------------------------ | ------------------------------------------------------------ | ------ |
| [`doc-summary-zh`](./doc-summary-zh/)                   | Structured deep summary for technical & course documents     | Slides, technical docs, lectures                             | ✅ v1.1 |
| [`algo-speed-run`](./algo-speed-run/)                   | One-shot algo breakdown: physical intuition + geek code + visualizer + cross-examination | Speed-run LeetCode, interview blitz, gap-filling             | ✅ v1.0 |
| [`algo-deconstruct-engine`](./algo-deconstruct-engine/) | Deep algo deconstruction: blind-push gating + physical models + cold-start recall test | Deep mastery, long-term retention, building algo intuition   | ✅ v1.0 |
| [`cook-from-zero`](./cook-from-zero/)                   | Learn a dish or technique from scratch: transferable principles + anti-procrastination layering | Home-cooking beginners who want the why, not just the recipe | 🚧 v0.1 |

*More skills still brewing, coming soon...*

---

## 🆚 Prompt or Skill?

Not every handy prompt is worth packaging as a skill. The two solve different problems:

| Dimension           | Skill                                                     | Prompt Template                                              |
| ------------------- | --------------------------------------------------------- | ------------------------------------------------------------ |
| Triggering          | Claude **auto-detects the scenario** from the description | You **paste it manually** into the chat                      |
| Reuse               | Install once, hits repeatedly over time                   | Copy when needed, one-off                                    |
| Control             | Claude decides whether to use it                          | You fully decide when and how                                |
| Install             | Must package as `.skill` and upload                       | Zero install, copy & go                                      |
| Tweaking on the fly | Awkward (requires repackaging)                            | Just edit the placeholders, flexible                         |
| Best for            | Fixed workflows that recur across similar scenarios       | Occasional use, on-the-fly params, or prompts still being refined |

**The one-line test:**

> "I want Claude to **recognize the scenario automatically**" → make it a **Skill**
>
> "I **know when to use it** and want to feed it manually" → keep it a **Prompt**

For things like knowledge capture or periodic review — where you already know when to use them and want to tweak params each time — a prompt template is actually smoother than a skill.

---

## 📋 Prompt Templates

Paste manually, no install required. Click a command to see the full template and usage.

| Command                                            | Purpose                                                      | Input                                                | Output                                           |
| -------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------------------ |
| [`/extract`](./prompts/extract.md)                 | Knowledge capture + meta-cognitive feedback on your questions | The current conversation                             | A note-ready capture doc                         |
| [`/weekly-review`](./prompts/weekly-review.md)     | Cross-doc thinking-pattern insights                          | This week's N conversation-question docs             | Question habits / blind spots / training tips    |
| [`/question-review`](./prompts/question-review.md) | Question-asking training (focused on raw questions only)     | Your raw questions across N conversations on a topic | The single deadliest blind spot + rewrite drills |
| [`/handoff-export`](./prompts/handoff-export.md)   | Cross-conversation handoff · transcribe (lock in conclusions + open questions) | The current long conversation                        | A paste-ready handoff record                     |
| [`/handoff-resume`](./prompts/handoff-resume.md)   | Cross-conversation handoff · resume (calibrate + ask 3 key questions) | The handoff record from the previous step            | Recap confirmation + 3 key questions back        |

---

## 🚀 Installation

### Option 1: Download a Single Skill

1. Navigate to the skill folder (e.g., [`doc-summary-zh/`](./doc-summary-zh/))
2. Download the `.skill` file
3. In Claude.ai, go to Settings → Capabilities → Skills
4. Click **Upload Skill** and select the downloaded `.skill` file
5. Trigger it using keywords described in that skill's README

### Option 2: Clone the Entire Repo

```bash
git clone https://github.com/xqs-xqs/my-agent-skills.git
cd my-agent-skills
```

Then upload individual skills following Option 1.

---

## 💡 Usage Tips

| Scenario            | Recommendation                                               |
| ------------------- | ------------------------------------------------------------ |
| First-time use      | Read the skill's README first                                |
| Unexpected behavior | Open an [issue](https://github.com/xqs-xqs/my-agent-skills/issues) |
| Want to customize   | Fork → edit SKILL.md → repackage                             |
| Cross-device usage  | Sign in to the same Claude account                           |

---

## 🤝 Contributing

This is primarily a **personal-use repository**, but contributions are welcome:

- 🐛 **Issues**: Report bugs, triggering problems, or suboptimal outputs
- 💬 **Discussions**: Share usage insights and scenarios
- 🔀 **Pull Requests**: Meaningful improvements to existing skills are welcome

---

## 🛠️ Build Your Own Skill

Want to build your own? Use Claude's built-in **skill-creator**:

1. Type `/skill-creator` in Claude.ai
2. Describe the capability you want
3. Claude will guide you through drafting, testing, and packaging

Once done, drop the generated `.skill` file into your own repo to share.

---

## 📌 FAQ

**Q: What's the difference between SKILL.md and .skill?**

A: `SKILL.md` is the source file (human-readable, editable); `.skill` is the packaged installer (a zip archive). Edit the former, distribute the latter.

**Q: Do skills auto-trigger?**

A: Yes. Claude decides based on keywords and scenarios in the skill's description. You can also invoke explicitly: "Use the xxx skill on this."

**Q: Can multiple skills conflict?**

A: No. Skills cover different scenarios; for overlapping contexts, Claude picks the best match.

**Q: Why are some things skills and others just prompts?**

A: It comes down to whether you want Claude to *auto-trigger*. Fixed, recurring workflows become skills; occasional prompts that need on-the-fly tweaks stay as paste-in prompts. See [Prompt or Skill?](#-prompt-or-skill).

**Q: Does this cost anything?**

A: This repo is fully free. Using skills doesn't incur extra cost — they consume normal Claude message quota.

---

## 📜 License

[MIT License](./LICENSE) — Feel free to use, modify, and share. Attribution appreciated.

---

## 🌟 Star History

If these skills help you, a Star would mean a lot ⭐

---

<div align="center">


**Maintained by [@xqs-xqs](https://github.com/xqs-xqs)** · Made with Claude 🤖

</div>