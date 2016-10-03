from functions import *
import os
import re
import json
from pprint import pprint

input = '/Users/stephane.sol/Developer/OfficialProjectOCR/Data/json_not_parsed.json'
output = os.listdir('/Users/stephane.sol/Developer/OfficialProjectOCR/OutPut/')

dict = {}

with open(input) as data_file:
    data = json.load(data_file)

class word(object):
    def __init__(self, english_word, french_word, english_sent, english_sent2, french_sent, french_sent2,entry = 'none'):
        self.entry = entry
        self.english_word = english_word
        self.french_word = french_word
        self.english_sent = english_sent
        self.english_sent2 = english_sent2
        self.french_sent = french_sent
        self.french_sent2 = french_sent2


for item in data:
	entry = item
	french_word = data[item]["words"].split('|')[0].strip()
	english_word = data[item]["words"].split('|')[1].strip()
	english_sent = data[item]["english_sent"].strip()
	english_sent2 = data[item]["english_sent2"].strip()
	french_sent = data[item]["french_sent"].strip()
	french_sent2 = data[item]["french_sent2"].strip()

	dict[entry] = word(english_word=english_word, french_word=french_word, english_sent=english_sent, english_sent2=english_sent2, french_sent=french_sent, french_sent2=french_sent2)



with open('/Users/stephane.sol/Developer/OfficialProjectOCR/OutPut/cleaned.json', 'w') as outfile:
    json.dump(dict, outfile, indent=4, ensure_ascii=False, default=jdefault, sort_keys=True)
