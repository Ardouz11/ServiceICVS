# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:01:44 2021

@author: G525459
"""

import re 
#------------------------------------------ Clean Function----------------------------------
#Function that removes punctuation from words
def removePunctuation(word):
    return re.sub(r'[^\w]', '', word)
#----------------------------------- Function that cleans the names ----------------------
def clean(word):
    return re.sub('[^a-zA-Z]','',word)