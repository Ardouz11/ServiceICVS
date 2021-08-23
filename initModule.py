# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:07:20 2021

@author: G525459
"""
import pandas as pd
import sortingList 
from configparser import ConfigParser
import listToSublists
#Instantiation of ConfigParser
config=ConfigParser()
def init():
    df=pd.read_csv("./Datasets/national_names.csv")
    list_sorted=sortingList.dataFrameToList(df)
    #set the size of sharding
    size=config['tresholds']['size_of_sharding']
    #List into sublists
    lists=listToSublists.shardingList(list_sorted, size)
    return lists
def initConfig():
    #---------------------------------------------- Variables Globales------------------------------
    #set default treshold 
    #Read configuration file
    config.read('config.ini')
    #set the treshold to default defined in config file
    jarowinkler_treshold=config['tresholds']['jarowinkler_default']
    return jarowinkler_treshold
def configTesseractPath():
    #---------------------------------------------- Variables Globales------------------------------
    #set default treshold 
    #Read configuration file
    config.read('config.ini')
    #set the treshold to default defined in config file
    tesseractPath=config['tresholds']['tesseractPath']
    return tesseractPath

    