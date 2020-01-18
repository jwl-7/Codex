"""Discord BOT

This module contains the core functionality of the bot.
"""


import discord
from discord.ext import commands


API_TOKEN = '---> DISCORD API TOKEN GOES HERE <---'
BOT_NAME = '---> BOT NAME GOES HERE <---'
PREFIX = '!'
extensions = [
    'cogs.info'
    ]


bot = commands.Bot(command_prefix=PREFIX)


@bot.event
async def on_ready():
    print('Logged in as:')
    print('-----------------------')
    print(f'BOT: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('-----------------------')


def main():
    for extension in extensions:
        bot.load_extension(extension)


if __name__ == '__main__':
    main()


bot.run(API_TOKEN)
