## @file misc.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief 
#  @date Mar 5, 2020

import discord
from discord.ext import commands

class MiscCog(commands.Cog, name="Miscellaneous"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        print(f'[Log] "ping" from {ctx.author}.')
        await ctx.send('pong')

    @commands.command()
    async def hello(self, ctx):
        print(f'[Log] "hello" from {ctx.author}.')
        await ctx.send(f'Hello {ctx.author.mention}!')

    @commands.command()
    async def say(self, ctx, *, msg=None):
        print(f'[Log] "say" {msg} from {ctx.author}.')
        await ctx.message.delete()
        await ctx.send(msg)

def setup(bot):
    bot.add_cog(MiscCog(bot))