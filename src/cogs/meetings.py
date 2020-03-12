## @file meetings.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing meeting commands.
#  @date Mar 10, 2020

from discord.ext import commands

## @brief Discord commands related to the creation, removal and modification of meetings.
#  @details These commands are only to be used inside a guild.
class MeetingCogs(commands.Cog, name="Meeting Commands"):
    def __init__(self, bot):
        self.bot = bot

    ## @brief Adds a meeting to a given project.
    @commands.command(name="addMeeting", brief="Create a meeting.")
    @commands.guild_only()
    async def add_meeting(self, ctx, *args):
        # TODO ADD MEETINGS
        return None

    ## @brief Removes a given meeting from the list of meetings.
    @commands.command(name="removeMeeting", brief="Remove a meeting")
    @commands.guild_only()
    async def rm_meeting(self, ctx, *args):
        # TODO REMOVE MEETINGS
        return None

def setup(bot):
    bot.add_cog(MeetingCogs(bot))