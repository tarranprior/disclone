#! /usr/bin/env python3

import os, platform
from loguru import logger

import disnake
from disnake.ext import commands, tasks
from disnake import ApplicationCommandInteraction

from utils import *
from exceptions import *


class Bot(commands.InteractionBot):
    """
    A class which represents a Discord bot instance.
    """

    def __init__(self, config = None, *args, **kwargs) -> None:
        """
        Initialises a new instance of the Bot class.

        :param self: -
            Represents this object.
        :param config: (Optional[Dictionary]) -
            A dictionary containing configuration details.

        :return: (None)
        """

        super().__init__(*args, **kwargs)
        self.config = config or configuration()
        self.bot = Bot


    def load_extensions(self, exts: list) -> None:
        """
        Loads all extensions (cogs) for the bot.

        :param self: -
            Represents this object.
        :param exts: (List) -
            A list of file paths for the extensions.

        :return: (None)
        """

        count = 0
        for ext in exts:
            try:
                self.load_extension(ext)
                logger.success(f"Load ext: '{ext}' complete.")
                count += 1
            except Exception as e:
                exception = f'{type(e).__name__}: {e}'
                logger.error(f"Unable to load extension: {ext}\n{exception}.")

        logger.info(f"{count} extension(s) have loaded successfully.\n")


    async def on_connect(self) -> None:
        """
        A coroutine that is called when the bot has connected to
        the Discord gateway.

        :param self: -
            Represents this object.

        :return: (None)
        """

        logger.success("Disclone is connected to the gateway.")
        logger.info(f"Logged in as {self.user.name} ({self.user.id})")
        logger.info(f"API Version: {disnake.__version__}")
        logger.info(f"Platform: {platform.system()} {platform.release()} {os.name}\n")


    async def on_ready(self) -> None:
        """
        A coroutine that executes when the bot is fully initialised
        and ready to respond to events.

        :param self: -
            Represents this object.

        :return: (None)
        """

        logger.success("Disclone is ready.")
        logger.info("For more information on usage, see the README.")


    async def on_slash_command_error(
        self,
        inter: ApplicationCommandInteraction,
        error: Exception
    ) -> None:
        """
        A coroutine that is called when a slash command encounters
        an error.

        :param self: -
            Represents this object.
        :param inter: (ApplicationCommandInteraction) -
            The interaction that resulted in the error.
        :param error: (Exception) -
            The error that was raised.

        :return: (None)
        """

        if isinstance(error, commands.errors.CommandInvokeError):
            if "GcloneError" in str(error.__str__()):
                embed = EmbedFactory().create(
                    title="Gclone Error",
                    description=str("An error has occured during this operation."),
                    colour=disnake.Colour.red()
                )
                embed.add_field(
                    name="Error Message",
                    value=f"```{error.__cause__}```",
                    inline=False
                )
                return await inter.edit_original_message(embed=embed)

        logger.error(f"Ignoring exception in slash command {inter.application_command.name}: {error}")


    @tasks.loop(minutes=10.0)
    async def status() -> None:
        await Bot.change_presence(
            activity=disnake.Game(
                name=Bot.config["configuration"]["activity"]
            )
        )
