"""Dictionary

This module includes dictionary commands.
"""


import urllib.parse

import requests
import discord
from discord.ext import commands


class Dictionary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def udefine(self, ctx, *, search):
        """!udefine - Search Urban Dictionary."""
        url = 'http://api.urbandictionary.com/v0/define?term='

        r = requests.get(f'{url}{urllib.parse.quote_plus(search)}')
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as error:
            await ctx.send('Sorry, your **!udefine** search failed')
            return print(f'[ERROR] {error}')

        data = r.json()
        word = data['list'][0]['word']
        definition = data['list'][0]['definition']
        example = data['list'][0]['example']
        link = data['list'][0]['permalink']

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='Urban Dictionary')
        embed.add_field(name=f'**{word}**', value=f'{definition}', inline=False)
        embed.add_field(name=f'**Example**', value=f'{example}', inline=False)
        embed.add_field(name='**Search Result**', value=f'{link}', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Dictionary(bot))
