import requests as rq
import pandas as pd
import json
import time

url = 'https://api.github.com/repos/microsoft/vscode/issues?state=all&per_page=100&page='
header = {'Authorization': 'token 01c4fbe3ebbc9a4c88452ab17a00a0269df7a11d'}
res = []
for i in range(100):
    print('page ' + str(i + 1), end=' ')
    begin = time.time()
    r = rq.get(url + str(i + 1), headers=header)
    # r = rq.get(url + str(i + 1))
    print(time.time() - begin)
    r_json = r.json()
    r_content = r.content
    res.extend(r_json)
print('ok')
fw = open('issues.json', 'w', encoding='utf-8')
fw.write(json.dumps(res))

df = pd.read_json('issues.json', orient='records')
df.to_csv('issues.csv', encoding='utf-8-sig')
