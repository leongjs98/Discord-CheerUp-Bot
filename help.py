from typing import Optional, Set
from discord.ext import commands
from discord import Embed


class HelpCog(commands.Cog, name='help'):
    def __init__(self, bot):
        self._original_help_command = bot.help_command
        bot.help_command = MyHelpCommand()
        bot.help_command.cog = self

    def cog_unload(self):
        self.bot.help_command = self._original_help_command


def setup(bot):
    bot.add_cog(HelpCog(bot))


class MyHelpCommand(commands.MinimalHelpCommand):
    def get_command_signature(self, command):
        return '{0.clean_prefix}{1.qualified_name} {1.signature}'.format(
            self, command)
        # return f"{self.context.clean_prefix}{command.qualified_name} {command.signature}"

    # description is an opitonal string
    async def _help_embed(self,
                          title,
                          description: Optional[str] = None,
                          mapping: Optional[dict] = None,
                          command_set: Optional[Set[commands.Command]] = None):
        embed = Embed(title=title)
        if description:
            embed.description = description
        if command_set:
            # show help about all commands in the set
            filtered = await self.filter_commands(command_set, sort=True)
            for command in filtered:
                embed.add_field(name=self.get_command_signature(command),
                                value=command.help,
                                inline=False)
        elif mapping:
            # add a short description of commands in each cog
            for cog, command_set in mapping.items():
                # So some functions are viewed and some are not by user
                filtered = await self.filter_commands(command_set, sort=True)
                if not filtered:  # If this is empty
                    continue
                # if some commands are not in the cog, error will arise, so the 'if' is necessary
                name = cog.qualified_name if cog else "No category"
                # \u2002 is an en-space
                cmd_list = "\u2002".join(
                    # Go through the list of commands that have been filtered and return the prefix and the name of the command
                    f"`{self.clean_prefix}{cmd.name}`" for cmd in filtered)
                # if the cog has a description, it will be included
                value = (
                    # Give command list if there's no description
                    # Or description and command list if there is a cog and a description for that cog
                    f"{cog.description}\n{cmd_list}"
                    if cog and cog.description else cmd_list)
                embed.add_field(name=name, value=value)

        return embed

    # Send help via a dictionary that sends the cogs and commands within each cog
    async def send_bot_help(self, mapping: dict):
        # Description is sent if we have one
        embed = await self._help_embed(
            title="Bot Commands",
            description="use .help command_name for more information",
            mapping=mapping)
        # get_destination gets where the channel to send msg in
        await self.get_destination().send(embed=embed)

# Send help about a specific command and say what that command will do

    async def send_command_help(self, command: commands.Command):
        embed = await self._help_embed(
            title=command.qualified_name,
            # command.help gives the description on how to use the command
            description=command.help,
            # only send a command set if the user is asking for a group help
            command_set=command.commands
            if isinstance(command, commands.Group) else None)
        await self.get_destination().send(embed=embed)

# Group is just a subclass of command, can use the same function

    send_group_help = send_command_help

    # Sending help about commands in each cog, and each of the short description
    async def send_cog_help(self, cog: commands.Cog):
        embed = await self._help_embed(
            title=cog.qualified_name,
            # command.help gives the description on how to use the command
            description=cog.description,
            # only send a command set if the user is asking for a group help
            command_set=cog.get_commands())
        await self.get_destination().send(embed=embed)
