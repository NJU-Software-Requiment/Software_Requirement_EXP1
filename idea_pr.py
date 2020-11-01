import requests as rq
import pandas as pd
import json
import time
import pickle

url = 'https://api.github.com/repos/JetBrains/intellij-community/pulls?state=all&per_page=100&page='
header = {'Authorization': 'token 01c4fbe3ebbc9a4c88452ab17a00a0269df7a11d'}
res = []
for i in range(100):
    print('page ' + str(i + 1))
    r = rq.get(url + str(i + 1), headers=header)
    # r = rq.get(url + str(i + 1))
    r_json = r.json()
    res.extend(r_json)
print('ok')

fw = open('idea_pr', 'wb')
pickle.dump(res, fw)
fw.close()

fw = open('idea_pr_title.txt', 'w', encoding='utf-8')
for pr in res:
    fw.write(pr['title'] + '\n')
fw.close()


fr = open('idea_pr', 'rb')
all_pr = pickle.load(fr)
fr.close()


fw = open('idea_pr.json', 'w', encoding='utf-8')
json.dump(all_pr, fw, indent=4, ensure_ascii=False)
fw.close()
res = {}
for pr in all_pr:
    if len(pr['labels']) > 0:
        for label in pr['labels']:
            res[label['name']] = res.setdefault(label['name'], 0) + 1
fw = open('idea_pr_labels.txt', 'w', encoding='utf-8')
label_sort = sorted(res.items(), key=lambda x: x[1], reverse=True)
for lab in label_sort:
    fw.write(lab[0] + '; ' + str(lab[1]) + '\n')
fw.close()
