import discord
from discord import app_commands
from discord.ext import commands

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
    await bot.add_cog(LycanBot(bot))
    await bot.load_extension('LycanBot.commands.reloader')
    await bot.load_extension('LycanBot.commands.source')