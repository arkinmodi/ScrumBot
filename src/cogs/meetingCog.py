## @file meetingCog.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing commands related to meetings.
#  @date Mar 10, 2020

from discord.ext import commands

## @brief Discord commands related to the creation, removal and modification of meetings.
#  @details These commands are only to be used inside a guild.
class MeetingCog(commands.Cog, name="Meeting Commands"):
    def __init__(self, bot):
        self.bot = bot

    ## @brief Adds a meeting to a given project.
    @commands.command(name="addMeeting", brief="Create a meeting.")
    @commands.guild_only()
    async def add_meeting(self, ctx, *args):
        raise NotImplementedError

    ## @brief Removes a given meeting from the list of meetings.
    @commands.command(name="removeMeeting", brief="Remove a meeting.")
    @commands.guild_only()
    async def rm_meeting(self, ctx, *args):
        raise NotImplementedError

    @commands.command(name="listMeetings", brief="List all scheduled meetings.")
    @commands.guild_only()
    async def list_meetings(self, ctx):
        raise NotImplementedError

def setup(bot):
    bot.add_cog(MeetingCog(bot))