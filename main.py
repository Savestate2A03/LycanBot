import discord
import configparser
import asyncio
from discord.ext import commands

config = configparser.ConfigParser()
config.read('settings.ini')

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="----", intents=intents)

async def main():
    await bot.load_extension("LycanBot.LycanBot")

if __name__ == "__main__":
    asyncio.run(main())

bot.run(config['settings']['token'])