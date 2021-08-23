# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:44:00 2021

@author: G525459
"""

import cv2 
import json
import pytesseract as tess
import initModule
tesseractPath=initModule.initConfig()
tess.pytesseract.tesseract_cmd=r"C:\Users\g525459\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
import re
import image_preprocessing as preprocessing
# Our custom config
custom_config = r'-l eng --oem 3 --psm 6 '
#-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789>< -c load_system_dawg=F -c load_freq_dawg=F
# reading the image in the first place 
def getText(filename):
    img = cv2.imread(str(filename))
    prctg_width=560/img.shape[1]
    prctg_height=790/img.shape[0]
#reshape of the image
    img = cv2.resize(img, (int(img.shape[0]*prctg_height),int(img.shape[1]*prctg_width)),fx=2,fy=2,interpolation = cv2.INTER_CUBIC)


# Transform the image to Gray
    gray = preprocessing.get_grayscale(img)
# Tresholding to convert the picture in black and white
    thresh= preprocessing.thresholding(gray)[1]
# Getting the text from the image
    Text_of_img=tess.image_to_string(thresh, config=custom_config)
    Text_of_img1=Text_of_img.split('\n')
# clean the text
    Text_of_img_clean=re.sub('[^a-zA-Z0-9\<\/\s]','',Text_of_img)
    Text_of_img_clean=Text_of_img_clean.replace('\n',' ')
    Text_of_img_clean=Text_of_img_clean.strip()
    return str(Text_of_img_clean)