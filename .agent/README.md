# Agent 配置与能力说明

这个文件夹 `.agent` 是您的 AI 助手（Antigravity/Asher）的**核心工作台**。这里存放了所有已安装的“技能”（Skills）和“工作流”（Workflows）。

此文档用于：
1.  **记录变更**：每次安装或更新插件时，请在此更新日志。
2.  **能力速查**：快速了解目前 AI 都有哪些本事。

---

## 📝 更新日志 (Change Log)

### 2026-01-24
- **[初始化]** 建立了 `.agent` 目录结构。
- **[新增 Workflows]**:
  - `/add-skill`: 自动搜索并安装新技能。
  - `/update-skills`: 检查并更新现有技能。
- **[新增 Skills]**: 批量安装了核心开发与设计套件：
  - `vercel-labs/agent-skills` (React 最佳实践, Web 设计指南)
  - `remotion-dev/skills` (视频生成)
  - `anthropics/skills` (前端设计, PPT, PDF, 文档工具等)
  - `ui-ux-pro-max` (高级 UI/UX 设计系统, shadcn/ui 集成)
- **[配置]**: 配置了 `.agents` (源码库) 到 `.agent` (快捷方式) 的映射。

---

## 🛠️ 能力清单 (Capabilities)

### 🤖 自动化工作流 (Workflows)
| 命令 | 描述 |
| :--- | :--- |
| **`/add-skill`** | **安装新技能**。想加新功能时运行这个。 |
| **`/update-skills`** | **更新技能**。保持工具库为最新版本。 |

### ⚡️ 已安装技能 (Skills)

#### 🎨 设计与 UI
| 技能名 | 来源 | 功能描述 |
| :--- | :--- | :--- |
| **ui-ux-pro-max** | nextlevelbuilder | **高级 UI 设计系统**。提供 shadcn/ui 组件、现代化布局和 Tailwind 最佳实践。 |
| **web-design-guidelines** | Vercel | **网页设计规范**。提供排版、间距、无障碍设计等专业建议。 |
| **frontend-design** | Anthropic | **前端设计实现**。帮您写出好看、现代的 UI 代码。 |
| **canvas-design** | Anthropic | **绘图设计**。生成海报、卡片等静态视觉设计。 |
| **algorithmic-art** | Anthropic | **算法艺术**。用代码生成艺术图案 (P5.js)。 |
| **brand-guidelines** | Anthropic | **品牌一致性**。确保输出符合特定的品牌色和风格。 |
| **theme-factory** | Anthropic | **主题工厂**。快速生成或切换文档/PPT的配色主题。 |

#### 💻 编程与开发
| 技能名 | 来源 | 功能描述 |
| :--- | :--- | :--- |
| **vercel-react-best-practices** | Vercel | **React 专家**。写出高性能、无 Bug 的 Next.js/React 代码。 |
| **remotion-best-practices** | Remotion | **视频代码化**。用 React 代码来制作视频。 |
| **webapp-testing** | Anthropic | **Web 测试**。自动测试网页功能是否正常。 |
| **mcp-builder** | Anthropic | **MCP 服务器构建**。开发新的 AI 工具接口。 |

#### 📄 文档与办公
| 技能名 | 来源 | 功能描述 |
| :--- | :--- | :--- |
| **pptx** | Anthropic | **PPT 大师**。从头生成、修改 PPT，或分析 PPT 内容。 |
| **docx** | Anthropic | **Word 处理**。读取和生成 Word 文档。 |
| **xlsx** | Anthropic | **Excel 处理**。处理电子表格数据。 |
| **pdf** | Anthropic | **PDF 处理**。读取、分析 PDF 内容。 |
| **doc-coauthoring** | Anthropic | **文档共创**。辅助写长文档、标书、提案。 |

#### 🔧 工具与效率
| 技能名 | 来源 | 功能描述 |
| :--- | :--- | :--- |
| **skill-creator** | Anthropic | **技能生成器**。教 AI 怎么写新的 Skill。 |
| **slack-gif-creator** | Anthropic | **Gif 制作**。生成适合 Slack 发送的动图。 |
| **internal-comms** | Anthropic | **内部沟通**。撰写专业的周报、通知、邮件。 |
| **web-artifacts-builder** | Anthropic | **网页组件生成**。生成复杂的交互式网页组件。 |
| **template-skill** | Anthropic | **技能模板**。用于创建新技能的基础模板。 |

---

## 💡 如何使用
*   **直接提问**：例如“帮我做一个关于 AI 的 PPT”、“优化这段 React 代码”、“生成一张海报”。
*   **调用 Workflow**：输入 `/add-skill` 来增加新能力。
