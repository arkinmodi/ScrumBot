## @file members.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing commands suited for members of the guild.
#  @date Mar 6, 2020

import discord
from discord.ext import commands

## @brief Discord commands related to members of the guild.
#  @details These commands are only to be used inside a guild.
class Members(commands.Cog, name="Member Commands"):
    ## @brief Members constructor    
    def __init__(self, bot):
        self.bot = bot

    ## @brief Gets the list of roles of a specific member in a guild, or the person initiating the command if no parameter is given.
    @commands.command(name='role', aliases=['perms', 'role_for'], brief="Lists the roles of a user.")
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

## @brief The setup command for this cog.
#  @param bot The bot defined in bot.py.
def setup(bot):
    bot.add_cog(Members(bot))