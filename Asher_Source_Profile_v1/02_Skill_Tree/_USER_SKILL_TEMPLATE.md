# User Skill Module Template (用户技能模块模板)

> **AI 协作者必读**: 当用户要求创建自己的技能模块时，参考此文件。

---

## 一、共享 vs 专属

### 共享知识库 (所有用户可调用)
```
02_Skill_Tree/Modules/          ← Asher 构建的知识库
├── Content_Creation/           ← 内容创作
├── Business/                   ← 商业
├── Philosophy/                 ← 哲学
├── Psychology/                 ← 心理学
├── Logic_and_Reasoning/        ← 逻辑推理
├── ...                         ← 更多共享模块
```

**任何用户都可以引用这些模块中的知识。** 这是修荷系统的核心价值——站在 Asher 的知识积累上。

**用户也可以向共享知识库贡献新模块。** 使用 `/learn` 工作流学习任何想学的东西，产出的知识文档会存入 `Modules/`，供所有用户调用。**但请勿删除或修改已有模块。**

### 用户专属技能 (个人独有)
```
02_Skill_Tree/Users/{Username}/ ← 用户自己的技能模块
├── {Skill_Name}/
│   ├── README.md               ← 技能说明
│   └── {子文件}.md             ← 具体内容
```

**用户可以在这里创建自己独有的技能。** 比如：你是医生，可以创建 `Medical_Diagnosis/` 模块；你是律师，可以创建 `Legal_Analysis/` 模块。

---

## 二、创建用户技能的流程

### Step 1: 确定技能领域
```
AI: "你有什么独特的专业技能或知识领域？
     比如某个行业的深度经验、某种独特的工作方法、某个领域的专业知识？"
```

### Step 2: 创建技能目录
```
02_Skill_Tree/Users/{Username}/{Skill_Name}/
```

### Step 3: 创建 README.md
按下面的模板填写。

### Step 4: 创建具体内容文件

---

## 三、技能模块 README.md 模板

```markdown
# {技能名称}

> **Owner:** {Username}
> **Domain:** {领域，例如：医疗 / 法律 / 设计 / 教育 / ...}
> **Level:** {入门 / 进阶 / 专家 / 大师}
> **Created:** {YYYY-MM-DD}

---

## 概述
{这个技能模块是关于什么的？}

## 核心能力
1. {能力1}
2. {能力2}
3. {能力3}

## 知识结构

### {子领域1}
- {要点}

### {子领域2}
- {要点}

## 工作方法论
{你在这个领域的独特方法/流程/框架}

## 常见场景
- **场景1:** {描述} → {你的解决方案}
- **场景2:** {描述} → {你的解决方案}

## 与共享知识库的关系
{这个技能如何和 Modules/ 里的共享知识互补？}
例如：
- 结合 `Modules/Content_Creation/` 可以产出 {什么内容}
- 结合 `Modules/Business/` 可以实现 {什么目标}
```

---

## 四、示例

### 假设用户 Luna 是一名产品经理

```
02_Skill_Tree/Users/Luna/
├── Product_Management/
│   ├── README.md
│   ├── User_Research_Framework.md
│   ├── PRD_Template.md
│   └── Prioritization_Models.md
└── UX_Design/
    ├── README.md
    └── Design_Principles.md
```

Luna 可以同时调用:
- 自己的 `Product_Management/` 技能
- Asher 共享的 `Modules/Business/` 商业知识
- Asher 共享的 `Modules/Content_Creation/` 内容技术
- 全局 `AI_Skills_Library/` 的 23 个通用技能

---

## 五、向共享知识库贡献

用户可以通过 `/learn` 工作流向 `Modules/` 添加新知识模块：

```
"用 /learn 帮我学习 {主题}"
```

`/learn` 工作流会：
1. 研究该主题
2. 生成标准化的知识文档
3. 存入 `Modules/` 供所有用户调用

**规则:**
- **可以添加** — 新的知识模块
- **不要删除** — 已有的模块（其他用户可能在使用）
- **不要修改** — Asher 创建的模块内容

---

## 六、注意事项

1. **共享知识库可添加不可删除** — 使用 `/learn` 贡献新知识，但不要删改已有内容
2. **鼓励用户创建独特技能** — 越独特越好，这是他们的核心竞争力
3. **支持渐进式构建** — 不需要一次写完，可以随时补充
4. **与 Profile 联动** — 技能模块应该反映用户在 `01_Base_Attributes/` 中描述的能力

---

*Last Updated: 2026-01-28*
