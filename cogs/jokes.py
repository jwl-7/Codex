"""Jokes

This module includes joke commands.
"""


import discord
import requests

from discord.ext import commands


class Jokes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        """!joke - Receive random dad joke."""
        url = 'https://icanhazdadjoke.com/'
        embed = discord.Embed(colour=discord.Colour.blue())

        try:
            r = requests.get(url, headers={'Accept': 'application/json'})
            r.raise_for_status()
        except requests.exceptions.RequestException:
            embed = discord.Embed(
                colour=discord.Colour.darker_grey(),
                description='Failed to connect to the *Joke API*'
            )
            return await ctx.send(embed=embed)

        data = r.json()
        joke = data['joke']
        embed.add_field(name='Joke', value=joke)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jokes(bot))
