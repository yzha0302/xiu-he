"""
蜕升计划 (The Ascension Protocol) - 服务器初始化脚本
一键创建所有频道和身份组
运行一次即可
"""

import discord
import asyncio
import os

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID', 0))

# ============ 身份组配置 (Clearance Levels) ============
ROLES = [
    {'name': '🤖 Protocol', 'color': 0x95A5A6, 'permissions': discord.Permissions(), 'hoist': False},
    {'name': '🟢 Awakened', 'color': 0x2ECC71, 'permissions': discord.Permissions(), 'hoist': True},
    {'name': '🔵 Augmented', 'color': 0x3498DB, 'permissions': discord.Permissions(), 'hoist': True},
    {'name': '🔴 Architect', 'color': 0xE74C3C, 'permissions': discord.Permissions(), 'hoist': True},
    {'name': '⚡ System Core', 'color': 0xFFD700, 'permissions': discord.Permissions(administrator=True), 'hoist': True},
]

# ============ 频道配置 ============
CATEGORIES = [
    {
        'name': '📡 SYSTEM BROADCAST',
        'channels': [
            {'name': 'global-signal', 'type': 'text', 'topic': '系统广播 | 重大更新', 'readonly': True},
            {'name': 'nav-chart', 'type': 'text', 'topic': '导航图 | 规则与指引', 'readonly': True},
            {'name': 'access-key', 'type': 'text', 'topic': '权限密钥 | 付费入口', 'readonly': True},
        ],
        'access': ['all']
    },
    {
        'name': '🌍 THE WASTELAND',
        'channels': [
            {'name': 'human-touch', 'type': 'text', 'topic': '人类温存 | 自由交流'},
            {'name': 'signal-fire', 'type': 'text', 'topic': '烽火台 | 情报共享'},
            {'name': 'alliance', 'type': 'text', 'topic': '结盟 | 自我介绍'},
            {'name': 'debug', 'type': 'text', 'topic': '排障 | 公开提问'},
        ],
        'access': ['all']
    },
    {
        'name': '🛠️ COGNITIVE ARMORY',
        'channels': [
            {'name': 'mental-os', 'type': 'text', 'topic': '思维操作系统 | 深度方法论'},
            {'name': 'tools-lib', 'type': 'text', 'topic': '工具库 | AI工具/Prompt/源码'},
            {'name': 'black-box', 'type': 'text', 'topic': '黑匣子 | 视频/直播回放'},
            {'name': 'lab-notes', 'type': 'text', 'topic': '实验笔记 | 碎片思考'},
        ],
        'access': ['augmented', 'architect', 'core']
    },
    {
        'name': '🚀 HIGH ORBIT',
        'channels': [
            {'name': 'overview-effect', 'type': 'text', 'topic': '总观效应 | 战略讨论'},
            {'name': 'direct-link', 'type': 'voice', 'topic': '神经直连 | VIP直播'},
            {'name': 'club-lounge', 'type': 'voice', 'topic': '云端会所 | 语音挂机'},
        ],
        'access': ['architect', 'core']
    },
    {
        'name': '⚔️ BOUNTY BOARD',
        'channels': [
            {'name': 'missions', 'type': 'text', 'topic': '任务板 | 社区任务'},
            {'name': 'credits', 'type': 'text', 'topic': '信用点 | 积分兑换'},
        ],
        'access': ['all']
    },
    {
        'name': '🔧 BACKEND',
        'channels': [
            {'name': 'system-log', 'type': 'text', 'topic': 'Bot日志'},
            {'name': 'transaction-log', 'type': 'text', 'topic': '订单记录'},
        ],
        'access': ['core']
    },
]

# ============ 角色映射 ============
ROLE_MAP = {
    'awakened': '🟢 Awakened',
    'augmented': '🔵 Augmented',
    'architect': '🔴 Architect',
    'core': '⚡ System Core',
}

async def setup_server():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'✅ Connected: {client.user}')

        if not GUILD_ID:
            print("❌ GUILD_ID not set")
            await client.close()
            return

        guild = client.get_guild(GUILD_ID)
        if not guild:
            print(f"❌ Guild not found: {GUILD_ID}")
            await client.close()
            return

        print(f"📍 Target: {guild.name}")

        # ===== 创建身份组 =====
        print("\n🎭 Creating clearance levels...")
        created_roles = {}

        for role_config in ROLES:
            existing = discord.utils.get(guild.roles, name=role_config['name'])
            if existing:
                print(f"  ⏭️  {role_config['name']} exists")
                created_roles[role_config['name']] = existing
            else:
                role = await guild.create_role(
                    name=role_config['name'],
                    color=discord.Color(role_config['color']),
                    permissions=role_config['permissions'],
                    hoist=role_config['hoist'],
                    mentionable=True
                )
                print(f"  ✅ Created: {role_config['name']}")
                created_roles[role_config['name']] = role

        # 调整顺序
        print("\n📊 Adjusting hierarchy...")
        positions = {}
        for i, role_config in enumerate(reversed(ROLES)):
            role = created_roles[role_config['name']]
            positions[role] = i + 1

        try:
            await guild.edit_role_positions(positions)
            print("  ✅ Hierarchy set")
        except Exception as e:
            print(f"  ⚠️ Could not adjust: {e}")

        # ===== 创建频道 =====
        print("\n📁 Building channels...")

        for category_config in CATEGORIES:
            existing_cat = discord.utils.get(guild.categories, name=category_config['name'])
            if existing_cat:
                print(f"  ⏭️  {category_config['name']} exists")
                category = existing_cat
            else:
                overwrites = {
                    guild.default_role: discord.PermissionOverwrite(read_messages=False)
                }

                access = category_config['access']
                if 'all' in access:
                    overwrites[guild.default_role] = discord.PermissionOverwrite(read_messages=True)
                else:
                    for role_key in access:
                        role_name = ROLE_MAP.get(role_key)
                        if role_name:
                            role = created_roles.get(role_name)
                            if role:
                                overwrites[role] = discord.PermissionOverwrite(
                                    read_messages=True,
                                    send_messages=True,
                                    connect=True,
                                    speak=True
                                )

                category = await guild.create_category(
                    name=category_config['name'],
                    overwrites=overwrites
                )
                print(f"  ✅ Created: {category_config['name']}")

            for channel_config in category_config['channels']:
                channel_name = channel_config['name']
                existing_channel = discord.utils.get(
                    guild.channels,
                    name=channel_name
                )

                if existing_channel and existing_channel.category == category:
                    print(f"    ⏭️  {channel_name} exists")
                    continue

                channel_overwrites = {}

                if channel_config.get('readonly'):
                    channel_overwrites[guild.default_role] = discord.PermissionOverwrite(
                        read_messages=True,
                        send_messages=False
                    )
                    core_role = created_roles.get('⚡ System Core')
                    if core_role:
                        channel_overwrites[core_role] = discord.PermissionOverwrite(
                            read_messages=True,
                            send_messages=True
                        )

                if channel_config['type'] == 'voice':
                    await guild.create_voice_channel(
                        name=channel_name,
                        category=category,
                        overwrites=channel_overwrites if channel_overwrites else None
                    )
                else:
                    await guild.create_text_channel(
                        name=channel_name,
                        category=category,
                        topic=channel_config.get('topic', ''),
                        overwrites=channel_overwrites if channel_overwrites else None
                    )
                print(f"    ✅ Created: {channel_name}")

        # ===== Bot 身份 =====
        print("\n🤖 Assigning Protocol role...")
        protocol_role = created_roles.get('🤖 Protocol')
        if protocol_role:
            bot_member = guild.get_member(client.user.id)
            if bot_member:
                await bot_member.add_roles(protocol_role)
                print("  ✅ Protocol assigned")

        print("\n" + "=" * 50)
        print("🎉 BASE CONSTRUCTION COMPLETE")
        print("=" * 50)
        print("\nNext steps:")
        print("1. Edit #nav-chart - add your rules")
        print("2. Edit #access-key - add payment links")
        print("3. Assign yourself ⚡ System Core role")
        print("4. Deploy bot to Railway")

        await client.close()

    await client.start(TOKEN)

if __name__ == '__main__':
    if not TOKEN:
        print("❌ Set DISCORD_TOKEN")
        exit(1)
    if not GUILD_ID:
        print("❌ Set GUILD_ID")
        exit(1)

    asyncio.run(setup_server())
