from discord.ext import commands
import discord

class Bark(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def bark(self, ctx, *, member: discord.Member = None):
        """Says hello"""
        member = member or ctx.author
        await ctx.send(f'arrruf !! hi {member.name} !!!!')

async def setup(bot):
    await bot.add_cog(Bark(bot))