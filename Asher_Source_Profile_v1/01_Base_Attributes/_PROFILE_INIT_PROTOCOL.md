# Profile Init Protocol (用户画像构建协议)

> **AI 协作者必读**: 当新用户要求构建自己的 Profile 时，请完整阅读本文件。

---

## 一、概述

本系统支持多用户并存。每个用户拥有独立的 Profile 文件夹，同时可以调用 Asher 的共享知识库（`02_Skill_Tree/Modules/`）。

**核心架构:**
```
01_Base_Attributes/
├── _TEMPLATES/              ← 空白模板（AI 读取结构）
├── _PROFILE_INIT_PROTOCOL.md ← 你正在读的这个文件
├── 1.1_Character_Stats.md   ← Asher 的属性（参考案例）
├── 1.2_Cognitive_Traits.md  ← Asher 的认知
├── 1.3_Aesthetic_Matrix.md  ← Asher 的审美
├── 1.4_Social_Game.md       ← Asher 的社交
├── Bio.md                   ← Asher 的简介
│
└── {Username}/              ← 新用户的 Profile
    ├── Character_Stats.md
    ├── Cognitive_Traits.md
    ├── Aesthetic_Matrix.md
    ├── Social_Game.md
    └── Bio.md
```

---

## 二、AI 执行流程

### Step 1: 确认用户名

```
AI: "请告诉我你想用的用户名（英文，无空格，例如: Luna, Max, Zhangsan）"
```

用户名将作为文件夹名和系统内的唯一标识。

### Step 2: 创建用户文件夹

在 `01_Base_Attributes/` 下创建 `{Username}/` 目录。

### Step 3: 渐进式对话构建

**不要一次性抛出所有问题。** 按以下顺序，每次聚焦一个维度，用自然对话的方式收集信息。

**对话轮次建议:**

| 轮次 | 维度 | 对话方向 | 产出文件 |
|------|------|----------|----------|
| 1 | 基础属性 | 性格、能量类型、风险偏好、核心能力 | `Character_Stats.md` |
| 2 | 认知内核 | 思维方式、信息处理、决策模式 | `Cognitive_Traits.md` |
| 3 | 审美矩阵 | 审美偏好、感官喜好、消费观 | `Aesthetic_Matrix.md` |
| 4 | 社交博弈 | 社交风格、信任机制、人生哲学 | `Social_Game.md` |
| 5 | 简介 | 总结为 Bio | `Bio.md` |

### Step 4: 每轮对话的执行方式

```
1. 读取 _TEMPLATES/{对应模板}.md → 获取结构
2. 参考 Asher 的对应文件 → 了解"填写好的"长什么样
3. 用自然对话收集信息（不要让用户看到模板，用聊天的方式）
4. 将收集到的信息填入模板结构
5. 写入 {Username}/{对应文件}.md
6. 展示给用户确认
```

### Step 5: 同时初始化技能树

创建用户的专属技能目录:
```
02_Skill_Tree/Users/{Username}/
```

参见 `02_Skill_Tree/_USER_SKILL_TEMPLATE.md` 获取技能模块的创建规范。

---

## 三、对话引导技巧

### 第一轮: Character Stats

**开场:**
```
"我需要了解你这个人。不用急，我们慢慢聊。
先从最基本的开始——你觉得你是什么类型的人？
比如：你做决策时是靠直觉还是分析？你在团队里通常是什么角色？"
```

**关键问题（不要一次问完，根据对话自然推进）:**
- 你知道自己的 MBTI 吗？九型人格？
- 什么事情让你充满能量？什么事情让你耗尽？
- 你对风险的态度？会在什么条件下冒险？
- 你觉得自己最强的能力是什么？最弱的呢？
- 如果给自己的能力打分（算力、执行、社交、稳定、体能），你怎么打？
- 你有什么独特的"杀手锏"——别人做不到但你能做到的事？
- 你最致命的弱点是什么？

### 第二轮: Cognitive Traits

**开场:**
```
"现在聊聊你怎么思考。
你处理复杂问题的时候，脑子里是什么画面？文字？数字？还是某种感觉？"
```

**关键问题:**
- 你接收新信息时，倾向于哪种方式？（读/听/看/做）
- 面对模糊不清的问题，你的第一反应是？
- 你做决策时，直觉和分析哪个先来？
- 你有什么认知偏差或盲点？
- 什么状态下你思维最清晰？什么状态下最差？

### 第三轮: Aesthetic Matrix

**开场:**
```
"聊聊你的品味和偏好。
你理想的工作环境长什么样？你讨厌什么样的环境？"
```

### 第四轮: Social Game

**开场:**
```
"最后聊聊你和人打交道的方式。
你的社交圈大概分几层？最核心的人是谁？"
```

---

## 四、文件命名规则

| 文件 | 路径 |
|------|------|
| 基础属性 | `01_Base_Attributes/{Username}/Character_Stats.md` |
| 认知内核 | `01_Base_Attributes/{Username}/Cognitive_Traits.md` |
| 审美矩阵 | `01_Base_Attributes/{Username}/Aesthetic_Matrix.md` |
| 社交博弈 | `01_Base_Attributes/{Username}/Social_Game.md` |
| 个人简介 | `01_Base_Attributes/{Username}/Bio.md` |
| 用户技能 | `02_Skill_Tree/Users/{Username}/` |

---

## 五、共享与专属的边界

### 共享资源（所有用户可调用）
- `02_Skill_Tree/Modules/` — Asher 构建的知识库（Content_Creation、Philosophy、Business 等）
- `AI_Skills_Library/` — 23 个通用 AI 技能
- `Projects/Asyre/` — 内容创作系统（可用自己的画像配置）
- `.agent/workflows/` — 标准工作流

### 用户专属（每人独立）
- `01_Base_Attributes/{Username}/` — 个人属性
- `02_Skill_Tree/Users/{Username}/` — 个人技能模块
- Asyre `Creators/{Username}/` — 个人创作者画像

---

## 六、渐进式完善

**Profile 不需要一次完成。**

- **Level 1 (骨架):** 完成 Character_Stats 的基本信息（30 分钟对话）
- **Level 2 (血肉):** 补充 Cognitive + Aesthetic + Social（多次对话）
- **Level 3 (灵魂):** 随着使用系统，持续补充和修正

AI 在后续对话中发现用户的新特征时，应主动提议更新 Profile。

---

## 七、注意事项

1. **尊重隐私:** 不要强迫用户回答不想回答的问题
2. **自然对话:** 用聊天的方式，不要让用户感觉在填表
3. **参考但不复制:** 参考 Asher 的结构和深度，但内容必须是用户自己的
4. **不修改 Asher 的文件:** 永远不要修改 `1.1_` 到 `1.4_` 开头的文件
5. **鼓励独特性:** 每个人的 Profile 应该反映他们独特的特质，不需要和 Asher 的格式完全一样

---

*Last Updated: 2026-01-28*
