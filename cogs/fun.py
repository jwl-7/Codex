"""Fun

This module includes fun/simple commands.
"""


import random

import discord
import requests

from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coin(self, ctx):
        """!coin - Flip a coin."""
        icon_url = 'https://i.imgur.com/jQX05l8.png'
        faces = ['Heads!', 'Tails!']
        outcome = random.choice(faces)

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='Coin Flip', icon_url=icon_url)
        embed.add_field(name=f'*{ctx.author.name}, the coin lands...*', value=f'**{outcome}**')
        await ctx.send(embed=embed)

    @commands.command()
    async def dice(self, ctx):
        """!dice - Roll two dice."""
        icon_url = 'https://i.imgur.com/rkfXx3q.png'
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        total = die1 + die2

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='Dice Roller', icon_url=icon_url)
        embed.add_field(
            name=f'*{ctx.author.name} rolls the dice...*',
            value=f'**{die1}** and **{die2}** for a total of **{total}**'
        )
        await ctx.send(embed=embed)

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

    @commands.command()
    async def lmgtfy(self, ctx, *, search):
        """!lmgtfy <search> - Create LMGTFY link."""
        url = 'https://lmgtfy.com/?iie=1&q='
        link = f'{url}{requests.utils.quote(search)}'
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name='LMGTFY', value=link)
        await ctx.send(embed=embed)

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
    bot.add_cog(Fun(bot))
