## @file scrumbotCog.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing all commands related to projects.
#  @date Mar 12, 2020

import discord
from discord.ext import commands
import os, sys, inspect
currentDir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentDir = os.path.dirname(currentDir)
sys.path.insert(0, parentDir)

from project import *
from projectList import ProjectList

## @brief Discord commands related to scrumbot
#  @details These commands are only to be used inside a guild.
class scrumbotCog(commands.Cog, name="Scrumbot Commands"):
    def __init__(self, bot):
        self.project_list = ProjectList()
        self.bot = bot
    
    # PROJECT COG 
    @commands.command(name="addMeeting", brief="Add a meeting to a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_meeting(self, ctx, project_id: int, name, date, time, meeting_type, *, description=None):
        print(f'[Log] add_meeting from {ctx.author}, name: {name}, date: {date}, time: {time}, desc: {description} in project: {project_id}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to add meeting: project not found.')
            return

        proj.add_meeting(name, date, time, meeting_type, description)        
        await ctx.send(f'> Added meeting **{name}** to {proj.get_name()}.')

    @commands.command(name="addProject", brief="Add a project to the guild.")
    @commands.guild_only()
    @commands.is_owner()
    async def add_project(self, ctx, name, *, description=None):
        print(f'[Log] add_project from {ctx.author}, name: {name}, desc: {description}')
        proj = Project(name, description)
        self.project_list.add(proj)

        await ctx.send(f'> Added project **{name}**')

    @commands.command(name="addRqe", aliases=["addRequirement", "addReq"], brief="Add a requirement to a project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def add_rqe(self, ctx, project_id: int, *, requirement):
        print(f'[Log] add_rqe from {ctx.author}, project: {n}, rqe: {requirement}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to add requirement: project not found.')
            return

        proj.add_rqe(requirement)
        await ctx.send(f'> Added requirement to {proj.get_name()}.')

    @commands.command(name="addSprint", brief="Add a sprint to a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_sprint(self, ctx, project_id: int):
        print(f'[Log] add_sprint from {ctx.author}, project: {project_id}')

        proj = self.__get_project(project_id)                
        if (not proj):
            await ctx.send(f'> Failed to add sprint: project not found.')
            return

        proj.add_sprint()
        await ctx.send(f'> Added a new sprint to {proj.get_name()}.')

    @commands.command(name="getProjectDesc", aliases=["getProjectDescription", "getProjDesc"], brief="Get the description of a project.")
    @commands.guild_only()
    async def get_project_desc(self, ctx, project_id: int):
        print(f'[Log] get_project_desc from {ctx.author}, project: {project_id}')

        proj = self.__get_project(project_id)                
        if (not proj):
            await ctx.send(f'> Failed to get project description: project not found.')
            return

        desc = f'Project Name: {proj.get_name()}\nDescription: {proj.get_desc()}'

        embed = discord.Embed(title='Project Description')
        embed.add_field(name='\uFEFF', value=f'Description: {desc}')
        await ctx.send(content=None, embed=embed)

    @commands.command(name="getRqes", aliases=["getRequirements", "getReqs"], brief="Get the requirements of a project.")
    @commands.guild_only()
    async def get_rqes(self, ctx, project_id: int):
        print(f'[Log] get_rqes from {ctx.author}, project: {project_id}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to get project requirements: project not found.')
            return

        if (not proj.get_rqes()):
            await ctx.send(f' No current requirements in {proj.get_name()}.')
            return
        
        rqe_lst = [f'{i}. {proj.get_rqes()[i]}' for i in range(len(proj.get_rqes()))]
        lst = '\n'.join(rqe_lst)

        embed = discord.Embed(title=f'List of Requirements', description=f'{proj.get_name()}:')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="getSprints", aliases=["listSprints"], brief="Get the sprints of a project.")
    @commands.guild_only()
    async def get_sprints(self, ctx, project_id: int):
        print(f'[Log] get_sprints from {ctx.author}, project: {project_id}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to get project sprints: project not found.')
            return
            
        if (not proj.get_sprints()):
            await ctx.send(f'> No current sprints in {proj.get_name()}.')
            return

        sprint_lst = [f'Sprint {i} - Created on: {sprint_lst[i]}' for i in range(len(sprint_lst))]
        lst = '\n'.join(sprint_lst)

        embed = discord.Embed(title=f'List of Sprints', description=f'{proj.get_name()}:')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="listMeetings", brief="List all meetings of a project.")
    @commands.guild_only()
    async def list_meetings(self, ctx, project_id: int):
        print(f'[Log] list_meetings from {ctx.author}, project: {project_id}')

        proj = self.__get_project(project_id)                
        if (not proj):
            await ctx.send(f'> Failed to list meetings: project not found.')
            return

        seq = [f'id: {index} - name: {i[0]}, on {i[1]}. Meeting type: {i[2]}' for index, i in enumerate(proj.get_meetings())]

        if (not seq):
            await ctx.send(f'> No current projects in {proj.get_name()}.')
            return
        
        lst = '\n'.join(seq)

        embed = discord.Embed(title='List of Meetings', description=f'{proj.get_name()}')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="listProjects", aliases=["listProject"], brief="List all projects in a guild.")
    @commands.guild_only()
    async def list_projects(self, ctx):
        print(f'[Log] list_projects from {ctx.author}')
        
        seq = [f'id: {i} - name: {j.get_name()} - desc: {j.get_desc()}' for i, j in self.project_list.to_seq()]
        if (not seq):
            await ctx.send(f'> No current projects.')
            return

        lst = '\n'.join(seq)

        embed = discord.Embed(title='List of Projects')
        embed.add_field(name='\uFEFF', value=lst)

        await ctx.send(content=None, embed=embed)

    @commands.command(name="rmLastSprint", aliases=["removeLastSprint", "rmSprint", "removeSprint"], brief="Remove the last sprint of a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_last_sprint(self, ctx, project_id: int):
        print(f'[Log] rm_last_sprint from {ctx.author}, project: {project_id}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to remove last sprint: project not found.')
            return

        try:
            proj.rm_sprint()
        except IndexError as e:
            print(f'[Error] rm_last_sprint raised IndexError')
            await ctx.send(f'> Sprint list is empty! Cannot remove last sprint.')
            return
        
        await ctx.send(f'> Removed last sprint from {proj.get_name()}.')


    @commands.command(name="rmMeeting", aliases=["removeMeeting"], brief="Removes a meeting from a project.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_meeting(self, ctx, project_id: int, meeting_id: int):
        print(f'[Log] rm_meeting from {ctx.author}, project: {project_id}, meeting: {meeting_id}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to remove meeting: project not found.')
            return
            
        try:    
            proj.rm_meeting(meeting_id)
        except KeyError as e:
            await ctx.send(f'> Failed to remove meeting: meeting not found.')
            return
        
        await ctx.send(f'> Removed meeting {meeting_id} from {proj.get_name()}.')

    @commands.command(name="rmProject", aliases=["removeProject"], brief="Removes a project from the guild.")
    @commands.guild_only()
    @commands.is_owner()
    async def rm_project(self, ctx, project_id: int):
        print(f'[Log] rm_project from {ctx.author}, project: {project_id}')

        try:
            self.project_list.remove(project_id)
        except KeyError as e:
            await ctx.send(f'> Failed to remove project: project not found.')
            return

        await ctx.send(f'> Removed project {project_id}.')

    @commands.command(name="rmRqe", aliases=["removeRqe", "rmReq", "rmRequirement"], brief="Removes a requirement from a project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def rm_rqe(self, ctx, project_id: int, rqe_id: int):
        print(f'[Log] rm_rqe from {ctx.author}, project: {project_id}, rqe: {rqe_id}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to remove requirement: project not found.')
            return
        
        if (rqe_id < 0 or rqe_id > len(proj.get_rqes())):
            await ctx.send(f'> Failed to remove requirement: requirement not found.')
            return
            
        proj.rm_rqe(rqe_id)

        await ctx.send(f'> Removed requirement from {proj.get_name()}.')


    @commands.command(name="setProjectDesc", aliases=["setProjectDescription"], brief="Set a description for a given project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def set_project_desc(self, ctx, project_id: int, *, description):
        print(f'[Log] set_project_desc from {ctx.author}, project: {project_id}, desc: {description}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to set project description: project not found.')
            return
                       
        proj.set_desc(description)

        await ctx.send(f'> Successfully updated description for {proj.get_name()}.')

    # MEETING COG
    @commands.command(name="getMeetingDesc", aliases=["getMeetingDescription"], brief="Get the description of a given meeting.")
    @commands.guild_only()
    async def get_meeting_desc(self, ctx, n: int, m: int):
        print(f'[Log] get_meeting_desc from {ctx.author}, project: {n}, meeting: {m}')
        proj = self.__get_project(n)
        meeting = self.__get_meeting(n, m)        
        if (not meeting):
            return
        
        lst = f'Project Name: {proj.get_name()}\nMeeting Name: {meeting.get_name()}\nDescription: {meeting.get_desc()}'
        print(lst)
        embed = discord.Embed(title='Meeting Description')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="setMeetingDesc", aliases=["setMeetingDescription"], brief="Set a meeting description.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def set_meeting_desc(self, ctx, n: int, m: int, *, s):
        print(f'[Log] set_meeting_desc from {ctx.author}, project: {n}, meeting: {m}, desc: {s}')
        proj = self.__get_project(n)
        meeting = self.__get_meeting(n, m)
        if (not meeting):
            return
        
        meeting.set_desc(s)
        proj.update_meeting(m, meeting)
        await ctx.send(f'> Successfully updated description for {meeting.get_name()}.')

    # SPRINT COG
    @commands.command(name="addTask", brief="Add a task to a sprint.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_task(self, ctx, n: int, name, date, time, *, s=None):
        print(f'[Log] add_task from {ctx.author}, project: {n}, name: {name}, date: {date}, time: {time}, detail: {s}')
        date_val = [int(i) for i in date.split('/')]
        time_val = [int(i) for i in time.split(':')]

        datetime = dt.datetime(date_val[0], date_val[1], date_val[2], time_val[0], time_val[1])
        proj = self.__get_project(n)
        if (not proj or len(proj.get_sprints()) <= 0):
            return

        task = Task(name, datetime, s)
        sprint = proj.get_sprints()[-1]
        sprint.add_task(task)

        await ctx.send(f'> Added {name} to {proj.get_name()}.')
        
    @commands.command(name="listTasks", brief="List all tasks of a sprint.")
    @commands.guild_only()
    async def list_tasks(self, ctx, n: int, m: int):
        print(f'[Log] list_tasks from {ctx.author}, project: {n}, sprint: {m}')
        proj = self.__get_project(n)
        if (not proj or len(proj.get_sprints()) <= 0):
            return
        sprint = proj.get_sprints()[m]

        seq = [f'id: {i} - name: {j.get_name()}, due: {j.get_deadline()}' for i, j in sprint.get_tasks()]
        lst = '\n'.join(seq)

        if (not seq):
            await ctx.send(f'> No current tasks in given sprint.')
            return
        
        embed = discord.Embed(title='List of Tasks', description=f'{proj.get_name()}, sprint {m}')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="rmTask", aliases=["removeTask"], brief="Removes a task in a sprint.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_task(self, ctx, n: int, k: int):
        print(f'[Log] rm_task from {ctx.author}, project: {n}, task: {k}')
        proj = self.__get_project(n)
        if (not proj):
            return
        
        sprint = proj.get_sprints()[-1]
        sprint.rm_task(k)
        await ctx.send(f'> Removed task {k} in {proj.get_name()}.')

    # TASK COG
    @commands.command(name="addFeedback", brief="Add feedback to a specific task.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_feedback(self, ctx, n: int, k: int, *, s):
        print(f'[Log] add_feedback from {ctx.author}, project: {n}, task: {k}, feedback: {s}')
        proj = self.__get_project(n)
        if (not proj):
            return

        sprint = proj.get_sprints()[-1]
        task = self.__get_task(sprint, k)
        if (not task):
            return
        
        task.add_feedback(s)
        sprint.update_task(k, task)
        await ctx.send(f'> Added feedback to {task.get_name()}.')

    @commands.command(name="getDetails", brief="Get details of a specific task.")
    @commands.guild_only()
    async def get_details(self, ctx, n: int, m: int, k: int):
        print(f'[Log] get_details from {ctx.author}, project: {n}, sprint: {m}, task: {k}')
        proj = self.__get_project(n)
        if (not proj):
            return
        sprint = proj.get_sprints()[m]
        task = self.__get_task(sprint, k)
        if (not task):
            return
        
        details = f'Task Name: {task.get_name()}\nDetails: {task.get_details()}'

        embed = discord.Embed(title='Task Details', description=f'{proj.get_name()}, sprint {m}')
        embed.add_field(name='\uFEFF', value=details)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="listFeedback", brief="List all feedback from a specific task.")
    @commands.guild_only()
    async def list_feedback(self, ctx, n: int, m: int, k: int):
        print(f'[Log] list_feedback from {ctx.author}, project: {n}, sprint: {m}, task: {k}')
        proj = self.__get_project(n)
        if (not proj):
            return
        
        sprint = proj.get_sprints()[m]
        task = self.__get_task(sprint, k)
        if (not task):
            return
        
        seq = [f'{i}. {task.get_feedback()[i]}' for i in range(len(task.get_feedback()))]
        lst = '\n'.join(seq)

        if (not seq):
            await ctx.send(f'> No current feedback in {task.get_name()}.')
            return
        
        embed = discord.Embed(title='List of Feedback', description=f'{proj.get_name()}, sprint {m}, {task.get_name()}')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="rmFeedback", aliases=["removeFeedback"], brief="Remove a specific feedback from a specific task.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_feedback(self, ctx, n: int, k: int, x: int):
        print(f'[Log] rm_feedback from {ctx.author}, project: {n}, task: {k}, feedback: {x}')
        proj = self.__get_project(n)
        if (not proj):
            return

        sprint = proj.get_sprints()[-1]
        task = self.__get_task(sprint, k)
        if (not task):
            return
        
        task.rm_feedback(x)
        await ctx.send(f'> Removed feedback from {task.get_name()}.')

    @commands.command(name="setDetails", brief="Set the details of a specific task.")
    @commands.guild_only()
    @commands.has_role(["Scrum Master", "Business Analyst"])
    async def set_details(self, ctx, n: int, k: int, *, s):
        print(f'[Log] set_details from {ctx.author}, project: {n}, task: {k}, details: {s}')
        proj = self.__get_project(n)
        if (not proj):
            return
        sprint = proj.get_sprints()[-1]
        task = self.__get_task(sprint, k)
        if (not task):
            return
        
        task.set_details(s)
        await ctx.send(f'> Added details to {task.get_name()}.')

    # ADMIN COG
    ## @brief Loads a new cog into the bot.
    #  @param cog A string having the name of the python file, usually in the form of 'cogs.<file_name>'.
    #  @throws Exception if the extension fails to load.
    @commands.command(name='load')
    @commands.is_owner()
    async def load(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(cog)
        except Exception as e:
            print(f'[Log] Failed to load {cog}')
            await ctx.send(f'> Error: failed to load **{cog}**')
            return
        print(f'[Log] Successfully loaded {cog}')
        await ctx.send(f'> **{cog}** loaded')

    ## @brief Reloads a cog in the bot.
    #  @param cog A string having the name of the python file, usually in the form of 'cogs.<file_name>'.g 
    #  @throws Exception if the extension fails to reload.
    @commands.command(name='reload')
    @commands.is_owner()
    async def reload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            print(f'[Log] Failed to reload {cog}')
            await ctx.send(f'> Error: failed to reload **{cog}**')
            return
        print(f'[Log] Successfully reloaded {cog}')
        await ctx.send(f'> **{cog}** reloaded')
    
    ## @brief Unloads a cog from the bot.
    #  @param cog A string having the name of the python file, usually in the form of 'cogs.<file_name>'.g 
    #  @throws Exception if the extension fails to unload.
    @commands.command(name='unload')
    @commands.is_owner()
    async def unload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            print(f'[Log] Failed to unload {cog}')
            await ctx.send(f'> Error: failed to unload **{cog}**')
            return
        print(f'[Log] Successfully unloaded {cog}')
        await ctx.send(f'> **{cog}** unloaded')

    # MEMBER COG
    ## @brief Gets the list of roles of a specific member in a guild, or the person initiating the command if no parameter is given.
    @commands.command(name='role', aliases=['perms', 'roleFor'], brief="Lists the roles of a user.")
    @commands.guild_only()
    async def get_roles(self, ctx, *, member: discord.Member=None):
        if not member:
            member = ctx.author

        print(f'[Log] get_role from {ctx.author} for {member}')
        roles = '\n'.join([role.name for role in member.roles if role.name != '@everyone'])
        
        embed = discord.Embed(title='Roles for:', description=member.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        embed.add_field(name='\uFEFF', value=roles)

        await ctx.send(content=None, embed=embed)

    def __get_project(self, n):
        proj_key = self.project_list.to_seq()
        for i in range(len(proj_key)):
            if (proj_key[i][0] == n):
                return proj_key[i][1]
        return None

    def __get_meeting(self, n, m):
        proj = self.__get_project(n)
        if (not proj):
            return None
        
        meet_key = proj.get_meetings()
        for i in range(len(meet_key)):
            if (meet_key[i][0] == m):
                return meet_key[i][1]
        return None

    def __get_task(self, sprint, k):
        task_key = sprint.get_tasks()
        for i in range(len(task_key)):
            if (task_key[i][0] == k):
                return task_key[i][1]
        return None

def setup(bot):
    bot.add_cog(scrumbotCog(bot))