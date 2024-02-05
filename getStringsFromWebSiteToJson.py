import requests
from bs4 import BeautifulSoup
import json
import re

#ウェブページのURL
url = 'url here'

#リクエストを送り、レスポンスを取得
response = requests.get(url)

#レスポンス内容をBSで解析
soup = BeautifulSoup(response.text, 'html.parser')

#選択したタグの内容をゲット find_all関数内と内包表記を編集して選択すること
title_tags = soup.find_all('a',title=True )
title_texts = [title.get_text() for title in title_tags]

#データの整形
final_texts = []
for text in title_texts:
    # 大文字を小文字に変換し、括弧やコンマ以前の部分のみを取得
    cleaned_text = re.split(r'\(|,', text.lower())[0].strip()

    # A-Zの小文字および空白のみを含む文字列を確認
    if re.match(r'^[a-z\s]*$', cleaned_text):
        final_texts.append(cleaned_text)

#結果をJSONファイルで保存
with open('con5.json', 'w', encoding='utf-8') as file:
    json.dump(final_texts, file, ensure_ascii=False, indent=4)


"""
example_code see below

import requests
from bs4 import BeautifulSoup
import json

url = 'https://en.m.wikipedia.org/wiki/List_of_composers_by_name'

response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

titles = []
for a_tag in soup.find_all('a', title=True):
    titles.append(a_tag['title'])

with open('classicalMusicComposers.json', 'w', encoding='utf-8') as file:
    json.dump(titles, file, ensure_ascii=False, indent=4)

"""