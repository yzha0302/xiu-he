# Humanizer Bilingual 双语人性化写作工具

去除 AI 写作痕迹，让内容像人写的。支持中文和英文。

## 安装

```bash
# 复制到 Claude Code skills 目录
cp -r humanizer-bilingual ~/.claude/skills/
```

## 使用

```
/humanizer-bilingual

[粘贴你的文本]
```

或直接说：

```
请帮我人性化这段文字：[你的文本]
```

---

## 核心功能

### 中英文叙事差异处理

| 维度 | 英文人味 | 中文人味 |
|:-----|:---------|:---------|
| 节奏 | 长短句交替 | 四字格+口语混搭 |
| 情感词 | 直接表达 (I feel) | 语气词承载 (嘛、啊、吧) |
| 连接 | 显性连接词 | 意合为主 |
| 态度 | 直接陈述 | 反问+金句 |
| 亲近感 | we | "咱们"+"你看" |

---

## AI 模式检测清单

### 英文 (24种模式)

**内容层面:**
1. 夸大重要性 - "pivotal moment", "testament to"
2. 媒体名堆砌 - "featured in NYT, BBC..."
3. -ing 虚假分析 - "symbolizing..., reflecting..."
4. 推销式语言 - "nestled", "vibrant", "breathtaking"
5. 模糊来源 - "Experts argue", "Industry observers"
6. 套路化挑战 - "Despite challenges... continues to thrive"

**语言层面:**
7. AI 高频词 - Additionally, crucial, delve, enhance, foster
8. 回避 is/are - "serves as", "stands as"
9. 否定式并列 - "It's not just X, it's Y"
10. 三段论滥用
11. 同义词轮换
12. 虚假范围

**格式层面:**
13-18. Em dash/粗体/列表标题/大小写/Emoji/引号

**沟通层面:**
19-24. 聊天痕迹/截止声明/讨好语气/填充词/过度对冲/空洞结论

### 中文 (12种特征)

**语言层面:**
1. 通用模糊 - "这是一个很有趣的话题"
2. 重复词汇 - "此外...此外...此外..."
3. 过度正式 - "鉴于上述情况"
4. AI专属词汇 - "深入探讨"、"值得一提的是"
5. 零语法错误

**结构层面:**
6. 三段论 - "第一...第二...第三..."
7. 过渡词泛滥 - "然而"、"因此"、"综上所述"
8. 句式单一
9. 缺失话题跳跃

**情感层面:**
10. 无个人视角
11. 情绪平淡
12. 两边讨好

---

## 人性化技巧

### 英文
- 有观点，不只是报道
- 变换节奏 (短。然后长。)
- 承认复杂和不确定
- 用第一人称
- 允许不完美

### 中文
1. **共情视角**: 你 → 我们/咱们
2. **问题钩子**: 陈述 → 提问
3. **情绪高潮**: 设计爆发点
4. **态度鲜明**: 禁止骑墙
5. **口语温度**: 书面 → 说话
6. **节奏变化**: 长短交替

---

## 人味公式

```
人味 = 态度强度 × 情绪起伏 × 视角亲近度
(任一为0则无人味)
```

---

## 与 Asyre 集成

建议工作流：

```
Asyre 生成初稿
    ↓
/humanizer-bilingual 处理
    ↓
人工微调
    ↓
发布
```

---

## 参考

- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing)
- Asyre Content_Creation/Human_Like_Expression.md

## 版本

- v1.0.0 - 初始版本，整合英文24模式 + 中文12特征
