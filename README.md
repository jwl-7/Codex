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
    - **!lmgtfy** *\<search>* - Create LMGTFY link.
    - **!slots** - Play fruit emojis slot machine.

* Jokes
    - **!csjoke** - Receive random programming joke.
    - **!chucknorris** - Receive random chuck norris joke.
    - **!joke** - Receive random dad joke.

* Jargon
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

* Dogs
    - **!dog** - Display random dog image.
    - **!labrador** - Display random Labrador image.
    - **!pyrenees** - Display random Pyrenees image.
    - **!shiba** - Display random Shiba image.

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
- Triggered when a message includes the BOT name or @mentions Codex.
- Words grabbed from chatlog stored in sqlite database.
- Sentences become more amusing overtime as Codex "learns" more words.

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