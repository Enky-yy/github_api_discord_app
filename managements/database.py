import sqlite3
import datetime

conn = sqlite3.connect('bot.db')
cursor = conn.cursor()
cursor.execute('''
                CREATE TABLE IF NOT EXISTS moderation (
                discord_id TEXT,
               reason TEXT,
               timestamp TEXT
               )
                ''')


async def warn_user(discord_id, reason):
    async with sqlite3.connect('bot.db').cursor() as cursor:
        await cursor.execute('''
                                INSERT INTO moderation VALUES(?,?,?)''', (discord_id,reason, datetime.now().strftime("%d-%m-%Y %H:%M:%S")))
        
        await sqlite3.connect('bot.db').commit()
        await sqlite3.connect('bot.db').close()

async def get_warnings(discord_id):
    async with sqlite3.connect('bot.db').cursor() as cursor:
        await cursor.execute('''
                                SELECT reason FROM moderation WHERE discord_id =?
                                ''', (discord_id))
        
        rows = cursor.fetchall()
        return [r[0] for r in rows]
        
        await sqlite3.connect('bot.db').commit()
        await sqlite3.connect('bot.db').close()