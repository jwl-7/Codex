"""Info

This module contains the bot's utility commands.
"""


import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """!ping - Bot Response Time"""
        latency = self.bot.latency
        milliseconds = int(round(latency * 1000))

        embed = discord.Embed(colour=discord.Colour.green())
        embed.add_field(name=f'*Pong!*', value=f'*Latency:* **{milliseconds}ms**')
        await ctx.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        """!help - Bot Command List"""
        command_list = (
            '**!8ball** - magic 8-ball\n'
            '**!coin** - heads or tails\n'
            '**!slots** - slot machine\n'
            '**!sponge** *<message>* - convert message to spongemock text\n'
            '**!wisdom** - generate fake deepak chopra quote\n'
            '**!cbs** - generate corporate bullshit'
            )
        embed = discord.Embed(colour=discord.Colour.purple())
        embed.set_author(name='Codex BOT - Command List')
        embed.add_field(name=command_list, value='\u200b')
        try:
            await ctx.author.send(embed=embed)
        except discord.Forbidden:
            print(f'[ERROR] Failed to send !help list to {ctx.author.name}')


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Info(bot))
