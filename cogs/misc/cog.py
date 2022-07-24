from discord.commands import slash_command
from discord.ext import commands
from clogging import logpath, setup_logger
from main import prefix
import requests
import json


logger = setup_logger('Misc', logpath)


class Misc(commands.Cog, name="Misc commands"):
    """Misc commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    # Is called when a message is sent in a channel the bot is in.
    async def on_message(self, message):
        bot = self.bot
        UserNAME = message.author.name
        NickNAME = message.author.nick
        guildNAME = message.guild.name
        if NickNAME:
            UserNAME = NickNAME
        if message.content.startswith(f'{prefix}hello'):
            logger.info(
                f'User {UserNAME} requested {prefix}hello in {guildNAME}... Saying ":wave: {UserNAME}" in channel {message.channel}')
            await message.channel.send(f'👋 {UserNAME}')

        await bot.process_application_commands(message)

    
    

    # The new way of doing things, with slash commands. This is much cleaner to the user.

    @slash_command(description="Test command, just says 'Hello!'")
    async def hello(self, ctx):
        UserNAME = ctx.author.name
        NickNAME = ctx.author.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        logger.info(
            f'User {UserNAME} requested /hello in {guildNAME}... Saying "Hello!" in channel {ctx.channel}')
        await ctx.respond("Hello!")

    @slash_command(description='Gives a random quote!')
    async def get_quote(self, ctx):
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        url = 'https://zenquotes.io/api/random'
        response = requests.get(url)
        json_data = json.loads(response.text)
        quote = json_data[0]['q'] + " -" + json_data[0]['a']
        logger.info(
            f"User {UserNAME} requested /quote in {guildNAME}... saying {quote} in channel {ctx.channel}")
        await ctx.respond(quote)


def setup(bot: commands.Bot):
    bot.add_cog(Misc(bot))
