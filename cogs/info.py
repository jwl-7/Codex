"""Info

This module contains information commands.
"""


import os
import time

import discord
import psutil

from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            self.bot.messages_sent += 1
        self.bot.message_count += 1

        if (
            self.bot.user.name.lower() in message.content.lower() or
            self.bot.user.mentioned_in(message)
        ):
            self.bot.mentions_count += 1

    @commands.command()
    async def about(self, ctx):
        """!about - Codex BOT information."""
        github_url = 'https://github.com/jwl-7/Codex'
        preview_url = 'https://i.imgur.com/GsFqPu8.gif'
        avatar_url = 'https://i.imgur.com/sR82NlB.jpg'
        features = (
            '**Features**\n'
            '- Ask the Magic 8-ball\n'
            '- Play fruit emoji slots\n'
            '- Convert text to ASCII art\n'
            '- Display random shiba image\n'
            '- Generate corporate bulls**t\n'
            '- Look up words on Merriam-Webster\n'
            '- Funny Markov chain sentence responses\n'
            '- ...and much more!'
            )

        embed = discord.Embed(
            colour=discord.Colour.purple(),
            title='Codex BOT - Information'
        )
        embed.add_field(name=features, value=f'[🤖 View on GitHub]({github_url})')
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.set_image(url=preview_url)
        embed.set_footer(text='Made by JWL', icon_url=avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def ping(self, ctx):
        """!ping - Test BOT latency."""
        latency = self.bot.latency
        milliseconds = int(round(latency * 1000))

        embed = discord.Embed(colour=discord.Colour.green())
        embed.add_field(name='Pong!', value=f'Latency: *{milliseconds}ms*')
        await ctx.send(embed=embed)

    @commands.command()
    async def status(self, ctx):
        """!status - Codex BOT stats."""
        uptime = time.time() - self.bot.uptime
        minutes, seconds = divmod(uptime, 60)
        hours, minutes = divmod(minutes, 60)

        process = psutil.Process(os.getpid())
        mem_usage = process.memory_info().rss
        mem_usage /= 1024 ** 2

        embed = discord.Embed(
            colour=discord.Colour.green(),
            title='Codex BOT - Stats'
        )
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(
            name='🕖 Uptime',
            value=f'{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds',
            inline=False
        )
        embed.add_field(name='📥 Messages Received', value=self.bot.message_count)
        embed.add_field(name='📤 Messages Sent', value=self.bot.messages_sent)
        embed.add_field(name='🏷️ Mentions', value=self.bot.mentions_count)
        embed.add_field(name='💾 Memory Usage', value=f'{mem_usage:.2f} MiB')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Info(bot))
