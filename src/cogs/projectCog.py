## @file projectCog.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing commands related to projects.
#  @date Mar 12, 2020

import discord
from discord.ext import commands
import os, sys
sys.path.append("/mnt/c/Users/timch/Desktop/ScrumBot/src")

from project import *
from projectList import ProjectList

## @brief Discord commands related to the creation, removal and modification of projects.
#  @details These commands are only to be used inside a guild.
class projectCog(commands.Cog, name="Project Commands"):
    def __init__(self, bot):
        self.project_list = ProjectList()
        self.bot = bot
    
    @commands.command(name="addMeeting", brief="Add a meeting to a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_meeting(self, ctx, n: int, *s):
        raise NotImplementedError

    @commands.command(name="addProject", brief="Add a project to the guild.")
    @commands.guild_only()
    @commands.is_owner()
    async def add_project(self, ctx, name, *, desc: str=None):
        print(f'[Log] add_project from {ctx.author}, name: {name}, desc: {desc}')
        if (not desc):
            proj = Project(name)
        else:
            proj = Project(name, desc)
        self.project_list.add(proj)
        
        await ctx.send(f'> Added project **{name}**')

    @commands.command(name="addRqe", aliases=["addRequirement", "addReq"], brief="Add a requirement to a project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def add_rqe(self, ctx, a: int, *s):
        raise NotImplementedError

    @commands.command(name="addSprint", brief="Add a sprint to a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_sprint(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="getProjectDesc", aliases=["getProjectDescription", "getProjDesc"], brief="Get the description of a project.")
    @commands.guild_only()
    async def get_project_desc(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="getRqes", aliases=["getRequirements", "getReqs"], brief="Get the requirements of a project.")
    @commands.guild_only()
    async def get_rqes(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="getSprints", brief="Get the sprints of a project.")
    @commands.guild_only()
    async def get_sprints(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="listMeetings", brief="List all meetings of a project.")
    @commands.guild_only()
    async def list_meetings(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="listProjects", brief="List all projects in a guild.")
    @commands.guild_only()
    async def list_projects(self, ctx):
        lst = '\n'.join(self.project_list.to_seq())

        embed = discord.Embed(title='List of Projects')
        embed.add_field(name='\uFEFF', value=lst)

        await ctx.send(content=None, embed=embed)

    @commands.command(name="rmLastSprint", aliases=["removeLastSprint", "rmSprint", "removeSprint"], brief="Remove the last sprint of a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_last_sprint(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="rmMeeting", aliases=["removeMeeting"], brief="Removes a meeting from a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_meeting(self, ctx, a: int, b: int):
        raise NotImplementedError

    @commands.command(name="rmProject", aliases=["removeProject"], brief="Removes a project from the guild.")
    @commands.guild_only()
    @commands.is_owner()
    async def rm_project(self, ctx, n: int):
        raise NotImplementedError

    @commands.command(name="rmRqe", aliases=["removeRqe", "rmReq", "rmRequirement"], brief="Removes a requirement from a project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def rm_rqe(self, ctx, n: int, m: int):
        raise NotImplementedError

    @commands.command(name="setProjectDesc", aliases=["setProjectDescription"], brief="Set a description for a given project.")
    @commands.guild_only()
    @commands.has_role(["Business Analyst", "Admin"])
    async def set_project_desc(self, ctx, n: int, *s):
        raise NotImplementedError

def setup(bot):
    bot.add_cog(projectCog(bot))