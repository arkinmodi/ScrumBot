## @file admin.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing administrative commands.
#  @date Mar 6, 2020

from discord.ext import commands

## @brief Discord commands related to administrative actions in a guild.
#  @details These commands should only be run by administrators of guilds.
class Admin(commands.Cog, name="Admin Commands"):
    ## @brief Admin constructor
    def __init__(self, bot):
        self.bot = bot

    ## @brief Loads a new cog into the bot.
    #  @param cog A string having the name of the python file, usually in the form of 'cogs.<file_name>'.
    #  @throws Exception if the extension fails to load.
    @commands.command(name='load', hidden=True)
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
    
    ## @brief Unloads a cog from the bot.
    #  @param cog A string having the name of the python file, usually in the form of 'cogs.<file_name>'.g 
    #  @throws Exception if the extension fails to unload.
    @commands.command(name='unload', hidden=True)
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

    ## @brief Reloads a cog in the bot.
    #  @param cog A string having the name of the python file, usually in the form of 'cogs.<file_name>'.g 
    #  @throws Exception if the extension fails to reload.
    @commands.command(name='reload', hidden=True)
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

    ## @brief Purges messages from the Discord channel.
    #  @param number An integer representing the max amount of messages to delete.
    @commands.command(name='purge', hidden=True)
    @commands.is_owner()
    @commands.guild_only()
    async def purge_msg(self, ctx, *, number: int):
        deleted = await ctx.channel.purge(limit=number)
        print(f'[Log] {ctx.author} purged {len(deleted)} messages.')
        await ctx.send(f'> Deleted **{len(deleted)}** messages')

## @brief The setup command for this cog.
#  @param bot The bot defined in bot.py.
def setup(bot):
    bot.add_cog(Admin(bot))