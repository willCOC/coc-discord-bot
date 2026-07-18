import discord

# Stores who is IN or OUT (temporary - resets if the bot restarts)
war_signups = {}


class WarSignupView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label="✅ I'm In", style=discord.ButtonStyle.success)
    async def join_war(self, interaction: discord.Interaction, button: discord.ui.Button):
        war_signups[interaction.user.id] = "IN"
        await interaction.response.send_message(
            "✅ You have been signed up for the next war!",
            ephemeral=True
        )

    @discord.ui.button(label="❌ I'm Out", style=discord.ButtonStyle.danger)
    async def leave_war(self, interaction: discord.Interaction, button: discord.ui.Button):
        war_signups[interaction.user.id] = "OUT"
        await interaction.response.send_message(
            "❌ You have been removed from the next war.",
            ephemeral=True
        )


async def post_signup(interaction: discord.Interaction):
    embed = discord.Embed(
        title="⚔️ Clan War Signup",
        description=(
            "Click a button below to let the leaders know if you're available.\n\n"
            "✅ = I'm In\n"
            "❌ = I'm Out"
        ),
        colour=discord.Colour.red()
    )

    await interaction.response.send_message(
        embed=embed,
        view=WarSignupView()
    )
