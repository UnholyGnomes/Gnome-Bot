import asyncio
import discord
import os
from clogging import setup_logger
from clogging import logpath
from clogging import check_if_logger_exists
from discord.ext import tasks
from dotenv import load_dotenv
import random


# Load the .env file
load_dotenv()

# Check if the log file exists, if not, create it.
check_if_logger_exists()

# Load / define our variables.
prefix = os.getenv('PREFIX')
logger = setup_logger('MAIN', logpath)
intents = discord.Intents.all()
bot = discord.Bot(command_prefix=prefix, intents=intents)
client = discord.Client()

# Collect the guilds our bot is currently in.
listofids = []
for guild in bot.guilds:
    listofids.append(guild.id)

# Is called when the bot is loading up.


@bot.event
async def on_ready():
    logger.info(f"We have logged in as {bot.user}")
    logger.info('Bot is ready!')
    logger.info(f"This bot is active in {len(bot.guilds)} guild(s).")
    logger.info(f"- - - SERVER LIST - - -")
    for guild in bot.guilds:
        logger.info(f"Server {guild.id} : {guild.name}")
    await bot.change_presence(activity=discord.Game(name='Starting up... ;)'))
    randomstatus.start()

# Listen for new guilds and add them to our list of guilds.


@bot.event
async def on_guild_join(guild):
    listofids.append(guild.id)
    logger.info(f"Just joined guild {guild.id} : {guild.name}")
    logger.info(f"This bot is active in {len(bot.guilds)} guild(s).")

# Cycles through these statuses every 30 seconds.


@tasks.loop(seconds=30)
async def randomstatus():
    rng = random.randint(1, 4)
    logger.info(f"Changing status...")
    logger.info(f"Random status is {rng}")
    if rng == 1:
        logger.info(f'Setting status to "Playing Amogus? :amogusemoji:"')
        await bot.change_presence(activity=discord.Game(name="Amogus? ඞ"))
    if rng == 2:
        logger.info(f'Setting status to "Streaming "Not actually streaming""')
        await bot.change_presence(activity=discord.Streaming(name="Not actually streaming", url="https://www.twitch.tv/twitch"))
    if rng == 3:
        logger.info(f'Setting status to "Listening to Godzilla!"')
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Godzilla!"))
    if rng == 4:
        logger.info(
            f'Setting status to "Watching https://github.com/UnholyGnomes/Gnome-Bot/"')
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="https://github.com/UnholyGnomes/Gnome-Bot/"))

# Loads our cogs
for folder in os.listdir("cogs"):
    if os.path.exists(os.path.join("cogs", folder, "cog.py")):
        bot.load_extension(f"cogs.{folder}.cog")
        logger.info(f"Loaded {folder}")


# Gets the token from the environment variables.
bot.run(os.environ.get('TOKEN'))
