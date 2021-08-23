# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 08:46:51 2021

@author: G525459
"""
#------------------------------------------ List into Sublists -----------------------------
#Function that shards list into sublist 
def shardingList(li,size):
    li = [li[x:x+int(size)] for x in range(0, len(li), int(size))]
    return li