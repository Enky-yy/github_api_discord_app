from discord import app_commands
from discord.ext import commands
import discord

class auto_embed(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.bot:
            return
        
        target_channel = discord.utils.get(message.guild.text_channels, name="general")

        if target_channel and message.channel == target_channel:
            embed = discord.Embed(
                description=message.content,
                color=0x5865F2
            )
            embed.set_author(
                name=str(message.author),
                icon_url=message.author.avatar.url if message.author.avatar else None
            )
            embed.set_footer(text="From HOGWARTS")

            await message.delete()
            await target_channel.send(embed=embed)

        await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(auto_embed(bot))
