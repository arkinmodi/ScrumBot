## @file misc.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing miscellaneous commands that don't relate to any category.
#  @date Mar 5, 2020

import discord
from discord.ext import commands

## @brief Miscellaneous Discord commands.
class MiscCog(commands.Cog, name="Miscellaneous"):
    ## @brief MiscCog constructor
    def __init__(self, bot):
        self.bot = bot

    ## @brief Pings the bot to send a pong back.
    #  @details Used to test the latency of the bot.
    @commands.command()
    async def ping(self, ctx):
        print(f'[Log] "ping" from {ctx.author}.')
        await ctx.send('pong')

    ## @brief Say hello to ScrumBot.
    @commands.command()
    async def hello(self, ctx):
        print(f'[Log] "hello" from {ctx.author}.')
        await ctx.send(f'Hello {ctx.author.mention}!')

    ## @brief Make ScrumBot say something.
    #  @details ScrumBot will delete the original message and replace it with its own message.
    @commands.command()
    async def say(self, ctx, *, msg=None):
        print(f'[Log] "say" {msg} from {ctx.author}.')
        await ctx.message.delete()
        await ctx.send(msg)

## @brief The setup command for this cog.
#  @param bot The bot defined in bot.py.
def setup(bot):
    bot.add_cog(MiscCog(bot))