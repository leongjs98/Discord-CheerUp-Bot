import requests
import json
import os
import random
from discord import Embed
from discord.ext import commands


class Cat(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["cats", "kitties", "kitty"])
    async def cat(self, ctx, random_breed=False):
        # random cats
        """ Command: `.cat <random_breed>`\n
            Alt: `cats` `kitties` `kitty`\n
            Function depends on the **random_breed**\n
            **random_breed**:\n
            If true/1, it will show a random breed of cat\n
            If left out, shows random images of cats\n"""
        json_cat = get_cat()
        image_link = json_cat[0]["url"]

        if random_breed:
            json_cat = random.choice(get_cat_breed())
            image_link = json_cat["image"]["url"]

            name = json_cat["name"]
            description = json_cat["description"]
            origin = json_cat["origin"]
            temperament = json_cat["temperament"]
            life_span = json_cat["life_span"] + " years"

            embed = Embed(title=name, description=description, color=0x5b453e)
            embed.set_thumbnail(url=image_link)
            embed.add_field(name="Origin", value=origin)
            embed.add_field(name="Life Span", value=life_span)
            embed.add_field(name="Temperament",
                            value=temperament,
                            inline=False)

            await ctx.send(embed=embed)
        else:
            await ctx.send(image_link)


def setup(client):
    client.add_cog(Cat(client))


# For all breeds
def get_cat_breed():
    headers = {'x-api-key': '{key}'.format(key=CAT_API_KEY)}

    response = requests.get(url="https://api.thecatapi.com/v1/breeds/",
                            headers=headers)

    json_data = json.loads(response.text)
    return json_data  # return the json


# For random cats images
def get_cat():
    response = requests.get(url="https://api.thecatapi.com/v1/images/search/")

    json_data = json.loads(response.text)
    return json_data  # return the json


CAT_API_KEY = os.environ['CAT_API_KEY']
