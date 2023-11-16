# -*- coding: utf-8 -*-
"""
Created on Wed May 19 14:14:56 2021

@author: G525459
"""
import initPrediction
RETURNFEMALE="FEMALE"
RETURNMALE="MALE"
def genderpredictor_tree(a)->str:
    """Function that predict the gender"""
    #String to array
    test_name_tree = [a]
    #vectorize array using features
    vector_tree = initPrediction.dv_dtree.transform(initPrediction.features(test_name_tree)).toarray()
    #predict the gender (1 for female and 0 for male this is defined in the training part)
    #df_m.sex=[0 if each=="M" else 1 for each in df_m.sex])
    if initPrediction.loaded_dtree_model.predict(vector_tree) == 1:
        return RETURNFEMALE
    else:
        return RETURNMALE
