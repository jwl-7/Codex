# Codex
a python discord bot with Markov chain responses, slots, and more

## Commands
* Info
    - **!about** - Codex BOT information.
    - **!help** - DM command list.
    - **!ping** - Test BOT latency.
    - **!status** - Codex BOT stats.

* Fun
    - **!8ball** - Ask the Magic 8-Ball.
    - **!coin** - Flip a coin.
    - **!dice** - Roll two dice.
    - **!horoscope** *\<sunsign>* - Find out daily horoscope.
    - **!joke** - Receive random dad joke.
    - **!lmgtfy** *\<search>* - Create LMGTFY link.
    - **!shiba** - Display random Shiba image.
    - **!slots** - Play fruit emojis slot machine.

* Generators
    - **!audiophile** - Generate hipster audio jargon.
    - **!corporate** - Generate corporate bulls**t.
    - **!education** - Generate educational nonsense.
    - **!excuse** - Generate the perfect excuse.
    - **!technology** - Generate hollywood tech jargon.
    - **!wisdom** - Generate deepak chopra quote.

* Text
    - **!ascii** *\<message>* - Convert text to ASCII art.
    - **!fliptext** *\<message>* - Flip text upside down/backwards.
    - **!sponge** *\<message>* - Convert text to sPoNgEbOb mOcKiNg tExT.

* Dictionary
    - **!define** *\<search>* - Search Merriam-Webster dictionary.
    - **!udefine** *\<search>* - Search Urban Dictionary.

## Admin Commands
- **!admincheck** - Check if you are the Codex BOT owner.
- **!adminhelp** - DM admin command list.
- **!load** *\<name>* - Load extension.
- **!unload** *\<name>* - Unload extension.
- **!reload** *\<name>* - Reload extension.
- **!restart** - Restart Codex.

## Markov Sentence Generator
- triggered when a message includes the bot name or @mentions it
- words grabbed from chatlog stored in sqlite database
- sentences become more amusing overtime as bot "learns" more words

## Preview
[![codex-chatbot.png](https://i.imgur.com/GsFqPu8.gif)](https://imgur.com/a/VX450os)

## Requirements
* Python 3.8+
* [discord.py](https://pypi.org/project/discord.py/)
* [psutil](https://pypi.org/project/psutil/)
* [PyYAML](https://pypi.org/project/PyYAML/)
* [requests](https://pypi.org/project/requests/)

## License
This project is released under the GNU GPL License - see the [LICENSE](LICENSE) file for details