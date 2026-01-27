# 蜕升计划 (The Ascension Protocol) - Discord Bot

> AI 时代的认知军械库 & 进化者基地

## 快速部署

### 1. 获取服务器 ID

1. Discord 设置 → 高级设置 → 开启「开发者模式」
2. 右键你的服务器图标 → 复制服务器 ID

### 2. 本地运行（测试）

```bash
# 安装依赖
pip install -r requirements.txt

# 设置环境变量
export DISCORD_TOKEN="你的Token"
export GUILD_ID="你的服务器ID"

# 初始化服务器结构（只需运行一次）
python setup_server.py

# 运行 Bot
python bot.py
```

### 3. 部署到 Railway（生产）

```bash
# 安装 Railway CLI
npm install -g @railway/cli

# 登录
railway login

# 初始化
railway init

# 设置环境变量
railway variables set DISCORD_TOKEN="你的Token"
railway variables set GUILD_ID="你的服务器ID"

# 部署
railway up
```

## 指令列表

| 指令 | 描述 | 权限 |
|------|------|------|
| `/status` | 查看个人系统状态 | 所有人 |
| `/leaderboard` | 查看算力排行榜 | 所有人 |
| `/sync` | 每日同步获取算力 | 所有人 |
| `/broadcast [内容]` | 发布全频段广播 | System Core |
| `/upgrade [成员] [等级]` | 提升成员权限 | System Core |
| `/disconnect [成员]` | 断开成员连接 | System Core |

## 权限体系

| Level | Code Name | 对应 | 颜色 |
|-------|-----------|------|------|
| L4 | System Core | Admin | Gold |
| L3 | Architect | VIP | Red |
| L2 | Augmented | 付费 | Blue |
| L1 | Awakened | 免费 | Green |
| L0 | Protocol | Bot | Grey |

## 频道结构

```
📡 SYSTEM BROADCAST
├── global-signal (公告)
├── nav-chart (规则)
└── access-key (付费入口)

🌍 THE WASTELAND
├── human-touch (自由聊天)
├── signal-fire (情报共享)
├── alliance (自我介绍)
└── debug (提问)

🛠️ COGNITIVE ARMORY [L2+]
├── mental-os (深度文章)
├── tools-lib (工具/源码)
├── black-box (视频)
└── lab-notes (碎片思考)

🚀 HIGH ORBIT [L3+]
├── overview-effect (战略讨论)
├── direct-link (VIP直播)
└── club-lounge (语音挂机)

⚔️ BOUNTY BOARD
├── missions (任务)
└── credits (积分)

🔧 BACKEND [L4]
├── system-log
└── transaction-log
```

## 文件说明

- `bot.py` - 主程序
- `setup_server.py` - 服务器初始化
- `requirements.txt` - 依赖
- `Procfile` - 部署配置

---

*Mission Status: Go.*
