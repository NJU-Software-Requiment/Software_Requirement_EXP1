# -*- coding: utf-8 -*-
"""
Created on Sun Nov  1 19:01:56 2020

@author: ZQY
"""
import pandas as pd
import re

def clean_name(name):
    rst=re.split('-',name)
    return rst[0]

tag_dict={}
df=pd.read_csv('issues.csv')
title_tag=df.loc[:,['title','labels']]
for i in range (10000):
    if title_tag.loc[i,'labels']!='[]':
        tmp_tag=title_tag.loc[i,'labels']
        tmp_tag=tmp_tag[1:-1]
        dict_tuple=eval(tmp_tag)
        
        if type(dict_tuple)==type(()):
            len_dict=len(dict_tuple)
            for j in range (len_dict):
                tmp_name=dict_tuple[j]['name']
                #tmp_name=clean_name(tmp_name)
                last_value=tag_dict.get(tmp_name)
                if last_value==None:
                    tag_dict[tmp_name]=1
                else:
                    tag_dict[tmp_name]=last_value+1
            
        if type(dict_tuple)==type({}):
            tmp_name=dict_tuple['name']
            #tmp_name=clean_name(tmp_name)
            last_value=tag_dict.get(tmp_name)
            if last_value==None:
                tag_dict[tmp_name]=1
            else:
                tag_dict[tmp_name]=last_value+1
        
            
          
            
            
        

with open("tag.txt","w",encoding='utf-8') as f:
    for key,value in tag_dict.items() :
        if value>=10:
            f.write(str(key)+';'+str(value)+'\n')

