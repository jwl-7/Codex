import discord
import random
from dbhelper import DBHelper
from commands import Commands
from corporatebs import Corporate
from markov import Markov
from wisdom import Chopra

API_TOKEN = '---> DISCORD API TOKEN GOES HERE <---'
BOT_NAME  = '---> BOT NAME GOES HERE <---'

bot = discord.Client()
db = DBHelper()
db.setup()

@bot.event
async def on_ready():
    print('Logged in as:')
    print('BOT ' + bot.user.name)
    print('ID ' + str(bot.user.id))
    print('----------------------')

@bot.event
async def on_message(message):
    cmd = Commands()
    cbs = Corporate()
    wisdom = Chopra()

    if message.author == bot.user:
        return
    elif message.content.startswith('!8ball'):
        fortune = cmd.magic_8ball()
        await message.channel.send(fortune + ' ' + message.author.mention)
    elif message.content.startswith('!help'):
        bot_help = cmd.help()
        await message.author.send(bot_help)
    elif message.content.startswith('!slots'):
        slot_spin = cmd.slot_machine()
        await message.channel.send(slot_spin + ' ' + message.author.mention)
    elif message.content.startswith('!coin'):
        coin_face = cmd.coin_flip()
        await message.channel.send(coin_face + ' ' + message.author.mention)
    elif message.content.startswith('!sponge'):
        sponge_text = cmd.sponge(message.content)
        await message.channel.send(sponge_text)
    elif message.content.startswith('!cbs')
        corporate_statement = cbs.generate_statement()
        await message.channel.send(corporate_statement)
    elif message.content.startswith('!wisdom'):
        wisdom_quote = wisdom.generate_quote()
        await message.channel.send(wisdom_quote)
    elif message.content.startswith('!') or message.attachments:
        return
    elif BOT_NAME in message.content.lower() or bot.user.mentioned_in(message):
        db.add_item(message.content)
        markov = Markov()
        response = markov.create_chain()
        await message.channel.send(response)
    else:
        db.add_item(message.content)

bot.run(API_TOKEN)