from discord.ext import commands
from discord import app_commands
import discord

# An owner-only set of commands to load/reload/unload cogs from the bot
# All of these are hidden (ephemeral) commands, only the invoker will see them.
class Reloader(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.hybrid_command()
    async def load_extension(self, ctx, *, extension):
        # If you're not the owner, reject the command
        if not await self.bot.is_owner(ctx.author):
            await ctx.send(f'HEY ... ur not the owner . sorry bud !!',
                           ephemeral=True)
            return
        # Attempt to load the extension, if failed, handle in several ways
        try:
            await self.bot.load_extension('LycanBot.commands.' + extension)
            await ctx.send(f'YAY omg .. loaded {extension} !!! ARF',
                            ephemeral=True)
            # Resync the commands after loading to add the slash command
            try:
                print('Syncing after load...')
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands.")
            except Exception as e:
                print(e)
        # Several ways this can fail, let the owner know how!
        except discord.ext.commands.ExtensionNotFound:
            await ctx.send(f'awrruu.. {extension} not found ...',
                           ephemeral=True)
        except discord.ext.commands.ExtensionAlreadyLoaded:
            await ctx.send(f'heyuh ,.. {extension} already loadedd lollll x3',
                           ephemeral=True)
        except discord.ext.commands.NoEntryPointError:
            await ctx.send(f'wrruf.. {extension} doesnt have a setup lol,.',
                           ephemeral=True)
        except discord.ext.commands.ExtensionFailed:
            await ctx.send(f'UM.. {extension} .. it EXPLODED !!!!!',
                           ephemeral=True)

    # The rest of these are mostly the same so I will not comment on them

    @commands.hybrid_command()
    async def reload_extension(self, ctx, *, extension):
        if not await self.bot.is_owner(ctx.author): 
            await ctx.send(f'HEY ... ur not the owner . sorry bud !!',
                           ephemeral=True)            
            return
        try:
            await self.bot.reload_extension('LycanBot.commands.' + extension)
            await ctx.send(f'arf arf :3 reloaded {extension} !!! wruf.,',
                           ephemeral=True)
        except discord.ext.commands.ExtensionNotFound:
            await ctx.send(f'awrruu.. {extension} not found ...',
                           ephemeral=True)
        except discord.ext.commands.ExtensionNotLoaded:
            await ctx.send(f'arf.. {extension} not loaded !! ...',
                           ephemeral=True)
        except discord.ext.commands.NoEntryPointError:
            await ctx.send(f'wrruf.. {extension} doesnt have a setup lol,.',
                           ephemeral=True)
        except discord.ext.commands.ExtensionFailed:
            await ctx.send(f'UM.. {extension} .. it EXPLODED !!!!!',
                           ephemeral=True)

    @commands.hybrid_command()
    async def unload_extension(self, ctx, *, extension):
        if not await self.bot.is_owner(ctx.author): 
            await ctx.send(f'HEY ... ur not the owner . sorry bud !!',
                           ephemeral=True)            
            return
        try:
            await self.bot.unload_extension('LycanBot.commands.' + extension)
            await ctx.send(f'arf arf >< unloaded {extension} !!! awooo',
                           ephemeral=True)
            try:
                print('Syncing after unload...')
                synced = await self.bot.tree.sync()
                print(f"Synced {len(synced)} commands.")
            except Exception as e:
                print(e)
        except discord.ext.commands.ExtensionNotFound:
            await ctx.send(f'awrruu.. {extension} not found ...',
                           ephemeral=True)
        except discord.ext.commands.ExtensionNotLoaded:
            await ctx.send(f'awrruu.. {extension} not loaded !! ...',
                           ephemeral=True)

async def setup(bot):
    await bot.add_cog(Reloader(bot))