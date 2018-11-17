from dbhelper import DBHelper
import random
import string
import re

BOT_NAME = '---> BOT NAME GOES HERE <---'

class Markov:
    """
    This class generates the Markov chain messages for the chatbot.

    """

    def __init__(self):
        return

    def fix_message(self, item_text):
        """ reformats message to be used in Markov chain """

        message = item_text
        message = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', message)
        de_punctuate = str.maketrans('', '', string.punctuation)
        message = message.translate(de_punctuate)
        message = message.lower()
        return message

    def format_sentence(self, item_text):
        """ adds some formatting to the generated sentence """

        sentence = item_text
        punctuation_list = ['!', '?', '.']
        chance = [0.2, 0.1, 0.9]

        # capitalize first word and add punctuation to end of sentence
        sentence = sentence.capitalize()
        punctuation = random.choices(punctuation_list, chance)
        punctuation = str(punctuation[0])
        sentence = sentence.rstrip()
        sentence += punctuation
        return sentence

    def create_chain(self):
        """ create Markov chain from messages stored in the database """

        start_words = []
        word_dict = {}
        flag = 1
        count = 0
        db = DBHelper()
        messages = db.get_items()

        for item in messages:

            # reformat messages and split the words into lists
            item = self.fix_message(item)
            temp_list = item.split()
            
            # add the first word of each message to a list
            if (
                len(temp_list) > 0 and 
                temp_list[0].lower() != BOT_NAME and 
                temp_list[0].isdigit() != True
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
                    temp_list[index + 1].lower() != BOT_NAME and 
                    temp_list[index + 1].isdigit() != True
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
        sentence = self.format_sentence(sentence)
        return sentence