import requests as rq
import json
import time
import pickle


tags = {}
all_json = []
remain = 0
for i in range(101):
    url = f'https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&tagged=ide&page={i + 1}&pagesize=100&site=stackoverflow&' + \
        'filter=!)5IW-1CBLPxKYw2x*xmfiaebgSti&' + \
        'key=602UeLTB17TQ0y7WP3t*)w(('
    r = rq.get(url)
    # time.sleep(0.01)
    r_json = r.json()
    print('page:', i + 1, 'len:', len(r_json["items"]))
    all_json.extend(r_json["items"])
    remain = r_json["quota_remaining"]

fw = open('ide_questions', 'wb')
pickle.dump(all_json, fw)
print(remain)
