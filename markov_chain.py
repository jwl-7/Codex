"""Markov Chain Sentence Generator

This module uses words from the database to construct fun sentences.
"""


import random
import string
import re

from dbhelper import Database


class Markov:
    """This class contains a simple Markov chain implementation.

    The markov chain is used for the bot to generate funny sentences
    based on what users have said in the Discord server.
    """

    def fix_message(self, item):
        """Reformats message to be used in the chain.

        Args:
            item (str): Text that is grabbed from the sqlite db.

        Returns:
            message (str): Text that has been stripped of all punctuation.
        """
        message = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', item)
        de_punctuate = str.maketrans('', '', string.punctuation)
        message = message.translate(de_punctuate)
        message = message.lower()
        return message

    def format_sentence(self, unformatted_sentence):
        """Adds formatting to generated sentence.

        Args:
            unformatted_sentence (str): Unformatted generated sentence.

        Returns:
            formatted_sentence (str): Formatted generated sentence with first word capitalized and punctation at end.
        """
        punctuation_list = ['!', '?', '.']
        chance = [0.2, 0.1, 0.9]
        formatted_sentence = unformatted_sentence.capitalize()
        punctuation = random.choices(punctuation_list, chance)
        punctuation = str(punctuation[0])
        formatted_sentence = formatted_sentence.rstrip()
        formatted_sentence += punctuation
        return formatted_sentence

    def create_chain(self, bot_name):
        """Creates Markov chain from messages stored in the sqlite db and generates sentence.

        Args:
            bot_name (str): Name of the Discord bot.

        Returns:
            markov_sentence (str): Markov chain generated sentence.
        """
        start_words = []
        word_dict = {}
        flag = 1
        count = 0
        db = Database()
        messages = db.get_items()

        for item in messages:
            # reformat messages and split the words into lists
            item = self.fix_message(item)
            temp_list = item.split()

            # add the first word of each message to a list
            if (
                len(temp_list) > 0 and
                temp_list[0].lower() != bot_name and
                not temp_list[0].isdigit()
            ):
                start_words.append(temp_list[0])

            # create a dictionary of words that will be used to form the sentence
            for index, item in enumerate(temp_list):
                # add new word to dictionary
                if temp_list[index] not in word_dict:
                    word_dict[temp_list[index]] = []

                # add next word to dictionary
                if (
                    index < len(temp_list) - 1 and
                    temp_list[index + 1].lower() != bot_name and
                    not temp_list[index + 1].isdigit()
                ):
                    word_dict[temp_list[index]].append(temp_list[index + 1])

        # choose a random word to start the sentence
        curr_word = random.choice(start_words)
        sentence = ''

        # loop through the chain
        while flag == 1 and count < 100:
            # add word to sentence
            count += 1
            sentence += curr_word + ' '

            # choose a random word
            if len(word_dict[curr_word]) != 0:
                curr_word = random.choice(word_dict[curr_word])

            # nothing can follow the current word, end the chain
            elif len(word_dict[curr_word]) == 0:
                flag = 0

        # format final sentence
        markov_sentence = self.format_sentence(sentence)
        return markov_sentence
