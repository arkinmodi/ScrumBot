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

from fileio import *

## @brief Discord commands related to scrumbot
#  @details These commands are only to be used inside a guild.
class scrumbotCog(commands.Cog, name="Scrumbot Commands"):
    def __init__(self, bot):
        self.project_list = fileio.read()
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

        datetime = date + " " + time
        meeting_type = meeting_type.upper()
        try:
            proj.add_meeting(name, datetime, meeting_type, description) 
        except TypeError:
            await ctx.send(f'> Failed to add meeting: meeting type must be GROOMING, STANDUP, RETROSPECTIVE, or SPRINTPLANNING.')
            return

        info = f'{proj.get_last_meeting_id()},{name},{datetime},{meeting_type},{description}'
        fileio.write(self.project_list.get_last_id(), "addMeeting", info)

        await ctx.send(f'> Added meeting **{name}** to {proj.get_name()}.')

    @commands.command(name="addProject", brief="Add a project to the guild.")
    @commands.guild_only()
    @commands.has_role("Admin")
    async def add_project(self, ctx, name, *, description=None):
        print(f'[Log] add_project from {ctx.author}, name: {name}, desc: {description}')
        proj = Project(name, description)
        self.project_list.add(proj)

        fileio.create(self.project_list.get_last_id(), name, description)

        await ctx.send(f'> Added project **{name}**')

    @commands.command(name="addRqe", aliases=["addRequirement", "addReq"], brief="Add a requirement to a project.")
    @commands.guild_only()
    @commands.has_role("Business Analyst")
    async def add_rqe(self, ctx, project_id: int, *, requirement):
        print(f'[Log] add_rqe from {ctx.author}, project: {project_id}, rqe: {requirement}')

        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to add requirement: project not found.')
            return

        proj.add_rqe(requirement)
        fileio.write(self.project_list.get_last_id(), "addRqe", requirement)
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
        fileio.write(self.project_list.get_last_id(), "addSprint")
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
        
        sprint_lst = proj.get_sprints()
        sprints = [f'Sprint {i} - Created on: {sprint_lst[i]}' for i in range(len(sprint_lst))]
        lst = '\n'.join(sprints)

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

        seq = [f'id: {i} - name: {j[0]}, on {j[1]}. Meeting type: {j[2]}' for i, j in proj.get_meetings()]

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
        except IndexError:
            print(f'[Error] rm_last_sprint raised IndexError')
            await ctx.send(f'> Failed to remove last sprint: no sprints found in project.')
            return

        fileio.write(self.project_list.get_last_id(), "rmLastSprint")
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
        except KeyError:
            await ctx.send(f'> Failed to remove meeting: meeting not found.')
            return
        
        fileio.write(self.project_list.get_last_id(), "rmMeeting", meeting_id)
        await ctx.send(f'> Removed meeting {meeting_id} from {proj.get_name()}.')

    @commands.command(name="rmProject", aliases=["removeProject"], brief="Removes a project from the guild.")
    @commands.guild_only()
    @commands.has_role("Admin")
    async def rm_project(self, ctx, project_id: int):
        print(f'[Log] rm_project from {ctx.author}, project: {project_id}')

        try:
            self.project_list.remove(project_id)
        except KeyError:
            await ctx.send(f'> Failed to remove project: project not found.')
            return

        fileio.delete(self.project_list.get_last_id())
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

        try:
            proj.rm_rqe(rqe_id)
        except IndexError:
            await ctx.send(f'> Failed to remove requirement: requirement not found.')
            return            

        fileio.write(self.project_list.get_last_id(), "rmRqe", rqe_id)
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
        fileio.write(self.project_list.get_last_id(), "setProjectDesc", description)
        await ctx.send(f'> Successfully updated description for {proj.get_name()}.')

    # MEETING COG
    @commands.command(name="getMeetingDesc", aliases=["getMeetingDescription"], brief="Get the description of a given meeting.")
    @commands.guild_only()
    async def get_meeting_desc(self, ctx, project_id: int, meeting_id: int):
        print(f'[Log] get_meeting_desc from {ctx.author}, project: {project_id}, meeting: {meeting_id}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to get meeting description: project not found.')
            return
        
        try:
            lst = f'Project Name: {proj.get_name()}\nMeeting Name: {proj.get_meeting_name(meeting_id)}\nDescription: {proj.get_meeting_desc(meeting_id)}'
        except KeyError:
            await ctx.send(f'> Failed to get meeting description: meeting not found.')
            return

        embed = discord.Embed(title='Meeting Description')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="setMeetingDesc", aliases=["setMeetingDescription"], brief="Set a meeting description.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def set_meeting_desc(self, ctx, project_id: int, meeting_id: int, *, description):
        print(f'[Log] set_meeting_desc from {ctx.author}, project: {project_id}, meeting: {meeting_id}, desc: {description}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to set meeting description: project not found.')
            return

        try:
            proj.set_meeting_desc(meeting_id, description)
        except KeyError:
            await ctx.send(f'> Failed to set meeting description: meeting not found.')
            return
        
        fileio.write(self.project_list.get_last_id(), "setMeetingDesc", meeting_id, description)
        await ctx.send(f'> Successfully updated description for {proj.get_meeting_name(meeting_id)}.')

    # SPRINT COG
    @commands.command(name="addTask", brief="Add a task to a sprint.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_task(self, ctx, project_id: int, name, date, time, *, details=None):
        print(f'[Log] add_task from {ctx.author}, project: {project_id}, name: {name}, date: {date}, time: {time}, detail: {details}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to add task: project not found.')
            return

        deadline = date + " " + time
        try:
            proj.add_task(name, deadline, details)
        except IndexError:
            await ctx.send(f'> Failed to add task: project contains no sprints.')
            return

        fileio.write(self.project_list.get_last_id(), "addTask", proj.get_last_task_id(), name, deadline, details)
        await ctx.send(f'> Added {name} to {proj.get_name()}.')
        
    @commands.command(name="listTasks", brief="List all tasks of a sprint.")
    @commands.guild_only()
    async def list_tasks(self, ctx, project_id: int, sprint_id: int):
        print(f'[Log] list_tasks from {ctx.author}, project: {project_id}, sprint: {sprint_id}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to list tasks: project not found.')
            return

        if (len(proj.get_sprints()) == 0):
            await ctx.send(f'> Failed to list tasks: project contains no sprints.')
            return

        try:
            tasks = proj.get_tasks(sprint_id)
        except IndexError:
            await ctx.send(f'> Failed to list tasks: no such sprint id exists.')
            return

        seq = [f'id: {i} - name: {j[0]}, due: {j[1]}' for i, j in tasks]
        lst = '\n'.join(seq)

        if (not seq):
            await ctx.send(f'> No current tasks in given sprint.')
            return
        
        embed = discord.Embed(title='List of Tasks', description=f'{proj.get_name()}, sprint {sprint_id}')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="rmTask", aliases=["removeTask"], brief="Removes a task in a sprint.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_task(self, ctx, project_id: int, task_id: int):
        print(f'[Log] rm_task from {ctx.author}, project: {project_id}, task: {task_id}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to remove task: project not found.')
            return

        try:
            proj.rm_task(task_id)
        except IndexError:
            await ctx.send(f'> Failed to remove task: project contains no sprints.')
            return
        except KeyError:
            await ctx.send(f'> Failed to remove task: task not found.')
            return
            
        fileio.write(self.project_list.get_last_id(), "rmTask", task_id)
        await ctx.send(f'> Removed task {task_id} in {proj.get_name()}.')

    # TASK COG
    @commands.command(name="addFeedback", brief="Add feedback to a specific task.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def add_feedback(self, ctx, project_id: int, task_id: int, *, feedback):
        print(f'[Log] add_feedback from {ctx.author}, project: {project_id}, task: {task_id}, feedback: {feedback}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to add feedback: project not found.')
            return

        try:
            proj.add_feedback(task_id, feedback)
        except IndexError:
            await ctx.send(f'> Failed to add feedback: project contains no sprints.')
            return
        except KeyError:
            await ctx.send(f'> Failed to add feedback: task not found.')
            return

        fileio.write(self.project_list.get_last_id(), "addFeedback", task_id, feedback)
        await ctx.send(f'> Added feedback to task {task_id}.')

    @commands.command(name="getDetails", brief="Get details of a specific task.")
    @commands.guild_only()
    async def get_details(self, ctx, project_id: int, sprint_id: int, task_id: int):
        print(f'[Log] get_details from {ctx.author}, project: {project_id}, sprint: {sprint_id}, task: {task_id}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to get details: project not found.')
            return

        try:
            task = proj.get_task(sprint_id, task_id)
        except IndexError:
            await ctx.send(f'> Failed to get details: sprint not found.')
            return
        
        if (not task):
            await ctx.send(f'> Failed to get details: task not found.')
            return

        
        details = f'Task Name: {task[0]}\nDetails: {task[2]}'

        embed = discord.Embed(title='Task Details', description=f'{proj.get_name()}, sprint {sprint_id}')
        embed.add_field(name='\uFEFF', value=details)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="listFeedback", brief="List all feedback from a specific task.")
    @commands.guild_only()
    async def list_feedback(self, ctx, project_id: int, sprint_id: int, task_id: int):
        print(f'[Log] list_feedback from {ctx.author}, project: {project_id}, sprint: {sprint_id}, task: {task_id}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to list feedback: project not found.')
            return

        try:
            feedback = proj.get_feedback(sprint_id, task_id)
        except IndexError:
            await ctx.send(f'> Failed to list feedback: sprint not found.')
            return
        except KeyError:
            await ctx.send(f'> Failed to list feedback: task not found.')
            return
        
        print(feedback)
        seq = [f'{i}. {feedback[i]}' for i in range(len(feedback))]
        lst = '\n'.join(seq)

        if (not seq):
            await ctx.send(f'> No current feedback in task {task_id}.')
            return
        
        embed = discord.Embed(title='List of Feedback', description=f'{proj.get_name()}, sprint {sprint_id}, task {task_id}')
        embed.add_field(name='\uFEFF', value=lst)
        await ctx.send(content=None, embed=embed)

    @commands.command(name="rmFeedback", aliases=["removeFeedback"], brief="Remove a specific feedback from a specific task.")
    @commands.guild_only()
    @commands.has_role("Scrum Master")
    async def rm_feedback(self, ctx, project_id: int, task_id: int, feedback_id: int):
        print(f'[Log] rm_feedback from {ctx.author}, project: {project_id}, task: {task_id}, feedback: {feedback_id}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to remove feedback: project not found.')
            return

        try:
            proj.rm_feedback(task_id, feedback_id)
        except IndexError:
            await ctx.send(f'> Failed to remove feedback: project contains no sprints.')
            return
        except KeyError:
            await ctx.send(f'> Failed to remove feedback: task not found.')
            return

        fileio.write(self.project_list.get_last_id(), "rmFeedback", task_id, feedback_id)
        await ctx.send(f'> Removed feedback from task {task_id}.')

    @commands.command(name="setDetails", brief="Set the details of a specific task.")
    @commands.guild_only()
    @commands.has_any_role("Scrum Master", "Business Analyst")
    async def set_details(self, ctx, project_id: int, task_id: int, *, details):
        print(f'[Log] set_details from {ctx.author}, project: {project_id}, task: {task_id}, details: {details}')
        proj = self.__get_project(project_id)
        if (not proj):
            await ctx.send(f'> Failed to set details: project not found.')
            return
        
        try:
            proj.set_details(task_id, details)
        except IndexError:
            await ctx.send(f'> Failed to set details: project contains no sprints.')
            return
        except KeyError:
            await ctx.send(f'> Failed to set details: task not found.')
            return

        fileio.write(self.project_list.get_last_id(), "setDetails", task_id, details)
        await ctx.send(f'> Set details for task {task_id}.')

    # ADMIN COG
    ## @brief Loads a new cog into the bot.
    #  @param cog A string having the name of the python file, usually in the form of 'cogs.<file_name>'.
    #  @throws Exception if the extension fails to load.
    @commands.command(name='load')
    @commands.has_role("Admin")
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
    @commands.has_role("Admin")
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
    @commands.has_role("Admin")
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

def setup(bot):
    bot.add_cog(scrumbotCog(bot))