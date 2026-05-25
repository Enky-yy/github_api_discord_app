from discord.ext import commands
from discord import app_commands
import discord
import asyncio
from database import warn_user , get_warnings

class Moderation(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
    @app_commands.command(name='kick',description='Kick a member')
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self,interaction: discord.Interaction,member : discord.Member,reason:str ='No Reason'):
        await member.kick(reason=reason)
        await interaction.response.send_message('{} kicked. Reason: {}'.format(member,reason))

    @app_commands.command(name='ban',description='Ban a member')
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self,interaction: discord.Interaction,member : discord.Member,reason:str ='No Reason'):
        await member.ban(reason=reason)
        await interaction.response.send_message('{} banned. Reason: {}'.format(member,reason))

    @app_commands.command(name='warn',description='Warns a member')
    async def warn(self,interaction: discord.Interaction,member : discord.Member,reason:str ='No Reason'):
        await warn_user(member.id,reason)
        await interaction.response.send_message('{} has been warned'.format(member))

    @app_commands.command(name='warnings',description='check warnings')
    async def check_warning(self,interaction: discord.Interaction,member : discord.Member,reason:str ='No Reason'):
        warnings= await get_warnings(member.id)
        formatted = '\n'.join('{}. {}'.format(i+1,w) for i ,w in enumerate(warnings)) or 'No Warning'
        await interaction.response.send_message(formatted)
    
    
async def setup(bot):
    await bot.add_cog(Moderation(bot))




