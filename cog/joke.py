import json
import requests
from time import sleep
from discord.ext import commands


# For a cog to work
class Joke(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['j'])
    async def joke(self, ctx, category=None):
        """ Command: `.joke <category>`\n
            Alt: `j`\n
            Tells you a joke in the following categories:\n
            `Programming` `Dark` `Pun` `Spooky` `Chrristmas` `Safe`\n
            The joke will be random if the category is left out"""
        joke_json = get_joke_json(category)
        
        if joke_json["type"] == "single":
            await ctx.send(joke_json["joke"])

        # If it's a 2 part joke, send the first part, wait and send the second part
        else:
            await ctx.send(joke_json["setup"])
            sleep(3)
            await ctx.send(joke_json["delivery"])


def setup(client):
    client.add_cog(Joke(client))


def get_joke_json(category):
    # Call the API according to the requested category
    if category:
        url = f"https://v2.jokeapi.dev/joke/{category}"
    # Only call the safe jokes
    elif category == "safe" or category == "sfw":
        url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,political,racist,sexist,explicit"
    # Any jokes go
    else:
        url = "https://v2.jokeapi.dev/joke/Any"

    print(url+'\n')
    response = requests.get(url)

    # Must use response.text to convert them into full str
    json_data = json.loads(response.text)
    print(json_data)
    return json_data