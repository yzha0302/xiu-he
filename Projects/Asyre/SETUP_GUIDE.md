# Asyre 快速设置指南

> **非对称内容创作系统 v2.9**
> 解压即用，5分钟上手

---

## 第一步：解压文件

将这个压缩包解压到你的工作目录。

解压后的文件结构：
```
Asyre_Package/
├── Asyre/                    # 引擎核心
│   ├── Config/               # 配置文件
│   ├── Creators/             # 创作者画像（你的个人配置会存这里）
│   ├── Engine/               # 推导引擎
│   ├── Docs/                 # 文档
│   └── README.md             # 详细说明
│
├── .claude/commands/         # Claude Skill 定义
│   └── asyre.md              # 这是核心！
│
└── SETUP_GUIDE.md            # 本文件
```

---

## 第二步：配置 Claude Code

### 方式 A: 复制到你的项目（推荐）

1. 把 `Asyre/` 文件夹复制到你的工作目录
2. 把 `.claude/commands/asyre.md` 复制到你工作目录的 `.claude/commands/` 下

```bash
# 假设你的工作目录是 ~/my-project
cp -R Asyre ~/my-project/
mkdir -p ~/my-project/.claude/commands
cp .claude/commands/asyre.md ~/my-project/.claude/commands/
```

### 方式 B: 直接在解压目录使用

在 Claude Code 中打开这个解压后的目录，直接使用即可。

---

## 第三步：开始使用

打开 Claude Code，输入：

```bash
/asyre 写一篇关于"为什么年轻人不想上班"的口播稿
```

系统会自动执行六阶段流程：
1. **意图解析** - 分析主题的意图因子
2. **参数推导** - 输出关键参数分析
3. **自由创作** - 带着方向感自由发挥
4. **评价文档** - 七层质量公式评分
5. **雕刻修正** - 去冗余（10-20%）
6. **精修审核** - 质量提升轨迹报告

---

## 常用命令

### 内容创作
```bash
/asyre [主题]                    # 完整六阶段流程
/asyre quick [主题]              # 跳过确认，直接输出精修版
/asyre critique [内容]           # 仅评价现有内容
/asyre refine [内容]             # 仅对现有内容进行雕刻
```

### 创作者画像（个性化）
```bash
/asyre profile init              # 初始化你的画像
/asyre profile enrich            # 深化画像（继续问问题）
/asyre profile view              # 查看当前画像
```

### 数据反馈学习
```bash
/asyre feedback                  # 提交实际发布内容+数据
/asyre baseline init             # 初始化播放量基线
/asyre baseline view             # 查看当前基线
```

---

## 建议的使用流程

### 第一次使用

1. 先运行 `/asyre profile init` 让系统了解你
2. 然后尝试 `/asyre [你想写的主题]`
3. 跟着流程走，感受六阶段迭代

### 发布后

1. 内容发布后收集数据（播放量、完播率、互动率）
2. 运行 `/asyre feedback` 提交数据
3. 系统会诊断问题并给出优化建议

---

## 核心理念

> **内容价值 = 人的不可替代性 × AI 的放大效率**

**创作哲学**: "雕刻大卫" — 米开朗琪罗说"大卫本来就在石头里"，但前提是那块石头本身就是好石头。初稿就要有灵魂，雕刻只是去冗余。

**框架定位**: 框架用来**启动思考**和**评价优化**，不用来**限制创作**。

---

## 遇到问题？

1. 确保 `.claude/commands/asyre.md` 在正确位置
2. 确保 `Asyre/` 文件夹在工作目录根目录
3. 详细文档见 `Asyre/README.md`

---

祝创作愉快！🎨
