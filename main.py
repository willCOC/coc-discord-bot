import os

print("===================================")
print("🤖 ClanHQ is starting...")
print("===================================")

TOKEN = os.getenv("DISCORD_TOKEN")

if TOKEN:
    print("✅ Discord token detected.")
else:
    print("⚠️ No Discord token found yet.")
