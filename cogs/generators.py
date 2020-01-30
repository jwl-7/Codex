"""Generators

This module includes jargon generators.
"""


import random
import discord
import jargon.chopra as chopra
import jargon.corporate as corp
import jargon.education as edu

from discord.ext import commands


class Generators(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def wisdom(self, ctx):
        """!wisdom - Generates faux Deepak Chopra quote using randomly selected words."""
        part1 = random.choice(chopra.words1)
        part2 = random.choice(chopra.words2)
        part3 = random.choice(chopra.words3)
        part4 = random.choice(chopra.words4)
        quote = f'{part1} {part2} {part3} {part4}.'

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name=f'Chopra Wisdom', value=f'**{quote}**')
        await ctx.send(embed=embed)

    @commands.command()
    async def corporate(self, ctx):
        """!corporate - Generates corporate bulls**t statement using randomly selected words."""
        adverb = random.choice(corp.adverbs)
        verb = random.choice(corp.verbs)
        adjective = random.choice(corp.adjectives)
        noun = random.choice(corp.nouns)
        statement = f'{adverb} {verb} {adjective} {noun}'

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name=f'Corporate Bullshit', value=f'**{statement}**')
        await ctx.send(embed=embed)

    @commands.command()
    async def education(self, ctx):
        """!education - Generates educational nonsense using randomly selected words."""
        verb = random.choice(edu.verbs)
        adjective = random.choice(edu.adjectives)
        noun = random.choice(edu.nouns)
        phrase = random.choice(edu.phrase)
        statement = f'We will {verb} {adjective} {noun} {phrase}.'

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name=f'Educational Nonsense', value=f'**{statement}**')
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Generators(bot))
