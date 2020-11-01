import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence
file_name='vscode_issues_title'
inp='data/'+file_name+'.txt'
outp1='Model/'+file_name+'.model'
def train():
    #outp2 = 'Model/test.vector'
    model = Word2Vec(LineSentence(inp), size=200, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())
    model.save(outp1)
    #model.wv.save_word2vec_format(outp2, binary=False)


train()
model = Word2Vec.load(outp1)

testwords = ['debug', 'editor', 'console', 'code']
for i in range(len(testwords)):
    res = model.most_similar(testwords[i],topn=10)
    print(testwords[i])
    print(res)