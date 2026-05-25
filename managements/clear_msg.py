from discord.ext import commands
from discord import app_commands
import discord

class Clear(commands.Cog):
    def __init__(self,bot):
        self.bot =bot
    
    @app_commands.command(name='Clear emssages',description='Clear specified number of messages')
    @app_commands.checks.has_permissions(manage_messages=True)
    async def clear_messages(self , interation:discord.Interaction,member:discord.Member,limit:int):
        await interation.channel.purge(limit=limit)
        await interation.response.send_message(" Cleared **{}** messages!".format(limit), ephemeral=True)

async def setup(bot):
    await bot.add_cog(Clear(bot))