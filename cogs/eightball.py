"""EightBall

This module includes the Magic 8-ball command.
"""


import random

import discord

from discord.ext import commands


class EightBall(commands.Cog):
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


def setup(bot):
    bot.add_cog(EightBall(bot))
