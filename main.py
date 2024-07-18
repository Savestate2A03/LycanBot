import asyncio
import configparser
import discord
from discord.ext import commands

# Read settings ini file using configparser
config = configparser.ConfigParser()
config.read('settings.ini')

# Explicitly disable message content intent, only allow slash commands!
intents = discord.Intents.default()
intents.message_content = False

# Create the bot
bot = commands.Bot(command_prefix="----", intents=intents)

# async main function, required to await load_extension
async def main():
    await bot.load_extension("LycanBot.LycanBot")

# Load LycanBot using asyncio (required in discord.py 2.0+) and run the bot
if __name__ == "__main__":
    asyncio.run(main())
    # Run using the token from settings.ini
    bot.run(config['settings']['token'])

