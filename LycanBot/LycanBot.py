import configparser
import discord
from discord import app_commands
from discord.ext import commands

# Main cog, handles loading other extensions
class LycanBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        # Print out useful connection information on the console
        @self.bot.event
        async def on_ready():
            print(f'{bot.user} has connected to Discord! '
                  f'Version {discord.__version__}')
            try:
                synced = await bot.tree.sync()
                print(f"Synced {len(synced)} commands.")
            except Exception as e:
                print(e)

async def setup(bot):
    # Add this cog to the bot
    await bot.add_cog(LycanBot(bot))

    # Add extensions from settings.ini
    config = configparser.ConfigParser()
    config.read('settings.ini')
    cogs = [x.strip() for x in config['default_cogs']['cogs'].split(',')]

    # Iterate through cog names and load their respective extensions
    print('Loading default cogs...')
    for cog in cogs:
        print(f'    Loading {cog}...')
        await bot.load_extension('LycanBot.commands.' + cog)
    print('Finished loading default cogs!')