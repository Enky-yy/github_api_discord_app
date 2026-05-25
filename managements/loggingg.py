import discord
from discord.ext import commands

LOG_CHANNEL_id ='1432340635083608117'

class logging(commands.Cog):
    def __init__(self,bot):
        self.bot =bot

    @commands.Cog.listener()
    async def on_member_ban(self,guild , user):
        channel = guild.get_channel(LOG_CHANNEL_id)
        if channel:
            await channel.send('{} has been kicked'.format(user))
    
    @commands.Cog.listener()
    async def on_member_remove(self,member):
        channel = member.guild.get_channel(LOG_CHANNEL_id)
        if channel:
            await channel.send('{} has left or kicked'.format(member))
    

async def setup(bot):
    await bot.add_cog(logging(bot))