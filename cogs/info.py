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
            '```!8ball - magic 8-ball\n'
            '!coin - heads or tails\n'
            '!slots - slot machine\n'
            '!sponge - spongebob meme text\n'
            '!wisdom - deepak chopra quote\n'
            '!cbs - corporate bullshit statement```'
            )
        try:
            await ctx.author.send(command_list)
        except discord.Forbidden:
            print(f'[ERROR] Failed to send !help list to {ctx.author.name}')


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Info(bot))
