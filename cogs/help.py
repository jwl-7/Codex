"""Help

This module contains help commands.
"""


import disnake

from disnake.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def adminhelp(self, ctx):
        """.adminhelp - DM admin command list."""
        admin_cmds = (
            '**.admincheck** - Check if you are the Codex BOT owner.\n'
            '**.adminhelp** - DM admin command list.\n'
            '**.load** *<name>* - Load extension.\n'
            '**.unload** *<name>* - Unload extension\n'
            '**.reload** *<name>* - Reload extension\n'
            '**.restart** - Restart Codex.'
            )

        embed = disnake.Embed(
            colour=disnake.Colour.red(),
            title='Codex BOT - Admin Command List'
        )
        embed.add_field(name='Admin', value=admin_cmds, inline=False)
        await ctx.author.send(embed=embed)

    @commands.command()
    async def help(self, ctx):
        """.help - DM command list."""
        info_cmds = (
            '**.about** - Codex BOT information.\n'
            '**.help** - DM command list.\n'
            '**.ping** - Test BOT latency.\n'
            '**.status** - Codex BOT stats.'
            )
        fun_cmds = (
            '**.8ball** - Ask the Magic 8-Ball.\n'
            '**.coin** - Flip a coin.\n'
            '**.dice** - Roll two dice.\n'
            '**.horoscope** *<sunsign>* - Find out daily horoscope.\n'
            '**.lmgtfy** *<search>* - Create LMGTFY link.\n'
            '**.slots** - Play fruit emojis slot machine.'
            )
        joke_cmds = (
            '**.csjoke** - Receive random programming joke.\n'
            '**.chucknorris** - Receive Chuck Norris joke.\n'
            '**.joke** - Receive random dad joke.'
            )
        jargon_cmds = (
            '**.audiophile** - Generate hipster audio jargon.\n'
            '**.corporate** - Generate corporate bullshit.\n'
            '**.education** - Generate educational nonsense.\n'
            '**.excuse** - Generate the perfect excuse.\n'
            '**.technology** - Generate hollywood tech jargon.\n'
            '**.wisdom** - Generate deepak chopra quote.'
            )
        text_cmds = (
            '**.ascii** *<message>* - Convert text to ASCII art.\n'
            '**.fliptext** *<message>* - Flip text upside down/backwards.\n'
            '**.sponge** *<message>* - Convert text to sPoNgEbOb mOcKiNg tExT.'
            )
        dog_cmds = (
            '**.dog** - Display random dog image.\n'
            '**.labrador** - Display random Labrador image.\n'
            '**.pyrenees** - Display random Pyrenees image.\n'
            '**.shiba** - Display random Shiba image.\n'
            )
        dictionary_cmds = (
            '**.define** *<search>* - Search Merriam-Webster dictionary.\n'
            '**.udefine** *<search>* - Search Urban Dictionary.'
            )

        embed = disnake.Embed(
            colour=disnake.Colour.purple(),
            title='Codex BOT - Command List'
        )
        embed.add_field(name='Info', value=info_cmds, inline=False)
        embed.add_field(name='Fun', value=fun_cmds, inline=False)
        embed.add_field(name='Jokes', value=joke_cmds, inline=False)
        embed.add_field(name='Jargon', value=jargon_cmds, inline=False)
        embed.add_field(name='Text', value=text_cmds, inline=False)
        embed.add_field(name='Dogs', value=dog_cmds, inline=False)
        embed.add_field(name='Dictionary', value=dictionary_cmds, inline=False)
        await ctx.author.send(embed=embed)


def setup(bot):
    bot.remove_command('help')
    bot.add_cog(Help(bot))
