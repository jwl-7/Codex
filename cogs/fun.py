"""Fun Commands

This module includes fun/simple commands.
"""


import random
import urllib.parse

import requests
import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def coin(self, ctx):
        """!coin - Coin Flip"""
        faces = ['Heads!', 'Tails!']
        outcome = random.choice(faces)

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name=f'*{ctx.author.name}, the coin lands...*', value=f'**{outcome}**')
        await ctx.send(embed=embed)

    @commands.command()
    async def joke(self, ctx):
        """!joke - Random dad joke"""
        r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as error:
            return print(f'[ERROR] {error}')

        await ctx.send(r.text)

    @commands.command()
    async def lmgtfy(self, ctx, *, search):
        """!lmgtfy <search> - Create lmgtfy link"""
        await ctx.send(
            '<https://lmgtfy.com/?iie=1&q={}>'
            .format(urllib.parse.quote_plus(search))
        )

    @commands.command()
    async def shiba(self, ctx):
        """!shiba - Random Shiba"""
        r = requests.get('https://dog.ceo/api/breed/shiba/images/random')
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as error:
            return print(f'[ERROR] {error}')

        image = r.json()['message']
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def slots(self, ctx):
        """!slots - Fruit Emojis Slot Machine"""
        slots = ['apple', 'watermelon', 'taco', 'cherries', 'doughnut', 'grapes']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        slot4 = slots[random.randint(0, 5)]

        slot_spin = f'|\t:{slot1}:\t|\t:{slot2}:\t|\t:{slot3}:\t|\t:{slot4}:\t|'
        jackpot = '$$$ !!! JACKPOT !!! $$$'

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='Slot Machine', icon_url='https://i.imgur.com/8oGuoyq.png')
        embed.add_field(
            name=f'*{ctx.author.name} pulls the slot machine handle...*',
            value='\u200b',
            inline=False
        )

        if (
            slot1 == slot2 and slot3 == slot4 or
            slot1 == slot3 and slot2 == slot4 or
            slot1 == slot4 and slot2 == slot3
        ):
            embed.add_field(name=slot_spin, value='\u200b')
            embed.set_footer(text=jackpot)
        else:
            embed.add_field(name=slot_spin, value='\u200b')
        await ctx.send(embed=embed)

    @commands.command()
    async def sponge(self, ctx, *, message):
        """!sponge <message> - Converts message to SpongeBob meme text."""
        text = message
        sponge_text = ''
        await ctx.message.delete()
        for i, char in enumerate(text):
            sponge_text += char.upper() if i & 1 else char.lower()

        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_author(name='Spongemock', icon_url='https://i.imgur.com/TIXAQhB.png')
        embed.add_field(name=f'*{ctx.author.name} mocks...*', value=f'**{sponge_text}**')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Fun(bot))
