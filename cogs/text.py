"""Text

This module includes commands that modify text.
"""


import discord
from discord.ext import commands


class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def fliptext(self, ctx, *, message):
        """!fliptext <message> - Flip text upside down/backwards."""
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

        text = message
        await ctx.message.delete()
        flip_text = ''
        for char in text:
            flip_text += flipped[char] if char in flipped else char

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name=f'*{ctx.author.name} says...*', value=f'**{flip_text[::-1]}**')
        await ctx.send(embed=embed)

    @commands.command()
    async def sponge(self, ctx, *, message):
        """!sponge <message> - Convert message to SpongeBob meme text."""
        text = message
        sponge_text = ''
        await ctx.message.delete()
        for i, char in enumerate(text):
            sponge_text += char.upper() if i & 1 else char.lower()

        embed = discord.Embed(colour=discord.Colour.blue())
        embed.add_field(name=f'*{ctx.author.name} mocks...*', value=f'**{sponge_text}**')
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Text(bot))
