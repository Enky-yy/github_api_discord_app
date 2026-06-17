import aiohttp
from services.caching import get_cache, set_cache
from dotenv import load_dotenv
import os

load_dotenv()


GITHUB_TOKEN =  os.getenv("GITHUB_TOKEN")

HEADERS = {
    "Authorization" : "Bearer {}".format(GITHUB_TOKEN)

}

def process_data(data):
    user = data.get("data", {}).get("user")

    if not user:
        return None

    repos = user["repositories"]["nodes"]

    total_stars = sum(repo["stargazerCount"] for repo in repos)

    languages = {}
    for repo in repos:
        lang = repo.get("primaryLanguage")
        if lang:
            name = lang["name"]
            languages[name] = languages.get(name, 0) + 1

    top_language = max(languages, key=languages.get) if languages else "N/A"

    return {
        "name": user.get("name"),
        "login": user.get("login"),
        "avatar": user.get("avatarUrl"),
        "stars": total_stars,
        "followers": user["followers"]["totalCount"],
        "contributions": user["contributionsCollection"]["contributionCalendar"]["totalContributions"],
        "top_language": top_language
    }

GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"

async def fetch_graphql(query , variables=None):
    async with aiohttp.ClientSession() as session:
        async with session.post(
            GITHUB_GRAPHQL_URL,
            json={
                "query": query , "variables": variables
            },
            headers= HEADERS
        ) as resp:
            if resp.status != 200:
                raise Exception(f"GitHub API error: {resp.status}")

            return await resp.json()
        
async def get_user_stats(username):
    query = """
    query($login: String!) {
      user(login: $login) {
        name
        login
        avatarUrl
        repositories(first: 100, ownerAffiliations: OWNER) {
          nodes {
            stargazerCount
            primaryLanguage {
              name
            }
          }
        }
        contributionsCollection {
          contributionCalendar {
            totalContributions
          }
        }
        followers {
          totalCount
        }
      }
    }
    """
    cache_key = f"user:{username}"

    cached = get_cache(cache_key)
    if cached:
        return cached

    data = await fetch_graphql(query, {"login": username})
    result = process_data(data)

    if result is None:
        return None

    set_cache(cache_key, result)
    return result


async def get_top_repos(username):
    query = """
    query($login: String!) {
      user(login: $login) {
        repositories(first: 10, orderBy: {field: STARGAZERS, direction: DESC}) {
          nodes {
            name
            stargazerCount
            url
          }
        }
      }
    }
    """

    data = await fetch_graphql(query, {"login": username})
    user = data.get("data", {}).get("user")
    if not user:
        return []

    repos = user["repositories"]["nodes"]
    return repos

