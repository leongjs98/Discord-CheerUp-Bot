import requests
import json
from discord.ext import commands


# For a cog to work
class Dog(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["doggo", "dogs"])
    async def dog(self, ctx):
        """ Command: `.dog <random_breed>`\n
            Alt: `dogs` `doggo`\n
            Show random images of dogs\n"""
        image_link = get_dog()
        await ctx.send(image_link)


def setup(client):
    client.add_cog(Dog(client))


def get_dog():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    json_data = json.loads(response.text)
    return json_data["message"]  # return the image link