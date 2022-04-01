"""Text

This module includes commands that modify text.
"""


import disnake
import pyfiglet

from disnake.ext import commands


class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ascii(self, ctx, *, message):
        """.ascii <message> - Convert text to ASCII art."""
        ascii_art = str(pyfiglet.figlet_format(message.strip()))

        if len(ascii_art) > 2000:
            embed = disnake.Embed(
                colour=disnake.Colour.darker_grey(),
                description='Your message was too long for **.ascii**'
            )
            return await ctx.send(embed=embed)

        embed = disnake.Embed(
            colour=disnake.Colour.blue(),
            description=(
                f'**{ctx.author.name}:**\n'
                f'```{ascii_art}```'
            )
        )
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def fliptext(self, ctx, *, message):
        """.fliptext <message> - Flip text upside down/backwards."""
        chars = (
            "!#$%&'()*+,-./0123456789:;<=>?@"
            "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "[\]^_`abcdefghijklmnopqrstuvwxyz{|}"
            )
        alt_chars = (
            "¡#$%⅋,)(*+'-˙/0ƖᄅƐㄣϛ9ㄥ86:;>=<¿@"
            "∀qƆpƎℲפHIſʞ˥WNOԀQɹS┴∩ΛMX⅄Z"
            "]\[^‾,ɐqɔpǝɟƃɥᴉɾʞlɯuodbɹsʇnʌʍxʎz}|{"
            )
        flipped = dict(zip(chars, alt_chars))

        flip_text = ''
        for char in message:
            flip_text += flipped[char] if char in flipped else char

        embed = disnake.Embed(
            colour=disnake.Colour.blue(),
            description=f'**{ctx.author.name}:** {flip_text[::-1]}'
        )
        await ctx.message.delete()
        await ctx.send(embed=embed)

    @commands.command()
    async def sponge(self, ctx, *, message):
        """.sponge <message> - Convert text to sPoNgEbOb mOcKiNg tExT."""
        sponge_text = ''
        for i, char in enumerate(message):
            sponge_text += char.upper() if i & 1 else char.lower()

        embed = disnake.Embed(
            colour=disnake.Colour.blue(),
            description=f'**{ctx.author.name}:** {sponge_text}'
        )
        await ctx.message.delete()
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Text(bot))
