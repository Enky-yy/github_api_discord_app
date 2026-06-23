import discord
from discord import app_commands
from discord.ext import commands, tasks
import asyncio
import itertools
from dotenv import load_dotenv
import os


from flask import Flask
import threading
import os

app = Flask(__name__)

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
    await bot.load_extension('managements.auto_embed')
    await bot.load_extension('managements.automod')
    await bot.load_extension('managements.channels')
    await bot.load_extension('managements.clear_msg')
    # await bot.load_extension('managements.database')
    await bot.load_extension('managements.embedded')
    await bot.load_extension('managements.loggingg')
    await bot.load_extension('managements.join_leave')
    await bot.load_extension('managements.moderation')


load_dotenv()
secret = os.getenv("MY_TOKEN")

@app.route("/")
def home():
    return "Bot online"

def run_web():
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 10000))
    )

threading.Thread(target=run_web, daemon=True).start()


async def main():
    async with bot:
        await load_ext()
        await bot.start(secret)

asyncio.run(main())

