# Codex
a python discord bot with Markov chain responses, slots, and more

## Commands
* Info
    - **!help** - dm bot command list
    - **!ping** - test bot latency

* Fun
    - **!8ball** - magic 8-ball
    - **!coin** - heads or tails
    - **!horoscope** *\<sunsign>* - daily horoscope
    - **!joke** - random dad joke
    - **!lmgtfy** *\<search>* - create lmgtfy link
    - **!shiba** - random shiba image
    - **!slots** - fruit emojis slot machine
    - **!sponge** *\<message>* - convert message to spongemock text

* Generators
    - **!audiophile** - generate hipster audio jargon
    - **!corporate** - generate corporate bulls**t
    - **!education** - generate educational nonsense
    - **!excuse** - generate the perfect excuse
    - **!technology** - generate hollywood tech jargon
    - **!wisdom** - generate deepak chopra quote

## Admin Commands
- **!admincheck** - bot owner check
- **!load** *\<name>* - load extension
- **!unload** *\<name>* - unload extension
- **!reload** *\<name>* - reload extension

## Markov Sentence Generator
- triggered when a message includes the bot name or @mentions it
- words grabbed from chatlog stored in sqlite database
- sentences become more amusing overtime as bot "learns" more words

## Screenshots
[![codex-chatbot.png](https://i.imgur.com/dMXa1q0.png)](https://imgur.com/dMXa1q0)

## Requirements
* Python 3.8+
* [discord.py](https://github.com/Rapptz/discord.py)

## License
This project is released under the GNU GPL License - see the [LICENSE](LICENSE) file for details