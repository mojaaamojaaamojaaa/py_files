import json

#JSONファイルを読み込む
with open('hangmanWordsData.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

#データの重複を避けつつ空のデータと一文字だけのデータを削除
seen = set()#データの重複を避けるためsetに入れる。
filtered_data = []
for item in data:
    if item and len(item) > 1 and item not in seen:#一文字orデータが空、seenになければリストに入れる
        filtered_data.append(item)
        seen.add(item)

#データをJSONファイルで保存
with open('hangmanWordsDataversion1.json', 'w', encoding='utf-8') as file:
    json.dump(filtered_data, file, ensure_ascii=False, indent=4)
