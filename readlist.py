# -*- coding: utf-8 -*-
"""
Created on Wed May 19 11:05:19 2021

@author: G525459
"""

with open("output_list.txt") as file:
    lines = [line.strip() for line in file]
print(lines[0:2])