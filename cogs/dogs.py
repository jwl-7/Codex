"""Dogs

This module includes dog image commands.
"""


import discord
import requests

from discord.ext import commands


class Dogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def shiba(self, ctx):
        """!shiba - Display random Shiba image."""
        url = 'https://dog.ceo/api/breed/shiba/images/random'
        embed = discord.Embed(colour=discord.Colour.blue())

        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.RequestException:
            embed = discord.Embed(
                colour=discord.Colour.darker_grey(),
                description='Failed to connect to the *Dog API*'
            )
            return await ctx.send(embed=embed)

        image = r.json()['message']
        embed.set_image(url=image)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Dogs(bot))
