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

    @commands.command(name='8ball')
    async def _8ball(self, ctx):
        """!8ball - Ask the Magic 8-Ball."""
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'As I see it, yes.',
            'Most likely.',
            'Outlook good.',
            'Yes.',
            'Signs point to yes.',
            'Reply hazy, try again.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Do not count on it.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Very doubtful.'
            ]
        fortune = random.choice(responses)

        embed = discord.Embed(colour=discord.Colour.purple())
        embed.set_author(name='Magic 8-Ball', icon_url='https://i.imgur.com/XhNqADi.png')
        embed.add_field(name=f'*{ctx.author.name}, your fortune says...*', value=f'**{fortune}**')
        await ctx.send(embed=embed)

    @commands.command()
    async def coin(self, ctx):
        """!coin - Flip a coin."""
        faces = ['Heads!', 'Tails!']
        outcome = random.choice(faces)

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.set_author(name='Coin Flip', icon_url='https://i.imgur.com/jQX05l8.png')
        embed.add_field(name=f'*{ctx.author.name}, the coin lands...*', value=f'**{outcome}**')
        await ctx.send(embed=embed)

    @commands.command()
    async def horoscope(self, ctx, sign):
        """!horoscope <sunsign> - Get daily horoscope."""
        emojis = {
            'Aries': '♈',
            'Taurus': '♉',
            'Gemini': '♊',
            'Cancer': '♋',
            'Leo': '♌',
            'Virgo': '♍',
            'Libra': '♎',
            'Scorpio': '♏',
            'Sagitarrius': '♐',
            'Capricorn': '♑',
            'Aquarius': '♒',
            'Pisces': '♓'
        }
        sign = sign.lower().capitalize()

        r = requests.get(f'http://horoscope-api.herokuapp.com/horoscope/today/{sign}')
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as error:
            return print(f'[ERROR] {error}')

        astrology = r.json()['horoscope']
        embed = discord.Embed(title=f'{emojis[sign]} {sign}', colour=discord.Colour.gold())
        embed.set_author(name='Horoscope', icon_url='https://i.imgur.com/MWu59YN.png')
        embed.add_field(
            name=f'*{ctx.author.name}, your daily horoscope is...*',
            value=f'**{astrology}**'
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def joke(self, ctx):
        """!joke - Get random dad joke."""
        r = requests.get('https://icanhazdadjoke.com/', headers={'Accept': 'text/plain'})
        try:
            r.raise_for_status()
        except requests.exceptions.HTTPError as error:
            return print(f'[ERROR] {error}')

        await ctx.send(r.text)

    @commands.command()
    async def lmgtfy(self, ctx, *, search):
        """!lmgtfy <search> - Create lmgtfy link."""
        await ctx.send(
            '<https://lmgtfy.com/?iie=1&q={}>'
            .format(urllib.parse.quote_plus(search))
        )

    @commands.command()
    async def shiba(self, ctx):
        """!shiba - Get random Shiba image."""
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
        """!slots - Play fruit emojis slot machine."""
        slots = ['apple', 'watermelon', 'taco', 'cherries', 'doughnut', 'grapes']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        slot4 = slots[random.randint(0, 5)]

        slot_spin = f'|\t:{slot1}:\t|\t:{slot2}:\t|\t:{slot3}:\t|\t:{slot4}:\t|'
        jackpot = '$$$ !!! JACKPOT !!! $$$'

        embed = discord.Embed(colour=discord.Colour.gold())
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
        """!sponge <message> - Convert message to SpongeBob meme text."""
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
