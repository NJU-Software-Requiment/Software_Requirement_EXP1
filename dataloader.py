import json
import json
from transformers import BertTokenizer
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import torch.autograd as autograd
import torch.nn.functional
from torch.utils.data import Dataset, DataLoader
import random
import numpy as np
def setup_seed(seed):
     torch.manual_seed(seed)
     torch.cuda.manual_seed_all(seed)
     np.random.seed(seed)
     random.seed(seed)

setup_seed(44)
path="questions.json"


def load_train(datalines):
    rel2id,id2rel=map_id_rel()
    max_length=128
    tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
    train_data = {}
    train_data['label'] = []
    train_data['mask'] = []
    train_data['text'] = []
    print(len(datalines))
    for line in datalines:
        for j in line:
            if j not in rel2id:
                train_data['label'].append(0)
            else:
                train_data['label'].append(rel2id[j])
            sent=line[j]
            indexed_tokens = tokenizer.encode(sent, add_special_tokens=True)
            avai_len = len(indexed_tokens)
            while len(indexed_tokens) <  max_length:
                indexed_tokens.append(0)  # 0 is id for [PAD]
            indexed_tokens = indexed_tokens[: max_length]
            indexed_tokens = torch.tensor(indexed_tokens).long().unsqueeze(0)  # (1, L)

            # Attention mask
            att_mask = torch.zeros(indexed_tokens.size()).long()  # (1, L)
            att_mask[0, :avai_len] = 1
            train_data['text'].append(indexed_tokens)
            train_data['mask'].append(att_mask)
    return train_data

def load_dev(datalines):
    rel2id,id2rel=map_id_rel()
    max_length=128
    tokenizer = BertTokenizer.from_pretrained('bert-base-cased')
    train_data = {}
    train_data['label'] = []
    train_data['mask'] = []
    train_data['text'] = []
    for line in datalines:
        for j in line:
            if j not in rel2id:
                train_data['label'].append(0)
            else:
                train_data['label'].append(rel2id[j])
            sent=line[j]
            indexed_tokens = tokenizer.encode(sent, add_special_tokens=True)
            avai_len = len(indexed_tokens)
            while len(indexed_tokens) <  max_length:
                indexed_tokens.append(0)  # 0 is id for [PAD]
            indexed_tokens = indexed_tokens[: max_length]
            indexed_tokens = torch.tensor(indexed_tokens).long().unsqueeze(0)  # (1, L)

            # Attention mask
            att_mask = torch.zeros(indexed_tokens.size()).long()  # (1, L)
            att_mask[0, :avai_len] = 1
            train_data['text'].append(indexed_tokens)
            train_data['mask'].append(att_mask)
    return train_data

def loader(path):
    f=open(path,'r',encoding='utf-8')
    labels=[]
    result=json.load(f)
    for i in result:
        for j in i:
            labels.append(j)
    random.shuffle(result)
    all=len(result)
    train=result[:int(all*0.9)]
    dev=result[int(all*0.9):]

    train=load_train(train)
    dev=load_dev(dev)
    return  train,dev




def map_id_rel():
    id2rel={0: 'UNK', 1: 'python', 2: 'javascript', 3: 'php', 4: 'intellij-idea', 5: 'netbeans', 6: 'visual-studio', 7: 'eclipse', 8: 'c++', 9: 'java', 10: 'android'}
    rel2id={}
    for i in id2rel:
        rel2id[id2rel[i]]=i
    return rel2id,id2rel
