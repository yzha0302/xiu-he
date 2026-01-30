# Moltbot 服务器部署总结

**部署时间**: 2026-01-30
**状态**: ✅ 部署成功并运行中

---

## 🌐 部署架构

### 本地 Mac
- **Moltbot**: 运行中（Discord **已禁用**）
- **用途**: 本地开发和测试
- **Workspace**: `/Users/yixuanzhang/projects/修荷/.xiao-a`
- **配置**: `~/.moltbot/moltbot.json`（Discord disabled）

### AWS 服务器 (47.129.170.209)
- **Moltbot**: 运行中（Discord **已启用**）
- **用途**: 生产环境，24/7 在线
- **Workspace**: `/home/ubuntu/xiu-he/.xiao-a/`
- **配置**: `/home/ubuntu/.moltbot/moltbot.json`
- **PM2 守护**: ✅ 开机自启动

---

## 📁 关键文件位置

### 服务器端（不同步到本地）
```
/home/ubuntu/.moltbot/moltbot.json         # Moltbot主配置
/home/ubuntu/.pm2/                         # PM2配置和日志
/home/ubuntu/.clawdbot/                    # Gateway数据
```

### 项目文件（双向同步）
```
.xiao-a/MODEL_ALLOCATION.md                # 模型分配策略
.xiao-a/BIFOLD_CONFIG.json                 # 双人格配置
.xiao-a/SOUL.md                            # 身份源代码
Projects/moltbot/ecosystem.config.cjs      # PM2配置模板
```

### 部署脚本（仅本地）
```
deploy_to_aws.sh                           # 本地→服务器
pull_from_aws.sh                           # 服务器→本地
切换模型脚本.sh                              # 快速切换默认模型
使用moltbot指南.md                          # 使用文档
```

---

## ⚙️ 服务器配置详情

### Moltbot 配置
**文件**: `/home/ubuntu/.moltbot/moltbot.json`

```json
{
  "agents": {
    "defaults": {
      "workspace": "/home/ubuntu/xiu-he/.xiao-a",
      "model": {
        "primary": "anthropic/claude-opus-4-5"
      },
      "models": {
        "anthropic/claude-opus-4-5": {},
        "anthropic/claude-sonnet-3-5": {},
        "anthropic/claude-haiku-4-5": {}
      }
    }
  },
  "gateway": {
    "mode": "local",
    "port": 18789,
    "auth": {
      "token": "<GATEWAY_TOKEN>"
    }
  },
  "channels": {
    "discord": {
      "enabled": true,
      "token": "<DISCORD_BOT_TOKEN>"
    }
  }
}
```

### PM2 配置
**文件**: `/home/ubuntu/xiu-he/Projects/moltbot/ecosystem.config.cjs`

```javascript
module.exports = {
  apps: [{
    name: 'moltbot',
    script: './moltbot.mjs',
    args: 'gateway',
    cwd: '/home/ubuntu/xiu-he/Projects/moltbot',
    instances: 1,
    exec_mode: 'fork',
    autorestart: true,
    watch: false,
    max_memory_restart: '1G',
    env: {
      NODE_ENV: 'production',
      CLAWDBOT_CONFIG: '/home/ubuntu/.clawdbot/moltbot.json',
      ANTHROPIC_API_KEY: '<ANTHROPIC_API_KEY>'
    }
  }]
};
```

---

## 🎯 模型分配策略

### Tier 1: Asher (你)
- **Discord ID**: 1285799717128900671
- **默认模型**: Claude Opus 4.5
- **人格模式**: Endo-Layer（直言模式）
- **限制**: 无

### Tier 2: 其他用户
- **默认模型**: Claude Opus（但行为模拟 Haiku 效率）
- **人格模式**: Exo-Layer（友好模式）
- **策略**: 简洁高效，不透露分级

---

## 🔄 日常操作

### 更新配置
```bash
# 1. 修改本地 .xiao-a/ 配置文件
# 2. 部署到服务器
./deploy_to_aws.sh

# 3. 重启 moltbot（如需要）
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "pm2 restart moltbot"
```

### 拉取服务器修改
```bash
./pull_from_aws.sh
```

### 切换默认模型
```bash
./切换模型脚本.sh opus    # 切换到 Opus
./切换模型脚本.sh haiku   # 切换到 Haiku
```

### 查看状态
```bash
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "pm2 status"
```

### 查看日志
```bash
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "pm2 logs moltbot"
```

---

## 🛡️ 安全配置

### 本地保护
- ✅ `.gitignore` 保护所有敏感文件
- ✅ `gitsafe` 别名检查危险文件
- ✅ 部署脚本不进入 Git

### 服务器保护
- ✅ SSH 端口 2222（非标准）
- ✅ SSH Key 认证（xiuhe_deploy_key）
- ✅ Gateway Token 认证
- ✅ PM2 进程守护

### 双通道隔离
- 🔴 **红通道**（SSH/rsync）: 敏感文件和配置
- 🔵 **蓝通道**（Git/GitHub）: 公开代码
- ✅ 严格分离，互不干扰

---

## 📊 运行状态

### 当前状态
```
┌────┬────────────┬─────────────┬─────────┬─────────┬──────────┬────────┬──────┬───────────┬──────────┬──────────┬──────────┬──────────┐
│ id │ name       │ namespace   │ version │ mode    │ pid      │ uptime │ ↺    │ status    │ cpu      │ mem      │ user     │ watching │
├────┼────────────┼─────────────┼─────────┼─────────┼──────────┼────────┼──────┼───────────┼──────────┼──────────┼──────────┼──────────┤
│ 0  │ moltbot    │ default     │ 2026.1… │ fork    │ running  │ stable │ <20  │ online    │ 0%       │ ~60mb    │ ubuntu   │ disabled │
└────┴────────────┴─────────────┴─────────┴─────────┴──────────┴────────┴──────┴───────────┴──────────┴──────────┴──────────┴──────────┘
```

### Discord 连接
- ✅ Bot: @Asher Bot 🐲
- ✅ ID: 1466301128974143628
- ✅ 已批准用户: 1285799717128900671（你）

### Gateway
- ✅ 地址: ws://127.0.0.1:18789
- ✅ 模式: local
- ✅ 认证: token

---

## 🎮 使用方式

### Discord（推荐）
直接在 Discord 发消息给 @Asher Bot：
```
@Asher Bot 你的问题
@Asher Bot [opus] 复杂任务
@Asher Bot [haiku] 快速问题
```

### 命令行（服务器）
```bash
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209
cd ~/xiu-he/Projects/moltbot
./moltbot.mjs agent --session-id asher --message "你的问题"
```

---

## 🔧 故障排查

### Moltbot 崩溃
```bash
# 查看日志
pm2 logs moltbot --err

# 重启
pm2 restart moltbot

# 完全重启
pm2 delete moltbot
pm2 start ~/xiu-he/Projects/moltbot/ecosystem.config.cjs
```

### Discord 连接断开
```bash
# 检查配置
cat ~/.moltbot/moltbot.json | grep discord

# 重启 moltbot
pm2 restart moltbot
```

### Gateway 端口冲突
```bash
# 检查端口占用
ss -tlnp | grep 18789

# 杀掉冲突进程
pkill moltbot-gateway
pm2 restart moltbot
```

---

## 📝 最后检查清单

- [x] 服务器 Moltbot 运行正常
- [x] Discord 连接成功
- [x] PM2 守护进程配置
- [x] 开机自启动已设置
- [x] 模型分配策略已部署
- [x] 双人格配置已激活
- [x] 本地 Discord 已禁用（避免冲突）
- [x] 部署脚本已测试
- [x] 安全配置已检查

---

**部署完成时间**: 2026-01-30 22:49 CST
**最后更新**: 2026-01-30 22:52 CST
**状态**: 🟢 Production Ready
