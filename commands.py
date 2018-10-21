import random

class Commands:
    # This class provides unnecessary commands and rng games for the bot.

    # list of bot commands
    def help(self):
        command_list = ("```!8ball - magic 8-ball\n" 
                           "!coin - heads or tails\n"
                           "!slots - slot machine\n" 
                           "!sponge - spongebob meme text\n"
                           "!wisdom - deepak chopra quote```")

        return command_list

    # magic 8-ball
    def magic_8ball(self):
        responses = ['It is certain.', 
                     'It is decidedly so.',
                     'Without a doubt.', 
                     'Yes - definitely.', 
                     'You may rely on it.', 
                     'As I see it, yes.',
                     'Most likely.', 
                     'Outlook good.', 
                     'Yes.', 
                     'Signs point to yes.', 
                     'Reply hazy, try again.', 
                     'Ask again later.', 
                     'Better not tell you now.', 
                     'Cannot predict now.', 
                     'Concentrate and ask again.', 
                     'Do not count on it.', 
                     'My reply is no.', 
                     'My sources say no.', 
                     'Outlook not so good.', 
                     'Very doubtful.']
        
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
        slot_spin = '|\t:{}:\t|\t:{}:\t|\t:{}:\t|\t:{}:\t|    '.format(slot1, slot2, slot3, slot4)
        jackpot = '\n< $$$ !!! JACKPOT !!! $$$ >'

        if (slot1 == slot2 and slot3 == slot4 or slot1 == slot3 and slot2 == slot4 
                                              or slot1 == slot4 and slot2 == slot3):
            return slot_spin + jackpot
        else:
            return slot_spin

    # converts message to spongebob mocking meme text
    def sponge(self, item_text):
        text = item_text
        text = text.replace('!sponge ', '')
        sponge_text = ''

        for i, s in enumerate(text):
            if i % 2 == 0:
                sponge_text += s.lower()
            else:
                sponge_text += s.upper()

        return sponge_text