import os
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix=".")


# is_server_owner, makes certain commands only used by the server owner
def is_guild_owner(ctx):
    return ctx.guild.owner_id == ctx.author.id


# To tell if the bot has come online
@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))


@client.command()
@commands.check(is_guild_owner)
async def load(ctx, extension):
    """ Command: .load <cog>\n
        Load the selected cog extension"""
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"`{extension}` has been loaded.")


@client.command()
@commands.check(is_guild_owner)
async def unload(ctx, extension):
    """ Command: .reload <cog>\n
        Unload the selected cog extension"""
    client.unload_extension(f"cogs.{extension}")
    await ctx.send(f"`{extension}` has been unloaded.")


@client.command()
@commands.check(is_guild_owner)
async def reload(ctx, extension):
    """ Command: .reload <cog>\n
        Reload the selected cog extension"""
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
    await ctx.send(f"`{extension}` has been reloaded.")


# Load the cogs once the bot comes online
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f"cogs.{filename[:-3]}")


@client.command(aliases=['p'])
async def ping(ctx):
    """ Command: .ping\n
        Alt: `p`\n
        Show your ping"""

    await ctx.send(
        f"{ctx.author.mention} Pong! `{round(client.latency * 1000)}ms`")


# A command for deleting channel messages
@client.command()
@commands.check(is_guild_owner)
async def clear(ctx, amount=1):
    """Command: .clear <amount>\n
          Delete the amount of messages specified including the amount must includes the clear command it self"""
    await ctx.channel.purge(limit=amount)


keep_alive()
TOKEN = os.environ["TOKEN"]
client.run(TOKEN)
