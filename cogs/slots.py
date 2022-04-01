"""Slots

This module includes the fruit emoji slots command.
"""


import disnake
import random

from disnake.ext import commands


class Slots(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def slots(self, ctx):
        """.slots - Play fruit emojis slot machine."""
        icon_url = 'https://i.imgur.com/8oGuoyq.png'
        emojis = ['apple', 'cherries', 'doughnut', 'grapes', 'taco', 'watermelon']
        jackpot = '$$$ !!! JACKPOT !!! $$$'
        jackshit = '(◕‿◕)╭∩╮ YOU GET NOTHING !!!'

        embed = disnake.Embed(colour=disnake.Colour.gold())
        embed.set_author(name='Slot Machine', icon_url=icon_url)
        embed.add_field(
            name=f'*{ctx.author.name} pulls the slot machine handle...*',
            value='\u200b',
            inline=False
        )
        slots = ['\t' for _ in range(4)]
        slot_spin = self.slot_spin(slots)
        embed.add_field(name=slot_spin, value='\u200b')
        embed_dict = embed.to_dict()
        slot_message = await ctx.send(embed=embed)

        for slot_num in range(4):
            for _ in range(5):
                slot = random.choice(emojis)
                slot = f':{slot}:'
                slots[slot_num] = slot
                slot_spin = self.slot_spin(slots)
                embed_dict['fields'][1]['name'] = slot_spin
                embed = disnake.Embed.from_dict(embed_dict)
                await slot_message.edit(embed=embed)

        if (
            slots[0] == slots[1] and slots[2] == slots[3] or
            slots[0] == slots[2] and slots[1] == slots[3] or
            slots[0] == slots[3] and slots[1] == slots[2]
        ):
            embed.set_footer(text=jackpot)
        else:
            embed.set_footer(text=jackshit)
        await slot_message.edit(embed=embed)

    def slot_spin(self, slots):
        return f'|\t{slots[0]}\t|\t{slots[1]}\t|\t{slots[2]}\t|\t{slots[3]}\t|'


def setup(bot):
    bot.add_cog(Slots(bot))
