# -*- coding: utf-8 -*-
"""
Created on Mon May 17 14:18:12 2021

@author: G525459
"""
import initModule
from strsimpy.jaro_winkler import JaroWinkler
#--------------------------------- Initialisation --------------------------
#set the treshold to default
default_treshold=initModule.initConfig()
#--------------------------------------------- Finding Similarities in list -----------------------------
#Function that finds similarities between a word and other words in list 
#it takes an optional argument treshold 
def findSimilaritiesInShardedList(w,l,treshold=float(default_treshold)):
    #List of similarities 
    similarities_in_shardedlist=[]
    #Instantiation of JaroWinkler Algorithme
    jarowinkler = JaroWinkler()
    for word in l:
        #Calculate similarity and comparing it with the treshold
        if jarowinkler.similarity(w, word.lower())>=treshold: 
            similarities_in_shardedlist.append(word)
    return similarities_in_shardedlist
#------------------------------------ Searching Algorithm -------------------------
def findShardedList(arr, left, right, x):
    # Check if the right of the list is bigger than the left
    if right >= left:
        #calculate middle of the list
        mid = left + (right - left) // 2
        # Check if the word is in range of the middle sublist
        if arr[mid][0].lower()<= x and arr[mid][-1].lower()>=x: 
            return mid
        # if the last word in the middle sublist is bigger than the word 
        # then we will check the left sublists
        elif arr[mid][-1].lower() > x:
            return findShardedList(arr, left, mid-1, x)
        # check the right sublists
        else:
            return findShardedList(arr, mid + 1, right, x)
    else:
        # Element is not present in the list
        return -1
#-------------------------- Find Similarities in lists --------------------
def findSimilarities(word,treshold=float(default_treshold)):
    list_of_similarities=[]
    #list that contains the sublists
    lists=initModule.init()
    #get the index of the sublist
    index_of_shardedlist=findShardedList(lists, 0, len(lists),word)
    #find the similarities in the sublist
    #check if the index is valid 
    if index_of_shardedlist!=-1:
        list_of_similarities=findSimilaritiesInShardedList(word,lists[index_of_shardedlist],treshold)
        return list_of_similarities
    #return empty list
    else:
        return []

    