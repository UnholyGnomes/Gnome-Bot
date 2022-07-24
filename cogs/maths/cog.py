from discord.commands import slash_command
from discord.ext import commands
from main import logger
import math


class Maths(commands.Cog, name="Math commands"):
    """Misc math commands"""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @slash_command(description="Adds two arguements that are passed to it!")
    async def add(self, ctx: commands.Context, x: float, y: float):
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        sumofargs = x + y
        logger.info(
            f"User {UserNAME} requested /add in {guildNAME}... {x} + {y} = {sumofargs}")
        await ctx.respond(f"{x} + {y} = {sumofargs}")

    @slash_command(description='Subtracts two arguements that are passed to it!')
    async def subtract(self, ctx, x: float, y: float):
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        differenceofargs = x - y
        logger.info(
            f"User {UserNAME} requested /subtract in {guildNAME}... {x} - {y} = {differenceofargs}")
        await ctx.respond(f"{x} - {y} = {differenceofargs}")

    @slash_command(description='Divides two arguements that are passed to it!')
    async def divide(self, ctx, x: float, y: float):
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        dividendofargs = x / y
        logger.info(
            f"User {UserNAME} requested /divide in {guildNAME}... {x} / {y} = {dividendofargs}")
        await ctx.respond(f"{x} / {y} = {dividendofargs}")

    @slash_command(description='Multiplies two arguements that are passed to it!')
    async def multiply(self, ctx, x: float, y: float):
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        productofargs = x * y
        logger.info(
            f"User {UserNAME} requested /multiply in {guildNAME}... {x} * {y} = {productofargs}")
        await ctx.respond(f"{x} * {y} = {productofargs}")

    @slash_command(description='Squares the arguement that is passed to it!')
    async def squared(self, ctx, x: float):
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        xsquared = x * x
        logger.info(
            f"User {UserNAME} requested /squared in {guildNAME}... {x}^2 = {xsquared}")
        await ctx.respond(f"{x}^2 = {xsquared}")

    @slash_command(description='Finds the squre root of the arguement that is passed to it!')
    async def squareroot(self, ctx, x: float):
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        squareroot = math.sqrt(x)
        logger.info(
            f"User {UserNAME} requested /squareroot in {guildNAME}... :squarerootsymbol:{x} = {squareroot}")
        await ctx.respond(f"√{x} = {squareroot}")

    @slash_command(description='Finds the hypotenuse of two arguements that are passed to it!')
    async def pythagorean(self, ctx, x: float, y: float):
        UserNAME = ctx.user.name
        NickNAME = ctx.user.nick
        guildNAME = ctx.guild.name
        if ctx.user.nick:
            UserNAME = NickNAME
        hypotenuse = ((x * x) + (y * y))
        logger.info(
            f"User {UserNAME} requested /pythagorean in {guildNAME}... {x}^2 + {y}^2 = {math.sqrt(hypotenuse)}^2")
        await ctx.respond(f"{x}^2 + {y}^2 = {math.sqrt(hypotenuse)}^2")


def setup(bot: commands.Bot):
    bot.add_cog(Maths(bot))
