import requests
import json
import os
from discord.ext import commands
from discord import Embed


# For a cog to work
class Urban_dictionary(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["ud"])
    async def urban_dictionary(self, ctx, *, term):
        """ Command: `.urban_dictionary <term>`\n
            Alt: `ud`\n
            Look up the meaning of a word on Urban Dictionary\n"""
        ud_json = get_ud(term)
        max_thumbs_up = 0
        for i in range(len(ud_json)):
          if ud_json[i]["thumbs_up"] > max_thumbs_up:
            ud_display = ud_json[i]
            max_thumbs_up = ud_json[i]["thumbs_up"]

        permalink = ud_display["permalink"]
        definition = (ud_display["definition"].replace('[',"**")).replace(']',"**")
        example = (ud_display["example"].replace('[',"**")).replace(']',"**")
        thumbs_up = str(ud_display["thumbs_up"]) + ":thumbsup:"
        author = ud_display["author"]

        # Embed the information into a message
        embed = Embed(title="Urban Dictionary: "+term.capitalize(), url=permalink, description=thumbs_up, color=0x1f1fe2)
        embed.set_thumbnail(url="https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse1.mm.bing.net%2Fth%3Fid%3DOIP.Yl8QBHEgN648bPyHoboAoAHaHa%26pid%3DApi&f=1")
        embed.set_author(name=author)
        embed.add_field(name="Definition", value=definition, inline=False)
        embed.add_field(name="Example", value=example, inline=False)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Urban_dictionary(client))


def get_ud(term):
    response = requests.get("https://dog.ceo/api/breeds/image/random")

    url = "https://mashape-community-urban-dictionary.p.rapidapi.com/define"

    querystring = {"term":"{search}".format(search=term)}

    headers = {
        'x-rapidapi-host': "mashape-community-urban-dictionary.p.rapidapi.com",
        'x-rapidapi-key': "{API_KEY}".format(API_KEY=UD_API_KEY)
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    json_data = json.loads(response.text)
    # print(json_data["list"])

    return json_data["list"]  # return the json list


UD_API_KEY = os.environ['UD_API_KEY']
