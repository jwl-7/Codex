"""Horoscope

This module includes the daily horoscope command.
"""


import disnake
import requests

from disnake.ext import commands


class Horoscope(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def horoscope(self, ctx, sign):
        """!horoscope <sunsign> - Find out daily horoscope."""
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

        if sign not in emojis:
            embed = disnake.Embed(
                colour=disnake.Colour.darker_grey(),
                description='Invalid astrological sign for **!horoscope**'
            )
            return await ctx.send(embed=embed)

        embed = disnake.Embed(title=f'{emojis[sign]} {sign}', colour=disnake.Colour.blue())
        embed.set_author(name='Horoscope', icon_url=icon_url)

        try:
            r = requests.get(f'{url}{sign}')
            r.raise_for_status()
        except requests.exceptions.RequestException:
            embed = disnake.Embed(
                colour=disnake.Colour.darker_grey(),
                description='Failed to connect to the *Horoscope API*'
            )
            return await ctx.send(embed=embed)

        astrology = r.json()['horoscope']
        embed.add_field(
            name=f'*{ctx.author.name}, your daily horoscope is...*',
            value=astrology
        )
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Horoscope(bot))
