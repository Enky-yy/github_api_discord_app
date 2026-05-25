import discord
from discord import app_commands
from discord.ext import commands

class embeds(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="sendembed", description="Sends an Embedded message")
    @app_commands.checks.has_permissions(send_messages=True)
    async def sendEmbed(self, interaction: discord.Interaction):

        target_channel =discord.utils.get(interaction.guild.text_channels,name='general')

        if not interaction.guild.text_channels:
            return await interaction.response.send_message("No text channels found", ephemeral=True)


        embed = discord.Embed(
            title="Hello",
            description="Hey Guys welcome to my channel",
            color=0x5865F2
        )

        # embed.set_thumbnail(url="/")
        # embed.set_image(url="/")

        embed.set_author(
            name=str(interaction.user),
            icon_url=interaction.user.avatar.url if interaction.user.avatar else None
        )

        embed.set_footer(text=f"by {interaction.user}")
        # embed.timestamp = discord.utils.utcnow()

        await target_channel.send(embed=embed)
        await interaction.response.send_message("Announcement sent successfully", ephemeral=True)

async def setup(bot):
    await bot.add_cog(embeds(bot))
