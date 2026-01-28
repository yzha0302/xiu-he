# Getting Started / 使用指南

> 如何使用修荷系统构建你自己的数字分身。

---

## 这是什么？

修荷是一个**个人能力操作系统**。它把你的记忆、技能、思维模型结构化存储，让 AI 成为你的思维外骨骼。

你将获得：
- **Asher 的共享知识库** — 内容创作、商业、哲学、心理学等 20+ 个技能模块
- **Asyre 内容创作引擎** — 意图驱动的创作系统
- **23 个通用 AI 技能** — PDF/Word/PPT/设计等工具
- **你自己的 Profile** — 属于你的性格、认知、技能数据

---

## Quick Start

### Step 1: Clone

```bash
git clone https://github.com/YixuanZhang/xiu-he.git
cd xiu-he
```

### Step 2: 构建你的 Profile

用 Claude Code 或任何 AI 助手打开项目，然后说：

```
"我想构建自己的 Profile。请先读取
Asher_Source_Profile_v1/01_Base_Attributes/_PROFILE_INIT_PROTOCOL.md，
然后引导我完成。"
```

AI 会：
1. 通过自然对话了解你的性格、认知方式、审美偏好、社交风格
2. 在 `01_Base_Attributes/{你的用户名}/` 下创建你的 Profile 文件
3. 在 `02_Skill_Tree/Users/{你的用户名}/` 下初始化你的技能库

**不需要一次完成。** 可以分多次对话逐步补充。

### Step 3: 开始使用

构建完 Profile 后，你可以：

**调用共享知识库:**
```
"帮我用 Content_Creation 模块写一篇口播稿"
"参考 Business 模块帮我分析这个商业模式"
```

**使用 Asyre 创作:**
```
"用 Asyre 帮我写一篇关于 {主题} 的文章"
```

**创建你自己的技能模块:**
```
"我想在我的技能树里添加一个 {领域} 模块"
```

**使用通用 AI 技能:**
```
"用 pdf 技能处理这个文档"
"用 pptx 技能帮我做演示文稿"
```

---

## 系统架构

```
xiu-he/
│
├── Asher_Source_Profile_v1/          ← 核心系统
│   ├── 01_Base_Attributes/
│   │   ├── _PROFILE_INIT_PROTOCOL.md ← AI 读此引导你构建 Profile
│   │   ├── _TEMPLATES/               ← 空白模板
│   │   ├── 1.1-1.4 (Asher的)        ← 参考案例
│   │   └── {你的用户名}/             ← 你的 Profile
│   │
│   └── 02_Skill_Tree/
│       ├── Modules/                   ← 共享知识库（所有人可用）
│       └── Users/{你的用户名}/        ← 你的专属技能
│
├── AI_Skills_Library/                 ← 23个通用 AI 技能
├── Projects/Asyre/                    ← 内容创作引擎
├── Quests/                            ← 任务管理
└── skill-mcp-server/                  ← Claude App 集成
```

### 共享 vs 专属

| 类型 | 内容 | 你可以... |
|------|------|----------|
| **共享** | `02_Skill_Tree/Modules/` | 调用，但不修改 |
| **共享** | `AI_Skills_Library/` | 调用 |
| **共享** | `Projects/Asyre/` | 使用，配置自己的画像 |
| **专属** | `01_Base_Attributes/{你}/` | 创建、修改、删除 |
| **专属** | `02_Skill_Tree/Users/{你}/` | 创建、修改、删除 |

---

## 可选：集成 Claude Desktop

如果你使用 Claude Desktop App，可以通过 MCP 服务器让 Claude 直接调用技能库。

### 安装

```bash
cd skill-mcp-server
npm install
```

### 配置

编辑 `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "skill-server": {
      "command": "node",
      "args": ["/你的路径/xiu-he/skill-mcp-server/index.js"]
    }
  }
}
```

重启 Claude Desktop 即可。

详见: `skill-mcp-server/README.md`

---

## FAQ

### Q: 我需要了解 Asher 的全部内容吗？
**不需要。** Asher 的 Profile 是参考案例。你只需要构建自己的 Profile，然后按需调用共享知识库。

### Q: 我可以修改共享知识库吗？
**不建议。** `02_Skill_Tree/Modules/` 由 Asher 维护。如果你有独特知识，请创建在 `02_Skill_Tree/Users/{你}/` 下。

### Q: Profile 需要一次写完吗？
**不需要。** 系统支持渐进式构建。先完成 Character Stats（约 30 分钟对话），其余的慢慢补充。

### Q: 我可以同时使用 Asher 的知识和自己的技能吗？
**这正是设计目的。** 你的专属技能 + Asher 的共享知识库 = 更强的组合能力。

---

*Last Updated: 2026-01-28*
