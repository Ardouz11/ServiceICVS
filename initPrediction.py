# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 10:37:24 2021

@author: G525459
"""
import pandas as pd
import joblib
import numpy as np
import cleanWords
import extractFeatures
from sklearn.feature_extraction import DictVectorizer
#------------------------------------------ Load Saved Model -----------------------------
loaded_dtree_model = joblib.load('dtree_model.sav')
#---------------------- Convert dictionnary to numpy array ---------------------------------
features = np.vectorize(extractFeatures.features)
#----------------------------- To initialize the dictVectorizer  ------------------
df_m=pd.read_csv("../Datasets/national_names_shuf.csv")[0:480000]
#------------------------------------------- Clean dataset -------------------------------
df_m["name"]=df_m["name"].apply(cleanWords.clean)
#------------------------------------ Extract Features from dataset --------------------
X_train_features_dtree = features(df_m['name'])
#----------------------------------- Initiate the dictVectorizer that vectorizes dictionnary --------------
dv_dtree = DictVectorizer()
dv_dtree.fit_transform(X_train_features_dtree)