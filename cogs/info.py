"""Info

This module contains help commands.
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
        """!about - Get information on Codex."""
        features = (
            '**Features**\n'
            '- Ask the Magic 8-ball\n'
            '- Play fruit emoji slots\n'
            '- Generate tons of corporate/tech jargon\n'
            '- Markov chain sentence responses\n'
            '- ...and much more!'
            )

        embed = discord.Embed(colour=discord.Colour.purple())
        embed.set_author(
            name='Codex BOT - Information',
            icon_url='https://i.imgur.com/wSg6r3n.jpg'
        )
        embed.add_field(
            name=features,
            value='[🤖 View on GitHub](https://github.com/jwl-7/Codex)'
        )
        embed.set_image(url='https://i.imgur.com/GsFqPu8.gif')
        embed.set_footer(
            text='Made by JWL#5526',
            icon_url='https://avatars2.githubusercontent.com/u/37751085?s=460&v=4'
        )
        await ctx.send(embed=embed)
        print(os.getpid())

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def adminhelp(self, ctx):
        """!adminhelp - DM bot admin command list."""
        admin_cmds = (
            '**!admincheck** - bot owner check\n'
            '**!adminhelp** - dm bot admin command list\n'
            '**!load** *<name>* - load extension\n'
            '**!unload** *<name>* - unload extension\n'
            '**!reload** *<name>* - reload extension'
            )

        embed = discord.Embed(colour=discord.Colour.red())
        embed.set_author(
            name='Codex BOT - Admin Command List',
            icon_url='https://i.imgur.com/wSg6r3n.jpg'
        )
        embed.add_field(name=admin_cmds, value='\u200b')
        try:
            await ctx.author.send(embed=embed)
        except discord.Forbidden:
            return print(f'[ERROR] Failed to send !adminhelp list to {ctx.author.name}')

    @commands.command()
    async def help(self, ctx):
        """!help - DM bot command list."""
        info_cmds = (
            '**!about** - codex bot information\n'
            '**!help** - dm bot command list\n'
            '**!ping** - test bot latency\n'
            '**!status** - codex bot stats'
            )
        fun_cmds = (
            '**!8ball** - magic 8-ball\n'
            '**!coin** - heads or tails\n'
            '**!dice** - roll two dice\n'
            '**!horoscope** *<sunsign>* - daily horoscope\n'
            '**!joke** - random dad joke\n'
            '**!lmgtfy** *<search>* - create lmgtfy link\n'
            '**!shiba** - random shiba image\n'
            '**!slots** - fruit emojis slot machine'
            )
        generators_cmds = (
            '**!audiophile** - generate hipster audio jargon\n'
            '**!corporate** - generate corporate bullshit\n'
            '**!education** - generate educational nonsense\n'
            '**!excuse** - generate the perfect excuse\n'
            '**!technology** - generate hollywood tech jargon\n'
            '**!wisdom** - generate deepak chopra quote'
            )
        text_cmds = (
            '**!ascii** *<message>* - convert message to ascii art\n'
            '**!fliptext** *<message>* - flip message upside down/backwards\n'
            '**!sponge** *<message>* - convert message to spongemock text'
            )
        dictionary_cmds = (
            '**!define** *<search>* - search merriam-webster dictionary\n'
            '**!udefine** *<search>* - search urban dictionary'
            )

        embed = discord.Embed(colour=discord.Colour.purple())
        embed.set_author(
            name='Codex BOT - Command List',
            icon_url='https://i.imgur.com/wSg6r3n.jpg'
        )
        embed.add_field(name='Info', value=info_cmds, inline=False)
        embed.add_field(name='Fun', value=fun_cmds, inline=False)
        embed.add_field(name='Generators', value=generators_cmds, inline=False)
        embed.add_field(name='Text', value=text_cmds, inline=False)
        embed.add_field(name='Dictionary', value=dictionary_cmds, inline=False)
        try:
            await ctx.author.send(embed=embed)
        except discord.Forbidden:
            return print(f'[ERROR] Failed to send !help list to {ctx.author.name}')

    @commands.command()
    async def ping(self, ctx):
        """!ping - Test bot latency."""
        latency = self.bot.latency
        milliseconds = int(round(latency * 1000))

        embed = discord.Embed(colour=discord.Colour.green())
        embed.add_field(name='Pong!', value=f'*Latency:* **{milliseconds}ms**')
        await ctx.send(embed=embed)

    @commands.command()
    async def status(self, ctx):
        """!status - Get stats on Codex."""
        uptime = time.time() - self.bot.uptime
        minutes, seconds = divmod(uptime, 60)
        hours, minutes = divmod(minutes, 60)

        process = psutil.Process(os.getpid())
        mem_usage = process.memory_info().rss
        mem_usage /= 1024 ** 2

        embed = discord.Embed(colour=discord.Colour.green())
        embed.set_author(
            name='Codex BOT - Status',
            icon_url='https://i.imgur.com/wSg6r3n.jpg'
        )
        embed.add_field(
            name='🕖 Uptime',
            value=f'{int(hours)} hours, {int(minutes)} minutes, {int(seconds)} seconds',
            inline=False
        )
        embed.add_field(name='📥 Messages Received', value=f'{self.bot.message_count}')
        embed.add_field(name='📤 Messages Sent', value=f'{self.bot.messages_sent}')
        embed.add_field(name='🏷️ Mentions', value=f'{self.bot.mentions_count}')
        embed.add_field(name='💾 Memory Usage', value=f'{mem_usage:.2f} MiB')
        await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Info(bot))
