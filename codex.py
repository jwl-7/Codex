"""Codex Discord BOT

This module contains the core functionality of the bot.
"""


import config
import disnake
import os
import time

from disnake.ext import commands


bot = commands.Bot(command_prefix=config.bot['prefix'])


@bot.event
async def on_ready():
    print('\nConnected to Discord...\n')
    print(f'BOT: {bot.user.name}')
    print(f'ID: {bot.user.id}')
    print('-----------------------\n')

    bot.uptime = time.time()
    bot.message_count = 0
    bot.messages_sent = 0
    bot.mentions_count = 0


def main():
    for file in os.listdir('cogs'):
        if file.endswith('.py'):
            extension = file[:-3]
            try:
                bot.load_extension(f'cogs.{extension}')
            except disnake.DiscordException:
                print(f'[ERROR] Failed to load extension {extension}.py')


if __name__ == '__main__':
    main()


bot.run(config.bot['token'])
