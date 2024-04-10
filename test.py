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
#r = ""
with open('output.txt', 'w', encoding='utf-8') as output_file:
    for word in frequency_list:
        translation = translator.translate(word, dest='ko').text
        output_file.write(f"{word}  {translation}\n")