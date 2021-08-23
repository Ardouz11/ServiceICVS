# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:00:55 2021

@author: G525459
"""
import cleanWords as clean
#Read dataframe from csv file #add to another module 
def dataFrameToList(df):
    #Removing punctuation from names
    df["name"]=df["name"].apply(clean.removePunctuation)
    #Convert dataframe to list #add to tools module
    list_=df["name"].tolist()
    #Sort list after removing duplication names 
    list_sorted=sorted(list(set(list_)))
    return list_sorted