#! /usr/bin/env python3

from disnake.ext import commands
from disnake import ApplicationCommandInteraction, Option, OptionType

from config import *
from templates.bot import Bot
from utils import *


class Copy(commands.Cog, name='copy'):
    """
    A class which represents a Discord cog instance.
    """

    def __init__(self, bot: Bot) -> None:
        """
        Initialises a new instance of the Copy class.

        :param self: -
            Represents this object.
        :param bot: (Bot) -
            An instance of the Bot class.

        :return: (None)
        """

        self.bot = bot

    @commands.slash_command(
        name="copy",
        description="Copy files from source to destination (server-side), "
                    "skipping identical files.",
        options=[
            Option(
                name="source",
                description='Specify the source directory.',
                type=OptionType.string,
                required=True
            ),
            Option(
                name="destination",
                description="Specify the destination directory.",
                type=OptionType.string,
                required=False
            ),
        ]
    )
    async def copy(
        self,
        inter: ApplicationCommandInteraction,
        source: str,
        destination: str = None
    ) -> None:
        """
        Creates a slash command for the `copy` function.

        :param self: -
            Represents this object.
        :param inter: (ApplicationCommandInteraction) -
            Represents an interaction with an application command.
        :param source: (String) -
            Represents a source remote/path.
        :param destination: (String) -
            Represents a destination remote/path.

        :return: (None)
        """
        if destination is None:
            destination = DEFAULT_DESTINATION

        embed = EmbedFactory().create(
            title="Remote Copy Initialising...",
            description=f"Copy files from source to destination (server-side), skipping identical files.\n\nInitialising...\n\n"
        )
        embed.set_footer(text="Initialising...")
        await inter.response.send_message(embed=embed)

        progress_lines = []
        async for line in gclone_copy_stream(source, destination):
            progress_lines.append(line)

            if len(progress_lines) % 5 == 0:
                output = "\n".join(progress_lines[-5:])
                embed.description = f"Copy files from source to destination (server-side), skipping identical files.\n\n```\n{output}\n```"
                embed.set_footer(text="In Progress...")
                await inter.edit_original_message(embed=embed)

        embed.title = "Remote Copy Complete"
        output = "\n".join(progress_lines[-5:])
        embed.description = f"Copy files from source to destination (server-side), skipping identical files.\n\n```\n{output}\n```"
        embed.set_footer(text="Complete")

        await inter.edit_original_message(embed=embed)
        await inter.followup.send(
            f"Hey, {inter.author.mention}! The remote copy has completed successfully!"
        )


def setup(bot) -> None:
    """
    Setup function for the `copy` command.

    :param bot: (Bot) -
        An instance of the Bot class.

    :return: (None)
    """

    bot.add_cog(Copy(bot))
