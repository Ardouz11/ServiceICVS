# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:01:44 2021

@author: Ardouz11
"""

import re 
def remove_punctuation(word)->str:
    """Function that removes punctuation"""
    return re.sub(r'[^\w]', '', word)
def clean(word)->str:
    """Function that cleans the names"""
    return re.sub('[^a-zA-Z]','',word)