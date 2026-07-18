import discord
from database import save_signup, get_signups

class WarSignupView(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    async def refresh(self, interaction):
        signups = get_signups()

        in_players = []
        out_players = []

        for username, status in signups:
            if status == "IN":
                in_players.append(f"• {username}")
            else:
                out_players.append(f"• {username}")

        embed = discord.Embed(
            title="⚔️ Clan War Signup",
            description="Click a button below to choose your status.",
            colour=discord.Colour.red()
        )

        embed.add_field(
            name=f"✅ IN ({len(in_players)})",
            value="\n".join(in_players) if in_players else "Nobody yet.",
            inline=True
        )

        embed.add_field(
            name=f"❌ OUT ({len(out_players)})",
            value="\n".join(out_players) if out_players else "Nobody yet.",
            inline=True
        )

        await interaction.message.edit(embed=embed, view=self)

    @discord.ui.button(label="✅ I'm In", style=discord.ButtonStyle.success)
    async def join(self, interaction: discord.Interaction, button: discord.ui.Button):
        save_signup(
            interaction.user.id,
            interaction.user.display_name,
            "IN"
        )

        await interaction.response.defer()

        await self.refresh(interaction)

    @discord.ui.button(label="❌ I'm Out", style=discord.ButtonStyle.danger)
    async def leave(self, interaction: discord.Interaction, button: discord.ui.Button):
        save_signup(
            interaction.user.id,
            interaction.user.display_name,
            "OUT"
        )

        await interaction.response.defer()

        await self.refresh(interaction)


async def post_signup(interaction: discord.Interaction):

    embed = discord.Embed(
        title="⚔️ Clan War Signup",
        description="Click a button below to choose your status.",
        colour=discord.Colour.red()
    )

    embed.add_field(
        name="✅ IN (0)",
        value="Nobody yet.",
        inline=True
    )

    embed.add_field(
        name="❌ OUT (0)",
        value="Nobody yet.",
        inline=True
    )

    await interaction.response.send_message(
        embed=embed,
        view=WarSignupView()
    )
