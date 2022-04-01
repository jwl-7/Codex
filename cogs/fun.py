"""Fun

This module includes simple fun commands.
"""


import disnake
import random
import requests

from disnake.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coin(self, ctx):
        """.coin - Flip a coin."""
        icon_url = 'https://i.imgur.com/jQX05l8.png'
        faces = ['Heads!', 'Tails!']
        outcome = random.choice(faces)

        embed = disnake.Embed(colour=disnake.Colour.blue())
        embed.set_author(name='Coin Flip', icon_url=icon_url)
        embed.add_field(name=f'*{ctx.author.name}, the coin lands...*', value=f'**{outcome}**')
        await ctx.send(embed=embed)

    @commands.command()
    async def dice(self, ctx):
        """.dice - Roll two dice."""
        icon_url = 'https://i.imgur.com/rkfXx3q.png'
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        embed = disnake.Embed(colour=disnake.Colour.blue())
        embed.set_author(name='Dice Roller', icon_url=icon_url)
        embed.add_field(
            name=f'*{ctx.author.name} rolls the dice...*',
            value=f'**{die1}** and **{die2}** for a total of **{total}**'
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def lmgtfy(self, ctx, *, search):
        """.lmgtfy <search> - Create LMGTFY link."""
        url = 'https://lmgtfy.com/?iie=1&q='
        link = f'{url}{requests.utils.quote(search)}'
        embed = disnake.Embed(colour=disnake.Colour.blue())
        embed.add_field(name='LMGTFY', value=link)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
