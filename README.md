

<div align="center">

# 🧰 my-agent-skills

> 一个个人维护的 Claude Skills 收藏仓库
>
> 分享一些在日常学习、工作、阅读中自制的 skill。


**🌐 Language**: **简体中文** | [English](./README_EN.md)

</div>
  
---

## 📖 目录

- [🧰 my-agent-skills](#-my-agent-skills)
  - [📖 目录](#-目录)
  - [🤔 什么是 Skill](#-什么是-skill)
  - [📁 仓库结构](#-仓库结构)
  - [📚 Skill 列表](#-skill-列表)
  - [🆚 Prompt 还是 Skill？](#-prompt-还是-skill)
  - [📋 Prompt 模板](#-prompt-模板)
  - [🚀 安装使用](#-安装使用)
    - [方式一：下载单个 skill](#方式一下载单个-skill)
    - [方式二：克隆整个仓库](#方式二克隆整个仓库)
  - [💡 使用建议](#-使用建议)
  - [🤝 贡献与反馈](#-贡献与反馈)
  - [🛠️ 开发自己的 Skill](#️-开发自己的-skill)
  - [📌 常见问题](#-常见问题)
  - [📜 协议](#-协议)
  - [🌟 Star History](#-star-history)

---

## 🤔 什么是 Skill

Skill 是 Claude 的**可插拔能力包**。它本质上是一份结构化的 Markdown 指令文件（SKILL.md），告诉 Claude 在遇到某类任务时应该如何思考、如何执行、输出什么格式。

你可以把它理解为：
- 📝 一份专业领域的 SOP（标准操作流程）
- 🧠 一个领域专家的「工作手册」
- 🔌 Claude 的「App 插件」—— 装上之后，遇到对应场景就会自动触发

**核心优势：**
- **自动触发**：无需每次都复制提示词，Claude 会根据描述判断何时调用
- **一次编写，长期复用**：写好一次，之后每次都按你设定的方式工作
- **可分享、可迭代**：打包成 `.skill` 文件即可分发给他人

---

## 📁 仓库结构

```
my-agent-skills/
├── README.md                     # 中文主页（本文件）
├── README.en.md                  # 英文版
├── LICENSE                       # 开源协议
│
├── doc-summary-zh/               # Skill 1: 中文文档结构化总结
│   ├── SKILL.md                  # 核心指令文件
│   ├── doc-summary-zh.skill      # 打包安装文件
│   └── README.md                 # 该 skill 的详细说明
│
├── [skill-2]/                    # 后续添加的 skill
│   └── ...
│
├── prompts/                      # Prompt 模板（手动粘贴使用，无需安装）
│   ├── extract.md                # 单次对话知识沉淀
│   ├── weekly-review.md          # 跨文档思维模式洞察
│   └── question-review.md        # 提问能力训练
│
└── docs/                         # 通用文档
    ├── how-to-install.md         # 安装教程
    └── how-to-create.md          # 如何创建自己的 skill
```

**设计原则**

- 每个 skill 独立一个文件夹，文件夹名 = skill 的 `name` 字段
- 每个 skill 同时提供 `SKILL.md`（可读可编辑）和 `.skill`（一键安装）
- 各 skill 有自己的 README，说明独特用法
- 每个 prompt 也是独立一个文件夹，具体用法一并包含在 `.md` 文件中
---

## 📚 Skill 列表
| Skill | 功能 | 语言 | 适用场景 | 状态 |
|-------|------|------|----------|------|
| [`doc-summary-zh`](./doc-summary-zh/) | 技术/课程文档结构化深度总结 | 🇨🇳  | 课件、技术文档、学术讲义 | ✅ v1.0 |
| [`algo-speed-run`](./algo-speed-run/) | 算法题单轮完整解构：物理模型+极客代码+可视化+灵魂拷问 | 🇨🇳  | 速刷力扣、面试突击、查漏补缺 | ✅ v1.0 |
| [`algo-deconstruct-engine`](./algo-deconstruct-engine/) | 算法题深度解构：盲推阻断+物理直觉+冷启动测试卷 | 🇨🇳  | 深度掌握、长期留存、建立算法直觉 | ✅ v1.0 |

*更多沉淀中的 skill 正在路上……*

---

## 🆚 Prompt 还是 Skill？

不是所有好用的提示词都值得封装成 skill。两者解决的是不同的问题：

| 维度 | Skill | Prompt 模板 |
|------|-------|-------------|
| 触发方式 | Claude 根据描述**自动识别场景**触发 | 你**手动粘贴**到对话里 |
| 复用方式 | 装一次，长期反复命中 | 用的时候复制，一次性 |
| 可控性 | 由 Claude 判断要不要用 | 完全由你决定何时、怎么用 |
| 安装 | 需打包成 `.skill` 上传 | 零安装，复制即用 |
| 现场改参数 | 不方便（要重新打包） | 直接改占位符，灵活 |
| 适合 | 固定流程、会在相似场景反复命中的能力 | 偶尔用一次、需现场改参数、或还在打磨不值得固化的指令 |

**一句话判断：**

> 「我希望 Claude **自动认出场景**并触发」 → 做成 **Skill**
> 「我**自己知道何时该用**，想手动喂给它」 → 留作 **Prompt**

像「知识沉淀」「周期复盘」这类——你心里清楚什么时候该用、每次还想微调参数——做成 prompt 模板反而比 skill 更顺手。

---

## 📋 Prompt 模板

手动粘贴使用，无需安装。点击命令名查看完整模板与用法。

| 命令 | 用途 | 输入 | 输出 |
|------|------|------|------|
| [`/extract`](./prompts/extract.md) | 对话知识沉淀 + 提问元认知点评 | 当前这次对话 | 一份可直接入笔记的沉淀文档 |
| [`/weekly-review`](./prompts/weekly-review.md) | 跨文档思维模式洞察 | 本周 N 篇 对话的提问文档 | 提问惯性 / 盲点 / 训练建议 |
| [`/question-review`](./prompts/question-review.md) | 提问能力训练（只盯提问原文） | 某主题下多次对话的提问原文 | 最致命盲点 + 改写练习 |

---

## 🚀 安装使用

### 方式一：下载单个 skill

1. 进入对应的 skill 文件夹（如 [`doc-summary-zh/`](./doc-summary-zh/)）
2. 下载 `.skill` 文件
3. 打开 Claude.ai → Settings → Capabilities → Skills
4. 点击 **Upload Skill**，选择刚才下载的 `.skill` 文件
5. 根据该 skill 的 README 中的触发关键词使用

### 方式二：克隆整个仓库

```bash
git clone https://github.com/xqs-xqs/my-agent-skills.git
cd my-agent-skills
```

然后按方式一逐个上传需要的 skill。

---

## 💡 使用建议

| 场景 | 推荐做法 |
|------|----------|
| 第一次使用某个 skill | 先读该 skill 的 README |
| 触发效果不理想 | 在仓库 [Issues](https://github.com/xqs-xqs/my-agent-skills/issues) 中反馈 |
| 想自己改造 | Fork 仓库 → 修改 SKILL.md → 重新打包 |
| 希望在多台设备使用 | 登录同一 Claude 账号即可同步 |

---

## 🤝 贡献与反馈

这是一个**主要服务于个人需求**的仓库，但也欢迎：

- 🐛 **Issues**：反馈使用问题、触发异常、输出不理想的案例
- 💬 **Discussions**：交流 skill 使用心得、分享触发场景
- 🔀 **Pull Requests**：如果你基于我的 skill 做了有意义的改进，欢迎 PR

---

## 🛠️ 开发自己的 Skill

想自己写一个 skill？推荐使用 Claude 自带的 **skill-creator** 工作流：

1. 在 Claude.ai 对话框输入 `/skill-creator`
2. 描述你想要的能力
3. Claude 会引导你完成起草、测试、打包的全过程

完成后，把生成的 `.skill` 文件放进你自己的仓库即可分享。

---

## 📌 常见问题

**Q: SKILL.md 和 .skill 文件有什么区别？**

A: `SKILL.md` 是源文件（人类可读、可编辑），`.skill` 是打包后的安装文件（zip 压缩包）。编辑维护改 `SKILL.md`，分发安装用 `.skill`。

**Q: Skill 会自动触发吗？**

A: 会。Claude 根据 skill 描述中的关键词和场景自动判断。你也可以显式调用，例如说「用 xxx skill 处理这个」。

**Q: 多个 skill 会冲突吗？**

A: 不会。不同 skill 覆盖不同场景；同类场景中 Claude 会选择最匹配的那个。

**Q: 为什么有的做成 skill，有的只放 prompt？**

A: 取决于你想不想让 Claude「自动触发」。固定流程、会反复命中的做成 skill；偶尔用、需现场改参数的留作 prompt 手动粘贴更顺手。详见 [Prompt 还是 Skill？](#-prompt-还是-skill)。

**Q: 需要付费吗？**

A: 本仓库完全免费。使用 skill 本身不产生额外费用，只占用正常的 Claude 对话额度。

---

## 📜 协议

自由使用、修改、分享，请保留署名。

---

## 🌟 Star History

如果这些 skill 对你有帮助，欢迎点个 Star ⭐

---

<div align="center">

**Maintained by [@xqs-xqs](https://github.com/xqs-xqs)** · Made with Claude 🤖

</div>
