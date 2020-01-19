# Codex
a python discord bot with Markov chain responses, slots, and more

## Commands
- **!help** - dm user bot command list
- **!8ball** - magic 8-ball
- **!slots** - slot machine
- **!coin** - heads or tails
- **!sponge** *\<message>* - convert message to spongemock text
- **!wisdom** - generate fake deepak chopra quote
- **!cbs** - generate corporate bulls**t
- **!ping** - test bot latency

## Admin Commands
- **!admincheck** - check if you are the bot owner
- **!load** *\<name>* - load extension
- **!unload** *\<name>* - unload extension
- **!reload** *\<name>* - reload extension

## Markov Sentence Generator
- bot includes a Markov chain sentence generator
- words grabbed from chatlog stored in sqlite database
- triggered when a message includes the bot name or @mentions it
- sentences become more amusing overtime as bot "learns" more words

## Screenshots
[![codex-chatbot.png](https://i.imgur.com/dMXa1q0.png)](https://imgur.com/dMXa1q0)

## Requirements
* Python 3.7+
* [discord.py](https://github.com/Rapptz/discord.py)

## License
This project is released under the GNU GPL License - see the [LICENSE](LICENSE) file for details