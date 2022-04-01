"""Admin

This module contains utility commands for the owner.
"""


import config
import disnake
import sys

from disnake.ext import commands


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def admincheck(self, ctx):
        """!admincheck - Check if you are the Codex BOT owner."""
        is_admin = ctx.author.id == config.bot['owner']
        embed = disnake.Embed(colour=disnake.Colour.red())
        if is_admin:
            embed.add_field(
                name='Admin',
                value=f'*{ctx.author.name}*, you are the admin!'
            )
        else:
            embed.add_field(
                name='Admin',
                value=f'*{ctx.author.name}*, who are you?'
            )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, name):
        """!load <name> - Load extension."""
        embed = disnake.Embed(colour=disnake.Colour.red())
        try:
            self.bot.load_extension(f'cogs.{name}')
        except disnake.DiscordException:
            embed.add_field(
                name='Admin',
                value=f'Failed to load extension *{name}.py*'
            )
            return await ctx.send(embed=embed)

        embed.add_field(
            name='Admin',
            value=f'Loaded extension *{name}.py*'
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, name):
        """!unload <name> - Unload extension."""
        embed = disnake.Embed(colour=disnake.Colour.red())
        try:
            self.bot.unload_extension(f'cogs.{name}')
        except disnake.DiscordException:
            embed.add_field(
                name='Admin',
                value=f'Failed to unload extension *{name}.py*'
            )
            return await ctx.send(embed=embed)

        embed.add_field(
            name='Admin',
            value=f'Unloaded extension *{name}.py*'
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, name):
        """!reload <name> - Reload extension."""
        embed = disnake.Embed(colour=disnake.Colour.red())
        try:
            self.bot.reload_extension(f'cogs.{name}')
        except disnake.DiscordException:
            embed.add_field(
                name='Admin',
                value=f'Failed to reload extension *{name}.py*'
            )
            return await ctx.send(embed=embed)

        embed.add_field(
            name='Admin',
            value=f'Reloaded extension *{name}.py*'
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def restart(self, ctx):
        """!restart - Restart Codex."""
        embed = disnake.Embed(colour=disnake.Colour.red())
        embed.add_field(
            name='Admin',
            value=f'Restarting *Codex*...'
        )
        await ctx.send(embed=embed)
        await self.bot.logout()
        sys.exit(0)


def setup(bot):
    bot.add_cog(Admin(bot))
