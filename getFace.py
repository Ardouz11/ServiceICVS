# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 08:53:57 2021

@author: G525459
"""
import cv2
import numpy as np
faceNet = cv2.dnn.readNet("face_detector/deploy.prototxt", "face_detector/res10_300x300_ssd_iter_140000.caffemodel")

def getFace(filepath):
    image = cv2.imread(filepath)
    (h,w) = image.shape[:2]
    blob = cv2.dnn.blobFromImage(image, scalefactor=1.1, size=(300, 300), mean=(104.0, 177.0, 123.0))
    faceNet.setInput(blob)
    detections = faceNet.forward()
    counter=1
    for i in range(0, detections.shape[2]):
	
	# prediction
        confidence = detections[0, 0, i, 2]
	# filter out weak detections by ensuring the confidence is
	# greater than the minimum confidence
        if confidence > 0.5:
		# compute the (x, y)-coordinates of the bounding box for the
		# object
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
        
            (startX, startY, endX, endY) = box.astype("int")
		# extract the ROI of the face and then construct a blob from
		# *only* the face ROI
            face = image[startY:endY, startX:endX]
            faceBlob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), (78.4263377603, 87.7689143744, 114.895847746), swapRB=False)
            y = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.rectangle(image, (startX-20, startY-20), (endX+20, endY),(0, 0, 125), 2)
            crop_face = image[startY-20: endY, startX-20: endX+20 ]
            cv2.imwrite("Output/SavedFaces/face"+str(counter)+".jpg", crop_face)
            counter=counter+1
            return crop_face