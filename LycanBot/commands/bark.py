from discord.ext import commands
import discord

# A simple command that lets the bot bark at you or others!
class Bark(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # State that the command parameter is a member so the slash command
    # functionaly reflects that appopriately! Very cool feature
    @commands.hybrid_command()
    async def bark(self, ctx, *, member: discord.Member = None):
        member = member or ctx.author # If no member provided, use the invoker
        await ctx.send(f'arrruf !! hi {member.name} !!!!')

async def setup(bot):
    await bot.add_cog(Bark(bot))