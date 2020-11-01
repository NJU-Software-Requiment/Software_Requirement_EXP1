import logging
import os
import sys
import multiprocessing

from gensim.models import Word2Vec
from gensim.models.word2vec import LineSentence

file_names=['ide_ques','vscode_issues_title','vscode_pr_title','idea_pr_title']
def train(inp,outp):
    #outp2 = 'Model/test.vector'
    model = Word2Vec(LineSentence(inp), size=200, window=5, min_count=5,
                     workers=multiprocessing.cpu_count())
    model.save(outp)
    #model.wv.save_word2vec_format(outp2, binary=False)

#retrain=True
retrain=False
if retrain==True:
    for i in file_names:
        inp = 'data/' + i + '.txt'
        outp1 = 'Model/' + i + '.model'
        print("training: ",outp1)
        train(inp,outp1)

def test(model):
    model = Word2Vec.load("Model/"+model)

    testwords = ['debug', 'editor', 'console', 'code']
    for i in range(len(testwords)):
        res = model.most_similar(testwords[i],topn=10)
        print(testwords[i])
        print(res)

test('ide_ques.model')