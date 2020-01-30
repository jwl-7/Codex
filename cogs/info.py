"""Info

This module contains help commands.
"""


import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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

        embed = discord.Embed(
            colour=discord.Colour.red(),
            title='Codex BOT - Admin Command List'
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
            '**!help** - dm bot command list\n'
            '**!ping** - test bot latency'
            )
        fun_cmds = (
            '**!8ball** - magic 8-ball\n'
            '**!coin** - heads or tails\n'
            '**!horoscope** *<sunsign>* - daily horoscope\n'
            '**!joke** - random dad joke\n'
            '**!lmgtfy** *<search>* - create lmgtfy link\n'
            '**!shiba** - random shiba image\n'
            '**!slots** - fruit emojis slot machine\n'
            '**!sponge** *<message>* - convert message to spongemock text'
            )
        generators_cmds = (
            '**!audiophile** - generate hipster audio jargon\n'
            '**!corporate** - generate corporate bullshit\n'
            '**!education** - generate educational nonsense\n'
            '**!excuse** - generate the perfect excuse\n'
            '**!technology** - generate hollywood tech jargon\n'
            '**!wisdom** - generate deepak chopra quote'
            )

        embed = discord.Embed(
            colour=discord.Colour.purple(),
            title='Codex BOT - Command List'
        )
        embed.add_field(name='Info', value=info_cmds, inline=False)
        embed.add_field(name='Fun', value=fun_cmds, inline=False)
        embed.add_field(name='Generators', value=generators_cmds, inline=False)
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
        embed.add_field(name=f'Pong!', value=f'*Latency:* **{milliseconds}ms**')
        await ctx.send(embed=embed)


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Info(bot))
