"""Admin

This module contains utility commands for the owner.
"""


import discord
import yaml
from discord.ext import commands


with open('config.yml') as file:
    config = yaml.safe_load(file)


class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    def is_owner(self, ctx):
        """Check the ID against the owner ID in config file."""
        return ctx.author.id == config['bot']['owner']

    @commands.command()
    async def admincheck(self, ctx):
        """!admincheck - Check if the message author is the bot owner."""
        is_admin = self.is_owner(ctx)

        embed = discord.Embed(colour=discord.Colour.red())
        if is_admin:
            embed.add_field(
                name=f'OMG JWL!!!',
                value=f'**It\'s you master! You ARE the admin!**'
            )
        else:
            embed.add_field(
                name=f'Who are you, {ctx.author.name}?',
                value=f'**You are NOT the admin!**'
            )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def load(self, ctx, name):
        """!load <name> - Load extension."""
        embed = discord.Embed(colour=discord.Colour.red())
        try:
            self.bot.load_extension(f'cogs.{name}')
        except discord.DiscordException:
            embed.add_field(
                name=f'Admin',
                value=f'[ERROR] *Failed to load extension* **{name}.py**'
            )
            return await ctx.send(embed=embed)

        print(f'[ADMIN] Loaded extension {name}.py')
        embed.add_field(
            name=f'Admin',
            value=f'*Loaded extension* **{name}.py**'
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def unload(self, ctx, name):
        """!unload <name> - Unload extension."""
        embed = discord.Embed(colour=discord.Colour.red())
        try:
            self.bot.unload_extension(f'cogs.{name}')
        except discord.DiscordException:
            embed.add_field(
                name=f'Admin',
                value=f'[ERROR] *Failed to unload extension* **{name}.py**'
            )
            return await ctx.send(embed=embed)

        print(f'[ADMIN] Unloaded extension {name}.py')
        embed.add_field(
            name=f'Admin',
            value=f'*Unloaded extension* **{name}.py**'
        )
        await ctx.send(embed=embed)

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def reload(self, ctx, name):
        """!reload <name> - Reload extension."""
        embed = discord.Embed(colour=discord.Colour.red())
        try:
            self.bot.reload_extension(f'cogs.{name}')
        except discord.DiscordException:
            embed.add_field(
                name=f'Admin',
                value=f'[ERROR] *Failed to reload extension* **{name}.py**'
            )
            return await ctx.send(embed=embed)

        print(f'[ADMIN] Reloaded extension {name}.py')
        embed.add_field(
            name=f'Admin',
            value=f'*Reloaded extension* **{name}.py**'
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Admin(bot))
