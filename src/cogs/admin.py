## @file admin.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief A cog containing administrative commands.
#  @date Mar 6, 2020

from discord.ext import commands

## @brief Discord commands related to administrative actions in a guild.
#  @details These commands should only be run by administrators of guilds.
class AdminCog(commands.Cog, name="Admin Commands"):
    ## @brief AdminCog constructor
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
            await ctx.send(f'```Error: failed to load {cog}```')
            return
        await ctx.send(f'{cog} loaded.')
    
    ## @brief Unloads a cog from the bot.
    #  @param cog A string having the name of the python file, usually in the form of 'cogs.<file_name>'.g 
    #  @throws Exception if the extension fails to unload.
    @commands.command(name='unload', hidden=True)
    @commands.is_owner()
    async def cunload(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'```Error: failed to unload {cog}```')
            return
        await ctx.send(f'{cog} unloaded.')

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
            await ctx.send(f'```Error: failed to reload {cog}```')
            return
        await ctx.send(f'{cog} reloaded.')

    ## @brief Purges messages from the Discord channel.
    #  @param number An integer representing the max amount of messages to delete.
    @commands.command(name='purge', hidden=True)
    @commands.is_owner()
    @commands.guild_only()
    async def purge_msg(self, ctx, *, number: int):
        deleted = await ctx.channel.purge(limit=number)
        print(f'{ctx.author} purged {len(deleted)} messages.')
        await ctx.send(f'```Deleted {len(deleted)} messages.```')

## @brief The setup command for this cog.
#  @param bot The bot defined in bot.py.
def setup(bot):
    bot.add_cog(AdminCog(bot))