# Codex
a python discord bot with Markov chain responses, slots, and more

## Features
- !help = dm user list of bot commands
- !8ball = magic 8-ball
- !slots = slot machine
- !coin = heads or tails
- !sponge - spongebob meme text
- !cbs - generate corporate bullshit statement
- !wisdom - generate faux Deepak Chopra quote

## Chatbot
- bot includes a Markov chain sentence generator
- triggered when a message includes the bot name or @mentions it
- automatically adds messages to sqlite database
- sentences become more amusing overtime as bot "learns" more words

## Screenshots
[![codex-chatbot.png](https://i.imgur.com/dMXa1q0.png)](https://imgur.com/dMXa1q0)

## Requirements
* Python 3.7+
* [discord.py](https://github.com/Rapptz/discord.py/tree/rewrite/)

## License
This project is released under the GNU GPL License - see the [LICENSE](LICENSE) file for details