from discord.ext import commands
import random


# For a cog to work
class _8ball(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["8ball", "8b"])
    async def _8ball(self, ctx, question):
        """ Command: `._8ball <question>`\n
            Shorthand: `8b` `8ball`\n
            Answer your question with a magic 8 ball"""
        await ctx.send(f"{ctx.author.mention} {random.choice(responses)}")


def setup(client):
    client.add_cog(_8ball(client))


# Random responses
responses = [
    "It is certain.", 
    "It is decidedly so.", 
    "Without a doubt.",
    "Yes - definitely.", 
    "You may rely on it.", 
    "As I see it, yes.",
    "Most likely.", 
    "Outlook good.", 
    "Yes.", 
    "Signs point to yes.",
    "Reply hazy, try again.", 
    "Ask again later.", 
    "Better not tell you now.",
    "Cannot predict now.", 
    "Concentrate and ask again.", 
    "Don't count on it.",
    "Nope.", 
    "My sources say no.", 
    "Outlook not so good.",
    "Very doubtful."
]
