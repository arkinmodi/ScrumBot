## @file taskCog.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing commands related to tasks.
#  @date Mar 12, 2020

from discord.ext import commands

## @brief Discord commands related to the creation, removal and modification of meetings.
#  @details These commands are only to be used inside a guild.
class TaskCog(commands.Cog, name="Sprint Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="addFeedback", brief="Add feedback to a specific task.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_feedback(self, ctx, a: int, b: int, c: int, *s):
        raise NotImplementedError

    @commands.command(name="getDetails", brief="Get details of a specific task.")
    @commands.guild_only()
    async def get_details(self, ctx, a: int, b: int, k: int):
        raise NotImplementedError

    @commands.command(name="listFeedback", brief="List all feedback from a specific task.")
    @commands.guild_only()
    async def list_feedback(self, ctx, a: int, b: int, k: int):
        raise NotImplementedError

    @commands.command(name="rmFeedback", aliases=["removeFeedback"], brief="Remove a specific feedback from a specific task.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_feedback(self, ctx, a: int, b: int, c: int, d: int):
        raise NotImplementedError

    @commands.command(name="setDetails", brief="Set the details of a specific task.")
    @commands.guild_only()
    @commands.has_role(["Scrum Master", "Business Analyst"])
    async def set_details(self, ctx, a: int, b: int, *s):
        raise NotImplementedError

def setup(bot):
    bot.add_cog(TaskCog(bot))