# bot.py
import discord
from discord.ext import commands

from MeetingList import MeetingList
import settings

token = settings.TOKEN # Currently removed for security reasons

bot = commands.Bot(command_prefix='!')

MeetingList.init()

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello', help='Gives a warm greeting to the user who asked.')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command(name='say', help='Make Scrumbot say something!', pass_context=True)
async def say(ctx, *, msg = None):
    print(f'{ctx.author} log: ' + msg)
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command(name='purge', help='Testing purposes, clears chat.', pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, number: int):
    deleted = await ctx.channel.purge(limit=number)
    print(f'{ctx.author} purged {len(deleted)} messages.')
    await ctx.send(f'Deleted {len(deleted)} messages.')

@purge.error
async def purgeError(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have permissions.")

@bot.command(name='addMeeting', help='Adds a meeting in the form of: mm/dd/yyyy hh:mm meeting_type')
async def addMeeting(ctx, *args):
    print(args)
    date = args[0]
    time = args[1]
    meeting_type = ' '.join(args[2:])

    mID = MeetingList.add_meeting(date, time, meeting_type)
    datetime = MeetingList.get_meeting_datetime(mID)
    await ctx.send(f'Added meeting {mID} on: {datetime}')

@bot.command(name='listMeetings', help='Lists all added meetings')
async def listMeeting(ctx):
    list = MeetingList.list_meetings()
    for i in list:
        await ctx.send(f'{i}')

@bot.command(name='delMeeting', help='Deletes specified meeting given the meeting ID')
async def delMeeting(ctx, id: int):
    print(f'Deleting ID {id}')
    MeetingList.remove_meeting(id)
    await ctx.send(f'Deleted meeting {id}.')

# @bot.command(name='setDescription', help='Set the description of a meeting. Usage: !setDescription <meetingID> <description>')
# async def setDescription(ctx, *args):
#     print(f'Set description for {args}')
#     meeting = args[0]
#     description = ' '.join(args[1:])

bot.run(token)