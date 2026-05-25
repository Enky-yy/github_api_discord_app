from discord.ext import commands
import discord
import time

class AutoMod(commands.Cog):
    def __init__(self,bot):
        self.bot = bot
        self.spam={}
    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot : return
        now = time.time()
        user =message.author.id
        self.spam.setdefault(user,[])
        self.spam[user] = [t for t in self.spam[user] if now -t <5]
        self.spam[user].append(now)

        if len(self.spam[user])>5 :
            await message.channel.send('{} please slow down'.format(message.author.mention))
            self.spam[user].clear()

            await self.bot.process_commands(message)

async def setup(bot):
    await bot.add_cog(AutoMod(bot))

