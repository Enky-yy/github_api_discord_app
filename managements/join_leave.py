import discord
from discord.ext import commands
from discord import app_commands

class Reception(commands.Cog):
    def __init__(self,bot):
        self.bot=bot


    @commands.Cog.listener()
    async def welcome(member:discord.Member):
        target_guild = discord.utils.get(member.guild.text_channels, name="general")

        if not target_guild:
            return
        
        embed = discord.Embed(
            title="Welcome",
            description="have a great day"
        )

        # embed.set_thumbnail(url="/")
        embed.set_author(name=str(member), icon_url=member.avatar.url if member.avatar.url else None)

        embed.set_footer('Meow Meow')
        embed.timestamp= discord.utils.utcnow()

        await target_guild.send(embed=embed)

    @commands.Cog.listener()
    async def leave(member:discord.Member):
        target_guild = discord.utils.get(member.guild.text_channels, name="general")

        if not target_guild:
            return 
        
        embed = discord.Embed(
            title='Byeee',
            description='have a great day'
        )

        embed.set_thumbnail(url='/')
        embed.set_author(name=str(member), icon_url= member.avatar.url if member.avatar.url else None)

        embed.set_footer('Meow Meow')

        await target_guild.send(embed=embed)



    @commands.Cog.listener()
    async def on_message_delete(message):
        if message.author.bot:
            return
        log = discord.utils.get(message.guild.text_channels, name="moderator-only")
        if log:
            embed = discord.Embed(
                title="🗑️ Message Deleted",
                description=f"**Author:** {message.author.mention}\n**Content:** {message.content}",
                color=0xFAA61A
            )
            embed.timestamp = discord.utils.utcnow()
            await log.send(embed=embed)



async def setup(bot):
    await bot.add_cog(Reception(bot=bot))