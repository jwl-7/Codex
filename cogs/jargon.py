"""Generators

This module includes jargon generators.
"""


import random

import discord

import jargon.audio as audio
import jargon.chopra as chopra
import jargon.corporate as corp
import jargon.education as edu
import jargon.excuses as excuses
import jargon.technology as tech
from discord.ext import commands


class Jargon(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def audiophile(self, ctx):
        """!audiophile - Generate hipster audio jargon."""
        words = {
            0: random.choice(audio.words0),
            1: random.choice(audio.words1),
            2: random.choice(audio.words2),
            3: random.choice(audio.words3),
            4: random.choice(audio.words4)
        }
        sentence = random.choice(audio.sentences)
        for x in range(5):
            s = f'{{{x}}}'
            sentence = sentence.replace(s, words[x])

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name='Audio Jargon', value=sentence)
        await ctx.send(embed=embed)

    @commands.command()
    async def corporate(self, ctx):
        """!corporate - Generate corporate bulls**t statement."""
        adverb = random.choice(corp.adverbs)
        verb = random.choice(corp.verbs)
        adjective = random.choice(corp.adjectives)
        noun = random.choice(corp.nouns)
        statement = f'{adverb} {verb} {adjective} {noun}'

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name='Corporate Bullshit', value=statement)
        await ctx.send(embed=embed)

    @commands.command()
    async def education(self, ctx):
        """!education - Generate educational nonsense."""
        verb = random.choice(edu.verbs)
        adjective = random.choice(edu.adjectives)
        noun = random.choice(edu.nouns)
        phrase = random.choice(edu.phrases)
        statement = f'We will {verb} {adjective} {noun} {phrase}.'

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name='Educational Nonsense', value=statement)
        await ctx.send(embed=embed)

    @commands.command()
    async def excuse(self, ctx):
        """!excuse - Generate the perfect excuse."""
        words = {
            0: random.choice(excuses.words0),
            1: random.choice(excuses.words1),
            2: random.choice(excuses.words2),
            3: random.choice(excuses.words3),
            4: random.choice(excuses.words4)
        }
        sentence = random.choice(excuses.sentences)
        for x in range(5):
            s = f'{{{x}}}'
            sentence = sentence.replace(s, words[x])

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name='Perfect Excuse', value=sentence)
        await ctx.send(embed=embed)

    @commands.command()
    async def technology(self, ctx):
        """!technology - Generate hollywood tech jargon."""
        words = {
            0: random.choice(tech.words0),
            1: random.choice(tech.words1),
            2: random.choice(tech.words2),
            3: random.choice(tech.words3),
            4: random.choice(tech.words4)
        }
        sentence = random.choice(tech.sentences)
        for x in range(5):
            s = f'{{{x}}}'
            sentence = sentence.replace(s, words[x])

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name='Tech Jargon', value=sentence)
        await ctx.send(embed=embed)

    @commands.command()
    async def wisdom(self, ctx):
        """!wisdom - Generate Deepak Chopra quote."""
        part0 = random.choice(chopra.words0)
        part1 = random.choice(chopra.words1)
        part2 = random.choice(chopra.words2)
        part3 = random.choice(chopra.words3)
        quote = f'{part0} {part1} {part2} {part3}.'

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name='Chopra Wisdom', value=quote)
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Jargon(bot))
