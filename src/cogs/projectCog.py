## @file projectCog.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing commands related to projects.
#  @date Mar 12, 2020

from discord.ext import commands

## @brief Discord commands related to the creation, removal and modification of projects.
#  @details These commands are only to be used inside a guild.
class projectCog(commands.Cog, name="Project commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="addProject", brief="Create a new project.")
    @commands.guild_only()
    async def add_project(self, ctx, *args):
        raise NotImplementedError

def setup(bot):
    bot.add_cog(projectCog(bot))