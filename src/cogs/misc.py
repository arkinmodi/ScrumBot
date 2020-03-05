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
        await ctx.send('pong')

def setup(bot):
    bot.add_cog(MiscCog(bot))