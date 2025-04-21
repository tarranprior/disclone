#! /usr/bin/env python3

from os import environ as env
from dotenv import load_dotenv

import disnake

from templates.bot import Bot
from utils.helpers import configuration

load_dotenv()

if __name__ == "__main__":

    bot = Bot(
        activity=disnake.Game(
            name=configuration()["configuration"]["activity"]
        ),
        intents=disnake.Intents.all(),
        owner_id=int(env["BOT_OWNER"])
    )

bot.load_extensions(exts=[
    "cogs.copy",
    "cogs.remotes"
])

bot.run(env["BOT_TOKEN"])
