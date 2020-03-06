## @file members.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief 
#  @date Mar 6, 2020

import discord
from discord.ext import commands

class MembersCog(commands.Cog, name="Member Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='role', aliases=['perms', 'role_for'])
    @commands.guild_only()
    async def get_roles(self, ctx, *, member: discord.Member=None):
        if not member:
            member = ctx.author
            
        roles = '\n'.join([role.name for role in member.roles if role.name != '@everyone'])
        
        embed = discord.Embed(title='Roles for:', description=member.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        embed.add_field(name='\uFEFF', value=roles)

        await ctx.send(content=None, embed=embed)


def setup(bot):
    bot.add_cog(MembersCog(bot))