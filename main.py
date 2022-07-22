import asyncio
import discord
import os
from clogging import setup_logger
from clogging import logpath
from discord.ext import commands
import random
import time
from dotenv import load_dotenv
load_dotenv()

prefix = os.getenv('PREFIX')
intents = discord.Intents.all()
logger = setup_logger('MAIN', logpath)
bot = discord.Bot(command_prefix='!', intents=intents)
client = discord.Client()


@bot.event
async def on_ready():  # Is called when the bot is ready to use
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    logger.info(f"We have logged in as {bot.user}")
    logger.info('bot is ready!')
    await bot.change_presence(activity=discord.Game(name='Being worked on... ;)'))


@bot.event
async def on_message(message):
    UserNAME = message.author.name
    if message.content.startswith(f'{prefix}hello'):
        logger.info(
            f'User {UserNAME} requested {prefix}hello... Saying 👋 {UserNAME} in channel {message.channel}')
        await message.channel.send(f'👋 {UserNAME}')

    await bot.process_application_commands(message)


@bot.slash_command(guild=os.getenv('GUILD_ID'), description="Test command, just says 'Hello!'")
async def hello(ctx):
    UserNAME = ctx.user.name
    logger.info(
        f'User {UserNAME} requested /hello... Saying Hello! in channel {ctx.channel}')
    await ctx.respond("Hello!")

# Gets the token from the environment variables
bot.run(os.environ.get('TOKEN'))
