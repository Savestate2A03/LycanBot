from discord.ext import commands
from discord import app_commands
import discord

class Reloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def load_extension(self, ctx, *, extension):
        if not await self.bot.is_owner(ctx.author): 
            await ctx.send(f'HEY ... ur not the owner . sorry bud !!')
            return
        try:
            await self.bot.load_extension('LycanBot.commands.' + extension)
            await ctx.send(f'YAY omg .. loaded {extension} !!! ARF')
            try:
                print('Syncing after load...')
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands.")
            except Exception as e:
                print(e)
        except discord.ext.commands.ExtensionNotFound:
            await ctx.send(f'awrruu.. {extension} not found ...')
        except discord.ext.commands.ExtensionAlreadyLoaded:
            await ctx.send(f'heyuh ,.. {extension} already loadedd lollll x3')
        except discord.ext.commands.NoEntryPointError:
            await ctx.send(f'wrruf.. {extension} doesnt have a setup lol,.')
        except discord.ext.commands.ExtensionFailed:
            await ctx.send(f'UM.. {extension} .. it EXPLODED !!!!!')

    @commands.hybrid_command()
    async def reload_extension(self, ctx, *, extension):
        if not await self.bot.is_owner(ctx.author): 
            await ctx.send(f'HEY ... ur not the owner . sorry bud !!')            
            return
        try:
            await self.bot.reload_extension('LycanBot.commands.' + extension)
            await ctx.send(f'arf arf :3 reloaded {extension} !!! wruf.,')
            try:
                print('Syncing after reload...')
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands.")
            except Exception as e:
                print(e)
        except discord.ext.commands.ExtensionNotFound:
            await ctx.send(f'awrruu.. {extension} not found ...')
        except discord.ext.commands.ExtensionNotLoaded:
            await ctx.send(f'arf.. {extension} not loaded !! ...')
        except discord.ext.commands.NoEntryPointError:
            await ctx.send(f'wrruf.. {extension} doesnt have a setup lol,.')
        except discord.ext.commands.ExtensionFailed:
            await ctx.send(f'UM.. {extension} .. it EXPLODED !!!!!')

    @commands.hybrid_command()
    async def unload_extension(self, ctx, *, extension):
        if not await self.bot.is_owner(ctx.author): 
            await ctx.send(f'HEY ... ur not the owner . sorry bud !!')            
            return
        try:
            await self.bot.unload_extension('LycanBot.commands.' + extension)
            await ctx.send(f'arf arf >< unloaded {extension} !!! awooo')
            try:
                print('Syncing after unload...')
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands.")
            except Exception as e:
                print(e)
        except discord.ext.commands.ExtensionNotFound:
            await ctx.send(f'awrruu.. {extension} not found ...')
        except discord.ext.commands.ExtensionNotLoaded:
            await ctx.send(f'awrruu.. {extension} not loaded !! ...')

async def setup(bot):
    await bot.add_cog(Reloader(bot))