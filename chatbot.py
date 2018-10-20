from dbhelper import DBHelper
from commands import Commands
from markov import Markov
import discord
import random

# Discord API Token for BOT
TOKEN = '---> DISCORD API TOKEN GOES HERE <---'
BOT_NAME = '---> BOT NAME GOES HERE <---'

# create Discord client connection
bot = discord.Client()

# create database
db = DBHelper()
db.setup()

# log into Discord
@bot.event
async def on_ready():
    print('Logged in as:')
    print('BOT ' + bot.user.name)
    print('ID ' + str(bot.user.id))
    print('----------------------')

# chat bot response
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
    
    # coin flip
    elif message.content.startswith('!coin'):
        flip = cmd.coin_flip()
        await message.channel.send(flip + ' ' + message.author.mention)

    # slot machine
    elif message.content.startswith('!slots'):
        fruits = cmd.slot_machine()
        await message.channel.send(fruits + ' ' + message.author.mention)
    
    # spongebob text
    elif message.content.startswith('!sponge'):
        spongeText = cmd.sponge(message.content)
        await message.channel.send(spongeText)

    # DM bot commands
    elif message.content.startswith('!help'):
        botHelp = cmd.help()
        await message.author.send(botHelp)
    
    # ignore commands and attachments
    elif message.content.startswith('!') or message.attachments:
        return
    
    # reply with Markov chain generated sentence if bot name is in message
    elif BOT_NAME in message.content.lower() or bot.user.mentioned_in(message):

        # add message to sqlite database
        db.add_item(message.content)

        # generate sentence and reply
        markov = Markov()
        response = markov.create_chain()
        await message.channel.send(response)

    else:
        db.add_item(message.content)

bot.run(TOKEN)