from discord.commands import slash_command
from discord.ext import commands
from main import logger


class Tools(commands.Cog, name="Tool commands"):
    """Misc tool commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(description='Returns the total round trip time to communicate with the bot!')
    async def ping(self, ctx: commands.Context):
        bot = self.bot
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        logger.info(
            f"User {UserNAME} requested /ping in {guildNAME}... saying 'Pong! {round (bot.latency * 1000)} ms' in channel {ctx.channel}")
        await ctx.respond(f'Pong! {round (bot.latency * 1000)} ms')


def setup(bot: commands.Bot):
    bot.add_cog(Tools(bot))
