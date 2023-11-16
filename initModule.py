# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 09:07:20 2021

@author: Ardouz11
"""
from configparser import ConfigParser
import pandas as pd
import sortingList 
import listToSublists
#Instantiation of ConfigParser
config=ConfigParser()
def init():
    """Function of initilialization"""
    df=pd.read_csv("./Datasets/national_names.csv")
    list_sorted=sortingList.dataFrameToList(df)
    #set the size of sharding
    size=config['tresholds']['size_of_sharding']
    #List into sublists
    lists=listToSublists.shardingList(list_sorted, size)
    return lists
def init_config():
    """Function that inits config"""
    #---------------------------------------------- Variables Globales------------------------------
    #set default treshold 
    #Read configuration file
    config.read('config.ini')
    #set the treshold to default defined in config file
    jarowinkler_treshold=config['tresholds']['jarowinkler_default']
    return jarowinkler_treshold
def config_tesseract_path():
    """Function that initilize global variables"""
    #---------------------------------------------- Variables Globales------------------------------
    #set default treshold 
    #Read configuration file
    config.read('config.ini')
    #set the treshold to default defined in config file
    tesseract_path=config['tresholds']['tesseractPath']
    return tesseract_path

    