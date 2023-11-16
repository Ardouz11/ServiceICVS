# -*- coding: utf-8 -*-
"""
Created on Wed Aug 11 10:44:00 2021

@author: Ardouz11
"""

import image_preprocessing as preprocessing
import json
import cv2 
import pytesseract as tess
import initModule
tesseractPath=initModule.initConfig()
tess.pytesseract.tesseract_cmd=r"tesseract installation path"
import re
# Our custom config
CUSTOMCONFIG = R'-L ENG --OEM 3 --PSM 6 '
#-c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789>< -c load_system_dawg=F -c load_freq_dawg=F
# reading the image in the first place 
def get_text(filename):
    """Function that gets text from image"""
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
    text_of_img=tess.image_to_string(thresh, config=CUSTOMCONFIG)
# clean the text
    text_of_img_clean=re.sub('[^a-zA-Z0-9\<\/\s]','',text_of_img)
    text_of_img_clean=text_of_img_clean.replace('\n',' ')
    text_of_img_clean=text_of_img_clean.strip()
    return str(text_of_img_clean)