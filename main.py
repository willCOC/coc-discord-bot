import os
import aiohttp
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()

bot = commands.Bot(command_prefix="!", intents=intents)


async def print_public_ip():
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("https://api.ipify.org") as response:
                ip = await response.text()
                print("=" * 40)
                print(f"🌐 Railway Public IP: {ip}")
                print("=" * 40)
    except Exception as e:
        print(f"❌ Could not get public IP: {e}")


@bot.event
async def on_ready():
    print("=" * 40)
    print(f"✅ Logged in as {bot.user}")

    try:
        synced = await bot.tree.sync()
        print(f"✅ Synced {len(synced)} slash commands.")
    except Exception as e:
        print(f"❌ Failed to sync commands: {e}")

    await print_public_ip()

    print("🤖 ClanHQ is online!")
    print("=" * 40)


@bot.tree.command(name="ping", description="Check if ClanHQ is online")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message("🏓 Pong! ClanHQ is online!")


@bot.tree.command(name="help", description="Show ClanHQ commands")
async def help_command(interaction: discord.Interaction):
    await interaction.response.send_message(
        "**🤖 ClanHQ Commands**\n\n"
        "🏓 `/ping` - Check if the bot is online\n"
        "❓ `/help` - Show this help menu"
    )


if not TOKEN:
    raise ValueError("DISCORD_TOKEN environment variable is not set.")

bot.run(TOKEN)
