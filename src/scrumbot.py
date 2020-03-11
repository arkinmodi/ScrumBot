## @file scrumbot.py
#  @author Arkin Modi, Leon So, Timothy Choy
#  @brief The main controller for ScrumBot. Initializes the Discord bot.
#  @date Mar 5, 2020

from discord.ext import commands

import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

startup_extensions = ["cogs.misc", "cogs.admin", "cogs.members", "cogs.meetings"]
bot = commands.Bot(command_prefix="!", description='ScrumBot')

## @brief Sends a message to the terminal stating that the Discord bot is ready to use.
#  @details When ScrumBot is ready, it sends the terminal its name and id.
@bot.event
async def on_ready():
    print('Logged in as')
    print(f'name: {bot.user.name}')
    print(f'id: {bot.user.id}')
    print('------')

## @brief ScrumBot initializer. Loads all startup extensions.
#  @throws Exception if any extensions fail to load.
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = f'{type(e).__name__}: {e}'
            print(f'Failed to load extension {extension}\n{exc}')

    bot.run(TOKEN, bot=True, reconnect=True)