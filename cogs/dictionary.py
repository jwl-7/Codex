"""Dictionary

This module includes dictionary commands.
"""


import urllib.parse

import requests
import discord
import yaml
from discord.ext import commands


with open('config.yml') as file:
    config = yaml.safe_load(file)


class Dictionary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx, *, search):
        """!define - Search Merriam-Webster Dictionary."""
        url = 'https://dictionaryapi.com/api/v3/references/collegiate/json/'
        token = config['dictionary']['token']

        r = requests.get(f'{url}{search}?key={token}')
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as error:
            await ctx.send('Sorry, your **!define** search failed')
            return print(f'[ERROR] {error}')

        data = r.json()
        word = data[0]['meta']['id']
        pronunciation = data[0]['hwi']['prs'][0]['mw']
        word_type = data[0]['fl']
        definition = data[0]['shortdef'][0]
        link = f'https://www.merriam-webster.com/dictionary/{search}'

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(
            name='Merriam-Webster Dictionary',
            icon_url='https://i.imgur.com/rPvCVSQ.png'
        )
        embed.add_field(name=f'**{word}**', value=f'/{pronunciation}/', inline=False)
        embed.add_field(name=f'**{word_type}**', value=f'{definition}', inline=False)
        embed.add_field(name='**Search Result**', value=f'{link}', inline=False)
        await ctx.send(embed=embed)

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
        embed.set_author(
            name='Urban Dictionary',
            icon_url='https://i.imgur.com/Ojxf6W5.png'
        )
        embed.add_field(name=f'**{word}**', value=f'{definition}', inline=False)
        embed.add_field(name=f'**Example**', value=f'{example}', inline=False)
        embed.add_field(name='**Search Result**', value=f'{link}', inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Dictionary(bot))
