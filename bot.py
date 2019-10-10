"""Discord BOT

This module contains the core functionality of the bot.
"""


import random
import discord

from dbhelper import Database
from commands import BotCommands
from markov_chain import Markov


API_TOKEN = '---> DISCORD API TOKEN GOES HERE <---'
BOT_NAME = '---> BOT NAME GOES HERE <---'

bot = discord.Client()
db = Database()
db.setup()


@bot.event
async def on_ready():
    print('[LOGIN SUCCESSFUL]')
    print('----------------------')
    print(f'BOT: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('----------------------')


@bot.event
async def on_message(message):
    cmd = BotCommands()
    if message.author == bot.user:
        return
    elif message.content.startswith('!8ball'):
        fortune = cmd.magic_8ball()
        await message.channel.send(f'{fortune} {message.author.mention}')
    elif message.content.startswith('!coin'):
        coin_toss = cmd.coin_flip()
        await message.channel.send(f'{coin_toss} {message.author.mention}')
    elif message.content.startswith('!help'):
        bot_help = cmd.help()
        await message.author.send(bot_help)
    elif message.content.startswith('!slots'):
        slot_spin = cmd.slot_machine()
        await message.channel.send(f'{slot_spin} {message.author.mention}')
    elif message.content.startswith('!sponge'):
        sponge_text = cmd.sponge(message.content)
        await message.channel.send(sponge_text)
    elif message.content.startswith('!cbs'):
        corporate_statement = cmd.corporate_bullshit()
        await message.channel.send(corporate_statement)
    elif message.content.startswith('!wisdom'):
        chopra_quote = cmd.wisdom()
        await message.channel.send(chopra_quote)
    elif message.content.startswith('!') or message.attachments:
        return
    elif BOT_NAME in message.content.lower() or bot.user.mentioned_in(message):
        db.add_item(message.content)
        markov = Markov()
        response = markov.create_chain(BOT_NAME)
        await message.channel.send(response)
    else:
        db.add_item(message.content)


bot.run(API_TOKEN)
