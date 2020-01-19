"""Codex Discord BOT

This module contains the core functionality of the bot.
"""

import os
import discord
import yaml
from discord.ext import commands


with open('config.yml') as file:
    config = yaml.safe_load(file)

bot = commands.Bot(command_prefix=config['bot']['prefix'])


@bot.event
async def on_ready():
    print('Logged in as:')
    print('--------------')
    print(f'BOT: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('-----------------------')


def main():
    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            extension = file[:-3]
            bot.load_extension(f'cogs.{extension}')


if __name__ == '__main__':
    main()


bot.run(config['bot']['token'])
