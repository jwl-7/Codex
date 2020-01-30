"""Info

This module contains help commands.
"""


import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

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
        embed.set_image(url='https://i.imgur.com/cbeWRSU.gif')
        embed.set_footer(text='Made by JWL#5526', icon_url='https://avatars2.githubusercontent.com/u/37751085?s=460&v=4')
        await ctx.send(embed=embed)

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
            '**!about** - codex bot information\n'
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
