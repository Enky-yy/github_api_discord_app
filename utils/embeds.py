import discord

def github_embed(data):
    embed = discord.Embed(
        title=f"{data['name']} (@{data['login']})",
        color=0x24292e
    )

    embed.set_thumbnail(url=data["avatar"])

    embed.add_field(name="⭐ Total Stars", value=data["stars"])
    embed.add_field(name="👥 Followers", value=data["followers"])
    embed.add_field(name="🔥 Contributions", value=data["contributions"])
    embed.add_field(name="💻 Top Language", value=data["top_language"])

    return embed