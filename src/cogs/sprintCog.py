## @file sprintCog.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing commands related to sprints.
#  @date Mar 12, 2020

from discord.ext import commands

## @brief Discord commands related to the creation, removal and modification of meetings.
#  @details These commands are only to be used inside a guild.
class SprintCog(commands.Cog, name="Sprint Commands"):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(SprintCog(bot))