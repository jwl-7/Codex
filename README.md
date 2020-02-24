# Codex
a python discord bot with Markov chain responses, slots, and more

## Commands
* Info
    - **!about** - codex bot information
    - **!help** - dm bot command list
    - **!ping** - test bot latency
    - **!status** - codex bot stats

* Fun
    - **!8ball** - magic 8-ball
    - **!coin** - heads or tails
    - **!dice** - roll two dice
    - **!horoscope** *\<sunsign>* - daily horoscope
    - **!joke** - random dad joke
    - **!lmgtfy** *\<search>* - create lmgtfy link
    - **!shiba** - random shiba image
    - **!slots** - fruit emojis slot machine

* Generators
    - **!audiophile** - generate hipster audio jargon
    - **!corporate** - generate corporate bulls**t
    - **!education** - generate educational nonsense
    - **!excuse** - generate the perfect excuse
    - **!technology** - generate hollywood tech jargon
    - **!wisdom** - generate deepak chopra quote

* Text
    - **!ascii** *\<message>* - convert message to ascii art
    - **!fliptext** *\<message>* - flip message upside down/backwards
    - **!sponge** *\<message>* - convert message to spongemock text

* Dictionary
    - **!define** *\<search>* - search merriam-webster dictionary
    - **!udefine** *\<search>* - search urban dictionary

## Admin Commands
- **!admincheck** - bot owner check
- **!adminhelp** - dm bot admin command list
- **!load** *\<name>* - load extension
- **!unload** *\<name>* - unload extension
- **!reload** *\<name>* - reload extension
- **!restart** - restart bot

## Markov Sentence Generator
- triggered when a message includes the bot name or @mentions it
- words grabbed from chatlog stored in sqlite database
- sentences become more amusing overtime as bot "learns" more words

## Preview
[![codex-chatbot.png](https://i.imgur.com/GsFqPu8.gif)](https://imgur.com/a/VX450os)

## Requirements
* Python 3.8+
* [discord.py](https://github.com/Rapptz/discord.py)

## License
This project is released under the GNU GPL License - see the [LICENSE](LICENSE) file for details