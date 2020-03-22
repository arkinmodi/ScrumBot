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

    @commands.command(name="getMeetingDesc", aliases=["getMeetingDescription"], brief="Get the description of a given meeting.")
    @commands.guild_only()
    async def get_meeting_desc(self, ctx, a: int, b: int):
        raise NotImplementedError

    @commands.command(name="setMeetingDesc", aliases=["setMeetingDescription"], brief="Set a meeting description.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def set_meeting_desc(self, ctx, a: int, b: int, *s):
        raise NotImplementedError

def setup(bot):
    bot.add_cog(MeetingCog(bot))