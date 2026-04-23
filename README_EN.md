

<div align="center">

# 🧰 my-agent-skills

> A personal collection of Claude Skills
>
> Sharing skills that genuinely improve daily learning, work, and reading workflows.

**🌐 Language**: [简体中文](./README.md) | **English**

</div>


---

## 📖 Table of Contents

- [What is a Skill](#-what-is-a-skill)
- [Repository Structure](#-repository-structure)
- [Skill List](#-skill-list)
- [Installation](#-installation)
- [Usage Tips](#-usage-tips)
- [Contributing](#-contributing)
- [Build Your Own](#-build-your-own-skill)
- [FAQ](#-faq)
- [License](#-license)

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
└── docs/                         # General documentation
    ├── how-to-install.md         # Installation guide
    └── how-to-create.md          # Skill authoring guide
```

**Design Principles**

- Each skill lives in its own folder; folder name matches the skill's `name` field
- Each skill ships with both `SKILL.md` (readable/editable) and `.skill` (one-click install)
- Each skill has its own README describing specific usage

---

## 📚 Skill List

| Skill | Function | Lang | Use Case | Status |
|-------|----------|------|----------|--------|
| [`doc-summary-zh`](./doc-summary-zh/) | Structured deep summary for technical & course documents | 🇨🇳 Chinese | Slides, technical docs, lectures | ✅ v1.0 |

*More skills coming soon...*

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

| Scenario | Recommendation |
|----------|----------------|
| First-time use | Read the skill's README first |
| Unexpected behavior | Open an [issue](https://github.com/xqs-xqs/my-agent-skills/issues) |
| Want to customize | Fork → edit SKILL.md → repackage |
| Cross-device usage | Sign in to the same Claude account |

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
