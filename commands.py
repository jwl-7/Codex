import random
import corporatebs
import chopra

class BotCommands:
    """This class provides the functions that serve as the backend of the bot commands."""

    def help(self):
        """!help - Bot Command List
        
        Returns:
            command_list (str): List of bot commands.
        """
        command_list = (
            "```!8ball - magic 8-ball\n"
            "!cbs - corporate bullshit statement\n" 
            "!coin - heads or tails\n"
            "!slots - slot machine\n" 
            "!sponge - spongebob meme text\n"
            "!wisdom - deepak chopra quote```"
            )
        return command_list

    def magic_8ball(self):
        """!8ball - Magic 8-Ball

        Returns:
            response (str): Random response.
        """
        responses = [
            'It is certain.', 
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
            'Very doubtful.'
            ]
        return random.choice(responses)

    def coin_flip(self):
        """!coin - Coin Flip

        Returns:
            coin_flip (str): The result of the coin flip - heads or tails.
        """
        faces = ['Heads!', 'Tails!']
        coin_flip = random.choice(faces)
        return coin_flip

    def corporate_bullshit(self):
        """Generates random corporate bullshit statement that is built using a randomly selected
        choice of words from the adverbs, verbs, adjectives, and nouns lists.

        Returns:
            statement (str): The corporate bullshit statement.
        """
        adverb = random.choice(corporatebs.adverbs)
        verb = random.choice(corporatebs.verbs)
        adjective = random.choice(corporatebs.adjectives)
        noun = random.choice(corporatebs.nouns)
        statement = f'{adverb} {verb} {adjective} {noun}'
        return statement

    def slot_machine(self):
        """!slots - Fruit Emojis Slot Machine
        
        Returns:
            slot_spin (str): The slot machine spin results in the form of fruit emojis.
            slot_spin + jackpot_msg (str): The slot machine spin results + jackpot message.
        """
        slots = ['apple', 'watermelon', 'taco', 'cherries', 'doughnut', 'grapes']
        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]
        slot4 = slots[random.randint(0, 5)]

        # display slot machine 
        slot_spin = '|\t:{}:\t|\t:{}:\t|\t:{}:\t|\t:{}:\t|    '.format(slot1, slot2, slot3, slot4)
        jackpot_msg = '\n< $$$ !!! JACKPOT !!! $$$ >'

        if (
            slot1 == slot2 and slot3 == slot4 or 
            slot1 == slot3 and slot2 == slot4 or 
            slot1 == slot4 and slot2 == slot3
        ):
            return slot_spin + jackpot_msg
        else:
            return slot_spin

    def sponge(self, message):
        """!sponge - Converts message to SpongeBob meme text.

        Args:
            message (str): The message the user wants to convert to sponge text.

        Returns:
            sponge_msg (str): Converted sPoNgEbOb mEmE tExT.
        """
        message = message.replace('!sponge ', '')
        sponge_msg = ''
        for i, s in enumerate(message):
            if i % 2 == 0:
                sponge_msg += s.lower()
            else:
                sponge_msg += s.upper()
        return sponge_msg

    def wisdom(self):
        """Generates faux Deepak Chopra quote using randomly selected words from 4 lists.

        Returns:
            quote (str): The generated quote.
        """
        part1 = random.choice(chopra.words_1)
        part2 = random.choice(chopra.words_2)
        part3 = random.choice(chopra.words_3)
        part4 = random.choice(chopra.words_4)
        quote = f'{part1} {part2} {part3} {part4}.'
        return quote