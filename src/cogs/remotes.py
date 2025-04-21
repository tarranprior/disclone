#! /usr/bin/env python3

from disnake.ext import commands
from disnake import ApplicationCommandInteraction

from templates.bot import Bot
from utils import *


class Remotes(commands.Cog, name="remotes"):
    """
    A class which represents a Discord cog instance.
    """

    def __init__(self, bot: Bot) -> None:
        """
        Initialises a new instance of the Remotes class.

        :param self: -
            Represents this object.
        :param bot: (Bot) -
            An instance of the Bot class.

        :return: (None)
        """

        self.bot = bot

    @commands.slash_command(
        name="remotes",
        description="List all the remotes in the 'rclone.conf' configuration file.",
    )
    async def remotes(self, inter: ApplicationCommandInteraction) -> None:
        """
        Creates a slash command for the `remotes` function.

        :param self: -
            Represents this object.
        :param inter: (ApplicationCommandInteraction) -
            Represents an interaction with an application command.

        :return: (None)
        """

        remotes = await rclone_remotes()

        description = (
            "List all the remotes in the `rclone.conf` configuration file.\n\n" +
            "```" +
            "Name                 | Status\n"
            "-------------------- | --------------------\n" +
            "\n".join(
                f"{line:<20} | 🟢 Default" if line == "gclone:" else f"{line:<20} |"
                for line in remotes.splitlines()
            ) +
            "```"
        )
        embed = EmbedFactory().create(
            title="Remotes",
            description=description
        )
        await inter.response.send_message(embed=embed)


def setup(bot) -> None:
    """
    Setup function for the `remotes` command.

    :param bot: (Bot) -
        An instance of the Bot class.

    :return: (None)
    """

    bot.add_cog(Remotes(bot))
