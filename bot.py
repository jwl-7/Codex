from dbhelper import DBHelper
from commands import Commands
from markov import Markov
from wisdom import Chopra
import discord
import random

API_TOKEN = '---> DISCORD API TOKEN GOES HERE <---'
BOT_NAME = '---> BOT NAME GOES HERE <---'

# connect to Discord
bot = discord.Client()

# create database
db = DBHelper()
db.setup()

# bot has successfully joined server
@bot.event
async def on_ready():
    print('Logged in as:')
    print('BOT ' + bot.user.name)
    print('ID ' + str(bot.user.id))
    print('----------------------')

# bot responses to messages
@bot.event
async def on_message(message):

    # load commands
    cmd = Commands()

    # do not reply to messages from self
    if message.author == bot.user:
        return

    # magic 8-ball
    elif message.content.startswith('!8ball'):
        fortune = cmd.magic_8ball()
        await message.channel.send(fortune + ' ' + message.author.mention)

    # dm user list of bot commands
    elif message.content.startswith('!help'):
        bot_help = cmd.help()
        await message.author.send(bot_help)

    # slot machine
    elif message.content.startswith('!slots'):
        slot_spin = cmd.slot_machine()
        await message.channel.send(slot_spin + ' ' + message.author.mention)
    
    # coin flip
    elif message.content.startswith('!coin'):
        coin_face = cmd.coin_flip()
        await message.channel.send(coin_face + ' ' + message.author.mention)
    
    # spongebob text
    elif message.content.startswith('!sponge'):
        sponge_text = cmd.sponge(message.content)
        await message.channel.send(sponge_text)
    
    # deepak chopra quote
    elif message.content.startswith('!wisdom'):
        wisdom = Chopra()
        wisdom_quote = wisdom.get_quote()
        await message.channel.send(wisdom_quote)
    
    # ignore commands and attachments
    elif message.content.startswith('!') or message.attachments:
        return
    
    # reply with ridiculous sentence when someone mentions the bot
    elif BOT_NAME in message.content.lower() or bot.user.mentioned_in(message):

        # add message to database
        db.add_item(message.content)

        # generate sentence and reply
        markov = Markov()
        response = markov.create_chain()
        await message.channel.send(response)

    else:
        db.add_item(message.content)

bot.run(API_TOKEN)