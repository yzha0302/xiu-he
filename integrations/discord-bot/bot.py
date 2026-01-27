"""
蜕升计划 (The Ascension Protocol) - Discord Bot
AI 时代的认知军械库 & 进化者基地
"""

import discord
from discord.ext import commands, tasks
from discord import app_commands
import os
import json
from datetime import datetime
from collections import defaultdict

# ============ 配置 ============
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID', 0))

# 身份组配置 (Clearance Levels)
ROLES_CONFIG = {
    'protocol': {'name': '🤖 Protocol・协议', 'color': 0x95A5A6, 'level': 0},
    'awakened': {'name': '🟢 Awakened・觉醒者', 'color': 0x2ECC71, 'level': 1},
    'augmented': {'name': '🔵 Augmented・增强者', 'color': 0x3498DB, 'level': 2},
    'vanguard': {'name': '🟠 Vanguard・先锋', 'color': 0xE67E22, 'level': 3},
    'architect': {'name': '🔴 Architect・架构师', 'color': 0xE74C3C, 'level': 3},
    'core': {'name': '⚡ System Core・系统核心', 'color': 0xFFD700, 'level': 4},
}

# 算力配置 (Compute Points)
COMPUTE_PER_MESSAGE = 5
COMPUTE_COOLDOWN = 60
LEVEL_MULTIPLIER = 100

# 版本称号
VERSION_TITLES = {
    1: 'v1.0 初期型号',
    5: 'v1.5 稳定版本',
    10: 'v2.0 迭代版本',
    20: 'v2.5 增强版本',
    50: 'v3.0 完全体',
    100: 'v4.0 超越者',
}

# 违禁词
BANNED_WORDS = ['广告词1', '广告词2']

# ============ 视觉配置 ============
COLORS = {
    'success': 0x00D26A,    # 亮绿
    'primary': 0x5865F2,    # Discord 蓝紫
    'warning': 0xFEE75C,    # 警告黄
    'danger': 0xED4245,     # 危险红
    'gold': 0xF1C40F,       # 金色
    'cyan': 0x00CED1,       # 赛博青
    'dark': 0x2F3136,       # 深灰
}

# ============ Bot 初始化 ============
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

# 数据存储
user_data = defaultdict(lambda: {'compute': 0, 'level': 1, 'last_time': None, 'messages': 0})
DATA_FILE = 'user_data.json'

def load_data():
    global user_data
    try:
        with open(DATA_FILE, 'r') as f:
            loaded = json.load(f)
            user_data = defaultdict(lambda: {'compute': 0, 'level': 1, 'last_time': None, 'messages': 0}, loaded)
    except FileNotFoundError:
        pass

def save_data():
    with open(DATA_FILE, 'w') as f:
        json.dump(dict(user_data), f, indent=2, default=str)

def get_version(level):
    """获取版本称号"""
    version = 'v0.9 原型'
    for lvl, v in sorted(VERSION_TITLES.items()):
        if level >= lvl:
            version = v
    return version

def progress_bar(current, total, length=10):
    """生成进度条"""
    filled = int(length * current / total) if total > 0 else 0
    empty = length - filled
    bar = '█' * filled + '░' * empty
    percent = int(100 * current / total) if total > 0 else 0
    return f"`{bar}` {percent}%"

# ============ 事件处理 ============

@bot.event
async def on_ready():
    print(f'✅ {bot.user} 已上线')
    print(f'📡 已连接 {len(bot.guilds)} 个基地')
    load_data()

    try:
        synced = await bot.tree.sync()
        print(f'⚡ 已同步 {len(synced)} 个指令')
    except Exception as e:
        print(f'❌ 指令同步失败: {e}')

    if not daily_report.is_running():
        daily_report.start()

@bot.event
async def on_member_join(member: discord.Member):
    """新成员接入"""
    guild = member.guild

    # 分配 Awakened 权限
    awakened_role = discord.utils.find(lambda r: 'Awakened' in r.name, guild.roles)
    if awakened_role:
        await member.add_roles(awakened_role)

    # 发送接入协议
    welcome_channel = discord.utils.find(lambda c: 'human-touch' in c.name, guild.text_channels)
    if not welcome_channel:
        welcome_channel = guild.system_channel

    if welcome_channel:
        embed = discord.Embed(
            title="",
            description="",
            color=COLORS['cyan']
        )
        embed.set_author(name="⚡ SIGNAL CONNECTED", icon_url=member.display_avatar.url)

        embed.add_field(
            name="",
            value=(
                f"欢迎，**{member.display_name}**\n"
                f"这里是 **[蜕升计划]** 的前哨站。\n"
                f"外面的世界正在断裂，人类正在分裂为两个物种。\n"
                f"这里没有安慰剂，只有进化的武器。"
            ),
            inline=False
        )

        embed.add_field(
            name="📡 接入状态",
            value=(
                f"```\n"
                f"权限等级: L1 Awakened\n"
                f"识别码:   {member.id}\n"
                f"状态:     ACTIVE\n"
                f"```"
            ),
            inline=False
        )

        embed.add_field(
            name="🔰 初始化任务",
            value=(
                "> `01` 阅读 **#nav-chart**，签署接入协议\n"
                "> `02` 在 **#alliance** 留下识别信号\n"
                "> `03` 需要高级武器？前往 **#access-key**"
            ),
            inline=False
        )

        embed.set_footer(text="「不要温和地走进那个良夜。」")
        embed.timestamp = datetime.utcnow()

        await welcome_channel.send(embed=embed)

@bot.event
async def on_message(message: discord.Message):
    """消息处理 - 算力累积 + 内容过滤"""
    if message.author.bot:
        return

    # 内容过滤
    if any(word in message.content.lower() for word in BANNED_WORDS):
        await message.delete()
        await message.channel.send(
            f"{message.author.mention} `⚠️ 信号异常，已被协议过滤`",
            delete_after=5
        )
        return

    # 算力系统
    user_id = str(message.author.id)
    now = datetime.utcnow()
    last_time = user_data[user_id].get('last_time')

    if last_time:
        last_time = datetime.fromisoformat(last_time) if isinstance(last_time, str) else last_time
        if (now - last_time).seconds < COMPUTE_COOLDOWN:
            await bot.process_commands(message)
            return

    user_data[user_id]['compute'] += COMPUTE_PER_MESSAGE
    user_data[user_id]['messages'] += 1
    user_data[user_id]['last_time'] = now.isoformat()

    # 检查升级
    current_level = user_data[user_id]['level']
    compute_needed = current_level * LEVEL_MULTIPLIER

    if user_data[user_id]['compute'] >= compute_needed:
        user_data[user_id]['level'] += 1
        user_data[user_id]['compute'] = 0
        new_level = user_data[user_id]['level']
        new_version = get_version(new_level)

        embed = discord.Embed(
            description=(
                f"**⚡ VERSION UPGRADE**\n\n"
                f"{message.author.mention}\n"
                f"```\n"
                f"NEW LEVEL:   Lv.{new_level}\n"
                f"VERSION:     {new_version}\n"
                f"STATUS:      EVOLUTION COMPLETE\n"
                f"```"
            ),
            color=COLORS['gold']
        )
        await message.channel.send(embed=embed, delete_after=15)

    save_data()
    await bot.process_commands(message)

# ============ 斜杠命令 ============

@bot.tree.command(name="status", description="查看你的系统状态")
async def status(interaction: discord.Interaction):
    """查看个人状态"""
    user_id = str(interaction.user.id)
    data = user_data[user_id]
    version = get_version(data['level'])
    compute_needed = data['level'] * LEVEL_MULTIPLIER

    embed = discord.Embed(
        title="",
        color=COLORS['primary']
    )
    embed.set_author(
        name=f"{interaction.user.display_name} | SYSTEM STATUS",
        icon_url=interaction.user.display_avatar.url
    )

    # 主要数据区
    embed.add_field(
        name="",
        value=(
            f"```\n"
            f"╔══════════════════════════════╗\n"
            f"║  LEVEL      │  Lv.{data['level']:>3}          ║\n"
            f"║  VERSION    │  {version:<14}║\n"
            f"║  SIGNALS    │  {data['messages']:>5} msgs      ║\n"
            f"╚══════════════════════════════╝\n"
            f"```"
        ),
        inline=False
    )

    # 算力进度
    embed.add_field(
        name="💾 COMPUTE POWER",
        value=f"{progress_bar(data['compute'], compute_needed)}\n`{data['compute']} / {compute_needed}`",
        inline=False
    )

    embed.set_thumbnail(url=interaction.user.display_avatar.url)
    embed.set_footer(text="蜕升计划 | The Ascension Protocol")
    embed.timestamp = datetime.utcnow()

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="leaderboard", description="查看算力排行榜")
async def leaderboard(interaction: discord.Interaction):
    """排行榜"""
    sorted_users = sorted(
        user_data.items(),
        key=lambda x: (x[1]['level'], x[1]['compute']),
        reverse=True
    )[:10]

    embed = discord.Embed(
        title="",
        color=COLORS['gold']
    )
    embed.set_author(name="🏆 COMPUTE LEADERBOARD", icon_url=interaction.guild.icon.url if interaction.guild.icon else None)

    if not sorted_users:
        embed.description = "```\n暂无数据\n```"
    else:
        ranks = ['🥇', '🥈', '🥉', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '🔟']
        lines = []

        for i, (uid, data) in enumerate(sorted_users):
            try:
                user = await bot.fetch_user(int(uid))
                version = get_version(data['level'])
                lines.append(f"{ranks[i]} **{user.display_name}**\n   └ `Lv.{data['level']}` · {version}")
            except:
                continue

        embed.description = "\n\n".join(lines) if lines else "```\n暂无数据\n```"

    embed.set_footer(text="Top 10 by processing power")
    embed.timestamp = datetime.utcnow()

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="sync", description="每日同步，获取算力")
async def daily_sync(interaction: discord.Interaction):
    """每日签到"""
    user_id = str(interaction.user.id)
    today = datetime.utcnow().date().isoformat()

    if user_data[user_id].get('last_sync') == today:
        embed = discord.Embed(
            description="```diff\n- 今日已同步，明日再来\n```",
            color=COLORS['danger']
        )
        await interaction.response.send_message(embed=embed, ephemeral=True)
        return

    bonus = 50
    user_data[user_id]['compute'] += bonus
    user_data[user_id]['last_sync'] = today
    save_data()

    compute_needed = user_data[user_id]['level'] * LEVEL_MULTIPLIER

    embed = discord.Embed(
        title="",
        color=COLORS['success']
    )
    embed.set_author(name="✅ SYNC COMPLETE", icon_url=interaction.user.display_avatar.url)

    embed.add_field(
        name="",
        value=(
            f"```diff\n"
            f"+ 算力获取: +{bonus}\n"
            f"```"
        ),
        inline=False
    )

    embed.add_field(
        name="💾 当前算力",
        value=f"{progress_bar(user_data[user_id]['compute'], compute_needed)}\n`{user_data[user_id]['compute']} / {compute_needed}`",
        inline=False
    )

    embed.timestamp = datetime.utcnow()

    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="broadcast", description="[Core] 发布全频段广播")
@app_commands.describe(content="广播内容")
async def broadcast(interaction: discord.Interaction, content: str):
    """发布公告"""
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("`❌ 权限不足：需要 System Core`", ephemeral=True)
        return

    embed = discord.Embed(
        title="📢 GLOBAL SIGNAL",
        description=f"\n{content}\n",
        color=COLORS['gold']
    )
    embed.set_author(name=interaction.user.display_name, icon_url=interaction.user.display_avatar.url)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text="蜕升计划 | The Ascension Protocol")

    announce_channel = discord.utils.find(lambda c: 'global-signal' in c.name, interaction.guild.text_channels)
    if announce_channel:
        await announce_channel.send(embed=embed)
        await interaction.response.send_message("`✅ 广播已发射`", ephemeral=True)
    else:
        await interaction.response.send_message(embed=embed)

@bot.tree.command(name="upgrade", description="[Core] 提升成员权限等级")
@app_commands.describe(member="目标成员", clearance="目标权限")
@app_commands.choices(clearance=[
    app_commands.Choice(name="L2 Augmented (增强者)", value="augmented"),
    app_commands.Choice(name="L3 Vanguard (先锋)", value="vanguard"),
    app_commands.Choice(name="L3 Architect (架构师)", value="architect"),
])
async def upgrade(interaction: discord.Interaction, member: discord.Member, clearance: str):
    """晋升成员"""
    if not interaction.user.guild_permissions.administrator:
        await interaction.response.send_message("`❌ 权限不足`", ephemeral=True)
        return

    role_config = ROLES_CONFIG.get(clearance)
    if not role_config:
        await interaction.response.send_message("`❌ 无效的权限等级`", ephemeral=True)
        return

    role = discord.utils.find(lambda r: clearance.capitalize() in r.name or role_config['name'] in r.name, interaction.guild.roles)
    if not role:
        await interaction.response.send_message("`❌ 找不到对应身份组`", ephemeral=True)
        return

    # 移除旧等级
    for key, config in ROLES_CONFIG.items():
        if key in ['awakened', 'augmented', 'vanguard', 'architect']:
            old_role = discord.utils.find(lambda r: key.capitalize() in r.name, interaction.guild.roles)
            if old_role and old_role in member.roles:
                await member.remove_roles(old_role)

    await member.add_roles(role)

    embed = discord.Embed(
        description=(
            f"**⚡ CLEARANCE UPGRADED**\n\n"
            f"{member.mention}\n"
            f"```\n"
            f"NEW LEVEL:   {role.name}\n"
            f"STATUS:      AUTHORIZED\n"
            f"```"
        ),
        color=role_config['color']
    )
    await interaction.response.send_message(embed=embed)

@bot.tree.command(name="disconnect", description="[Core] 断开成员连接")
@app_commands.describe(member="目标成员", reason="原因")
async def disconnect_member(interaction: discord.Interaction, member: discord.Member, reason: str = "违反协议"):
    """踢出成员"""
    if not interaction.user.guild_permissions.kick_members:
        await interaction.response.send_message("`❌ 权限不足`", ephemeral=True)
        return

    try:
        await member.kick(reason=reason)
        embed = discord.Embed(
            description=(
                f"**🚫 CONNECTION TERMINATED**\n\n"
                f"```\n"
                f"TARGET:  {member.display_name}\n"
                f"REASON:  {reason}\n"
                f"STATUS:  DISCONNECTED\n"
                f"```"
            ),
            color=COLORS['danger']
        )
        await interaction.response.send_message(embed=embed)
    except discord.Forbidden:
        await interaction.response.send_message("`❌ 无法断开此连接`", ephemeral=True)

# ============ 定时任务 ============

@tasks.loop(hours=24)
async def daily_report():
    """每日报告"""
    await bot.wait_until_ready()

    if not GUILD_ID:
        return

    guild = bot.get_guild(GUILD_ID)
    if not guild:
        return

    log_channel = discord.utils.find(lambda c: 'system-log' in c.name, guild.text_channels)
    if not log_channel:
        return

    total = guild.member_count
    online = len([m for m in guild.members if m.status != discord.Status.offline])
    signals = sum(d['messages'] for d in user_data.values())

    embed = discord.Embed(
        title="",
        color=COLORS['primary']
    )
    embed.set_author(name="📊 DAILY SYSTEM REPORT")
    embed.add_field(
        name="",
        value=(
            f"```\n"
            f"╔══════════════════════════════╗\n"
            f"║  TOTAL NODES  │  {total:>5}       ║\n"
            f"║  ONLINE       │  {online:>5}       ║\n"
            f"║  SIGNALS      │  {signals:>5}       ║\n"
            f"╚══════════════════════════════╝\n"
            f"```"
        ),
        inline=False
    )
    embed.timestamp = datetime.utcnow()

    await log_channel.send(embed=embed)

# ============ 启动 ============

if __name__ == '__main__':
    if not TOKEN:
        print("❌ 错误：请设置 DISCORD_TOKEN 环境变量")
        exit(1)
    bot.run(TOKEN)
