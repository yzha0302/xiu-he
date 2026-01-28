# Skill MCP Server 配置指南

这个 MCP Server 让 Claude App 能够读取你本地的 AI Skills Library。

## 安装步骤

### 1. 安装依赖

```bash
cd "/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/skill-mcp-server"
npm install
```

### 2. 配置 Claude Desktop

编辑 Claude Desktop 的配置文件：

**macOS 路径**：
```
~/Library/Application Support/Claude/claude_desktop_config.json
```

添加以下配置：

```json
{
  "mcpServers": {
    "skill-server": {
      "command": "node",
      "args": [
        "/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/skill-mcp-server/index.js"
      ]
    }
  }
}
```

如果文件中已有其他 MCP 配置，将 `skill-server` 添加到 `mcpServers` 对象中。

### 3. 重启 Claude Desktop

完全退出并重新打开 Claude Desktop。

## 使用方式

配置完成后，Claude App 将获得以下工具：

| 工具 | 功能 |
|------|------|
| `list_skills` | 列出所有可用的技能和工作流 |
| `use_skill` | 加载指定技能的完整内容 |
| `read_file` | 读取技能库目录内的任意文件 |

### 示例对话

- "列出所有可用的技能"
- "帮我用 pdf 技能处理这个文档"
- "使用 meeting-analysis 工作流分析这段会议记录"

## 技能库路径

Server 会扫描以下两个目录：

1. **AI Skills Library** (通用技能)
   ```
   .../修荷/AI_Skills_Library/.agents/skills/
   ```

2. **Asher Workflows** (个人工作流)
   ```
   .../修荷/Asher_Source_Profile_v1/.agent/workflows/
   ```

## 故障排查

### 检查 Server 是否正常运行

```bash
cd "/Users/yixuanzhang/Library/Mobile Documents/com~apple~CloudDocs/工作/修荷/skill-mcp-server"
node index.js
```

如果看到 "Skill MCP Server running on stdio" 说明正常。

### 查看 Claude Desktop 日志

```bash
tail -f ~/Library/Logs/Claude/mcp*.log
```

### 常见问题

1. **Claude App 没有显示新工具**：确保完全退出并重启 Claude Desktop
2. **路径错误**：检查 `claude_desktop_config.json` 中的路径是否正确
3. **权限问题**：确保 Node.js 有权限读取 iCloud 目录
