# _Learn Standard (知识内化标准)

> **核心原则:**
> 1.  **拒绝有损压缩 (No Lossy Compression):** 禁止将丰富的推导过程简化为干瘪的 Bullet Points。必须保留原文的隐喻、口语化表达和思维链条。
> 2.  **原子级视觉化 (Atomic Visualization):** 每一个重要的逻辑单元（Step, Phase, Concept）**必须**搭配一个视觉化结构（表格、Mermaid、ASCII）。文字与图表是 1:1 的伴生关系，而非 1:N 的总结关系。
> 3.  **中文为主 (Chinese First):** 所有的元数据和指令必须使用中文，确保语境准确。

---

## Step 0: 预处理 (Pre-Processing)
*   **动作:** 全文阅读/收听素材。
*   **指令:**
    *   识别并提取所有 "Asher-isms" (独特的黑话/隐喻)。
    *   **Lossless Protocol (拒绝信息丢失):** 哪怕原文废话连篇，如果其中包含情绪或逻辑的起承转合，也要保留。**宁可啰嗦，不可遗漏。**
    *   **Death Command - Word Floor (死命令 - 字数底线):**
        *   输出内容字数必须至少达到原文的 **30%-40%**。
        *   **Exclusion:** 代码块、Mermaid、表格内容**不计入**字数。文字部分必须实打实达标。
        *   长篇Transcript (1万字级) 的输出**严禁低于 3000 字** (纯文字)。
        *   禁止 "Lazy Summarization" (把10句干货压缩成1句废话)。
    *   **Mandatory Examples (强制举例):** 只要出现了理论，**必须**保留或补充原文的例子。没有例子的理论是死理论。
    *   **Term Definition (术语“人话”解释):** 遇到任何专业术语（如“熵增”、“拟像”），必须在括号内用**大白话**立刻解释清楚。禁止堆砌辞藻。

## Step 0.5: 归档决策 (Integration vs Separation)
*   **目标:** 避免知识孤岛。
*   **判断逻辑:**
    *   **强关联 (Strong Link):** 如果新内容是对现有文件的补充或深化 -> **合并 (Merge)**。
    *   **弱关联 (Weak Link):** 如果是全新领域 -> **新建 (New File)**。
    *   **原则:** 优先让文件变长 (Long Context)，而非让文件变多 (Fragmentation)。逻辑的连贯性高于一切。

## Step 1: 建立框架 (Framework Layout)
*   **动作:** 复制 `_TEMPLATE.md` 到目标文件。
*   **指令:**
    *   框架必须包含：元认知 (Why)、核心架构 (What)、视觉化 (Structure)、执行协议 (How)、反模式 (Anti-Patterns)。
    *   **禁止删除模板中的任何章节**，即使没有内容，也要留空待填。

## Step 2: 深度还原 & 原子级视觉化 (Deep Context & Atomic Vis)
*   **这是最核心的步骤。** 在填充每一个章节时，必须同时进行视觉化。
*   **指令:**
    *   **文字层 (Text Layer):** 保留原文的每一个 Example、每一个反问句、 every "Why"。
        *   **Deep Reasoning (知其所以然):** 不要只记录结果 (What)，必须记录推导过程 (How & Why)。
    *   **视觉层 (Visual Layer):**
        *   **Quantity (数量):** 长文档 (>2000字) 至少 **15+** 个可视化。
        *   **Anti-Trivial Rule (拒绝凑数):**
            *   严禁 "为了画图而画图"。
            *   每一个图表必须有明确的信息增量 (Information Gain)。如果只是简单的 A->B，必须丰富其Context。
            *   严禁使用 "Generic Visuals" (空洞的框框)。
        *   **Language Rule (语言规则):**
            *   图表内可以用英文术语 (e.g., Cycle of Doom)，但**禁止纯英文**。必须中英混杂或全中文，确保阅读流畅。
        *   **Trigger Rule (触发规则):**
            *   只要出现了 >= 3 个并列要素，或者有了先后顺序，就**必须**画图。
        *   **Syntax Rule (v8.8.0 Compatible & Safe Mode):**
            *   **Edges:** 必须使用管道符语法 `-->|Label|`。严禁使用 `--"Label"-->`。
            *   **Quotes:** 节点名称若包含特殊符号(冒号/Emoji)，必须使用双引号包裹。e.g., `id["Label: Text"]`。
            *   **LaTeX Ban:** 严禁在 Mermaid 代码块中使用 `$` 符号，会引起渲染冲突。
            *   **Direction:** 优先使用 `graph TD/LR`，慎用 `flowchart`。
        *   **Format Options:**
            *   **表格 (Tables):** 用于对比 (Before/After, A vs B)、清单 (Checklist)、多维度分析。
            *   **Mermaid:** 用于流程 (Flowchart)、层级 (Mindmap)、类关系 (Class Diagram)。
            *   **ASCII Art:** 用于展示空间关系、物理结构或强调重点。

## Step 2.5: Anti-Patterns (反模式 - Teacher Mode)
*   **指令:**
    *   这一章必须写得像**老师**一样详细。
    *   禁止只写 bullet points。
    *   每个 Trap 必须包含:
        *   **Trap:** 错误的做法。
        *   **Why:** 为什么会犯错 (心理机制)。
        *   **Fix:** 如何修正。
        *   **Example/Nuance:** 具体的案例或细节。
        *   **Positive Real Scenario (正向实例):** 举一个现实中“因为做对了所以成功”的例子，证明这套逻辑的有效性 (Proof of Efficacy)。
        *   **Visual:** 每个 Trap 最好配一个图 (Matrix/Flow)。
## Step 3: 交叉验证 (Verification)
*   **动作:** 自查。
*   **Checklist:**
    *   [ ] 原文的那个绝妙的比喻还在吗？
    *   [ ] 每一个 Step 下面都有图表/表格吗？
    *   [ ] 是否所有专业术语都在 Glossary 中有定义？
    *   [ ] Anti-Patterns 是否都有正向案例 (Positive Scenario)？
    *   [ ] **Data Sync:** 是否更新了 `_Glossary_Index.json` 和 `_Formula_Index.json`？(此为 3D 可视化必须)
    *   [ ] 有没有把复杂的逻辑错误地简化成了简单的列表？
    *   [ ] 是否删除了任何原本存在的有效信息？(严禁删除！)

## Step 3.5: Metadata Sync (数据层同步)
*   **目标:** 维护 3D 知识图谱的数据源。
*   **动作:** 每次修改或新增 `.md` 文件后，**必须**同步更新同目录下的两个 JSON 文件：
    1.  `_Glossary_Index.json`: 聚合该目录下所有文件的术语。
    2.  `_Formula_Index.json`: 聚合该目录下所有文件的公式。
*   **格式:** 严格遵守 JSON 格式，确保 `source_file` 指向正确。
*   **最低数量要求:**
    | 类型 | 最低数量 | 说明 |
    | :--- | :--- | :--- |
    | **Glossary 术语** | 15+ | 挖掘文档中每一个专业概念、脑区、心理过程、方法论 |
    | **Formula 公式** | 5+ | 提炼可指导行动的思维工具，不是数学公式 |

> **原则:** 宁可多提取，不可遗漏。每个术语/公式都是 3D 图谱的一个潜在节点。

### 3.5.1 Glossary 深度标准 (Deep Glossary)
**每个术语必须包含以下字段 (为 3D 图谱 HUD 提供丰富内容):**
| 字段 | 描述 | 示例 |
| :--- | :--- | :--- |
| `term_en` | 英文术语 | "Default Mode Network" |
| `term_cn` | 中文术语 | "默认模式网络" |
| `definition_short` | 一句话定义 (人话) | "大脑的待机程序" |
| `definition_deep` | 深度解析 (3-5句, ≥80字) | 包含机制、因果、关联 |
| `why_it_matters` | 为什么重要 (与用户的关联) | "理解它能让你更好利用走神" |
| `common_mistakes` | 常见误解 | "以为刷手机是休息" |
| `related_terms` | 关联术语 (用于图谱连线) | ["TPN", "Incubation"] |
| `source_file` | 来源文件 | "Default_Mode_Network.md" |

> **Death Command:** 每个术语的 `definition_deep` 必须至少 80 字。禁止一句话带过。

### 3.5.2 Formula 深度标准 (Deep Formula)
**每个公式必须包含以下字段:**
| 字段 | 描述 | 示例 |
| :--- | :--- | :--- |
| `formula_name_en` | 英文名称 | "Creativity Generation Formula" |
| `formula_name_cn` | 中文名称 | "创意生成公式" |
| `equation` | 公式表达式 | "Creativity = Input × DMN × Connectivity" |
| `variables` | 变量定义 (对象) | { "Input": "学过的知识量", ... } |
| `mechanism` | 机制解释 (为什么这样, ≥50字) | "因为 DMN 只能处理已有知识..." |
| `application` | 应用场景 (怎么用它诊断问题) | "在卡住时用这个公式诊断..." |
| `anti_pattern` | 违反公式的后果 | "只输入不孵化→无产出" |
| `source_file` | 来源文件 | "Default_Mode_Network.md" |

> **原则:** 公式不是数学题，而是**思维工具**。每个公式都应该能指导行动。


*   **目标:** 将逻辑关系 (Logic) 转化为可交互的 3D 结构 (Structure)，而非简单的静态图表。
*   **工具:** Reference Code Sequence (`_TEMPLATE_GRAPH.html`).

### 4.1 Category Naming (领域命名 - AI 自主决策)
*   **原则:** 不同的学习模块 (Module) 应有不同的领域分类策略。**AI 负责根据新概念的语义自主创建或复用已有领域。**
*   **命名规则:**
    *   领域名称 (Group Name) 应为**英文单词或短语**，首字母大写 (e.g., "Psychology", "System", "Core", "AI")。
    *   每个领域必须同时定义 `label_en` 和 `label_cn`。
*   **颜色分配:** 使用预定义 `COLOR_PALETTE` 自动分配，无需手动指定。
*   **AI 自主权:** 当新概念无法归入现有领域时，AI 有权创建新领域并赋予合适的中英文名称。

### 4.2 Node Schema (节点数据结构 - Bilingual)
每个节点必须包含以下字段 (全部必填):
| 字段 | 类型 | 描述 |
| :--- | :--- | :--- |
| `id` | String | 唯一标识符 (English) |
| `en` | String | 英文名称 (Keyword) |
| `cn` | String | 中文名称 |
| `group` | String | 所属领域 (对应 `CATEGORY_CONFIG` 中的 Key) |
| `val` | Number | 节点大小 (重要性权重, 10-40) |
| `desc_en` | String | 英文定义 |
| `desc_cn` | String | 中文定义 |
| `notes_en` | String | 英文深度解析 (支持 `<span class='keyword'>`) |
| `notes_cn` | String | 中文深度解析 |
| `scenes_en` | Array | 英文应用场景列表 |
| `scenes_cn` | Array | 中文应用场景列表 (与 `scenes_en` 一一对应) |

### 4.3 Legend (图例 - 自动生成)
*   模板已内置 `buildLegend()` 函数，会根据 `nodes` 数组自动生成左下角图例。
*   图例显示：**领域颜色 + 中英文名称 + 节点数量**。

### 4.4 Workflow (工作流程)
1.  **Copy Template:** 复制 `Modules/_TEMPLATE_GRAPH.html` 到目标目录，重命名为 `3D_Knowledge_Graph.html`。
2.  **Configure Categories:** 在 `CATEGORY_CONFIG` 对象中定义该模块的领域分类。
3.  **Data Injection:** 填充 `nodes` 和 `links` 数组。
4.  **Validation:** 打开 HTML 检查:
    *   [ ] HUD 是否正确显示中英对照
    *   [ ] Legend 是否正确显示所有领域
    *   [ ] 节点颜色是否与领域匹配

## Appendix: Technical Pitfalls (技术避坑指南 - Post-Mortem)
*From previous failure modes.*
1.  **Mermaid Rendering Failure:**
    *   **Cause:** 使用了 Mermaid 8.8.0 不支持的 `--"Text"-->` 语法，或使用了 LaTeX 触发符 `$$`。
    *   **Fix:** 强制使用 `-->|Text|` 管道符语法。严禁在 Mermaid 代码块内使用 `$`。
    *   **Safety:** 节点名称若包含 Emoji 或冒号，必须用双引号包裹 `id["🅰️: Text"]`。
2.  **Density Failure (Lazy AI):**
    *   **Cause:** 习惯性对长文进行总结 (Summarize)，导致“知其然不知其所以然”。
    *   **Fix:** 强制执行 **Death Command** (30% Word Floor)。如果原文是 10k 字，输出必须 > 3k 字。
    *   **Process:** 长文必须分块执行 (Chunking)，禁止一次性处理全文。
3.  **Visual Anti-Pattern:**
    *   **Cause:** 为了画图而画图，画出空洞的 Generic Flowchart。
    *   **Fix:** 每一个 node 必须有具体的 Text Content，每一个 edge 必须有具体的 Logic Label。

## Summary (给 Agent 的备忘)
**When in doubt, Expand.** 
**When in doubt, Visualize.** 
用户需要的是一个**全息备份 (Digital Twin)**，而不是一份会议纪要。
算力不是瓶颈，**信息密度**的丢失才是真正的灾难。
