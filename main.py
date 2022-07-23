import asyncio
from math import hypot
import discord
import os
from clogging import setup_logger
from clogging import logpath
from discord.ext import commands
import math
from dotenv import load_dotenv

load_dotenv()

prefix = os.getenv('PREFIX')
intents = discord.Intents.all()
logger = setup_logger('MAIN', logpath)
bot = discord.Bot(command_prefix='!', intents=intents)
client = discord.Client()


@bot.event
async def on_ready():  # Is called when the bot is ready to use.
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    logger.info(f"We have logged in as {bot.user}")
    logger.info('bot is ready!')
    await bot.change_presence(activity=discord.Game(name='Being worked on... ;)'))

# The old way of doing things, before slash commands were the new trend.


@bot.event
async def on_message(message): # Is called when a message is sent in a channel the bot is in.
    UserNAME = message.author.name
    NickNAME = message.author.nick
    if NickNAME:
        UserNAME = NickNAME
    if message.content.startswith(f'{prefix}hello'):
        logger.info(
            f'User {UserNAME} requested {prefix}hello... Saying ":wave: {UserNAME}" in channel {message.channel}')
        await message.channel.send(f'👋 {UserNAME}')

    await bot.process_application_commands(message)

# The new way of doing things, with slash commands. This is much cleaner to the user.


@bot.slash_command(guild=os.getenv('GUILD_ID'), description="Test command, just says 'Hello!'")
async def hello(ctx):
    UserNAME = ctx.author.name
    NickNAME = ctx.author.nick
    if ctx.user.nick:
        UserNAME = NickNAME
    logger.info(
        f'User {UserNAME} requested /hello... Saying "Hello!" in channel {ctx.channel}')
    await ctx.respond("Hello!")


@bot.slash_command(guild=os.getenv('GUILD_ID'), description='Adds two arguements that are passed to it!')
async def add(ctx, x: float, y: float):
    UserNAME = ctx.user.name
    NickNAME = ctx.user.nick
    if ctx.user.nick:
        UserNAME = NickNAME
    sumofargs = x + y
    logger.info(f"User {UserNAME} requested /add... {x} + {y} = {sumofargs}")
    await ctx.respond(f"{x} + {y} = {sumofargs}")


@bot.slash_command(guild=os.getenv('GUILD_ID'), description='Subtracts two arguements that are passed to it!')
async def subtract(ctx, x: float, y: float):
    UserNAME = ctx.user.name
    NickNAME = ctx.user.nick
    if ctx.user.nick:
        UserNAME = NickNAME
    differenceofargs = x - y
    logger.info(
        f"User {UserNAME} requested /subtract... {x} - {y} = {differenceofargs}")
    await ctx.respond(f"{x} - {y} = {differenceofargs}")


@bot.slash_command(guild=os.getenv('GUILD_ID'), description='Divides two arguements that are passed to it!')
async def divide(ctx, x: float, y: float):
    UserNAME = ctx.user.name
    NickNAME = ctx.user.nick
    if ctx.user.nick:
        UserNAME = NickNAME
    dividendofargs = x / y
    logger.info(
        f"User {UserNAME} requested /divide... {x} / {y} = {dividendofargs}")
    await ctx.respond(f"{x} / {y} = {dividendofargs}")


@bot.slash_command(guild=os.getenv('GUILD_ID'), description='Multiplies two arguements that are passed to it!')
async def multiply(ctx, x: float, y: float):
    UserNAME = ctx.user.name
    NickNAME = ctx.user.nick
    if ctx.user.nick:
        UserNAME = NickNAME
    productofargs = x * y
    logger.info(
        f"User {UserNAME} requested /multiply... {x} * {y} = {productofargs}")
    await ctx.respond(f"{x} * {y} = {productofargs}")


@bot.slash_command(guild=os.getenv('GUILD_ID'), description='Squares the arguement that is passed to it!')
async def squared(ctx, x: float):
    UserNAME = ctx.user.name
    NickNAME = ctx.user.nick
    if ctx.user.nick:
        UserNAME = NickNAME
    xsquared = x * x
    logger.info(f"User {UserNAME} requested /squared... {x}^2 = {xsquared}")
    await ctx.respond(f"{x}^2 = {xsquared}")


@bot.slash_command(guild=os.getenv('GUILD_ID'), description='Finds the squre root of the arguement that is passed to it!')
async def squareroot(ctx, x: float):
    UserNAME = ctx.user.name
    NickNAME = ctx.user.nick
    if ctx.user.nick:
        UserNAME = NickNAME
    squareroot = math.sqrt(x)
    logger.info(
        f"User {UserNAME} requested /squareroot... :squarerootsymbol:{x} = {squareroot}")
    await ctx.respond(f"√{x} = {squareroot}")


@bot.slash_command(guild=os.getenv('GUILD_ID'), description='Finds the hypotenuse of two arguements that are passed to it!')
async def pythagorean(ctx, x: float, y: float):
    UserNAME = ctx.user.name
    NickNAME = ctx.user.nick
    if ctx.user.nick:
        UserNAME = NickNAME
    hypotenuse = ((x * x) + (y * y))
    logger.info(
        f"User {UserNAME} requested /pythagorean... {x}^2 + {y}^2 = {math.sqrt(hypotenuse)}^2")
    await ctx.respond(f"{x}^2 + {y}^2 = {math.sqrt(hypotenuse)}^2")

# Gets the token from the environment variables.
bot.run(os.environ.get('TOKEN'))
