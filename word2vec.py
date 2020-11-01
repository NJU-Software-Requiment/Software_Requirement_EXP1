import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

def train():
    inp='ide_ques.txt'
    outp1='test.model'
    outp2 = 'test.vector'

    model = Word2Vec(LineSentence(inp), size=200, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())

    model.save(outp1)
    model.wv.save_word2vec_format(outp2, binary=False)


train()
en_wiki_word2vec_model = Word2Vec.load('test.model')

testwords = ['debug', 'editor', 'console', 'code']
for i in range(len(testwords)):
    res = en_wiki_word2vec_model.most_similar(testwords[i],topn=10)
    print(testwords[i])
    print(res)