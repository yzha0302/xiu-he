# AI Skills Index

你拥有一个技能库，可以根据用户需求加载对应的技能。

## 技能库位置

### 来源 1：AI Skills Library (通用技能)
```
/AI_Skills_Library/.agents/skills/
```
- 每个子文件夹是一个技能
- 技能定义文件：`{文件夹名}/SKILL.md`
- 可能包含附属文件：`rules/`、`templates/` 等子目录

### 来源 2：Asher Workflows (个人工作流)
```
/Asher_Source_Profile_v1/.agent/workflows/
```
- 每个 `.md` 文件是一个工作流
- 文件名即工作流名称

## 使用方式

当用户的需求可能匹配某个技能时：

1. **发现技能**：扫描上述目录，列出可用的技能/工作流
2. **读取技能**：根据需求读取对应的 SKILL.md 或 workflow.md
3. **执行技能**：按照技能文件中的指令执行

## 触发场景

以下场景应主动查阅技能库：
- 用户提到 PDF、Word、PPT、Excel 等文档处理
- 用户需要 UI/UX 设计、前端开发指导
- 用户需要会议分析、事实核查、学习辅助
- 用户需要创建演示文稿、品牌设计
- 用户明确说"用 xxx 技能"或"帮我做 xxx"

## 注意

- 优先检查 AI Skills Library，再检查 Asher Workflows
- 读取技能后，严格按照技能定义执行
- 如有附属文件（rules/、templates/），根据需要一并读取
