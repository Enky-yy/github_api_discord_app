import discord
from discord import app_commands
from discord.ext import commands, tasks
import asyncio
import itertools

intents = discord.Intents.default()
intents.message_content=True
intents.members=True

bot = commands.Bot(command_prefix="/" , intents=intents)

statuses = itertools.cycle([
    "Watching over the Server",
    'Pushing commits to Main',
    "Reading README.md"
])

@tasks.loop(seconds=10)
async def change_status():
    await bot.change_presence(
        status=statuses,
        activity=discord.Activity(
            type = discord.ActivityType.watching,
            name = next(statuses)
        )
    )


@bot.event
async def on_ready():
    print("logged in as {0} , yehehe".format(bot.user))
    await change_status()
    await bot.tree.sync()
    print("Slash Commands activated and synced")

async def load_ext():
    await bot.load_extension('cogs.github')
    await bot.load_extension('managements.*')

secret = ""

async def main():
    async with bot:
        await load_ext()
        await bot.start(secret)

asyncio.run(main())

