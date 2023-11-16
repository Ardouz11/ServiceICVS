# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:00:55 2021

@author: Ardouz11
"""
import cleanWords as clean
def data_frame_to_list(df):
    """Read dataframe from csv file #add to another module """
    #Removing punctuation from names
    df["name"]=df["name"].apply(clean.remove_punctuation)
    #Convert dataframe to list #add to tools module
    list_=df["name"].tolist()
    #Sort list after removing duplication names 
    list_sorted=sorted(list(set(list_)))
    return list_sorted