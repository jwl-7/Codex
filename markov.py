from dbhelper import DBHelper
import random
import string
import re

BOT_NAME = '---> BOT NAME GOES HERE <---'

class Markov:
# This class generates the Markov chain messages for the chatbot.

    def __init__(self):
        return

    # reformats message to be used in Markov chain:
    # removes URL, removes punctuation, converts to lowercase
    def fix_message(self, item_text):
        message = item_text
        message = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', message)
        dePunctuator = str.maketrans('', '', string.punctuation)
        message = message.translate(dePunctuator)
        message = message.lower()
        return message

    # adds punctuation to generated sentence
    def format_sentence(self, item_text):
        sentence = item_text

        # punctuation with weighted chances
        punctuationList = ['!', '?', '.']
        chance = [0.2, 0.1, 0.9]

        # capitalize first word and add punctuation to sentence
        sentence = sentence.capitalize()
        punctuation = random.choices(punctuationList, chance)
        punctuation = str(punctuation[0])
        sentence = sentence.rstrip()
        sentence += punctuation
        return sentence


    # create Markov chain from database messages
    def create_chain(self):
        startWords = []
        wordDict = {}
        flag = 1
        count = 0

        # connect to database
        db = DBHelper()

        # grab messages from database
        messages = db.get_items()

        # loop through all messages and create dictionary
        for item in messages:

            # reformat messages and then split them into word lists
            item = self.fix_message(item)
            tempList = item.split()
            
            # add the first word of each message to a list
            if (len(tempList) > 0 and tempList[0].lower() != BOT_NAME and tempList[0].isdigit() != True):
                startWords.append(tempList[0])

            # create a dictionary of words that will be used to form the sentence
            for index, item in enumerate(tempList):

                # add new word to dictionary
                if tempList[index] not in wordDict:
                    wordDict[tempList[index]] = []

                # add next word to dictionary
                if (index < len(tempList) - 1 and tempList[index + 1].lower() != BOT_NAME
                                              and tempList[index + 1].isdigit() != True):
                    wordDict[tempList[index]].append(tempList[index + 1])
        
        # choose a random word to start the sentence
        currWord = random.choice(startWords)
        sentence = ''

        # generate the Markov chain
        while flag == 1 and count < 100:

            # add word to sentence
            count += 1
            sentence += currWord + ' '

            # choose a random word
            if len(wordDict[currWord]) != 0:
                currWord = random.choice(wordDict[currWord])
                
            # nothing can follow the current word, end the chain
            elif len(wordDict[currWord]) == 0:
                flag = 0
        
        # format final sentence
        sentence = self.format_sentence(sentence)
        return sentence