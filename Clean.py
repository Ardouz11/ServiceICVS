# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:02:10 2021

@author: Ardouz11
"""
import re
import pandas as pd
def remove_punctuation(word)->str:
    """Function that removes punctuation"""
    return re.sub(r'[^\w\s]', '', word)
def clean(word)->str:
    """Function that cleans the names"""
    return re.sub('[^a-zA-Z]','',word)
df=pd.read_csv("./Datasets/national_names.csv")
df.sort_values('name')
df_m=df.drop(["year","count"],axis=1)
df_m["name"]=df_m["name"].apply(remove_punctuation)
list_=df_m["name"].tolist()
list_=sorted(list_)
textfile = open("output_list.txt", "w")
for element in list_:
    textfile.write(element + "\n")
textfile.close()