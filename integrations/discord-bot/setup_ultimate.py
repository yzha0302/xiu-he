
import discord
import asyncio
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')
GUILD_ID = int(os.getenv('GUILD_ID', 0))

# ============ 1. Identity System (Roles) ============
# Rank: L1 to L5
ROLES = [
    # Bot
    {'name': '🤖 协议 | Protocol', 'color': 0x95A5A6, 'hoist': False, 'perm_level': 1},
    # Users
    {'name': '🟢 觉醒者 | Awakened', 'color': 0x2ECC71, 'hoist': True, 'perm_level': 2},  # L2: Public 
    {'name': '🔵 增强者 | Augmented', 'color': 0x3498DB, 'hoist': True, 'perm_level': 3}, # L3: Paid
    {'name': '🔴 架构师 | Architect', 'color': 0xE74C3C, 'hoist': True, 'perm_level': 4}, # L4: Mods
    {'name': '⚡ 系统核心 | System Core', 'color': 0xFFD700, 'hoist': True, 'perm_level': 5, 'admin': True},
]

# Role Map for easy access
ROLE_KEY_MAP = {
    'bot': '🤖 协议 | Protocol',
    'L2': '🟢 觉醒者 | Awakened',
    'L3': '🔵 增强者 | Augmented',
    'L4': '🔴 架构师 | Architect',
    'L5': '⚡ 系统核心 | System Core',
}

# ============ 2. The Matrix (Channels) ============
# Format: Emoji｜english-name・中文名
CATEGORIES = [
    {
        'name': '📡 系统广播 | SYSTEM BROADCAST',
        'channels': [
            {'name': '📢｜system-broadcast・系统广播', 'type': 'news', 'topic': 'Critical Updates & Announcements'},
            {'name': '📜｜manifesto・领主宣言', 'type': 'forum', 'topic': 'Deep Thoughts & Core Philosophy (Admin Post Only)'},
            {'name': '🗺️｜navigation・导航图', 'type': 'text', 'topic': 'Rules, Guidelines, and Orientations'},
            {'name': '💳｜access-key・权限密钥', 'type': 'text', 'topic': 'Upgrade to L3/L4 (Payment Portal)'},
        ],
        'access_level': 'public_read_admin_write' # L0 Read, L5 Write
    },
    {
        'name': '🌍 荒原连接 | THE WASTELAND',
        'channels': [
            {'name': '☕｜human-touch・人类温存', 'type': 'text', 'topic': 'General Chat & Connection'},
            {'name': '💡｜open-ideas・灵感集市', 'type': 'forum', 'topic': 'Share your ideas freely (Public Forum)'},
            {'name': '🎨｜creations・创作展示', 'type': 'forum', 'topic': 'Showcase your work (Public Forum)'},
            {'name': '🤝｜alliance・结盟', 'type': 'text', 'topic': 'Introductions & Networking'},
            {'name': '❓｜debug・排障', 'type': 'text', 'topic': 'Help & Support'},
            {'name': '🐦｜neural-feed・神经流', 'type': 'text', 'topic': 'Twitter/X Feed (Auto)', 'readonly': True},
        ],
        'access_level': 'public' # L0 Read/Write (except readonly channels)
    },
    {
        'name': '🛠️ 认知军械库 | COGNITIVE ARMORY',
        'channels': [
            {'name': '🔥｜prometheus・观火台', 'type': 'text', 'topic': 'Market Insight & Trend Analysis'},
            {'name': '🧠｜mental-os・思维操作系统', 'type': 'forum', 'topic': 'Methodology & Structured Learning'},
            {'name': '🔫｜tools-lib・工具库', 'type': 'text', 'topic': 'AI Tools, Prompts & Resources'},
            {'name': '📼｜black-box・黑匣子', 'type': 'text', 'topic': 'Archives & Recordings'},
        ],
        'access_level': 'L3' # L3+ Read/Write (Augmented)
    },
    {
        'name': '🚀 高维轨道 | HIGH ORBIT',
        'channels': [
            {'name': '🔭｜overview-effect・总观效应', 'type': 'text', 'topic': 'Strategic Discussion (Inner Circle)'},
            {'name': '⚡｜direct-link・神经直连', 'type': 'voice', 'topic': 'VIP Live Sessions'},
            {'name': '🥂｜club-lounge・云端会所', 'type': 'voice', 'topic': 'Casual Voice Hangout'},
        ],
        'access_level': 'L4' # L4+ Read/Write (Architect)
    },
    {
        'name': '⚔️ 赏金猎人 | BOUNTY BOARD',
        'channels': [
            {'name': '📜｜missions・任务板', 'type': 'text', 'topic': 'Community Jobs & Bounties'},
            {'name': '💰｜credits・信用点', 'type': 'text', 'topic': 'Shop & Redemption'},
        ],
        'access_level': 'public'
    },
    {
        'name': '🔧 后台管理 | BACKEND',
        'channels': [
            {'name': '⚙️｜system-log・系统日志', 'type': 'text', 'topic': 'Bot Logs'},
            {'name': '💸｜transaction-log・订单记录', 'type': 'text', 'topic': 'Sales & Payments'},
        ],
        'access_level': 'L5' # L5 Only
    },
]

async def setup_ultimate():
    intents = discord.Intents.default()
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'✅ Connected: {client.user}')
        guild = client.get_guild(GUILD_ID)
        
        if not guild:
            print("❌ Guild not found")
            await client.close()
            return

        print(f"📍 Deploying Ultimate Schema to: {guild.name}")

        # ===== 1. Roles =====
        print("\n🎭 Configuring Identity System...")
        role_objects = {} # Map Name -> Role Object
        
        for r_config in ROLES:
            existing = discord.utils.get(guild.roles, name=r_config['name'])
            if existing:
                print(f"  ⏭️  Role exists: {r_config['name']}")
                role_objects[r_config['name']] = existing
                # Optional: Update color/perms if needed, but skipping for safety
            else:
                perms = discord.Permissions(administrator=True) if r_config.get('admin') else discord.Permissions()
                role = await guild.create_role(
                    name=r_config['name'],
                    color=discord.Color(r_config['color']),
                    hoist=r_config['hoist'],
                    permissions=perms,
                    mentionable=True
                )
                print(f"  ✅ Created Role: {r_config['name']}")
                role_objects[r_config['name']] = role

        # ===== 2. Channels & Categories =====
        print("\n📁 Constructing The Matrix...")
        
        for cat_config in CATEGORIES:
            # --- Category Setup ---
            cat_name = cat_config['name']
            existing_cat = discord.utils.get(guild.categories, name=cat_name)
            
            # Define Base Perms for Category
            overwrites = {
                guild.default_role: discord.PermissionOverwrite(read_messages=False), # Default deny
            }
            
            # Apply Access Logic
            level = cat_config['access_level']
            
            if level == 'public' or level == 'public_read_admin_write':
                # Public: Everyone can read
                overwrites[guild.default_role] = discord.PermissionOverwrite(read_messages=True)
            elif level == 'L3':
                # L3+: Augmented, Architect, Core
                for role_key in ['L3', 'L4', 'L5']:
                    r_obj = role_objects.get(ROLE_KEY_MAP[role_key])
                    if r_obj: overwrites[r_obj] = discord.PermissionOverwrite(read_messages=True)
            elif level == 'L4':
                # L4+: Architect, Core
                for role_key in ['L4', 'L5']:
                    r_obj = role_objects.get(ROLE_KEY_MAP[role_key])
                    if r_obj: overwrites[r_obj] = discord.PermissionOverwrite(read_messages=True)
            elif level == 'L5':
                # L5: Core only
                r_obj = role_objects.get(ROLE_KEY_MAP['L5'])
                if r_obj: overwrites[r_obj] = discord.PermissionOverwrite(read_messages=True)

            if existing_cat:
                category = existing_cat
                # await category.edit(overwrites=overwrites) # Optional: Enforce perms
            else:
                category = await guild.create_category(cat_name, overwrites=overwrites)
                print(f"  ✅ Created Category: {cat_name}")

            # --- Channel Setup ---
            for ch_config in cat_config['channels']:
                ch_name = ch_config['name']
                ch_type = ch_config['type']
                ch_topic = ch_config['topic']
                
                existing_ch = discord.utils.get(guild.channels, name=ch_name)
                
                # Check Overwrites for Channels (Special cases)
                ch_overwrites = {} 
                # (Permissions sync with category by default, unless specified)
                
                # Case: Public Read / Admin Write (e.g. System Broadcast)
                if level == 'public_read_admin_write' or ch_config.get('readonly'):
                     # Deny Send for Public
                     ch_overwrites[guild.default_role] = discord.PermissionOverwrite(
                         read_messages=True, 
                         send_messages=False,
                         create_public_threads=False
                     )
                     # Allow Send for L5
                     l5_role = role_objects.get(ROLE_KEY_MAP['L5'])
                     if l5_role:
                         ch_overwrites[l5_role] = discord.PermissionOverwrite(
                             read_messages=True, 
                             send_messages=True,
                             create_public_threads=True,
                             manage_messages=True
                         )
                
                # Case: Forum (Needs message_content for some bots, threads for users)
                # Forum permissions are tricky, usually managed via 'send_messages' (post)
                
                create_kwargs = {
                    'name': ch_name,
                    'category': category,
                    'topic': ch_topic
                }
                if ch_overwrites:
                    create_kwargs['overwrites'] = ch_overwrites

                if existing_ch and existing_ch.category == category:
                    print(f"    ⏭️  {ch_name} exists")
                    continue
                
                try:
                    if ch_type == 'voice':
                        if 'topic' in create_kwargs: del create_kwargs['topic']
                        await guild.create_voice_channel(**create_kwargs)
                    elif ch_type == 'news':
                        await guild.create_text_channel(news=True, **create_kwargs)
                    elif ch_type == 'forum':
                        await guild.create_forum(**create_kwargs)
                    else:
                        await guild.create_text_channel(**create_kwargs)
                    print(f"    ✅ Created: {ch_name}")
                except Exception as e:
                    print(f"    ❌ Failed {ch_name}: {e}")

        print("\n🎉 Ultimate Setup Complete.")
        await client.close()

    await client.start(TOKEN)

if __name__ == '__main__':
    asyncio.run(setup_ultimate())
