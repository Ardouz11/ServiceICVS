 -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:02:10 2021

@author: G525459
"""
import pandas as pd
import re
def removePunctuation(word):
    return re.sub(r'[^\w\s]', '', word)
def clean(word):
    return re.sub('[^a-zA-Z]','',word)
df=pd.read_csv("../Datasets/national_names.csv")
df.sort_values('name')
df_m=df.drop(["year","count"],axis=1)
df_m["name"]=df_m["name"].apply(removePunctuation)
list_=df_m["name"].tolist()
list_=sorted(list_)
textfile = open("output_list.txt", "w")
for element in list_:
    textfile.write(element + "\n")
textfile.close()