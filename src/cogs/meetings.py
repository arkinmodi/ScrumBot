## @file meetings.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing meeting commands.
#  @date Mar 10, 2020

from discord.ext import commands

class MeetingCogs(commands.Cog, name="Meeting Commands"):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(MeetingCogs(bot))