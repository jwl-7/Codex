"""Dictionary

This module includes dictionary commands.
"""


import config
import disnake
import requests

from disnake.ext import commands


class Dictionary(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def define(self, ctx, *, search):
        """.define <search> - Search Merriam-Webster Dictionary."""
        url = 'https://dictionaryapi.com/api/v3/references/collegiate/json/'
        web_url = 'https://www.merriam-webster.com/dictionary/'
        icon_url = 'https://i.imgur.com/rPvCVSQ.png'
        token = config.dictionary['token']
        link = f'{web_url}{requests.utils.quote(search)}'
        embed = disnake.Embed(colour=disnake.Colour.blue())
        embed.set_author(name='Merriam-Webster Dictionary', icon_url=icon_url)

        try:
            r = requests.get(f'{url}{search}?key={token}')
            r.raise_for_status()
        except requests.exceptions.RequestException:
            embed = disnake.Embed(
                colour=disnake.Colour.darker_grey(),
                description='Failed to connect to the *Dictionary API*'
            )
            return await ctx.send(embed=embed)

        data = r.json()
        if not data or type(data[0]) is not dict:
            embed.description = f'No definition found for *{search}*'
            return await ctx.send(embed=embed)

        word = data[0]['meta']['id']
        pronunciation = data[0]['hwi']['prs'][0]['mw']
        word_type = data[0]['fl']
        definition = data[0]['shortdef'][0]
        embed.add_field(name=f'**{word}**', value=f'/{pronunciation}/', inline=False)
        embed.add_field(name=f'**{word_type}**', value=definition, inline=False)
        embed.add_field(name='**Search Result**', value=link, inline=False)
        await ctx.send(embed=embed)

    @commands.command()
    async def udefine(self, ctx, *, search):
        """.udefine <search> - Search Urban Dictionary."""
        url = 'http://api.urbandictionary.com/v0/define?term='
        icon_url = 'https://i.imgur.com/Ojxf6W5.png'
        embed = disnake.Embed(colour=disnake.Colour.blue())
        embed.set_author(name='Urban Dictionary', icon_url=icon_url)

        try:
            r = requests.get(f'{url}{search}')
            r.raise_for_status()
        except requests.exceptions.RequestException:
            embed = disnake.Embed(
                colour=disnake.Colour.darker_grey(),
                description='Failed to connect to the *Dictionary API*'
            )
            return await ctx.send(embed=embed)

        data = r.json()
        if not data or not data['list']:
            embed.description = f'No definition found for *{search}*'
            return await ctx.send(embed=embed)

        word = data['list'][0]['word']
        definition = data['list'][0]['definition']
        example = data['list'][0]['example']
        link = data['list'][0]['permalink']
        embed.add_field(name=f'**{word}**', value=definition, inline=False)
        embed.add_field(name=f'**Example**', value=example, inline=False)
        embed.add_field(name='**Search Result**', value=link, inline=False)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Dictionary(bot))
