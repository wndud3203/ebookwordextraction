import re
import string
import sys
import googletrans

translator = googletrans.Translator()
frequency = {}

document_text = open('test.txt', 'rt' ,encoding="UTF-8")
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word,0)
    frequency[word] = count + 1
     
frequency_list = frequency.keys()
 

#sys.stdout = open('asdf.txt','w')
r = ""
for words in frequency_list:
    r = translator.translate(words,dest='ko')
    print(f"{r.text}")



    