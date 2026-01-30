# Moltbot 使用指南

## 🔗 连接信息

- **Gateway 地址**: ws://127.0.0.1:18789 (仅 localhost)
- **Gateway Token**: `5adc98b66b882e324c0760c4d74277ffce241db6da17c153043a8907ea6cd47e`
- **AI 模型**: claude-opus-4-5
- **Workspace**: /home/ubuntu/xiu-he/.xiao-a/

## 📖 使用方法

### 方式 1：SSH 隧道（从 Mac 连接）

```bash
# 1. 创建 SSH 隧道
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key -L 18789:localhost:18789 ubuntu@47.129.170.209

# 2. 在另一个终端设置 token
export CLAWDBOT_GATEWAY_TOKEN="5adc98b66b882e324c0760c4d74277ffce241db6da17c153043a8907ea6cd47e"

# 3. 使用 moltbot（如果本地安装了）
moltbot agent --message "你好小A" --json
```

### 方式 2：直接在服务器使用

```bash
# SSH 连接
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209

# 进入目录
cd ~/xiu-he/Projects/moltbot

# 发送消息给 AI
./moltbot.mjs agent --message "分析一下 /home/ubuntu/xiu-he/README.md" --json

# 查看 gateway 状态
./moltbot.mjs status

# 查看健康检查
./moltbot.mjs health
```

### 方式 3：WhatsApp 渠道

```bash
# 1. SSH 到服务器
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209

# 2. 登录 WhatsApp
cd ~/xiu-he/Projects/moltbot
./moltbot.mjs channels login --verbose

# 3. 扫描显示的二维码

# 4. 之后可以直接通过 WhatsApp 发消息给小A
```

## 🛠️ 管理命令

### PM2 管理

```bash
# 查看状态
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "pm2 status"

# 查看实时日志
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "pm2 logs moltbot"

# 重启
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "pm2 restart moltbot"

# 停止
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "pm2 stop moltbot"
```

### 查看 AI 生成的文件

```bash
# 查看 workspace（AI 输出位置）
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "ls -la ~/xiu-he/.xiao-a/"

# 查看 AI 记忆
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "cat ~/xiu-he/.xiao-a/memory/\$(date +%Y-%m-%d).md"
```

## 📁 重要路径

- **配置文件**: `/home/ubuntu/.moltbot/moltbot.json`
- **PM2 配置**: `/home/ubuntu/xiu-he/Projects/moltbot/ecosystem.config.cjs`
- **Workspace**: `/home/ubuntu/xiu-he/.xiao-a/` (AI 生成文件存放处)
- **小A 身份配置**: `/home/ubuntu/xiu-he/.xiao-a/BIFOLD_CONFIG.json`
- **日志**: `/home/ubuntu/.pm2/logs/moltbot-*.log`

## 🔄 同步更新

当你在本地修改 `.xiao-a/` 配置后：

```bash
# 同步到服务器
./deploy_to_aws.sh

# 重启 moltbot 加载新配置
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "pm2 restart moltbot"
```

## 🧪 测试连接

```bash
# 从服务器测试
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209 "cd ~/xiu-he/Projects/moltbot && ./moltbot.mjs health"

# 应该看到：
# {
#   "status": "ok",
#   "gateway": "running",
#   "port": 18789
# }
```

## 🎯 典型使用场景

### 场景 1: 让 AI 分析服务器上的文件

```bash
ssh -p 2222 -i ~/.ssh/xiuhe_deploy_key ubuntu@47.129.170.209
cd ~/xiu-he/Projects/moltbot
./moltbot.mjs agent --message "读取 /home/ubuntu/xiu-he/README.md 并总结" --json
```

### 场景 2: 通过 WhatsApp 远程指挥

1. 配置 WhatsApp 登录（只需一次）
2. 之后直接用手机 WhatsApp 发消息
3. AI 可以访问服务器上的 `/home/ubuntu/xiu-he/` 所有文件
4. 生成的文件保存在 `.xiao-a/` 目录

### 场景 3: 定时任务

可以配置 cron 定时发送消息给 AI：

```bash
# 每天早上 9 点生成日报
0 9 * * * cd /home/ubuntu/xiu-he/Projects/moltbot && ./moltbot.mjs agent --message "生成今日工作计划" > /dev/null 2>&1
```
