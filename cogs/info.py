"""Info

This module contains the bot's utility commands.
"""


import discord
from discord.ext import commands


command_list = (
    '```!8ball - magic 8-ball\n'
    '!coin - heads or tails\n'
    '!slots - slot machine\n'
    '!sponge - spongebob meme text\n'
    '!wisdom - deepak chopra quote\n'
    '!cbs - corporate bullshit statement```'
    )


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        """!ping - Bot Response Time

        Returns:
            milliseconds (int): API latency in ms.
        """
        latency = self.bot.latency
        milliseconds = int(round(latency * 1000))
        await ctx.send(f'Pong! Latency: {milliseconds}ms')

    @commands.command()
    async def help(self, ctx):
        """!help - Bot Command List

        Returns:
            command_list (str): List of bot commands.
        """
        await ctx.author.send(command_list)


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Info(bot))
