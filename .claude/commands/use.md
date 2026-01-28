# /use - 加载并执行指定的 AI 技能或工作流

根据用户指定的名称，从多个来源中加载对应的技能/工作流并执行。

## 参数

- `$ARGUMENTS`：技能或工作流名称（如 `pdf`、`meeting-analysis` 等）

## 来源路径

### 来源 1：AI Skills Library (通用技能)
```
/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/AI_Skills_Library/.agents/skills/
```
- 文件位置：`{来源1}/{$ARGUMENTS}/SKILL.md`

### 来源 2：Asher Source Profile (个人工作流)
```
/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/Asher_Source_Profile_v1/.agent/workflows/
```
- 文件位置：`{来源2}/{$ARGUMENTS}.md`

## 执行步骤

1. **验证参数**：确保用户提供了名称
   - 如果没有提供，提示用户使用 `/skills` 查看可用列表

2. **按优先级查找**（先找到的优先）：
   - 先检查 AI Skills Library：`{来源1}/{$ARGUMENTS}/SKILL.md`
   - 再检查 Asher Workflows：`{来源2}/{$ARGUMENTS}.md`

3. **读取定义文件**：
   - 使用 Read 工具读取找到的文件的完整内容
   - 如果两个来源都不存在，提示用户并建议使用 `/skills`

4. **检查附属文件**（仅针对 Skills Library）：
   - 检查该技能目录下是否有其他 `.md` 文件或子目录（如 `rules/`、`templates/` 等）
   - 如有需要，也读取这些附属文件

5. **执行**：
   - 按照文件中定义的指令执行
   - 将内容作为当前任务的上下文和行为指南

## 示例

| 用户输入 | 来源 | 读取文件 |
|----------|------|----------|
| `/use pdf` | AI Skills Library | `.../skills/pdf/SKILL.md` |
| `/use meeting-analysis` | Asher Workflows | `.../workflows/meeting-analysis.md` |

## 错误处理

- 不存在：「`{name}` 不存在。使用 `/skills` 查看所有可用技能和工作流。」
- 路径问题：检查对应目录是否可访问
