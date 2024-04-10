import re
import pandas as pd
from googletrans import Translator

translator = Translator()
frequency = {}

document_text = open('t.txt', 'rt' ,encoding="UTF-8")
text_string = document_text.read().lower()
match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
 
for word in match_pattern:
    count = frequency.get(word, 0)
    frequency[word] = count + 1

# 단어와 번역을 저장할 리스트 생성
data = []

# 각 단어에 대해 번역 수행 및 데이터 리스트에 추가
for word, count in frequency.items():
    translation = translator.translate(word, dest='ko').text
    data.append({'단어': word, '번역': translation, '빈도수': count})

# 데이터프레임 생성
df = pd.DataFrame(data)

# 엑셀 파일로 저장
df.to_excel('result.xlsx', index=False)
