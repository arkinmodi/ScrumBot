## @file bot.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief 
#  @date Mar 5, 2020

from discord.ext import commands
import settings

startup_extensions = ["cogs.misc"]
token = settings.TOKEN
bot = commands.Bot(command_prefix="!")

## @brief
@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def load(ctx, extension_name: str):
    try:
        bot.load_extension(extension_name)
    except (AttributeError, ImportError) as e:
        await ctx.send(f'```py\n{type(e).__name__}: {str(e)}\n```')
        return
    await ctx.send(f'{extension_name} loaded.')

@bot.command()
async def unload(ctx, extension_name: str):
    bot.unload_extension(extension_name)
    await ctx.send(f'{extension_name} unloaded.')

if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Failed to load extension {extension}\n{exc}')

    bot.run(token, bot=True, reconnect=True)