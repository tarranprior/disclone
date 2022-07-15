from disnake.ext import commands
from disnake.ext.commands import Context
from disnake import ApplicationCommandInteraction, Option, OptionType

from config import *
from templates.bot import Bot
from utils import *


class Copy(commands.Cog, name='copy'):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(name="copy", description="Copy files from source to destination (server-side), skipping identical files.", aliases=["clone"])
    async def copy(self, ctx: Context, source: str, destination: str = None) -> None:
        embed = EmbedFactory().create(title="Clone Operation", description="Clone operation in progress...")
        await ctx.send(embed=embed)
        output = await gclone_copy(source, destination)
        embed = EmbedFactory().create(title="Clone Operation Complete", description=f"Hey {ctx.author.mention}! This operation is complete and your files are ready.")
        return await ctx.send(embed=embed)

    @commands.slash_command(name="copy", description="Copy files from source to destination (server-side), skipping identical files.", options=[
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
    async def copy_slash(self, inter: ApplicationCommandInteraction, source: str, destination: str = None) -> None:
        embed = EmbedFactory().create(title="Clone Operation", description="Clone operation in progress...")
        await inter.response.send_message(embed=embed)
        if not destination:
            destination = "{" + DEFAULT_DESTINATION + "}"
        output = await gclone_copy(source, destination)
        embed = EmbedFactory().create(title="Clone Operation Complete", description=f"Hey {inter.author.mention}! This operation is complete and your files are ready.")
        return await inter.followup.send(embed=embed)

def setup(bot) -> None:
    bot.add_cog(Copy(bot))