import discord
from discord import app_commands
from discord.ext import commands
import configparser

class LycanBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
        @self.bot.event
        async def on_ready():
            print(f'{bot.user} has connected to Discord! Version {discord.__version__}')
            try:
                synced = await bot.tree.sync()
                print(f"Synced {len(synced)} commands.")
            except Exception as e:
                print(e)

async def setup(bot):
    config = configparser.ConfigParser()
    config.read('settings.ini')

    await bot.add_cog(LycanBot(bot))
    cogs = [x.strip() for x in config['default_cogs']['cogs'].split(',')]
    for cog in cogs:
        await bot.load_extension('LycanBot.commands.' + cog)