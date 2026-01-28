---
description: Sync Glossary/Formula terms to 3D Knowledge Graph
---

# /sync-graph - 知识图谱自动同步

> [!CAUTION]
> **零遗漏原则:** 每一个可节点化的概念都必须作为**独立节点**出现在 3D Graph 中。严禁以"整合"为由跳过任何概念。

## 触发条件
- 手动触发: `/sync-graph [模块名]`
- 完成新学习模块后自动执行

---

## 工作流程

### Step 1: 扫描目标模块
// turbo
```
1. 目标目录: Modules/[模块名]
2. 列出所有 *.md 文件 (排除 _*.md 模板)
3. 定位 3D_Knowledge_Graph.html
4. 定位 _Glossary_Index.json (如有)
```

### Step 2: 全量提取概念 (5 大类)

> [!CAUTION]
> **必须扫描以下 5 类内容，不仅仅是 Glossary！这是之前遗漏的根本原因。**

// turbo
**Category 1: 术语表 (Glossary)**
```bash
# 扫描 Glossary 区块下所有 **术语:** 格式的条目
grep -E "^\* \*\*[^*]+\*\*:" *.md
```
提取模式: `* **一人公司 (Solopreneur):** ...`

**Category 2: 公式表 (Formula Table)**
```bash
# 扫描 Formula Table 下所有公式行
grep -E "^\| \*\*[^*]+\*\*" *.md
```
提取模式: `| **Power Formula** | Force × Distance = Power |`

**Category 3: 执行阶段 (Phases)**
```bash
# 扫描所有 ### Phase X: 格式的标题
grep -E "^### Phase [0-9]" *.md
```
提取模式: `### Phase 1: Selection & Validation (选品与验证)`

**Category 4: 反模式陷阱 (Anti-Patterns / Traps)**
```bash
# 扫描所有 ### Trap X: 格式的标题
grep -E "^### Trap [0-9]" *.md
```
提取模式: `### Trap 1: The Premature Automation Trap (过早自动化陷阱)`

**Category 5: 路线/路径 (Routes / Paths)**
```bash
# 扫描所有 ### Route X: 格式的标题
grep -E "^### Route [0-9]" *.md
```
提取模式: `### Route 1: 一人公司路线 (Solopreneur Path)`

**Category 6: _Glossary_Index.json**
```javascript
// 读取 JSON 中所有 term 字段
glossaryIndex.forEach(item => concepts.push(item.term));
```

> [!IMPORTANT]
> **每一类都必须独立扫描！** 之前的问题是只扫描 Glossary 而漏掉了 Phases 和 Traps。

### Step 3: 汇总所有概念

```javascript
const allConcepts = [
    ...glossaryTerms,      // Category 1: 术语表
    ...formulaTerms,       // Category 2: 公式表
    ...phases,             // Category 3: 执行阶段
    ...traps,              // Category 4: 反模式陷阱
    ...routes,             // Category 5: 路线路径
    ...glossaryIndexTerms  // Category 6: JSON 索引
];

// 去重
const uniqueConcepts = [...new Set(allConcepts)];
```

### Step 4: 逐一对比
// turbo
```javascript
const missingNodes = [];

for (const concept of uniqueConcepts) {
    const exists = nodes.some(n => 
        n.id === concept || 
        n.en === concept || 
        n.cn === concept ||
        n.id.includes(concept) ||
        concept.includes(n.id)
    );
    
    if (!exists) {
        missingNodes.push(concept);
    }
}
```

> [!WARNING]
> **禁止以下行为:**
> - 认为"Phase 1 是 Solopreneur 的子概念"而不添加 Phase 1
> - 认为"Trap 1 和 Trap 2 语义相近"而只添加一个
> - 认为"Route 已经被 Path 覆盖"而跳过 Route

### Step 5: 按类别生成节点

**节点 Group 分配规则:**

| 概念类别 | 默认 Group | 示例 |
|---------|-----------|------|
| Glossary (术语) | 语义推断 | Marginal Cost → Capital |
| Formula (公式) | Core | Power Formula → Core |
| Phase (阶段) | System | Phase 1 Selection → System |
| Trap (陷阱) | Psychology | Premature Automation Trap → Psychology |
| Route (路线) | Capital | Capital Path → Capital |

**节点权重分配规则:**

| 概念类别 | 默认 val | 说明 |
|---------|---------|------|
| Glossary (核心术语) | 18-25 | 重要性高 |
| Formula (公式) | 18-22 | 中高 |
| Phase (阶段) | 18-22 | 执行流程节点 |
| Trap (陷阱) | 12-16 | 警示性节点 |
| Route (路线) | 20-24 | 战略选择节点 |

**节点模板 (v2.0 深度版):**
```javascript
{
    id: "ConceptID",           // 英文名或唯一标识
    en: "English Name",        // 英文全称
    cn: "中文名",              // 中文全称
    group: "Domain",           // 按上表分配
    val: 20-40,                // 按上表分配 (重要概念 → 更大)
    desc_en: "...",            // 英文定义 (简短)
    desc_cn: "...",            // 中文定义 (简短)
    notes_en: "...<span class='keyword'>关键词</span>...",  // 深度解析
    notes_cn: "...<span class='keyword'>关键词</span>...",
    why_matters: "为什么重要 (绿色框显示)",
    mistakes: "常见误区 (红色框显示)",
    related: ["RelatedNodeID1", "RelatedNodeID2"],  // 点击可跳转
    scenes_en: ["场景1", "场景2"],
    scenes_cn: ["场景1", "场景2"]
}
```

> [!TIP]
> **数据来源:** `why_matters` 和 `mistakes` 字段可从 `_Glossary_Index.json` 的 `why_it_matters` 和 `common_mistakes` 字段复制。`related` 字段可从 `related_terms` 复制。

### Step 6: 为每个新节点生成关系

**关系类型参考 (扩展版):**

| 关系 | 含义 | 常用于 |
|------|------|--------|
| Powers | 赋能 | 工具→目标 |
| Enables | 使可能 | 前置条件→结果 |
| Validates | 验证 | 测试→假设 |
| Defines | 定义 | 理论→概念 |
| Breaks | 打破 | 创新→旧模式 |
| Is Part Of | 组成部分 | 组件→整体 |
| Follows | 顺序跟随 | **Phase 2 → Phase 1** |
| Skips | 跳过 | **Trap → 对应 Phase** |
| Fixed By | 被修复 | **Trap → 修复方案** |
| Alternative To | 替代选择 | **Route 1 vs Route 2** |
| Opposite Of | 相反 | Specialist vs Synthesizer |
| Blocks | 阻碍 | Trap → 目标 |
| Requires | 需要 | 路径→前置条件 |

### Step 7: 注入到 3D Graph
// turbo
1. 在 `nodes` 数组末尾追加所有新节点
2. 在 `links` 数组末尾追加所有新关系
3. 保存文件

### Step 8: 验证

> [!CAUTION]
> **必须报告每个类别的覆盖情况！**

// turbo
```
╔════════════════════════════════════════════════════════════╗
║                   /sync-graph 完成报告                      ║
╠════════════════════════════════════════════════════════════╣
║ 类别                  │ 提取数 │ 已有 │ 新增 │ 覆盖率      ║
╠═══════════════════════╪════════╪══════╪══════╪═════════════╣
║ Category 1: Glossary  │   20   │  18  │   2  │ 100% ✓     ║
║ Category 2: Formula   │    3   │   3  │   0  │ 100% ✓     ║
║ Category 3: Phases    │    4   │   0  │   4  │ 100% ✓     ║
║ Category 4: Traps     │    7   │   1  │   6  │ 100% ✓     ║
║ Category 5: Routes    │    2   │   1  │   1  │ 100% ✓     ║
╠═══════════════════════╧════════╧══════╧══════╧═════════════╣
║ 总计                  │   36   │  23  │  13  │ 100% ✓     ║
╠════════════════════════════════════════════════════════════╣
║ 新增关系: 24                                                ║
║ 最终节点: 66                                                ║
║ 最终关系: 100                                               ║
╚════════════════════════════════════════════════════════════╝
```

---

## 执行标准

| 检查项 | 要求 |
|--------|------|
| 术语覆盖率 | **100%** |
| Phase 覆盖率 | **100%** |
| Trap 覆盖率 | **100%** |
| Route 覆盖率 | **100%** |
| 节点格式 | 必须包含 bilingual 双语字段 |
| 深度字段 | 每个节点必须有 `why_matters` 和 `mistakes` |
| related 字段 | 每个节点至少 1 个关联 |
| 关系数量 | 每个新节点至少 1 条关系 |
| 禁止合并 | 即使语义相近也必须分开 |

---

## 常见遗漏检查清单

执行 `/sync-graph` 后，**必须逐项检查**以下内容是否全部添加为节点：

- [ ] `## Glossary` 下的每个 `* **术语:**` → 节点
- [ ] `## Formula Table` 下的每个 `| **公式** |` → 节点
- [ ] `### Phase X:` 每个阶段标题 → 节点
- [ ] `### Trap X:` 每个陷阱标题 → 节点
- [ ] `### Route X:` 每个路线标题 → 节点
- [ ] `_Glossary_Index.json` 每个 `term` → 节点

---

## 故障排除

**Q: 为什么之前总是漏掉 Phases 和 Traps？**
A: 旧版工作流只扫描 Glossary 区块，没有扫描 `### Phase` 和 `### Trap` 标题。新版已修复。

**Q: 为什么节点比术语多？**
A: 允许。节点 = Glossary + Formulas + Phases + Traps + Routes。

**Q: 有些概念已经隐含在其他节点中？**
A: 仍然添加。例如 "Imposter Syndrome" 是一个 Trap，同时也是一个 Glossary 术语，两个来源合并为一个节点即可，但不能因为已有一个就跳过另一个。

---

## ⚠️ 常见导致 Force Graph 失效的错误

> [!CAUTION]
> **以下错误会导致图谱节点堆在中间、无法正常展开！** 执行 `/sync-graph` 后必须检查。

### 错误类型 1: Links 指向不存在的节点

**症状:** 图谱节点全部聚集在中心无法展开

**错误示例:**
```javascript
// ❌ 错误: 没有 id: "Science" 的节点
{ source: "Capital", target: "Science", label: "Invests in" }

// ✅ 正确: 改用已存在的节点 ID
{ source: "Capital", target: "Scientific_Revolution", label: "Invests in" }
```

**检查方法:**
```bash
# 在 links 数组中找到的所有 target 值
grep -oE 'target: "[^"]+"' 3D_Knowledge_Graph.html | sort | uniq

# 对比 nodes 数组中的 id 值
grep -oE 'id: "[^"]+"' 3D_Knowledge_Graph.html | sort | uniq

# 找出差异 = 不存在的节点引用
```

### 错误类型 2: related 字段引用拼写错误

**症状:** 点击关联术语时找不到节点

**错误示例:**
```javascript
// ❌ 错误: 少了一个 s
related: ["Happines_Formula", "Agricultural_Revolution"]

// ✅ 正确:
related: ["Happiness_Formula", "Agricultural_Revolution"]
```

**检查方法:** 在浏览器 DevTools Console 中点击 related tag，报错则说明 ID 不存在。

### 错误类型 3: 物理参数被过度调整

**症状:** 节点过度聚集或过度分散

**正确的默认配置 (与模板保持一致):**
```javascript
const settings = { 
    linkDistance: 80,       // 不要改太大（如 250）
    chargeStrength: -200,   // 不要改太负（如 -2000）
    labelSize: 1.0, 
    opacity: 0.8, 
    autoRotate: true 
};
```

### 错误类型 4: 添加了不必要的 d3-force 扩展

**症状:** 节点无法正常受力展开

**错误示例:**
```html
<!-- ❌ 不要添加这个 -->
<script src="https://unpkg.com/d3-force@3"></script>
```

**原则:** 除非特别需要，不要添加额外的力导向库。模板的默认配置已足够。

### 快速验证检查表

执行 `/sync-graph` 后，按顺序检查：

1. [ ] **所有 links 的 target 都指向存在的节点 ID**
2. [ ] **所有 nodes 的 related 数组中的 ID 都存在**
3. [ ] **settings 配置与模板一致** (`linkDistance: 80, chargeStrength: -200`)
4. [ ] **没有添加额外的 d3-force 库**
5. [ ] **刷新浏览器 (Cmd+Shift+R) 后图谱正常展开**

