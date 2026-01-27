>
> **核心理念:** 把"状态最好时的思考"外化、结构化存储，让"状态不好时的我"可以随时调用。AI 接管"怎么做"，人类守护"为什么做"。
>
> **Version:** v2.0 | Updated: 2026-01-26

---

## 一、系统全景

```
修荷/
│
├── Asher_Source_Profile_v1/    ← 内部能力（我是谁、我会什么、我有什么）
├── AI_Skills_Library/          ← 外部技能（23个通用 AI Skills）
├── Projects/                   ← 产品与项目（Asyre、vibe-kanban 等）
├── Content/                    ← 内容输出
├── Quests/                     ← 外部任务（赏金/支线/代练）
│
├── skill-mcp-server/           ← MCP 服务器（Claude App 集成）
├── skill-index.md              ← 技能索引导航
└── vibe-kanban/                ← vibe-kanban 开发快捷入口
```

---

## 二、系统目的

### 解决什么问题？

**问题:** 人的状态是波动的。疲惫、情绪低落、信息过载时，决策质量会大幅下降。但"状态最好的我"曾经想清楚过很多事情——这些思考如果不记录下来，下次遇到类似情况又要从头想。

**解决方案:**
1. **内部能力外化** — 把个人的记忆、技能、思维模型结构化存储
2. **外部能力接入** — 通过 AI Skills 和产品能力放大执行效率
3. **系统集成** — 通过 MCP 服务器让 AI 能随时调用这些能力

### 两个核心角色

| 角色 | 功能 | 使用场景 |
|------|------|----------|
| **内在顾问** | 当我困惑时，告诉我"状态最好的我会怎么做" | 决策、情绪低落、方向迷失 |
| **数字分身** | 代替我执行已经想清楚的事情 | 写作、分析、重复性认知任务 |

### 核心对话模式

```
我: "如果是状态最好的我，现在会怎么做？"
系统: [调用相关模块] → 给出建议
```

---

## 三、内部能力 (Asher_Source_Profile_v1)

**定位:** 个人的"源代码"——记忆、能力、逻辑、资产的结构化存储。

### 3.1 目录结构

```
Asher_Source_Profile_v1/
│
├── 00_System_Manifesto.md      ← 系统功能说明（入口）
├── 00_Archive/                 ← 档案存储
│   ├── Meeting_Notes/          ← 会议记录（含 AI 讨论、商业讨论）
│   └── Raw_Transcripts/        ← 原始对话记录
├── 00_Inbox/                   ← 待处理收件箱
│
├── 01_Base_Attributes/         ← 我是谁（性格、认知特征、审美）
├── 02_Skill_Tree/              ← 我会什么（技能模块库）
├── 03_Inventory_Assets/        ← 我有什么（资产、人脉、文件）
├── 04_Strategy_Models/         ← 我怎么想（战略模型、商业计划）
├── 05_Protocols/               ← 我怎么做（执行协议、决策树）
├── 06_Consciousness_Stream/    ← 我在想什么（意识流日志）
│
└── .agent/                     ← 自动化工作流配置
    └── workflows/              ← 可调用的标准流程
```

### 3.2 各目录用途

| 目录 | 存什么 | 什么时候用 |
|------|--------|------------|
| `01_Base_Attributes/` | 性格、认知模式、优缺点 | 需要了解"我是什么样的人"时 |
| `02_Skill_Tree/` | 技能模块、知识文档 | 需要调用某个能力时 |
| `03_Inventory_Assets/` | 证件、合同、人脉、财务 | 需要查找具体资料时 |
| `04_Strategy_Models/` | 商业计划、思维模型 | 需要战略层面的参考时 |
| `05_Protocols/` | 决策流程、执行标准 | 需要知道"遇到X怎么办"时 |
| `06_Consciousness_Stream/` | 原始想法、灵感记录 | 需要追溯思考脉络时 |

### 3.3 技能模块系统 (02_Skill_Tree)

**当前主要模块（21个）:**

| 类别 | 模块 | 用途 |
|------|------|------|
| **内容创作** | Content_Creation | 口播风格、Hook技术、视频语言、平台分发策略 |
| **商业** | Business | 商业与资本运作 |
| **合同** | Contract_Warfare | 合同攻防、风险识别 |
| **哲学** | Philosophy | 蜕升世界观、价值观 |
| **心理学** | Psychology | 心理学理论与应用 |
| **逻辑** | Logic_and_Reasoning | 逻辑推理框架 |
| **投资** | Investment_Trading | 投资交易策略 |
| **社会观察** | China_Social_Observation | 中国社会现象分析 |
| **政治经济** | Political_Economy | 政治经济学 |
| **技术** | Tech | 技术能力 |
| **生存** | Survival | 生存技能 |
| **艺术** | Arts | 艺术相关 |

### 3.4 Workflows 工作流

**位置:** `.agent/workflows/`

| 类别 | 命令 | 功能 |
|------|------|------|
| **知识管理** | `/learn` | 学习新内容 → 生成标准文档 |
| | `/fact-check` | 核查并补充知识 |
| | `/synthesize` | 整合多个文档 |
| **会议处理** | `/raw-transcript` | 保存原始对话 |
| | `/meeting-analysis` | 深度分析会议 |
| | `/distill-discussion` | 提炼讨论要点 |
| **内容创作** | `/asyre` | Asyre 内容创作系统 |
| | `/create-script` | 创作脚本 |
| **工具** | `/export-pdf` | 导出PDF |
| | `/analyze-contract` | 分析合同 |

---

## 四、外部赋能 (AI_Skills_Library)

**定位:** 从外部下载/收集的通用 AI 技能，可被任何 AI 平台调用。

### 4.1 目录结构

```
AI_Skills_Library/
├── PROTOCOL.md                 ← 技能使用协议
├── manage-skills.sh            ← 技能管理脚本
│
├── .agents/                    ← 通用技能库（23个技能）
│   └── skills/
│       ├── pdf/                ← PDF 处理
│       ├── docx/               ← Word 文档处理
│       ├── pptx/               ← PPT 处理
│       ├── xlsx/               ← Excel 处理
│       ├── ui-ux-pro-max/      ← UI/UX 设计
│       ├── frontend-design/    ← 前端设计
│       ├── web-design-guidelines/ ← Web 设计指南
│       ├── mcp-builder/        ← MCP 构建器
│       ├── skill-creator/      ← 技能创建器
│       └── ...                 ← 更多技能
│
├── .claude/                    ← Claude 专用（链接到 .agents）
├── .cursor/                    ← Cursor 编辑器
├── .codex/                     ← OpenAI Codex
└── .gemini/                    ← Google Gemini
```

### 4.2 技能清单（23个）

| 技能 | 功能 |
|------|------|
| `pdf` | PDF 文档处理与生成 |
| `docx` | Word 文档处理 |
| `pptx` | PowerPoint 处理 |
| `xlsx` | Excel 处理 |
| `html-presentation` | HTML 演示文稿创建 |
| `ui-ux-pro-max` | UI/UX 专业设计 |
| `frontend-design` | 前端设计规范 |
| `web-design-guidelines` | Web 设计指南 |
| `canvas-design` | Canvas 设计 |
| `brand-guidelines` | 品牌指南 |
| `theme-factory` | 主题工厂 |
| `algorithmic-art` | 算法艺术 |
| `doc-coauthoring` | 文档协作写作 |
| `internal-comms` | 内部沟通 |
| `mcp-builder` | MCP 服务器构建 |
| `skill-creator` | 技能创建工具 |
| `template-skill` | 技能模板 |
| `remotion-best-practices` | Remotion 视频最佳实践 |
| `vercel-react-best-practices` | Vercel/React 最佳实践 |
| `web-artifacts-builder` | Web 构件构建 |
| `webapp-testing` | Web App 测试 |
| `slack-gif-creator` | Slack GIF 创建 |

### 4.3 技能使用方式

```
1. 发现技能 → 扫描 AI_Skills_Library/.agents/skills/
2. 读取技能 → 读取 {技能名}/SKILL.md
3. 执行技能 → 按照 SKILL.md 中的指令执行
```

---

## 五、产品与项目 (Projects)

### 5.1 Asyre — 非对称内容创作系统 (v2.9)

**定位:** 意图驱动的内容创作引擎，核心理念"内容价值 = 人的不可替代性 × AI 的放大效率"。

**创作哲学:** "雕刻大卫" — 初稿就要有灵魂，雕刻只是去冗余。

**核心创新:**

1. **意图因子系统** — 13个意图因子驱动参数推导
   - value_guidance（价值观引导）
   - persuasion（观点说服）
   - concept_clarification（概念澄清）
   - emotional_resonance（情感共鸣）
   - cognitive_disruption（认知颠覆）
   - ...

2. **七层质量公式**
   ```
   Q = T_gate × Σ(wi × Fi)

   T (可信度) — 门槛层，< 0.70 则归零
   E (经验专业) — 护城河 31.7%
   C (深度判断) — 护城河 25.7%
   F (受众匹配) — 放大器 14.0%
   D (表达能力) — 放大器 16.0%
   A (执行质量) — 放大器 9.3%
   B (时机把控) — 放大器 3.3%
   ```

3. **六阶段创作流程**
   1. 意图解析 — 分析主题的意图因子组合
   2. 参数推导 — 输出关键参数（启发，不是约束）
   3. 自由创作 — 初稿即高质量
   4. 七层评价 — 质量公式评分
   5. 雕刻修正 — 去冗余 10-20%
   6. 精修审核 — 质量提升轨迹报告

4. **创作者画像系统** (v2.9 新增)
   - 定制化配置文件
   - 6维度画像模板
   - 渐进式对话构建画像

**使用方式:**
```bash
/asyre 写一篇关于"为什么年轻人不想上班"的口播稿
```

### 5.2 vibe-kanban — 任务管理系统

**技术栈:** Rust (后端) + React/TypeScript (前端)

**功能:** 项目任务管理、看板视图、工作空间

**位置:** `Projects/vibe-kanban/`（完整项目）

### 5.3 situation-monitor — 态势监控

**技术栈:** Svelte + TypeScript

**功能:** 态势感知与监控

---

## 六、任务系统 (Quests)

**定位:** 使用修荷系统资源的外部"游戏任务"分类系统。

### 6.1 任务类别

| 类别 | 定义 | 目标 | 示例 |
|------|------|------|------|
| **💰 Bounties** (赏金) | 解决问题即获酬 | 即时现金流 | 咨询、外包、一次性服务 |
| **📜 Side_Quests** (支线) | 战略性任务 | 声誉、人脉、经验 | 帮助合作伙伴、作品集项目 |
| **🛡 Power_Leveling** (代练) | 纯支持/合作 | 利他、帮助朋友 | 技术支持、无偿建议 |

### 6.2 与系统的整合

- 任务执行时可调用 `Asher_Source_Profile_v1/` 的能力
- 任务产出存入 `Content/` 或相应项目

---

## 七、系统集成 (skill-mcp-server)

**功能:** 让 Claude Desktop 应用能够读取本地 AI Skills Library 和个人工作流。

### 7.1 提供的工具

| 工具 | 功能 |
|------|------|
| `list_skills` | 列出所有可用的技能和工作流 |
| `use_skill` | 加载指定技能的完整内容 |
| `read_file` | 读取技能库目录内的任意文件 |

### 7.2 扫描的目录

1. **AI Skills Library** — `AI_Skills_Library/.agents/skills/`
2. **Asher Workflows** — `Asher_Source_Profile_v1/.agent/workflows/`

### 7.3 配置方式

编辑 `~/Library/Application Support/Claude/claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "skill-server": {
      "command": "node",
      "args": ["/path/to/修荷/skill-mcp-server/index.js"]
    }
  }
}
```

详见: `skill-mcp-server/README.md`

---

## 八、内容输出 (Content)

**定位:** 内部能力 + 外部赋能 → 产出的最终内容。

当前内容:
- `AI时代的阶级断裂_口播稿.md`

---

## 九、能力整合架构

```
┌──────────────────────────────────────────────────────────────────────┐
│                         修荷系统 v2.0                                 │
├──────────────────────────────────────────────────────────────────────┤
│                                                                       │
│   ┌─────────────────────┐        ┌─────────────────────┐            │
│   │    内部能力          │        │    外部赋能          │            │
│   │    (Internal)       │        │    (External)       │            │
│   ├─────────────────────┤        ├─────────────────────┤            │
│   │ • 01 属性 (我是谁)   │        │ • AI Skills (23个)  │            │
│   │ • 02 技能树 (我会啥) │        │ • 多平台支持         │            │
│   │ • 03 资产库 (我有啥) │        │                     │            │
│   │ • 04 战略模型        │        ├─────────────────────┤            │
│   │ • 05 执行协议        │        │ 产品能力            │            │
│   │ • 06 意识流          │        │ • Asyre v2.9       │            │
│   │ • Workflows          │        │ • vibe-kanban      │            │
│   └──────────┬──────────┘        │ • situation-monitor│            │
│              │                    └──────────┬──────────┘            │
│              │                               │                       │
│              └───────────────┬───────────────┘                       │
│                              │                                       │
│   ┌──────────────────────────┼──────────────────────────┐           │
│   │                          ▼                          │           │
│   │              系统执行与整合                          │           │
│   │           (Integration Engine)                     │           │
│   │   ┌────────────────────────────────────────────┐   │           │
│   │   │ • skill-mcp-server (Claude 集成)           │   │           │
│   │   │ • Asyre 意图推导引擎                        │   │           │
│   │   │ • Quests 任务分类系统                       │   │           │
│   │   └────────────────────────────────────────────┘   │           │
│   └──────────────────────────┬──────────────────────────┘           │
│                              │                                       │
│                              ▼                                       │
│                 ┌───────────────────────┐                           │
│                 │      内容输出          │                           │
│                 │      (Content/)       │                           │
│                 │  • 口播稿、文章、视频  │                           │
│                 └───────────────────────┘                           │
│                                                                       │
└──────────────────────────────────────────────────────────────────────┘
```

---

## 十、使用场景示例

### 场景1: 写一篇口播稿

```
1. 调用内部能力
   - 02_Skill_Tree/Modules/Content_Creation/ — 口播风格、Hook 技术
   - 02_Skill_Tree/Modules/Philosophy/ — 世界观素材

2. 调用外部赋能
   - Projects/Asyre/ — 意图推导 + 七层质量评估
   - AI_Skills_Library — 如需要特定格式处理

3. 产出内容
   - 输出到 Content/ — 最终口播稿
```

### 场景2: 处理一个付费咨询任务

```
1. 创建任务
   - Quests/Bounties/ — 记录任务详情

2. 调用能力
   - 02_Skill_Tree/ — 相关领域技能模块
   - 03_Inventory_Assets/ — 相关资料

3. 执行并产出
   - 使用 Workflows 标准流程
   - 输出交付物
```

### 场景3: 状态不好时做决策

```
我: "如果是状态最好的我，现在会怎么做？"

系统调用:
- 01_Base_Attributes/ — 了解认知倾向
- 05_Protocols/ — 查找相关决策协议
- 04_Strategy_Models/ — 参考战略模型

输出: 基于"最好状态的我"的思考框架给出建议
```

---

## 十一、快速导航

| 我想... | 去哪里 | 关键文件 |
|---------|--------|----------|
| 了解这个系统怎么用 | 你在这里 | `README.md` |
| 了解"我是谁" | Asher_Source_Profile_v1 | `00_System_Manifesto.md` |
| 调用我自己的技能 | Asher_Source_Profile_v1/02_Skill_Tree | 各模块 `.md` |
| 使用外部 AI Skills | AI_Skills_Library | `.agents/skills/` |
| 使用 Asyre 创作内容 | Projects/Asyre | `/asyre` 命令 |
| 管理任务 | Projects/vibe-kanban | 完整项目 |
| 分类外部任务 | Quests | Bounties/Side_Quests/Power_Leveling |
| 集成到 Claude App | skill-mcp-server | `README.md` |
| 查看已产出的内容 | Content | 输出物 |
| 查找技能索引 | 根目录 | `skill-index.md` |

---

## 十二、扩展方向

### 内部能力扩展
- 持续将新的经验、思考写入 `Asher_Source_Profile_v1/`
- 新技能封装为模块存入 `02_Skill_Tree/Modules/`
- 每发现重复的认知流程 → 封装为新 Workflow

### 外部赋能扩展
- 发现好用的 AI Skills → 存入 `AI_Skills_Library/`
- 开发新产品 → 存入 `Projects/`

### 系统集成扩展
- 优化 MCP 服务器功能
- 增加更多 AI 平台支持

---

## 十三、版本历史

| 版本 | 日期 | 变更 |
|------|------|------|
| v1.0 | 2026-01-24 | 初始版本，基础架构说明 |
| v2.0 | 2026-01-26 | 完整架构文档：新增 Quests 任务系统说明、skill-mcp-server 集成说明、Asyre v2.9 详细介绍、完整技能清单、系统整合架构图、使用场景示例 |

---

*Last Updated: 2026-01-26*
=======
# xiu-he
修荷的完整能力操作系统——融合内部能力（个人记忆、技能、资产）、外部赋能（AI Skills、产品能力）、与执行系统（MCP 服务器、任务管理），用于内容创作、项目执行与个人进化。
