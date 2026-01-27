---
description: 学习新内容并生成标准化知识文档 + 3D 图谱
---

# /learn - 知识内化工作流

> **触发方式:** `/learn [模块名] [素材来源]`
> **示例:** `/learn AI_Agent_Revolution 附件是课程transcript`

---

## 配置文件 (动态引用)

> [!IMPORTANT]
> **本工作流的所有标准都来自以下三个文件。** 修改这些文件会自动改变后续执行效果。

| 文件 | 用途 | 路径 |
|------|------|------|
| **_Learn standard.md** | 执行标准 (字数底线/视觉化要求) | `Modules/_Learn standard.md` |
| **_TEMPLATE.md** | 文档结构模板 | `Modules/_TEMPLATE.md` |
| **_TEMPLATE_GRAPH.html** | 3D 图谱模板 | `Modules/_TEMPLATE_GRAPH.html` |

**Execution Lock (执行锁):** 
在开始任何工作之前，**必须**显式调用 `view_file` 读取上述三个文件的**原始内容**。
**严禁**凭记忆或近似值操作。

---

## 工作流程

### Phase 0: 强制预检 (Pre-Flight Check)
// turbo
```
1. view_file: Modules/_Learn standard.md -> 获取执行规则
2. view_file: Modules/_TEMPLATE.md -> 获取文档结构
3. view_file: Modules/_TEMPLATE_GRAPH.html -> 获取图谱代码
4. 初始化 task.md -> 包含 "Verify Standard Compliance" 检查项
```

### Phase 1: 预处理 (Pre-Processing)
// turbo
**严格按照 `_Learn standard.md` Step 0 执行:**
- 全文阅读素材
- 识别 Asher-isms (独特隐喻)
- 计算原文字数 -> 设定输出下限 (30%)
- 提取所有专业术语

### Phase 2: 归档决策 (Structure)
```
IF 内容是现有文件的补充/深化:
    -> 合并到现有 .md 文件
ELSE:
    -> 创建新 .md 文件，命名规则: [序号]_[Module_Name].md
```

### Phase 3: 框架建立 (Framework)
// turbo
```
1. 复制 _TEMPLATE.md 到目标文件 (COPY-PASTE EXACTLY)
2. 填充元数据 (Tags, Date, 一句话总结)
3. 禁止删除模板中的任何章节
```

### Phase 4: 深度还原 (Deep Context)
**同时执行文字层和视觉层:**

**文字层:**
- 保留每一个 Example
- 保留每一个 Why
- 保留每一个隐喻
- 术语必须配"人话"解释

**视觉层 (数量要求):**
| 文档长度 | 最低视觉化数量 |
|---------|---------------|
| < 2000 字 | 8+ |
| 2000-5000 字 | 12+ |
| > 5000 字 | 15+ |

**视觉化规则 (从 Standard 读取):**
- 使用 `-->|Label|` 管道符语法
- 节点名称含特殊符号用双引号包裹
- 禁止 LaTeX ($) 符号
- 优先 `graph TD/LR`

### Phase 5: Anti-Patterns (Teacher Mode)
**每个陷阱必须包含:**
```
- Trap: 错误做法
- Why: 心理机制
- Fix: 修正方法
- Example: 具体案例
- Positive Real Scenario: 成功案例
- Visual: 配图 (可选但推荐)
```

### Phase 6: STRICT QUALITY GATE (强制质检)
**STOP AND CHECK (必须停下来检查):**

1. **Word Count Check:** 输出字数 (不含代码/图表) 是否 > 原文的 30%?
    - NO -> **重写** (Refuse to complete task until met)
2. **Template Check:** 是否包含了 Anti-Patterns, Glossary, Formula Table?
    - NO -> **补全**
3. **Graph Code Check:** 3D 图谱代码是否使用了 *TEMPLATE_GRAPH.html* 的结构?
    - NO -> **重写**

### Phase 7: 数据层同步 (Data Sync)
// turbo
```
1. 更新 _Glossary_Index.json (追加新术语)
2. 更新 _Formula_Index.json (追加新公式)
3. 格式: 严格 JSON，source_file 指向正确
```

**最低数量要求:**
| 类型 | 最低数量 | 说明 |
|------|---------|------|
| Glossary 术语 | **15+** | 挖掘每一个专业概念 |
| Formula 公式 | **5+** | 提炼思维工具 |

**Glossary 深度字段 (每条必填):**
```json
{
  "term_en": "英文术语",
  "term_cn": "中文术语",
  "definition_short": "一句话定义",
  "definition_deep": "深度解析 (≥80字)",
  "why_it_matters": "为什么重要",
  "common_mistakes": "常见误解",
  "related_terms": ["关联术语1", "关联术语2"],
  "source_file": "xxx.md"
}
```

**Formula 深度字段 (每条必填):**
```json
{
  "formula_name_en": "英文名",
  "formula_name_cn": "中文名",
  "equation": "公式表达式",
  "variables": { "变量": "定义" },
  "mechanism": "为什么这样 (≥50字)",
  "application": "怎么用",
  "anti_pattern": "违反后果",
  "source_file": "xxx.md"
}
```

### Phase 8: 3D 图谱 (Knowledge Graph)
**必须使用 `_TEMPLATE_GRAPH.html` 的 RAW CODE:**
```
1. 复制 _TEMPLATE_GRAPH.html -> 3D_Knowledge_Graph.html
2. 配置 CATEGORY_CONFIG (领域分类)
3. 填充 nodes 和 links 数组
4. 验证 HUD / Legend / 颜色
```

**节点深度字段 (v2.0):**
```javascript
{
    id: "ConceptID",
    en: "English Name",
    cn: "中文名",
    group: "Domain",
    val: 20-40,
    desc_en: "英文定义",
    desc_cn: "中文定义",
    notes_en: "深度解析 (带 <span class='keyword'>高亮</span>)",
    notes_cn: "中文深度解析",
    why_matters: "为什么重要 (显示在绿色框)",
    mistakes: "常见误区 (显示在红色框)",
    related: ["关联节点ID", "点击可跳转"],
    scenes_en: ["场景1", "场景2"],
    scenes_cn: ["场景1", "场景2"]
}
```

### Phase 9: 最终报告
// turbo
```
输出统计:
- 原文字数: X
- 输出字数: Y (比例: Y/X %)
- 视觉化数量: Z
- Anti-Patterns: N
- 新增 Glossary 术语: M (≥15)
- 新增 Formula 公式: F (≥5)
- 3D 节点: P
- 3D 关系: R
```

---

## 故障排除

**Q: 视觉化渲染失败**
A: 检查 Mermaid 语法是否符合 v8.8.0 标准 (参考 `_Learn standard.md` Appendix)

**Q: 输出太短**
A: 触发 Death Command，分块处理 (Chunking)

**Q: 3D 图谱节点缺失**
A: 执行 `/sync-graph` 并检查 100% 覆盖率
