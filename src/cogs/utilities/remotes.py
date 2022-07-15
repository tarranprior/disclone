from disnake.ext import commands
from disnake.ext.commands import Context
from disnake import ApplicationCommandInteraction

from templates.bot import Bot
from utils import *


class Remotes(commands.Cog, name='remotes'):
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @commands.command(name="remotes", description="List all the remotes in the `rclone` configuration file.", aliases=["ls", "list", "listremotes"])
    async def remotes(self, ctx: Context) -> None:
        remotes = await rclone_remotes()
        embed = EmbedFactory().create(title="Remotes", description="List all the remotes in the `rclone` configuration file. To view more options for a particular remote, select an option in the dropdown or use `>config <remote>`.")
        embed.add_field(name="Remotes", value=f"```\n{remotes[1]}```", inline=True)
        embed.add_field(name="Configuration", value=f"```\n[+] new <remote>\n[+] config <remote>\n[+] del <remote>\n[+] copy <remote>\n[+] edit <remote>```", inline=True)
        await ctx.send(embed=embed)
    
    @commands.slash_command(name="remotes", description="List all the remotes in the `rclone` configuration file.", aliases=["ls", "list", "listremotes"])
    async def remotes_slash(self, inter: ApplicationCommandInteraction) -> None:
        remotes = await rclone_remotes()
        embed = EmbedFactory().create(title="Remotes", description="List all the remotes in the `rclone` configuration file. To view more options for a particular remote, select an option in the dropdown or use `>config <remote>`.")
        embed.add_field(name="Remotes", value=f"```\n{remotes[1]}```", inline=True)
        embed.add_field(name="Configuration", value=f"```\n[+] new <remote>\n[+] config <remote>\n[+] del <remote>\n[+] copy <remote>\n[+] edit <remote>```", inline=True)
        await inter.response.send_message(embed=embed)

def setup(bot) -> None:
    bot.add_cog(Remotes(bot))