"""Codex Discord BOT

This module contains the core functionality of the bot.
"""


import discord
import yaml
from discord.ext import commands


with open('config.yml') as file:
    config = yaml.safe_load(file)


PREFIX = config['bot']['prefix']
API_TOKEN = config['bot']['token']


extensions = [
    'cogs.chatlog',
    'cogs.chopra',
    'cogs.corporatebs',
    'cogs.eightball',
    'cogs.fun',
    'cogs.info',
    'cogs.markov'
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
