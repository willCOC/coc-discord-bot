import os
import discord
from discord.ext import commands

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print("=" * 40)
    print(f"✅ Logged in as {bot.user}")
    print("🤖 ClanHQ is online!")
    print("=" * 40)


@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong! ClanHQ is online.")


if __name__ == "__main__":
    if not TOKEN:
        print("❌ DISCORD_TOKEN not found.")
    else:
        bot.run(TOKEN)
