# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 08:46:51 2021

@author: Ardouz11
"""
#------------------------------------------ List into Sublists -----------------------------
def sharding_list(li,size):
    """Function that shards list into sublist """
    li = [li[x:x+int(size)] for x in range(0, len(li), int(size))]
    return li