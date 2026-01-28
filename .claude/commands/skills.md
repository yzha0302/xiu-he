# /skills - 列出所有可用的 AI 技能和工作流

扫描多个目录，列出所有可用的技能 (skills) 和工作流 (workflows)。

## 技能库路径

### 来源 1：AI Skills Library (通用技能)
```
/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/AI_Skills_Library/.agents/skills/
```
- 结构：每个子文件夹是一个 skill，包含 `SKILL.md`

### 来源 2：Asher Source Profile (个人工作流)
```
/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/Asher_Source_Profile_v1/.agent/workflows/
```
- 结构：每个 `.md` 文件是一个 workflow

## 执行步骤

1. **扫描 AI Skills Library**：
   - 列出所有子文件夹
   - 对于每个 skill，读取 `SKILL.md` 的前几行提取名称和简介

2. **扫描 Asher Workflows**：
   - 列出所有 `.md` 文件（排除 README.md）
   - 读取每个文件的前几行提取名称和简介

3. **分类展示**：按来源分组显示

## 输出格式

```
## AI Skills Library (通用技能)

| 技能 | 描述 | 调用方式 |
|------|------|----------|
| pdf | PDF 文档处理 | /use pdf |
| docx | Word 文档处理 | /use docx |

## Asher Workflows (个人工作流)

| 工作流 | 描述 | 调用方式 |
|--------|------|----------|
| meeting-analysis | 会议分析 | /use meeting-analysis |
| fact-check | 事实核查 | /use fact-check |
...
```
