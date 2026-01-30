# Moltbot 部署文档

Moltbot 是一个 WhatsApp 网关 + AI 代理系统，支持多渠道（Discord、WhatsApp、Telegram 等）。

## 📁 文件说明

### 部署脚本（`../../scripts/moltbot/`）
- `deploy_to_aws.sh` - 部署到 AWS 服务器（本地→服务器）
- `pull_from_aws.sh` - 从服务器拉取配置（服务器→本地）
- `setup_moltbot_pm2.sh` - 配置 PM2 守护进程
- `start_moltbot_on_server.sh` - 快速启动脚本
- `切换模型脚本.sh` - AI 模型切换工具

### 文档
- `MOLTBOT_部署总结.md` - 完整部署架构和配置
- `使用moltbot指南.md` - 使用说明和命令参考
- `moltbot_config.json` - 配置文件示例

## 🚀 快速开始

### 部署到服务器
```bash
cd /Users/yixuanzhang/projects/修荷
./scripts/moltbot/deploy_to_aws.sh
```

### 拉取服务器配置
```bash
./scripts/moltbot/pull_from_aws.sh
```

### 切换 AI 模型
```bash
# 切换到 Opus（最强）
./scripts/moltbot/切换模型脚本.sh opus

# 切换到 Haiku（最快）
./scripts/moltbot/切换模型脚本.sh haiku
```

## 📚 详细文档

查看以下文档了解详情：
- [完整部署总结](./MOLTBOT_部署总结.md)
- [使用指南](./使用moltbot指南.md)

## 🔐 安全提醒

所有脚本和配置包含敏感信息，已通过 `.gitignore` 保护，仅通过 🔴 红色通道（SSH）同步。

**不要将这些文件提交到 Git！**

---

**服务器状态**: 运行中
**Discord Bot**: @Asher Bot 🐲
**Gateway**: ws://127.0.0.1:18789
