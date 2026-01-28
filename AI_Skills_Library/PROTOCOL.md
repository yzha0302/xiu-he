# AI Skill 挂载协议 (Protocol)

为了保持项目根目录的整洁，所有的 AI 技能（Skills）都存放在本文件夹 `AI_Skills_Library` 中。

## 📍 目录结构
- **`.agents/`**: 源代码仓库（不要动这里）。
- **`.agent/`, `.claude/`, `.cursor/`**: 各个 IDE 的专用配置文件夹。

## 🚀 如何使用 (挂载说明)

当您在某个 IDE（如 Cursor, Claude Desktop）中**需要使用这些技能时**，请遵循以下协议：

### 方案 A：直接打开 (推荐)
直接在 IDE 中打开 `AI_Skills_Library` 文件夹作为**工作区**。
*   这样 IDE 会自动读取 `.cursor` 或 `.claude` 中的配置，所有技能立即生效。

### 方案 B：手动挂载 (在其他项目中使用)
如果您在其他项目（根目录）中工作，但依然想用这些技能：
1.  **Cursor**: 将本文件夹下的 `.cursor/rules` 里的内容复制到您项目的 `.cursorrules` 文件中。
2.  **Antigravity**: 在对话中直接告诉 AI：“技能在这个位置：`./AI_Skills_Library/.agent/skills/`”。

## ⚠️ 注意事项
*   不要随意删除本文件夹中的隐藏文件（以 `.` 开头的）。
*   如需安装新技能，请进入本文件夹运行 `npx skills add ...`。
