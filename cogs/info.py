"""Info

This module contains help commands.
"""


import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        """!help - Bot Command List"""
        command_list1 = (
            '**!8ball** - magic 8-ball\n'
            '**!coin** - heads or tails\n'
            '**!slots** - slot machine\n'
            '**!wisdom** - generate fake chopra quote\n'
            '**!cbs** - generate corporate bullshit\n'
            )
        command_list2 = (
            '**!sponge** *<message>* - spongemock text\n'
            '**!lmgtfy** *<search>* - generate lmgtfy link\n'
            '**!joke** - random joke\n'
            '**!shiba** - random shiba image\n'
            '**!ping** - test bot latency'
        )
        embed = discord.Embed(
            colour=discord.Colour.purple(),
            title='Codex BOT - Command List'
        )
        embed.add_field(name=command_list1, value='\u200b')
        embed.add_field(name=command_list2, value='\u200b')
        try:
            await ctx.author.send(embed=embed)
        except discord.Forbidden:
            return print(f'[ERROR] Failed to send !help list to {ctx.author.name}')

    @commands.command()
    async def ping(self, ctx):
        """!ping - Bot Response Time"""
        latency = self.bot.latency
        milliseconds = int(round(latency * 1000))

        embed = discord.Embed(colour=discord.Colour.green())
        embed.add_field(name=f'Pong!', value=f'*Latency:* **{milliseconds}ms**')
        await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Info(bot))
