"""Magic 8-Ball

This module lets the bot tell accurate fortunes.
"""


import random
import discord
from discord.ext import commands


class MagicEightBall(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def eight_ball(self, ctx):
        """!8ball - Magic 8-Ball"""
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


def setup(bot):
    bot.add_cog(MagicEightBall(bot))
