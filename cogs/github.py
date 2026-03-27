import discord
from discord.ext import commands
from discord import app_commands
import os
from services.database import link_user , get_linked_user
from typing import Optional

from services.github_api import get_user_stats, get_top_repos, fetch_graphql
from utils.embeds import github_embed
from utils.heatmap import generate_heatmap



HEATMAP_QUERY = """
query($login: String!) {
  user(login: $login) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays {
            contributionCount
          }
        }
      }
    }
  }
}
"""


class githubCog(commands.Cog):
    def __int__(self, bot):
        self.bot =bot

    @app_commands.command(name="github", description="Get Github Stats")
    async def github(self , interaction : discord.Interaction, username :Optional[str]):
        await interaction.response.defer()

        if not username:
            username = get_linked_user(str(interaction.user.id))

        try:
            data = await get_user_stats(username)
            embed = github_embed(data)
            await interaction.followup.send(embed=embed)
        except Exception:
            await interaction.followup.send("User not found or error ❌")

    @app_commands.command(name="repos", description="Top GitHub repositories")
    async def repos(self, interaction: discord.Interaction, username: Optional[str] = None):
        await interaction.response.defer()

        if not username:
            username = get_linked_user(str(interaction.user.id))

        repos = await get_top_repos(username)

        embed = discord.Embed(title=f"Top Repos - {username}", color=0x00ff00)

        for repo in repos[:5]:
            embed.add_field(
            name=f"{repo['name']} ⭐ {repo['stargazerCount']}",
            value=repo["url"],
            inline=False
            )

        await interaction.followup.send(embed=embed)

    @app_commands.command(name="heatmap", description="GitHub contribution heatmap")
    async def heatmap(self, interaction: discord.Interaction, username: Optional[str]):
        await interaction.response.defer()

        if not username:
            username = get_linked_user(str(interaction.user.id))

        try:
            data = await fetch_graphql(HEATMAP_QUERY, {"login": username})

            user = data.get("data", {}).get("user")
            if not user:
                await interaction.followup.send("User not found ❌")
                return

            weeks = data["data"]["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]

            file_path = generate_heatmap(weeks, filename=f"{username}_heatmap.png")

            await interaction.followup.send(file=discord.File(file_path))

            os.remove(file_path)

        except Exception as e:
            await interaction.followup.send("Error generating heatmap ❌")
            print(e)

    @app_commands.command(name="link", description="Link your GitHub account")
    async def link(self, interaction: discord.Interaction, username: str):

        link_user(str(interaction.user.id), username)
        await interaction.response.send_message(f"Linked to {username} ✅")

async def setup(bot):
    await bot.add_cog(githubCog(bot))