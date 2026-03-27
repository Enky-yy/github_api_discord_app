import sqlite3

conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        discord_id TEXT PRIMARY KEY,
        github_username TEXT
    )
    """)
conn.commit()


def link_user(discord_id, github_username):
    cursor.execute(
        "INSERT OR REPLACE INTO users VALUES (?, ?)",
            (discord_id, github_username)
    )
    conn.commit()


def get_linked_user(discord_id):
    cursor.execute(
        "SELECT github_username FROM users WHERE discord_id=?",
            (discord_id,)
    )
    result = cursor.fetchone()
    return result[0] if result else None