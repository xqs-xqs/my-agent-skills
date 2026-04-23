

<div align="center">

# 🧰 my-agent-skills

> 一个个人维护的 Claude Skills 收藏仓库
>
> 分享一些在日常学习、工作、阅读中真正好用的 skill。


**🌐 Language**: **简体中文** | [English](./README.en.md)

</div>
  
---

## 📖 目录

- [什么是 Skill](#-什么是-skill)
- [仓库结构](#-仓库结构)
- [Skill 列表](#-skill-列表)
- [安装使用](#-安装使用)
- [使用建议](#-使用建议)
- [贡献与反馈](#-贡献与反馈)
- [开发自己的 Skill](#-开发自己的-skill)
- [常见问题](#-常见问题)
- [协议](#-协议)

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
└── docs/                         # 通用文档
    ├── how-to-install.md         # 安装教程
    └── how-to-create.md          # 如何创建自己的 skill
```

**设计原则**

- 每个 skill 独立一个文件夹，文件夹名 = skill 的 `name` 字段
- 每个 skill 同时提供 `SKILL.md`（可读可编辑）和 `.skill`（一键安装）
- 各 skill 有自己的 README，说明独特用法

---

## 📚 Skill 列表

| Skill | 功能 | 语言 | 适用场景 | 状态 |
|-------|------|------|----------|------|
| [`doc-summary-zh`](./doc-summary-zh/) | 技术/课程文档结构化深度总结 | 🇨🇳 中文 | 课件、技术文档、学术讲义 | ✅ v1.0 |

*更多 skill 正在路上……*

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

**Q: 需要付费吗？**

A: 本仓库完全免费。使用 skill 本身不产生额外费用，只占用正常的 Claude 对话额度。

---

## 📜 协议

[MIT License](./LICENSE) — 自由使用、修改、分享，请保留署名。

---

## 🌟 Star History

如果这些 skill 对你有帮助，欢迎点个 Star ⭐

---

<div align="center">

**Maintained by [@xqs-xqs](https://github.com/xqs-xqs)** · Made with Claude 🤖

</div>
