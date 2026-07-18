import os
import discord
from discord.ext import commands

from coc_api import get_player
from war_signup import post_signup
from database import setup_database

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(
    command_prefix="!",
    intents=intents
)


@bot.event
async def on_ready():
    setup_database()

    print("=" * 40)
    print(f"✅ Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

    print("🤖 ClanHQ is online!")
    print("=" * 40)


@bot.tree.command(
    name="ping",
    description="Check if ClanHQ is online"
)
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(
        "🏓 Pong! ClanHQ is online!"
    )


@bot.tree.command(
    name="help",
    description="Show ClanHQ commands"
)
async def help(interaction: discord.Interaction):

    embed = discord.Embed(
        title="🤖 ClanHQ Commands",
        colour=discord.Colour.blue()
    )

    embed.add_field(
        name="General",
        value="""
🏓 /ping
❓ /help
""",
        inline=False
    )

    embed.add_field(
        name="Clash",
        value="""
👤 /player
⚔️ /warsignup
""",
        inline=False
    )

    await interaction.response.send_message(embed=embed)


@bot.tree.command(
    name="player",
    description="View a Clash of Clans player"
)
async def player(interaction: discord.Interaction, tag: str):

    await interaction.response.defer()

    data = get_player(tag)

    if not data:
        await interaction.followup.send(
            "❌ Player not found or Clash API unavailable."
        )
        return

    embed = discord.Embed(
        title=data["name"],
        colour=discord.Colour.green()
    )

    embed.add_field(
        name="🏰 Town Hall",
        value=data["townHallLevel"],
        inline=True
    )

    embed.add_field(
        name="🏆 Trophies",
        value=data["trophies"],
        inline=True
    )

    embed.add_field(
        name="⭐ XP Level",
        value=data["expLevel"],
        inline=True
    )

    if "clan" in data:
        embed.add_field(
            name="🛡️ Clan",
            value=data["clan"]["name"],
            inline=False
        )

    await interaction.followup.send(embed=embed)


@bot.tree.command(
    name="warsignup",
    description="Create a war signup message"
)
async def warsignup(interaction: discord.Interaction):
    await post_signup(interaction)


if not TOKEN:
    raise ValueError(
        "DISCORD_TOKEN environment variable is not set."
    )

bot.run(TOKEN)
