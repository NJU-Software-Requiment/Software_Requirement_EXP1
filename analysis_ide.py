import json
import time
import pickle
import random


exchange = {
    '&#60;': '<',
    '&#62;': '>',
    '&#38;': '&',
    '&#34;': "'",
    '&#39;': "'",
    '&#234;': 'ê',
    '&#182;': '¶',
    '&amp;': '&',
    '&quot;': "'",
    '&lt;': '<',
    '&gt;': '>',
    '\u201c': "'",
    '\u201d': "'",
    '\u2018': "'",
    '\u2019': "'",
    '\uff08': '(',
    '\uff09': ')',
    '\uff1f': '?'
}


def myReplace(string):
    for key in exchange:
        string = string.replace(key, exchange[key])
    return string


tags = {}
fr = open('ide_questions', 'rb')
ide_que = pickle.load(fr)
fr.close()

for item in ide_que:
    # tag = item['tags'][0]
    for tag in item['tags']:
        tags[tag] = tags.setdefault(tag, 0) + 1

tags_sorted = sorted(tags.items(), key=lambda x: x[1], reverse=True)
fw = open('ide_tags_sort.txt', 'w', encoding='utf-8')
for tag in tags_sorted:
    if tag[0] != 'ide':
        fw.write(tag[0] + '; ' + str(tag[1]) + '\n')
fw.close()
temp = tags_sorted.copy()
for i in temp:
    if i[0] == 'ide':
        temp.remove(i)
        break
tags_order = temp[:10]
my_tags = ['eclipse', 'python', 'visual-studio', 'php', 'netbeans']
res = []
'''
for tag in tags_order:
    for item in ide_que:
        if item['tags'][0] == tag[0]:
            res.append({tag[0]: myReplace(item['title'])})
'''
num = 0
for tag in my_tags:
    for item in ide_que:
        if item['tags'][0] == tag:
        # if tag in item['tags']:
            res.append({tag: myReplace(item['title'])})
            num += 1
print(num)

fw = open('ide_questions.json', 'w', encoding='utf-8')
fw.write(json.dumps(res, indent=4, ensure_ascii=False))
fw.close()

# tags_order = tags_sorted[1:11]
fw = open('ide_ques.txt', 'w', encoding='utf-8')
for item in ide_que:
    fw.write(myReplace(item['title']) + '\n')
fw.close()
