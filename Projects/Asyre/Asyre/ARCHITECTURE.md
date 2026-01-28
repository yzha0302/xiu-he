# Asyre Architecture - 架构说明

> **Version:** 2.0
> **Date:** 2026-01-13

---

## 1. 系统定位

Asyre 是一个**意图驱动的内容创作参数系统**。

核心问题：用大语言模型写口播稿/文章时，如何让 AI 知道"应该怎么写"？

解决方案：不是预设固定参数，而是根据**创作意图**动态推导参数。

---

## 2. 核心组件

### 2.1 Config 层 (配置)

```
Config/
├── Schema/                     # 定义层
│   ├── _schema_master.json     # 所有参数的定义
│   ├── intent_factors.json     # 意图因子定义
│   └── derivation_rules.json   # 推导规则
│
├── Presets/                    # 预设层
│   └── _PRESET_TEMPLATE.json   # 预设模板
│
└── layer_weights.json          # 七层权重 (兼容旧版)
```

### 2.2 Engine 层 (推导引擎)

```
Engine/
├── derivation_process.md       # 推导流程说明
└── reference_hierarchy.md      # 参考层次说明
```

推导引擎负责：
1. 解析用户意图
2. 匹配推导规则
3. 生成参数配置
4. 输出执行规则

### 2.3 Modules 层 (知识库)

```
Modules/
└── _INHERITED.md               # 继承说明
```

当前状态：继承自个人外挂能力系统
独立后：复制相关模块到此文件夹

### 2.4 Docs 层 (文档)

```
Docs/
├── Asyre_Project_Summary.md    # 项目概述
└── Asyre_Unified_Knowledge.md  # 核心知识
```

---

## 3. 数据流

```
┌─────────────────────────────────────────────────────────────────┐
│                        Asyre Data Flow                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   [用户输入]                                                     │
│       │                                                         │
│       ▼                                                         │
│   ┌─────────────────┐                                           │
│   │ 意图解析        │ ← intent_factors.json                     │
│   │ (Intent Parse)  │                                           │
│   └────────┬────────┘                                           │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │ 规则匹配        │ ← derivation_rules.json                   │
│   │ (Rule Match)    │                                           │
│   └────────┬────────┘                                           │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │ 参数推导        │ ← _schema_master.json                     │
│   │ (Param Derive)  │                                           │
│   └────────┬────────┘                                           │
│            │                                                    │
│            ▼                                                    │
│   ┌─────────────────┐                                           │
│   │ 参考绑定        │ ← Modules (Level 3)                       │
│   │ (Ref Bind)      │                                           │
│   └────────┬────────┘                                           │
│            │                                                    │
│            ▼                                                    │
│   [参数配置 + 执行规则]                                          │
│            │                                                    │
│            ▼                                                    │
│   [AI 生成内容]                                                  │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 4. 参数双属性

每个参数不是单一数值，而是包含：

| 属性 | 说明 |
|:-----|:-----|
| **importance** | 重要性 (critical/high/medium/low) |
| **target** | 目标值或范围 |
| **reference** | 参考来源 (Glossary/Formula/Module) |

```json
{
  "attitude_strength": {
    "importance": "critical",
    "target": 0.9,
    "reference": {
      "glossary": ["Attitude_Output"],
      "formula": "Attitude_over_Analysis",
      "module": "Content_Creation/Oral_Script_Style.md"
    }
  }
}
```

---

## 5. 意图因子系统

### 设计理念

传统方式按**形式**分类 (口播/长文)，但同样是口播稿，"科普"和"带货"的参数完全不同。

Asyre 按**意图**分类，内容形式只是意图的载体。

### 因子组合

```json
{
  "社会评论": {
    "value_guidance": 0.9,
    "persuasion": 0.8,
    "emotional_resonance": 0.7
  },
  "深度科普": {
    "concept_clarification": 0.9,
    "hidden_reveal": 0.7,
    "cognitive_disruption": 0.6
  }
}
```

### 扩展机制

意图因子通过 `/learn` 工作流持续扩展：

1. 学习新的创作意图类型
2. 更新 `intent_factors.json`
3. 添加对应的推导规则

---

## 6. 独立化路径

当 Asyre 需要作为独立项目分离时：

### Step 1: 复制依赖模块

```bash
cp -r ../../Modules/Content_Creation ./Modules/
```

### Step 2: 更新引用路径

将所有 `../../Modules/` 引用改为 `./Modules/`

### Step 3: 删除继承标记

删除 `Modules/_INHERITED.md`

### Step 4: 验证自包含

确保所有参考内容都可以在项目内找到

---

## 7. 版本兼容

### 旧版文件

| 文件 | 状态 | 说明 |
|:-----|:-----|:-----|
| `layer_weights.json` | 保留 | 兼容旧的七层权重方式 |
| `Asyre_Creation_Config.json` | 迁移到 Docs | 旧版配置参考 |
| `Asyre_Quality_Scorecard.json` | 迁移到 Docs | 旧版评分卡 |

### 迁移指南

旧版预设 → 新版预设：

1. 识别旧预设的核心意图
2. 转换为意图因子权重
3. 验证推导结果是否一致

---

## 8. 待完成项

| 项目 | 优先级 | 状态 |
|:-----|:-------|:-----|
| 完善意图因子列表 | 高 | 待 /learn |
| 补充推导规则 | 高 | 进行中 |
| 实践验证 | 高 | 待执行 |
| 反馈收集机制 | 中 | 待设计 |
| 平台适配规则 | 中 | 待补充 |
