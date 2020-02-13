# bot.py
import os
import discord
from discord.ext import commands

from Meeting import *

token = '' # Currently removed for security reasons

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name='hello', help='Gives a warm greeting to the user who asked.')
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}!')

@bot.command(name='say', help='Make Scrumbot say something!', pass_context=True)
async def say(ctx, *, msg = None):
    print("log " + msg)
    await ctx.message.delete()
    await ctx.send(msg)

@bot.command(name='purge', help='Testing purposes, clears chat.', pass_context=True)
@commands.has_permissions(administrator=True)
async def purge(ctx, number: int):
    deleted = await ctx.channel.purge(limit=number)
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

    meeting = Meeting(date, time, meeting_type)
    await ctx.send(f'Added meeting on: {meeting.get_date_time()}')

bot.run(token)