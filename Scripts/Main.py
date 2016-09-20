from functions import *
import os
import re

output = os.listdir('/Users/stephane.sol/Developer/OfficialProjectOCR/OutPut')
input = '/Users/stephane.sol/Developer/OfficialProjectOCR/Data/Text/39.txt'

page = parse(input)

dict = {}

class word(object):
    def __init__(self, page, entry, english_word, french_word, english_sent, english_sent2, french_sent, french_sent2):
        self.page = page
        self.entry = entry
        self.english_word = english_word
        self.french_word = french_word
        self.english_sent = english_sent
        self.english_sent2 = english_sent2
        self.french_sent = french_sent
        self.french_sent2 = french_sent2

    def __repr__(self):
        return "<page:%s entry:%s english_word:%s french_word:%s english_sent:%s english_sent2:%s french_sent:%s french_sent2:%s>" % (self.page, self.entry, self.english_word, self.french_word, self.english_sent, self.english_sent2, self.french_sent, self.french_sent2)

for idx, val in enumerate(page[1::]):

    #split = re.sub(r'([.?"!])\s*(?=[A-Z])', r'\1|', val).replace('\n',' ').split('|')
    ## http://stackoverflow.com/questions/5553410/regular-expression-match-a-sentence
    split = re.sub(r'([A-Z\“\"][^.!?]*(?:[.!?](?![\'"]?\s|$)[^.!?]*)*[.!?]?[\'"]?(?=\s|$))', r'|\1', val.replace('\n', ' ')).split('|')
    ## split2 = re.sub(r'.([A-Z])', r'|\1', split[0]).split('|')
    ##split2 = re.sub(r'.([A-Z][^.!?]*(?:[.!?](?![\'"]?\s|$)[^.!?]*)*[.!?]?[\'"]?(?=\s|$))',r'|\1', split[0]).split('|')
    split2 = re.sub(r'([a-z]{1,2}\.(?!\s[a-z]{1,2}\.)|\(.*\)(?!\s[a-z]{1,2}\.)|\s(?![a-z]{1,2}\.)(?!\(.*\))(?!m\s)(?!pl\s)(?!f\s))',r'\1|', split[0],1).split('|')



    try:
        entry = idx + 1
        page_num = page[0]
        entry_key = ('{0}-{1}').format(page_num, entry)

        english_sentence = split[2]
        french_sentence = split[1]
        english_word = split2[1]
        french_word = split2[0]
        try:
            french_sent2 = split[3]
        except IndexError:
            french_sent2 = ''
        try:
            english_sent2 = split[4]
        except IndexError:
            english_sent2 = ''
    except IndexError:
            print('Error at {0} - {1}'.format(entry_key,french_word))

    dict[entry_key] = word(page=page_num, entry=entry, english_word=english_word,
                           french_word=french_word, english_sent=english_sentence,
                           english_sent2=english_sent2, french_sent=french_sentence, french_sent2=french_sent2)

print(dict)