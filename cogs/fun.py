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

    @commands.command(name='8ball')
    async def _8ball(self, ctx):
        """!8ball - Ask the Magic 8-Ball."""
        icon_url = 'https://i.imgur.com/XhNqADi.png'
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
        embed.set_author(name='Magic 8-Ball', icon_url=icon_url)
        embed.add_field(name=f'*{ctx.author.name}, your fortune says...*', value=f'**{fortune}**')
        await ctx.send(embed=embed)

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
    async def horoscope(self, ctx, sign):
        """!horoscope <sunsign> - Get daily horoscope."""
        url = 'http://horoscope-api.herokuapp.com/horoscope/today/'
        icon_url = 'https://i.imgur.com/MWu59YN.png'
        sign = sign.capitalize()
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
        embed = discord.Embed(title=f'{emojis[sign]} {sign}', colour=discord.Colour.gold())
        embed.set_author(name='Horoscope', icon_url=icon_url)

        try:
            r = requests.get(f'{url}{sign}')
            r.raise_for_status()
        except requests.exceptions.RequestException:
            embed.description = 'Failed to connect to the astrology API'
            return await ctx.send(embed=embed)

        astrology = r.json()['horoscope']
        embed.add_field(
            name=f'*{ctx.author.name}, your daily horoscope is...*',
            value=astrology
        )
        await ctx.send(embed=embed)

    @commands.command()
    async def joke(self, ctx):
        """!joke - Get random dad joke."""
        url = 'https://icanhazdadjoke.com/'
        embed = discord.Embed(colour=discord.Colour.blue())

        try:
            r = requests.get(url, headers={'Accept': 'application/json'})
            r.raise_for_status()
        except requests.exceptions.RequestException:
            embed.add_field(name='Joke', value='Failed to connect to the joke API')
            return await ctx.send(embed=embed)

        data = r.json()
        joke = data['joke']
        embed.add_field(name='Joke', value=joke)
        await ctx.send(embed=embed)

    @commands.command()
    async def lmgtfy(self, ctx, *, search):
        """!lmgtfy <search> - Create lmgtfy link."""
        url = 'https://lmgtfy.com/?iie=1&q='
        link = f'{url}{requests.utils.quote(search)}'
        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name='LMGTFY', value=link)
        await ctx.send(embed=embed)

    @commands.command()
    async def shiba(self, ctx):
        """!shiba - Get random Shiba image."""
        url = 'https://dog.ceo/api/breed/shiba/images/random'
        embed = discord.Embed(colour=discord.Colour.blue())

        try:
            r = requests.get(url)
            r.raise_for_status()
        except requests.exceptions.RequestException:
            embed.add_field(name='Shiba', value='Failed to connect to the dog API')
            return await ctx.send(embed=embed)

        image = r.json()['message']
        embed.set_image(url=image)
        await ctx.send(embed=embed)

    @commands.command()
    async def slots(self, ctx):
        """!slots - Play fruit emojis slot machine."""
        icon_url = 'https://i.imgur.com/8oGuoyq.png'
        slots = ['apple', 'watermelon', 'taco', 'cherries', 'doughnut', 'grapes']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        slot4 = slots[random.randint(0, 5)]

        slot_spin = f'|\t:{slot1}:\t|\t:{slot2}:\t|\t:{slot3}:\t|\t:{slot4}:\t|'
        jackpot = '$$$ !!! JACKPOT !!! $$$'

        embed = discord.Embed(colour=discord.Colour.gold())
        embed.set_author(name='Slot Machine', icon_url=icon_url)
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


def setup(bot):
    bot.add_cog(Fun(bot))
