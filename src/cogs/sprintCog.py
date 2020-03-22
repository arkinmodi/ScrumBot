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

    @commands.command(name="addTask", brief="Add a task to a sprint.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_task(self, ctx, a: int, b: int, *s):
        raise NotImplementedError

    @commands.command(name="listTasks", brief="List all tasks of a sprint.")
    @commands.guild_only()
    async def list_tasks(self, ctx, a: int, b: int):
        raise NotImplementedError

    @commands.command(name="rmTask", aliases=["removeTask"], brief="Removes a task in a sprint.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_task(self, ctx, a: int, b: int, c: int):
        raise NotImplementedError

def setup(bot):
    bot.add_cog(SprintCog(bot))