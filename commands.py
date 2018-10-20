import random

class Commands:
    # This class provides unnecessary commands and rng games for the bot.

    # list of bot commands
    def help(self):
        commandList = ("```!8ball - Magic 8-Ball\n" 
                          "!coin - Heads or Tails\n"
                          "!slots - Slot Machine\n" 
                          "!sponge - Spongebob Meme Text\n```")

        return commandList

    # magic 8-ball
    def magic_8ball(self):
        responses = ['It is certain.', 'It is decidedly so.', 'Without a doubt.',
                   'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
                   'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                   'Reply hazy, try again.', 'Ask again later.',
                   'Better not tell you now.', 'Cannot predict now.',
                   'Concentrate and ask again.', 'Do not count on it.',
                   'My reply is no.', 'My sources say no.',
                   'Outlook not so good.', 'Very doubtful.']
        
        return random.choice(responses)

    # coin flip
    def coin_flip(self):
        faces = ['Heads!', 'Tails!']
        return random.choice(faces)

    # slot machine with fruit emojis
    def slot_machine(self):
        slots = ['apple', 'watermelon', 'taco', 'cherries', 'doughnut', 'grapes']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        slot4 = slots[random.randint(0, 5)]

        # display slot machine 
        slotRoll = '|\t:{}:\t|\t:{}:\t|\t:{}:\t|\t:{}:\t|    '.format(slot1, slot2, slot3, slot4)
        jackpot = '\n< $$$ !!! JACKPOT !!! $$$ >'

        if (slot1 == slot2 and slot3 == slot4 or slot1 == slot3 and slot2 == slot4 
                                              or slot1 == slot4 and slot2 == slot3):
            return slotRoll + jackpot
        else:
            return slotRoll

    # converts message to spongebob mocking meme text
    def sponge(self, item_text):
        sText = item_text
        sText = sText.replace('!sponge ', '')
        spongeText = ''

        for i, s in enumerate(sText):
            if i % 2 == 0:
                spongeText += s.lower()
            else:
                spongeText += s.upper()

        return spongeText