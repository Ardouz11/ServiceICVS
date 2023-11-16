# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:36:24 2021

@author: Ardouz11
"""

def features(name):
    """ Function that exracts caracters from a given name in a dictionnary """
    name = name.lower()
    return {
        'first-letter': name[0], # First letter
        'first2-letters': name[0:2], # First 2 letters
        'first3-letters': name[0:3], # First 3 letters
        'last-letter': name[-1], #last letter
        'last2-letters': name[-2:],
        'last3-letters': name[-3:],
    }