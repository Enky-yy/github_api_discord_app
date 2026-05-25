from discord.ext import commands
from discord import app_commands
import discord

class Channels(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @app_commands.command(name='Create Text')
    @app_commands.checks.has_permissions(manage_channels=True)
    async def create_text(self,interaction:discord.Interaction,name:str):
        guild = interaction.guild
        await guild.create_text_channel(name=name)
        await interaction.response.send_message(f"Created Text channel: **{name}**")

    @app_commands.command(name='Create Voice')
    @app_commands.checks.has_permissions(manage_channels=True)
    async def create_voice(self,interaction:discord.Interaction,name:str):
        guild = interaction.guild
        await guild.create_voice_channel(name=name)
        await interaction.response.send_message(f"Created Voice channel: **{name}**")

    @app_commands.command(name='Delete Text')
    @app_commands.checks.has_permissions(manage_channels=True)
    async def delete_text(self,interaction:discord.Interaction,text:discord.TextChannel):
        
        await text.delete(text)
        await interaction.response.send_message(f"Created channel: **{text}**")

    @app_commands.command(name="Delete Voice", description="Delete your current voice channel")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def delete_voice(self, interaction: discord.Interaction ,vc_name:discord.VoiceChannel):
        if vc_name: True 
        else: None

        if not vc_name:
            if interaction.user.voice:
                vc_name = interaction.user.voice.channel
            else:
                return await interaction.response.send_message("You're not in a voice channel!", ephemeral=True)

        await vc_name.delete()
        await interaction.response.send_message(f"Deleted voice channel: **{vc_name.name}**")


async def setup(bot):
    await bot.add_cog(Channels(bot))